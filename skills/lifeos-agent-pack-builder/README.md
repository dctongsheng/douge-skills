# lifeos-agent-pack-builder

Build and import LifeOS Platform character Agent Packs.

This skill guides an agent through researching a character or persona,
converting the source material into a modern LifeOS identity, writing a
`docs/agent-packs/<pack_id>.md` document, validating the embedded
`AgentPackConfig` JSON, and importing the pack into a local LifeOS server.

## Best for

- Creating a new LifeOS character, persona, or Agent Pack
- Turning fictional, historical, or public-source material into a modern
  LifeOS identity
- Generating `docs/agent-packs/*.md` files that include source summaries,
  prompts, and structured `AgentPackConfig` JSON
- Importing a generated pack and creating a matching World

## Included files

- [`SKILL.md`](./SKILL.md) — agent workflow instructions
- [`references/agent-pack-checklist.md`](./references/agent-pack-checklist.md) —
  compact field checklist for pack writing
- [`scripts/import_agent_pack.py`](./scripts/import_agent_pack.py) — helper for
  importing the first fenced JSON block from a pack Markdown file
- [`agents/openai.yaml`](./agents/openai.yaml) — reference agent configuration

## Import helper

After creating a pack Markdown file in a LifeOS project, run:

```bash
python /path/to/skill/scripts/import_agent_pack.py docs/agent-packs/nanzhi.md \
  --server http://127.0.0.1:8000 \
  --api-key "${LIFEOS_API_KEY:-dev-lifeos-key-change-me}"
```

Add `--no-world` when only the Agent Pack should be imported.
