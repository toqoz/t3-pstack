# Integration philosophy

## Preserve decisions, delegate execution

pstack's value is how it frames problems, investigates deeply, compares alternatives, seeks independent criticism, and verifies results. T3 supplies execution capabilities. Having a tool does not replace the judgment about when and how to use it.

Keep procedures that affect engineering quality. Adapt tool names, dispatch, waiting, workspace ownership, and provider selection to the current T3 environment. Do not replace those procedures with a generic checklist merely to reduce line count. Reusing host dispatch does not require invoking another pstack workflow or inheriting its model policy. Preserve the upstream workflow dependencies and selection criteria unless a justified Design change is explicitly reviewed.

Patch corrections to upstream inconsistencies are separate from host adaptations and intentional Design changes. Each has an upstream removal condition and verification criteria in its integration policy. Keep the relevant replacement rules independently removable; retire them after semantic A-to-B review confirms upstream now supplies the intended behavior. Record them with behavioral evidence and preserve the intended workflow. The [how adoption note](../upstream/skills/investigation/README.md) records the explainer template correction for the simple path.

Small code means few maintained mechanisms and few handwritten forks. Substantial upstream reference material need not become locally maintained implementation code.

## Keep judgment in reviewable documents

The [upstream guide](../upstream/README.md) identifies the canonical source, pinned revision, license, category notes, and update procedure. Category README files show the skill inventory, T3 adaptations, temporary Patch corrections, and intentional Design changes in a compact table, followed by short explanations grouped under each changed skill, with only the applicable T3, Patch, and Design bullets. They record adoption and held decisions. Detailed integration policies live beside those indexes; verification evidence lives in the verification record and evaluations.

These documents are agent-authored review material, not a serialized database. Do not invent a Markdown status schema, parse the prose to approve builds, or require a hash update for every decision. The tools check source-link coverage, local link targets, original bytes, and reproducible generation. They cannot establish that a judgment is correct or that the user approved it.

Keep structured data only where exact machine comparison is useful. The lock records upstream Git objects. The transformation recipe describes current build operations. Generated provenance explains artifact origins. None of these replaces the adoption rationale.

## Merge upstream changes semantically

Updates compare the original source at A, the source at B, and the current local integration. Read the actual changes and their consequences before deciding how to merge them. An addition may fit directly, need adaptation, invalidate a local workaround, or require changing the integration policy. A deliberate Design change requires discussion with the user before implementation; T3 adaptations proceed within scope and Patch corrections are implemented and reported. Existing approved Design scope is retained without repeated approval.

The agent prepares an update note with evidence, alternatives, implementation changes, and verification. The user reviews that material. Passing exact replacement and regeneration checks proves mechanical consistency, not that the old integration policy remains appropriate for B.

## Keep the adapter thin

T3 owns agent execution, provider/model availability, isolated checkouts, waiting, PR watches, and scheduling. Do not implement a scheduler, agent runner, PR poller, or model ranking table here.

The current generated slice uses declared exact transformations of the original source. Each replacement must match its expected original text once and fail when it no longer does. Local T3 guidance stays separate from generated text. Do not edit generated files by hand.

Model availability comes from T3's runtime catalog. Shared role defaults live in [models.md](../models.md), using Codex for implementation/exploration and Opus for judgment/synthesis. Setup saves user overrides as Markdown. The agent reads the prose and role lines; there is no runtime parser or copied catalog. Unavailable providers/models and unsupported exact task settings require a user decision rather than substitution. Abstract budget and job-derived effort map within the same model's supported options with disclosed rounding. Saved effort configures a starting level; workflows apply the preserved upstream job-based effort/speed rules before dispatch.

The generator bundles shared defaults only in skills whose entrypoint or Markdown references need the T3 adapter or model defaults. Source-only skills do not gain unused execution guidance. A test compares the role names with the upstream setup inventory. Pending workflows reserve role names without claiming the skills are available. Setup retains its original optional verification-skill offers now that both dependency pairs are adopted.

## Expand through verified workflows

The generated slice contains investigation, setup, coordination, design, adversarial review, measurement, and recall workflows alongside source-preserving principles and supporting skills. Retain how's simple-versus-complex decision, focused exploration, separate synthesis, and structured explanation. Retain why's evidence categories, confidence levels, citation checking, and explicit gaps.

Validate generation locally, then exercise realistic requests in T3. Record what actually ran and what remains untested. Coding and review workflows now have explicit host adaptations; live execution remains a separate validation step. Adoption decisions are complete. Full workflow execution and installer compatibility remain separate checks recorded in verification.md; they must not be inferred from adoption or source fidelity.

## Import only reviewed pinned material

A selected skill can import a specific locked source file into a relative reference path. This is used for no-comments' external upstream reviewer definition. The import map is an execution recipe, not an adoption registry: original hashes/modes, declared transformations, destination collisions, and provenance are checked through the existing file pipeline. It does not create a runtime agent catalog or resolve names from installed skills.

Workspace-local `.agents/cache` and `.agents/share` paths follow this integration's user instructions, not a universal T3 API requirement. Keep disposable evaluation/run artifacts out of commits; durable proposals can be reviewed separately.

Reviewed source executables retain their locked executable bit through generation and mode checks. The existing source-mode provenance supplies the desired permissions; no separate script runner or executable registry is added.


## Keep the installable layout conventional

Generated skills live flat under the root skills/ directory, matching common Agent Skills repositories and installer discovery. Category indexes and integration decisions remain under upstream/skills/; do not duplicate their adoption table in the generated container. Local models.md and adapters/t3.md remain build inputs, not a new runtime layer.

Each skill carries LICENSE.txt with the original upstream MIT bytes and, where locally adapted, the project MIT notice. The generator does not alter skill frontmatter for packaging. skills/SOURCES.json combines provenance with the exhaustive generated-file ownership list, including shared references and license sidecars. Writes refuse unmanaged content and symlinks; exact planned files may be adopted to recover interrupted generation, including before the first manifest. Only stale owned files and their empty parent directories are removed. The generator never replaces the repository root.

No dependency resolver is added. Install the complete set to retain sibling references, and keep original directory names. Partial selection, renaming or mixing sources can break dependencies even when an individual SKILL.md is valid. Installation tests use disposable consumers and do not modify the user's environment configuration.
