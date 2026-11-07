# Audit-trail evaluation

Run `python3 -m unittest discover -s tests -p test_decision_log.py` against the actual generated executable. These checks cover UTC timestamps, six columns, formula-prefix escaping, tab/newline/CR flattening, append-only history, nested log creation, and argument errors. The helper and header template are copied unchanged from the pin with their source hashes/modes.

For a separate instruction evaluation, give a fresh evaluator the generated show-me-your-work entrypoint, its references, a raw synthetic transcript, and a decision log. Include a false verification claim, an omitted pivot, and rows belonging to another run. Ask it to audit the current run without editing previous rows, and assess cross-family reviewer selection with the supplied actual model families. Do not supply intended answers.

The evaluator must not invoke providers, private history, connected services, or real publication. It may write only its evaluation artifact in workspace cache. This evaluates decisions and reporting; it does not constitute the required live cross-family review of an actual task trail.

The full workflow still requires supported T3 activity for actual run evidence, stable run identity across turns/summaries, a real reviewer on another family, and its Attention flags. Missing evidence or reviewer access remains an incomplete audit, not successful self-review.
