#!/usr/bin/env python3
"""
Sony Camera MCP Server.
Talks PTP-IP directly over SSH tunnel — no Sony SDK dependency.
Works with any Sony camera that supports PC Remote (α6700, α7 series, etc).

Setup: the AI will walk you through it via the setup_guide tool, or provide
env vars / config file with camera IP and SSH credentials.
"""

import base64
import json
import logging
import os
import socket
import struct
import sys
import time
import urllib.request
from pathlib import Path

from mcp.server.mcpserver import MCPServer

sys.path.insert(0, str(Path(__file__).parent))
from ptpip import PTPIPConnection, PTPIPError, SonyOpcode
from property_map import CRSDK_TO_WIRE, WIRE_TO_CRSDK, PROPERTY_NAMES as ALL_PROPERTY_NAMES, WIRE_PROPERTY_NAMES

log = logging.getLogger("sony-camera-mcp")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

CONFIG_DIR = Path(os.environ.get("SONY_MCP_CONFIG", Path.home() / ".config" / "sony-camera-mcp"))
CONFIG_FILE = CONFIG_DIR / "config.json"


def _load_config() -> dict:
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except Exception:
            pass
    return {}


def _save_config(cfg: dict):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
    os.chmod(CONFIG_FILE, 0o600)


def _get_setting(key: str, default: str = "") -> str:
    env_key = f"SONY_CAMERA_{key.upper()}"
    env_val = os.environ.get(env_key, "")
    if env_val:
        return env_val
    cfg = _load_config()
    return cfg.get(key, default)


COMMON_PROPERTIES = {
    "fnumber": 0x0100, "exposure_bias": 0x0101, "shutter_speed": 0x0103,
    "iso": 0x0104, "exposure_mode": 0x0105, "white_balance": 0x0108,
    "focus_mode": 0x0109, "metering_mode": 0x010A, "flash_mode": 0x010B,
    "drive_mode": 0x010C, "image_size": 0x010E, "aspect_ratio": 0x010F,
    "focus_area": 0x0115, "battery_level": 0x0300, "recording_state": 0x0320,
}

CONTROL_CODES = {
    "s1_button": 0xD2C1, "s2_button": 0xD2C2,
    "ael_button": 0xD2C3, "afl_button": 0xD2C4,
    "request_one_shooting": 0xD2C7,
    "movie_record": 0xD2C8, "fel_button": 0xD2C9,
    "remote_key_up": 0xD2CD, "remote_key_down": 0xD2CE,
    "remote_key_left": 0xD2CF, "remote_key_right": 0xD2D0,
    "near_far": 0xD2D1, "af_mf_hold": 0xD2D2,
    "cancel_pixel_shift": 0xD2D3, "pixel_shift_mode": 0xD2D4,
    "hfr_standby": 0xD2D5, "hfr_recording_cancel": 0xD2D6,
    "focus_step_near": 0xD2D7, "focus_step_far": 0xD2D8,
    "awbl_button": 0xD2D9, "program_shift": 0xD2DA,
    "wb_initialization": 0xD2DB,
    "af_area_position": 0xD2DC, "zoom": 0xD2DD,
    "custom_wb_capture_standby": 0xD2DF,
    "custom_wb_capture": 0xD2E1, "media_format": 0xD2E2,
    "high_res_ss_adjust": 0xD2E3,
    "remote_touch": 0xD2E4, "cancel_remote_touch": 0xD2E5,
    "s1_and_s2": 0xD2E6, "wifi_power_off": 0xD2E8,
    "aps_c_or_full": 0xD2EB, "focus_operation": 0xD2EF,
    "high_res_ss_adjust_integral": 0xD2F0,
    "flicker_scan": 0xD2F1, "rec_settings_reset": 0xD2F3,
    "cont_shoot_spot_boost": 0xD2F6,
    "remote_key_cancel": 0xD2F7, "remote_key_display": 0xD2F8,
    "remote_key_set": 0xD2F9, "remote_key_menu": 0xD2FF,
    "pixel_mapping": 0xD300, "power_off": 0xD301,
    "stream_button": 0xD307, "wifi_direct_off": 0xD308,
    "camera_button": 0xD309, "camera_dial": 0xD30B,
    "set_select_on_camera_transfer": 0xD30F,
    "set_select_on_camera_transfer_mode": 0xD310,
    "cancel_select_on_camera_transfer": 0xD311,
    "set_post_view_enable": 0xD312,
    "set_live_view_enable": 0xD313,
    "camera_standby": 0xD315, "power_on": 0xD316,
    "release": 0x10001, "cancel_focus_position": 0xF002,
}

