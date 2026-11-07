# No-comments integration policy

The user approved a partial integration of pstack's no-comments workflow with John Ousterhout's *A Philosophy of Software Design*. The goal is lower reader complexity, not fewer comments. This policy is implemented and the workflow is adopted. Pinned-source generation and a narrow independent behavioral evaluation have passed; the live integration limits are recorded below.

## Design basis and sources

Ousterhout distinguishes information expressed by code from the additional information documentation supplies. His publicly released second-edition extract discusses why replacing comments with extracted methods and elaborate names can make understanding harder. This supports evaluating the combined design rather than treating comment removal as proof of improvement. See [the author's second-edition extract, discussion of comments](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf) and [the author's edition notes](https://web.stanford.edu/~ouster/cgi-bin/book.php).

His [Writing Comments lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=comments) distinguish redundant narration from useful interface semantics, design rationale, and higher-level explanations. They also discuss using documentation to evaluate a design and keeping it close to the relevant code. These are paraphrased ideas, not reproduced book text.

The operational rules below are this project's synthesis of those ideas, the upstream workflow, and the user's explicit preferences. In particular, approval requirements and retaining constraints until a replacement is verified are local decisions, not claims about rules prescribed by the book.

## What to retain from pstack

Keep an independent review, evidence for each finding, a strict scope, parent inspection of proposed changes, at most one rejected-report retry, and verification of accepted root-cause fixes. Use architect for a fix that needs a different shape. A comment must not become an excuse to leave a feasible, in-scope design defect unresolved.

Delete comments made redundant by an implemented and verified structural improvement. Also remove dead commented-out code, misleading statements after checking the actual behavior, and narration that adds no information. Preserve legal/license notices and tooling directives unless their specific removal is authorized and justified.

## What changes deliberately

Keep the upstream name Comment Sicko, understood here as obsessive attention to code and comment quality. Replace the upstream comment-hating persona and deletion-first verdict with an independent review of code and documentation together. Internal ownership is not a reason to reject a comment: useful rationale can describe our own design. Uncertainty is a reason to investigate or report a gap, not a default instruction to delete.

Actively add or improve comments that communicate missing design intent, important rejected alternatives, domain constraints, non-obvious contracts, or a useful high-level explanation. A reader should not need to reconstruct all of that from implementation details. State the relevant fact at its natural location; link to a longer decision record rather than duplicating it. Keep comments accurate as code changes.

Do not introduce extra layers, shallow helper methods, sprawling names, state, or public surface solely to eliminate a comment. For a proposed structural change, explain what becomes easier to understand or harder to misuse, and what additional concepts or navigation it introduces. If the code-plus-comment form is clearer overall, retain it. No comment-count target or deletion quota is used.

A comment can expose a design weakness without proving that every explanation should become code. When a simpler structure can genuinely remove that weakness, implement and verify it within scope, then reassess the comment. If the fix is outside scope, record it and preserve the necessary explanation rather than widening the task or claiming the comment fixes the defect.

## Constraint preservation

Retain a constraint comment until its replacement guarantee has been implemented and verified. If an encoding is declined, deferred, unapproved, or outside scope, preserve the comment and report the unresolved guarantee. Once an approved encoding makes the warning redundant, remove it. Rationale that remains useful after enforcement stays documented.

Do not remove a correctness-related suppression first and leave broken code behind. Verify a root-cause fix before removing the obsolete suppression; preserve necessary directives while reporting unresolved work. This follows the same principle as preserving an unenforced constraint.

## Review procedure

1. Identify the scope, current behavior, comment purpose, and intended invariant.
2. Have an independent reviewer propose removals, useful additions/clarifications, and structural fixes, each with evidence and a reader-facing reason. It does not edit application code.
3. The parent rejects scope escapes, lost rationale/contracts, legal-header removal, and refactors that increase overall complexity merely to reduce comments. Investigate uncertainty before accepting a deletion. Restore rejected removals. Re-run one rejected report with the failure named; a second rejection leaves the workflow incomplete.
4. Implement accepted in-scope structural fixes and verify the real behavior. Reassess affected comments afterward. Keep the existing approval boundary for proposed constraint encodings.
5. Report meaningful code/documentation improvements, verification, and unresolved constraints. Counts may describe the diff but are not success criteria.

## Host and provenance work before adoption

Retain the pinned upstream skill and agent as review inputs, with source hashes and their MIT notice. Their behavior must be deliberately adapted to this policy; do not package the original Comment Sicko instructions unchanged and hope a wrapper overrides conflicting deletion rules. Book ideas are cited and paraphrased; no book chapter or third-party text is bundled under the project's MIT license.

The parent selects models through shared preferences and T3 dispatch. A child performs its assigned review without dispatching more agents. When how/why evidence is needed, it returns the exact question to the parent, which runs the adopted workflow and supplies the findings. Pass distribution-local absolute paths and owned output locations, provide stable accessible scoped inputs, and obey host completion rules. The parent dispatches the reviewer directly; no arena workflow or model policy is imported to share host mechanics.

The generator imports the pinned external agent with an explicit destination/source map and applies the same hash, mode, exact-transform, collision, and provenance checks as ordinary skill files. Both coordinator acceptance rules and reviewer instructions are adapted together. No new runtime agent registry is introduced.

## Update and evaluation

An A-to-B review must inspect changes in both the skill and agent definition, comparing their intent with this policy. Retain useful upstream improvements without mechanically restoring deletion-first rules or importing the book as executable instructions.

Evaluation cases include: a redundant comment after a verified simplification; useful internal design rationale; a missing contract worth documenting; a proposed helper extraction that increases reader complexity; an unenforced constraint whose encoding is declined; legal-header preservation; an unresolved correctness suppression; a prohibited application-code edit; and the bounded rejection retry. Generation and license checks alone do not prove these judgments. An independent reviewer exercised a real code fixture and produced a comment-only patch, which the parent applied to a disposable copy and checked with executable AST comparison and three passing behavior tests. It removed arithmetic narration, added useful interface explanations, and preserved legal, rationale, compatibility, and API documentation. An independent coordinator assessment covered code-edit rejection, the retry limit, declined encoding, missing contracts, obsolete comments after verified fixes, and complexity-increasing extraction. The final approval wording and sketch-only scope clarification were inspected by the parent, not independently rerun. Live model dispatch, T3 input delivery, evidence exchange, and architect execution remain untested. See the [repeatable evaluation](../../../evals/no-comments.md).
