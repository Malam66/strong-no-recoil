@echo off
title Strong No Recoil Launcher
echo Starting Strong No Recoil Launcher...
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
echo Starting launcher...
echo.

REM Run the launcher
python launcher.py

if errorlevel 1 (
    echo.
    echo Launcher crashed or encountered an error
    pause
) 