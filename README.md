# Context-Sync (ctx) 🧠

[![GitHub License](https://img.shields.io/github/license/username/repo?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)](https://www.python.org/)

**Context-Sync** is a lightweight CLI tool designed to solve the "context gap" when working with AI assistants. It captures your current development state—Git changes, file structure, recently modified files, and terminal history—and compiles them into a single, LLM-friendly Markdown file.

Stop explaining your progress. Just `ctx sync` and let the AI catch up.

---

## ✨ Features

- **🚀 One-Click Snapshot**: Capture everything relevant to your task in one command.
- **📂 Smart File Scanning**: Generates a clean project tree, ignoring noise (like `node_modules`, `.git`, `.venv`).
- **🌿 Git Integration**: Includes current branch, short status, and a summarized diff of your uncommitted changes.
- **🖥️ Terminal History**: Pulls your most recent shell commands (PowerShell support on Windows, Bash/Zsh on Unix).
- **📝 LLM-Optimized**: Output is formatted specifically for high readability by models like GPT-4, Claude, and Gemini.

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/context-sync.git
cd context-sync

# Install dependencies
pip install click
```

---

## 🚀 Usage

Simply run the following command in your project root:

```bash
python ctx.py sync
```

This will generate a `context_state.md` file. You can then:
- **Copy-paste** the content into your next AI chat.
- **Upload** the file to a "Knowledge Base" or "Project Context" in your AI IDE (like Cursor).

### Options

- `--output`, `-o`: Specify a different output filename (default: `context_state.md`).

---

## 💡 Why use this?

When switching between tasks or IDEs, AI assistants often lose the "nuance" of what you just did. `ctx` provides the ground truth:
- "What files did I touch in the last 15 minutes?"
- "What was the exact error message I saw in the terminal?"
- "What code did I just change but haven't committed yet?"

---

## 🗺️ Roadmap

- [ ] VS Code Extension for "Sync on Save".
- [ ] Support for capturing actual terminal stdout/stderr via shell hooks.
- [ ] LLM-powered "Executive Summary" generator.
- [ ] Integration with MCP (Model Context Protocol).

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
