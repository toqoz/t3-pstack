# Installation and layout verification

## Scope

Test skill discovery, complete installation, license carriage, content/mode preservation and sibling references in disposable consumers. Do not activate Home Manager, edit user configuration, install into real agent directories, publish the repository or invoke the installed workflows.

## Sources and observed versions

- skills CLI 1.7.6, executed through npx with Node 24.21.0.
- agent-skills-nix f48aa227f3d157ae3abda12cd9c4ab867f400419, executed on aarch64-darwin with its pinned nixpkgs.
- Local t3-pstack checkout with 60 skills: 57 pstack and three cursor-team-kit companions.

The layout follows [skills discovery](https://github.com/vercel-labs/skills/blob/d3701c11b1101251af14c9d148f026e1a47ebe17/src/skills.ts), [per-directory copying](https://github.com/vercel-labs/skills/blob/d3701c11b1101251af14c9d148f026e1a47ebe17/src/installer.ts), and [Nix source/selection configuration](https://github.com/Kyure-A/agent-skills-nix/blob/f48aa227f3d157ae3abda12cd9c4ab867f400419/docs/configuration.md). Those source snapshots and the executed npm release are distinct evidence; do not claim they are identical versions.

## Procedure

1. Generate skills/ and run the source and artifact checks. When migrating from dist/, compare every original skill file and executable bit before deleting the verified old distribution. Only LICENSE.txt additions and relocated package provenance should differ.
2. Create disposable CLI HOME, XDG_CONFIG_HOME, CODEX_HOME, npm cache and project directories under workspace cache. From that project, run `npx --yes skills@1.7.6 add <absolute-checkout> --list`, then `npx --yes skills@1.7.6 add <absolute-checkout> --skill '*' --agent codex --yes`. Set the disposable environment on the command, not in persistent configuration.
3. Assert 60 installed SKILL.md files, no fixture skills, exact content and executable bits for every source skill file, LICENSE.txt in each directory, and a readable poteto-help/../poteto-mode/SKILL.md.
4. Create a disposable Nix consumer flake, pin agent-skills-nix, and use the generated directory as a non-flake path source. Use discoverCatalog, selectSkills and mkBundle to build all skills and, separately, only poteto-help.
5. Build mkLocalInstallProgram with an enabled agents copy-tree target and run it from a disposable project. Build mkSyncProgram with a symlink-tree target whose absolute destination is inside cache. Check the same file content, modes, licenses and sibling link as for the CLI.
6. In the partial Nix bundle, distinguish the missing lexical sibling entry from a path that follows a directory symlink back into the full source. Do not treat access through that source as dependency resolution.

## Observed result

On 2026-11-07 JST, the CLI found and installed all 60 skills without fixture entries. All 615 per-skill files matched the source bytes and executable bits, including six executables and 60 license sidecars. The sibling link resolved. No package-level metadata outside the skill directories was needed by the installed skills.

Nix built full and partial bundles. Full copy-tree and symlink-tree installations each contained the same 60 skills and 615 byte/mode-identical files. The partial bundle contained poteto-help only: poteto-mode was absent as a bundle sibling, while physical traversal through the source symlink could still reach it. The documented complete-set installation avoids depending on this distinction.

Migration preserved 555 previous skill files byte-for-byte and mode-for-mode. The new generated tree contains those files, 60 LICENSE.txt sidecars and SOURCES.json: 616 files total. Each sidecar includes the exact source-package MIT notice; locally adapted skills also include the project MIT notice. No SKILL.md, reference or script was changed by the layout migration.

Disposable evidence lives under .agents/cache/layout-review/ (migration.json, cli-install.log, cli-result.json, nix-result.json and nix-consumer/flake.lock).

## Limits

This is local-checkout CLI installation and an isolated Nix consumer, not GitHub-source installation, Home Manager activation, every harness's registration behavior or live workflow execution. Current artifacts must be committed and published before a GitHub source can distribute them; no commit or push was made by this evaluation. Partial installation, renamed skills and mixed-source companion resolution are not guaranteed by these checks. No dependency resolver or repository-owned installer was added.


## Review corrections

Opus reviewed the layout implementation and identified interrupted-write recovery, unrelated empty-directory cleanup, and an inherited local T3 dependency on the repository README. The materializer now adopts only exact planned bytes outside the old ownership list, allowing completed writes to resume safely; injection tests cover interrupted first and subsequent writes. Empty-directory removal is limited to parents of deleted owned files. Runtime byproducts remain explicit unmanaged content rather than a hidden ignore list.

The swarm, arena and reflect T3 instructions now carry companion resolution inline instead of requiring a root README at runtime. This is a local T3 translation correction; other workflow behavior is unchanged. It follows the initial byte-preserving layout migration and invalidates earlier installer copies for those three changed entrypoints. Final regeneration and local installer refresh are recorded separately. License provenance now identifies both package and local LICENSE inputs where both appear. Discovery tests inspect the whole repository outside .git, .agents and the generated skills container.


Final review-follow-up validation passed 59 repository tests, the 573-file source check and the 616-file generation check. After regenerating the three corrected coordinator instructions and license provenance, the local skills CLI installation and both Nix copy-tree/symlink-tree destinations were refreshed. All three again contained 60 skills and 615 byte/mode-identical per-skill files, with 60 license sidecars, six executable files, readable sibling links and no root-README dependency in swarm/arena/reflect. The recorded artifact fingerprint and comparisons are in .agents/cache/layout-review/final-install-result.json. GitHub-source installation and Home Manager activation remain untested.


## Published-source installation

After pushing commit 8224ba372b50cc32d881cee15c8bfc3b5ca31e4e to GitHub, skills CLI 1.7.6 installed from toqoz/t3-pstack into a new disposable project with isolated HOME, XDG_CONFIG_HOME, CODEX_HOME and npm cache. All 60 skills and 615 per-skill files matched local generated bytes and Git executable flags; 60 license sidecars and six executable files were present, fixture skills were absent, and the poteto-help sibling link resolved. This supersedes the earlier GitHub-source installation limitation; Home Manager activation and live workflow execution remain separate. The result is recorded in .agents/cache/release/github-install-result.json.

[GitHub Actions for that commit](https://github.com/toqoz/t3-pstack/actions/runs/42321182773) passed all 60 tests, source checks, pinned-source fetching and generation verification on Ubuntu/Python 3.10.
