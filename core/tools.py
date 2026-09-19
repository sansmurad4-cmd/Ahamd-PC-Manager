"""Launch real Windows system utilities."""
from __future__ import annotations

import os
import subprocess
from typing import Callable

from utils.logger import logger


def _start(cmd: list[str] | str, shell: bool = False) -> tuple[bool, str]:
    try:
        if os.name == "nt":
            if isinstance(cmd, str):
                os.startfile(cmd)  # type: ignore[attr-defined]
            else:
                subprocess.Popen(
                    cmd,
                    shell=shell,
                    creationflags=subprocess.CREATE_NO_WINDOW if not shell else 0,
                )
        else:
            subprocess.Popen(cmd if isinstance(cmd, list) else cmd.split(), shell=shell)
        return True, "Launched"
    except Exception as e:
        logger.error("launch failed: %s – %s", cmd, e)
        return False, str(e)


def open_task_manager() -> tuple[bool, str]:
    return _start(["taskmgr.exe"])


def open_device_manager() -> tuple[bool, str]:
    return _start(["devmgmt.msc"])


def open_disk_management() -> tuple[bool, str]:
    return _start(["diskmgmt.msc"])


def open_event_viewer() -> tuple[bool, str]:
    return _start(["eventvwr.msc"])


def open_services() -> tuple[bool, str]:
    return _start(["services.msc"])


def open_system_information() -> tuple[bool, str]:
    return _start(["msinfo32.exe"])


def open_command_prompt() -> tuple[bool, str]:
    return _start(["cmd.exe"])


def open_powershell() -> tuple[bool, str]:
    return _start(["powershell.exe"])


def open_windows_settings() -> tuple[bool, str]:
    if os.name == "nt":
        return _start("ms-settings:")
    return False, "Not Windows"


def open_control_panel() -> tuple[bool, str]:
    return _start(["control.exe"])


def restart_explorer() -> tuple[bool, str]:
    if os.name != "nt":
        return False, "Not Windows"
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "explorer.exe"],
            capture_output=True,
            timeout=10,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        subprocess.Popen(
            ["explorer.exe"],
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        return True, "Explorer restarted"
    except Exception as e:
        return False, str(e)


TOOL_MAP: dict[str, Callable[[], tuple[bool, str]]] = {
    "task_manager": open_task_manager,
    "device_manager": open_device_manager,
    "disk_management": open_disk_management,
    "event_viewer": open_event_viewer,
    "services": open_services,
    "system_information": open_system_information,
    "command_prompt": open_command_prompt,
    "powershell": open_powershell,
    "windows_settings": open_windows_settings,
    "control_panel": open_control_panel,
}
