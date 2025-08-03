@echo off
title Strong No Recoil - View Website Locally
echo Opening Strong No Recoil Website Locally...
echo.

REM Check if index.html exists
if not exist "index.html" (
    echo ERROR: index.html not found!
    echo Please make sure you're in the correct directory.
    pause
    exit /b 1
)

echo ✅ index.html found
echo.
echo Opening website in your default browser...
echo.

REM Open the website directly
start index.html

echo.
echo ✅ Website opened in your browser!
echo.
echo 💡 Note: Some features may not work when viewing locally.
echo    For full functionality, deploy to GitHub Pages.
echo.
pause 