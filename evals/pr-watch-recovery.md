# PR-watch read failure recovery

## Scope

This checks the generated Babysit instructions after the 2026-11-11 handoff. It is a source-level scenario review, not a live host recovery test or proof that a model follows the instructions. No PR watch was registered and no merge was attempted.

## Reproduce

Run `python3 -m tools.build --repo .agents/cache/cursor-plugins --write`, then repeat with `--check`. Run `python3 tools/upstream.py check` and `python3 -m unittest discover -s tests -v`.

Read step 6 of `skills/poteto-mode/playbooks/babysit.md` against these cases. Preserve its existing frontier, one-shot classifier, review, verification, and merge-authorization gates.

| Case | Expected action | Source review |
|---|---|---|
| The same host read error persists while shell reads succeed | Reassess actual gates, preserve the error and remaining work in a durable handoff, and report the blocked wait. Do not register again based on shell success or a changed head. | Explicit in the recovery paragraphs. |
| An actual check remains pending and a read through the same host path succeeds | Resume the needed host watch. | The recovery condition allows this. |
| Direct reads establish ready state and merge authorization exists | Continue the original merge workflow only after its existing gates pass. Babysit alone stops at merge-ready. | Both authorization and existing gates remain explicit. |
| Direct reads cannot establish the current head or gates | Report unknown and do not merge. | Explicit in the first recovery paragraph. |
| Only a non-required queued suite with zero CheckRuns remains | Do not treat that suite alone as pending. Resolve any classifier discrepancy before acting. | Actual CheckRuns, statuses, and required checks are named. |
| A notification requests re-registration while host failure remains unresolved | State the conflict and missing recovery evidence. Do not enter an unconditional loop. | Explicit in the second recovery paragraph. |

Host authentication causes and failure-counter behavior remain outside this change. A real same-path recovery test remains unexecuted.

## Repository results

On 2026-11-11, generation and its check both passed for 616 files. The upstream check passed for 573 source files and Markdown review indexes. All 60 repository unit tests passed. `git diff --check` passed. The generated recovery paragraphs were read against the cases above. These results validate generation and source consistency, not live recovery behavior.
