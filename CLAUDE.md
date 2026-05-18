# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 项目概述

**Douge Skills** 是一个面向 Claude Code、Cursor、Codex 等多个 AI 编程代理的 Agent Skills 集合仓库。每个 Skill 是一个独立的功能模块，遵循 `SKILL.md` 规范（YAML frontmatter + 指令文档）。

**架构特点**：
- Monorepo 结构，每个 Skill 独立版本号（遵循 SemVer）
- 零 npm 依赖的纯 ESM Node 发版工具链
- 多语言 README（英文/中文/日文）
- GitHub Actions 自动化发版与验证

---

## 核心目录结构

```
skills/                    # 所有 Skill 源码
├── web-video-presentation/
├── web-design-engineer/
├── gpt-image-2/
└── kb-retriever/

scripts/release/           # 发版工具链（纯 ESM，零依赖）
├── cut-release.mjs        # 交互式发版主入口
├── pack-skill.mjs         # skill → 钉版本 .zip + .sha256
├── update-readme.mjs      # 重写 README 的 Download 链接
└── list-skills.mjs        # 查看 manifest + 结构状态

.claude-plugin/
└── marketplace.json       # Claude Code 插件市场清单

.github/workflows/
├── release-skill.yml      # tag 触发的单 Skill 发版
└── validate-skills.yml    # PR 守门
```

---

## 常用命令

### 验证与检查

```bash
npm run list              # 列出所有 Skill + manifest 状态
npm run validate          # CI 同步检查（list + pack:all + readme:check）
```

### 发版

```bash
npm run release           # 交互式发版（99% 场景）
npm run release:dry       # 预览发版计划，不执行
npm run release -- --yes  # 跳过确认直接发版
```

### 打包与 README

```bash
npm run pack:all          # 把所有 Skill 打到 dist/release/
npm run readme:sync       # 重写 README 下载链接
npm run readme:check      # 检查 README 链接是否过期
```

---

## Skill 标准结构

每个 Skill 必须包含：

```
<skill-name>/
├── SKILL.md            # 必需：YAML frontmatter + Agent 指令
├── manifest.json       # 必需：name/version/category/description/compat
├── README.md           # 用户文档（英文）
├── README.zh-CN.md     # 用户文档（中文）
├── references/         # 可选：Agent 按需加载的扩展文档
├── scripts/            # 可选：确定性可执行代码
└── assets/             # 可选：模板、字体、图标
```

**关键约束**：
- 文件夹名、`manifest.json#name`、`SKILL.md` frontmatter `name` **必须完全一致**
- `manifest.json#version` 必须与 release tag 的版本号一致
- 每个 Skill 独立 SemVer，不跟随仓库统一版本

---

## 发版工作流

1. 运行 `npm run release`
2. 脚本检测每个 Skill 的变更，提示 bump 类型（patch/minor/major）
3. 自动：更新 manifest → 同步 README → commit → 打 tag → 原子 push
4. `release-skill.yml` CI 触发：生成 .zip/.sha256 → 创建 GitHub Release → 同步 README 回 main

**Tag 格式**：`<skill-name>-v<semver>`（如 `web-design-engineer-v1.1.0`）

---

## 添加新 Skill

1. 创建 `skills/<new-name>/`，包含 `SKILL.md` + `manifest.json`
2. 在根目录多语言 README 的对应区块添加 DOWNLOAD marker：
   ```markdown
   <!-- DOWNLOAD:<new-name>:start --><!-- DOWNLOAD:<new-name>:end -->
   ```
3. 运行 `npm run readme:sync` 填充占位符
4. `npm run validate` 确保通过
5. 合并后 `npm run release` 发首版

---

## 插件市场配置

在 `.claude-plugin/marketplace.json` 中定义 plugin packs：

```json
{
  "name": "web-design-skills",
  "description": "Skills for visual / front-end design work.",
  "skills": ["./skills/web-design-engineer"]
}
```

用户可通过 `/plugin marketplace add dctongsheng/douge-skills` 安装。

---

## 常见问题

| 现象 | 解决 |
|---|---|
| `validate-skills` 失败：README out of date | `npm run readme:sync` 后 commit |
| `release-skill` 失败：Version drift | 确保 `manifest.json#version` 与 tag 一致 |
| 新增 Skill 后 CI 失败 | 检查 `manifest.json` 必需字段是否存在 |

---

## 参考文档

- [agentskills.io](https://agentskills.io) — SKILL.md 规范
- [Anthropic 官方示例](https://github.com/anthropics/skills)
- [贡献指南](./CONTRIBUTING.zh-CN.md) — 发版流程、版本规则、CI 详情
