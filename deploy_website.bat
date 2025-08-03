@echo off
title Strong No Recoil - Website Deployment
echo Deploying Strong No Recoil Website to GitHub Pages...
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
echo Starting website deployment...
echo.

REM Run the deployment script
python deploy_website.py

pause 