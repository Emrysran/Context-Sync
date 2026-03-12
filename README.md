# Context-Sync (ctx) 🧠

[简体中文](./README.md) | [English](./README_en.md)

**Context-Sync** 是一个极致轻量级的命令行工具，旨在打破不同 AI 助手（如 Cursor, Claude, Windsurf, ChatGPT）之间的“上下文孤岛”。

它可以一键捕捉你当前的开发脉络——Git 变更、文件树、环境信息和终端历史——并瞬间同步给任何 AI，让它们在几秒钟内获得与你完全一致的“上帝视角”。

---

## 🔥 为何需要它？

当你频繁在不同 AI 工具间切换时（例如：在 Cursor 里写代码，去 Claude Projects 整理架构，在 ChatGPT 调试报错），最头疼的就是重复解释“我刚才做了什么”。

**Context-Sync 让你一秒解决这个问题：**
- **横跨所有 AI**：生成的报告是标准的 Markdown，适配任何支持文本输入的 AI 助手。
- **告别重复解释**：一键生成最新进度摘要，直接粘贴即可继续聊天。
- **精准投喂**：避免 AI 漫无目的地读取整个仓库，只给它最关键、最实时的上下文。

---

## ✨ 核心特性

- **🚀 一键快照**：同步所有相关上下文至单个文件。
- **📋 剪贴板同步 (`--clip`)**：运行即复制，直接 `Ctrl+V` 给 AI。
- **🛡️ 隐私保护**：自动扫描并打码 API Key、Token 等敏感信息。
- **🌿 Git & 终端记录**：包含代码差异和执行记录，AI 能秒读你的思路。
- **🤖 AI 自动导引**：报告末尾自带指令，引导 AI 快速给出下一步方案。

---

## 🚀 快速开始 (Quick AI Sync)

### 1. 安装
```bash
git clone https://github.com/Emrysran/Context-Sync.git
cd Context-Sync && pip install .
```

### 2. 同步并使用
```bash
# 生成快照并存入剪贴板
ctx sync --clip

# 针对不同 AI 的最佳实践：
# - Cursor: 在聊天框中使用 @Files 引用 context_state.md
# - Claude: 将生成的 md 文件上传到 Project Knowledge
# - ChatGPT: 直接 Ctrl+V 粘贴即可，报告末尾已自带引导 Prompt
```

---

## 🛠️ 进阶命令

```bash
ctx sync -f x.py    # 让 AI 重点关注特定文件的全文内容
ctx init           # 初始化本地配置文件 (.ctx.json)
ctx clean          # 清理生成的报告文件
```

---

## 📄 开源协议

MIT License - 详见 [LICENSE](LICENSE) 文件。
