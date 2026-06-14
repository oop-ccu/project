@echo off
REM Smart Store System - One Step Startup
REM This script starts both the API and Web UI

echo.
echo ================================================
echo     Smart Store System - Starting Services
echo ================================================
echo.

REM Start API Server in a new terminal
echo Starting API Server on http://localhost:5000...
start cmd /k python api.py

REM Wait a moment for the API to start
timeout /t 2 /nobreak

REM Start Web UI in a new terminal
echo Starting Web UI on http://localhost:5173...
cd smart-store
start cmd /k npm run dev

echo.
echo ================================================
echo     Services Starting...
echo ================================================
echo.
echo API:     http://localhost:5000
echo Web UI:  http://localhost:5173
echo.
echo Press Enter in either terminal window to stop services
echo ================================================
echo.

pause
