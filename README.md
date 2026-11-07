# t3-pstack

Preserve pstack's engineering judgment while letting T3 own execution.

A T3-focused integration of 57 of pstack's 58 skills, plus three supporting cursor-team-kit skills. The [skill index](upstream/skills/README.md) records adoption and the make-bot-ui omission. Automatic delegate stall/approval-wait detection remains unresolved, so unattended Autopilot-full/stack execution is blocked. Other workflow verification limits are recorded in [verification.md](docs/verification.md).

## Read a skill

In a T3 session, ask the agent to read one of these entrypoints and follow it for your question:

- `skills/how/SKILL.md` for architecture and execution flow.
- `skills/why/SKILL.md` for historical rationale and evidence.
- `skills/setup-pstack/SKILL.md` to choose role models and save Markdown preferences.

How and why read their bundled `references/t3.md` investigation adapter. Setup uses its own discovery, validation, and configuration-write procedure. Direct file invocation requires no installation. The repository does not install an automatic session hook or change machine configuration.

For example, ask: "Read skills/how/SKILL.md and explain how this repository detects a changed upstream reference file."

## Invoke any bundled skill

For help choosing a workflow, read `skills/poteto-help/SKILL.md` with your question. It explains the distribution and returns an example prompt without starting the work.

In a checkout, read this README and the complete `skills/<name>/SKILL.md`, including its frontmatter description. Some principles put essential guidance in that description. In a checkout, invoke the file directly. An installed harness controls command discovery and activation; installing files does not create a persistent T3 mode.

Resolve a pstack companion to the sibling `../<name>/SKILL.md` of the current skill, in the same checkout or installation, and read that file. A short principle name such as boundary-discipline resolves to `principle-boundary-discipline`. Do not substitute a namesake from another source or installation. If a required companion is absent, report the gap rather than running a different version. A documented illustrative reference does not require invoking that companion; if the task actually needs the absent workflow, report that limitation. A user's explicit request for another skill or path still takes precedence.

The host decides permissions, whether subagents may run, how dispatch works, and which source controls managed configuration. Reading a principle is not permission to spawn, commit, change CI, or install an always-on trigger. Preserve the requested conversation language and the project's formatting conventions when applying general writing guidance.

For parallel coverage or a declared race, read `skills/swarm/SKILL.md`. It uses the shared model preferences and T3 dispatch rules in its own entrypoint; it does not use the investigation-only adapter.

## Install

The skills target T3 execution; installing them in another harness does not supply T3 orchestration tools. Install the complete set so sibling references resolve. Selecting individual skills is not dependency-aware: a skill may require companions that the installer does not select automatically. Keep the original skill directory names.

GitHub-source installation was verified with skills CLI 1.7.6 in an isolated project (see [installation evidence](evals/installation.md)). Select your harness explicitly:

```sh
npx skills add toqoz/t3-pstack --skill '*' --agent codex
```

The tested form is a project-scoped local installation: `npx --yes skills@1.7.6 add <absolute-checkout> --skill '*' --agent codex --yes`, run from the destination project with an isolated test HOME. For the example above, replace `toqoz/t3-pstack` with the checkout's absolute path to install locally. The CLI owns installation destinations and update tracking. Each copied skill includes its own license notice. Do not copy only SKILL.md; references, playbooks and scripts are part of the skill.

For agent-skills-nix, add a non-flake input to your existing consumer flake:

```nix
inputs.t3-pstack = {
  url = "github:toqoz/t3-pstack";
  flake = false;
};
```

In an existing agent-skills-nix Home Manager configuration, with flake inputs passed through as described in its documentation:

```nix
programs.agent-skills = {
  enable = true;
  sources.t3-pstack = {
    input = "t3-pstack";
    subdir = "skills";
  };
  skills.enableAll = [ "t3-pstack" ];
  targets.agents.enable = true;
};
```

The Home Manager example is documentation-based; the executed Nix evaluation used the library with a path source and disposable copy-tree/symlink-tree destinations, not Home Manager activation. See [installation evidence and limits](evals/installation.md).

