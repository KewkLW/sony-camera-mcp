# Sony Camera MCP Server

Control any Sony camera over WiFi — no SDK, no proprietary libraries. Talks PTP-IP directly through the camera's built-in SSH tunnel.

Tested on the Sony α6700 (ILCE-6700). Should work with any Sony camera that has PC Remote over WiFi (α7 series, α9, ZV, FX, etc) but only the α6700 has been verified.

## Install

```bash
pip install mcp paramiko
```

## Camera Setup

1. **Connect camera to WiFi**: Network → Wi-Fi → Wi-Fi Connect → join your home/office network
2. **Enable PC Remote**: Network → PC Remote Function → PC Remote → On
3. **Get SSH credentials**: Network → PC Remote Function → Access Authentication Info
   - Note the **User** and **Password** shown on screen

That's it. The AI will walk you through the rest when you use `setup_guide`.

## Quick Start

Add via CLI:

```bash
claude mcp add sony-camera -- python3 /path/to/sony-camera-mcp/server.py
```

Or add to `.mcp.json` in your project:

```json
{
  "mcpServers": {
    "sony-camera": {
      "command": "python3",
      "args": ["/path/to/sony-camera-mcp/server.py"]
    }
  }
}
```

Then tell the AI: *"Connect to my Sony camera"* — it will call `setup_guide` and walk you through entering your camera's IP and credentials. They're saved to `~/.config/sony-camera-mcp/config.json` for future sessions.

### Environment Variables (alternative)

```bash
SONY_CAMERA_IP=192.168.1.xxx
SONY_CAMERA_SSH_USER=xxxxx
SONY_CAMERA_SSH_PASS=xxxxx
```

## What Can It Do?

| Tool | What it does |
|------|-------------|
| `setup_guide` | Walk through finding camera IP and SSH credentials |
| `discover_camera` | Scan the network for Sony cameras via SSDP |
| `camera_connect` | Connect (saves credentials for next time) |
| `camera_status` | Connection info + recent camera events |
| `take_photo` | Autofocus + shutter, one call |
| `get_property` | Read settings: ISO, aperture, shutter speed, etc. |
| `set_property` | Change any camera setting |
| `send_command` | Shutter, movie record, menu nav, zoom, focus |
| `get_live_view` | Grab a JPEG frame from the viewfinder |
| `get_live_view_b64` | Same but base64 for inline display |
| `list_properties` | 810+ readable/writable properties |
| `list_commands` | 65+ control commands |
| `raw_ptp` | Send any PTP-IP operation directly |

## How It Works

Sony cameras expose an SSH server on port 22. PTP-IP (Picture Transfer Protocol over IP) runs on `localhost:15740` inside the camera — reachable only through an SSH `direct-tcpip` tunnel. This server:

1. Opens an SSH connection to the camera using the credentials from Access Authentication Info
2. Tunnels PTP-IP through `direct-tcpip` to `localhost:15740`
3. Runs the full Sony vendor PTP-IP handshake (SDIO_Connect, vendor code negotiation)
4. Exposes every camera function as MCP tools

No Sony SDK. No `libCr_Core.so`. No NDAs. Just standard protocols.

## Protocol Documentation

See `PROTOCOL.md` for the full PTP-IP protocol analysis — every opcode, property code, and control command reverse-engineered from Sony's Camera Remote SDK and Creators' App.

## Troubleshooting

**Camera not found**: Make sure camera and computer are on the same WiFi network. Camera must be in PC Remote mode, not Wi-Fi Direct (phone pairing) mode.

**Connection refused**: The camera's WiFi goes to sleep aggressively after errors. Power-cycle the camera's WiFi or restart it.

**SSH auth failed**: Double-check User and Password from Access Authentication Info. They're randomly generated per camera and don't change.

**Camera overheating**: Long sessions with live view can heat up the camera. Use `send_probe` for keepalive without live view, or disconnect between operations.
