#!/bin/bash
#
# sync-slash-commands.sh
# Syncs slash commands from .claude/commands to slash-commands directory
# This allows sharing project-level slash commands publicly while keeping .claude git-ignored

set -e

# Define source and destination directories
SOURCE_DIR=".claude/commands"
DEST_DIR="slash-commands"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Warning: $SOURCE_DIR does not exist. Nothing to sync."
    exit 0
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Sync the contents
echo "Syncing slash commands from $SOURCE_DIR to $DEST_DIR..."

# Remove all files in destination first to handle deletions
if [ -d "$DEST_DIR" ]; then
    rm -rf "${DEST_DIR:?}"/*
fi

# Copy all files from source to destination
if [ "$(ls -A "$SOURCE_DIR")" ]; then
    cp -r "$SOURCE_DIR"/* "$DEST_DIR/"
    echo "✓ Slash commands synced successfully"

    # Add the synced files to git staging area
    git add "$DEST_DIR"
else
    echo "Warning: No files found in $SOURCE_DIR"
fi

exit 0