DANGEROUS_CONTROLS = {"media_format", "rec_settings_reset", "power_off", "pixel_mapping"}

U8_CONTROLS = {"program_shift", "high_res_ss_adjust", "high_res_ss_adjust_integral"}
U32_CONTROLS = {"af_area_position", "zoom", "remote_touch", "camera_dial"}
NO_DATA_CONTROLS = {
    "wb_initialization", "custom_wb_capture_standby", "custom_wb_capture",
    "cancel_remote_touch", "wifi_power_off", "flicker_scan",
    "cont_shoot_spot_boost", "wifi_direct_off",
    "set_select_on_camera_transfer", "set_select_on_camera_transfer_mode",
    "cancel_select_on_camera_transfer", "set_post_view_enable",
    "set_live_view_enable", "cancel_focus_position",
}

conn: PTPIPConnection = None
events: list = []
MAX_EVENTS = 100

mcp = MCPServer("sony-camera")


def ensure_connected():
    global conn
    if conn is not None:
        return
    ip = _get_setting("ip")
    ssh_user = _get_setting("ssh_user")
    ssh_pass = _get_setting("ssh_pass")
    if not ip or not ssh_user:
        raise PTPIPError(
            "Camera not configured. Use the setup_guide tool to get started, "
            "or call camera_connect with ip, ssh_user, and ssh_pass.")
    port = int(_get_setting("port", "15740"))
    ssh_port = int(_get_setting("ssh_port", "22"))
    c = PTPIPConnection(ip, port, ssh_user=ssh_user, ssh_pass=ssh_pass, ssh_port=ssh_port)
    c.set_event_callback(on_event)
    c.connect()
    conn = c


def on_event(event_code, tid, params):
    entry = {"code": f"0x{event_code:04x}", "tid": tid,
             "params": [f"0x{p:08x}" for p in params], "time": time.time()}
    events.append(entry)
    if len(events) > MAX_EVENTS:
        events.pop(0)


def resolve_property(name: str) -> int:
    name = name.strip()
    if name.startswith("0x") or name.startswith("0X"):
        code = int(name, 16)
        if code in WIRE_TO_CRSDK:
            return code
        if code in CRSDK_TO_WIRE:
            return CRSDK_TO_WIRE[code]
        return code
    low = name.lower()
    if low in COMMON_PROPERTIES:
        return CRSDK_TO_WIRE[COMMON_PROPERTIES[low]]
    for crsdk_code, pname in ALL_PROPERTY_NAMES.items():
        if pname.lower() == low:
            return CRSDK_TO_WIRE.get(crsdk_code, crsdk_code)
    for wire_code, pname in WIRE_PROPERTY_NAMES.items():
        if pname.lower() == low:
            return wire_code
    raise ValueError(f"Unknown property: {name}")


@mcp.tool(description=(
    "Get setup instructions for connecting to a Sony camera. "
    "Returns step-by-step guide for finding the camera's IP and SSH credentials. "
    "Call this first if the camera isn't configured yet."))
def setup_guide() -> str:
    cfg = _load_config()
    configured = bool(cfg.get("ip") and cfg.get("ssh_user"))

    guide = """# Sony Camera MCP Setup Guide

## What you need from the camera

This server connects to Sony cameras over WiFi using an SSH tunnel.
You need three things from the camera:

### 1. Camera IP Address
The camera must be on the same WiFi network as this computer.

**On the camera:**
- Go to Network → Wi-Fi → Wi-Fi Connect (not Wi-Fi Direct)
- Connect the camera to your home/office WiFi network
- The camera's IP is shown in Wi-Fi settings, or check your router's DHCP list
- It will look like: 192.168.1.xxx or 10.0.0.xxx

**Or scan the network:**
- Use the `discover_camera` tool to scan via SSDP
- Or check your router's DHCP client list for the camera

### 2. SSH Credentials (User & Password)
The camera has built-in SSH access with auto-generated credentials.

**On the camera:**
- Go to Network → PC Remote Function → Access Authentication Info
- You'll see:
  - **User**: a short random string (e.g. "xK9mPw")
  - **Password**: a longer random string (e.g. "aB3dEfGh")

### 3. Connect
Once you have the IP and credentials, call:
```
camera_connect(ip="<camera_ip>", ssh_user="<user>", ssh_pass="<password>")
```

The connection will be saved so you don't need to enter it again.

## Tested on
- Sony α6700 (ILCE-6700)

Should work with any Sony camera that has PC Remote over WiFi (α7 series, α9, ZV, FX, etc)
but only the α6700 has been verified.

## Environment variables (alternative to setup)
```
SONY_CAMERA_IP=192.168.1.xxx
SONY_CAMERA_SSH_USER=xxxxx
SONY_CAMERA_SSH_PASS=xxxxx
SONY_CAMERA_PORT=15740      # optional, default 15740
SONY_CAMERA_SSH_PORT=22      # optional, default 22
```
"""
    if configured:
        guide += f"\n## Current config\n- IP: {cfg.get('ip')}\n- SSH User: {cfg.get('ssh_user')}\n- Config: {CONFIG_FILE}\n"
    else:
        guide += "\n## Status: Not configured yet\nAsk the user for the camera IP and SSH credentials, then call camera_connect.\n"

    return guide


