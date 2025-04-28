#!/bin/bash

THE_DIR=$(pwd) # safer and preferred over backticks

# Ensure the source exists
if [ ! -f bin/chess ]; then
    echo "Error: bin/chess does not exist."
    exit 1
fi

# Create symlink (requires sudo to write to /usr/bin)
sudo ln -sf "$THE_DIR/bin/chess" /usr/bin/chess

CHESS_PATH="$THE_DIR/bin/chess"

# Optional: Patch the script if needed
sed -i "s|^PARENT_DIR=.*|PARENT_DIR=\"$THE_DIR\"|" "$CHESS_PATH"

# Confirm success
if [ -L /usr/bin/chess ]; then
    echo "Symbolic link created: /usr/bin/chess → $CHESS_PATH"
else
    echo "Failed to create symlink."
    exit 1
fi

