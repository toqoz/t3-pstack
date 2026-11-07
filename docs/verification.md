# Verification record

## Current scope

The [upstream guide](../upstream/README.md) identifies the pinned source. This record covers the current 57-skill generated distribution, category-index migration, investigation/setup evaluations, coordination and recall adoption, and review follow-up. It does not establish complete pstack coverage or live installation compatibility.

## Executed checks

- `python3 -m unittest discover -s tests -v` passes 50 tests. They cover source snapshots and CLI errors, file modes, worktree independence, source and license tampering, exact non-cascading replacements, overlaps, missing source files, malformed recipes, collisions, output paths, stale or edited generated files, symlinks, model defaults, upstream role names, source-only copying without added execution guidance, and missing cross-skill Markdown links.
- Markdown-index tests cover added/removed skills, duplicate ownership, old source links, central revision mismatch, linked integration plans, and links into planned generated output. They confirm that prose is not parsed as a decision and that reference changes remain visible in the file diff.
- `python3 tools/upstream.py check` verifies the category coverage of all 58 top-level skills against the 573-file lock, local links, and license bytes.
- `python3 -m tools.build --repo .agents/cache/cursor-plugins --write` and `--check` reproduce the current 556 generated files. Nineteen skill definitions use declared adaptations; 37 skills are copied unchanged.
- Ruby's YAML parser accepted all three generated frontmatter blocks and their string name and description fields during the preceding setup work.

The optional Codex skill validator could not run because its Python environment lacks PyYAML. YAML parsing is narrower than host registration validation. No dependencies were installed to work around that gap.

## Markdown adoption migration

The structured decision registry and per-decision fingerprints were removed. At that migration, adoption reasons for how, why, and setup-pstack were retained in category notes and the other 55 skills were unevaluated across seven categories. The subsequent first inventory pass is recorded below. Material outside top-level skills is described centrally rather than represented by dozens of empty decision records.

There is no replacement for the old machine readiness gate. Tool success means objective consistency only. The agent and user must review the adoption prose and A-to-B update assessment; a source-link refresh or a successful build is not an approval. The actual A-to-B update process has been documented, not exercised against a new real upstream revision in this migration.

## First source-preserving adoption batch

All 58 top-level entrypoints received an initial inventory screen. The full source of the 25 new adoptions was read. Each is a single non-executable SKILL.md with no additional bundled files. Eighteen are engineering principles; the other seven are bro, in-your-own-words, sharpen, unslop, technical-writing, tdd, and correct.

The generation recipe uses no replacements for these entries. Their source bytes and frontmatter are preserved exactly. They do not receive unused T3 execution or model reference files. A direct hash comparison against the pinned lock confirmed all 25 copied source files in that initial selection. The common upstream license and artifact attribution remain in the distribution.

That initial selection contained 28 generated skills and 30 holds; the subsequent review response below adds two skills and leaves 28 holds. Host-specific dispatch, automatic model replacement, Cursor transcript/skill paths, unported companion skills/agents, visuals, implicit rebasing, portable measurement commands, and bundled toolchains require follow-up. These are screening reasons, not full runtime audits or omission decisions.

Relative Markdown file links in generated text must resolve within the planned distribution. A test proves a missing cross-skill link fails generation. Separate tests inspect common explicit named-skill forms and canonicalize short principle names; an ordinary mention is not an invocation. This is a limited dependency check, not a parser for arbitrary prose or adoption decisions. Named companions were also inspected when selecting the batch. Behavioral quality, host registration, and all invocation paths have not been independently evaluated for every new skill. Source fidelity is distinct from those claims.

## Opus review of the source-preserving batch

Opus 5.5 independently read the initial 25 unchanged skills, inspected their named and linked dependencies, verified all 28 then-generated frontmatter blocks, and reran the 34 tests, lock comparison, and 52-file regeneration check. It found no defect requiring removal of those adoptions. This was a source and compatibility review, not a behavioral evaluation of every skill.

The response clarifies that guard-the-context-window does not authorize dispatch and that correct can request commits, CI changes, and instruction edits only within host rules. File-based invocation installs no persistent trigger. General writing advice yields to the requested language and repository formatting.

The README now requires reading the whole skill, including its frontmatter description, and resolving named pstack companions to this distribution's files rather than installed variants or slash commands. Short principle references resolve to their canonical principle-prefixed names. A user's explicit request for another source still takes precedence.

After reading the full TypeScript pattern reference, the parent adopted type-system-discipline and typescript-best-practices without source changes. Their principle companions are present. Preserved paths metadata does not imply automatic activation. The distribution now contains 30 skills, of which 27 are unchanged, and 55 files in total. Every unchanged file matches its pinned upstream hash.

The parent kept prove-it-works, build-the-lever, and attack-the-premise scoped out pending interpretation of the optional show-me-your-work example. The notes now explicitly distinguish that optional mention from a mandatory dependency and do not call commit guidance itself a T3 conflict. This remains a conservative hold, not a permanent rejection.

Tests cover missing named unslop, short principle resolution, ordinary non-invocation mentions, and explicitly deferred companions. Shared adapter/default detection now scans all Markdown files in a selected skill, not only the entrypoint. Documentation about bundling was corrected accordingly.

This review predates the parent's final fixes and two added adoptions; there was no additional independent re-review. Thirty final frontmatter blocks were parsed successfully with Ruby, with names matching their directories. Japanese prose behavior and TypeScript example compilation were not evaluated.

## Held-skill classification and first follow-up

The [review agenda](../upstream/held-skills.md) accounts for every one of the 28 holds that existed after the type-pair adoption. It groups them by optional-reference interpretation, local procedure/portability, delegation/review mechanisms, history/audit access, verification toolchains, and media/external integrations. Category notes remain the decision authority.

Before changing this selection, the existing 30-skill distribution passed all 39 tests and its 55-file generation check. The parent then reread prove-it-works, build-the-lever, and attack-the-premise. The audit-trail reference is an illustrative parenthesis, not a required execution step. All mandatory linked companions are present when these three are added together. No source replacement or new runtime mechanism is needed.

The three principles are now included unchanged, with host authorization/dispatch/commit rules preserved by the invocation instructions. The named-reference test explicitly allows only the illustrative show-me-your-work mention in prove-it-works, alongside setup's already-deferred verification offers. This does not adopt the audit workflow or claim its external dependencies are available. A task that actually needs it must report the gap.

The resulting artifact has 33 skills and 58 files, including 30 unchanged skills with 31 original files. All unchanged files match the pinned source hashes. The common license remains byte-for-byte intact. All 39 tests, Markdown/source checks, and regeneration checks pass. The new three principles have not received a separate behavioral evaluation or another independent review. Twenty-five skills remain held; next is sequence-verifiable-units' unconditional rebase instruction.

