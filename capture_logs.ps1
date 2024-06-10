# Capture shell session history
Get-History | Out-File -FilePath logs\shell_logs.txt

# Capture system logs
Get-EventLog -LogName System | Out-File -FilePath logs\system_logs.txt

# Add logs to git
git add -f logs\shell_logs.txt logs\system_logs.txt

# Get current timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Commit logs with timestamp
git commit -m "Update shell and system logs - $timestamp"
