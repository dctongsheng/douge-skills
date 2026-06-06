---
name: lifeos-agent-pack-builder
description: Create and import LifeOS Platform character Agent Packs from public research and docs/modern-agent-pack-template.md. Use when the user asks to add a new LifeOS人物/角色/persona/Agent Pack, generate a docs/agent-packs Markdown file, convert fictional or historical material into a modern LifeOS identity, or import the generated AgentPackConfig JSON into the local LifeOS database and create the corresponding World.
---

# LifeOS Agent Pack Builder

## Core Workflow

1. Read the repository instructions and inspect the local LifeOS project structure before editing.
2. If the character comes from a movie, novel, history, legend, or other non-modern source, browse the web first and cite the public sources used. Treat source material as research, not as the agent's current real-world identity.
3. Read `docs/modern-agent-pack-template.md` and any existing `docs/agent-packs/*.md` examples. Follow the repository's current location and style.
4. Generate `docs/agent-packs/<pack_id>.md` with:
   - `素材来源摘要`
   - `人物提示词`
   - `AgentPackConfig JSON`
5. Keep the modern identity original and realistic. Put source-character events into `前世记忆`, dream fragments, personality, values, or reaction patterns.
6. Validate the JSON block as `AgentPackConfig` when the repo package is available.
7. Import the Markdown file into LifeOS and create a matching World.
8. Verify via `/packs` and `/worlds` that the expected pack and world exist. Run focused tests when available.

## Research Rules

- Browse when the user requests web research, when the character/source is current, or when details could have changed.
- Prefer official, reputable, or primary sources. For entertainment characters, use interviews, news reports, production pages, and encyclopedic summaries.
- Summarize sources in your own words and include URLs in the generated Markdown.
- Do not copy long source passages.

## Pack-Writing Rules

- `pack_id`: lowercase ASCII slug, e.g. `nanzhi`.
- `display_name` and `identity.agent_name`: user-facing Chinese name when appropriate.
- `identity_code`: short stable code, e.g. `#NANZHI-029`.
- `runtime_modules.dreams`: normally `true` for character companions.
- `is_preset`: `false` unless adding a built-in preset.
- `base_system_prompt`: `null` for structured packs.
- Avoid machine-specific paths, secrets, API keys, personal tokens, or unsupported real-life claims.
- Update `CHANGELOG.md` when the repository says user-visible changes must be recorded.

For a compact field checklist, read `references/agent-pack-checklist.md`.

## Import Script

Use `scripts/import_agent_pack.py` after creating the Markdown file:

```bash
python /path/to/skill/scripts/import_agent_pack.py docs/agent-packs/nanzhi.md \
  --server http://127.0.0.1:8000 \
  --api-key "${LIFEOS_API_KEY:-dev-lifeos-key-change-me}"
```

The script extracts the first fenced `json` block, posts it to `/packs`, and creates a World using the pack display name. Add `--no-world` when only the Pack should be imported.

If the pack or world already exists, the script reports it and exits without duplicating that object.

## Verification

Before saying the task is complete, run fresh checks:

```bash
python /path/to/skill/scripts/import_agent_pack.py docs/agent-packs/<pack_id>.md --no-world
uv run pytest tests/test_modern_agent_pack_template.py
```

Then query `/packs` and `/worlds` or use the script output to confirm the new character is present.

For open-source character packs, ensure generated `docs/agent-packs/*.md` files are visible in `git status` and committed with the related workflow changes. Keep private or experimental character packs outside the repository.