## Sequencing and measurement follow-up

The parent adopted sequence-verifiable-units with one source replacement: identify the task's authorized baseline, including relevant uncommitted changes, and follow host branch/checkout-ownership rules instead of requiring a clean-trunk rebase. No rebase/reset or checkout change was performed. The resulting file matches exactly that declared transformation; the 39 tests passed before moving to the next unit.

Benchmark-checklist has four exact replacements covering portable load/capacity observation, host-appropriate profiler selection, standalone PR reporting, and optional performance-playbook integration. Its seven questions and ballpark/decision distinction are retained. Principle-explain-the-number is copied unchanged with its mandatory benchmark companion now present.

The [measurement exercise](../evals/measurement-checklist.md) ran `python3 evals/measurement_check.py` on identical synthetic controls. The parent inspected the raw samples and report under `.agents/cache/measurement-checklist/`, verified alternating trial labels, all work/output checks, warmup/profile exclusions, and source/function profile records. The exercise records a timestamp and its script hash. Its verdict is inconclusive, not a product speedup: effective quota/affinity, production configuration, and user-facing end-to-end relevance remain gaps. This is evidence that the procedure can collect and qualify a small measurement, not an independent agent behavioral evaluation of every checklist rule.

The current distribution has 36 skills and 61 files. All 39 tests, source/index checks, source-fidelity checks, and regeneration checks pass. Twenty-two skills remain held; next is shared delegation through swarm before arena and the dependent wide-change paths. No additional Opus review covers these final three adoptions.

## Earlier behavioral how runs

Before the Markdown migration and before role-specific defaults, the coordinator selected how's simple path and dispatched one native explainer in T3. The inherited model supplied an independent context, not model diversity.

The first run explained the then-current decision-fingerprint gate and found that the shared explainer template assumed explorers had already run, contradicting the simple path. A declared transformation made the template conditional. A fresh explainer then checked exact-replacement behavior against the code and tests and reported no ambiguity in the corrected simple path. The coordinator inspected the report and checked its core claims. The old decision-fingerprint explanation describes the earlier implementation and is not a guarantee of the current Markdown review process.

## Earlier Markdown setup evaluations

The user chose Codex/Opus defaults and a plain Markdown preference file. All 17 upstream role names are retained, and the same default document is bundled only in skills whose entrypoint or Markdown references need the T3 adapter or model defaults.

Two independent native agents evaluated setup with synthetic catalog fixtures under `.agents/cache/model-setup-eval/`. They did not invoke providers, read personal configuration, or use connected accounts. The [reusable evaluation prompts](../evals/setup-pstack.md) describe these cases.

The supported case saved 17 unique role lines for the small budget, mapped reasoning options to medium for each provider, preserved panel order, and kept how explorer as inherit-parent without options. Re-running required no changes. The coordinator inspected the actual file.

The unavailable case disabled the Claude provider while retaining an existing Opus preference. The evaluator requested a concrete choice without substituting a model or shrinking panels. The coordinator verified that the existing file remained byte-for-byte unchanged.

## Earlier Opus review

Opus 5.5 independently reviewed the initial slice, ran the then-current 19 tests, verified the lock, compared generated files with upstream, and checked the license bytes. It reported no blockers. Findings led to clearer coordinator/child boundaries, preserved Present rules, connector access requirements, accurate adoption reasons, non-cascading replacements, improved errors, explicit source hash names, and an attribution NOTICE.

That review predates the shared Markdown defaults, setup work, and adoption-document migration. It is not an Opus approval of the current state. No upstream issue was filed.

## Remaining checks

Why's full evidence-category fan-out and synthesis and how's complex path have not run. Dispatch using saved role preferences, cross-provider settings, installation, and plugin registration have not run end to end. Setup's failure behavior used a synthetic catalog. Personal configuration has not been changed. CI is configured but has not run on GitHub. A broader poteto-mode entrypoint and coding workflows remain absent.

## Swarm integration

Swarm is adopted with three declared replacements for model resolution, T3 dispatch and checkout ownership, and dropout/race termination. The [integration policy](../upstream/skills/orchestration/how-integrate-swarm.md) records the preserved procedure and semantic update criteria. No new runner, configuration parser, or scheduling mechanism was added.

An independent native agent read the generated entrypoint and bundled model defaults against three synthetic scenarios, without spawning workers, reading personal configuration, or invoking providers. It requested a choice for an unavailable saved model, retained a coverage gap after one retry still omitted the required SHA, and declined dispatch where required uncommitted inputs could not reach an isolated checkout and shared writes overlapped. It found a native race-interruption ambiguity; the final text now follows host interruption support and drains completion if interruption is unavailable. That final clarification was inspected by the parent, not independently re-evaluated.

The distribution now contains 37 skills and 64 files; 21 skills remain held. All 39 tests and source/index/regeneration checks pass. These checks and the synthetic evaluation do not establish live dispatch, worktree input transfer, or cancellation behavior. No additional Opus review covers swarm. Next is arena.

## Candidate and review workflow batch

Arena, architect, and interrogate now have declared T3 adaptations; blast-radius is copied unchanged after its arena dependency became available. The [integration policy](../upstream/skills/orchestration/how-integrate-arena.md) records preserved candidate independence, cross-family judging, verified review inputs, and semantic upstream-update review. All architect reference files were read and retained; only its runner prompt receives the declared coordinator/child boundary clarification.

The current distribution has 41 skills and 73 files, leaving 17 holds. All 39 tests passed after generation. Exact transforms, planned links, and source hashes are checked by the existing generator. This is artifact validation, not proof of live panel execution or uncommitted-file transfer. Independent Opus review was attempted but could not start: T3 returned `provider_unavailable` because Claude Code is not authenticated. A refreshed capability catalog confirmed `claudeAgent` cannot run child tasks. No substitute provider was used. Review remains pending authentication; no live arena/architect/interrogate run has been claimed. The [repeatable instruction scenarios](../evals/coordination.md) distinguish synthetic assessment from live execution.

## Recall and helper packaging

Recall is adopted with six replacements for scoped T3 history discovery, missing companion routes, worker dispatch, execution evidence, unknown status, and thread citations. A live current-project `t3_thread_list` call returned only the active top-level conversation. A one-item activity read of that already active conversation confirmed pagination metadata and the opening user message. The probe did not inspect other projects or mine prior conversations. No exhaustive recall, mining fan-out, or shared-record sweep ran.

Model-only workflows now bundle only model defaults, without the investigation adapter's write restrictions. A targeted test verifies that separation while retaining the adapter's model dependency. Existing source-only and reference-triggered helper tests still pass.

