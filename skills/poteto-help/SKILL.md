---
name: poteto-help
description: Guides users through pstack setup, poteto-mode, and picking the skill, playbook, or principle for a task. Read this skill with a question about the T3 distribution.
disable-model-invocation: true
---

# Poteto help

Answer the user's question about pstack, hand them a prompt they can send, and link the file the answer came from. For a help question, don't start the work. The user asked how, and a pstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use pstack to fix this bug", is not a help question. Read [`poteto-mode`](../poteto-mode/SKILL.md), do the work under it, using the distribution-local entrypoint.

This file maps questions to the skills and guide pages that hold the answers. Those files own the details. Read the file you route to before you quote it, and trust it when it disagrees with this map. Resolve links from this distribution and give the user the actual local file path. This trial uses files, not registered slash commands: ask the agent to read `<distribution>/skills/<name>/SKILL.md` and follow it. In the examples below, skill names are shorthand for those files. Resolve named companions here, not installed namesakes. Do not promise persistent mode activation.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. If the need is still unclear, ask one multiple-choice question with these options, then answer only the section they pick:

- Get set up
- Start a task with `poteto-mode`
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

Check the state that changes the answer, and mention it only when it does:

- Read `references/models.md` for the preferences location and shared defaults. Missing preferences mean roles use those defaults; do not infer that setup never ran elsewhere.
- No `verify-*` skill or other app harness in the project means agents have no scripted way to drive the app. Mention `create-verification-skill` when the question is about proving a change works.
- No formal verification skill in the project means no property is checked past what tests reach. Mention `create-formal-verification-skill` when the question is about a race, an invariant, or another case tests rarely hit. When one exists and the code it covers changed after the commit it records as last in sync, mention `maintain-formal-verification-skill` if the question touches that code.

When the model preferences are missing and it matters, ask whether the user wants to pick a model for each role and a reasoning budget now. It matters when the user is new, the question is about setup or cost, or the answer depends on which models run. Ask at most once per chat. If the need is also unclear, ask both questions together. Offer two choices:

- Now: give them `setup-pstack` to type, and answer their question too.
- Later: answer their question, and add one line saying every role keeps its default model until they run `setup-pstack`.

## Get set up

1. Use the generated T3 distribution. Read the complete `<distribution>/skills/<name>/SKILL.md` to invoke a skill; this trial does not register commands or install hooks.
2. Run [`setup-pstack`](../setup-pstack/SKILL.md). It asks for a reasoning budget, maps a model to each role, and saves Markdown preferences. Workflows read them on invocation; a new chat is not required. Then it offers once each to generate a verification skill and a formal verification skill for the project, unless the project already has one.
3. Start a real task with `poteto-mode`, a goal, and a check that can pass or fail.

Reading files installs no automatic triggers. The [setup skill](../setup-pstack/SKILL.md) and `references/models.md` have the details. Offer to word their first prompt with them, per [`references/prompting.md`](references/prompting.md).

If cost is the worry, say where the tokens go and how to spend fewer. pstack spends extra tokens on subagents and review panels. Rerun `setup-pstack` and pick a smaller budget or cheaper models. A role set to `auto` or `inherit-parent` runs on the chat's model, which saves tokens when the chat runs on a cheaper model. A shorter panel list runs fewer subagents, one for each entry. Save `poteto-mode` for work that needs rigor.

This distribution adapts pstack execution to T3. The [mode entrypoint](../poteto-mode/SKILL.md) owns host dispatch and continuation rules. Report an unavailable capability rather than substituting Cursor commands.

## Start a task with `poteto-mode`

`poteto-mode` matches the task to a playbook, copies the playbook's steps into the todo list, and runs the other skills as the steps need them. A step it skips stays in the list as `skip: <reason>`. A good prompt states the goal and how to tell it's done. It doesn't list skills, because a hand-written sequence tends to drop or reorder steps the playbook would keep. Read [`references/prompting.md`](references/prompting.md) before you help word one. The [mode entrypoint](../poteto-mode/SKILL.md) owns the routing rules.

Read the mode for each new task; this file-based trial installs no Custom Mode or session hook. Mid-chat, "new task" makes the mode match a fresh playbook. The mode already uses the bundled poteto-agent brief for its workers. For a worker of your own, follow the mode's dispatch rules and supply its [poteto-agent reference](../poteto-mode/references/poteto-agent.md) by absolute path.

## Pick a skill

