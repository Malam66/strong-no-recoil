@echo off
title Strong No Recoil - GitHub Deployment
echo Starting GitHub deployment...
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
echo Starting automated GitHub deployment...
echo.

REM Run the deployment script
python deploy_to_github.py

if errorlevel 1 (
    echo.
    echo Deployment script crashed or encountered an error
    pause
) 