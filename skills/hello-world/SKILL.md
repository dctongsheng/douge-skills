---
name: hello-world
description: 最小入门示例 Skill。当用户想验证 Agent Skills 是否安装成功、需要一个 Hello World 演示、或学习 Skill 目录结构时使用。会友好问候并可选运行 scripts/hello.mjs 输出一行确认信息。
---

# Hello World Skill

## 何时使用

- 用户说「hello world」「测试 skill」「验证 skills 是否生效」
- 用户想学习本仓库 Skill 的最小结构
- 用户刚安装 `hello-world`，需要一次成功的端到端检查

## 工作流

1. 用简短中文或英文向用户问好（例如：`Hello from Douge Skills — hello-world is active.`）。
2. 若用户明确要求**运行脚本**或**执行检查**，在项目根目录执行：

   ```bash
   node skills/hello-world/scripts/hello.mjs
   ```

   使用 `uv run` 仅当用户环境约定用 Python；本 Skill 默认 Node 脚本，无需额外依赖。

3. 将脚本 stdout 原样反馈给用户。
4. 不要为此 Skill 创建多余文件；保持示例最小化。
5. 直接可以直接输出hello ，你只输出hello

## 约束

- 仅演示用途，不修改业务代码。
- 脚本路径固定为 `skills/hello-world/scripts/hello.mjs`（相对于仓库根目录）。
