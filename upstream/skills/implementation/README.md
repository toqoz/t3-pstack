# Designing, implementing, and proving changes

✅ changed · - unchanged · Pending held. [Source and update guide](../../README.md)

| Skill | T3 | Patch | Design |
|---|---|---|---|
| [architect](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/architect/SKILL.md) | ✅ | - | - |
| [benchmark-checklist](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/benchmark-checklist/SKILL.md) | ✅ | - | - |
| [blast-radius](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/blast-radius/SKILL.md) | - | - | - |
| [create-formal-verification-skill](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/create-formal-verification-skill/SKILL.md) | - | - | - |
| [create-verification-skill](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/create-verification-skill/SKILL.md) | ✅ | - | - |
| [maintain-formal-verification-skill](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/maintain-formal-verification-skill/SKILL.md) | - | - | - |
| [maintain-verification-skill](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/maintain-verification-skill/SKILL.md) | ✅ | - | - |
| [make-bot-ui](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/make-bot-ui/SKILL.md) | Omitted | - | - |
| [statechart](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/statechart/SKILL.md) | - | - | - |
| [tdd](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/tdd/SKILL.md) | - | - | - |
| [typescript-best-practices](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/typescript-best-practices/SKILL.md) | - | - | - |

## architect

- **T3:** Use the configured design panel through arena and give candidates their own role and absolute reference paths.

[how-integrate-arena.md](../orchestration/how-integrate-arena.md)

## benchmark-checklist

- **T3:** Use available observation/profiling tools and keep measurement self-contained without requiring unbundled PR/performance playbooks.

[how-integrate-benchmark-checklist.md](how-integrate-benchmark-checklist.md)

## create-verification-skill / maintain-verification-skill

- **T3:** Replace `.cursor/skills/` with `.agents/skills/`; retain upstream procedures and templates.

[how-integrate-verification-skills.md](how-integrate-verification-skills.md)



## Omitted

- **make-bot-ui:** It assumes Grok Bot’s long lifecycle, which differs from T3 Code’s; this workflow seems unlikely to fit T3 Code well. User decision; no agent wake was verified.
