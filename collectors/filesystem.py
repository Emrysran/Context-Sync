import os
import time

def get_file_tree(startpath='.', max_depth=2):
    """Returns a string representation of the file tree."""
    tree = []
    startpath = os.path.abspath(startpath)
    prefix_len = len(startpath.rstrip(os.sep)) + 1
    
    for root, dirs, files in os.walk(startpath):
        # Exclude common noise directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'node_modules', '.next', 'out', 'dist', 'build']]
        
        level = root[prefix_len:].count(os.sep)
        if level >= max_depth:
            continue
            
        indent = '  ' * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        
        sub_indent = '  ' * (level + 1)
        # Limit the number of files per directory to avoid huge output
        limit = 10
        for i, f in enumerate(files):
            if i < limit:
                tree.append(f"{sub_indent}{f}")
            else:
                tree.append(f"{sub_indent}... ({len(files) - limit} more files)")
                break
                
    return "\n".join(tree)

def get_recently_modified_files(minutes=60):
    """Returns a list of files modified within the last N minutes."""
    current_time = time.time()
    modified_files = []
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'node_modules']]
        for file in files:
            path = os.path.join(root, file)
            try:
                mtime = os.path.getmtime(path)
                if (current_time - mtime) < (minutes * 60):
                    modified_files.append(f"{path} ({int((current_time - mtime) / 60)} mins ago)")
            except (OSError, FileNotFoundError):
                continue
                
    return "\n".join(modified_files) if modified_files else "No files modified recently."

def collect():
    """Collects all filesystem-related context."""
    tree = get_file_tree()
    modified = get_recently_modified_files()
    
    return f"""### File Tree (Depth limit: 2)
```
{tree}
```

### Recently Modified Files (Last 60 mins)
```
{modified}
```
"""