Current totals: 42 skills, 72 generated files, 40 passing tests, and 16 holds. Ruby parsed all 42 generated skill frontmatter blocks and confirmed matching names and string descriptions. The parent also checked the selected count, absence of the investigation adapter in swarm/arena, its presence in how, and byte-identical upstream license packaging. At that point the coordination Opus review was blocked by Claude authentication, with no model substitution. The completed review and response are recorded below.

## Opus coordination review and response

After reauthentication, Opus 5.5 independently reviewed swarm, arena, architect, interrogate, blast-radius, recall, and helper packaging. It ran all 40 tests, source checks with and without the upstream repository, generation checks, independent source-fidelity/provenance probes, license comparisons, and frontmatter parsing. It confirmed exact source-plus-transform output, 42 selected skills, 72 generated files, and retained licenses. Its scenario assessment was synthetic, not live worker or history execution.

The parent addressed its findings in the source transformation recipe and policies:

- Interrogate no longer assumes an unspecified host input-transfer API. Arena now defines two ordered scoped binary Git patches, declared untracked/ignored payloads, and an index/worktree manifest; children apply them inside a T3-created checkout and verify the baseline. The parent added and ran the [local Git replay exercise](../evals/input-bundle.md), covering mixed staging, rename, deletion, executable mode, binary content, untracked and relevant ignored inputs, symlinks, and tamper detection. This is not a live T3 checkout or bundle-access test.
- Arena retains upstream candidate expansion by cycling configured panel entries. Launch rejection is distinct from post-launch dropout; an unavailable seat cannot silently reduce the requested comparison. Judge eligibility is preflighted before candidate work, with unknown parent family explicit.
- Child briefs carry distribution-local absolute reference and companion paths. Architect candidates produce their design package and execute no coordinator phase. The rubric is withheld from runners but given to the judge. The judge preserves candidate directories; writing checks need its own scratch copy.
- Recall now qualifies uncertain filter defaults, unknown ordering, run metadata caps, last-activity windows, active delegate exclusion, and completed-result delivery effects. Worker tool access, multi-page traversal, and filter defaults remain untested. Its configurable swarm-default cost tradeoff is explicitly recorded rather than presented as upstream's fast/cheap model choice.
- Shared model prose now distinguishes grouped role labels, panel/pool lists, singleton roles, saved explicit options, and default effort overridden by a saved budget. Stale scope and adoption counts were corrected.

The final corrections were inspected and checked by the parent, not independently re-reviewed by Opus. The repeatable instruction scenarios include launch rejection, reference resolution, judge write isolation, and uncertain recall coverage; they remain prompts for future behavioral runs, not claimed completed live evaluations.

## Merged no-comments adoption

The user approved combining partial no-comments discipline with A Philosophy of Software Design: prefer verified structural simplification, remove resulting redundancy, retain/add useful intent and contracts, and reject refactoring that increases reader complexity merely to erase prose. Constraint warnings remain until an approved replacement guarantee is implemented and verified. The [policy and primary-source citations](../upstream/skills/review/how-integrate-no-comments.md) distinguish the book's ideas from local operational decisions.

The generator now imports a specifically mapped pinned source file through the existing hash/mode/transform/provenance pipeline. The adapted comment-sicko reference records its original agents/comment-sicko.md source hash and mode. Four new tests cover imported output/provenance/transformation, unsafe/unpinned input, destination collisions, and source tampering. No runtime agent registry or book text is bundled.

Two independent native evaluators were used under the skill-creator forward-testing guidance. The reviewer read the generated role and a raw code/task/test fixture without expected answers; it proposed replacing redundant arithmetic narration with a monotonic-clock contract and adding accurate retry documentation. It preserved the legal notice, internal design rationale, unapproved protocol constraint, and existing slicing contract, with no structural changes. The parent inspected the patch/report, applied the patch only to a disposable copy, verified executable AST equality excluding docstrings, checked retained context, and reran three passing fixture tests. The reusable raw fixture is under evals/fixtures/no-comments; the actual run artifacts are under .agents/cache/no-comments-eval.

The separate coordinator evaluator assessed six supplied reports and rejected application-code edits, stopped after a second invalid report, retained an unapproved constraint, allowed a useful contract addition, removed obsolete prose after an already verified simplification, and rejected unnecessary forwarding helpers. This was an instruction assessment, not live workflow dispatch. It found implicit approval wording; the parent made approval explicit and clarified that architect is used only through its sketch, without introducing a human design checkpoint. Those final wording changes were parent-inspected rather than independently rerun.

Teach was also adopted in the preceding unit with four exact replacements preserving investigation depth and progressive visuals while adapting language, host display, coordinator ownership, and confidence language. It has not had a live teaching/visual run.

Current totals are 44 adopted skills (12 adapted, 32 unchanged), 14 holds, 76 generated files, and 44 passing repository tests. Live no-comments role-model dispatch, T3 checkout input delivery, how/why evidence exchange, full architect integration, and an actual rejected-report retry remain untested. The earlier Opus coordination review predates teach and no-comments; these additions are not claimed as Opus-approved.

## Reflect adoption and category overview

Reflect retains all three reviewer templates, separate synthesis, structural-enforcement routing, untrusted-input boundaries, and explicit edit approval. Declared transformations adapt active-thread/digest access, Markdown models, T3 dispatch, actual skill usage/source paths, and host authoring capabilities. Local proposal/Backlog storage replaces automatic external filing and is identified as an author-level policy change. No generator changes were needed.

An independent native evaluator used the generated synthesis template with a raw synthetic transcript, three full reviewer reports, and two real fixture target files. It read those targets, proposed a repeated missing handoff requirement, rejected provider advice already covered by the target, merged duplicate findings, routed a cheap structural check to Backlog, and ignored embedded external-filing directives. It wrote only its result under .agents/cache/reflect-eval. A separate independent coordinator assessment covered generated targets without approval, unavailable lenses, digest-only evidence, managed source ownership, and missing authoring tools. The parent inspected both actual reports and clarified installation-scope wording and visibility of accepted-but-pending rows; those final wording changes were not independently rerun.

The [repeatable evaluation](../evals/reflect.md) and raw fixtures distinguish component/scenario evidence from full workflow execution. No full live three-reviewer/synthesizer sequence, provider resolution, connector lookup, history pagination, approved skill edit, or description optimization ran. These evaluations are not an Opus review of the addition.

The [skills index](../upstream/skills/README.md) initially recorded mutually exclusive T3-only, design-only, and both counts from the human-reviewed category notes; the classification revision below supersedes those columns. It is a readable overview, not a parsed decision registry or approval gate. Current totals: 45 adopted, 13 held, 82 generated files, and 44 passing repository tests.

## T3 / Patch / Design classification

