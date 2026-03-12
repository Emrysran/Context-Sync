# Context-Sync (ctx) 🧠

[简体中文](./README.md) | [English](./README_en.md)

**Context-Sync** is an ultra-lightweight CLI tool designed to break down "context silos" between different AI assistants (e.g., Cursor, Claude, Windsurf, ChatGPT).

It captures your current development context—Git changes, file tree, environment info, and terminal history—in one click and syncs it instantly to any AI, giving them the same "God view" as you in seconds.

---

## 🔥 Why Context-Sync?

When swapping between different AI tools (e.g., coding in Cursor, architecting in Claude Projects, debugging in ChatGPT), the biggest pain is repeatedly explaining "what I just did."

**Context-Sync solves this in one second:**
- **Cross-AI Compatibility**: Generates standard Markdown that works with any text-based AI assistant.
- **No More Repeating Yourself**: One-click summary of your latest progress. Just paste and resume.
- **Precision Context**: Stop AI from wandering through your entire repo; give it only the most critical, real-time data.

---

## ✨ Core Features

- **🚀 One-Click Snapshot**: Capture all relevant context in one command.
- **📋 Clipboard Integration (`--clip`)**: Sync directly to your clipboard. Just `Ctrl+V` to your AI assistant.
- **🛡️ Privacy Guard**: Automatically detects and masks API keys, Tokens, and other sensitive data.
- **🌿 Git & Shell Context**: Includes uncommitted diffs and recent execution history so the AI can follow your logic.
- **🤖 AI Guidance**: Built-in prompt footer to guide the AI on how to handle the provided context.

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Emrysran/Context-Sync.git
cd Context-Sync

# Install (enables global 'ctx' command)
pip install .
```

---

## 🚀 Usage

```bash
ctx sync            # Capture and generate report
ctx sync --clip     # Capture directly to clipboard (Recommended!)
ctx sync -f x.py    # Include full content of specific files
ctx clean           # Remove generated reports
```

---

## 📘 Integration Guide

Want to use these reports more effectively in **Cursor**, **Claude**, or **Windsurf**?
Check out our [**AI Integration Guide (GUIDE_AI.md)**](./GUIDE_AI.md).

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
