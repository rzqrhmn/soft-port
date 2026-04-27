@echo off
REM Weekly report generator — called by Task Scheduler every Sunday 20:00.

set "ROOT=%~dp0.."
cd /d "%ROOT%"

if not exist logs mkdir logs

echo. >> logs\weekly.log
echo --- Weekly run %date% %time% --- >> logs\weekly.log

python automation\weekly_report.py >> logs\weekly.log 2>&1
python automation\update_readme.py >> logs\weekly.log 2>&1
python automation\save.py "Weekly report auto-generated" >> logs\weekly.log 2>&1

exit /b %ERRORLEVEL%
