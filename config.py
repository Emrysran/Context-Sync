import json
import os

DEFAULT_CONFIG = {
    "output_file": "context_state.md",
    "ignore_patterns": [".git", "__pycache__", ".venv", "node_modules", ".next", "out", "dist", "build", ".ctx"],
    "max_depth": 2,
    "terminal_history_limit": 15,
    "sanitize_secrets": True
}

def load_config():
    """Loads configuration from .ctx.json if it exists, otherwise returns defaults."""
    config_path = os.path.join(os.getcwd(), '.ctx.json')
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                config.update(user_config)
        except Exception as e:
            print(f"Warning: Failed to load .ctx.json: {e}")
            
    return config

def save_default_config():
    """Saves the default configuration to a .ctx.json file."""
    config_path = os.path.join(os.getcwd(), '.ctx.json')
    if not os.path.exists(config_path):
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return True
    return False