The default answer is `poteto-mode`, which runs most of the others when its steps need them. Name a skill directly when the user wants more or less of something than the playbook gives. Read the skill before you recommend it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`poteto-mode`](../poteto-mode/SKILL.md) |
| Check that the agent understood their goal and the problem before it starts | [`in-your-own-words`](../in-your-own-words/SKILL.md) |
| Get a prompt rewritten deeper, not bigger, before sending it: what a top professional would add, their raw material and methods, and an outside check. It returns the prompt and doesn't do the task | [`sharpen`](../sharpen/SKILL.md) |
| Know how code works now, or where new code should live | [`how`](../how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`why`](../why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`teach`](../teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`recall`](../recall/SKILL.md) |
| Catch up on what changed in this chat since their last message, in plain words and small visuals, with every item waiting on them listed and decidable from the reply alone | [`ketchup`](../ketchup/SKILL.md) |
| Catch up like `ketchup`, in a short subtitled video of slides, with the waiting calls as text under it | [`ketchup-video`](../ketchup-video/SKILL.md) |
| Know what a small diff could break outside itself | [`blast-radius`](../blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`architect`](../architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`arena`](../arena/SKILL.md) |
| Run parallel checks over slices, or race workers, through T3 | [`swarm`](../swarm/SKILL.md) |
| Have different models review a diff and try to break it | [`interrogate`](../interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`tdd`](../tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| Improve code and useful comments together, using an independent reviewer | [`no-comments`](../no-comments/SKILL.md) |
| Clean AI tells out of prose | [`unslop`](../unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`technical-writing`](../technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`bro`](../bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`create-verification-skill`](../create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| Formally verify a race, invariant, or other property that tests rarely reach | [`create-formal-verification-skill`](../create-formal-verification-skill/SKILL.md) |
| Bring a formal verification back in line after the code it covers changed, and learn whether a failure is drift or a bug | [`maintain-formal-verification-skill`](../maintain-formal-verification-skill/SKILL.md) |
| Show a PM or designer what the user sees as a chart checked by a TLA+ model, with the shortest path to each state that breaks a rule | [`statechart`](../statechart/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`figure-it-out`](../figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`show-me-your-work`](../show-me-your-work/SKILL.md) |
| Pick a model for each role and a reasoning budget | [`setup-pstack`](../setup-pstack/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`automate-me`](../automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`reflect`](../reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`correct`](../correct/SKILL.md) |
| Build a page whose buttons wake a Grok Bot over a webhook | make-bot-ui is omitted: it assumes Grok Bot's long lifecycle, which seems unlikely to fit T3 Code's different lifecycle well. |
| Find their way around pstack | `poteto-help` |

If a skill directory next to this one is missing from the table, read its frontmatter and route by its description. The `principle-*` directories are covered under principles below.

Close calls:

- `how` explains what the code does. `why` explains the reasons. `teach` runs one or both and explains the result plainly.
- `arena` gives every worker the same brief and merges the best parts. `swarm` splits work into slices or a race and returns one report.
- `architect` implements right after it settles the design. Add "with checkpoint" to review the design before it writes code.
- `interrogate` reviews the diff. `blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `recall` rebuilds context across recent chats. `ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

Not in pstack:

- `deslop`, `control-cli`, and `control-ui` originate in cursor-team-kit and are bundled as supporting skills in this distribution.
- `/loop` and `/create-skill` are Cursor built-ins, not commands provided by this trial. Follow the mode's T3 continuation and host skill-authoring guidance.
- pstack has no orchestrate skill. Orchestrate is a poteto-mode playbook.

## Playbooks and principles

Playbooks are step lists inside `poteto-mode`, not skills, so they have no slash command. Inside `poteto-mode`, describing the task picks one, and these phrases name one directly:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" selects Autopilot-full. "autopilot, don't merge" selects Autopilot-stack. Unattended execution is blocked by unresolved automatic silent-hang and approval-wait detection in running delegates and descendants. Completion notification, cancellation and checkpoint handoff have bounded live evidence; they do not close the detection gap. Planning remains available with the blocker stated.
- "run the eval playbook" runs Eval.

Without the distribution-local mode entrypoint, the host may resolve a phrase such as "babysit this pr" to a different installed workflow. The Playbooks section of [`poteto-mode`](../poteto-mode/SKILL.md) lists every playbook and when it applies. Its [Opening a PR](../poteto-mode/playbooks/opening-a-pr.md), [Babysit](../poteto-mode/playbooks/babysit.md), and [Shipping](../poteto-mode/playbooks/shipping.md) playbooks own those procedures.

pstack has no planning skill. The host's planning mode, when available, works alongside it. For work that spans phases or stacked PRs, asking `poteto-mode` for a plan runs the [Multi-phase plan playbook](../poteto-mode/playbooks/multi-phase-plan.md), which writes the plan and doesn't implement it. For a design question, the Prototype playbook or `architect` settles it in code first.

Principles are one-rule skills that `poteto-mode` reads and cites in its replies. The user rarely invokes one. They steer with the names instead, as in "apply prove it works. show me the real output." Reading the corresponding `principle-<name>/SKILL.md` loads one on demand. The mode's Principles section lists them.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| The mode stopped applying after a few turns | Read the distribution-local mode for each new task; this trial does not install a persistent mode. |
| A question got treated as the next step of the last task | Say "new task", or say the turn doesn't need the mode. |
| A new model choice had no effect | Workflows read Markdown preferences on invocation. Check the actual preferences path and re-read them before the next dispatch. |
| Runs cost more than expected | See the cost paragraph under Get set up. |
| A skill didn't load on its own | This trial has no automatic triggers. Read its distribution-local entrypoint, or let the mode invoke it when its playbook needs it. |
| Parallel agents overwrote each other | Use T3-managed worktrees for isolated edits. They still share machine processes, ports and dependencies; isolate those resources when needed. |
| An overnight run moved but finished nothing | Use a checkable exit condition, not a duration. Read [Autonomous run](../poteto-mode/playbooks/autonomous-run.md); its supported continuation does not supply the missing Autopilot stall detector. |
| The reply claims success from a green build | Ask for the real command, flow, stored value, or profile. That's the prove-it-works principle. |

For a run that drifts, [`references/prompting.md`](references/prompting.md) has one-line steers. [The recipes](references/recipes.md) give prompts worth copying.

## Make pstack my own

- [`automate-me`](../automate-me/SKILL.md) drafts a personal mode skill from the user's own history, to use alongside `poteto-mode`.
- [`reflect`](../reflect/SKILL.md) after a session turns its lessons into skill edits the user approves.
- `poteto-mode write a skill for <workflow>` runs the authoring playbook. The eval playbook tests a skill change blind.
- Fix a misbehaving skill in its own PR, not inside the feature work where it went wrong.

Read the named skill or the mode's authoring/eval playbook for the actual procedure.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from [`references/recipes.md`](references/recipes.md) when one fits, then the link to that file. Keep it short unless the user asked for the whole map.
