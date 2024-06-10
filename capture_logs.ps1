# capture_logs.ps1

Write-Output "Starting capture_logs.ps1 execution"

# Set the logs directory inside the repository
$logsDir = "C:\dev\diamond_jack\logs"
if (!(Test-Path -Path $logsDir)) {
    New-Item -ItemType Directory -Path $logsDir
}

# Capturing shell session history
Write-Output "Capturing shell session history"
Get-Content (Get-PSReadLineOption).HistorySavePath | Out-File -FilePath "$logsDir\shell_logs.txt"
Write-Output "Shell session history captured successfully"

# Capturing system logs
Write-Output "Capturing system logs"
Get-EventLog -LogName System -Newest 100 | Out-File -FilePath "$logsDir\system_logs.txt"
Write-Output "System logs captured successfully"

# Navigate to the git repository
Set-Location -Path "C:\dev\diamond_jack"

# Adding logs to git
Write-Output "Adding logs to git"
git add logs/shell_logs.txt logs/system_logs.txt
Write-Output "Logs added to git successfully"

# Getting current timestamp
$tstamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Output "Getting current timestamp"

# Committing logs with timestamp
Write-Output "Committing logs with timestamp"
git commit -m "Update shell and system logs - $tstamp"
Write-Output "Logs committed to git successfully"
