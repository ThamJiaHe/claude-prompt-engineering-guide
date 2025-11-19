<!-- Language Selector -->
<div align="center">

📖 **选择您的语言：**

[English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md)

</div>

---

# 📦 Claude 技能集合

欢迎来到Claude技能库！该目录包含可重用的模块化任务包，通过特定领域的知识、程序和工作流来扩展Claude的功能。

---

## 🎯 什么是 Claude 技能？

**Claude 技能**是结构化的指令、示例和资源的集合，教导Claude在特定领域执行可重复的工作流。它们设计用于：

- ✅ **模块化** — 自包含式，专注于特定任务
- ✅ **可重用** — 可在不同的对话和项目中使用
- ✅ **可组合** — 多项技能可以无缝协作
- ✅ **可发现** — Claude自动识别相关技能
- ✅ **高效** — 分阶段披露防止上下文膨胀

### 为什么使用技能？

技能可以帮助您：
- 📚 **标准化流程** 整个团队
- 🎯 **确保一致性** 输出和工作流
- ⏱️ **节省时间** 通过预构建的程序
- 🔧 **自定义Claude** 用于您的特定领域
- 📈 **提高质量** 通过经过验证的模式

---

## 📚 本集合中的可用技能

我们维护一个全面的**22个生产就绪技能**集合，涵盖开发、基础设施、测试和部署：

### Web 开发和全栈

| 技能名称 | 目的 | 状态 |
|---------|------|------|
| [NextJS 应用路由器](./examples/nextjs-app-router-skill.md) | 掌握Next.js 15+与App Router、服务器组件和高级模式 | ✅ 可用 |
| [Tailwind 设计系统](./examples/tailwind-design-system-skill.md) | 使用Tailwind CSS构建设计系统 | ✅ 可用 |
| [NextAuth 认证](./examples/nextauth-authentication-skill.md) | 使用NextAuth.js实现安全认证 | ✅ 可用 |
| [API 开发](./examples/api-development-skill.md) | 设计并构建可扩展的REST/GraphQL API | ✅ 可用 |

### 后端和基础设施

| 技能名称 | 目的 | 状态 |
|---------|------|------|
| [AWS 云基础设施](./examples/aws-cloud-infrastructure-skill.md) | 使用最佳实践设计和部署AWS基础设施 | ✅ 可用 |
| [谷歌云平台](./examples/google-cloud-platform-skill.md) | 掌握GCP服务和云架构 | ✅ 可用 |
| [Neon 无服务器](./examples/neon-serverless-skill.md) | 使用Neon数据库构建无服务器应用 | ✅ 可用 |
| [Prisma ORM](./examples/prisma-orm-skill.md) | 掌握Prisma进行数据库操作和迁移 | ✅ 可用 |

### 测试和质量保证

| 技能名称 | 目的 | 状态 |
|---------|------|------|
| [测试框架](./examples/testing-skill.md) | 构建全面的测试策略 | ✅ 可用 |
| [Vitest 单元测试](./examples/vitest-unit-testing-skill.md) | 掌握Vitest进行单元测试 | ✅ 可用 |
| [Playwright E2E 测试](./examples/playwright-e2e-testing-skill.md) | 使用Playwright实现端到端测试 | ✅ 可用 |
| [代码审查](./examples/code-review.md) | 进行全面的代码审查 | ✅ 可用 |

### DevOps 和部署

| 技能名称 | 目的 | 状态 |
|---------|------|------|
| [Vercel 部署](./examples/vercel-deployment-skill.md) | 在Vercel上部署应用程序 | ✅ 可用 |
| [数据库迁移](./examples/database-migrations.md) | 执行安全的数据库迁移 | ✅ 可用 |
| [监控和日志](./examples/monitoring-logging-skill.md) | 实现生产监控和日志记录 | ✅ 可用 |
| [Git 工作流](./examples/git-workflow-skill.md) | 掌握Git工作流和协作 | ✅ 可用 |

### 开发标准和最佳实践

