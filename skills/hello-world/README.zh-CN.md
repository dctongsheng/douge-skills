# Hello World Skill — 入门示例

> 用于验证 Agent Skills 是否安装成功，并了解最小 Skill 目录结构。

[English](./README.md) · [返回集合首页](../../README.zh-CN.md)

## 功能

激活后，Agent 会向你问好，并可运行一行 Node 脚本做端到端检查：

```bash
node skills/hello-world/scripts/hello.mjs
# Hello, World! — hello-world skill is working.
```

## 安装

```bash
npx skills add dctongsheng/douge-skills -s hello-world
```

## 目录结构

```text
hello-world/
├── SKILL.md
├── manifest.json
├── README.md
├── README.zh-CN.md
└── scripts/
    └── hello.mjs
```
