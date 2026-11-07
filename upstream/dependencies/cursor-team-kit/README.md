# Cursor team kit dependency

Canonical source: [cursor-team-kit at the pinned revision](https://github.com/cursor/plugins/tree/2776ddd2355d6d6c8747d3964600f28daf62f049/cursor-team-kit).

Adopt deslop, control-ui, and control-cli to satisfy poteto-mode's existing dependencies. The user authorized proceeding with these dependencies. Their procedures remain subject to host permissions and available browser/terminal tools. No new workflow dependency is invented.

The package is MIT, copyright 2026 Cursor. [The exact notice](../../../licenses/cursor-team-kit-MIT.txt) accompanies generated output. No text from the reference T3 port is used.

The separate lock inventories this package at the same repository commit. Build verifies both locks against Git objects, retains file hashes/modes, rejects destination collisions, and records dependency identity in SOURCES.json. Unselected team-kit skills are not bundled. Pstack adoption counts remain out of 58; these three supporting skills are separate.

For updates, snapshot with `python3 tools/upstream.py snapshot <repo> <B> --path cursor-team-kit`, then compare with `python3 tools/upstream.py diff <candidate> --lock upstream/dependencies/cursor-team-kit/lock.json`. Apply the same A-to-B review to original source, local integration, and changed dependencies. Do not advance the dependency merely because pstack advances, or omit its diff from review.

| Skill | T3 | Patch | Design |
| --- | --- | --- | --- |
| deslop | - | ✅ | - |
| control-ui | - | - | - |
| control-cli | - | - | - |

## deslop

- **Patch:** Compare against the base branch instead of hardcoding `main`.

[how-integrate-deslop.md](how-integrate-deslop.md)

Artifact fidelity and dependency packaging are checked; live control-ui/control-cli sessions and deslop quality have not been independently evaluated here.
