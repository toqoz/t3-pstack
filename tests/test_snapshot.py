from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools.upstream import REMOTE, git, snapshot


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        cache = Path(".agents/cache")
        cache.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=cache)
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name).resolve()
        subprocess.check_call(["git", "init", "--quiet", str(self.repo)])
        git(self.repo, "remote", "add", "origin", REMOTE)
        self.add_blob("100644", "pstack/LICENSE", b"MIT fixture\n")
        self.add_blob("100644", "pstack/skills/example/SKILL.md", b"Fixture\n")
        self.add_blob("100755", "pstack/skills/example/run.sh", b"exit 0\n")
        self.commit = self.commit_tree()

    def add_blob(self, mode, path, content):
        oid = subprocess.check_output(["git", "-C", str(self.repo), "hash-object", "-w", "--stdin"], input=content).decode().strip()
        git(self.repo, "update-index", "--add", "--cacheinfo", mode, oid, path)

    def commit_tree(self):
        tree = git(self.repo, "write-tree").decode().strip()
        return subprocess.check_output([
            "git", "-C", str(self.repo), "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
            "commit-tree", tree,
        ], input=b"Fixture snapshot\n").decode().strip()

    def test_snapshot_records_git_modes_and_ignores_working_tree(self):
        before = snapshot(self.repo, self.commit)
        path = self.repo / "pstack/skills/example/SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("Uncommitted worktree change")
        self.assertEqual(snapshot(self.repo, self.commit), before)
        self.assertEqual(before["files"]["skills/example/run.sh"]["mode"], "100755")

    def test_other_origin_and_moving_reference_fail(self):
        with self.assertRaisesRegex(ValueError, "full commit SHA"):
            snapshot(self.repo, "main")
        git(self.repo, "remote", "set-url", "origin", "https://example.invalid/other")
        with self.assertRaisesRegex(ValueError, "Expected origin"):
            snapshot(self.repo, self.commit)

    def test_symlink_and_submodule_are_rejected(self):
        self.add_blob("120000", "pstack/link", b"outside")
        with self.assertRaisesRegex(ValueError, "Unsupported upstream entry"):
            snapshot(self.repo, self.commit_tree())
        git(self.repo, "update-index", "--force-remove", "pstack/link")
        git(self.repo, "update-index", "--add", "--cacheinfo", "160000", self.commit, "pstack/submodule")
        with self.assertRaisesRegex(ValueError, "Unsupported upstream entry"):
            snapshot(self.repo, self.commit_tree())

    def test_snapshot_cli_returns_json_and_clean_errors(self):
        import json

        script = Path("tools/upstream.py").resolve()
        result = subprocess.run([sys.executable, str(script), "snapshot", str(self.repo), self.commit], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), snapshot(self.repo, self.commit))
        result = subprocess.run([sys.executable, str(script), "snapshot", str(self.repo), "main"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("full commit SHA", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


    def test_sibling_package_has_separate_inventory_and_identity(self):
        self.add_blob("100644", "cursor-team-kit/LICENSE", b"Cursor MIT\n")
        self.add_blob("100644", "cursor-team-kit/skills/control-ui/SKILL.md", b"Control UI\n")
        revision = self.commit_tree()
        dependency = snapshot(self.repo, revision, "cursor-team-kit")
        self.assertEqual(dependency["path"], "cursor-team-kit")
        self.assertNotIn("skills/example/run.sh", dependency["files"])
        self.assertIn("skills/control-ui/SKILL.md", dependency["files"])
        self.assertNotEqual(dependency["files"]["LICENSE"], snapshot(self.repo, revision)["files"]["LICENSE"])
        with self.assertRaisesRegex(ValueError, "Unsupported source package"):
            snapshot(self.repo, revision, "../outside")
