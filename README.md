# My Personal Scripts

A collection of utility scripts for personal use.

## Structure

```
my_scripts/
├── bash/           # Bash shell scripts
├── python/         # Python scripts
├── utils/          # General utilities
├── docs/           # Documentation
└── README.md       # This file
```

## Available Scripts

### Bash Scripts

#### backup.sh
Creates timestamped backups of files.

```bash
# Usage
./bash/backup.sh <source_file> [destination_directory]

# Example
./bash/backup.sh important.txt ~/backups
```

#### sysinfo.sh
Displays quick system information including hostname, OS, CPU, memory, and disk usage.

```bash
# Usage
./bash/sysinfo.sh
```

### Python Scripts

#### file_organizer.py
Organizes files in a directory by their extensions into separate folders.

```bash
# Usage
python3 python/file_organizer.py <directory> [--dry-run]

# Example (dry run to preview)
python3 python/file_organizer.py ~/Downloads --dry-run

# Actual organization
python3 python/file_organizer.py ~/Downloads
```

#### text_analyzer.py
Analyzes text files and provides statistics (lines, words, characters).

```bash
# Usage
python3 python/text_analyzer.py <file>

# Example
python3 python/text_analyzer.py README.md
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/naonaoaya/my_scripts.git
cd my_scripts
```

2. Make scripts executable (if needed):
```bash
chmod +x bash/*.sh python/*.py
```

## Requirements

- **Bash scripts**: Bash shell (usually pre-installed on Linux/Mac)
- **Python scripts**: Python 3.6 or higher

## Adding New Scripts

When adding new scripts:

1. Place them in the appropriate directory (bash/, python/, etc.)
2. Make them executable: `chmod +x script_name`
3. Add a shebang line at the top (e.g., `#!/bin/bash` or `#!/usr/bin/env python3`)
4. Update this README with usage instructions

## License

MIT License - See [LICENSE](LICENSE) file for details.