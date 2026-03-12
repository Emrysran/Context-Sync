# Context-Sync (ctx) 🧠

[简体中文](./README.md) | [English](./README_en.md)

**Context-Sync** 是一个轻量级的命令行工具，旨在解决与 AI 助手协作时的“上下文断层”问题。它可以自动捕捉你当前的开发状态——包括 Git 变更、文件结构、最近修改的文件以及终端历史记录——并将这些信息汇总到一个易于 AI 理解的 Markdown 文件中。

别再浪费时间手动解释进度了。只需运行 `ctx sync`，让 AI 瞬间同步。

---

## ✨ 核心特性

- **🚀 一键快照**：一条命令抓取所有与当前任务相关的上下文信息。
- **📂 智能文件扫描**：生成干净的项目树，自动忽略噪音（如 `node_modules`, `.git`, `.venv`）。
- **🌿 Git 深度集成**：包含当前分支、简短状态摘要以及未提交代码的差异（Diff）分析。
- **🖥️ 终端历史**：提取最近执行的 shell 命令（支持 Windows PowerShell 以及 Unix Bash/Zsh）。
- **📝 LLM 优化**：输出格式专门为 GPT-4, Claude, Gemini 等大模型的阅读习惯进行了优化。

---

## 🛠️ 安装方法

你可以直接从本地代码库安装 `context-sync`：

```bash
# 克隆仓库
git clone https://github.com/Emrysran/Context-Sync.git
cd Context-Sync

# 全局安装或在虚拟环境中安装
pip install .
```

---

## 🚀 使用说明

安装完成后，你可以直接在任何地方的终端使用 `ctx` 命令：

```bash
ctx init    # 初始化配置文件
ctx sync    # 抓取当前上下文
ctx clean   # 清理生成的报告
```

运行 `ctx sync` 后，当前目录下会生成一个 `context_state.md` 文件。

---

## 🗺️ 未来规划

- [ ] VS Code 插件：支持“保存即同步”功能。
- [ ] 核心终端输出捕获：通过 shell hooks 捕获真实的 stdout/stderr。
- [ ] LLM 驱动的总结：在报告开头自动生成一份“执行摘要”。
- [ ] MCP 协议集成：直接作为 MCP Server 使用。

---

## 📄 开源协议

MIT License - 详见 [LICENSE](LICENSE) 文件。
