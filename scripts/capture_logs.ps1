# Define paths
$repoPath = "C:\dev\diamond_jack"
$logsDir = "$repoPath\logs"
$transcriptPath = "$logsDir\full_shell_logs.txt"

# Change to the git repository directory
Set-Location -Path $repoPath

# Stop any existing transcript, if active
try {
    Stop-Transcript
    Write-Host "Existing transcript stopped successfully"
} catch {
    Write-Host "No active transcription to stop"
}

# Ensure the logs directory exists
if (!(Test-Path -Path $logsDir)) {
    New-Item -ItemType Directory -Path $logsDir
}

# Add logs to git
Write-Host "Adding logs to git"
git add $transcriptPath
Write-Host "Logs added to git successfully"

# Get current timestamp
Write-Host "Getting current timestamp"
$currentTimestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"


# Start a new transcript session
Start-Transcript -Path $transcriptPath
Write-Host "Transcript started, output file is $transcriptPath"
