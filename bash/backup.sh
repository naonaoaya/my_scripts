#!/bin/bash
# Simple file backup script

# Usage: ./backup.sh <source_file> [destination_directory]

if [ $# -eq 0 ]; then
    echo "Usage: $0 <source_file> [destination_directory]"
    exit 1
fi

SOURCE_FILE="$1"
DEST_DIR="${2:-$HOME/backups}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file '$SOURCE_FILE' does not exist"
    exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Get the filename from the path
FILENAME=$(basename "$SOURCE_FILE")
BACKUP_FILE="$DEST_DIR/${FILENAME}.${TIMESTAMP}.bak"

# Copy the file
if cp "$SOURCE_FILE" "$BACKUP_FILE"; then
    echo "Backup created successfully: $BACKUP_FILE"
else
    echo "Error: Backup failed"
    exit 1
fi
