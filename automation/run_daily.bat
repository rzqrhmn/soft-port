@echo off
REM Daily template generator — called by Task Scheduler.
REM Logs go to logs\daily.log so failures are debuggable.

set "ROOT=%~dp0.."
cd /d "%ROOT%"

if not exist logs mkdir logs

echo. >> logs\daily.log
echo --- Daily run %date% %time% --- >> logs\daily.log

python automation\daily_template.py >> logs\daily.log 2>&1
python automation\update_readme.py >> logs\daily.log 2>&1

exit /b %ERRORLEVEL%
