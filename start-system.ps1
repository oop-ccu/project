#!/usr/bin/env pwsh
# Smart Store System - One Step Startup (PowerShell)
# This script starts both the API and Web UI

Write-Host "`n================================================" -ForegroundColor Cyan
Write-Host "     Smart Store System - Starting Services" -ForegroundColor Cyan
Write-Host "================================================`n" -ForegroundColor Cyan

# Start API Server in a new PowerShell window
Write-Host "Starting API Server on http://localhost:5000..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python api.py"

# Wait a moment for the API to start
Start-Sleep -Seconds 2

# Start Web UI in a new PowerShell window
Write-Host "Starting Web UI on http://localhost:5174..." -ForegroundColor Yellow
$webDir = Join-Path $PSScriptRoot "smart-store"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$webDir'; npm run dev"

Write-Host "`n================================================" -ForegroundColor Cyan
Write-Host "     Services Starting..." -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "`nAPI:     http://localhost:5000" -ForegroundColor Green
Write-Host "Web UI:  http://localhost:5174" -ForegroundColor Green
Write-Host "`nPress Ctrl+C in any terminal window to stop services" -ForegroundColor Yellow
Write-Host "================================================`n" -ForegroundColor Cyan
