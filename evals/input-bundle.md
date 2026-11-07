# Input bundle replay exercise

Run `python3 evals/input_bundle.py` from the repository root. The stdlib-only exercise recreates disposable repositories under `.agents/cache/input-bundle-eval/` and writes `result.json` plus the captured patches and manifest.

The fixture has staged and unstaged edits on the same path, a rename, deletion, executable-mode change, binary edit, untracked file, relevant ignored sketch, and symlink. It captures the two Git patches separately and records both index and worktree hashes/modes. It applies the staged patch to the replay index and worktree, then the unstaged patch to the worktree, then declared payloads. Both states must match. A deliberately corrupted input must fail the comparison.

This demonstrates the documented Git replay procedure. The fixture clone is an ordinary disposable repository, not an agent checkout. It does not launch T3 worktrees, prove child access to bundle paths, or provide a runtime transfer tool. It does not validate submodules, concurrent parent edits, or arbitrary filesystem metadata. Unsupported kinds, inaccessible inputs, unstable capture, or a manifest mismatch must block the actual review.
