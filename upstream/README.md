# Upstream source and review guide

## Source

The canonical source is [cursor/plugins, pstack/ at the pinned revision](https://github.com/cursor/plugins/tree/2776ddd2355d6d6c8747d3964600f28daf62f049/pstack).
The current baseline is `2776ddd2355d6d6c8747d3964600f28daf62f049`.
[lock.json](lock.json) records the commit, original file hashes, and executable modes. There are no per-decision fingerprints to update.

The original pstack license is MIT with `Copyright (c) 2026 Lauren Tan`. Its [complete notice](../licenses/pstack-MIT.txt) accompanies generated output. The reference T3 port is research material, not the canonical source or a source of copied implementation.

## Review by workflow

Read and edit the category notes when deciding what to retain. These notes are the source of truth for adoption, omission, integration, reasoning, and remaining uncertainty.

[Category counts](skills/README.md) summarize the adopted changes.

- [Investigation](skills/investigation/README.md) covers understanding behavior and rationale.
- [Implementation](skills/implementation/README.md) covers design, coding, and verification.
- [Orchestration](skills/orchestration/README.md) covers workflow routing, setup, and coordination.
- [Review](skills/review/README.md) covers independent criticism.
- [Writing](skills/writing/README.md) covers framing requests and communicating results.
- [Maintenance](skills/maintenance/README.md) covers learning from completed work.
- [Principles](skills/principles/README.md) covers engineering decisions across workflows.

Each skill has one source link in its owning category index. A skill directory includes its references, playbooks, and scripts. Category placement is organizational, not an adoption decision. The first screen covers all 58 entrypoints. Twenty skill definitions use declared adaptations and 37 are copied unchanged. None remain held; make-bot-ui is omitted by user decision because it assumes Grok Bot’s long lifecycle and seems unlikely to fit T3 Code’s different lifecycle well. The complete source of each newly adopted skill was read; held entries have screening or targeted follow-up notes, not necessarily a full audit of every reference or bundled dependency.

Category README files provide an overview and brief background. Start with skill, T3, Patch, and Design columns. Names link to pinned upstream source. Use ✅ for a change, - for no change, and Pending for held entries; three - marks mean adopted unchanged. These are human review notes, not a machine approval format.

- **T3:** Adapt execution, model/configuration access, storage, or tool discovery to the target environment. Workspace-local storage follows this integration's user instructions; it is not a universal T3 requirement.
- **Patch:** Temporarily reconcile an upstream inconsistency while preserving its intended procedure. Remove the correction when upstream supplies the intended behavior.
- **Design:** Deliberately change reasoning, behavior, or policy for this integration.

These categories overlap; one skill can have several marks. Category counts report each mark independently, not mutually exclusive groups.

Proceed with authorized T3 work. Implement Patch corrections and report them with their retirement criteria. Discuss every new Design change with the user before implementing it, using a concrete proposal and tradeoffs. Existing approved Design scope does not need repeated confirmation. Continue independent T3/Patch work while a Design choice is pending.

[integration-audit.md](../docs/integration-audit.md)

[how-integrate-model-policy.md](skills/orchestration/how-integrate-model-policy.md)

After the table, use one heading per changed skill. Under it, include only applicable **T3**, **Patch**, and **Design** bullets explaining the intent and change briefly, followed by a filename-only link to the integration document, without a prefix or trailing punctuation. Do not create a body heading for an unchanged skill. Link to how-integrate documents for detailed policy, source/reference mapping, evidence, and limitations. Keep held reasons short and explicit. Unchanged skills need no repeated per-skill rationale. The category overview and background are not a run log; detailed verification belongs in the verification record and evaluations.

For each Patch, keep its execution replacements separate from T3/Design changes. In how-integrate, record why it exists, the upstream condition that makes it unnecessary, and the checks needed to remove it. During A-to-B review, inspect the new upstream text and behavior against those conditions. Remove only superseded Patch rules, retaining required T3/Design adaptations. An unmatched replacement is a review signal, not permission to discard the patch automatically.

Do not treat an unevaluated item as omitted. Existing personal skills are not substitutes for upstream features.

For a substantial integration, add `how-integrate-<skill>.md` beside the category README and link it from each affected source entry. Explain the contributing workflows, behavior to preserve, overlap to remove, target files, reference migration, and verification. Keep the plan current when implementation changes it. Create a plan for a real decision, not an empty placeholder for every skill.

The [held-skill review agenda](held-skills.md) groups the 28 holds from the first review response into six work areas. The optional-reference, sequencing/measurement, and initial coordination groups are resolved, and recall has a scoped T3 history adaptation. Teach also retains its investigation depth and progressive visuals with host adaptations. No-comments also integrates independent review with useful documentation and verified simplification. Reflect retains independent review, approved skill edits, and upstream external Backlog delivery. The audit-trail helper and procedure are also adopted with T3 activity/dispatch adaptations. All skill adoption decisions are now resolved: 57 adopted and make-bot-ui omitted. Autopilot automatic delegate stall/approval-wait detection remains an explicit execution gap, not a held skill.

## Source-preserving first batch

The first batch retains source bytes and frontmatter. It adds engineering principles and self-contained writing, request-framing, regression-test, and recurring-mistake guidance without changing T3 execution rules. No fixed models, Cursor dispatch calls, external services, or bundled executable helpers are introduced by these unchanged entries. Required unslop guidance, the linked context-window principle, and the mutually referenced type-system/TypeScript guidance are included.

The post-review addition of type-system-discipline and typescript-best-practices includes the complete patterns reference. Source-only copying does not establish plugin registration or automatic routing. The current trial still uses explicit file-based invocation and host instructions take precedence. Remaining skills can be useful while needing adaptation: initial holds identify unsupported host assumptions, pending skill dependencies, portability work, or toolchain review. Holds are not permanent rejection or judgments that the underlying engineering idea is unsuitable.

## Material outside the top-level skill inventory

The full lock also covers agents, automations, documentation, assets, plugin metadata, and the license. The license is preserved. The comment-sicko agent is imported and adapted for no-comments with pinned-source provenance. Other upstream agents and automations have not been evaluated for inclusion, and the original plugin metadata and assets are not packaged in the current trial. This is the current implementation boundary, not a final omission decision. Documentation remains evidence for evaluating workflows. Report changes to these paths during updates rather than dropping them from the diff.

## Update from A to B

Treat an update as a semantic merge of three inputs: the original source at A, the original source at B, and the current local integration with its review notes. Applying the old transformation rules to B is a generation check, not an adoption review.

1. Keep the current lock, generated tree, and integration notes as the A baseline. Fetch B, then create a candidate snapshot without replacing the lock:

   ```sh
   python3 tools/upstream.py snapshot .agents/cache/cursor-plugins <B-full-sha> > .agents/cache/candidate.json
   python3 tools/upstream.py diff .agents/cache/candidate.json
   git -C .agents/cache/cursor-plugins diff <A-full-sha> <B-full-sha> -- pstack/
   ```

2. Read the actual A-to-B changes, including referenced files, removals, caller changes, and changes in intent. Locate the affected category notes and any integration plans. Compare the changes with the current generated behavior and local adaptations. Do not infer that unchanged replacement anchors mean unchanged semantics. Check each affected Patch's removal conditions and verification requirements, and retire corrections that B makes unnecessary.
3. Write a reviewable update note under `upstream/updates/<A-short>-to-<B-short>.md`. Link the exact A and B sources and affected category notes. Explain what changed upstream, what it means for the integration, what to do, and why. Distinguish the following cases in prose:
   - A change can be included directly without changing the integration design.
   - A change needs adaptation to preserve the current integration intent.
   - The integration plan itself needs revision, including possible removal of local workarounds now fixed upstream.
   - A tradeoff changes user-visible behavior, scope, model policy, or another agreed constraint and needs a user choice.
4. For choices that need user input, show the concrete alternatives, consequences, and recommendation. Keep dependent work pending until that choice is made. Continue independent analysis; do not silently pick an interpretation to make generation pass.
5. Update category decisions, integration plans, implementation, and tests together for resolved changes. Preserve useful upstream additions; copying additions blindly or reapplying the old policy unchanged are not defaults. Remove obsolete local adaptations when B makes them unnecessary.
6. Once the candidate is ready for review, update the lock, central source link, and pinned links in category indexes. Rebuild and run the checks documented in the [project README](../README.md). Source-link refresh is bookkeeping, not evidence that the decisions were reconsidered. Keep unresolved choices explicit in the update note.
7. Present the update note, A-to-B upstream diff, local integration changes, and verification evidence for the user's review. Record the outcome and any remaining limitations. Passing checks does not approve the update or establish semantic fidelity.

The agent prepares and updates this review material. The user reviews the meaningful decisions and changes. Periodic upstream detection is deferred until this workflow is established.

## What tools verify

`python3 tools/upstream.py check` checks that every top-level upstream skill is linked exactly once by a category index, that the links use the locked source revision, and that local documentation links exist. It also checks the preserved license bytes. With `--repo`, it verifies the complete lock against the pinned Git objects.

The checker does not interpret adoption prose, recognize an approval, decide whether an integration is sound, or claim that all pending work is complete. The old `--ready` gate is removed because a status parser would turn these notes back into a machine-owned decision format.

[transforms.json](transforms.json) remains an execution recipe for the currently generated slice: selected source directories, output paths, and exact replacements. It does not decide adoption. The generator checks original bytes, replacement matches, collisions, paths, and generated-file equality. Before changing this recipe, read the corresponding category decision and integration plan.

The [cursor-team-kit dependency](dependencies/cursor-team-kit/README.md) supplies three unchanged support skills with its own pin and MIT notice. They are not included in pstack’s 58-skill adoption denominator.
