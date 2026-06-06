# Agent Pack Checklist

Use this checklist while generating LifeOS character packs.

## Markdown Shape

- `# <name> Agent Pack`
- `## 素材来源摘要`
- `## 人物提示词`
- fenced `md` block containing the full persona prompt
- `## AgentPackConfig JSON`
- fenced `json` block containing the database config

## Required JSON Fields

- `pack_id`
- `display_name`
- `identity.agent_name`
- `identity.codename`
- `identity.identity_code`
- `identity.backstory`
- `identity.relationship_stance`
- `identity.core_values`
- `behavior_profile.speech_style`
- `behavior_profile.forbidden_patterns`
- `behavior_profile.emotion_rules`
- `behavior_profile.work_habits`
- `behavior_profile.addressing_rules`
- `behavior_profile.inner_voice_prompt`
- `behavior_trajectory.milestones`
- `behavior_trajectory.proactive_style`
- `behavior_trajectory.reaction_patterns`
- `world_rules.timezone`
- `world_rules.work_hours`
- `world_rules.locations`
- `world_rules.custom_facts`
- `runtime_modules`
- `is_preset`
- `base_system_prompt`

## Modernization Pattern

- Current identity: modern, original, realistic, not the source character.
- Source material: previous-life memory, dream fragment, values, relationship patterns, and emotional reflexes.
- Conflict rule: current reality beats source memory.
- Safety rule: no secrets, no fake real-world credentials, no unsupported real-life relationships or assets.

## Import Payload

The `/packs` API accepts the `AgentPackConfig` fields except `is_preset`; the service sets custom packs to `false`.

Create a World after pack import:

```json
{
  "pack_id": "<pack_id>",
  "display_name": "<display_name>"
}
```
