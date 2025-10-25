#!/bin/bash
#
# install-slash-commands.sh
# Copies slash commands from slash-commands directory to .claude/commands
# This allows end users to install shared slash commands into their local Claude Code config

set -e

# Define source and destination directories
SOURCE_DIR="slash-commands"
DEST_DIR=".claude/commands"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: $SOURCE_DIR does not exist. Nothing to install."
    exit 1
fi

# Check if source directory has any files
if [ ! "$(ls -A "$SOURCE_DIR")" ]; then
    echo "Error: No files found in $SOURCE_DIR"
    exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Copy all files from source to destination
echo "Installing slash commands from $SOURCE_DIR to $DEST_DIR..."
cp -r "$SOURCE_DIR"/* "$DEST_DIR/"

echo "✓ Slash commands installed successfully"
echo ""
echo "Installed commands:"
ls -1 "$DEST_DIR" | sed 's/^/  - /'

exit 0
