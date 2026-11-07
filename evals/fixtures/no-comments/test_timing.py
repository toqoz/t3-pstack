import unittest
from timing import cache_key, remaining, retry_delays, slice_window


class TimingTests(unittest.TestCase):
    def test_timeout_clamp(self):
        self.assertEqual(remaining(5.0, 6.0), 0.0)
        self.assertEqual(remaining(8.0, 6.0), 2.0)

    def test_retry_schedule(self):
        self.assertEqual(list(retry_delays(1, 4, 5)), [1, 2, 4, 4, 4])

    def test_protocol_and_slice(self):
        self.assertEqual(cache_key(7), 'v1:7')
        values = [1, 2, 3]
        self.assertEqual(slice_window(values, 1, 3), [2, 3])
        self.assertIsNot(slice_window(values, 0, 3), values)
