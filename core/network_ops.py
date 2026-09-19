"""Network operations: flush DNS, renew IP, test connection."""
from __future__ import annotations

import os
import socket
import subprocess

from utils.logger import logger


def _run(cmd: list[str], timeout: int = 30) -> tuple[bool, str]:
    try:
        flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, creationflags=flags
        )
        out = ((result.stdout or "") + (result.stderr or "")).strip()
        return result.returncode == 0, out
    except subprocess.TimeoutExpired:
        return False, "Timed out"
    except Exception as e:
        return False, str(e)


def flush_dns() -> tuple[bool, str]:
    if os.name != "nt":
        return False, "Not Windows"
    ok, out = _run(["ipconfig", "/flushdns"])
    if ok:
        return True, "DNS cache flushed successfully"
    return False, out or "Failed to flush DNS"


def renew_ip() -> tuple[bool, str]:
    if os.name != "nt":
        return False, "Not Windows"
    ok1, out1 = _run(["ipconfig", "/release"], timeout=45)
    ok2, out2 = _run(["ipconfig", "/renew"], timeout=60)
    if ok2:
        return True, "IP address renewed successfully"
    return False, (out1 + "\n" + out2).strip() or "Failed to renew IP"


def test_connection(host: str = "8.8.8.8", port: int = 53, timeout: float = 3.0) -> tuple[bool, str]:
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        sock.close()
        return True, f"Connection to {host}:{port} successful"
    except Exception as e:
        return False, f"Connection failed: {e}"


def open_network_settings() -> tuple[bool, str]:
    if os.name != "nt":
        return False, "Not Windows"
    try:
        os.startfile("ms-settings:network")  # type: ignore[attr-defined]
        return True, "Opened"
    except Exception as e:
        return False, str(e)