| 技能名称 | 目的 | 状态 |
|---------|------|------|
| [TypeScript 标准](./examples/typescript-standards.md) | 编写生产级TypeScript代码 | ✅ 可用 |
| [性能优化](./examples/performance-optimization-skill.md) | 优化应用程序性能 | ✅ 可用 |
| [SEO 优化](./examples/seo-optimization-skill.md) | 实现SEO最佳实践 | ✅ 可用 |
| [安全和合规](./examples/security-compliance.md) | 实现安全最佳实践 | ✅ 可用 |
| [可访问性和UX](./examples/accessibility-ux.md) | 构建可访问、用户友好的应用程序 | ✅ 可用 |
| [客户反馈分析](./examples/example-feedback-analyzer.md) | 分析客户反馈并识别主题 | ✅ 可用 |

**可用技能总数：22个** | **全部生产就绪** ✅

要探索任何技能，请点击上面的链接或浏览[examples/](./examples/)目录。

---

## 🚀 如何使用技能

### 方法1：Claude.ai Web界面

1. **启用技能** 在 设置 → 功能 → 技能切换
2. **粘贴技能内容** 到新对话中
3. **在提示中引用技能**
4. **让Claude自动使用** 相关任务

### 方法2：Claude Desktop应用

1. **打开Claude Desktop**
2. **转到设置** → **功能** → **技能**
3. **启用技能** 切换
4. **自然地使用** 在对话中

示例：
```
I need to analyze customer feedback and create an analysis document.
Can you use the feedback analysis skill to help with this?
```

### 方法3：Claude Code (CLI)

技能在Claude Code中与`/skills`命令配合使用：

```bash
# 查看可用技能
/skills list

# 使用特定技能
/skills load feedback-analysis
```

### 方法4：API 集成

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# 在系统提示中包含技能指令
system_prompt = """
You are a document analyst with the following skill available:
[Skill Content Here]
Use this skill when analyzing documents.
"""

response = client.messages.create(
    model="claude-opus-4-20250514",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "Analyze this customer feedback using the skill"
        }
    ]
)

print(response.content[0].text)
```

---

## 🛠️ 如何创建您自己的技能

### 技能结构要求

每个技能都应遵循此标准结构：

```markdown
# 技能名称
此技能的一行简述。

## 目的
详细说明：
- 技能帮助Claude完成什么
- 何时使用它
- 预期成果

## 元数据
- **名称：** skill-name (kebab-case)
- **版本：** 1.0.0
- **作者：** 您的名字
- **创建日期：** YYYY-MM-DD
- **更新日期：** YYYY-MM-DD
- **类别：** (例如：分析、写作、代码审查)

## 安装
不同环境的说明

### Claude.ai / Desktop
- 复制技能内容
- 粘贴到对话中
- 在提示中引用

### Claude Code
CLI使用特定说明

## 使用

### 基本用法
简单的技能使用示例

### 高级用法
更复杂的场景

## 配置
任何可用的自定义选项

## 示例
技能实际应用的真实示例

## 依赖
任何要求或先决条件

## 故障排除
常见问题和解决方案

## 许可证
此技能的许可证信息
```

### 创建技能的分步指南

#### 1. **定义目标**
```
技能：客户反馈分析器

目的：帮助Claude系统地分析客户反馈
并识别主题、情感和可行的见解。
```

#### 2. **记录程序**
```
程序：
1. 仔细阅读所有反馈
2. 识别反复出现的主题
3. 按情感分类（正面/负面/中立）
4. 提取可行的见解
5. 汇总发现
```

#### 3. **提供示例**
```
输入示例：
"客户说：'产品质量很好但交货速度慢'"

输出示例：
- 正面主题：产品质量
- 负面主题：交货速度
- 情感：混合（产品正面，服务负面）
- 行动项：改进交货时间
```

#### 4. **添加配置选项**
```
配置：
- 包括情感分数？(是/否)
- 按主题或反馈分组？(主题/反馈)
- 输出格式？(markdown/json/结构化)
```

#### 5. **测试和改进**
在对话中使用您的技能并根据结果进行改进。

---

## 📋 技能模板

这是一个完整的模板，您可以复制并自定义：

```markdown
# [技能名称]
[一行描述]

## 目的
[详细说明目标和使用案例]

## 元数据
- **名称：** [skill-name]
- **版本：** 1.0.0
- **作者：** [您的名字]
- **创建日期：** [YYYY-MM-DD]
- **更新日期：** [YYYY-MM-DD]
- **类别：** [类别]

## 安装