Category tables and skill-level explanations now distinguish host adaptation (T3), temporary upstream-intent correction (Patch), and deliberate integration policy (Design). How's simple-path template correction moved from Design to Patch. Teach's hedging clarification is a Patch; its language choice remains Design. Other adopted changes were reviewed against their recorded reasons, with no skill behavior, selection, or execution recipe changed.

The how and teach integration policies identify the exact independent replacement groups, why each Patch exists, the upstream conditions that make it unnecessary, and the verification needed to retire it. A-to-B review must assess those conditions and remove only superseded rules while retaining required T3/Design adaptations. An unmatched replacement is a review signal, not automatic retirement. No new upstream revision or actual Patch retirement was exercised.

The skills index counts marks independently: one skill can contribute to more than one column. A one-off consistency check compared all 58 category rows with the existing 45 selected skills and their declared replacements, confirming unchanged/held entries remain distinct. The documentation change does not add a runtime classification parser or approval gate.

## Recall direct-mining correction

The user challenged the added swarm dependency and its model-policy consequences. The integration had reused an entire coordination skill for implementation convenience, importing its xhigh worker default without evidence that recall needed it. That design change is withdrawn. Recall now dispatches its own parallel mining roles directly through T3, preserving upstream's fast/cheap criterion, one/two-chat direct path, topic/window boundaries, per-chat schema, shared why investigation, and live-state verification.

No new default model, role, budget rule, or runtime framework was added. Explicit task choices still take precedence; unknown speed/cost suitability requires a supported choice rather than guessing or borrowing another workflow's settings. The unverified output label remains a separate Design change, so the category marks and aggregate counts remain unchanged. Historical notes about the former shared-worker policy describe the earlier implementation and are superseded here.

An independent native evaluator read the corrected entrypoint and policy against four synthetic cases: known fast/cheap versus another workflow's expensive default, an explicit task model choice, two-chat direct reading, and a catalog without speed/cost evidence. It selected by recall's own criterion, respected the explicit choice, retained direct reading for two chats, and requested a supported choice when suitability was unknown. It found no residual coordination-skill dependency and confirmed the scoped schema, why sweep, and live-state verification remain in the instructions. The parent inspected its actual result under .agents/cache/recall-direct-eval. This was an instruction assessment, not live dispatch or history access. All 44 repository tests, 573-file source/index checks, and the 82-file generation check passed.

## Integration scope audit

The user clarified that the scope is host integration, removable upstream-intent patches, and explicit design changes worth reconsidering. The parent compared all 13 adapted skills' pinned sources, references/imports, replacements, generated instructions, and model choices. A limited named-companion comparison found added arena references in reflect and no-comments, used only to share dispatch mechanics. Both are removed; their parents now directly dispatch their original roles and preserve their own model choices and procedures. Original arena relationships in architect/interrogate and how/why relationships elsewhere remain. No new runtime abstraction was introduced.

Setup also no longer reads the investigation adapter: its source-edit prohibition conflicted with setup's approved configuration-write role. Setup retains its own catalog, validation, and write procedure plus shared model defaults. The now-unused adapter is absent from setup's generated directory, reducing output to 81 files. Its prior synthetic model-setup evaluations did not expose this instruction conflict and are not proof that the old boundary was sound.

The [audit](integration-audit.md) separates accidental reuse from remaining Design review questions. Current policy questions are arena's stricter reduced-review handling, sequencing's baseline change, reflect's default local backlog, and recall's unverified label; discussed language and comment-quality changes are recorded separately. Their classification is not a claim of necessity for T3 or benchmark-proven benefit.

All 44 tests passed after the corrections. A one-off comparison found no newly introduced recognized named-skill dependencies in any of the 13 adapted skills; the scanner remains limited to known name patterns and is not semantic proof. Source/index, exact regeneration, and helper/provenance checks are run separately. No full live execution of all corrected workflows is claimed. An independent scope audit is requested separately below.

Reading the upstream Subagents section exposed a further unresolved model-policy mismatch: the original workflows reference job-based effort/speed adjustment, while current T3 resolution does not state that adjustment. The audit records the source and a concrete correction proposal, including the distinction between a starting preference and an explicit fixed effort requirement. No model settings or personal configuration were changed; this issue remains open pending policy clarification and independent review.

## Opus scope-audit response and starting-effort restoration

Opus independently compared all 13 adapted skills and relevant references with pinned pstack, including the original Subagents and setup rules. It confirmed exact generation, 32 unchanged source skills, retained licenses, 45 selected skills, and 44 passing tests. It found that per-job effort/speed adjustment had been lost, and identified additional confirmation gates and weakened source requirements.

The user explicitly chose saved effort as a starting preference, with current-task exact settings fixed. Shared models.md now preserves the original ladder adjustment, standard/urgent speed, explicit delegated-verification model/speed exception, aliases, supported same-model rounding, and settings-aware native/delegate boundary. The common model policy is read by each direct role owner; recall reads effort rules without inheriting any other workflow's model. Setup uses its original abstract-budget rounding in the existing proposal, distinct from unsupported exact user options. No new accelerated default or personal setting was written. Codex speed-option meaning was checked against official OpenAI documentation and recorded with the host-capability qualification.

Other corrections scope judge preflight to Phase C, restore autonomous recall selection without price-metadata questions, retain progressive SVG teaching when image generation is absent, restore the real-baseline objective and freshness gaps, and require all four benchmark observation categories or explicit unavailable evidence. Recall's unverified follows attempted live verification, and unadopted session pickup is reported as a gap rather than replaced by an extra mini-workflow. Reflect reuses existing authorization and combines new delivery choices with the existing approval; its local-first policy and reduced-lens confirmation remain explicit Design questions.

Two independent native evaluators assessed actual generated instructions against synthetic catalogs and task cases. One resolved routine, judgment, ordinary, hardest, saved-medium, fixed-low, urgent, verification, incidental citation-check, and inheritance scenarios; it also confirmed autonomous recall selection without measured-cost claims. The other assessed abstract unlimited versus exact unsupported max, interrogate without a judge, SVG fallback versus PNG-only, missing benchmark observations, and attempted-verification gating. The parent read the actual reports under .agents/cache/effort-eval and clarified option preservation during setup mapping, explicit task-model precedence, and the Phase-C-only qualifier. These final clarifications were parent-inspected, not another independent rerun.

No real provider dispatch, speed/price benchmark, full three-lens run, history traversal, visual renderer, managed skill edit, or new upstream update was exercised by these tests. The unchanged role inventory remains 17 lines and no runtime model parser or extra workflow dependency was added.

