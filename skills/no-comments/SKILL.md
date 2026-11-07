---
name: no-comments
description: "Review code and comments together, simplify real design problems, remove redundant prose, and preserve useful intent and contracts. Use for no-comments or a focused comment/design review."
disable-model-invocation: true
---

# No comments

Review code and comments together to reduce the reader's work. Improve a weak design when a simpler structure is feasible; remove comments made redundant by the verified improvement. Actively retain or add useful intent, contracts, and explanations. Fewer comments is not the goal.

## Scope

Use the caller's files or diff, otherwise the current diff from the agreed base branch through the working tree. Establish the actual baseline rather than assuming main exists. Keep legal/license notices and the task's scope intact.

## Independent review

Read [the adapted reviewer](references/comment-sicko.md) and `references/models.md`. Resolve the `judgment and prose` role from the shared defaults, user preferences, and live T3 catalog. Apply its job-based effort/speed rules; explicit fixed task settings take precedence. Never silently replace an unavailable provider/model/options choice. The parent dispatches the reviewer directly under current T3 rules. Native children are for supported current-provider models with no settings beyond the parent; explicit settings, other providers, background work, and isolated checkouts use delegate_task. Before the first delegation, inspect orchestrator_capabilities once and put settings in target.options. Retain task IDs, follow the returned next, use native waits for native children, never poll delegates, and cancel abandoned delegates with task_cancel. Every fresh reviewer pass is a new task. Give absolute distribution-local template/companion paths and an owned report/patch output; never substitute installed namesakes. The reviewer can inspect the authorized shared checkout without editing source; keep the scoped inputs stable while it works and report changed or inaccessible inputs as a gap. Do not create child checkouts in the shell or assume isolated checkouts contain uncommitted inputs.

Give one independent reviewer its assigned reference, complete scope/baseline, relevant files, and an owned output location by absolute path. It proposes a comment-only patch and structural findings; it never edits application code or dispatches children. Do not give it this coordinator procedure as instructions to execute. If evidence requires how/why, the reviewer returns exact symbol questions instead of deciding without evidence. The parent runs the adopted **how** skill or **why** skill and supplies findings to one fresh reviewer pass. If that pass still lacks necessary evidence, report the item unresolved. This evidence exchange is separate from the rejected-report retry below and happens at most once.

## Inspect, improve, and verify

1. Inspect the report and proposed patch. Reject scope escapes, application-code edits, lost useful rationale/contracts, legal-header deletion, and refactors whose main effect is replacing a comment with more complexity. Comment additions must be accurate and useful. Restore rejected edits if any were applied. Re-run one rejected report in a fresh reviewer task with the failure named; reject a second report and mark the workflow incomplete.
2. Assess every proposed structural fix on the combined code-and-documentation result. Prefer fewer concepts, clearer ownership, and simpler interfaces; do not extract shallow helpers, add layers, or invent long names solely to eliminate prose. A useful comment about our own design is not a defect. A comment is also not a substitute for fixing a feasible, in-scope design problem.
3. Implement accepted small in-scope fixes. If a fix needs a new shape, follow the **architect** skill once for the accepted set through its synthesized sketch only. This invocation limits architect to design; do not enter its automatic implementation phase. The parent implements the accepted design under the existing task authorization within scope. Do not broaden the task to eliminate every workaround. The **principle-fix-root-causes** and **principle-redesign-from-first-principles** skills guide intent only; neither expands scope.
4. Verify the changed behavior against the real artifact. After a verified structural fix, remove comments that are now redundant, retain rationale that still matters, and add or clarify missing contracts or intent. Do not retain stale or false explanations; correct the explanation to match verified behavior and report the remaining defect.
5. For a constraint encoding, propose the cheapest appropriate type, runtime check, test, or lint and obtain explicit user approval before implementing the proposed encoding. Unattended/evaluation runs require caller pre-approval. Until an approved replacement is implemented and verified, retain the necessary constraint comment and report the open guarantee. Declined or out-of-scope work does not authorize deleting the warning. Preserve correctness suppressions until a verified root-cause fix makes them obsolete; do not break code by deleting a directive first.

## Report

Report meaningful structural and documentation improvements, evidence, rejected findings/retries, proposed or completed encodings, and unresolved constraints. A missing required reviewer or verification means an incomplete workflow. Counts may describe the patch but never establish success.
