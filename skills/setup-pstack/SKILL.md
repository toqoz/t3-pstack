---
name: setup-pstack
description: Configure pstack role models and reasoning preferences for T3. Detect available providers and models, then save the accepted choices to a plain Markdown file. Use for /setup-pstack, "configure pstack models", "pstack budget", or changing model choices.
---

# Setup pstack

Configure T3 model choices per role and save them as plain Markdown. Read `references/models.md` for the shared defaults and configuration location. The defaults use Codex for implementation and exploration, and Opus for judgment and synthesis.

## Steps

### 1. Detect available models

Read `references/models.md` for the shared role defaults, Markdown configuration location, budgets, and model-choice notation. Follow the host's current catalog and permission rules. Setup configures preferences; it must not dispatch test agents or install hooks.

Use `orchestrator_capabilities` to discover enabled providers, their models, and supported options. Its short list is not exhaustive. Search a missing requested model through the host's catalog discovery mechanism before declaring it unavailable, following the host's limits on repeated capability calls. Do not infer availability from a model name appearing in the defaults or an existing configuration. The aliases `inherit-parent` and `auto` need no catalog entry.

If discovery cannot establish availability, name the gap. Do not ask for credentials in chat, install a provider, or substitute another model without the user's choice.

### 2. Load current state

Read the configuration path defined in `references/models.md`, or an explicitly requested path. If it exists, preserve the user's model families, panels, aliases, and explicit options as the starting choices. Missing roles use the shared defaults. Show retired or unknown role lines and propose removing them when presenting the result. Do not silently discard unclear prose, conflicting entries, or unsupported options.

Keep a copy of the original content in memory until validation and the requested changes are complete. Do not write a file merely to discover the available models or prepare a proposal.

### 3. Budget, map, and confirm

Ask the user for the desired reasoning budget, naming the current one. Accept a budget and role choices already specified in the request without asking again. Offer unlimited (max), large (xhigh), medium (high), and small (medium). With no existing configuration, large matches the defaults.

Keep current model families, lists, aliases, and non-reasoning options unless the user changes them. For a requested budget change, propose the corresponding starting reasoning option for every explicit model, including panel entries. Saved efforts are job-adjustable starting levels; exact fixed settings specified for the current task remain authoritative. Resolve provider-specific option IDs and values through T3's live catalog. Map a budget-derived effort to the same selected model's highest supported level at or below the target and mark rounding in the full proposal. Mark a role needing a choice only when no supported level qualifies. Do not change providers/models to achieve a level. An explicitly requested exact option must be honored or resolved with the user. Combine unresolved rows into the existing proposal confirmation instead of asking separately for every row. Aliases retain the parent settings.

Show all roles with their proposed choices, budget, configuration path, unsupported entries, and any retired lines to remove. Distinguish defaults from overrides and future roles from currently generated workflows. Ask the user to accept the concrete proposal or change specific roles, offering available catalog models and aliases. If the request already specifies a complete concrete configuration and authorizes saving it, proceed without a redundant confirmation.

Panel roles and the cross-judge pool retain the behavior described in `references/models.md`. An unavailable panel member requires an explicit choice; do not shrink the panel silently.

### 4. Validate

Check every explicit provider/model pair and option against the current T3 catalog, including models retained from the previous configuration. The aliases `inherit-parent` and `auto` always pass and must not carry explicit target options. Unknown roles, malformed or ambiguous lines, unavailable models, disabled providers, and invalid options require a correction or explicit user choice before writing. Validate roles that the user retains even if their workflows are not generated yet.

### 5. Write the rule

Save the accepted choices to the Markdown configuration path defined in `references/models.md`, or the path explicitly requested by the user. Write a short explanatory header, the selected budget, and one plain role line per role using the names and notation from the shared defaults. Preserve explicit model options and ordered lists. No JSON, YAML frontmatter, always-applied host rule, or custom parser is needed.

Write only after the proposal has been accepted or the user has already authorized that concrete configuration. Follow the host's source-of-truth rules for managed configuration; do not overwrite a generated symlink or bypass configuration management. Replace the file as one completed write, keeping the previous file intact if validation fails. Re-running setup with the same choices must produce the same choices without accumulating duplicate lines.

### 6. Confirm

Read the saved file back and compare it with the accepted choices. Report its exact path and the selected budget, and say that subsequent workflow invocations read this file. Re-running setup changes the preferences; there is no background updater or session hook.

### 7. Offer a verification skill (optional)

Check whether the project has a way to drive the real app for proof (a `verify-*` skill, or an existing harness). If not, offer once: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work? I can generate one with /create-verification-skill." On yes, read and follow this distribution’s `../create-verification-skill/SKILL.md`. On no, move on without pushing.

### 8. Offer a formal verification skill (optional)

Check whether the project already has a formal verification skill (a project skill that runs a model checker, a proof, or another verifier against the code). If not, offer once: "want a formal verification skill, so agents can prove a key property of your code holds in every case in scope, not only the cases tests reach? I can generate one with /create-formal-verification-skill." On yes, read and follow this distribution’s `../create-formal-verification-skill/SKILL.md`. On no, move on without pushing.
