import copy
from pathlib import Path
import tempfile
import unittest

from tools.upstream import changes, check_docs


class UpstreamTests(unittest.TestCase):
    def setUp(self):
        cache = Path('.agents/cache')
        cache.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=cache)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.lock = {
            'remote': 'https://github.com/cursor/plugins.git',
            'commit': 'a' * 40,
            'path': 'pstack',
            'files': {
                'skills/how/SKILL.md': {'mode': '100644', 'sha256': 'a'},
                'skills/how/references/example.md': {'mode': '100644', 'sha256': 'b'},
                'LICENSE': {'mode': '100644', 'sha256': 'c'},
            },
        }
        upstream = self.root / 'upstream'
        upstream.mkdir()
        (upstream / 'README.md').write_text(
            f"[Pinned source](https://github.com/cursor/plugins/tree/{self.lock['commit']}/pstack)\n"
        )
        self.index = upstream / 'skills/investigation/README.md'
        self.index.parent.mkdir(parents=True)
        self.index.write_text(f"# Investigation\n\n[how]({self.source_url('how')})\n\nStill evaluating the workflow.\n")

    def source_url(self, skill):
        return f"https://github.com/cursor/plugins/blob/{self.lock['commit']}/pstack/skills/{skill}/SKILL.md"

    def check(self, generated=None):
        return check_docs(self.root, self.lock, generated)

    def test_indexes_cover_sources_without_interpreting_decision_prose(self):
        self.assertEqual(self.check(), [])
        self.index.write_text(f"Free-form review notes. [Source]({self.source_url('how')}). The merge decision still needs discussion.\n")
        self.assertEqual(self.check(), [])

    def test_added_skill_requires_an_index_entry(self):
        self.lock['files']['skills/why/SKILL.md'] = {'mode': '100644', 'sha256': 'd'}
        self.assertIn('Missing skill index entry: skills/why/SKILL.md', self.check())

    def test_removed_skill_rejects_stale_source_link(self):
        del self.lock['files']['skills/how/SKILL.md']
        errors = self.check()
        self.assertTrue(any('not in the locked skill inventory' in error for error in errors))

    def test_duplicate_category_ownership_fails(self):
        other = self.root / 'upstream/skills/review/README.md'
        other.parent.mkdir()
        other.write_text(self.index.read_text())
        self.assertIn('Duplicate skill index entry: skills/how/SKILL.md', self.check())

    def test_old_revision_links_fail(self):
        self.index.write_text(self.index.read_text().replace('a' * 40, 'b' * 40))
        self.assertTrue(any('not in the locked skill inventory' in error for error in self.check()))

    def test_central_source_revision_must_match_lock(self):
        (self.root / 'upstream/README.md').write_text('Old source guide\n')
        self.assertIn('Central source guide must link the locked upstream revision', self.check())

    def test_linked_integration_plan_must_exist(self):
        self.index.write_text(self.index.read_text() + '\n[Integration plan](how-integrate-how.md)\n')
        self.assertTrue(any('Broken local link' in error for error in self.check()))
        plan = self.index.parent / 'how-integrate-how.md'
        plan.write_text('Keep the investigation separate from implementation. Ask the user before changing the boundary.\n')
        self.assertEqual(self.check(), [])

    def test_reference_changes_are_reported_without_claiming_a_review_occurred(self):
        before = copy.deepcopy(self.lock['files'])
        self.lock['files']['skills/how/references/example.md']['sha256'] = 'changed'
        self.assertEqual(changes(before, self.lock['files'])['changed'], ['skills/how/references/example.md'])
        self.assertEqual(self.check(), [])

    def test_generated_links_are_checked_against_planned_output(self):
        self.index.write_text(self.index.read_text() + '\n[Output](../../../skills/how/SKILL.md)\n')
        self.assertTrue(any('Broken local link' in error for error in self.check()))
        self.assertEqual(self.check({'how/SKILL.md': b'New output'}), [])
        stale = self.root / 'skills/how/SKILL.md'
        stale.parent.mkdir(parents=True)
        stale.write_text('Old output')
        self.assertTrue(any('Broken local link' in error for error in self.check({})))

    def test_diff_includes_mode_changes_and_deletions(self):
        before = self.lock['files']
        after = copy.deepcopy(before)
        after['skills/how/SKILL.md']['mode'] = '100755'
        del after['LICENSE']
        after['new'] = {'mode': '100644', 'sha256': 'e'}
        self.assertEqual(changes(before, after), {
            'added': ['new'], 'removed': ['LICENSE'], 'changed': ['skills/how/SKILL.md'],
        })


if __name__ == '__main__':
    unittest.main()
