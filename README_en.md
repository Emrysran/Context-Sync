# Context-Sync (ctx) 🧠

[简体中文](./README.md) | [English](./README_en.md)

**Context-Sync** is an ultra-lightweight CLI tool designed to break down "context silos" between different AI assistants (e.g., Cursor, Claude, Windsurf, ChatGPT).

It captures your current development context—Git changes, file tree, environment info, and terminal history—in one click and syncs it instantly to any AI, giving them the same "God view" as you in seconds.

---

## 🔥 Why Context-Sync?

When swapping between different AI tools (e.g., coding in Cursor, architecting in Claude Projects, debugging in ChatGPT), the biggest pain is repeatedly explaining "what I just did."

**Context-Sync solves this in one second:**
- **Cross-AI Compatibility**: Works with any text-based AI assistant.
- **No More Repeating Yourself**: One-click summary of your latest progress. Just paste and resume.
- **Precision Context**: Give the AI only the most critical, real-time data.

---

## ✨ Core Features

- **🚀 One-Click Snapshot**: Sync all relevant context into a single file.
- **📋 Clipboard Integration (`--clip`)**: Sync directly to your clipboard. Just `Ctrl+V` to your AI.
- **🛡️ Privacy Guard**: Automatically masks API keys, Tokens, and sensitive data.
- **🌿 Git & Shell Context**: AI follows your logic via diffs and execution history.
- **🤖 AI Guidance**: Built-in prompt footer to guide the AI's next steps.

---

## 🚀 Quick Start (AI Syncing)

### 1. Install
```bash
git clone https://github.com/Emrysran/Context-Sync.git
cd Context-Sync && pip install .
```

### 2. Sync and Go
```bash
# Capture context and copy to clipboard
ctx sync --clip

# Best Practices for AI Tools:
# - Cursor: Use @Files to reference context_state.md in chat/composer.
# - Claude: Upload context_state.md to Project Knowledge.
# - ChatGPT: Just Ctrl+V; the report includes a built-in guide prompt.
```

---

## 🛠️ Advanced Commands

```bash
ctx sync -f x.py    # Include full content of specific files
ctx init           # Initialize local configuration (.ctx.json)
ctx clean          # Remove generated report files
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
