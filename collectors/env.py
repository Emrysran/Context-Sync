import platform
import sys
import subprocess
import os

def get_python_info():
    """Returns version and virtualenv info."""
    return f"Python {sys.version.split()[0]} (Executable: {sys.executable})"

def get_node_info():
    """Attempts to get Node.js version."""
    try:
        res = subprocess.run(['node', '-v'], capture_output=True, text=True, check=True)
        return f"Node.js {res.stdout.strip()}"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "Node.js not found"

def get_env_vars():
    """Captures relevant environment variables."""
    relevant = ['VIRTUAL_ENV', 'CONDA_DEFAULT_ENV', 'PATH']
    info = []
    for var in relevant:
        val = os.environ.get(var)
        if val:
            if var == 'PATH':
                # Just get the first few entries to avoid bloat
                val = ";".join(val.split(os.pathsep)[:3]) + "..."
            info.append(f"{var}={val}")
    return "\n".join(info)

def collect():
    """Collects system and dev environment info."""
    return f"""### System Environment
- **OS**: {platform.system()} {platform.release()} ({platform.machine()})
- **Python**: {get_python_info()}
- **Node**: {get_node_info()}

### Active Environment Variables
```
{get_env_vars()}
```
"""