Final parent verification passed all 44 repository tests, the pinned 573-file source/index check, and the 82-file generation check. All 45 entrypoint frontmatter blocks were parsed, imported license bytes and helper boundaries were checked, and the limited named-companion comparison still found no added workflow dependencies across the 13 adapted skills. Shared rule clarifications also make explicit task-model precedence and settings-aware delegation unambiguous. These are artifact/instruction checks, not live performance evidence.

## User-directed restoration of upstream decisions

The user chose original pstack behavior where no useful deliberate Design direction had been established. Arena again proceeds with an omitted judge or candidate dropout as upstream permits, reporting missing coverage rather than adding a reduced-review approval gate. No unavailable requested model is substituted without authorization. Sequencing is now copied byte-for-byte, restoring clean-trunk rebase instead of imposing a different agreed-working-state baseline. Recall's added unverified tag is removed; evidence gaps do not authorize unsupported status claims.

Reflect again files Backlog in the project's/team's external tracker, such as GitHub Issues, Notion, or Linear. Actual destination and host external-write/publication authorization are handled separately from Accepted skill-edit approval. Local drafts are temporary, not the durable default. The synthesizer's original external-filing instruction is restored, and incomplete role execution is reported without a new reduced-workflow approval gate. No issue, page, message, or external item was created while authoring this correction.

The new project AGENTS.md persists the user's operating rule for future work: authorized T3 adaptation proceeds, Patch corrections are implemented and reported with retirement criteria, and every new Design change is discussed before implementation. Already approved Design scope is not reconfirmed. Category notes and the aggregate index now retain Design only for no-comments and teach's language choice. Current selection remains 45 skills: 12 adapted and 33 unchanged, with 13 holds.


## Decision-trail adoption and executable packaging

Show-me-your-work is adopted with T3-only adaptations: distribution-local helper paths, workspace-local operational storage, scoped T3 activity evidence, and direct cross-family reviewer dispatch. Its six-column log format, append-only corrections, ownership stretches, and required review remain upstream procedures. The selection now contains 46 of 58 skills: 13 adapted and 33 unchanged, with 12 held.

The generator preserves pinned executable modes and checks mode drift alongside bytes. Regression checks execute a generated helper, detect and repair lost execution permission, and reject executable Markdown drift. Two tests exercise the actual unchanged decision-log helper: UTC timestamps, six-column output, cell sanitization, append preservation, and invalid argument handling. No shell worktree or additional runtime dependency was introduced.

An independent native evaluator read the generated skill and synthetic activity/log fixtures. It identified a false success claim and an omitted pivot, proposed append-only corrections limited to the owning conversation, and distinguished actual model family from provider identity. It did not execute the cross-family review or a live activity audit. A minor upstream reporting ambiguity remains: the required reviewer-model line cannot truthfully name a completed reviewer when review is incomplete. In that case, report the incomplete review explicitly; never invent a reviewer or claim completion.

A separate independent evaluator checked restored arena, reflect, sequencing, and recall instructions against synthetic scenarios and pinned source. It confirmed reported judge/dropout handling without the extra approval gate, external Backlog delivery independent of Accepted-edit approval, byte-identical sequencing, and the original recall status contract. These were component assessments; no provider, external tracker, actual rebase, or live history traversal was invoked.

Final repository checks cover 47 tests, all 573 pinned files, and 86 generated files. The adopted script and template remain byte-identical to upstream, including executable permission on the script. Live end-to-end decision-trail auditing and cross-family review remain unverified.


## Minimal verification and catch-up adoption

The user approved changing only `.cursor/skills/` to `.agents/skills/` in create-verification-skill and maintain-verification-skill. Both are adopted with those path-only replacements. A direct comparison confirmed every other byte and all three creation templates remain unchanged. Host storage, orchestration, and driving-tool rules are not duplicated in the skill. No generated verification skill or live maintenance session was executed.

Ketchup is adopted with two exact replacements mapping `/visualize` to available host visualization tools. Ketchup-video is copied unchanged. Their companion links resolve; no renderer is bundled or invented. Live catch-up, rendering, frame inspection, and media playback remain untested.

The current distribution contains 50 skills: 16 adapted and 34 unchanged, with 8 held. All 47 repository tests, the 573-file pinned source comparison, and the 93-file generation check passed.

## Statechart investigation, not adoption

The pinned statechart implementation uses TLC 1.7.4 with a SHA-256, Java through mise by default, and an existing-runtime override through TLA2TOOLS/JAVA. Its rendering reference specifies Pele 1.9.0. No toolchain or renderer was installed and no third-party runtime artifact was added to the distribution. Statechart and the formal-verification pair remain held.

Four original Node test files exercised parsing/chart generation, pipeline boundaries, and CLI replay fixtures. The initial run passed 192 of 193 tests; the symlink-launch test failed before subprocess output was available. Repeating that test with TMPDIR set to a canonical workspace-local cache path passed. The test constructs a relative symlink between temporary and source paths; macOS temporary-path aliases affect that setup. No upstream script was changed. These checks use recorded TLC output and simulated Java behavior; they do not establish actual model checking or Pele rendering.

## Next integration boundary

Make-bot-ui targets a Cursor Grok Bot webhook routine, including Cursor-specific creation, credential UI, request headers, and wake payloads. The current T3 schedule_task schema exposes webhook schedules, returned webhook URLs, and optional signature verification, so a host replacement is plausible. No scheduled task, secret request, webhook, server, or tailnet was created during inspection. Decide whether to include this Cursor-bot-specific workflow as a T3 agent UI before implementing its replacement lifecycle.


## Bot UI prerequisite probe

The user approved T3 agent webhook adaptation conditional on demonstrated operation. A disabled webhook schedule bound to the current thread was created through the actual T3 tool. No webhookUrl was returned; the tool contract identifies missing T3 Connect remote access. The disabled probe task was deleted successfully. No HTTP request, wake, UI, secret, server, or network change was made. Make-bot-ui remains held, and the selected distribution stays at 50 skills. Its integration plan records the actual prerequisite and the remaining browser/server/authentication/wake acceptance path.


## Tailnet versus relay correction

The earlier missing-webhookUrl result was incorrectly treated as proof that remote access had to be enabled. Installed T3 0.1.7 source maps show separate local hook paths and relay URLs: `/api/hooks/:hookId/:token` exists independently of relay URL construction. MCP response visibility also has additional conditions. A harmless request to a nonexistent hook over the existing tailnet HTTPS origin returned HTTP 404. This establishes reachability only, not a valid token or task wake. The integration plan now investigates direct tailnet delivery rather than requiring T3 Connect. No configuration was changed.


## Tailnet Serve discovery and credential boundary

