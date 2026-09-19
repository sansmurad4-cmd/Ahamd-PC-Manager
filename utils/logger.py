"""Local application logger – no telemetry, file-only."""
from __future__ import annotations

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_log_dir() -> Path:
    """Return a writable log directory under the user's AppData (or fallback)."""
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        if base:
            path = Path(base) / "AhamdPCManager" / "logs"
        else:
            path = Path.home() / "AhamdPCManager" / "logs"
    else:
        path = Path.home() / ".ahamd_pc_manager" / "logs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def setup_logger(name: str = "AhamdPCManager") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)
    log_file = get_log_dir() / "app.log"
    handler = RotatingFileHandler(
        log_file, maxBytes=2 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also log warnings+ to console when running from source
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger


logger = setup_logger()
