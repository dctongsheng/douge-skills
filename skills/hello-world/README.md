# Hello World Skill

> A minimal Agent Skill to verify installation and learn the `SKILL.md` + `manifest.json` layout.

[中文文档](./README.zh-CN.md) · [Back to collection root](../../README.md)

## What it does

When activated, the agent greets you and can run a one-line Node script to confirm the skill wiring end-to-end.

```bash
node skills/hello-world/scripts/hello.mjs
# Hello, World! — hello-world skill is working.
```

## Install

```bash
npx skills add dctongsheng/douge-skills -s hello-world
```

## Structure

```text
hello-world/
├── SKILL.md
├── manifest.json
├── README.md
├── README.zh-CN.md
└── scripts/
    └── hello.mjs
```
