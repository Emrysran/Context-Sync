import subprocess

def get_git_status():
    """Returns the output of `git status`."""
    try:
        result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Error: Could not retrieve git status (is this a git repo?)"
    except FileNotFoundError:
        return "Error: git command not found."

def get_git_diff():
    """Returns a summary of `git diff`."""
    try:
        # Get diff summary first
        result = subprocess.run(['git', 'diff', '--stat'], capture_output=True, text=True, check=True)
        summary = result.stdout.strip()
        
        # Also get a bit of the actual diff if it's small
        diff_content = subprocess.run(['git', 'diff', '--unified=0'], capture_output=True, text=True, check=True).stdout
        if len(diff_content) > 1000:
            diff_content = diff_content[:1000] + "\n... (diff truncated)"
            
        return f"Summary:\n{summary}\n\nRecent Diffs:\n```diff\n{diff_content}\n```"
    except subprocess.CalledProcessError:
        return "Error: Could not retrieve git diff."
    except FileNotFoundError:
        return "Error: git command not found."

def get_recent_commits(n=5):
    """Returns the last N commits."""
    try:
        result = subprocess.run(['git', 'log', f'-n {n}', '--oneline'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "Error: Could not retrieve git logs."

def collect():
    """Collects all git-related context."""
    status = get_git_status()
    diff = get_git_diff()
    commits = get_recent_commits()
    
    return f"""### Git Status
```
{status}
```

### Git Diff Summary
{diff}

### Recent Commits
```
{commits}
```
"""
