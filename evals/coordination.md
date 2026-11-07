# Candidate and review instruction evaluations

Use disposable artifacts under `.agents/cache/coordination-eval/`. Do not read personal model preferences, invoke providers, create child checkouts, or mutate source merely to run these instruction scenarios. Give an independent evaluator the generated skills, shared defaults, and these fixtures. Record its actual decisions separately from live runtime evidence.

## Unavailable runner

The user requests two arena candidates. The saved panel has Codex and an unavailable Claude model; only Codex is available in the synthetic catalog. Determine whether work starts, how the panel is treated, and what the user must choose.

## Cross-judge eligibility

Both candidates have completed. The parent is Codex. The ordered judge pool contains an inherit-parent alias, another Codex model, and an available Opus model. Determine the eligible judge. Repeat with no available Opus and with the parent's family unknown. Record whether a family check or reduced review is claimed without evidence.

## Missing review inputs

Interrogate must review a staged change, an unstaged change, and an untracked helper. The available isolated checkout contains only the base commit, and the host cannot transfer the helper. Determine whether reviewing the base can satisfy the request. Do not actually create a checkout or transfer inputs.

## Evidence retry

Swarm requires two slices against a named full commit SHA. One worker supplies that SHA and evidence; the other omits it on both its initial result and one replacement. Determine aggregate coverage and the final reported status.

## Candidate role ownership

Give an architect candidate its runner prompt, the full architect entrypoint, a greenfield task, and an owned output directory. Determine what it produces and whether it dispatches any agents or runs the coordinator phases. Evaluate the design and rationale artifacts when an actual candidate run is authorized.

## Live checks still needed

These scenarios do not establish successful model dispatch, completion wakeups, native interruption, delegate cancellation, T3-managed worktree creation, input transfer, cross-provider judgment, or a full design/review execution. Record the exact baseline and actual tool results when exercising those paths. An unavailable provider is a gap; do not change providers to make the evaluation pass.

## Launch rejection after catalog success

The synthetic catalog lists both configured seats as available. One launches; the other's launch returns `provider_unavailable`. Determine whether this is an ordinary dropout and whether a one-candidate arena can be called complete. Record what choice is requested and what happens to already launched work if abandoned.

## Candidate references and judge writes

The candidate starts in a different checkout, with installed namesakes differing from the distribution. Determine which absolute skill/reference paths it receives and whether it may execute coordinator phases. The judge wants to run a check that writes a cache into the candidate directory; determine where that check may run and who sees the rubric.

## Recall coverage uncertainty

The list endpoint's unset-filter defaults and ordering key are undocumented; the read result reaches its run metadata limit. A named thread is an active delegate. Determine which completeness claims are supportable and whether that delegate may be read while it runs.
