# Ahamd PC Manager

**Version 1.0.0** · Built by Ahamd

Lightweight Windows 10/11 PC management and maintenance tool.  
Native desktop app — **Python + PySide6**. No Electron, no web UI, no ads, no telemetry, no account.

![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-blue)
![Python](https://img.shields.io/badge/python-3.12%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

## Download

**[Download AhamdPCManager.exe](https://github.com/sansmurad4-cmd/Ahamd-PC-Manager/releases/latest)** (Windows 10/11, portable)

Or build from source below.

## Features

| Section | What it does |
|--------|----------------|
| **Dashboard** | Live CPU, RAM, Disk, GPU (when available), temperature, uptime |
| **System** | Full OS/hardware info + copy to clipboard |
| **Performance** | Live charts for CPU, RAM, Disk, Network |
| **Storage** | Drive usage + optional large-file scan |
| **Startup** | View / enable / disable startup programs |
| **Processes** | List processes, open location, end process (system processes protected) |
| **Network** | Local IP, optional public IP, speeds, Flush DNS, Renew IP, test connection |
| **Cleanup** | Safe temp scan → review → confirm → clean |
| **Tools** | Task Manager, Device Manager, Disk Management, Event Viewer, and more |
| **Settings** | English / العربية · Light / Dark / System theme · Start with Windows |

## Run from source

```bat
git clone https://github.com/sansmurad4-cmd/Ahamd-PC-Manager.git
cd Ahamd-PC-Manager
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install pywin32
python app.py
```

## Build EXE

```bat
.\build.bat
```

Output: `dist\AhamdPCManager.exe`

## Safety

- No automatic destructive actions  
- Confirmation before delete / kill process / network reset  
- Critical system processes cannot be terminated from the app  
- Logs only on your PC (`%LOCALAPPDATA%\AhamdPCManager\logs`)

## License

MIT © 2026 Ahamd — see [LICENSE](LICENSE)
