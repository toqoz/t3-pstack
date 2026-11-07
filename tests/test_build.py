import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.build import materialize, merge_dependency, render, safe_path, transform


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.source = {
            "LICENSE": b"Upstream permission and copyright\n",
            "skills/how/SKILL.md": b"Read references/example.md. Use Cursor dispatch.\n",
            "skills/how/references/example.md": b"Verify the explanation against code.\n",
        }
        self.lock = {"remote": "https://example.com/upstream", "commit": "a" * 40, "files": {
            name: {"mode": "100644", "sha256": hashlib.sha256(content).hexdigest()}
            for name, content in self.source.items()
        }}
        self.transforms = {"skills/how": {"target": "skills/how", "replacements": [{
            "file": "SKILL.md", "before": "Use Cursor dispatch.",
            "after": "Read references/t3.md.", "reason": "Use T3 execution",
        }]}}

    def build(self):
        return render(self.lock, self.transforms, self.source.__getitem__, b"T3 adapter\n", b"Model defaults\n", b"Project MIT\n")

    def test_build_preserves_reference_and_license_with_provenance(self):
        output = self.build()
        self.assertEqual(output["how/references/example.md"], self.source["skills/how/references/example.md"])
        self.assertEqual(output["how/LICENSE.txt"], self.source["LICENSE"] + b"\nLocal adaptations (MIT):\n\nProject MIT\n")
        self.assertIn(b"Read references/t3.md.", output["how/SKILL.md"])
        self.assertIn(b'"source": "skills/how/SKILL.md"', output["SOURCES.json"])
        self.assertEqual(self.build(), output)
        self.assertEqual(output["how/references/models.md"], b"Model defaults\n")

    def test_unmodified_skill_does_not_gain_execution_guidance(self):
        self.transforms["skills/how"]["replacements"] = []
        output = self.build()
        self.assertEqual(output["how/SKILL.md"], self.source["skills/how/SKILL.md"])
        self.assertNotIn("how/references/t3.md", output)
        self.assertNotIn("how/references/models.md", output)

    def test_model_preferences_do_not_add_investigation_boundaries(self):
        self.transforms["skills/how"]["replacements"][0]["after"] = "Read references/models.md."
        output = self.build()
        self.assertEqual(output["how/references/models.md"], b"Model defaults\n")
        self.assertNotIn("how/references/t3.md", output)

    def test_imported_reference_preserves_source_provenance_and_transforms(self):
        source = "agents/reviewer.md"
        content = b"Review the scoped code.\n"
        self.source[source] = content
        self.lock["files"][source] = {"mode": "100644", "sha256": hashlib.sha256(content).hexdigest()}
        spec = self.transforms["skills/how"]
        spec["imports"] = {"references/reviewer.md": source}
        spec["replacements"].append({"file": "references/reviewer.md", "before": "scoped code", "after": "code and comments", "reason": "Adapt role"})
        output = self.build()
        target = "how/references/reviewer.md"
        self.assertEqual(output[target], b"Review the code and comments.\n")
        self.assertEqual(json.loads(output["SOURCES.json"])["files"][target], {
            "source": source, "source_sha256": hashlib.sha256(content).hexdigest(), "source_mode": "100644",
            "output_sha256": hashlib.sha256(b"Review the code and comments.\n").hexdigest(),
        })

    def test_imports_reject_unpinned_sources_and_unsafe_paths(self):
        for imports in ([], {"references/role.md": "missing.md"}, {"../role.md": "LICENSE"}, {"references/role.md": "../LICENSE"}):
            with self.subTest(imports=imports):
                self.transforms["skills/how"]["imports"] = imports
                with self.assertRaises(ValueError):
                    self.build()

    def test_import_cannot_replace_an_existing_source_destination(self):
        self.transforms["skills/how"]["imports"] = {"SKILL.md": "LICENSE"}
        with self.assertRaisesRegex(ValueError, "Imported destination collision"):
            self.build()

    def test_imported_source_bytes_are_verified(self):
        source = "agents/reviewer.md"
        self.source[source] = b"Changed role\n"
        self.lock["files"][source] = {"mode": "100644", "sha256": hashlib.sha256(b"Original role\n").hexdigest()}
        self.transforms["skills/how"]["imports"] = {"references/reviewer.md": source}
        with self.assertRaisesRegex(ValueError, "Source hash mismatch"):
            self.build()

    def test_cross_skill_markdown_dependency_cannot_be_missing(self):
        path = "skills/how/SKILL.md"
        self.source[path] += b"\n[Companion](../missing/SKILL.md)\n"
        self.lock["files"][path]["sha256"] = hashlib.sha256(self.source[path]).hexdigest()
        with self.assertRaisesRegex(ValueError, "Broken generated Markdown link"):
            self.build()

    def test_reference_file_can_require_shared_execution_guidance(self):
        self.transforms["skills/how"]["replacements"] = []
        path = "skills/how/references/example.md"
        self.source[path] += b"Read references/t3.md from the skill directory.\n"
        self.lock["files"][path]["sha256"] = hashlib.sha256(self.source[path]).hexdigest()
        output = self.build()
        self.assertEqual(output["how/references/t3.md"], b"T3 adapter\n")
        self.assertEqual(output["how/references/models.md"], b"Model defaults\n")

    def test_drifted_or_ambiguous_replacement_fails(self):
        rule = self.transforms["skills/how"]["replacements"][0]
        for content in ("Different source", "Use Cursor dispatch. Use Cursor dispatch."):
            with self.assertRaisesRegex(ValueError, "exactly once"):
                transform(content, [rule])

    def test_replacements_match_original_text_without_cascading(self):
        rules = [
            {"before": "A", "after": "B", "reason": "First"},
            {"before": "B", "after": "C", "reason": "Second"},
        ]
        with self.assertRaisesRegex(ValueError, "exactly once"):
            transform("A", rules)
        self.assertEqual(transform("A B", rules), "B C")

    def test_overlapping_source_replacements_fail(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            transform("ABC", [
                {"before": "AB", "after": "X", "reason": "First"},
                {"before": "BC", "after": "Y", "reason": "Second"},
            ])

    def test_malformed_manifest_has_actionable_error(self):
        for key in ("reason", "file", "before", "after"):
            original = copy.deepcopy(self.transforms)
            del self.transforms["skills/how"]["replacements"][0][key]
            with self.assertRaisesRegex(ValueError, "Replacement requires string"):
                self.build()
            self.transforms = original
        del self.transforms["skills/how"]["target"]
        with self.assertRaisesRegex(ValueError, "Relative path must be a string"):
            self.build()

    def test_provenance_distinguishes_original_hash_and_notice(self):
        output = self.build()
        source = json.loads(output["SOURCES.json"])["files"]["how/SKILL.md"]
        self.assertEqual(source["source_sha256"], self.lock["files"]["skills/how/SKILL.md"]["sha256"])
        self.assertIn(self.source["LICENSE"], output["how/LICENSE.txt"])

    def test_source_tampering_fails(self):
        self.source["skills/how/SKILL.md"] += b"modified"
        with self.assertRaisesRegex(ValueError, "Source hash mismatch"):
            self.build()

    def test_license_tampering_fails(self):
        self.source["LICENSE"] = b"Changed permission"
        with self.assertRaisesRegex(ValueError, "Source hash mismatch: LICENSE"):
            self.build()

    def test_non_regular_source_mode_is_rejected(self):
        self.lock["files"]["skills/how/SKILL.md"]["mode"] = "120000"
        with self.assertRaisesRegex(ValueError, "Unsupported source mode"):
            self.build()

    def test_executable_source_runs_and_mode_drift_is_detected_and_repaired(self):
        source = "skills/how/scripts/check.sh"
        content = b"#!/bin/sh\nprintf ready\n"
        self.source[source] = content
        self.lock["files"][source] = {"mode": "100755", "sha256": hashlib.sha256(content).hexdigest()}
        output = self.build()
        cache = Path(".agents/cache")
        cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as temporary:
            directory = Path(temporary) / "skills"
            materialize(directory, output, check=False)
            script = directory / "how/scripts/check.sh"
            self.assertEqual(subprocess.check_output([str(script)]), b"ready")
            materialize(directory, output, check=True)
            script.chmod(0o644)
            with self.assertRaisesRegex(ValueError, "Generated files differ"):
                materialize(directory, output, check=True)
            materialize(directory, output, check=False)
            self.assertEqual(subprocess.check_output([str(script)]), b"ready")
            entrypoint = directory / "how/SKILL.md"
            entrypoint.chmod(0o755)
            with self.assertRaisesRegex(ValueError, "Generated files differ"):
                materialize(directory, output, check=True)
            materialize(directory, output, check=False)
            self.assertEqual(entrypoint.stat().st_mode & 0o111, 0)

    def test_removed_selected_source_cannot_be_generated(self):
        del self.lock["files"]["skills/how/SKILL.md"]
        del self.lock["files"]["skills/how/references/example.md"]
        with self.assertRaisesRegex(ValueError, "not an upstream skill"):
            self.build()

    def test_executable_check_accepts_a_private_checkout_umask(self):
        source = "skills/how/scripts/check.sh"
        self.source[source] = b"#!/bin/sh\nexit 0\n"
        self.lock["files"][source] = {"mode": "100755", "sha256": hashlib.sha256(self.source[source]).hexdigest()}
        with tempfile.TemporaryDirectory(dir=".agents/cache") as temporary:
            directory = Path(temporary) / "skills"
            output = self.build()
            materialize(directory, output, check=False)
            (directory / "how/scripts/check.sh").chmod(0o700)
            (directory / "how/SKILL.md").chmod(0o600)
            materialize(directory, output, check=True)

    def test_missing_replacement_file_fails(self):
        self.transforms["skills/how"]["replacements"][0]["file"] = "absent.md"
        with self.assertRaisesRegex(ValueError, "missing file"):
            self.build()

    def test_two_units_cannot_overwrite_each_other(self):
        for path, content in list(self.source.items()):
            if not path.startswith("skills/how/"):
                continue
            other = path.replace("skills/how/", "skills/other/")
            self.source[other] = content
            self.lock["files"][other] = copy.deepcopy(self.lock["files"][path])
        self.transforms["skills/other"] = copy.deepcopy(self.transforms["skills/how"])
        with self.assertRaisesRegex(ValueError, "collision"):
            self.build()

    def test_output_cannot_escape_distribution(self):
        for path in ("/tmp/escape", "skills/../escape", "skills//how", "skills\\how"):
            with self.assertRaises(ValueError):
                safe_path(path)

    def test_generated_tree_refuses_unmanaged_files_and_removes_only_owned_stale_files(self):
        with tempfile.TemporaryDirectory(dir=".agents/cache") as temporary:
            directory = Path(temporary) / "skills"
            output = self.build()
            materialize(directory, output, check=False)
            materialize(directory, output, check=True)
            (directory / "personal.md").write_text("keep")
            with self.assertRaisesRegex(ValueError, "Unmanaged"):
                materialize(directory, output, check=False)
            self.assertEqual((directory / "personal.md").read_text(), "keep")
            (directory / "personal.md").unlink()
            smaller = copy.deepcopy(output)
            del smaller["how/references/example.md"]
            manifest = json.loads(smaller["SOURCES.json"])
            del manifest["files"]["how/references/example.md"]
            smaller["SOURCES.json"] = json.dumps(manifest).encode()
            materialize(directory, smaller, check=False)
            self.assertFalse((directory / "how/references/example.md").exists())
            materialize(directory, smaller, check=True)
            (directory / "how/SKILL.md").write_text("manual edit")
            with self.assertRaisesRegex(ValueError, "Generated files differ"):
                materialize(directory, smaller, check=True)

    def test_nonempty_directory_without_manifest_is_preserved(self):
        with tempfile.TemporaryDirectory(dir=".agents/cache") as temporary:
            directory = Path(temporary) / "skills"
            directory.mkdir()
            (directory / "personal.md").write_text("keep")
            with self.assertRaisesRegex(ValueError, "Unmanaged"):
                materialize(directory, self.build(), check=False)
            self.assertEqual((directory / "personal.md").read_text(), "keep")

    def test_interrupted_generation_can_resume_without_deleting_user_files(self):
        for existing_manifest in (False, True):
            with self.subTest(existing_manifest=existing_manifest), tempfile.TemporaryDirectory(dir=".agents/cache") as temporary:
                directory = Path(temporary) / "skills"
                output = self.build()
                if existing_manifest:
                    materialize(directory, output, check=False)
                for name in ("how/new-a.txt", "how/new-b.txt"):
                    output[name] = name.encode()
                manifest = json.loads(output["SOURCES.json"])
                for name in ("how/new-a.txt", "how/new-b.txt"):
                    manifest["files"][name] = {"source_mode": "100644"}
                output["SOURCES.json"] = json.dumps(manifest).encode()
                write_bytes = Path.write_bytes

                def fail_second_new_file(path, content):
                    if path.name == "new-b.txt":
                        raise PermissionError("Injected write interruption")
                    return write_bytes(path, content)

                with patch.object(Path, "write_bytes", fail_second_new_file):
                    with self.assertRaises(PermissionError):
                        materialize(directory, output, check=False)
                materialize(directory, output, check=False)
                materialize(directory, output, check=True)

    def test_stale_cleanup_leaves_unmanaged_empty_directories(self):
        with tempfile.TemporaryDirectory(dir=".agents/cache") as temporary:
            directory = Path(temporary) / "skills"
            output = self.build()
            materialize(directory, output, check=False)
            personal = directory / "personal/empty"
            personal.mkdir(parents=True)
            materialize(directory, output, check=False)
            self.assertTrue(personal.is_dir())

    def test_all_outputs_have_ownership_provenance_and_plain_licenses_stay_upstream_only(self):
        adapted = self.build()
        self.transforms["skills/how"]["replacements"] = []
        plain = self.build()
        self.assertEqual(plain["how/LICENSE.txt"], self.source["LICENSE"])
        for output in [plain, adapted]:
            files = json.loads(output["SOURCES.json"])["files"]
            self.assertEqual(set(files), set(output) - {"SOURCES.json"})
            for name, record in files.items():
                self.assertEqual(record["output_sha256"], hashlib.sha256(output[name]).hexdigest())

    def test_license_sidecar_cannot_overwrite_future_upstream_content(self):
        path = "skills/how/LICENSE.txt"
        self.source[path] = b"An upstream sidecar"
        self.lock["files"][path] = {"mode": "100644", "sha256": hashlib.sha256(self.source[path]).hexdigest()}
        with self.assertRaisesRegex(ValueError, "License sidecar collision"):
            self.build()

    def test_unsafe_previous_manifest_is_refused_before_deleting_anything(self):
        with tempfile.TemporaryDirectory(dir=".agents/cache") as temporary:
            directory = Path(temporary) / "skills"
            materialize(directory, self.build(), check=False)
            outside = Path(temporary) / "keep.md"
            outside.write_text("keep")
            (directory / "SOURCES.json").write_text('{"files":{"../keep.md":{}}}')
            with self.assertRaisesRegex(ValueError, "Invalid relative path"):
                materialize(directory, self.build(), check=False)
            self.assertEqual(outside.read_text(), "keep")
            self.assertTrue((directory / "how/SKILL.md").is_file())

    def test_generated_symlink_is_refused_without_touching_target(self):
        cache = Path(".agents/cache")
        cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as temporary:
            directory = Path(temporary) / "skills"
            directory.mkdir()
            victim = Path(temporary) / "outside"
            victim.write_text("keep")
            (directory / "link").symlink_to(victim.resolve())
            with self.assertRaisesRegex(ValueError, "symlink"):
                materialize(directory, self.build(), check=False)
            self.assertEqual(victim.read_text(), "keep")

    def test_changed_manifest_or_adapter_invalidates_generated_tree(self):
        cache = Path(".agents/cache")
        cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=cache) as temporary:
            directory = Path(temporary) / "skills"
            materialize(directory, self.build(), check=False)
            self.transforms["skills/how"]["replacements"][0]["reason"] = "Reviewed again"
            with self.assertRaisesRegex(ValueError, "Generated files differ"):
                materialize(directory, self.build(), check=True)
            materialize(directory, self.build(), check=False)
            output = render(self.lock, self.transforms, self.source.__getitem__, b"Changed adapter", b"Model defaults\n", b"Project MIT\n")
            with self.assertRaisesRegex(ValueError, "Generated files differ"):
                materialize(directory, output, check=True)
            output = render(self.lock, self.transforms, self.source.__getitem__, b"T3 adapter\n", b"Changed defaults", b"Project MIT\n")
            with self.assertRaisesRegex(ValueError, "Generated files differ"):
                materialize(directory, output, check=True)

    def test_shared_models_cannot_overwrite_upstream_reference(self):
        path = "skills/how/references/models.md"
        self.source[path] = b"Upstream defaults"
        self.lock["files"][path] = {"mode": "100644", "sha256": hashlib.sha256(self.source[path]).hexdigest()}
        with self.assertRaisesRegex(ValueError, "Model defaults collision"):
            self.build()

    def test_default_roles_preserve_the_upstream_setup_role_inventory(self):
        transforms = json.loads(Path("upstream/transforms.json").read_text())
        original = next(rule["before"] for rule in transforms["skills/setup-pstack"]["replacements"]
                        if "# pstack model configuration." in rule["before"])
        upstream_roles = {line.split(": ", 1)[0] for line in original.splitlines()
                          if re.match(r"^[^#\n]+: (?:grok-|claude-)", line)}
        default_roles = {line.split(": ", 1)[0] for line in Path("models.md").read_text().splitlines()
                         if re.match(r"^[^#\n]+: (?:codex/|claudeAgent/)", line)}
        self.assertTrue(upstream_roles)
        self.assertEqual(default_roles, upstream_roles)


