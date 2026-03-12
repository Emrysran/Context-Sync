# Context-Sync (ctx) 🧠

[简体中文](./README.md) | [English](./README_en.md)

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

You can install `context-sync` directly from the local directory:

```bash
# Clone the repository
git clone https://github.com/Emrysran/Context-Sync.git
cd Context-Sync

# Install the package globally or in a virtual environment
pip install .
```

---

## 🚀 Usage

Once installed, the `ctx` command will be available globally in your terminal:

```bash
ctx init    # Initialize config file
ctx sync    # Capture context
ctx clean   # Clean up generated report
```

This will generate a `context_state.md` file in your current directory.

---

## 🗺️ Roadmap

- [ ] VS Code Extension for "Sync on Save".
- [ ] Support for capturing actual terminal stdout/stderr via shell hooks.
- [ ] LLM-powered "Executive Summary" generator.
- [ ] Integration with MCP (Model Context Protocol).

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
