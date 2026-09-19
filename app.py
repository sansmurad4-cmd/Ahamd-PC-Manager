#!/usr/bin/env python3
"""Ahamd PC Manager – lightweight Windows PC management tool."""
from __future__ import annotations

import os
import sys

# Ensure project root is on path
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from utils.logger import logger


def main() -> int:
    # High-DPI
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication(sys.argv)
    app.setApplicationName("Ahamd PC Manager")
    app.setOrganizationName("Ahamd")
    app.setApplicationVersion("1.0.0")

    # Application icon
    from PySide6.QtGui import QIcon
    icon_path = os.path.join(ROOT, "assets", "app.ico")
    if os.path.isfile(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    # Default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    logger.info("Starting Ahamd PC Manager v1.0.0")
    window = MainWindow()
    window.show()
    code = app.exec()
    logger.info("Exiting with code %s", code)
    return code


if __name__ == "__main__":
    sys.exit(main())
