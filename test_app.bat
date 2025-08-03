@echo off
title Strong No Recoil - App Test
echo Testing Strong No Recoil Application...
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
echo Running application test...
echo.

REM Run the test script
python test_app.py

if errorlevel 1 (
    echo.
    echo Test failed. Checking individual components...
    echo.
    
    echo Testing basic app...
    python -c "import no_recoil_app; print('Basic app works')" 2>nul
    if errorlevel 1 (
        echo Basic app has issues
    ) else (
        echo Basic app works
    )
    
    echo Testing advanced app...
    python -c "import advanced_no_recoil; print('Advanced app works')" 2>nul
    if errorlevel 1 (
        echo Advanced app has issues
    ) else (
        echo Advanced app works
    )
    
    echo Testing launcher...
    python -c "import launcher; print('Launcher works')" 2>nul
    if errorlevel 1 (
        echo Launcher has issues
    ) else (
        echo Launcher works
    )
)

echo.
echo Test completed.
pause 