@echo off
echo Starting ShadBot Mobile Web Version...
echo.
echo Installing required packages...
python -m pip install -r requirements.txt
echo.
echo Starting ShadBot Web Server...
echo.
echo ========================================
echo   ShadBot is starting on:
echo   http://localhost:5000
echo   
echo   Open this URL in any web browser
echo   (works on mobile and desktop!)
echo ========================================
echo.
python shadbot_web.py
pause
