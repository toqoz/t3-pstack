"""Exercise the measurement checklist on identical synthetic control workloads."""

import cProfile
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import pstats
import statistics
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '.agents/cache/measurement-checklist'
ROWS = 50000
TRIALS = 5


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(timezone.utc).isoformat()
    try:
        load_before = os.getloadavg()
    except (AttributeError, OSError):
        load_before = None
    payload = json.dumps([{'value': n} for n in range(ROWS)])
    expected_sum = ROWS * (ROWS - 1) // 2
    calls = 0

    def workload():
        nonlocal calls
        rows = json.loads(payload)
        result = sum(row['value'] for row in rows)
        calls += 1
        if len(rows) != ROWS or result != expected_sum:
            raise ValueError('Work/output verification failed')
        return result

    workload()
    workload()
    samples = []
    for trial in range(TRIALS):
        for side in ('A', 'B'):
            cpu_start = time.process_time()
            wall_start = time.perf_counter()
            result = workload()
            samples.append({
                'trial': trial + 1, 'side': side,
                'wall_seconds': time.perf_counter() - wall_start,
                'cpu_seconds': time.process_time() - cpu_start,
                'rows': ROWS, 'sum': result,
            })
    profile = cProfile.Profile()
    profile.runcall(workload)
    hot = sorted(pstats.Stats(profile).stats.items(), key=lambda entry: entry[1][2], reverse=True)[:5]
    try:
        load = os.getloadavg()
    except (AttributeError, OSError):
        load = None
    evidence = {
        'started_at': started_at,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'purpose': 'Workflow exercise only; identical controls cannot establish a product speedup.',
        'decision_before_run': 'Verify actual work, output correctness, alternating trials, and source-linked profile evidence. Reject any speedup or adoption claim.',
        'noise_policy': 'Report spread and no winner. This fixture has no meaningful treatment effect or product decision threshold.',
        'environment': {'platform': platform.platform(), 'python': sys.version, 'hardware_cpu_count': os.cpu_count(), 'load_average_before': load_before, 'load_average_after': load},
        'capacity_gap': 'Hardware CPU count is not a measured affinity/quota. The workload is single-threaded; process capacity and competing processes were not exhaustively audited.',
        'payload_sha256': hashlib.sha256(payload.encode()).hexdigest(),
        'samples': samples, 'failures': 0, 'calls_including_excluded': calls,
        'excluded': 'Two warmups and one profiled run. No profiler time is included in the reported samples.',
        'profile_hotspots': [{'file': key[0], 'line': key[1], 'function': key[2], 'self_seconds': value[2]} for key, value in hot],
        'verdict': 'inconclusive',
        'relevance_gap': 'No production configuration, user-facing end-to-end path, I/O bandwidth, or other product bottleneck is measured.',
    }
    assert len(samples) == TRIALS * 2 and calls == TRIALS * 2 + 3
    assert all(sample['rows'] == ROWS and sample['sum'] == expected_sum for sample in samples)
    (OUTPUT / 'results.json').write_text(json.dumps(evidence, indent=2) + '\n')
    lines = ['# Measurement workflow exercise', '', 'Verdict: inconclusive. This is a checklist exercise with identical control workloads, not a product benchmark or speedup claim.', '', 'The payload is constructed outside the timed region. Parsing, summation, and output verification run inside every sample. Both labels use the same implementation and settings, with two excluded warmups and a separate excluded profile.', '', '| Control | Trials | Median wall seconds | Wall range seconds |', '|---|---|---|---|']
    for side in ('A', 'B'):
        times = [sample['wall_seconds'] for sample in samples if sample['side'] == side]
        lines.append(f'| {side} | {len(times)} | {statistics.median(times):.6f} | {min(times):.6f} to {max(times):.6f} |')
    lines += ['', 'No winner is selected. Spread is recorded rather than interpreted as an optimization. Work/output checks passed for every sample; any exception would fail the exercise before a success report.', '', '## Observed profile', '', 'These source/function locations consumed the most self time in the excluded profile. They are evidence for this one synthetic run, not proof of a production bottleneck.', '']
    lines += [f"- `{item['file']}:{item['line']}` ({item['function']})." for item in evidence['profile_hotspots']]
    lines += ['', '## Limits', '', evidence['capacity_gap'], '', evidence['relevance_gap'], '', 'The seven checklist questions were considered: observed profile, equal control settings, no impossible throughput claim, verified errors/work, alternating trials and spread, explicit end-to-end gap, and execution inside the timed region. Raw samples, environment, excluded work, and profile data are in results.json.', '']
    (OUTPUT / 'report.md').write_text('\n'.join(lines))
    print('Measurement exercise passed work/output/trial checks; verdict remains inconclusive. See .agents/cache/measurement-checklist/report.md')


if __name__ == '__main__':
    main()
