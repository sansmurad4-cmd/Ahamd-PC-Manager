"""Basic smoke tests for core modules (run on Windows for full coverage)."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.system_info import (
    get_basic_system_info,
    get_cpu_percent,
    get_all_disk_usage,
    format_bytes,
    format_uptime,
)
from core.processes import list_processes, is_protected
from core.cleanup import get_cleanup_categories


def test_system_info():
    info = get_basic_system_info()
    assert info.computer_name
    assert info.ram_total_gb > 0
    assert get_cpu_percent() >= 0


def test_disks():
    disks = get_all_disk_usage()
    assert isinstance(disks, list)


def test_processes():
    procs = list_processes()
    assert isinstance(procs, list)
    assert is_protected("csrss.exe", 100) is True
    assert is_protected("notepad.exe", 12345) is False


def test_cleanup_cats():
    cats = get_cleanup_categories()
    assert len(cats) >= 1


def test_format():
    assert "GB" in format_bytes(5 * 1024**3) or "MB" in format_bytes(5 * 1024**2)
    assert format_uptime(3661)


if __name__ == "__main__":
    test_system_info()
    test_disks()
    test_processes()
    test_cleanup_cats()
    test_format()
    print("All tests passed")
