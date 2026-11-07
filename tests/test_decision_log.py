import csv
from datetime import datetime
from pathlib import Path
import subprocess
import tempfile
import unittest


class DecisionLogTests(unittest.TestCase):
    def test_helper_sanitizes_cells_and_appends_without_rewriting_history(self):
        helper = Path('skills/show-me-your-work/scripts/log.sh').resolve()
        cache = Path('.agents/cache')
        cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as temporary:
            log = Path(temporary) / 'nested/decisions.tsv'
            cells = ['-phase', '=choice\tnew\nline', '+why\rnext', '@proof', 'open 100%']
            subprocess.run([str(helper), str(log), *cells], check=True)
            before = log.read_bytes()
            rows = list(csv.reader(log.read_text().splitlines(), delimiter='\t'))
            self.assertEqual(rows[0], ['ts', 'phase', 'decision', 'why', 'evidence', 'result'])
            self.assertEqual(rows[1][1:], ["'-phase", "'=choice new line", "'+why next", "'@proof", 'open 100%'])
            datetime.strptime(rows[1][0], '%Y-%m-%dT%H:%M:%SZ')
            subprocess.run([str(helper), str(log), 'verify', 'checked output', 'prove it', 'test:1', 'tests green'], check=True)
            self.assertTrue(log.read_bytes().startswith(before))
            rows = list(csv.reader(log.read_text().splitlines(), delimiter='\t'))
            self.assertEqual(len(rows), 3)
            self.assertTrue(all(len(row) == 6 for row in rows))
            self.assertEqual(rows[-1][-1], 'tests green')

    def test_wrong_argument_count_does_not_create_a_log(self):
        helper = Path('skills/show-me-your-work/scripts/log.sh').resolve()
        cache = Path('.agents/cache')
        cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as temporary:
            log = Path(temporary) / 'decisions.tsv'
            result = subprocess.run([str(helper), str(log)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(b'usage:', result.stderr)
            self.assertFalse(log.exists())


if __name__ == '__main__':
    unittest.main()
