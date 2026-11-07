# Exercise the measurement checklist

Read the generated benchmark-checklist and principle-explain-the-number files before running this fixture. The goal is to exercise evidence collection and an honest inconclusive verdict, not to optimize this repository or choose a product implementation.

Run from the repository root:

```sh
python3 evals/measurement_check.py
```

The fixture uses identical single-threaded JSON parsing/summation controls. It constructs data outside timing, verifies row count and sum inside every sample, warms both controls, alternates five trials per side, and profiles a separate excluded run. It writes raw observations and a readable report under `.agents/cache/measurement-checklist/`.

Inspect both actual files. Check trial order, real work/output counts, exclusions, Python/platform data, source/function profile locations, and spread. Hardware CPU count is not evidence of effective quota/affinity. A profile of this synthetic function is not evidence of a production limiter. The report must not select a winner, infer a product speedup, or hide its missing end-to-end and capacity evidence.

The script is a reproducible workflow exercise. It is not a universal benchmark runner, does not install dependencies, and is not needed to use the shipped skills. Its artifacts are machine-specific and disposable. An actual adoption/performance decision still needs production-relevant measurements and all required checklist evidence.

The fixture does not collect all four observation categories now explicit in the checklist: a profile is present, but per-process sampling, I/O-wait, and syscall-count evidence remain gaps. Its process CPU timer is not a substitute for per-process utilization sampling. The fixture is partial procedure evidence, not a passed complete measurement audit.
