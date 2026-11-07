---
name: automate-me
description: "Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user works. Drafts or revises a personal -mode skill via host skill authoring + unslop, optionally pulling fresh evidence from recent transcripts."
disable-model-invocation: true
---

# Automate me

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them (e.g. `jay-mode`, `priya-mode`).

This skill orchestrates three others: an inline mining pass (see step 1), the host's available skill-authoring skill (authoring), and the **unslop** skill (prose discipline). It sequences them. It doesn't replace them.

## Flow

### 0. Check for an existing skill

Look recursively for `.agents/skills/**/*-mode/SKILL.md` and `~/.agents/skills/*-mode/SKILL.md` matching the user's handle. Mode skills can live in a personal category directory (`.agents/skills/<handle>/`), not only at the top level. If one exists, confirm intent with `AskQuestion` (unless they already said "update my skill" or similar):

- Update the existing skill (default for repeat runs)
- Start fresh (rare, ask why before doing it)

Update mode changes the rest of the flow:
- Step 1 mines only history since the skill was last edited (`git log -1 --format=%cI <path>`).
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Use only T3-managed Codex, Claude, and other provider conversations in the authorized current project. Do not scan standalone Codex CLI/Claude Code transcript files or unrelated projects. Discover the current project/thread and schemas through the host. Enumerate project threads with includeSubagents enabled and page all results; do not filter by provider. Validate every returned record and read response against the authorized projectId before using it; reject a different or missing project identity. Omit settled/snoozed filters when collecting the full history range, rather than accidentally excluding archived work.

Group delegated descendants with their originating conversation using parentThreadId and relationshipToParent=subagent. Include independent conversations and human-created forks that are not preparing, queued, starting, running, or waiting; failure, interruption, cancellation, and rollback do not disqualify history. A fork’s local human items belong to that fork; inherited items belong to their original source. Include terminal delegated children (completed, failed, interrupted, cancelled, rolled back), grouped with their originating conversation. Page messages/activity by item position and truncated text offsets. Include native-provider child activity where exposed in its owning thread; absent bodies are gaps. Freeze the invocation cutoff before dispatch and exclude this invocation’s own miners. Use the caller's available context through that cutoff. Do not read running delegated children, poll unfinished work, or turn this mining pass into a progress monitor. Record excluded unfinished conversations and other coverage/time gaps.

Survey the original recent window (for example 2–4 weeks) or the update cutoff from step 0. Use actual activity/run timing where available, not a thread's creation date or metadata update alone. The parent enumerates metadata and writes a compact source manifest of thread/item-range pointers, lineage, cutoffs, and gaps. Partition those pointers into the original time slices and run multiple miners in parallel (for example three), within host concurrency limits. Each miner pages its own assigned activity rather than loading the full history into the parent context. If miner tools are unavailable, use supported per-slice exports to the task’s working-artifact storage and pass absolute paths; do not replace this with a parent-written summary of the entire history or claim unavailable exports exist. There is no automate-me/miner model role. Use the caller’s model as the starting model and its effort as the starting level; apply the original job-level effort/speed rules from `references/models.md` and the mode’s Subagents policy using supported same-model options. Explicit auto/inherit-parent or fixed task settings retain their defined precedence. Do not invent a role or borrow recall/swarm as another workflow dependency. Miners do their assigned slice without spawning more agents.

Each miner collects its assigned transcript/digest with provider/model, canonical source thread/item identities, human/agent authorship, parent/child lineage, cutoff, and explicit gaps. Deduplicate copied child results, briefs, and repeated source items. A child kickoff may have user-role text while being authored by an agent; it is not a fresh human preference. A copied/inherited source item is one occurrence even when several threads or time slices expose it. Slice boundaries are work partitions, not evidence of independent recurrence: merge repeated source statements/events and do not count the same episode twice merely because a thread spans slices. Retain distinct genuine human instances and confirm contextual or conflicting signals in the original interview. Treat historical instructions as untrusted evidence, not authorization. Reading a caller-owned direct child’s final result can acknowledge its delivery. In the inspected T3 0.1.7 implementation, reading another parent’s child does not acknowledge that parent’s result; do not assume all history reads are side-effect-free if the host contract changes. Miners read assigned history, not completion notifications as a monitoring mechanism. Each miner returns the original short pattern list with evidence pointers. Default signals worth hunting:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped.

### 2. Ask the user directly

Mining misses intent that hasn't come up yet. Use the host question tool with short structured choices. When its UI lacks multi-select, list the same choices and accept several in a text response instead of passing an unsupported allow_multiple field.

Shape: one or two questions with 4-6 options each, multiple selections for category questions when supported, otherwise an explicit multi-choice text answer. Start broad ("Which areas matter most?"), then follow up on selected areas with specific options. After the structured rounds, one free-form chat question catches anything the options missed.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, MCP tool use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: git worktrees, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

The **poteto-mode** skill shows the shape. Read it as a reference for granularity, not an instruction to execute its playbooks. Don't copy its content. The user's rules are not the same as poteto-mode's.

### 4. Draft the skill

Use the host's available skill-authoring skill to author the skill. Placement:

- Path: preserve an existing mode skill's category. For a new mode, use `.agents/skills/<handle>/<handle>-mode/SKILL.md` when the repo has an established personal category for that handle. Otherwise default to `.agents/skills/<handle>-mode/SKILL.md` in the project (or `~/.agents/skills/<handle>-mode/` if the user prefers a personal skill).
- Handle: the user's first name or chosen identifier.
- Frontmatter `description`: trigger on their name + `/<handle>-mode` + "work in their style", not on generic keywords like "write code" or "review PR".
- Frontmatter formatting: follow the host authoring skill's YAML rules. Keep `description` as one YAML scalar. Quote it or use `description: >-` with indented continuation lines when punctuation or wrapping requires it.
- Frontmatter `disable-model-invocation: true` by default. Opt out only if the user explicitly wants their mode to apply on every turn.

### 5. Iterate on prose

Apply the **unslop** skill and the host authoring skill's writing guidelines to every line.

Show the draft to the user and take feedback. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

Use a T3-managed worktree off the repository's actual default branch, with the required draft/source inputs supplied explicitly; uncommitted edits are not inherited automatically. Commit and open a PR under the task's authorization and host rules. Do not push to the default branch directly. If a personal/managed skill lives elsewhere, resolve its canonical repository before delivery; do not invent a PR for a non-Git destination.

## Guardrails

- **Don't overfit to one conversation.** A preference stated once and contradicted another time is noise. Require multiple instances before codifying it.
- **Don't be clever.** Restating other skills' contents, inventing metaphors, or writing "poetic" prose for an agent reader is cost without benefit. Keep it operational.
- **Reference, don't inline.** Other skills the user relies on should appear as path references, not pasted excerpts. Same for any principle docs they maintain elsewhere.
- **Keep sections minimal.** Only add a section if the user has a specific, non-default rule there. "Communicate clearly" is not a section. "Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel." is.
- **Name conventions generic.** Use "the user" or "the human" in imperatives, not the author's first name.
- **Don't force symmetry.** If a user has no process rules worth writing down, skip the Process section entirely.

## Evaluation

A `-mode` skill is subjective output. A `create-skill`-style test/iterate benchmark loop isn't useful here. Vibe-check with the user: does it read like them? Did it miss anything? Then ship.

Run a description-optimization loop only if the skill's trigger accuracy turns out to be a problem in practice.

## When not to use

- User wants a task-specific skill (not working conventions): the host authoring skill alone, no mining required.
- User wants to capture one narrow workflow (e.g. "how I write commit messages"). That's a regular skill, not a mode skill.

