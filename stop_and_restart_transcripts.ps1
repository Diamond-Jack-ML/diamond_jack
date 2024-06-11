# Define paths
$repoPath = "C:\dev\diamond_jack"
$logsDir = "$repoPath\logs"
$transcriptPath = "$logsDir\full_shell_logs.txt"

# Change to the git repository directory
Set-Location -Path $repoPath

# Stop all active transcriptions
Get-Process | Where-Object { $_.ProcessName -eq "powershell" } | ForEach-Object {
    try {
        Stop-Transcript
        Write-Host "Stopped transcription for process ID: $_.Id"
    } catch {
        Write-Host "No active transcription to stop for process ID: $_.Id"
    }
}

# Concatenate all shell session logs into a single log file
Get-ChildItem -Path $logsDir -Filter "shell_logs_*.txt" | ForEach-Object {
    Get-Content -Path $_.FullName | Add-Content -Path $transcriptPath
    Remove-Item -Path $_.FullName
}

# Add consolidated log file to git
Write-Host "Adding logs to git"
git add $transcriptPath
Write-Host "Logs added to git successfully"

# Get current timestamp
Write-Host "Getting current timestamp"
$currentTimestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Commit logs with timestamp
Write-Host "Committing logs with timestamp"
git commit -m "Update shell logs - $currentTimestamp"
Write-Host "Logs committed to git successfully"

# Restart transcription for new shell sessions
Start-Transcript -Path $transcriptPath
Write-Host "Transcript started, output file is $transcriptPath"
