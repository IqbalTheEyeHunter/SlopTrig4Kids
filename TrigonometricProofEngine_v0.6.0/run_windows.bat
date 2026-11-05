@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Python 3 was not found. Install Python 3.11 or newer from python.org and enable Add Python to PATH.
  pause
  exit /b 1
)
py -3 -m pip install --user -r requirements.txt
if errorlevel 1 goto error
py -3 app.py
if errorlevel 1 goto error
exit /b 0
:error
echo.
echo The application could not start. See the error above.
pause
exit /b 1
