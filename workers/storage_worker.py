"""Background large-file scanner."""
from __future__ import annotations

from PySide6.QtCore import QThread, Signal

from core.storage_scan import LargeItem, scan_large_items


class StorageScanWorker(QThread):
    progress = Signal(str)
    finished_scan = Signal(list)
    error = Signal(str)

    def __init__(self, root: str, min_size: int = 50 * 1024 * 1024, parent=None):
        super().__init__(parent)
        self.root = root
        self.min_size = min_size
        self._stop = False

    def stop(self) -> None:
        self._stop = True

    def run(self) -> None:
        try:
            items = scan_large_items(
                self.root,
                min_size=self.min_size,
                progress=lambda p: self.progress.emit(p),
                should_stop=lambda: self._stop,
            )
            self.finished_scan.emit(items)
        except Exception as e:
            self.error.emit(str(e))
