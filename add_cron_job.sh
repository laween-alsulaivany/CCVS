#!/bin/bash

NEW_DIR=`pwd`

if [ -z "$NEW_DIR" ]; then
	echo "Usage: ./add...sh directory/..."
	exit 1
fi


SCRIPT_PATH=$(find . -type f -path "*/bin/run_cron.sh" | head -n 1)

sed -i "s|^THE_DIR=.*|THE_DIR=\"$NEW_DIR\"|" $SCRIPT_PATH

echo "Updated THE_DIR in .../bin/run_cron.sh to: $NEW_DIR"

if [ -z "$SCRIPT_PATH" ]; then
	echo "Error: Could not find bin/run..."
	exit 1
fi

ABS_PATH=$(realpath "$SCRIPT_PATH")

CRON_JOB="* * * * * /bin/bash $ABS_PATH"

(crontab -l 2>/dev/null | grep -Fxq "$CRON_JOB") && {
	echo "Cron job already exists."
	exit 0
}

(cronrtab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "Cron job added to run every minute: $ABS_PATH"

