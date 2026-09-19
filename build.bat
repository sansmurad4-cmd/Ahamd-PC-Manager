@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ========================================
echo   Ahamd PC Manager - Build EXE
echo ========================================
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in PATH.
    echo Install Python 3.12+ from https://www.python.org and try again.
    pause
    exit /b 1
)

python --version
echo.

echo [1/4] Creating virtual environment...
if not exist ".venv" (
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create venv.
        pause
        exit /b 1
    )
)

call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate venv.
    pause
    exit /b 1
)

echo [2/4] Installing dependencies...
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt pywin32 pyinstaller -q
if errorlevel 1 (
    echo [ERROR] pip install failed.
    pause
    exit /b 1
)

if not exist assets mkdir assets

echo [3/4] Building AhamdPCManager.exe (this may take a few minutes)...
echo.

if exist AhamdPCManager.spec (
    pyinstaller --noconfirm --clean AhamdPCManager.spec
) else (
    pyinstaller --noconfirm --clean --onefile --windowed ^
      --name AhamdPCManager ^
      --version-file version_info.txt ^
      --add-data "assets;assets" ^
      --hidden-import PySide6.QtCore ^
      --hidden-import PySide6.QtGui ^
      --hidden-import PySide6.QtWidgets ^
      --hidden-import psutil ^
      app.py
)

if errorlevel 1 (
    echo.
    echo [ERROR] Build FAILED. See messages above.
    pause
    exit /b 1
)

echo.
echo [4/4] Done.
echo.
if exist "dist\AhamdPCManager.exe" (
    echo SUCCESS: dist\AhamdPCManager.exe
    for %%A in ("dist\AhamdPCManager.exe") do echo Size: %%~zA bytes
) else (
    echo [WARN] EXE not found in dist\ - check dist folder.
)
echo.
echo You can copy dist\AhamdPCManager.exe anywhere - it is portable.
echo.
pause
endlocal
