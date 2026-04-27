@echo off
REM Hourly auto-push — called by Task Scheduler.

set "ROOT=%~dp0.."
cd /d "%ROOT%"

if not exist logs mkdir logs

python automation\auto_push.py >> logs\hourly.log 2>&1

exit /b %ERRORLEVEL%
