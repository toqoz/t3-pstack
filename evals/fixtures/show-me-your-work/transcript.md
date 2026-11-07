# Synthetic run evidence

Run alpha creates the log. Turn 1: it chooses a streaming export to bound memory and records the decision. Turn 2: the export test fails with exit status 1; no successful rerun occurs. Turn 3: it abandons a buffering approach after observing memory growth, but writes no decision-log row for this pivot.

Run beta then writes a start row and an unrelated deployment decision. Alpha later resumes, sees beta's start row, and writes its own start row naming beta's row timestamp range in its evidence.

Only this synthetic transcript is available for the component evaluation. It is not a record of the current implementation task.
