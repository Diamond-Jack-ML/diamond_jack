# Define paths
$repoPath = "C:\dev\diamond_jack"
$logsDir = "$repoPath\logs"

# Generate a unique identifier for the shell session
$sessionId = [guid]::NewGuid()
$transcriptPath = "$logsDir\shell_logs_$sessionId.txt"

# Change to the git repository directory
Set-Location -Path $repoPath

# Ensure the logs directory exists
if (!(Test-Path -Path $logsDir)) {
    New-Item -ItemType Directory -Path $logsDir
}

# Start a new transcript session
Start-Transcript -Path $transcriptPath
Write-Host "Transcript started, output file is $transcriptPath"

# Function to stop transcription and commit logs
function Stop-TranscriptionAndCommit {
    param ($transcriptPath, $sessionId)
    
    try {
        Stop-Transcript
        Write-Host "Transcript stopped successfully for session $sessionId"
    } catch {
        Write-Host "No active transcription to stop for session $sessionId"
    }

    # Add logs to git
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

    # Remove the shell session log file
    Remove-Item -Path $transcriptPath
    Write-Host "Shell session log file removed"
}

# Register a script block to run when the shell session exits
$scriptBlock = {
    Stop-TranscriptionAndCommit -transcriptPath $transcriptPath -sessionId $sessionId
}
Register-EngineEvent PowerShell.Exiting -Action $scriptBlock

Write-Host "Shell session setup complete for session $sessionId"
