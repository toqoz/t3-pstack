# Measurement checklist integration policy

Preserve all seven validity questions: effective load/capacity, limiter and source evidence, production tuning, relevant limits, actual work/errors, repeatable measurement, and end-to-end relevance. Keep the distinction between ballpark estimates and decision-grade evidence. Unsupported observations are gaps, not invented proof.

Collect per-process CPU, a runtime profile, I/O wait, and syscall counts with available host tools. Each unavailable category is an explicit evidence gap; tool portability does not permit quietly reducing the categories to only the suspected limiter. Linux nproc and macOS sysctl are examples, not guarantees of effective quota or affinity. Do not stop unrelated work merely to improve a measurement. Keep concise primary-number reporting without requiring the currently unbundled PR playbook; performance playbooks remain contextual integration points, not missing prerequisites.

The unchanged explain-the-number principle is adopted with its required checklist companion. The [repeatable measurement exercise](../../../evals/measurement-checklist.md) records actual work, alternating identical controls, raw trials, warmup/profile exclusions, and honest limitations. Its conclusion is inconclusive, not a product speedup. See the [verification record](../../../docs/verification.md).

For A-to-B updates, preserve compatible measurement improvements and reassess tool substitutions. Changes to validity criteria, relevance, or uncertainty require explicit semantic review; a portable command replacement must not weaken the evidence standard.