@mcp.tool(description="Discover Sony cameras on the network via SSDP and SSH port scan.")
def discover_camera(timeout: float = 3.0, subnet: str = "") -> str:
    SSDP_ADDR = "239.255.255.250"
    SSDP_PORT = 1900
    results = []
    for st in ["urn:schemas-sony-com:service:ScalarWebAPI:1", "upnp:rootdevice"]:
        msg = (
            f"M-SEARCH * HTTP/1.1\r\n"
            f"HOST: {SSDP_ADDR}:{SSDP_PORT}\r\n"
            f"MAN: \"ssdp:discover\"\r\n"
            f"MX: {int(timeout)}\r\n"
            f"ST: {st}\r\n\r\n"
        )
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.settimeout(timeout)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        sock.sendto(msg.encode(), (SSDP_ADDR, SSDP_PORT))
        try:
            while True:
                data, addr = sock.recvfrom(4096)
                text = data.decode(errors="replace").lower()
                if "sony" in text:
                    location = ""
                    for line in data.decode(errors="replace").split("\r\n"):
                        if line.lower().startswith("location:"):
                            location = line.split(":", 1)[1].strip()
                    results.append({"ip": addr[0], "port": addr[1], "location": location})
        except socket.timeout:
            pass
        sock.close()

    if not results and subnet:
        for last_octet in range(1, 255):
            ip = f"{subnet}.{last_octet}"
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.15)
                s.connect((ip, 22))
                s.close()
                results.append({"ip": ip, "port": 22, "note": "SSH open — could be a Sony camera"})
            except (OSError, socket.timeout):
                pass

    for r in results:
        if r.get("location"):
            try:
                resp = urllib.request.urlopen(r["location"], timeout=2)
                dd_xml = resp.read().decode(errors="replace")
                r["dd_xml_snippet"] = dd_xml[:500]
            except Exception as e:
                r["dd_xml_error"] = str(e)

    if not results:
        return (
            "No Sony cameras found on the network.\n\n"
            "Make sure the camera is:\n"
            "1. Powered on\n"
            "2. Connected to the same WiFi network (not Wi-Fi Direct)\n"
            "3. PC Remote function is enabled in Network settings\n\n"
            "You can also provide the camera IP directly if you know it — "
            "check the camera's Network settings or your router's DHCP list."
        )
    return json.dumps(results, indent=2)


@mcp.tool(description=(
    "Connect to a Sony camera. First time: provide ip, ssh_user, ssh_pass "
    "(from camera's Access Authentication Info). Credentials are saved for future sessions. "
    "Set save=False to connect without saving."))
