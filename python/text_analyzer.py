#!/usr/bin/env python3
"""
Simple text file analyzer - counts lines, words, and characters
"""

import sys
from pathlib import Path


def analyze_file(filepath):
    """
    Analyze a text file and return statistics.
    
    Args:
        filepath: Path to the file to analyze
        
    Returns:
        Dictionary with file statistics
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            words = content.split()
            
            stats = {
                'lines': len(lines),
                'words': len(words),
                'chars': len(content),
                'chars_no_spaces': len(content.replace(' ', '').replace('\n', '').replace('\t', '')),
                'size': filepath.stat().st_size
            }
            
            return stats
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 text_analyzer.py <file>")
        print("\nAnalyzes a text file and displays statistics")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    print(f"Analyzing: {filepath}")
    print("-" * 40)
    
    stats = analyze_file(filepath)
    
    if stats:
        print(f"Lines:              {stats['lines']:,}")
        print(f"Words:              {stats['words']:,}")
        print(f"Characters:         {stats['chars']:,}")
        print(f"Chars (no spaces):  {stats['chars_no_spaces']:,}")
        print(f"File size:          {stats['size']:,} bytes")
    else:
        print("Failed to analyze file")
        sys.exit(1)


if __name__ == '__main__':
    main()
