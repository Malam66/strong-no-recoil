@echo off
title Strong No Recoil Application
echo Starting Strong No Recoil Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip show pynput >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo Dependencies OK
echo.
echo Starting application...
echo.
echo NOTE: Run as Administrator for best compatibility
echo.

REM Run the application
python no_recoil_app.py

if errorlevel 1 (
    echo.
    echo Application crashed or encountered an error
    pause
) 