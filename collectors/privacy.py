import re

# Common patterns for secrets
SECRET_PATTERNS = [
    (re.compile(r'sk-[a-zA-Z0-9]{32,}', re.IGNORECASE), "sk-MASKED"), # OpenAI-like keys
    (re.compile(r'ghp_[a-zA-Z0-9]{36,}', re.IGNORECASE), "ghp_MASKED"), # GitHub tokens
    (re.compile(r'AIzaSy[a-zA-Z0-9_-]{33}', re.IGNORECASE), "AIzaSyMASKED"), # Google API keys
    (re.compile(r'xox[baprs]-[a-zA-Z0-9-]{10,}', re.IGNORECASE), "xox-MASKED"), # Slack tokens
    (re.compile(r'sqp_[a-f0-9]{40}', re.IGNORECASE), "sqp_MASKED"), # SonarQube
    (re.compile(r'(password|secret|key|token|access_key|secret_key|api_key)\s*[:=]\s*["\']?([a-zA-Z0-9!@#$%^&*()_+=-]{8,})["\']?', re.IGNORECASE), r"\1: MASKED"), # Generic password/key patterns
]

def sanitize(content):
    """Sanitizes sensitive information from the content."""
    if not content:
        return content
        
    sanitized = content
    for pattern, replacement in SECRET_PATTERNS:
        # Use replacement string if it contains groups (like r"\1: MASKED"), 
        # otherwise use the simple string replacement.
        if isinstance(replacement, str) and "\\" in replacement:
             sanitized = pattern.sub(replacement, sanitized)
        else:
             sanitized = pattern.sub(replacement, sanitized)
             
    return sanitized
