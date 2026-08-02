# install_windows_task.ps1 — register hfo-article-scanner-daily
#
# Registers two scheduled tasks:
#   1) hfo-article-scanner-daily      — 06:00 local, runs run.py
#   2) hfo-article-scanner-weekly     — Sunday 06:15 local, runs weekly_review.py
#
# Idempotent: /F forces overwrite if the task already exists.
# Run as the operator's own account so scheduler inherits env vars from .env
# (autoloaded by slack_escalate + litellm_client).
#
# Usage:
#   cd C:\Dev\hfo_gen_133_forge\factory\loops\article_scanner
#   .\install_windows_task.ps1                       # install both
#   .\install_windows_task.ps1 -Uninstall            # remove both

param(
    [switch]$Uninstall,
    [string]$PythonExe = "python",
    [string]$Time      = "06:00",
    [string]$WeeklyTime = "06:15",
    [string]$ForgeRoot = "C:\Dev\hfo_gen_133_forge"
)

$loop     = "$ForgeRoot\factory\loops\article_scanner\run.py"
$weekly   = "$ForgeRoot\factory\loops\article_scanner\weekly_review.py"
$sources  = "$ForgeRoot\factory\loops\article_scanner\sources.yaml"
$seed     = "$ForgeRoot\factory\loops\article_scanner\seed_urls.json"
$taskA    = "hfo-article-scanner-daily"
$taskB    = "hfo-article-scanner-weekly"

if ($Uninstall) {
    Write-Host "Removing $taskA + $taskB ..."
    schtasks /Delete /TN $taskA /F 2>$null
    schtasks /Delete /TN $taskB /F 2>$null
    Write-Host "Done."
    exit 0
}

# Sanity: files exist?
foreach ($f in @($loop, $weekly, $sources, $seed)) {
    if (-not (Test-Path $f)) {
        Write-Error "Missing file: $f"
        exit 1
    }
}

# Daily
$cmdDaily = "$PythonExe `"$loop`" --sources `"$sources`" --seed `"$seed`""
Write-Host "Installing $taskA @ daily $Time"
schtasks /Create /TN $taskA `
    /TR $cmdDaily `
    /SC DAILY /ST $Time /F

# Weekly (Sunday)
$cmdWeekly = "$PythonExe `"$weekly`""
Write-Host "Installing $taskB @ Sunday $WeeklyTime"
schtasks /Create /TN $taskB `
    /TR $cmdWeekly `
    /SC WEEKLY /D SUN /ST $WeeklyTime /F

Write-Host ""
Write-Host "Verify with:"
Write-Host "  schtasks /Query /TN $taskA /V /FO LIST"
Write-Host "  schtasks /Query /TN $taskB /V /FO LIST"
Write-Host ""
Write-Host "Fire-once smoke test (no wait for cron):"
Write-Host "  schtasks /Run /TN $taskA"
