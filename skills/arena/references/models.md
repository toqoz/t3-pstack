# Default model choices

These are T3 role preferences, not a catalog of available models. Resolve each choice against the live T3 catalog before use. Roles for skills not yet adopted reserve their upstream names; they do not make those workflows available.

The user configuration is a Markdown file at `$XDG_CONFIG_HOME/t3-pstack/models.md`, or `~/.config/t3-pstack/models.md` when XDG_CONFIG_HOME is unset or empty. Read it when running a workflow. An explicitly requested configuration path takes precedence. A missing role inherits this file's default. Conflicting or unclear lines require clarification rather than a guessed interpretation.

Write one role label per line. Existing labels such as `feature, refactoring` and `reflect judgment, divergent, synthesizer` are single shared role labels whose commas name related uses; do not split those labels into separate settings. Only the panel roles and cross-judge pool listed below accept comma-separated model lists. Every other role, including swarm workers, accepts exactly one choice; multiple choices require clarification and are not a fallback chain. A choice is `<providerInstanceId>/<modelId>` followed by any `optionId=value` pairs. Split provider and model at the first `/`; a model ID can contain further slashes. Map these to the T3 target's providerInstanceId, model, and options, preserving the catalog's value types such as booleans. Use the exact provider and option IDs from the live catalog. `inherit-parent` and `auto` mean omit the target and preserve the parent session's settings.

A budget describes the starting reasoning effort, not a spending cap or a fixed dispatch setting. Unlimited, large, medium, and small request max, xhigh, high, and medium respectively. Saved role effort options override the budget's starting level; otherwise a saved budget replaces the default effort. They remain starting preferences, even when setup writes an effort on every role line. Preserve other options during budget mapping; dispatch speed follows the job rules below. With no saved budget, use the default below.

At setup, map a budget-derived target to the selected model's supported effort levels: use the highest at or below the target and show any rounding in the full proposal. If none qualifies, mark that role for a choice in the same proposal. Do not change provider/model IDs to achieve a level. A user's explicitly requested exact option must be supported or resolved with the user; this is distinct from mapping an abstract budget.

The coordinator reads these preferences. A child receives its resolved role and task, not responsibility for selecting or spawning another model.

# budget: large (xhigh)

feature, refactoring: codex/gpt-6.1-sol reasoningEffort=xhigh
bug-fix: codex/gpt-6.1-sol reasoningEffort=xhigh
perf-issue: codex/gpt-6.1-sol reasoningEffort=xhigh
hillclimb: codex/gpt-6.1-sol reasoningEffort=xhigh
judgment and prose: claudeAgent/claude-opus-5-5 effort=xhigh
hardest tasks: claudeAgent/claude-opus-5-5 effort=xhigh
how explorer: codex/gpt-6.1-sol reasoningEffort=xhigh
how explainer: claudeAgent/claude-opus-5-5 effort=xhigh
why investigators: codex/gpt-6.1-sol reasoningEffort=xhigh
why synthesizer: claudeAgent/claude-opus-5-5 effort=xhigh
reflect tooling: codex/gpt-6.1-sol reasoningEffort=xhigh
reflect judgment, divergent, synthesizer: claudeAgent/claude-opus-5-5 effort=xhigh
arena runners: claudeAgent/claude-opus-5-5 effort=xhigh, codex/gpt-6.1-sol reasoningEffort=xhigh
arena cross-judge pool: claudeAgent/claude-opus-5-5 effort=xhigh, codex/gpt-6.1-sol reasoningEffort=xhigh
swarm workers: codex/gpt-6.1-sol reasoningEffort=xhigh
architect runners: claudeAgent/claude-opus-5-5 effort=xhigh, codex/gpt-6.1-sol reasoningEffort=xhigh
interrogate reviewers: claudeAgent/claude-opus-5-5 effort=xhigh, codex/gpt-6.1-sol reasoningEffort=xhigh

## Lists and model diversity

Arena runners, architect runners, and interrogate reviewers are panels. Their list length sets the initial number of participants, including alias entries. When arena or architect needs more design directions, cycle through configured entries in order and state the expanded count; do not add undeclared models. Arena cross-judge pool is an ordered candidate pool for one judge from a different model family than the parent. Aliases are not cross-judge candidates. Swarm workers is the default for each worker unless the task explicitly assigns a different model to a comparison arm.

Report unavailable panel entries and never substitute another provider/model without authorization. Follow the invoking workflow's original dropout or optional-stage behavior, reporting the missing coverage; do not add a global reduced-review approval gate. An explicitly required unavailable role remains an unmet task constraint. Different contexts on one model are not model diversity.

## Match effort and speed to the job

These rules preserve the pinned poteto-mode Subagents instructions referenced by the workflows; that does not require running poteto-mode. The user chose saved efforts as starting levels, with explicit fixed settings in the current task taking precedence.

1. Resolve the workflow's own model/role and starting effort. Recall selects its own fast/cheap mining model; it never borrows swarm's model role. An explicit current-task model request takes precedence over generic role assignments, including verification. An exact current-task effort/speed requirement stays fixed. The aliases auto/inherit-parent preserve the parent model and settings without adjustment.
2. Use the ordered effort ladder low, medium, high, xhigh, max. For the hardest or subtlest work, raise one step, capped at max. Otherwise lower one step for judgment/synthesis, or two or more for routine work, floored at low. State the job classification and final choice briefly. Ordinary work keeps its starting effort.
3. Map the derived level to supported options on the same selected model. Use the nearest supported ladder level (prefer the lower level on a tie) and disclose rounding. Never invent an option, switch models, silently inherit the parent, or repeatedly retry rejected options. Report explicitly requested unsupported settings or unavailable models without substitution. Resolve a replacement when needed; a workflow that already permits a dropout or skipped optional stage can proceed with that disclosed limitation.
4. Use standard speed for normal work, fast only for urgent work (red CI/trunk or a person blocked now). An explicitly delegated verification role is the upstream exception: use the configured swarm workers model and speed, while selecting effort for that job. Merely checking citations or evidence inside an explorer, investigator, explainer, or synthesizer does not change its designated workflow role. This exception does not apply to recall mining. If that role has no speed preference, keep the model's standard speed; do not invent acceleration from a provider name.
5. Resolve actual speed option IDs/values from the current host. Examples of host mappings are Codex serviceTier default/priority and Claude fastMode false/true. Use them only when the selected model exposes them. Omission can inherit settings, so explicitly select supported standard options when required. For Codex priority's Fast-mode meaning, see [official OpenAI documentation](https://developers.openai.com/api/docs/guides/fast-mode); this does not promise a measured latency or price. If a derived fast mode is unavailable on the same model, retain the available standard mode and report that limitation; an explicit fixed fast request requires a choice.
6. The parent resolves these settings and gives each child the final target. Native dispatch is allowed only within the host's provider/model/settings boundary; use delegate_task with target.options for explicit task settings or settings different from the parent. Follow the returned completion instructions. Do not rewrite saved preferences merely to make a per-job adjustment.
