"""Persistent application settings (SQLite + simple JSON fallback)."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from utils.logger import logger


def get_config_dir() -> Path:
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        if base:
            path = Path(base) / "AhamdPCManager"
        else:
            path = Path.home() / "AhamdPCManager"
    else:
        path = Path.home() / ".ahamd_pc_manager"
    path.mkdir(parents=True, exist_ok=True)
    return path


DEFAULTS: dict[str, Any] = {
    "language": "en",  # en | ar
    "theme": "system",  # light | dark | system
    "start_with_windows": False,
    "refresh_interval_ms": 2000,
    "notifications": True,
    "window_geometry": None,
}


class Config:
    def __init__(self) -> None:
        self._path = get_config_dir() / "settings.json"
        self._data: dict[str, Any] = dict(DEFAULTS)
        self.load()

    def load(self) -> None:
        try:
            if self._path.exists():
                with open(self._path, "r", encoding="utf-8") as f:
                    stored = json.load(f)
                if isinstance(stored, dict):
                    self._data.update(stored)
        except Exception as e:
            logger.warning("Failed to load settings: %s", e)

    def save(self) -> None:
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error("Failed to save settings: %s", e)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default if default is not None else DEFAULTS.get(key))

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value
        self.save()

    def as_dict(self) -> dict[str, Any]:
        return dict(self._data)


config = Config()
