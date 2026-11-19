"""
Sony PTP-IP transport layer.
Talks directly to the camera over TCP — no SDK dependency.
Supports both direct TCP and SSH-tunneled connections.
"""

import os
import socket
import struct
import uuid
import threading
import time
import logging
from enum import IntEnum
from typing import Optional

try:
    import paramiko
except ImportError:
    paramiko = None

log = logging.getLogger("ptpip")

PTPIP_PORT = 15740


class PacketType(IntEnum):
    INIT_CMD_REQ = 1
    INIT_CMD_ACK = 2
    INIT_EVENT_REQ = 3
    INIT_EVENT_ACK = 4
    INIT_FAIL = 5
    OPERATION_REQ = 6
    OPERATION_RESP = 7
    EVENT = 8
    START_DATA = 9
    DATA_PACKET = 10
    CANCEL = 11
    END_DATA = 12
    PROBE = 13
    PROBE_RESP = 14


class SonyOpcode(IntEnum):
    # Standard PTP
    GET_DEVICE_INFO = 0x1001
    OPEN_SESSION = 0x1002
    CLOSE_SESSION = 0x1003
    GET_STORAGE_IDS = 0x1004
    GET_OBJECT_HANDLES = 0x1007
    GET_OBJECT_INFO = 0x1008
    GET_OBJECT = 0x1009
    SEND_OBJECT_INFO = 0x100d
    GET_PARTIAL_OBJECT = 0x101b
    # Sony vendor
    SDIO_CONNECT = 0x9201
    GET_EXT_DEV_INFO = 0x9202
    SET_PROPERTY = 0x9205
    SEND_CONTROL = 0x9207
    GET_PROPERTIES = 0x9209
    GET_FTP_DISPLAY_NAME_LIST = 0x920e
    SET_FTP_PASSWORD = 0x920f
    OPEN_SESSION_EX = 0x9210
    SET_CONTENTS_TRANSFER_MODE = 0x9212
    SET_SDK_OS_INFO = 0x9214
    GET_DISPLAY_STRING_LIST = 0x9215
    GET_VENDOR_CODE = 0x9216
    GET_FTP_JOB_LIST = 0x9217
    ADD_DELETE_FTP_JOB = 0x9218
    UPLOAD_DATA = 0x921a
    CONTROL_UPLOAD_DATA = 0x921b
    DOWNLOAD_DATA = 0x921d
    GET_FTP_SETTING_LIST = 0x921f
    SET_FTP_SETTING_LIST = 0x9220
    CONTROL_GENERAL_SETTING = 0x9221
    GET_CONTROL_GENERAL_RESULT = 0x9222
    GET_LENS_INFO = 0x9223
    PRECHECK_FW_UPDATE = 0x9227
    SET_FW_UPDATE_MODE = 0x9228
    UPLOAD_PARTIAL_DATA = 0x9229
    EXECUTE_EFRAMING = 0x922a
    GET_OP_RESULTS_SUPPORTED = 0x922f
    CONTROL_MONITORING = 0x9230
    GET_ZOOM_FOCUS_PRESET = 0x9231
    GET_DISPLAY_FTP_RESULT = 0x9233
    GET_OSD_IMAGE = 0x9238
    GET_RESTRICTION_INFO = 0x9239
    GET_DEVICE_DESC_FILE = 0x923a
    GET_CAPTURED_DATE_LIST = 0x923b
    GET_CONTENTS_INFO_LIST = 0x923c
    GET_CONTENTS_DATA = 0x923d
    GET_CONTENTS_COMPRESSED = 0x923e
    GET_STREAM_SETTING_LIST = 0x9241
    SET_STREAM_SETTING_LIST = 0x9242
    CONTROL_PLAYBACK = 0x9243
    CONTROL_PTZF = 0x9245
    PRESET_PTZF = 0x9246
    GET_FW_UPDATER_INFO = 0x9247
    GET_TIMEZONE = 0x9248
    SET_TIMEZONE = 0x9249
    GET_LICENSE_INFO = 0x924d
    DELETE_CONTENT = 0x9250
    GET_EXT_DEV_PROP = 0x9251
    GET_THUMBNAIL = 0x9803