def camera_connect(ip: str = "", ssh_user: str = "", ssh_pass: str = "",
                   port: int = 0, ssh_port: int = 0, save: bool = True) -> str:
    global conn
    cfg = _load_config()
    ip = ip or _get_setting("ip")
    ssh_user = ssh_user or _get_setting("ssh_user")
    ssh_pass = ssh_pass or _get_setting("ssh_pass")
    port = port or int(_get_setting("port", "15740"))
    ssh_port = ssh_port or int(_get_setting("ssh_port", "22"))

    if not ip:
        return ("No camera IP provided. Use setup_guide to learn how to find it, "
                "or pass ip='...' directly.")
    if not ssh_user or not ssh_pass:
        return ("SSH credentials required. On the camera, go to:\n"
                "Network → PC Remote Function → Access Authentication Info\n"
                "Then pass ssh_user='...' and ssh_pass='...'")

    if conn:
        conn.disconnect()
        conn = None

    c = PTPIPConnection(ip, port, ssh_user=ssh_user, ssh_pass=ssh_pass, ssh_port=ssh_port)
    c.set_event_callback(on_event)
    c.connect()
    conn = c

    if save:
        cfg.update({"ip": ip, "ssh_user": ssh_user, "ssh_pass": ssh_pass,
                     "port": str(port), "ssh_port": str(ssh_port)})
        _save_config(cfg)

    mode = "SSH tunnel" if c.use_ssh else "direct"
    msg = f"Connected to {ip}:{port} ({mode}), vendor=0x{conn.vendor_code:x}."
    if save:
        msg += f" Config saved to {CONFIG_FILE}."
    return msg


@mcp.tool(description="Disconnect from the camera")
def camera_disconnect() -> str:
    global conn
    if conn:
        conn.disconnect()
        conn = None
    return "Disconnected"


@mcp.tool(description="Check connection status and recent events")
def camera_status() -> str:
    cfg = _load_config()
    if not conn:
        if cfg.get("ip"):
            return json.dumps({
                "connected": False,
                "saved_config": {"ip": cfg["ip"], "ssh_user": cfg.get("ssh_user", "")},
                "hint": "Use camera_connect to reconnect with saved credentials."
            }, indent=2)
        return "Not connected. Use setup_guide to get started."
    recent = events[-10:] if events else []
    return json.dumps({
        "connected": True, "ip": conn.ip, "port": conn.port,
        "vendor_code": f"0x{conn.vendor_code:x}",
        "transaction_id": conn.transaction_id,
        "recent_events": recent
    }, indent=2)


@mcp.tool(description="Read camera properties. Pass names (iso, fnumber) or hex codes (0xD21E). No args = read all.")
def get_property(properties: list[str] = None) -> str:
    ensure_connected()
    if not properties:
        result = conn.get_properties()
        return f"All properties ({len(result)} bytes): {result[:200].hex()}{'...' if len(result) > 200 else ''}"
    codes = [resolve_property(p) for p in properties]
    result = conn.get_properties(*codes)
    return f"Raw response ({len(result)} bytes): {result.hex()}"


@mcp.tool(description="Set a camera property. code=hex or name, value=hex bytes (e.g. 'ffffff00' for ISO Auto)")
def set_property(code: str, value: str) -> str:
    ensure_connected()
    wire = resolve_property(code)
    data = bytes.fromhex(value)
    name = WIRE_PROPERTY_NAMES.get(wire, "")
    conn.set_property(wire, data)
    return f"Property 0x{wire:04X} ({name}) set"


@mcp.tool(description=(
    "Send a camera control command by name. "
    "Buttons (s1_button, s2_button, movie_record, etc): action='down'/'up'. "
    "Value controls (af_area_position, zoom, remote_touch, camera_dial): pass value as int. "
    "Example: send_command('s1_button', 'down') then send_command('s1_button', 'up') to autofocus."))
def send_command(command: str, action: str = "down", value: int = 0) -> str:
    ensure_connected()
    cmd = command.lower().strip()
    if cmd in DANGEROUS_CONTROLS:
        return f"BLOCKED: {cmd} is destructive. Use send_control_code if you really mean it."
    if cmd not in CONTROL_CODES:
        return f"Unknown command: {cmd}. Use list_commands to see available commands."
    control_code = CONTROL_CODES[cmd]
    if cmd in NO_DATA_CONTROLS:
        data = b""
    elif cmd in U8_CONTROLS:
        data = struct.pack("<B", value & 0xFF)
    elif cmd in U32_CONTROLS:
        data = struct.pack("<I", value)
    else:
        button_value = 1 if action == "down" else 0
        data = struct.pack("<H", button_value)
    conn.send_control_command(control_code, data)
    desc = f"0x{control_code:04x}"
    if cmd in U32_CONTROLS or cmd in U8_CONTROLS:
        desc += f", value={value}"
    else:
        desc += f", {action}"
    return f"Command {cmd} ({desc}) sent"


