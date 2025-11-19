<!-- Language Selector -->
<div align="center">

📖 **选择您的语言：**

[English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md)

</div>

---

# 🎯 Claude 提示词工程指南

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/claude-prompt-engineering-guide?style=social)](https://github.com/yourusername/claude-prompt-engineering-guide)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Nov%202025-blue)](https://github.com/yourusername/claude-prompt-engineering-guide)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 🚀 **编写专业 Claude Standard 提示词的最终指南，涵盖 Opus、Sonnet 和 Haiku 模型**，全面覆盖 MCP、技能、Superpowers 以及高级提示词工程技术。

---

## 📖 目录

- [概述](#概述)
- [功能](#功能)
- [快速开始](#快速开始)
- [技能集合](#技能集合)
- [核心内容](#核心内容)
- [文档结构](#文档结构)
- [关键部分](#关键部分)
- [示例与模板](#示例与模板)
- [贡献](#贡献)
- [许可](#许可)
- [致谢](#致谢)

---

## 🌟 概述

本综合指南综合了 **Anthropic 官方最佳实践** 与 **真实世界提示词工程技术**，针对 Claude 4.x 模型。无论您通过网页界面、桌面应用、Claude Code CLI 还是 API 使用 Claude，本指南都提供了经过验证的模式和框架，帮助您充分发挥 Claude 的能力。

### 本指南适合谁？

- **开发者** - 使用 Claude API 构建应用程序
- **提示词工程师** - 为团队设计生产级提示词
- **AI 工程师** - 将 Claude 集成到工作流中
- **Claude Code 用户** - 利用代理功能
- **研究人员** - 探索 Claude 的推理能力
- **任何人** - 想要掌握专业提示词工程

### 为什么这很重要

Claude 4.x 模型功能非常强大，但要充分利用其功能需要 **结构化提示词**。本指南提供：

✅ **Anthropic 10 组件框架** — 专业提示词的官方结构
✅ **Claude 4.x 最佳实践** — 针对 Opus、Sonnet 和 Haiku 模型的具体技术
✅ **高级技术** — XML 标签、思维链、扩展思维等
✅ **实际应用模式** — 代码审查、业务分析、研究、文档创建
✅ **工具集成** — MCP、技能、Superpowers 和 Perplexity 集成
✅ **环境指南** — Claude.ai、Desktop、Code 和 API 的最优方法

---

## ✨ 功能

本指南包含：

- 📚 **1000+ 行全面参考资料**
- 🏗️ **官方 10 组件提示词框架** 附详细说明
- 💡 **5 个高级提示词模式** 附完整示例
- 🛠️ **工具集成指南**（MCP、技能、Superpowers）
- 🎯 **环境特定优化**（网页、桌面、CLI、API）
- 📋 **提示词模板**（最小化和综合）
- 🔍 **真实用例** 跨多个领域
- ⚙️ **模型对比表**（Opus vs Sonnet vs Haiku）
- 📊 **定价和性能指南**
- 🚀 **长期推理最佳实践**
- 🧠 **思维链和扩展思维技术**
- 🔐 **安全性和提示词注入防护**

---

## 🚀 快速开始

### 1. 阅读主要指南

从综合的 **[Claude 提示词工程指南](./Claude-Prompt-Guide.md)** 开始，涵盖：
- Claude 的架构和理念
- 10 组件框架
- Claude 4.x 最佳实践
- 高级技术
- 完整的模式示例

### 2. 选择您的环境

- **使用 Claude.ai？** → 阅读 [Claude.ai 优化指南](./docs/quick-start.md)
- **使用 Claude Desktop？** → 阅读 [MCP 集成指南](./docs/mcp-integration.md)
- **使用 Claude Code CLI？** → 阅读 [Claude Code 指南](./docs/claude-code-guide.md)
- **使用 API 构建？** → 阅读 [API 集成指南](./docs/api-guide.md)

### 3. 查找您的用例示例

- [编码任务](./docs/examples/coding-tasks.md)
- [研究与分析](./docs/examples/research-tasks.md)
- [业务分析](./docs/examples/business-analysis.md)
- [文档创建](./docs/examples/document-creation.md)

### 4. 使用模板

定制我们的提示词模板：
- [最小化提示词模板](./templates/minimal-prompt-template.md) — 快速项目
- [综合提示词模板](./templates/comprehensive-prompt-template.md) — 复杂任务

### 5. 探索 Claude 技能

在我们不断增长的集合中发现可重用的技能包：
- **[技能目录](./skills/)** — 浏览可用技能并贡献您自己的技能
- **[技能模板](./skills/examples/example-feedback-analyzer.md)** — 示例反馈分析器技能
- **学习创建技能** — 完整文档见 [skills/README.md](./skills/README.md)

---

## 📦 技能集合

### 什么是 Claude 技能？

**Claude 技能**是模块化、可重用的任务包，用特定领域的知识、流程和工作流扩展 Claude 的能力。它们的设计目的是：

- ✅ **模块化** — 自包含，专注于特定任务
- ✅ **可重用** — 可在不同对话和项目中使用
- ✅ **可组合** — 多个技能可以无缝协作
- ✅ **可发现** — Claude 自动识别相关技能
- ✅ **高效** — 渐进式披露防止上下文过载

### 可用技能

我们的综合集合包括 **22 个生产就绪的技能**：

**网页开发**：NextJS App Router、Tailwind Design System、NextAuth、API Development
**基础设施**：AWS、GCP、Neon Serverless、Prisma ORM
**测试**：Vitest、Playwright E2E、代码审查、测试框架
**DevOps**：Vercel Deployment、Database Migrations、Monitoring & Logging、Git Workflow
**标准**：TypeScript、Performance、SEO、Security、Accessibility、Feedback Analysis

[→ 查看全部 22 个技能](./skills/)

### 快速链接

- 📚 **[完整技能文档](./skills/README.md)** — 了解所有关于技能的信息
- 🛠️ **[如何创建技能](./skills/README.md#-如何创建您自己的技能)** — 分步指南
- 📋 **[技能模板](./skills/examples/example-feedback-analyzer.md)** — 用作起点
- 🤝 **[贡献您的技能](./skills/README.md#-贡献)** — 与社区分享

### 为什么使用技能？

技能帮助您：

- 📚 **跨团队标准化流程**
- 🎯 **确保输出和工作流的一致性**
- ⏱️ **通过预构建的流程节省时间**
- 🔧 **为您的特定领域定制 Claude**
- 📈 **通过经过验证的模式改进质量**

### 开始使用

1. **浏览** [skills/examples/](./skills/examples/) 中的可用技能
2. **复制** 技能以在您的对话中使用
3. **引用** 提示词中的技能："使用 [Skill Name] 来..."
4. **创建** 您自己的技能，遵循 [我们的模板](./skills/README.md#-技能模板)
5. **贡献** 您的技能回馈社区

---

## 📚 核心内容

### [Claude 提示词工程指南](./Claude-Prompt-Guide.md)

包含以下内容的综合参考文档：

#### 第 1 部分：理解 Claude 的架构
- Claude 的角色和理念
- 知识截止日期
- Claude 如何处理提示词

#### 第 2 部分：Claude 模型概览
- **Claude Opus 4.1** — 最强大的模型
- **Claude Sonnet 4.5** — 性能和成本平衡
- **Claude Haiku 4.5** — 快速高效
- 定价和性能对比

#### 第 3 部分：系统提示词 vs 用户提示词
- 何时使用系统提示词
- 何时使用用户提示词
- 各自的最佳实践

#### 第 4 部分：Anthropic 官方提示词结构
- **10 组件框架**（官方结构）
- 组件说明和示例
- 为什么这个结构有效

#### 第 5 部分：Claude 4.x 最佳实践
- 明确说明指令
- 添加上下文以改进性能
- 长期推理技术
- 状态跟踪最佳实践
- 工具使用模式
- 输出格式控制
- 并行工具调用
- 研究方法
- 避免幻觉

#### 第 6 部分：高级技术
- XML 标签用于结构化
- 思维链提示词
- 扩展思维
- 提示词链接
- 角色提示词

#### 第 7 部分：工具、MCP、技能和 Superpowers
- 模型上下文协议（MCP）
- MCP 文件系统服务器
- Claude 技能系统
- Superpowers 插件
- Perplexity MCP 集成

#### 第 8 部分：不同环境的提示词工程
- Claude.ai 网页界面
- Claude Desktop 应用
- Claude Code（CLI/VS Code）
- Claude API（直接集成）

#### 第 9 部分：常见模式和示例
- 模式 1：技术代码审查
- 模式 2：数据业务分析
- 模式 3：长期编码任务
- 模式 4：研究与综合
- 模式 5：使用技能创建文档

#### 第 10 部分：快速参考卡
- 最小化提示词模板
- 综合提示词模板
- 快速检查清单

---

## 📖 文档结构

```
claude-prompt-engineering-guide/
├── README.md                          # 此文件
├── Claude-Prompt-Guide.md             # 主综合指南
├── LICENSE                            # MIT 许可
├── CONTRIBUTING.md                    # 贡献指南
├── CHANGELOG.md                       # 版本历史
├── .gitignore                         # Git 忽略规则
│
├── docs/                              # 附加文档
│   ├── quick-start.md                # 快速开始指南
│   ├── mcp-integration.md            # MCP 设置和使用
│   ├── skills-guide.md               # 技能文档
│   ├── superpowers-guide.md          # Superpowers 插件指南
│   ├── api-guide.md                  # API 集成指南
│   ├── claude-code-guide.md          # Claude Code CLI 指南
│   └── examples/                      # 真实示例
│       ├── coding-tasks.md
│       ├── research-tasks.md
│       ├── business-analysis.md
│       └── document-creation.md
│
├── templates/                         # 即用型模板
│   ├── minimal-prompt-template.md    # 快速模板
│   └── comprehensive-prompt-template.md # 完整模板
│
├── skills/                            # Claude 技能集合
│   ├── README.md                     # 技能指南和文档
│   └── examples/                      # 示例技能
│       └── example-feedback-analyzer.md # 客户反馈分析器技能
│
└── .github/                          # GitHub 配置
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 🎯 关键部分

### 10 组件框架（官方）

这是 **Anthropic 推荐的专业提示词结构**：

1. **任务上下文** — WHO 和 WHAT（定义 Claude 的角色）
2. **语气上下文** — HOW（沟通风格）
3. **背景数据** — 相关上下文和文档
4. **详细任务描述** — 明确的需求和规则
5. **示例** — 1-3 个所需输出示例
6. **对话历史** — 相关的先前上下文
7. **即时任务描述** — 现在需要的具体可交付成果
8. **逐步思考** — 鼓励深思熟虑的推理
9. **输出格式** — 明确定义结构
10. **预填充响应** — 开始 Claude 的响应以指导风格

### Claude 4.x 最佳实践

📌 **明确** — Claude 4.x 响应精确指令
📌 **添加上下文** — 解释为什么，而不仅仅是什么
📌 **使用示例** — 展示，不只是讲述
📌 **鼓励推理** — 思维链大大提高质量
📌 **定义输出格式** — 明确说明结构和风格
📌 **利用并行工具** — 同时执行多个操作

---

## 📋 示例与模板

### 真实应用模式

1. **技术代码审查** — 审查代码的安全性、性能和最佳实践
2. **业务分析** — 分析指标并提供战略建议
3. **长期编码** — 跨多个上下文窗口构建完整功能
4. **研究与综合** — 进行全面的竞争分析
5. **文档创建** — 使用技能集成构建演示文稿

### 即用型模板

- **最小化模板** — 快速任务的基本组件
- **综合模板** — 复杂项目的完整框架

查看 [templates/](./templates/) 目录获取完整示例。

---

## 🤝 贡献

我们欢迎贡献！无论您是：
- 📝 添加新示例或模式
- 🐛 报告问题或建议改进
- 📚 改进文档
- 🎯 分享您自己的提示词工程发现

查看 [CONTRIBUTING.md](./CONTRIBUTING.md) 获取详细指南。

---

## 📜 许可

本项目根据 **MIT 许可** 授权 — 详见 [LICENSE](./LICENSE)。

Claude 提示词工程指南综合了来自 Anthropic 文档和开源社区资源的公开信息。

---

## 🙏 致谢

**创建时间**：2025 年 11 月 19 日
**位置**：新加坡
**目的**：专业 Claude 提示词工程的深度研究综合

### 鸣谢

- **Anthropic** 为 Claude 和综合文档
- **Anthropic 团队** 为 10 组件框架和最佳实践
- **开源社区** 为 MCP、技能和 Superpowers 生态
- **Claude 用户和开发者** 为真实应用模式发现

---

## 📞 支持与问题

### 需要帮助？

- 📖 **阅读指南** — 从 [Claude-Prompt-Guide.md](./Claude-Prompt-Guide.md) 开始
- 📚 **探索示例** — 查看 [docs/examples/](./docs/examples/)
- 🎯 **使用模板** — 定制一个 [模板](./templates/)

### 报告问题

发现错误或有建议？[开启一个问题](https://github.com/yourusername/claude-prompt-engineering-guide/issues)，包含：
- 问题的清晰描述
- 示例（如适用）
- 建议的改进（可选）

### 贡献

想改进本指南？查看 [CONTRIBUTING.md](./CONTRIBUTING.md) 获取流程。

---

## 🚀 开始使用

1. **克隆此仓库**
   ```bash
   git clone https://github.com/yourusername/claude-prompt-engineering-guide.git
   cd claude-prompt-engineering-guide
   ```

2. **从主指南开始**
   ```bash
   # 阅读综合指南
   cat Claude-Prompt-Guide.md
   ```

3. **选择您的路径**
   - 初次接触 Claude？ → 从 [快速开始指南](./docs/quick-start.md) 开始
   - 构建应用？ → 阅读 [API 指南](./docs/api-guide.md)
   - 想要模式？ → 浏览 [示例](./docs/examples/)

4. **选择一个模板**
   - 快速项目？ → [最小化模板](./templates/minimal-prompt-template.md)
   - 复杂任务？ → [综合模板](./templates/comprehensive-prompt-template.md)

---

## 📊 统计

- **页面**：1000+ 行综合参考
- **模式**：5 个真实提示词示例
- **模板**：2 个生产就绪的模板
- **示例**：15+ 个跨不同领域的用例
- **覆盖**：Claude Opus、Sonnet、Haiku、API、Desktop、CLI、Web

---

## 🌐 相关资源

### 官方 Anthropic

- [提示词工程指南](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Claude API 文档](https://docs.anthropic.com)
- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code)
- [系统提示词指南](https://docs.anthropic.com/en/release-notes/system-prompts)

### 社区

- [模型上下文协议](https://modelcontextprotocol.io)
- [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks)
- [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills)
- [Superpowers 插件](https://github.com/obra/superpowers-chrome)

---

<div align="center">

**为 Claude 社区用心打造 ❤️**

[⭐ 如果对您有帮助，请给这个仓库加星](https://github.com/yourusername/claude-prompt-engineering-guide)！

[报告问题](https://github.com/yourusername/claude-prompt-engineering-guide/issues) • [贡献](./CONTRIBUTING.md) • [讨论](https://github.com/yourusername/claude-prompt-engineering-guide/discussions)

</div>
