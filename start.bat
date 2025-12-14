@echo off
echo Starting Backend...
start cmd /k "cd backend && uvicorn app.main:app --reload"

echo Starting Frontend...
start cmd /k "cd frontend && npm start"

echo Both services started in separate windows.
