# Installation Guide

## Prerequisites

- Python 3.7 or higher
- tkinter (GUI library)

## Check Python Version
```bash
python --version
# or
python3 --version
```

## Platform-Specific Installation

### Windows

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"
   - tkinter is included automatically

2. **Clone the repository**:
```bash
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
```

3. **Create virtual environment** (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate
```

4. **Install dependencies** (if using PyInstaller):
```bash
pip install -r requirements.txt
```

5. **Run the application**:
```bash
python wordlist_gen.py
```

### Linux (Ubuntu/Debian)

1. **Install Python and tkinter**:
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-tk python3-venv
```

2. **Clone the repository**:
```bash
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
```

3. **Create virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Install dependencies** (if using PyInstaller):
```bash
pip install -r requirements.txt
```

5. **Run the application**:
```bash
python3 wordlist_gen.py
```

### Linux (Fedora)
```bash
sudo dnf install python3 python3-pip python3-tkinter
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
python3 -m venv venv
source venv/bin/activate
python3 wordlist_gen.py
```

### Linux (Arch)
```bash
sudo pacman -S python python-pip tk
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
python -m venv venv
source venv/bin/activate
python wordlist_gen.py
```

### macOS

1. **Install Python** (if not already installed):
```bash
# Using Homebrew
brew install python3
# tkinter is included
```

2. **Clone and run**:
```bash
git clone https://github.com/yourusername/wordlist-gen-by-g.git
cd wordlist-gen-by-g
python3 -m venv venv
source venv/bin/activate
python3 wordlist_gen.py
```

## Troubleshooting

### "No module named 'tkinter'"

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

**Windows/macOS:**
Reinstall Python from python.org ensuring you select "tcl/tk and IDLE" during installation.

### "Permission denied" on Linux
```bash
chmod +x wordlist_gen.py
```

### Python not found

Make sure Python is in your PATH:
```bash
# Windows
where python

# Linux/macOS
which python3
```

## Building Standalone Executable

### Windows
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Wordlist_Gen_By_G" --icon=icon.ico wordlist_gen.py
```

The executable will be in `dist/Wordlist_Gen_By_G.exe`

### Linux
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Wordlist_Gen_By_G" wordlist_gen.py
```

The executable will be in `dist/Wordlist_Gen_By_G`

### macOS
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Wordlist_Gen_By_G" wordlist_gen.py
```

The app will be in `dist/Wordlist_Gen_By_G`

## Quick Start Script

Save this as `setup.sh` (Linux/macOS):
```bash
#!/bin/bash
echo "Setting up Wordlist_Gen By G..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies if requirements.txt exists
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "Setup complete! Run 'source venv/bin/activate' then 'python3 wordlist_gen.py'"
```

Save this as `setup.bat` (Windows):
```batch
@echo off
echo Setting up Wordlist_Gen By G...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install it first.
    exit /b 1
)

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies if requirements.txt exists
if exist requirements.txt (
    pip install -r requirements.txt
)

echo Setup complete! Run 'venv\Scripts\activate.bat' then 'python wordlist_gen.py'
```

## Running Without Installation

If you just want to run it without any setup:
```bash
# Linux/macOS
python3 wordlist_gen.py

# Windows
python wordlist_gen.py
```

This works because the application has no external dependencies!