`tailscale serve status --json` confirmed existing HTTPS reverse proxies on ports 443 and 3373 targeting the T3 loopback server on port 3773. This is Tailscale Serve, not Funnel. No Serve configuration was changed. A new browser profile was unpaired on both loopback and tailnet origins; the MCP scheduled-task response omitted the local webhook path even with the probe enabled. The browser was closed, the private pairing request was declined, and the probe task was deleted. No real webhook wake has been established. Browser pairing is a management-session requirement in this verification route, not evidence that webhook senders must pair for each request. The integration remains held.


## Bot UI omission and formal-checking adoption

The user omitted make-bot-ui because it assumes Grok Bot's long lifecycle and seems unlikely to fit T3 Code's different lifecycle well. This is a fit judgment, not a finding that the webhook cannot work. The root skill index records the reason. No active probe remains.

Statechart and both formal-verification skills are now copied unchanged. The exact pinned TLC 1.7.4 JAR checksum matched. With existing Node 24.14.1 and an ephemeral Nix JRE (Zulu OpenJDK 21.0.11), actual TLC runs passed Counter and MediaPlayerFixed. MediaPlayer exited 1 and reported the one-step LoudWhenStopped invariant violation. Pele 1.9.0 rendered the fixed-model Mermaid to a 26,640-byte SVG. The parent's initial render attempt used an incorrect package entry path; resolving Pele's package export fixed that invocation without changing upstream code.

Runtime dependencies remain in disposable cache or the Nix store and are not bundled into dist. No environment configuration was edited, and default mise provisioning was not tested. The original statechart source, tests, and fixtures are packaged as a whole directory. These are fixture-level checker/renderer checks, not proof of correspondence to a product or visual inspection of the SVG. The full generated formal-skill creation/maintenance cycle remains untested. See [the integration record](../upstream/skills/implementation/how-integrate-formal-verification.md).

All 47 repository tests, the 573-file source check, and the 502-file generation check passed. The distribution has 53 adopted skills (16 adapted, 37 unchanged), 4 held, and 1 omitted. The remaining held routers are automate-me, figure-it-out, poteto-mode, and poteto-help.


## Supporting dependency and bespoke workflow adoption

The user authorized continued adoption of the existing cursor-team-kit dependencies. Deslop, control-ui, and control-cli are copied unchanged. Their separate package lock records the canonical Git repository and commit; the original Cursor MIT notice is retained alongside pstack's Lauren Tan notice. The generator verifies each package's Git objects, rejects output collisions, combines source identity/provenance, and preserves executable modes. CI fetches every distinct pinned package revision. The source snapshot and diff CLI can target the dependency independently, retaining A-to-B review rather than silently following pstack's pin.

Three regression tests cover separate sibling-package inventory/identity, dependency license/provenance/mode retention, and collision rejection before mutation. All 50 repository tests pass. Source/index checks passed, and direct byte comparisons confirmed all three supporting entrypoints and their license unchanged.

Figure-it-out is adopted with its original phase procedures. Its original Principles-section dependency is imported from the pinned poteto-mode entrypoint and extracted using exact source replacements. A direct comparison confirmed the resulting section is verbatim. Model adjustment uses the already reviewed models.md translation without introducing swarm as another workflow dependency. The full mode router remains held. Now that both verification pairs are present, setup's original two optional offers are restored with distribution-local companion resolution.

Current pstack selection is 54 of 58 (17 adapted, 37 unchanged), with 3 held and make-bot-ui omitted. Three additional unchanged cursor-team-kit support skills are separate from that denominator. Generation produces 509 files. No live bespoke migration, long-running program, or supporting UI/CLI control run was executed in this batch. The next review boundary is Orchestrate's fresh cloud VM default versus shared-machine T3 worktrees; the integration plan records the distinction without claiming equivalent isolation.


## Poteto-mode candidate and live interrogate prerequisite

The user approved the cloud-VM to T3-managed-worktree mapping and requested separate actual interrogate verification. A poteto-mode candidate is generated with declared host adaptations: worktree-based workers, shared role preferences, explicit child/distribution paths, scoped T3 activity, native PR-watch waits, and corresponding plan-check markers. The original workflow graph, phase/review/merge gates, and Comments section remain. Mandatory unsupported supervision is reported as blocked, not silently waived. The candidate adds no scheduler, VM provisioner, or worktree manager.

All 7 generated check-plan tests pass, and all 50 repository tests pass. Generation currently produces 554 files including this review candidate. Adoption status for the mode remains pending independent Opus review; the previously accepted pstack count remains 54 until review is resolved. No long-running program or live PR lifecycle was executed.

An actual delegate_task with isolation=worktree failed with invalid_request: "Unable to resolve the parent checkout commit." The parent HEAD is unborn. No child agent started, and no live input replay was verified. The fixture and next-step procedure are recorded in evals/interrogate-live.md. No initial commit or shell-created child checkout was made to bypass the host prerequisite.


## Opus corrections and authorized empty baseline

Opus independently rejected the first mode candidate pending F1–F9 corrections. The parent restored the hardest-task/prose/code model tiering and file-pointer rule, removed stale executable Cursor model defaults, aligned pinned-distribution reads, removed unavailable cleanup buckets, and made child owner/coordinator wait ownership explicit. The original readiness/Bugbot policy remains available through watch-pr --status-only only, from a disposable copy with frozen dependencies; all waits use host events. The combined upstream plan/readiness/GitHub/CLI tests passed 61 cases with fake clocks/readers, including one-shot classification. No live PR watcher was run.

Hourly drift audit plus stalled-worker replacement is explicitly not yet integrated or verified. Unattended Autopilot-full/stack execution remains blocked until that original requirement is satisfied; the plan and execution instruction no longer arm an incompatible probe loop. T3's interval scheduling schema does not by itself prove that composite supervision. No Design change was used to declare weaker supervision successful. These corrections were parent-inspected, not another delegated review.

The user explicitly authorized an empty initial commit. Commit 5ed8f181ab24f9b35348c5e3adcdd7473c3dd8c8 contains zero files and was not pushed. Controlled fixture additions were then temporarily staged in the parent, with further unstaged edits, mode/binary changes, deletion, rename/payloads, relevant ignored data, and symlink captured into a two-state manifest. Other project artifacts remain uncommitted. Live reviewer results and cleanup are recorded after completion, not inferred from this preparation.


## Completed live interrogate replay and cleanup

After the authorized empty baseline, actual T3-managed Codex and Opus worktrees both started clean at that same SHA with no fixture files. Each verified patch hashes, applied staged then unstaged binary patches, restored declared payloads/symlink, and matched the separate index/worktree manifests. Corruption of the child-local untracked payload failed the worktree comparison, and restoring it recovered both matches before review. Both executed the actual replayed bounds.py and reproduced the inclusive-limit defect; Opus also demonstrated the staged version passed the same boundary. Evidence and reproduction commands were retained in the run cache.

