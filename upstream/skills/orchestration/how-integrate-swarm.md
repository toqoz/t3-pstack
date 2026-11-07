# Swarm integration policy

## Procedure to preserve

Keep Frame, Fan out, Aggregate, and Report. Declare the completion predicate and race rule before dispatch. Each worker gets a self-contained brief and owns its writable output. Preserve exact commit and measurement-method evidence where requested, the single retry for missing evidence, and the distinction between missing coverage and a pass.

## Host adaptations

The coordinator resolves the `swarm workers` role through the shared Markdown defaults and user preferences. An unavailable target requires a choice, not automatic fallback. Workers receive resolved tasks and do not recursively dispatch.

T3 owns dispatch, completion, and checkout isolation. Native children follow the current provider/settings boundary; delegates cover explicit settings, other providers, isolated checkouts, and background execution. Follow returned completion instructions and cancel abandoned delegates. Do not emulate Cursor cloud flags, create another runner, or create child checkouts in shell commands.

Read-only workers may inspect a shared baseline. Writers must have disjoint outputs or a T3-managed separate checkout. State which committed and uncommitted inputs are actually available. A checkout that lacks required inputs is a blocking gap, not permission to commit or push the parent's work. The investigation-only `references/t3.md` is not bundled for this workflow; swarm workers may write within their assigned scope.

## Reviewing an upstream update

Compare the old source, new source, current generated skill, and these integration reasons before changing the recipe. Classify each upstream delta: preserve directly, adapt to the host, or ask the user because it changes scope or selection semantics. Revisit this policy if upstream changes race termination, retry limits, worker permissions, model selection, or evidence requirements. Exact replacement failure is a review signal, not a reason to update strings mechanically.

## Verification limits

Generation checks prove source fidelity plus the declared replacements, reference closure, and license preservation. They do not prove live model availability, T3 worktree input transfer, or cancellation behavior. Behavioral evaluations must record actual dispatch and result evidence separately; simulated catalogs cannot establish those properties.


## Installed companion resolution

The T3 translation carries companion-resolution rules inline: named skills resolve to sibling ../<name>/SKILL.md files in the same distribution, short principle names normalize to principle-<name>, relative references resolve from their containing file, and children receive absolute paths plus these rules. Installed skills do not require a repository-root README, which per-skill installers do not copy. This corrects the local host translation rather than changing upstream procedure; no new Patch/Design policy or dependency resolver is introduced. Mixed-source namesakes and partial installations still have no automatic closure guarantee.
