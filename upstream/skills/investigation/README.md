# Understanding behavior and rationale

✅ changed · - unchanged · Pending held. [Source and update guide](../../README.md)

| Skill | T3 | Patch | Design |
|---|---|---|---|
| [how](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/how/SKILL.md) | ✅ | ✅ | - |
| [recall](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/recall/SKILL.md) | ✅ | - | - |
| [teach](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/teach/SKILL.md) | ✅ | ✅ | ✅ |
| [why](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/why/SKILL.md) | ✅ | - | - |

## how

- **T3:** Use shared model preferences, T3 dispatch, and available evidence tools while retaining independent explanation.
- **Patch:** Correct the explainer template so the simple path investigates directly instead of assuming explorers already ran.

[how-integrate-how.md](how-integrate-how.md)

## recall

- **T3:** Use scoped T3 history access and direct parallel miners, preserving upstream's fast/cheap model selection.

[how-integrate-recall.md](how-integrate-recall.md)

## teach

- **T3:** Coordinate how/why roles from the parent and display progressive visuals through current host tools.
- **Patch:** Clarify the blanket hedging instruction so prose editing preserves why's evidence-based confidence.
- **Design:** Teach in the user's requested language instead of requiring English.

[how-integrate-teach.md](how-integrate-teach.md)

## why

- **T3:** Use shared model preferences, T3 dispatch, and available evidence tools while retaining independent synthesis.

[how-integrate-why.md](how-integrate-why.md)