Use `targets.claude.enable` instead for Claude's skill directory. Pin revisions through your consumer's lock file. This repository is a plain skill source; it needs no npm package, Nix flake or separate installer. See [agent-skills-nix configuration](https://github.com/Kyure-A/agent-skills-nix/blob/master/docs/configuration.md).

## Repository layout

```text
skills/             Generated installable skills and SOURCES.json; do not edit
upstream/           Pinned sources, transforms, adoption notes and update reviews
adapters/           Local T3 guidance used by generation
models.md           Shared model defaults used by generation
licenses/           Canonical upstream license notices
tools/              Generation and upstream checks
tests/              Automated checks
evals/              Repeatable behavioral evaluations and fixtures
docs/               Design and verification records
```

The [category index](upstream/skills/README.md) is the single adoption overview. Categories stay in review documents; installable skills remain flat so their sibling links survive installation. Disposable upstream checkouts, installer experiments and run state live under `.agents/` and are not distribution inputs.

## Configure role models

[models.md](models.md) holds the shared defaults. Codex handles implementation and exploration; Opus handles judgment and synthesis. Panel roles use both. The original 17 upstream role lines are retained, including roles for workflows not yet adopted.

Ask the agent to read `skills/setup-pstack/SKILL.md` and run setup. It discovers T3 providers, models, and supported options, loads current choices, shows the proposed roles and reasoning budget, validates the accepted choices, then saves and reads back a Markdown file. It does not install hooks or dispatch trial agents.

Preferences live at `$XDG_CONFIG_HOME/t3-pstack/models.md`, or `~/.config/t3-pstack/models.md` when XDG_CONFIG_HOME is unset or empty. A specifically requested configuration path overrides this location. Setup follows the host's configuration-management rules for managed files. Workflows read the preferences on invocation, so no session hook is needed.

For example, a partial override can contain:

```text
# budget: large (xhigh)
how explorer: codex/gpt-6.1-sol reasoningEffort=xhigh
how explainer: claudeAgent/claude-opus-5-5 effort=xhigh
```

Missing roles use the shared defaults with the saved budget. Saved role effort options take precedence over the budget as starting levels. Before dispatch, the workflow adjusts effort to the job; an exact effort/speed specified for the current task remains fixed. `inherit-parent` and `auto` explicitly preserve the parent model and settings. A budget is a starting reasoning level, not a spending limit. Abstract budget mapping uses a supported same-model level and shows rounding in the proposal. Availability and option support come from T3, not from this file; unavailable choices are reported without automatic substitution, while the calling workflow retains its documented dropout or optional-stage behavior. No runtime configuration parser is added.

## Check the repository

Requires Python 3.10+ and Git. No third-party Python packages are needed.

```sh
python3 tools/upstream.py check
python3 -m unittest discover -s tests -v
```

`check` verifies category index coverage of the pinned top-level skills, source revisions, local review-document links, and license bytes. It does not interpret adoption prose or approve an integration.

## Review adoption and upstream updates

[upstream/README.md](upstream/README.md) identifies the source and explains the review workflow. Category README files contain human-readable adoption, integration, omission, and unresolved decisions. Add and link an integration plan when a decision needs more detail. No structured decision registry or per-decision source hashes are used.

An upstream update compares source A, source B, and the current local integration. The agent explains the actual changes and proposes direct inclusion, adapted inclusion, a revised integration policy, or a user decision. The user reviews the update note and implementation diff. Successfully applying old replacements to B is not sufficient evidence to accept B.

Fetch a candidate without replacing the current baseline:

```sh
mkdir -p .agents/cache
git clone https://github.com/cursor/plugins.git .agents/cache/cursor-plugins
```

Clone only once. On later updates, fetch and specify B's full commit SHA:

```sh
git -C .agents/cache/cursor-plugins fetch origin
python3 tools/upstream.py snapshot .agents/cache/cursor-plugins <B-full-sha> > .agents/cache/candidate.json
python3 tools/upstream.py diff .agents/cache/candidate.json
```

Follow the [A-to-B review process](upstream/README.md#update-from-a-to-b) before accepting the candidate. Snapshot reads Git objects, not the upstream working tree. The complete file inventory includes reference material and files outside the top-level skills. Periodic detection remains deferred.

## Generate the selected skills

After fetching the locked commit, generate or verify the checked-in distribution:

```sh
python3 -m tools.build --repo .agents/cache/cursor-plugins --write
python3 -m tools.build --repo .agents/cache/cursor-plugins --check
```

`--write` updates generated files in `skills/`, using `skills/SOURCES.json` as its ownership record. Unmanaged content and symlinks stop writing without deletion. Files that exactly match planned output can be adopted after an interrupted write, including before the first manifest was written. Empty directories outside stale owned-file paths are left alone. Owned generated files are overwritten; keep personal edits in canonical inputs. Runtime byproducts such as .DS_Store, node_modules and __pycache__ also stop checks/writes; run tools from disposable copies or move those byproducts out before rebuilding. `--check` rejects edits, missing files, and stale files. Both verify the complete lock against upstream Git objects before rendering anything.

`upstream/transforms.json` is the execution recipe for the currently generated slice, not an adoption registry. Read the category decision before changing a recipe. It specifies selected source directories, target directories, and exact replacements with reasons. Selected directories retain their source files and executable modes; regeneration checks detect mode drift as well as content changes. Only skills whose entrypoint or Markdown references need the T3 adapter or model defaults receive those shared documents. Plain source-preserving skills do not gain execution guidance. Relative Markdown file links must resolve inside the generated distribution.

Each replacement must match once in the original source. Overlapping source spans fail, and replacements do not cascade. Source hash mismatches, missing files, collisions, and invalid output paths stop generation. The generator copies selected skill directories and explicitly declared imports from the pinned source. Imported files retain source provenance, and executable files retain their pinned modes. Write and review an integration plan before adding another packaging mechanism.

`skills/SOURCES.json` records every generated file, original paths/hashes/modes where applicable, output hashes, source revisions, and build-input fingerprints. Each `skills/<name>/LICENSE.txt` carries the full upstream MIT notice; locally adapted skills also carry the project MIT notice. These are artifact provenance, not per-decision approval records.

## License

Original project code is [MIT licensed](LICENSE). Upstream pstack's full [MIT license and Lauren Tan copyright notice](licenses/pstack-MIT.txt) are preserved separately and must accompany generated upstream content. No code or skill text has been copied from the reference T3 port.


The supporting deslop, control-ui, and control-cli skills come unchanged from [cursor-team-kit](upstream/dependencies/cursor-team-kit/README.md), with an independent source lock and [Cursor MIT notice](licenses/cursor-team-kit-MIT.txt). Build verifies that pin too and records its source identity in SOURCES.json. They are additional dependencies, not part of pstack's 58-skill count.