if __name__ == "__main__":
    unittest.main()


class DependencyMergeTests(unittest.TestCase):
    def test_dependency_retains_identity_license_and_executable_mode(self):
        root = {"SOURCES.json": b'{"files": {}}'}
        lock = {"path": "cursor-team-kit", "remote": "repo", "commit": "b" * 40}
        dep = {"control-cli/LICENSE.txt": b"Cursor notice",
               "control-cli/run": b"#!/bin/sh\nexit 0\n", "SOURCES.json": json.dumps({"transforms": "recipe", "files": {
                   "control-cli/LICENSE.txt": {"generated_from": "cursor-team-kit/LICENSE", "source_mode": "100644"},
                   "control-cli/run": {"source": "skills/control-cli/run", "source_sha256": "hash", "source_mode": "100755"}}}).encode()}
        merge_dependency(root, dep, lock)
        self.assertEqual(json.loads(root["SOURCES.json"])["files"]["control-cli/run"]["source_root"], "cursor-team-kit")
        self.assertEqual(root["control-cli/LICENSE.txt"], b"Cursor notice")
        with tempfile.TemporaryDirectory(dir=".agents/cache") as directory:
            path = Path(directory) / "skills"
            materialize(path, root, False)
            self.assertEqual((path / "control-cli/run").stat().st_mode & 0o111, 0o111)
            materialize(path, root, True)

    def test_collision_fails_before_mutating_output(self):
        root = {"skills/shared/SKILL.md": b"primary", "SOURCES.json": b'{"files": {}}'}
        before = copy.deepcopy(root)
        dep = {"skills/shared/SKILL.md": b"other", "SOURCES.json": b'{"files": {}, "transforms": "x"}'}
        with self.assertRaisesRegex(ValueError, "collision"):
            merge_dependency(root, dep, {"path": "cursor-team-kit"})
        self.assertEqual(root, before)
