# Delegate cancellation and checkpoint handoff

## Scope

Verify completion notification, cascading cancellation and fresh-task checkpoint resumption without polling a live delegate. This is an explicitly authorized experiment stop, not automatic stall detection. Use disposable workspace cache; no application, Git, configuration or external-service changes.

## Procedure

1. Prepare a one-shot coordinator cancellation command with a fixed experiment stop time and exact task IDs saved at dispatch. It must cancel unconditionally, without reading live task state or progress artifacts first. Include schedule deletion and a bounded fixture lifetime.
2. Dispatch a Claude Opus owner. It writes checkpoint unit 1, then explicitly dispatches one Codex descendant. Save returned IDs as part of dispatch; follow the returned next and end the turn.
3. The descendant runs one foreground Python command: record its exact PID and UTC start time, sleep 300 seconds, then write a natural-finish marker. Do not use background processes or a cooperative stop sentinel.
4. At the predetermined stop, call task_cancel on the owner and delete the schedule. Only then inspect cancellation results and terminal state once. If cancellation is still pending, record that outcome without a polling loop or success claim.
5. Verify the descendant's interrupt reason, command interruption and recorded exact PID exit before its natural lifetime. Verify no pending descendant runs remain and no natural-finish marker exists.
6. Dispatch a fresh task on the original owner's provider/model with the consolidated checkpoint brief. It reads unit 1 and writes unit 2, without repeating the sleeper or creating children. End the coordinator turn and use the completion notification to resume.
7. Read and validate the actual unit-2 JSON and record the observed scope and cleanup. Preserve task/model metadata as evidence.

## Observed run

On 2026-11-07 JST, the Claude Opus 5.5 owner retained its completed result with hasPendingChildRuns=false after cancellation. The Codex gpt-6.1-sol descendant and foreground command were interrupted; PID 46349 had exited and the natural-finish marker was absent. A fresh Claude Opus 5.5 delegate resumed unit 1 and completed unit 2 at 2026-11-06T23:04:24Z. Its completion notification woke the coordinator. The one-shot schedule was deleted.

This establishes the bounded cross-provider cancellation/handoff path. It does not establish general detached-process-tree cleanup, semantic-stall detection, approval/question notification paths, or a complete application/PR recovery workflow. Do not broaden the pass beyond those observations.
