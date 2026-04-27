# setup_windows_tasks.ps1
# Registers 3 scheduled tasks for the Soft portfolio.
# Run from PowerShell as Administrator:
#   PowerShell -ExecutionPolicy Bypass -File automation\setup_windows_tasks.ps1
#
# Tasks created:
#   Soft-Daily-Template   — every day 08:00, generate today's task folder
#   Soft-Hourly-Push      — every hour, push unpushed commits to GitHub
#   Soft-Weekly-Report    — every Sunday 20:00, generate weekly report

$ErrorActionPreference = "Stop"

$ROOT = Resolve-Path (Join-Path $PSScriptRoot "..")
$DAILY  = Join-Path $ROOT "automation\run_daily.bat"
$HOURLY = Join-Path $ROOT "automation\run_hourly.bat"
$WEEKLY = Join-Path $ROOT "automation\run_weekly.bat"

Write-Host "Repo root: $ROOT"
Write-Host ""

# Sanity checks
foreach ($p in @($DAILY, $HOURLY, $WEEKLY)) {
    if (-not (Test-Path $p)) {
        Write-Error "Missing script: $p"
        exit 1
    }
}

function Register-Or-Replace {
    param(
        [string]$Name,
        [Microsoft.Management.Infrastructure.CimInstance[]]$Triggers,
        [Microsoft.Management.Infrastructure.CimInstance]$Action,
        [string]$Description
    )

    if (Get-ScheduledTask -TaskName $Name -ErrorAction SilentlyContinue) {
        Write-Host "[=] Removing existing task: $Name"
        Unregister-ScheduledTask -TaskName $Name -Confirm:$false
    }

    $settings = New-ScheduledTaskSettingsSet `
        -AllowStartIfOnBatteries `
        -DontStopIfGoingOnBatteries `
        -StartWhenAvailable `
        -ExecutionTimeLimit (New-TimeSpan -Minutes 10)

    Register-ScheduledTask `
        -TaskName $Name `
        -Description $Description `
        -Action $Action `
        -Trigger $Triggers `
        -Settings $settings `
        -RunLevel Limited | Out-Null

    Write-Host "[+] Registered: $Name"
}

# === Soft-Daily-Template — every day 08:00 ===
$dailyAction  = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$DAILY`""
$dailyTrigger = New-ScheduledTaskTrigger -Daily -At "08:00"
Register-Or-Replace `
    -Name "Soft-Daily-Template" `
    -Triggers @($dailyTrigger) `
    -Action $dailyAction `
    -Description "Soft portfolio: generate today's task folder + refresh README."

# === Soft-Hourly-Push — every hour, every day ===
$hourlyAction = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$HOURLY`""
$hourlyTrigger = New-ScheduledTaskTrigger -Once -At (Get-Date).Date.AddHours(9) `
    -RepetitionInterval (New-TimeSpan -Hours 1) `
    -RepetitionDuration (New-TimeSpan -Days 365)
Register-Or-Replace `
    -Name "Soft-Hourly-Push" `
    -Triggers @($hourlyTrigger) `
    -Action $hourlyAction `
    -Description "Soft portfolio: push unpushed commits to GitHub every hour."

# === Soft-Weekly-Report — every Sunday 20:00 ===
$weeklyAction = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$WEEKLY`""
$weeklyTrigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At "20:00"
Register-Or-Replace `
    -Name "Soft-Weekly-Report" `
    -Triggers @($weeklyTrigger) `
    -Action $weeklyAction `
    -Description "Soft portfolio: generate weekly progress report."

Write-Host ""
Write-Host "All 3 tasks registered. Verify in Task Scheduler:"
Write-Host "  Start menu -> Task Scheduler -> Task Scheduler Library"
Write-Host ""
Write-Host "To disable temporarily (e.g. on holidays):"
Write-Host '  Disable-ScheduledTask -TaskName "Soft-Daily-Template"'
Write-Host '  Disable-ScheduledTask -TaskName "Soft-Hourly-Push"'
Write-Host '  Disable-ScheduledTask -TaskName "Soft-Weekly-Report"'
Write-Host ""
Write-Host "To re-enable: Enable-ScheduledTask -TaskName ..."
Write-Host ""
Write-Host "To remove entirely:"
Write-Host '  Unregister-ScheduledTask -TaskName "Soft-Daily-Template" -Confirm:$false'
