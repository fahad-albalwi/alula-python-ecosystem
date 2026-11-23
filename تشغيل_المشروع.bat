@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 beginner_demo.py
) else (
    python beginner_demo.py
)
if errorlevel 1 (
    echo Python could not start. Please install Python 3.10 or newer.
)
pause
