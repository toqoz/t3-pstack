---
name: swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
disable-model-invocation: true
---

# Swarm

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Read `references/models.md` and the user preferences at the path it defines. Resolve the `swarm workers` role against the live T3 catalog, with an explicit task choice taking precedence. Use their starting effort and apply the job-based effort/speed rules there; honor current-task fixed settings. Missing preferences use the shared Codex default; only explicit `auto` or `inherit-parent` inherits the parent. If a provider, model, or option is unavailable, report it and ask for an available choice before launching that worker; never substitute silently. For a model race, name each arm's provider, model, and settings up front.
4. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Launch independent workers concurrently through the host's current T3 orchestration rules. Use native subagents only for a supported model on the current provider with no settings beyond the parent. Use `delegate_task` for another provider, explicit settings, a separate checkout, or background work. Before the first delegation, read `orchestrator_capabilities` once; put settings in `target.options`. Do not create top-level threads for workers.

Choose the working context before dispatch. Read-only workers can share the task's authorized baseline. Writing workers need disjoint owned outputs or T3-managed `isolation: "worktree"`; never create a child's checkout in the shell or in its task. A separate checkout starts from its supported committed baseline, so do not assume it includes the parent's uncommitted changes. Name the actual baseline and any missing inputs in the brief; if required inputs cannot be supplied, report the gap before launching. Do not commit, push, or rebase merely to enable dispatch without task authorization.

Retain delegate task IDs and follow each returned `next`. Do not poll, sleep, or schedule watchers while waiting for delegates. Use the native wait mechanism for native children. Cancel delegates abandoned or replaced with `task_cancel`. Children perform their assigned slice themselves and do not dispatch further workers. Resolve relative references from the directory containing their source file. Resolve named companions from sibling `../<name>/SKILL.md` files in this same distribution. Pass each child the relevant skill entrypoint, templates, references, named companions, and these resolution rules as absolute distribution-local pointers and instructions; normalize short principle names to `principle-<name>`. Tell children not to substitute installed namesakes or slash commands. Reading a coordinator skill provides context, not permission to execute its phases.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with the available results and note the missing coverage. A dropout never satisfies a required slice. For a first-pass race, cancel remaining delegates once the declared selection condition is met; do not leave abandoned workers running. Stop native workers through the host's supported interruption mechanism; if interruption is unavailable, drain their completion and mark late results as unselected.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

## Phase D: Report

Return one consolidated in-chat report with a result table, issue one-liners, gaps or dropouts, and the race rule when used.
