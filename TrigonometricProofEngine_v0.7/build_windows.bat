@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo   BUILDING TRIGONOMETRIC PROOF ENGINE FOR WINDOWS
echo ============================================================
where py >nul 2>nul
if errorlevel 1 (
  echo Python 3 was not found. Install Python 3.11 or newer first.
  pause
  exit /b 1
)
py -3 -m pip install --upgrade pip
if errorlevel 1 goto error
py -3 -m pip install -r requirements.txt pyinstaller
if errorlevel 1 goto error
py -3 -m PyInstaller --noconfirm --clean --onefile --windowed --collect-all sympy --name TrigonometricProofEngine --add-data "knowledge\SKILL.md;knowledge" app.py
if errorlevel 1 goto error
echo.
echo BUILD COMPLETE: dist\TrigonometricProofEngine.exe
echo Copy the EXE to any Windows PC. No internet connection is required at runtime.
pause
exit /b 0
:error
echo.
echo BUILD FAILED. Review the error messages above.
pause
exit /b 1
