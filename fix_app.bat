@echo off
title Strong No Recoil - App Fix
echo Fixing Strong No Recoil Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

echo Python found
echo.
echo Running app fix...
echo.

REM Run the fix script
python fix_app.py

if errorlevel 1 (
    echo.
    echo Fix script failed. Trying manual fixes...
    echo.
    
    echo Installing dependencies manually...
    pip install -r requirements.txt
    
    echo.
    echo Manual fix completed.
)

echo.
echo Fix process completed.
pause 