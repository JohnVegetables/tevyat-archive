@echo off
cd /d "%~dp0"
where pythonw >nul 2>nul
if %errorlevel%==0 (
    start "" pythonw "tools\importer_app.py"
    exit /b
)
where python >nul 2>nul
if %errorlevel%==0 (
    start "" python "tools\importer_app.py"
    exit /b
)
echo Python is not installed.
echo.
echo Install it from https://www.python.org/downloads/ and tick "Add python.exe to PATH",
echo then double-click this file again. Or download the ready-made .exe from the Releases page.
echo.
start "" "https://www.python.org/downloads/"
pause
