#!/bin/bash

# This is a program that will add bin to PATH.
# This file is in src.
# CCVS/
# ├── src/
# │   ├── player_install.sh  <- this file
# │   └── main.py
# └── bin/
#     └── chess              <- the launcher script/command

set -e

# Determine script location and root project directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( dirname "$SCRIPT_DIR" )"
BIN_DIR="$PROJECT_ROOT/bin"
CHESS_CMD="$BIN_DIR/chess"
BASHRC="$HOME/.bashrc"

# Function to make bin/chess executable
make_executable() {
    if [ -f "$CHESS_CMD" ]; then
        chmod +x "$CHESS_CMD"
        echo "Made $CHESS_CMD executable."
    else
        echo "Error: $CHESS_CMD not found!"
        exit 1
    fi
}

# Function to add bin to PATH in .bashrc
add_to_path() {
    grep -qxF "export PATH=\"\$PATH:$BIN_DIR\"" "$BASHRC" || {
        echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$BASHRC"
        echo "Added $BIN_DIR to PATH in $BASHRC"
    }
}

# Function to uninstall (remove PATH entry)
uninstall() {
    if grep -q "$BIN_DIR" "$BASHRC"; then
        sed -i.bak "\|$BIN_DIR|d" "$BASHRC"
        echo "Removed $BIN_DIR from PATH in $BASHRC"
        echo "Backup saved as $BASHRC.bak"
    else
        echo "$BIN_DIR not found in $BASHRC"
    fi
    exit 0
}

# Handle uninstall argument
if [ "$1" == "uninstall" ]; then
    uninstall
fi

# Main installation steps
make_executable
add_to_path

echo "Installation complete. Restart your terminal or run 'source ~/.bashrc' to update your PATH."