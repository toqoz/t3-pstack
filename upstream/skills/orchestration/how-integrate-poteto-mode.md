# Mode router integration

The user approved mapping cloud VMs to T3-managed worktrees. The current candidate retains the upstream playbook graph, principles, phase gates, model-role intent, review criteria, and Comments section. No Design change is introduced. Adopted after independent Opus review and parent corrections. The review found required host-translation corrections, not approval of live operation.

## T3 adaptations

- Replace cloud worker/VM references with host-managed worktrees. Record the parent commit and exact PR head. Worktrees share processes, ports, dependencies, and machine state; isolate live-check resources as needed. Commit/PR-based artifact exchange is retained, not replaced by shared dirty state.
- Use the already reviewed models.md translation for original role preferences and effort/speed selection. Native/delegated dispatch follows the host; do not add another model-selection runtime.
- Import the pinned poteto-agent prompt and replace Cursor plugin discovery with explicit absolute distribution paths. Reading the full mode gives task/style context, not permission to run the coordinator's other phases.
- Translate PR waiting to host watch events and actual forge states. Retain the original one-shot watch-pr --status-only readiness/Bugbot classifier in a disposable copy with its pinned dependencies; never run polling mode or manufacture JSON verdicts. Retain frontier, verification, operator, and merge gates.
- Translate Cursor activity paths and worktree-usage collection to authorized T3 activity with explicit gaps. Retain source pickup, evidence, in-use, and loss-approval boundaries.
- Align the plan template and its three host-mechanism markers in check-plan.mjs/check-plan.test.ts. Other plan structure, ten live lanes, and verification requirements remain unchanged. Resolve local capacity before fan-out without reducing required coverage.

G1 is narrowed to detecting silent hangs (including hung tools and delegated descendants) and permission-approval waits in running Codex/Claude delegates. The active host instruction prohibits probing running delegates; no sufficient host-delivered event was established for these cases. This is an unresolved integration requirement, not product-level impossibility. Unattended Autopilot-full/stack execution remains blocked on this detection requirement; adoption and planning remain available.

T3 source supports terminal-result and question notifications, PR-watch events, and cascading task_cancel followed by fresh dispatch. Replacement retains the assigned provider/model and consolidated brief under the existing selection rules. Completion notification, cascading cancellation and same-target checkpoint handoff now have bounded live evidence (see below). Question/PR events remain separate evidence; none of these establish silent-hang detection. Coordinator-owned records can expose record gaps, but do not prove a worker is stalled. Do not start a monitoring schedule while the detection gate remains unresolved.

An independent Opus investigation compared twelve alternatives against pinned pstack and T3 b90e554e0a942605c4de2d4ff5d4654caf998e27. A coordinator-only deadline would avoid reading workers but replace slow, progressing or approval-blocked workers and potentially their whole subtree. It changes upstream's progress-based predicate and is not adopted. Sibling monitors, indirect artifact probes, and external watchers do not resolve the active polling restriction. Top-level owners do not cover delegated descendants; no topology change is adopted. No scheduler, VM service, watcher implementation, or worktree manager is added.

Resolution requires a permitted mechanism that distinguishes progress and operator waits from silent hangs down to delegated descendants, followed by a bounded live test of detection, cascading cancellation and same-target recovery. The existing gate must not be removed solely because interval continuation or top-level handoff passes.

Sources: [upstream audit](https://github.com/cursor/plugins/blob/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack/skills/poteto-mode/playbooks/autopilot-full.md), [T3 task contracts](https://github.com/pingdotgg/t3code/blob/b90e554e0a942605c4de2d4ff5d4654caf998e27/apps/server/src/mcp/toolkits/orchestrator/tools.ts), [question reactor](https://github.com/pingdotgg/t3code/blob/b90e554e0a942605c4de2d4ff5d4654caf998e27/apps/server/src/orchestration-v2/DelegatedTaskQuestionReactor.ts), [approval notification issue](https://github.com/pingdotgg/t3code/issues/26294).

## Evidence and limits

The generated plan-check tests pass all 7 tests. A disposable copy with frozen Bun dependencies passes 61 combined plan, readiness-policy, GitHub pagination/Bugbot-count, and CLI tests. These include the one-shot status-only path with fake readers/clocks, not real PR waits. Repository checks cover declared source changes and companion closure. Supporting cursor-team-kit skills are pinned separately with their original MIT notice. Watcher scripts are retained for the one-shot classifier, not as the T3 PR-wait runtime. The model-role difficulty tiering and file-pointer briefing rules lost in the first candidate were restored. Model defaults in playbooks and plan instructions now resolve through shared preferences. Cleanup instructions no longer depend on unavailable Cursor-only bucket labels; child PR ownership explicitly survives worker turns while the coordinator owns waits.

A bounded nested-delegate cancellation and handoff fixture ran; no long-running application program, live PR lifecycle, or automatic stall detection/recovery ran. The original source and local decisions must be compared again on A-to-B updates; an exact replacement match alone is not acceptance.

## Separate interrogate verification

The input-replay protocol is separate from cloud/worktree translation. The first actual T3 worktree dispatch failed before child launch because the repository had no commit. After the authorized empty initial commit, Codex and Opus managed-worktree fixture replay, corruption rejection, and child-local boundary review passed. [The live evaluation procedure](../../../evals/interrogate-live.md) records the prerequisite and prepared fixture. No shell-created child checkout or project-file commit was used. This is scoped replay evidence, not a full interrogate/application run.


## Review follow-up

Opus found F1–F9 in the first candidate. The parent corrected the contradictory audit instructions and pinned-distribution reads, restored one-shot readiness policy and Bugbot counts, removed stale Cursor model slugs, restored hardest-task/prose/code tiering and file pointers, aligned cleanup terminology, and made child-owner/wait ownership explicit. These corrections were parent-inspected and exercised through existing tests, not another delegated review.

G2 now has scoped live uncommitted-input replay evidence on both Codex and Opus; full application/coordinator review remains untested. The user authorized an empty initial commit, created as 5ed8f181ab24 (prefix), to enable host worktrees without committing project files. Live replay results are recorded separately. G3 remains unexecuted real PR creation-to-merge, nested coordination, and ten-lane runtime concurrency. No new Design policy or relaxed success gate was introduced to conceal these gaps.


## Live cancellation and handoff

A Claude Opus 5.5 owner saved checkpoint unit 1 and explicitly dispatched a Codex gpt-6.1-sol descendant. The descendant started a foreground Python process with a 300-second natural lifetime. A pre-authorized one-shot cancellation command called task_cancel on the owner without reading live worker state first. This was an experiment stop, not an inferred stall or a timeout-as-stall policy.

Post-cancel evidence showed the owner retained its completed result with no pending child runs, the Codex descendant and its command were interrupted, and exact fixture PID 46349 had exited before its natural lifetime. No cooperative stop sentinel or shell kill was used. A fresh Claude Opus 5.5 task read unit 1 and wrote unit 2; its completion notification woke the coordinator, which read and validated the actual output. The schedule was deleted.

This verifies completion delivery, cascading cancellation of this nested cross-provider fixture, foreground-process exit, and same-target checkpoint handoff. It does not verify every detached process tree, approval/question delivery, PR watches, or automatic stall detection. The remaining G1 blocker is detection, not the availability of cancellation or replacement. See [the reproducible procedure](../../../evals/delegate-cancel-handoff.md).
