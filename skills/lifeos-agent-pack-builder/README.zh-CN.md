# lifeos-agent-pack-builder

用于创建并导入 LifeOS Platform 角色 Agent Pack。

这个 Skill 会指导 Agent 先研究人物或角色素材，再把素材转化成现代 LifeOS
身份，生成 `docs/agent-packs/<pack_id>.md`，校验其中的
`AgentPackConfig` JSON，并把 Pack 导入本地 LifeOS 服务。

## 适合场景

- 新增 LifeOS 人物、角色、persona 或 Agent Pack
- 将虚构角色、历史人物或公开资料转化成现代 LifeOS 身份
- 生成包含素材摘要、人物提示词和 `AgentPackConfig` JSON 的
  `docs/agent-packs/*.md`
- 导入生成好的 Pack，并创建匹配的 World

## 包含文件

- [`SKILL.md`](./SKILL.md)：Agent 工作流说明
- [`references/agent-pack-checklist.md`](./references/agent-pack-checklist.md)：
  Agent Pack 字段检查清单
- [`scripts/import_agent_pack.py`](./scripts/import_agent_pack.py)：从 Pack
  Markdown 中提取第一个 fenced JSON 并导入 LifeOS 的辅助脚本
- [`agents/openai.yaml`](./agents/openai.yaml)：参考 Agent 配置

## 导入辅助脚本

在 LifeOS 项目中创建 Pack Markdown 后运行：

```bash
python /path/to/skill/scripts/import_agent_pack.py docs/agent-packs/nanzhi.md \
  --server http://127.0.0.1:8000 \
  --api-key "${LIFEOS_API_KEY:-dev-lifeos-key-change-me}"
```

如果只想导入 Agent Pack、不创建 World，可以加 `--no-world`。
