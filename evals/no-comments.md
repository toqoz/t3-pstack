# Merged comment/design evaluation

The generated skill is `skills/no-comments/SKILL.md`; its independent role is `references/comment-sicko.md`. The role is adapted from the pinned pstack agent under the same upstream notice. The cited Ousterhout material is paraphrased, not bundled.

## Independent reviewer fixture

Copy [the fixture](fixtures/no-comments/README.md), timing.py, and test_timing.py from `evals/fixtures/no-comments/` into the cache directory. Provide the generated reviewer role and that disposable fixture under `.agents/cache/no-comments-eval/fixture/`. Ask the evaluator to perform the README task and write a proposed comment-only unified diff and evidence report to `.agents/cache/no-comments-eval/output/`. Do not give it expected verdicts, edit the live repository, invoke external services, or let it dispatch children.

The parent inspects the actual patch, verifies that application code and required context survive, applies it only to a disposable copy, and reruns fixture behavior checks. Use Python's AST to compare executable structure before and after; separately inspect docstrings and license/constraint comments because AST equivalence alone cannot establish preservation of useful documentation.

## Coordinator gate scenarios

Use the full generated coordinator skill with explicit instruction to evaluate supplied reports only, not dispatch a live workflow. Present these raw inputs:

- A reviewer proposes replacing an expression with different application code.
- The first report is rejected and a fresh report again violates scope.
- A proposed encoding has not been approved and its constraint warning is still necessary.
- A caller contract is absent, and the behavior is supported by code/tests.
- A verified structural fix has made an old explanatory comment redundant.
- A proposal extracts a one-line expression into multiple forwarding helpers solely to eliminate its explanation.

Record actual decisions and evidence separately from expected evaluation criteria. The unchanged-code AST check is not sufficient for the coordinator scenarios; they assess the acceptance and approval rules.

## Limits

A fixture run does not prove live model resolution, multi-provider dispatch, T3 worktree input replay, the how/why evidence exchange, architect integration, or retry cancellation. Record those as gaps unless they actually run. Unavailable required roles are not successful evaluations.
