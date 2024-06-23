#!/bin/bash

# Define paths
LOGS_DIR="$HOME/diamond_jack/logs"
mkdir -p $LOGS_DIR
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
TRANSCRIPT_FILE="$LOGS_DIR/shell_logs_$TIMESTAMP.txt"

# Start transcription
script -q -a $TRANSCRIPT_FILE

# Mark the end of the transcription
echo "End of transcription for session $TIMESTAMP" >> $TRANSCRIPT_FILE