class PTPIPError(Exception):
    pass


GUID_PATH = os.path.join(os.path.expanduser("~"), ".config", "a6700-mcp", "guid")


def _load_or_create_guid() -> bytes:
    try:
        with open(GUID_PATH, "rb") as f:
            g = f.read(16)
            if len(g) == 16:
                return g
    except FileNotFoundError:
        pass
    g = uuid.uuid4().bytes
    os.makedirs(os.path.dirname(GUID_PATH), exist_ok=True)
    with open(GUID_PATH, "wb") as f:
        f.write(g)
    return g


class PTPIPConnection:
    def __init__(self, ip: str, port: int = PTPIP_PORT, name: str = "a6700-mcp",
                 ssh_user: str = "", ssh_pass: str = "", ssh_port: int = 22):
        self.ip = ip
        self.port = port
        self.name = name
        self.guid = _load_or_create_guid()
        self.cmd_sock = None
        self.evt_sock = None
        self.transaction_id = 0
        self.connection_number = 0
        self.camera_guid = b""
        self.vendor_code = 0
        self._evt_thread: Optional[threading.Thread] = None
        self._evt_running = False
        self._lock = threading.Lock()
        self._event_callback = None
        self._ssh_user = ssh_user
        self._ssh_pass = ssh_pass
        self._ssh_port = ssh_port
        self._ssh_client = None
        self._ssh_transport = None

    @property
    def use_ssh(self):
        return bool(self._ssh_user)

    def connect(self):
        if self.use_ssh:
            log.info("connecting via SSH tunnel to %s:%d", self.ip, self._ssh_port)
            self._ssh_connect()
        else:
            log.info("connecting directly to %s:%d", self.ip, self.port)
        self._open_command_channel()
        self._open_event_channel()
        self._open_session()
        self._sony_handshake()
        self._start_event_thread()
        log.info("connected, vendor_code=0x%x", self.vendor_code)

    def _ssh_connect(self):
        if paramiko is None:
            raise PTPIPError("paramiko required for SSH tunnel: pip install paramiko")
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.connect(
            self.ip, self._ssh_port,
            username=self._ssh_user, password=self._ssh_pass,
            look_for_keys=False, allow_agent=False, timeout=10)
        self._ssh_transport = self._ssh_client.get_transport()
        log.info("SSH connected to %s:%d", self.ip, self._ssh_port)

    def _open_ssh_channel(self, dst_port: int):
        return self._ssh_transport.open_channel(
            'direct-tcpip', ('localhost', dst_port), ('localhost', 0), timeout=10)

    def disconnect(self):
        self._evt_running = False
        if self._evt_thread and self._evt_thread.is_alive():
            self._evt_thread.join(timeout=3)
        try:
            self._send_cmd_req(SonyOpcode.CLOSE_SESSION)
        except Exception:
            pass
        for s in (self.cmd_sock, self.evt_sock):
            if s:
                try:
                    s.close()
                except Exception:
                    pass
        self.cmd_sock = None
        self.evt_sock = None
        if self._ssh_client:
            try:
                self._ssh_client.close()
            except Exception:
                pass
            self._ssh_client = None
            self._ssh_transport = None
        log.info("disconnected")

    def set_event_callback(self, cb):
        self._event_callback = cb

    # --- public operations ---

    def get_properties(self, *params) -> bytes:
        return self._send_cmd_req(SonyOpcode.GET_PROPERTIES, list(params))

    def set_property(self, prop_code: int, data: bytes, *extra_params):
        params = [prop_code] + list(extra_params)
        return self._send_data_req(SonyOpcode.SET_PROPERTY, params, data)

    def send_control_command(self, control_code: int, data: bytes, *extra_params):
        params = [control_code] + list(extra_params)
        return self._send_data_req(SonyOpcode.SEND_CONTROL, params, data)

    def get_live_view(self) -> bytes:
        return self._send_cmd_req(SonyOpcode.GET_OBJECT, [0xFFFFC002])

    def send_command(self, opcode: int, params: list = None) -> bytes:
        return self._send_cmd_req(opcode, params or [])

    def send_data_command(self, opcode: int, params: list, data: bytes) -> bytes:
        return self._send_data_req(opcode, params, data)

    # --- connection setup ---

    def _open_command_channel(self):
        if self.use_ssh:
            self.cmd_sock = self._open_ssh_channel(self.port)
        else:
            self.cmd_sock = self._make_socket()
            self.cmd_sock.connect((self.ip, self.port))
        self._send_init_cmd_req()
        pkt_type, payload = self._recv_packet(self.cmd_sock, timeout=10)
        if pkt_type == PacketType.INIT_FAIL:
            reason = struct.unpack_from("<I", payload, 0)[0] if len(payload) >= 4 else 0
            raise PTPIPError(f"InitCommandFail reason={reason:#x}")
        if pkt_type != PacketType.INIT_CMD_ACK:
            raise PTPIPError(f"expected InitCmdAck, got type={pkt_type}")
        self.connection_number = struct.unpack_from("<I", payload, 0)[0]
        if len(payload) >= 20:
            self.camera_guid = payload[4:20]
        log.info("cmd channel open, conn#=%d", self.connection_number)

    def _open_event_channel(self):
        if self.use_ssh:
            self.evt_sock = self._open_ssh_channel(self.port)
        else:
            self.evt_sock = self._make_socket(rcv_timeout=5)
            self.evt_sock.connect((self.ip, self.port))
        self._send_init_event_req()
        pkt_type, payload = self._recv_packet(self.evt_sock, timeout=10)
        if pkt_type == PacketType.INIT_FAIL:
            reason = struct.unpack_from("<I", payload, 0)[0] if len(payload) >= 4 else 0
            raise PTPIPError(f"InitEventFail reason={reason:#x}")
        if pkt_type != PacketType.INIT_EVENT_ACK:
            raise PTPIPError(f"expected InitEventAck, got type={pkt_type}")
        log.info("event channel open")

    def _open_session(self, mode: int = 0):
        if mode == 0:
            opcode = SonyOpcode.OPEN_SESSION
            params_fn = lambda sid: [sid]
        else:
            opcode = SonyOpcode.OPEN_SESSION_EX
            params_fn = lambda sid: [sid, mode]

        for sid in range(1, 256):
            try:
                self._send_cmd_req(opcode, params_fn(sid))
                log.info("OpenSession OK: opcode=0x%04x sid=%d mode=%d", opcode, sid, mode)
                return
            except PTPIPError:
                if sid == 1:
                    log.info("OpenSession sid=1 failed, retrying 2..255")
                continue
        raise PTPIPError("all OpenSession attempts failed")

    def _sony_handshake(self):
        self._send_cmd_req(SonyOpcode.SDIO_CONNECT, [1, 0, 0])
        self._send_cmd_req(SonyOpcode.SDIO_CONNECT, [2, 0, 0])
        try:
            vc_code, vc_params, vc_data = self._send_cmd_req_full(
                SonyOpcode.GET_VENDOR_CODE)
            if vc_params:
                self.vendor_code = vc_params[0]
            elif len(vc_data) >= 4:
                self.vendor_code = struct.unpack_from("<I", vc_data, 0)[0]
        except PTPIPError as e:
            log.warning("getVendorCode failed: %s", e)
        try:
            if self.vendor_code >= 310:
                self._send_cmd_req(SonyOpcode.GET_EXT_DEV_INFO, [300, 1])
            else:
                self._send_cmd_req(SonyOpcode.GET_EXT_DEV_INFO, [300])
        except PTPIPError as e:
            log.warning("getExtDeviceInfo failed: %s", e)
        self._sdio_connect_phase3()

    def _sdio_connect_phase3(self):
        tid = self._next_tid()
        pkt = struct.pack("<IIIHIIII",
                          30,
                          PacketType.OPERATION_REQ,
                          1,
                          SonyOpcode.SDIO_CONNECT,
                          tid,
                          3, 0, 0)
        self._send_raw(self.cmd_sock, pkt)
        self._recv_response()

    # --- packet I/O ---

    def _send_init_cmd_req(self):
        name_utf16 = (self.name + "\x00").encode("utf-16-le")
        length = 28 + len(name_utf16)
        pkt = struct.pack("<II", length, PacketType.INIT_CMD_REQ)
        pkt += self.guid
        pkt += name_utf16
        pkt += struct.pack("<I", 0x00010000)
        self._send_raw(self.cmd_sock, pkt)

    def _send_init_event_req(self):
        pkt = struct.pack("<III", 12, PacketType.INIT_EVENT_REQ, self.connection_number)
        self._send_raw(self.evt_sock, pkt)

    def _send_cmd_req(self, opcode: int, params: list = None) -> bytes:
        _, _, data = self._send_cmd_req_full(opcode, params)
        return data

    def _send_cmd_req_full(self, opcode: int, params: list = None):
        params = params or []
        with self._lock:
            tid = self._next_tid()
            n_params = len(params)
            length = 18 + n_params * 4
            pkt = struct.pack("<IIIH", length, PacketType.OPERATION_REQ, 1, opcode)
            pkt += struct.pack("<I", tid)
            for p in params:
                pkt += struct.pack("<I", p & 0xFFFFFFFF)
            self._send_raw(self.cmd_sock, pkt)
            return self._recv_response_full()

    def _send_data_req(self, opcode: int, params: list, data: bytes) -> bytes:
        with self._lock:
            tid = self._next_tid()
            n_params = len(params)
            length = 18 + n_params * 4
            pkt = struct.pack("<IIIH", length, PacketType.OPERATION_REQ, 2, opcode)
            pkt += struct.pack("<I", tid)
            for p in params:
                pkt += struct.pack("<I", p & 0xFFFFFFFF)
            self._send_raw(self.cmd_sock, pkt)
            time.sleep(0.001)

            start_pkt = struct.pack("<IIIQ", 20, PacketType.START_DATA, tid, len(data))
            self._send_raw(self.cmd_sock, start_pkt)
            time.sleep(0.001)

            end_length = 12 + len(data)
            end_pkt = struct.pack("<III", end_length, PacketType.END_DATA, tid)
            end_pkt += data
            self._send_raw(self.cmd_sock, end_pkt)

            return self._recv_response()

    def _recv_response(self) -> bytes:
        _, _, data = self._recv_response_full()
        return data

    def _recv_response_full(self):
        all_data = b""
        while True:
            pkt_type, payload = self._recv_packet(self.cmd_sock, timeout=60)
            if pkt_type == PacketType.OPERATION_RESP:
                resp_code = 0
                resp_params = []
                if len(payload) >= 2:
                    resp_code = struct.unpack_from("<H", payload, 0)[0]
                if len(payload) >= 6:
                    offset = 6
                    while offset + 4 <= len(payload):
                        resp_params.append(struct.unpack_from("<I", payload, offset)[0])
                        offset += 4
                if resp_code not in (0x2001, 0x2019):
                    raise PTPIPError(
                        f"operation failed: response=0x{resp_code:04x} "
                        f"params={[f'0x{p:08x}' for p in resp_params]}")
                return resp_code, resp_params, all_data
            elif pkt_type == PacketType.START_DATA:
                pass
            elif pkt_type == PacketType.DATA_PACKET:
                if len(payload) >= 4:
                    all_data += payload[4:]
            elif pkt_type == PacketType.END_DATA:
                if len(payload) > 4:
                    all_data += payload[4:]
            else:
                log.warning("unexpected packet type %d in response", pkt_type)

    def _recv_packet(self, sock: socket.socket, timeout: float = 60) -> tuple:
        sock.settimeout(timeout)
        hdr = self._recv_exact(sock, 8)
        length, pkt_type = struct.unpack("<II", hdr)
        payload = b""
        if length > 8:
            payload = self._recv_exact(sock, length - 8)
        return pkt_type, payload

    def _recv_exact(self, sock: socket.socket, n: int) -> bytes:
        buf = bytearray()
        while len(buf) < n:
            chunk = sock.recv(n - len(buf))
            if not chunk:
                raise PTPIPError("connection closed")
            buf.extend(chunk)
        return bytes(buf)

    def _send_raw(self, sock: socket.socket, data: bytes):
        sock.sendall(data)

    def _next_tid(self) -> int:
        self.transaction_id += 1
        return self.transaction_id

    def _make_socket(self, rcv_timeout: int = 2) -> socket.socket:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4 * 1024 * 1024)
        s.settimeout(rcv_timeout)
        return s

    @staticmethod
    def _skip_ptp_string(data: bytes, offset: int) -> int:
        if offset >= len(data):
            return offset
        num_chars = data[offset]
        return offset + 1 + num_chars * 2

    def _has_extension(self, dev_info: bytes, opcode: int) -> bool:
        """Check if opcode is in OperationsSupported of a PTP DeviceInfo blob.
        DeviceInfo layout: u16 StdVer, u32 VendorExtId, u16 VendorExtVer,
        PTPString VendorExtDesc, u16 FuncMode, then u32Array OperationsSupported."""
        if len(dev_info) < 10:
            return False
        try:
            off = 8  # skip StdVer(2) + VendorExtId(4) + VendorExtVer(2)
            off = self._skip_ptp_string(dev_info, off)
            off += 2  # FunctionalMode
            if off + 4 > len(dev_info):
                return False
            count = struct.unpack_from("<I", dev_info, off)[0]
            off += 4
            for _ in range(min(count, 1000)):
                if off + 2 > len(dev_info):
                    break
                op = struct.unpack_from("<H", dev_info, off)[0]
                if op == opcode:
                    return True
                off += 2
            return False
        except Exception:
            return False

    # --- event thread ---

    def _start_event_thread(self):
        self._evt_running = True
        self._evt_thread = threading.Thread(target=self._event_loop, daemon=True)
        self._evt_thread.start()

    def _event_loop(self):
        while self._evt_running:
            try:
                pkt_type, payload = self._recv_packet(self.evt_sock, timeout=5)
                if pkt_type == PacketType.PROBE:
                    try:
                        resp = struct.pack("<II", 8, PacketType.PROBE_RESP)
                        self.evt_sock.sendall(resp)
                    except OSError:
                        break
                elif pkt_type == PacketType.EVENT and len(payload) >= 6:
                    event_code = struct.unpack_from("<H", payload, 0)[0]
                    tid = struct.unpack_from("<I", payload, 2)[0]
                    params = []
                    offset = 6
                    while offset + 4 <= len(payload):
                        params.append(struct.unpack_from("<I", payload, offset)[0])
                        offset += 4
                    if self._event_callback:
                        try:
                            self._event_callback(event_code, tid, params)
                        except Exception as e:
                            log.warning("event callback error: %s", e)
                    else:
                        log.debug("event 0x%04x tid=%d params=%s", event_code, tid, params)
            except socket.timeout:
                continue
            except PTPIPError:
                if self._evt_running:
                    log.warning("event channel error, reconnecting may be needed")
                break
            except Exception as e:
                if self._evt_running:
                    log.warning("event loop error: %s", e)
                break