The parent checked both real worktrees, including head, distinct checkout, actual index/worktree state, and identity of copied evidence. It then removed only the exercise fixture/index entries in those children, preserved proof and host-managed checkout metadata, and restored the parent fixture byte-for-byte and mode-for-mode to the saved original. Parent index is empty again. The only commit remains the user-authorized empty initial commit, with no files and no push.

This establishes actual T3 two-provider dispatch and input replay for the fixture. It does not establish a full interrogate coordinator workflow, live application review, arbitrary permissions/ACLs, a committed-file rename scenario, or all runtime isolation conditions. The child report's generic cross-provider disclaimer does not negate the parent-observed Codex/Opus dispatch; the scope is this observed case only.

Poteto-mode is adopted after the independent review and parent corrections. Current selection is 55 of 58 pstack skills (18 adapted, 37 unchanged), with 2 held and 1 omitted, plus 3 unchanged team-kit support skills. Hourly active-worker audit/replacement remains an explicit blocked capability for unattended Autopilot-full/stack execution, not a weakened successful run. Real PR creation-to-merge, nested coordinators, and ten-lane concurrency remain untested.


## Completed-child and multi-provider history candidate

The user requested completed-child logs in reflect and selected T3-managed Codex/Claude history only for automate-me. Reflect now scopes the current conversation and relevant completed delegated descendants, rather than the parent alone. The automate-me candidate preserves the original mining/interview/authoring flow while mapping history, paths, questions, and delivery to T3. Standalone CLI transcript stores and other projects are excluded by the selected scope.

A project-scoped thread-list probe returned both providers and subagent parent relationships. The installed T3 0.1.7 implementation confirms omitted settled/snoozed filters do not filter those histories. Two known-completed child threads were exported through activity position and text-offset pagination: 12 non-reasoning items in 2 pages for Codex (6 command events), and 23 in 4 pages for Claude (11 command events). Each included an agent-authored user_message kickoff, demonstrating why role text alone cannot establish human preference. No running delegate was read and no standalone provider log was scanned.

A synthetic collection fixture covers delegated descendants, unfinished work, another project, another conversation, human forks, reflection self-inclusion, inherited/copied evidence, old activity with recent metadata, and unavailable native-child bodies. It is not actual personal-preference mining. An independent Opus review is requested for the new instructions and these cases. All 50 repository tests and pinned source checks passed; generation currently includes 556 files. No full three-lens reflect run, actual persona/interview, skill installation, commit, PR, or external filing was executed for this change.


## History review follow-up

Opus found coverage and attribution gaps in the first history candidate, not a need for a new workflow dependency or Design change. The parent corrected collection of fork-local human messages and terminal failures/interruption/cancellation/rollback; success-only filtering was unintended. Returned records and read responses now require the authorized project identity. Agent-authored kickoffs, inherited items, copied results, and repeated source events retain canonical identity instead of becoming extra independent observations across time slices.

Automate-me again leaves raw slice reading to its miners. The parent partitions metadata/pointers; miners page their assigned activity or consume supported per-slice exports. No hardcoded personal storage destination or parent-context bulk transcript summarizer was introduced. There is no source-defined miner role: the caller model/effort is the starting point for the preserved job adjustments, with explicit aliases/fixed settings retaining precedence. No recall/swarm model or new configuration line was borrowed. The duplicated authoring word was corrected.

The review's hypothesized cross-parent delivery consumption was checked against installed T3 0.1.7 source. readThread obtains the caller and gates acknowledgement through directAppOwnedChildTasks, which rejects a target not directly delegated by that caller. The exact helper was extracted without changing its body and executed for four cases: own direct child selected; another parent's child, grandchild, and human fork not selected. This supports the ownership boundary, not a live notification delivery test. Own-child final-result reads may acknowledge delivery and are not described as globally pure.

The synthetic fixture now includes failed-child and interrupted-conversation evidence. These and the final wording were parent-inspected; no second delegated review or full workflow was run. Existing 50 repository tests and the source/index check pass. Current distribution is 56 of 58 pstack skills (19 adapted, 37 unchanged), one held (poteto-help), one omitted (make-bot-ui), plus three unchanged team-kit support skills. Generation contains 556 files. The actual completed-child API probes, protocol/helper checks, full reflection/mining/authoring limits, and selected T3-only scope remain distinct claims.


## Coordinator continuation probe and remaining execution constraint

A bounded real interval task ran twice in the same conversation. Tick records were 64.690377 seconds apart, and both turns answered prior-conversation questions without reading project/history files for the answers. The scheduled task was deleted after the second tick. This verifies periodic coordinator continuation/context in the observed case, not worker stall detection or replacement.

The following explanation was corrected: the active session's prohibition on polling/monitoring a running delegate is an execution instruction, not proof that the T3 product lacks monitoring capabilities. The user explicitly requested a supervision test, but this session cannot create an exception to that instruction. No running-worker polling or monitoring timer was started.

Installed server source inspection confirmed delegate_task timeoutMs bounds its blocking wait; a timeout leaves the child running and does not establish stalled execution. The inspected APIs/source did not establish a usable Codex/Claude semantic-stall notification contract. Provider-specific transport timeouts and idle-session cleanup are not evidence of the upstream progress-based stall detector. A full active-worker detection/replacement experiment remains unperformed; do not relabel the timer/context probe as that test or claim product-level impossibility.


## Autopilot detection boundary after independent source research

The independent Opus investigation read pinned pstack and public T3 b90e554 source and evaluated twelve repository-local alternatives. No faithful, host-permitted silent-hang/approval-wait detector for running Codex/Claude delegates and descendants was established. T3 has an ACP inactivity watchdog, but it is not wired to Codex/Claude and pauses during tools, requests and subagents; it does not close this gap. Terminal notifications, question notifications and cascading cancellation are source-supported mechanisms, not an end-to-end recovery test. A total-runtime deadline and a top-level-only architecture are not adopted as substitutes.

A separate user-authorized synthetic top-level experiment observed 123.153 seconds without progress while its process remained alive. A cooperative stop sentinel plus top-level interruption was followed by exact-PID exit, then a fresh top-level owner resumed checkpoint 3 and wrote unit 4. The one-shot schedule was deleted. This does not establish noncooperative process-tree cleanup, semantic-stall detection, or delegated-descendant supervision.

The distribution retains poteto-mode adoption while narrowing G1 to the missing detection above. Unattended Autopilot-full/stack remains explicitly blocked; no weaker policy or extra runtime was introduced. The generated instructions distinguish source-supported recovery mechanisms from the unresolved detection and require preserving the assigned target on replacement.


## Live delegate cancellation and checkpoint handoff

