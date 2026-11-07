# Copyright (c) 2026 Fixture Authors. MIT licensed.
import time


def deadline_after(seconds):
    # Monotonic time keeps NTP adjustments from changing an already scheduled timeout.
    return time.monotonic() + seconds


def remaining(deadline, now):
    # Subtract now from deadline and clamp to zero.
    return max(0.0, deadline - now)


def retry_delays(initial, cap, count):
    delay = initial
    for _ in range(count):
        yield delay
        delay = min(cap, delay * 2)


def cache_key(account_id):
    # Do not change the v1: prefix: deployed consumers use it to locate existing entries.
    return 'v1:' + str(account_id)


def slice_window(values, start, end):
    """Return a new list for the zero-based half-open interval [start, end)."""
    return list(values[start:end])
