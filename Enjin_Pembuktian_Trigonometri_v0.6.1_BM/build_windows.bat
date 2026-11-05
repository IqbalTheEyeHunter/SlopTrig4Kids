@echo off
setlocal
cd /d "%~dp0"
echo ============================================================
echo   MEMBINA ENJIN PEMBUKTIAN TRIGONOMETRI UNTUK WINDOWS
echo   EDISI BAHASA MELAYU v0.6.1
echo ============================================================
where py >nul 2>nul
if errorlevel 1 (
  echo Python 3 tidak ditemukan. Pasang Python 3.11 atau versi lebih baharu.
  pause
  exit /b 1
)
py -3 -m pip install --upgrade pip
if errorlevel 1 goto error
py -3 -m pip install -r requirements.txt pyinstaller
if errorlevel 1 goto error
py -3 -m PyInstaller --noconfirm --clean --onefile --windowed --collect-all sympy --name EnjinPembuktianTrigonometri --add-data "knowledge\SKILL.md;knowledge" --add-data "knowledge\Panduan_Identiti_MS.md;knowledge" app.py
if errorlevel 1 goto error
echo.
echo PEMBINAAN SELESAI: dist\EnjinPembuktianTrigonometri.exe
echo Salin fail EXE ke komputer Windows. Sambungan Internet tidak diperlukan semasa aplikasi dijalankan.
pause
exit /b 0
:error
echo.
echo PEMBINAAN GAGAL. Semak mesej ralat di atas.
pause
exit /b 1
