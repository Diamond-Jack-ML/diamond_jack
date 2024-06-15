#/bin/bash

# Define paths
repo_path="/home/alan/diamond_jack"
logs_dir="$repo_path/logs"
timestamp=$(date +"%Y%m%d_%H%M%S")
transcript_path="$logs_dir/shell_logs_$timestamp.txt"

# Change to the git repository directory
cd $repo_path

# Ensure the logs directory exists
mkdir -p $logs_dir

# Stop any existing script logs if running
if [ -f /tmp/current_transcript_pid ]; then
    kill $(cat /tmp/current_transcript_pid)
    rm /tmp/current_transcript_pid
fi

# Start a new transcript session
script -q -c "exec bash" "$transcript_path" &
echo $! > /tmp/current_transcript_pid
echo "Transcript started, output file is $transcript_path"

# Add logs to git
echo "Adding logs to git"
git add $transcript_path
echo "Logs added to git successfully"

# Get current timestamp
echo "Getting current timestamp"
current_timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Commit logs with timestamp
echo "Committing logs with timestamp"
git commit -m "Update shell logs - $current_timestamp"
echo "Logs committed to git successfully"

# Cleanup old log files
find $logs_dir -name "shell_logs_*.txt" ! -name "shell_logs_$timestamp.txt" -exec rm {} \;
echo "Old log files removed"

# Ensure a new transcript is started for the next commands
script -q -c "exec bash" "$logs_dir/full_shell_logs.txt" &
echo "New transcript started for the next session"
