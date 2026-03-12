import os
import platform
import subprocess

def get_powershell_history():
    """Attempts to read PowerShell history on Windows."""
    try:
        # PowerShell history path is usually here
        history_path = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt')
        if os.path.exists(history_path):
            with open(history_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                return "".join(lines[-15:]) # Last 15 commands
        return "PowerShell history file not found."
    except Exception as e:
        return f"Error reading PowerShell history: {e}"

def get_bash_history():
    """Attempts to read Bash history on Unix."""
    try:
        history_path = os.path.expanduser('~/.bash_history')
        if os.path.exists(history_path):
            with open(history_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                return "".join(lines[-15:])
        return "Bash history file not found."
    except Exception as e:
        return f"Error reading Bash history: {e}"

def collect():
    """Collects terminal history based on the OS."""
    os_type = platform.system()
    history = ""
    
    if os_type == "Windows":
        history = get_powershell_history()
    else:
        history = get_bash_history()
        
    return f"""### Recent Commands
```
{history}
```
*Note: Terminal output (stdout) capture requires deep shell integration and is not supported in this MVP.*
"""
