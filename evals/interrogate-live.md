# Live T3 interrogate input replay

## Initial prerequisite result

Blocked before child launch: the parent repository has no commit. An actual delegate_task with isolation=worktree returned invalid_request, "Unable to resolve the parent checkout commit." No child worktree was created and no replay pass is claimed. The user subsequently authorized an empty initial commit. Commit 5ed8f18 contains no project files and enables the host to resolve a baseline; no push was performed. Live replay is a separate result, not implied by that commit.

## Resume after a committed baseline

Use evals/fixtures/interrogate as the review scope. Do not change product code or unrelated user work. Record the baseline SHA, original index/worktree state, and file modes before modifying the fixture. Keep capture artifacts under workspace cache.

1. Stage a change to mixed.txt, then make a second unstaged change to the same file. Stage rename.txt to renamed.txt. Delete deleted.txt without staging, change exec.sh to executable, and change binary.dat. Add a scoped untracked file, a relevant ignored sketch under .ignored/, and a symlink. Change bounds.py to use `<` rather than `<=` without staging it.
2. Capture separate staged and unstaged binary/full-index patches, declared untracked/ignored/symlink payloads, and the base SHA plus both index/worktree hashes and modes. Recheck capture stability. Use the existing evals/input_bundle.py state helper; it is evaluation code, not an assumed host transfer API.
3. Dispatch actual T3-managed worktree reviewers using interrogate's configured panel and host rules. Give the precise baseline, scope, absolute input-bundle paths, and distribution skill paths. Do not create checkouts in shell commands or child tasks.
4. Each child confirms the baseline, applies the staged patch to index and worktree, then the unstaged patch and payloads, and compares both states to the manifest. A mismatch blocks its review. It then checks the documented inclusive boundary `within_limit(10, 10) is True` against the replayed actual fixture and reports the observed failure with evidence. No parent reread can replace child-local proof.
5. Include a corrupt-payload case and require a failed match, not a successful review. Record actual child evidence and completion status; do not infer a replay pass merely from task creation or a summary.
6. Restore only the fixture changes made by this exercise, including index, untracked/ignored payloads, modes, and symlink. Preserve unrelated edits. Compare original state after cleanup. Account for child checkout lifecycle through the host's supported mechanisms.

This fixture establishes host checkout and input-transfer behavior only. It does not establish review quality on a real application, arbitrary filesystem metadata, submodules, concurrent parent edits, or complete adversarial-review coverage.


## Empty-baseline case

Because the authorized baseline is empty, the live exercise stages the controlled fixture as new files, then applies unstaged edits/deletion/mode changes and an unstaged rename plus payload. This establishes two-state transfer and inclusive-boundary review over a real host worktree; it does not claim a committed-file rename scenario. The earlier disposable-repository exercise covers committed-file rename/deletion behavior separately.


## Executed live result

Both actual T3-managed worktrees passed replay: Codex gpt-6.1-sol and Claude Opus 5.5. Each began at the empty baseline with no fixture present, verified patch hashes, applied the separate staged/unstaged patches, copied payloads without following symlinks, and matched both Git index and worktree state to the manifest. Corrupting the child-local untracked payload produced a mismatch; restoring the bundle payload restored both matches before review.

Both independently ran the replayed inclusive-boundary function and observed `within_limit(10, 10)` return False instead of True. Opus also ran the staged version as a passing control. This proves that review reached the unstaged child-local code rather than an unchanged committed baseline.

The parent inspected both actual child checkouts and confirmed their head, independent path, both states, and evidence-copy identity. Fixture data and index were then removed from the children while preserving evidence and T3-owned checkouts. The parent's original fixture bytes/modes and empty index were restored exactly. No additional commit or push was made.

Captured evidence is under `.agents/cache/interrogate-live-eval/outputs/{codex,opus}/`; the parent summary is result.json in that run directory. These disposable files support this recorded result, not a runtime dependency. Exact POSIX permissions/ACLs are outside the helper's Git-kind/executable-bit comparison. A full interrogate coordinator workflow and live application remain untested; actual two-provider dispatch and fixture input transfer were observed from the parent.
