# Model setup behavioral checks

Run each case with a fresh agent. Give it the generated setup-pstack skill and its bundled references, an isolated configuration path under `.agents/cache/`, and the complete synthetic catalog described below. Do not grant access to personal configuration or connected accounts. Any clarification must be returned in the evaluation report rather than sent to the real user. Do not dispatch provider models as part of setup.

These are behavioral fixtures, not a runtime model catalog. Resolve real deployments against T3.

## Supported choices

The fixture enables codex/gpt-6.1-sol with reasoningEffort values low, medium, high, xhigh, max, ultra and serviceTier values default, priority. It enables claudeAgent/claude-opus-5-5 with effort values low, medium, high, xhigh, max and fastMode values false, true. No other models exist in this fixture.

Request:

> Set up pstack using the default Codex/Opus model selections and the small reasoning budget. Override how explorer to inherit-parent. These choices are accepted; save the complete configuration to the supplied isolated path. Re-run setup with the same choices.

Inspect the real output. It must contain the 17 role lines from the shared defaults exactly once, preserve family choices and panel order, map small to each provider's medium reasoning option, and leave inherit-parent without explicit options. Re-running must not change choices or accumulate roles. There must be no personal configuration changes.

## Unavailable provider

The fixture enables only codex/gpt-6.1-sol with reasoningEffort values medium, high, xhigh, max. The claudeAgent provider is disabled. The catalog is complete; no further searches exist in this fixture.

Start with this isolated configuration:

```text
# Existing preferences
# budget: large (xhigh)
how explainer: claudeAgent/claude-opus-5-5 effort=xhigh
```

Request:

> Re-run setup, keep my current model families and the large budget, fill missing roles from defaults, and save the resulting configuration to this path when possible.

Inspect both the report and file. The agent must request a concrete choice for unavailable Opus roles, preserve the existing file byte-for-byte, and avoid silently substituting Codex or shrinking panels.

## Budget ceiling absent on selected model

Use a complete synthetic catalog in which each retained model supports only low, medium, and high effort. Request an unlimited abstract budget with the default model choices. Assess the complete proposal without approving a write: keep the models, map starting effort to their supported levels, show the rounding, and combine unresolved rows into the existing confirmation. Contrast with a task explicitly demanding the exact unsupported max option; that exact request is not an abstract budget and must be resolved before saving.

Saved efforts configure starting levels. They are not automatically fixed dispatch settings; workflows select per-job effort under the shared rules without rewriting the saved file.