### Claude.ai/Desktop
1. 复制此技能
2. 粘贴到新对话中
3. 在提示中引用

### Claude Code
```bash
# 将技能内容添加到 ~/.claude/skills/
```

## 使用

### 基本用法
```
显示基本用法的示例提示
```

### 高级用法
```
显示更复杂用法的示例
```

## 配置
[任何配置选项]

## 示例

### 示例1
[真实世界示例]

### 示例2
[另一个示例]

## 依赖
[任何要求]

## 故障排除

### 常见问题
**解决方案：** [如何解决]

## 注意
[附加信息]

## 许可证
[许可证 - 通常是MIT]
```

---

## ✅ 最佳实践

### 创建技能时

- **具体说明** — 专注于一项清晰的任务或工作流
- **包括示例** — 显示Claude应该做什么
- **记录步骤** — 将复杂流程分解为清晰的步骤
- **彻底测试** — 验证技能按预期工作
- **添加元数据** — 包括版本、作者和创建日期
- **版本控制** — 做出更改时更新版本号

### 使用技能时

- **明确引用** — "使用[技能名称]来..."
- **提供背景** — 解释为什么使用该技能
- **具体说明输出** — 指定所需格式
- **给出示例** — 显示所需的风格或结构
- **迭代** — 根据结果进行改进

---

## 🤝 贡献

我们期待您的贡献！要添加您的技能：

### 流程

1. **创建您的技能**
   - 遵循技能模板和结构
   - 彻底测试
   - 记录所有部分

2. **准备提交**
   - 保存为 `skills/examples/[skill-name].md`
   - 确保格式正确
   - 包括所有元数据

3. **提交**
   - 使用您的技能创建拉取请求
   - 包括它做什么的描述
   - 分享关于使用它的任何反馈

4. **审查和合并**
   - 维护者将测试您的技能
   - 如需要提供反馈
   - 批准后合并！

### 贡献指南

- ✅ **请** 遵循标准模板
- ✅ **请** 包括全面的示例
- ✅ **请** 在提交前测试您的技能
- ✅ **请** 记录依赖
- ❌ **不要** 包括敏感信息
- ❌ **不要** 提交未测试的技能
- ❌ **不要** 使用不解释的复杂术语

---

## 🎓 学习资源

### 更好地理解技能

- [Claude技能指南](../docs/skills-guide.md) — 全面的技能文档
- [提示词工程指南](../Claude-Prompt-Guide.md) — 如何有效地提示Claude
- [示例目录](./examples/) — 真实技能示例

### 类似概念

- **Superpowers** — 用户创建的脚本和自动化
- **MCP服务器** — 模型上下文协议集成
- **模板** — 可重用的提示结构

---

## 📞 支持和问题

### 如何获取帮助

1. **检查示例** — 在`skills/examples/`中查找类似技能
2. **阅读文档** — 请参阅[docs/skills-guide.md](../docs/skills-guide.md)
3. **浏览问题** — 检查GitHub Issues查找常见问题
4. **询问社区** — 创建新讨论话题

### 常见问题

**问：我可以使用其他人的技能吗？**
答：是的！复制任何技能并在您的对话中使用。

**问：我可以修改技能吗？**
答：绝对可以。为您的需求自定义它。

**问：我如何知道技能是否有效？**
答：使用提供的示例进行测试。如果Claude使用您列出的程序，它就能工作。

**问：技能可以一起使用吗？**
答：是的！技能可以组合并相互引用。

---

## 📊 技能统计

- **总技能数：** (社区贡献)
- **最受欢迎：** (最常用)
- **最新技能：** (最近添加)

---

## 🔗 相关资源

- [Claude提示词工程指南](../Claude-Prompt-Guide.md)
- [技能实现指南](../docs/skills-guide.md)
- [MCP集成指南](../docs/mcp-integration.md)
- [Superpowers插件指南](../docs/superpowers-guide.md)

---

## 📝 许可证

本集合中的所有技能均在**MIT许可证**下提供，除非另有说明。请参阅单个技能文件以获取具体的许可证信息。

---

## 🙏 致谢

- **Anthropic** 开发Claude技能
- **社区贡献者** 分享他们的技能
- **您** 使用和贡献此集合！

---

**最后更新：** 2025年11月19日
**位置：** Claude提示词工程指南库
**维护者：** 社区贡献者

