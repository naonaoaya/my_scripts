#!/usr/bin/env python3
"""
File organizer script - organizes files in a directory by extension
"""

import os
import sys
import shutil
from pathlib import Path
from collections import defaultdict


def organize_files(directory, dry_run=False):
    """
    Organize files in the given directory by their extensions.
    
    Args:
        directory: Path to the directory to organize
        dry_run: If True, only show what would be done without making changes
    """
    directory = Path(directory).resolve()
    
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return
    
    if not directory.is_dir():
        print(f"Error: '{directory}' is not a directory")
        return
    
    # Group files by extension
    files_by_ext = defaultdict(list)
    
    for item in directory.iterdir():
        if item.is_file():
            ext = item.suffix.lower() or '.no_extension'
            files_by_ext[ext].append(item)
    
    # Display what will be done
    print(f"Organizing files in: {directory}")
    print(f"Found {sum(len(files) for files in files_by_ext.values())} files")
    print()
    
    for ext, files in sorted(files_by_ext.items()):
        folder_name = ext[1:] if ext.startswith('.') else ext
        folder_path = directory / folder_name
        
        print(f"{ext}: {len(files)} files -> {folder_name}/")
        
        if not dry_run:
            folder_path.mkdir(exist_ok=True)
            
            for file in files:
                dest = folder_path / file.name
                # Handle name conflicts
                if dest.exists():
                    base = file.stem
                    counter = 1
                    while dest.exists():
                        dest = folder_path / f"{base}_{counter}{file.suffix}"
                        counter += 1
                
                shutil.move(str(file), str(dest))
                print(f"  Moved: {file.name} -> {folder_name}/{dest.name}")
    
    if dry_run:
        print("\n(Dry run - no files were moved)")
    else:
        print("\nFiles organized successfully!")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 file_organizer.py <directory> [--dry-run]")
        print("\nOrganizes files in the specified directory by their extensions")
        sys.exit(1)
    
    directory = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    organize_files(directory, dry_run)


if __name__ == '__main__':
    main()