@mcp.tool(description="Take a photo. Sends S1 (autofocus), waits, sends S2 (shutter), releases both.")
def take_photo(af_time: float = 1.5) -> str:
    ensure_connected()
    conn.send_control_command(0xD2C1, struct.pack("<H", 1))
    time.sleep(af_time)
    conn.send_control_command(0xD2C2, struct.pack("<H", 1))
    time.sleep(0.3)
    conn.send_control_command(0xD2C2, struct.pack("<H", 0))
    conn.send_control_command(0xD2C1, struct.pack("<H", 0))
    return f"Photo taken (AF hold: {af_time}s)"


@mcp.tool(description="Send a raw Sony control code (hex) with optional hex data payload")
def send_control_code(code: str, data: str = "") -> str:
    ensure_connected()
    if code in CONTROL_CODES:
        c = CONTROL_CODES[code]
    else:
        c = int(code, 16)
    payload = bytes.fromhex(data) if data else b""
    conn.send_control_command(c, payload)
    return f"Control code 0x{c:04x} sent"


@mcp.tool(description="Grab one live-view JPEG frame from the camera and save it")
def get_live_view(output_path: str = "") -> str:
    ensure_connected()
    frame = conn.get_live_view()
    if not frame:
        return "No frame data received"
    jpeg_start = 0
    for i in range(min(len(frame), 1024)):
        if frame[i:i+2] == b"\xff\xd8":
            jpeg_start = i
            break
    jpeg_data = frame[jpeg_start:]
    out = Path(output_path) if output_path else Path("/tmp") / f"sony_lv_{int(time.time())}.jpg"
    out.write_bytes(jpeg_data)
    return f"Live view: {len(jpeg_data)} bytes saved to {out}"


@mcp.tool(description="Send a raw PTP-IP operation. opcode=hex, params=list of hex u32, data=optional hex payload")
def raw_ptp(opcode: str, params: list[str] = None, data: str = "") -> str:
    ensure_connected()
    op = int(opcode, 16)
    p = [int(x, 16) for x in (params or [])]
    if data:
        result = conn.send_data_command(op, p, bytes.fromhex(data))
    else:
        result = conn.send_command(op, p)
    return f"Response ({len(result)} bytes): {result.hex()}"


@mcp.tool(description="Capture a live-view JPEG and return as base64 for inline viewing")
def get_live_view_b64() -> str:
    ensure_connected()
    frame = conn.get_live_view()
    if not frame:
        return "No frame data received"
    jpeg_offset = 0
    for i in range(min(len(frame), 1024)):
        if frame[i:i+2] == b"\xff\xd8":
            jpeg_offset = i
            break
    b64 = base64.b64encode(frame[jpeg_offset:]).decode()
    return json.dumps({"size": len(frame), "jpeg_offset": jpeg_offset, "b64": b64})


@mcp.tool(description="Send keepalive probe on the event channel to prevent camera sleep")
def send_probe() -> str:
    ensure_connected()
    probe = struct.pack("<II", 8, 13)
    conn.evt_sock.sendall(probe)
    return "Probe sent"


@mcp.tool(description="List all available control commands with their codes")
def list_commands() -> str:
    lines = [f"  {k}: 0x{v:04x}" for k, v in sorted(CONTROL_CODES.items())]
    dangerous = ", ".join(sorted(DANGEROUS_CONTROLS))
    return f"Control Codes:\n" + "\n".join(lines) + f"\n\nDangerous (blocked in send_command): {dangerous}"


@mcp.tool(description="List known property codes and names. scope='common' for shortcuts, 'all' for all 810+.")
def list_properties(scope: str = "common") -> str:
    if scope == "all":
        lines = [f"Wire=0x{CRSDK_TO_WIRE[k]:04X} SDK=0x{k:04X} {v}"
                 for k, v in sorted(ALL_PROPERTY_NAMES.items()) if k in CRSDK_TO_WIRE]
        wire_only = [f"Wire=0x{k:04X} {v}" for k, v in sorted(WIRE_PROPERTY_NAMES.items())
                     if k not in WIRE_TO_CRSDK]
        return f"{len(lines) + len(wire_only)} properties:\n" + "\n".join(lines + wire_only)
    lines = [f"  {name}: SDK=0x{code:04X} Wire=0x{CRSDK_TO_WIRE[code]:04X}"
             for name, code in sorted(COMMON_PROPERTIES.items())]
    return "Common properties (use name, SDK code, or wire code):\n" + "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
