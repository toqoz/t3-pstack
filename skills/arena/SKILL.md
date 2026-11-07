---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

# Arena

Open a todolist with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Read `references/models.md` and the user preferences at the path it defines. Resolve the `arena runners` panel against the live T3 catalog, respecting explicit task choices, saved starting preferences, and the job-based effort/speed rules there. Use the configured panel as the initial seats, preserving their order and explicit `auto` or `inherit-parent` entries. For multiple design directions, add runners by cycling through those configured entries in order and state the expanded count. For generation-bound tasks, repeated instances of an already configured model are allowed; name that choice. Do not invent new models. Never replace an unavailable provider/model without authorization; report the unavailable seat. Preserve the upstream dropout procedure and report missing coverage instead of adding a separate reduced-review approval gate. Independent contexts are not model diversity. For invocations including Phase C, establish the parent's actual family from host metadata when available; this check does not block candidate work merely because a judge may be unavailable. Interrogate skips Phase C and needs no judge check.
4. Give each candidate its own writable output, per the **separate-before-serializing-shared-state** principle skill. Use T3-managed isolated checkouts for independent code changes. For independent non-code artifacts, use owned directories under `.agents/cache/arena/<run>/candidate-<n>/`; keep accepted durable artifacts under `.agents/share/` or the task's agreed destination. State the baseline and inputs each candidate can actually read. Do not assume separate checkouts contain parent uncommitted changes.

For required uncommitted inputs, the coordinator captures an immutable input bundle under `.agents/cache/<workflow>/<run>/inputs/` before launching writers. Record the parent HEAD SHA and repository-relative scope. Save `git diff --cached --binary --full-index --no-ext-diff --no-textconv -- <scoped-paths>` as the staged patch, then `git diff --binary --full-index --no-ext-diff --no-textconv -- <scoped-paths>` as the unstaged patch. Include the explicitly scoped untracked files and relevant ignored artifacts, such as grounding sketches, as separate payloads. Do not collect unrelated ignored files or secrets. Record a manifest of index and working-tree states: each scoped path's kind, bytes SHA-256 (or symlink target), executable mode, and deleted/absent state. Include old and new paths for renames. Hash the patches and payloads too. Exclude the bundle itself from capture. Recheck the parent state and patch hashes after capture; if inputs changed, capture again before dispatch, never mix states.

Pass the bundle and manifest by absolute path to each child. T3 creates the checkout; the child only applies inputs inside that existing checkout. Verify its HEAD equals the recorded base and that its initial index/worktree are clean. Apply the staged patch with `git apply --index --binary`, then the unstaged patch with `git apply --binary`; skip empty patches. Copy only declared untracked/ignored payloads, preserving file kinds and modes without following symlinks outside the scope. Compare both index and working-tree states to the manifest, including deletions and modes, before any probe. Block on missing bundle access, unsupported file kinds/submodules, an apply error, or any mismatch. Do not claim a host transfer API exists. Never create a child's checkout, commit, push, or alter the parent's index to make this work.

## Phase B: Fan out

Each runner receives the same task, absolute pointers to shared grounding, its owned output location, and instructions to produce the artifact with a short rationale naming the alternatives considered and rejected. Do not give runners the scoring rubric; the coordinator and cross-judge use it. Children produce their assigned candidate themselves; they do not run the coordinator phases or dispatch further agents.

Launch independent workers concurrently through the host's current T3 orchestration rules. Use native subagents only for a supported model on the current provider with no settings beyond the parent. Use `delegate_task` for another provider, explicit settings, a separate checkout, or background work. Before the first delegation, read `orchestrator_capabilities` once; put settings in `target.options`. Do not create top-level threads for workers.

Choose the working context before dispatch. Read-only workers can share the task's authorized baseline. Writing workers need disjoint owned outputs or T3-managed `isolation: "worktree"`; never create a child's checkout in the shell or in its task. A separate checkout starts from its supported committed baseline, so do not assume it includes the parent's uncommitted changes. Name the actual baseline and any missing inputs in the brief; if required inputs cannot be supplied, report the gap before launching. Do not commit, push, or rebase merely to enable dispatch without task authorization.

Retain delegate task IDs and follow each returned `next`. Do not poll, sleep, or schedule watchers while waiting for delegates. Use the native wait mechanism for native children. Cancel delegates abandoned or replaced with `task_cancel`. Children perform their assigned slice themselves and do not dispatch further workers. Resolve relative references from the directory containing their source file. Resolve named companions from sibling `../<name>/SKILL.md` files in this same distribution. Pass each child the relevant skill entrypoint, templates, references, named companions, and these resolution rules as absolute distribution-local pointers and instructions; normalize short principle names to `principle-<name>`. Tell children not to substitute installed namesakes or slash commands. Reading a coordinator skill provides context, not permission to execute its phases.

If a candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all Phase B candidates complete, resolve the `arena cross-judge pool` through `references/models.md`. Use real configured pool entries in order, excluding auto/inherit-parent. When the parent family is known, select an available model from another actual family, not merely another provider instance. When the family is unknown, try real pool entries in order and disclose that the family check could not run. Never claim unverified model diversity. If no eligible judge runs, skip the judge, make the Phase D choice as the parent, and report the omission as upstream prescribes; no extra approval is needed solely to omit that stage. Never substitute an unavailable requested model or use a rejected target through another tool. If the current task explicitly requires a judge, report the unmet requirement and resolve that task constraint instead of claiming full success.

Dispatch one judge through Phase B's T3 rules. The judge inspects candidates read-only and must not edit or run commands that mutate their directories. If a check is needed, run it only in the judge's own scratch copy, preserving candidate bytes; report any inability to verify. Runtime permission modes do not enforce this boundary, so put it explicitly in the judge task. Give it the rubric and candidates by path label; it scores each criterion and recommends a base with rationale. It works in parallel with the coordinator reading candidates in Phase D. Do not start while candidates are still writing. Give judges and runners only their assigned role, not instructions to dispatch children.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge when Phase C ran one. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict or that Phase C skipped the judge, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.
