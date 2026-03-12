# AI 助手集成指南 (AI Integration Guide) 🤖

本指南介绍了如何将 `Context-Sync` 生成的报告高效地喂给各种 AI 编程工具。

---

## 🚀 Cursor 集成

Cursor 是目前最推荐的集成方式。

### 方法 1：使用 `@Files` (推荐)
1. 运行 `ctx sync` 生成 `context_state.md`。
2. 在 Cursor 的聊天框 (Ctrl+L) 或 Composer (Ctrl+I) 中，输入 `@` 并选择 `context_state.md`。
3. AI 将瞬间理解你当前的代码改动、项目结构和最近的报错。

### 方法 2：结合 .cursorrules
在你的项目根目录创建或编辑 `.cursorrules` 文件，加入以下指令：
> *“在开始任何编码任务前，请优先阅读 `context_state.md` 文件（如果存在）。它包含了项目最新的 Git 差异、文件树和我的终端执行历史，能帮助你更准确地理解我的意图。”*

---

## 📝 Claude / ChatGPT 集成

针对网页版 AI 助手：

1. 运行 `ctx sync`。
2. 如果使用 **Claude Projects**：
   - 将 `context_state.md` 上传到项目的 **Project Knowledge** 中。
3. 如果使用普通对话：
   - 直接将 `context_state.md` 的内容全部复制并粘贴给 AI。
   - 我们的报告末尾自带 **AI 指引 Prompt**，AI 会自动总结你的进度。

---

## 🌊 Windsurf / VS Code Copilot

1. 保持 `context_state.md` 在编辑器中处于打开状态。
2. AI 通常会自动索引打开的文件上下文。
3. 在提问时明确提到：“请基于 `context_state.md` 里的最新同步状态给我建议。”

---

##💡 最佳实践

*   **任务切换前同步**：当你准备停下手里工作或者需要 AI 接管时，运行一次 `ctx sync`。
*   **遇到报错时同步**：如果你在终端遇到复杂报错，运行 `ctx sync`。生成的报告会包含你最近执行的错误命令，方便 AI 帮你 Debug。
*   **配合 .ctx.json**：通过自定义 `ai_guidance_prompt`，你可以让 AI 以特定的格式（如 Todo List）回复你。
