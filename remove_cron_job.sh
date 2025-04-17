#!/bin/bash

# Find the script
SCRIPT_PATH=$(find . -type f -path "*/bin/run_cron.sh" | head -n 1)

# Check if found
if [ -z "$SCRIPT_PATH" ]; then
    echo "Error: Could not find bin/run_cron.sh in subdirectories."
    exit 1
fi

# Get absolute path
ABS_PATH=$(realpath "$SCRIPT_PATH")

# The exact cron job line
CRON_JOB="* * * * * /bin/bash $ABS_PATH"

# Remove matching line from crontab
NEW_CRON=$(crontab -l 2>/dev/null | grep -Fxv "$CRON_JOB")

# Update crontab
echo "$NEW_CRON" | crontab -
echo "Cron job removed (if it existed): $ABS_PATH"

