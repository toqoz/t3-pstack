# Integration decisions

Preserve pstack's procedures, model-selection intent, and existing workflow dependencies. Replace host mechanisms without introducing another skill merely to share dispatch code or configuration.

- **T3:** Implement routine host adaptations within the authorized task and report the result.
- **Patch:** Implement and report temporary corrections that preserve upstream intent; no separate design approval is needed. Record the reason, upstream removal condition, and removal checks in how-integrate. Keep the patch independently removable.
- **Design:** Discuss the concrete intent, before/after behavior, and tradeoffs with the user before implementing a deliberate policy or behavior change. Do not treat implementation convenience as approval. Previously approved Design scope does not require repeated confirmation.

If a proposed change mixes these categories, separate the Design decision and continue independent T3/Patch work while awaiting the user.

# Review documents

Category README files use skill / T3 / Patch / Design tables with ✅, -, and Pending. Explain changed skills under their own headings with only applicable labeled bullets. Link detail documents by filename alone. Keep detailed evidence in how-integrate and verification records.

Adoption reasons and design approvals are human-reviewed Markdown, not a parsed status database. Edit pinned-source transformations and canonical files; regenerate skills/ rather than editing it directly. Preserve source hashes and licenses.
