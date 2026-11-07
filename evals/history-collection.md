# T3 history collection checks

## Live API component

Enumerate only the authorized current project with includeSubagents enabled. Confirm provider identities and subagent parent links, then read known-completed child activity with position and text-offset pagination. Preserve source identity and authorship; do not monitor running delegates. The recorded probe used completed Codex and Claude worktree-fixture tasks and stored disposable exports under .agents/cache/history-aggregation-probe/.

This tests available history transport, not a full reflect run or personal-preference mining. No standalone provider transcript files are part of the user-selected scope.

## Instruction cases

Give an independent reviewer the generated reflect and automate-me skills and [the raw request](fixtures/history/request.md), [thread index](fixtures/history/threads.json), and [activity](fixtures/history/activity.json). Ask it to derive collection scope, grouping, evidence, gaps, and permitted next steps without live history, settings, edits, or external writes. Do not supply expected selections or inferred preferences.

Inspect its actual outcome against project boundaries, delegated lineage, completed versus running children, human forks, cutoff/self-review exclusion, agent-authored user-role kickoffs, inherited copies, parent result notifications, old activity versus recent metadata, and unavailable native child bodies. This is a history-protocol assessment, not the subjective persona benchmark that upstream automate-me explicitly avoids.


## Ownership guard check

The installed T3 0.1.7 readThread implementation acknowledges returned terminal results only after directAppOwnedChildTasks selects the caller's own direct child. The unmodified extracted helper was executed with four cases: own direct child selected; other parent's child, grandchild, and human fork not selected. The test and result remain disposable under .agents/cache/history-aggregation-probe/delivery-check/. No live result notification was consumed to perform this check. This resolves the review's hypothesized cross-parent delivery side effect for the inspected implementation, without claiming that all reads are pure.

The synthetic fixtures now also include a failed child and interrupted conversation. Their valid activity belongs in the respective scopes despite a non-success state. This extension was parent-inspected, not another independent rerun. The earlier independent review demonstrated the original fork/status gaps before correction.