This supersedes the earlier source-only status for completion delivery, cascading cancellation and checkpoint handoff. A Claude Opus 5.5 delegate created a Codex gpt-6.1-sol descendant whose foreground Python command wrote its PID and slept for 300 seconds. At the pre-authorized experiment stop, the coordinator called task_cancel on the original owner before reading live status or artifacts, then deleted the one-shot schedule. The first post-cancel check showed no pending child runs; the descendant was interrupted, its command carried the experiment cancellation reason, exact PID 46349 had exited, and its natural-finish marker was absent. The completed owner result was preserved.

A fresh delegate on the same Claude provider and Opus model resumed checkpoint unit 1 and wrote unit 2 at 2026-11-06T23:04:24Z. Its completion notification resumed this conversation. The parent read and asserted the actual output, rather than accepting the final summary alone. Evidence is in .agents/cache/delegate-cancel-handoff-probe/{result.json,owner-after-cancel.json,descendant-after-cancel.json,replacement-result.json,replacement-dispatch.json}. The durable procedure is evals/delegate-cancel-handoff.md.

No live-delegate polling, cooperative sentinel, detached-process cleanup claim, git operation or user-configuration change was used. This was an unconditional experiment cancellation, not health monitoring or automatic stall detection. Failure/question/approval notification variants and full application recovery were not exercised by this fixture. Only the missing automatic detection remains the Autopilot integration blocker.


## Poteto-help adoption

Poteto-help retains upstream's help/work distinction, five need categories, single-example reply and both prompt references. Declared paragraph replacements adapt file invocation, Markdown model preferences, local adapted links, T3 isolation/continuation and already-recorded omission/design decisions. No new registration, installer, persistent mode, runtime or Design policy was added. The shared models reference is bundled unchanged.

A native independent evaluator read routed source files and produced three synthetic help answers covering setup/model reload, no-comments/make-bot-ui and overnight Autopilot feasibility. It started no workflows and read no personal preferences. Opus independently checked source fidelity, all help links, licenses/provenance, helper equality and counts, and found no blocker or new Design change. Two minor wording findings were corrected by the parent: explicit Multi-phase plan routing for Autopilot-target plans without execution, and removal of the Cursor Auto-selector wording. These final wording edits were not independently rerun.

Current selection is 57 of 58 pstack skills (20 adapted, 37 unchanged), none held, one omitted (make-bot-ui), plus three unchanged cursor-team-kit companions. Generation contains 560 files. Automatic delegate stall/approval-wait detection remains the explicit Autopilot execution gap; adoption completeness does not establish installation, automatic triggering or full workflow compatibility.


## Conventional layout and isolated installation

The generated container moved from dist/skills/ to root skills/. All 555 prior per-skill files and executable bits were compared and preserved before the verified old dist tree was removed. The generator adds 60 per-skill LICENSE.txt sidecars and moves exhaustive provenance/ownership to skills/SOURCES.json, for 616 generated files. Package-level duplicate LICENSE/NOTICE/licenses outputs are removed; canonical source notices remain in root licenses/. No skill procedure, frontmatter, role default or execution behavior changed.

The materializer no longer removes its entire output directory. Before writing, it refuses symlinks, unmanaged files, unsafe manifest paths and nonempty directories without an ownership manifest. Only obsolete owned files are removed; original-source and output hashes, local helper/license ownership and executable bits are checked. Tests cover these boundaries plus skill names and license carriage.

[Installation evaluation](../evals/installation.md) records actual skills CLI 1.7.6 local discovery/installation and agent-skills-nix f48aa227 full/partial bundle builds plus copy-tree/symlink-tree installation into disposable destinations. Each full installation preserved 60 skills and 615 per-skill files, including six executables and 60 license sidecars. Sibling references resolved. Partial Nix selection demonstrated the lexical/source-symlink distinction; it is not advertised as automatic companion resolution. Real user configuration and installed skill directories were untouched.

GitHub-source installation, Home Manager activation, individual harness registration and live workflow execution remain separate validation work. No artifacts were committed or pushed. Earlier dist paths and file counts in this chronological record refer to the prior layout.


## Layout review corrections

Opus independently reran 56 tests, source checks and 616-file generation, confirmed retained source/hash/mode records and all license sidecars, and found no major data-loss defect or workflow Design change. The parent corrected interrupted-write recovery with injected first/subsequent-write tests, limited empty-directory cleanup to stale owned-file parents, expanded discovery checks beyond selected directories, and identified the local LICENSE in combined-license provenance. Exact planned bytes can be adopted safely after interruption; differing unmanaged content still stops writes. Runtime byproducts are explicitly documented as unmanaged.

The review also found pre-existing local T3 instructions in swarm/arena/reflect that required a distribution-root README not carried by per-skill installers. Those three translations now carry sibling/reference/absolute-pointer rules inline. This is separate from the earlier byte-preserving layout move; no upstream reasoning procedure or workflow dependency was changed, and no new Patch/Design category was added. README distinguishes its checkout guidance and documentation-based GitHub/Home Manager examples from the actually executed local CLI/library tests. The parent handles these small findings without another delegate review.


Final review-follow-up validation passed 59 repository tests, the 573-file source check and the 616-file generation check. After regenerating the three corrected coordinator instructions and license provenance, the local skills CLI installation and both Nix copy-tree/symlink-tree destinations were refreshed. All three again contained 60 skills and 615 byte/mode-identical per-skill files, with 60 license sidecars, six executable files, readable sibling links and no root-README dependency in swarm/arena/reflect. The recorded artifact fingerprint and comparisons are in .agents/cache/layout-review/final-install-result.json. GitHub-source installation and Home Manager activation remain untested.


## Pre-push clean-checkout audit

The release candidate includes all 616 generated files. A repository ignore exception retains 134 pinned statechart .out fixtures that the author's global Git ignore would otherwise hide. A staged-only export exposed an executable-permission assumption: Git checkout under a private umask produces mode 0700 for executable files, while the former checker expected every 0111 bit. The checker now compares Git's owner executable flag and still detects executable/nonexecutable drift; a private-umask regression test covers this case. Contents and Git source modes are unchanged.

The staged whitespace check has one inherited empty final line in automate-me/SKILL.md, also present in pinned upstream; it is retained to avoid an unrelated source change. All other staged files pass whitespace checking. No disposable .agents artifacts or credential-pattern matches are in the publication set.


The final staged-only export passed 60 tests, the 573-file pinned-source check and the 616-file generation check under the actual private checkout umask. The publication candidate contains 705 files, including all pinned generated fixtures and no disposable .agents artifacts. GitHub-source installation and remote CI are checked only after push; passing these local release checks does not close the recorded Autopilot/A-to-B/periodic-detection or full-workflow gaps.
