"""Check the installable artifact without invoking an installer or changing HOME."""

import hashlib
import json
import os
from pathlib import Path
import re
import unittest


class DistributionTests(unittest.TestCase):
    def test_installed_coordinators_carry_their_own_companion_rules(self):
        for name in ["swarm", "arena", "reflect"]:
            text = (Path("skills") / name / "SKILL.md").read_text()
            self.assertNotIn("distribution root README", text)
            self.assertNotIn("distribution README's", text)
            self.assertIn("../<name>/SKILL.md", text)
            self.assertIn("principle-<name>", text)

    def test_skill_names_and_per_directory_licenses_survive_individual_copy(self):
        sources = json.loads(Path("skills/SOURCES.json").read_text())
        specs = json.loads(Path("upstream/transforms.json").read_text())
        dependency = json.loads(Path("upstream/dependencies/cursor-team-kit/transforms.json").read_text())
        for package, recipes in [("pstack", specs), ("cursor-team-kit", dependency)]:
            for spec in recipes.values():
                directory = Path(spec["target"])
                text = (directory / "SKILL.md").read_text()
                self.assertEqual(re.search(r"^name: (.+)$", text, re.M)[1], directory.name)
                upstream_license = Path(f"licenses/{package}-MIT.txt").read_bytes()
                adapted = bool(spec["replacements"] or spec.get("imports") or
                               (directory / "references/models.md").exists() or
                               (directory / "references/t3.md").exists())
                expected = upstream_license
                if adapted:
                    expected += b"\nLocal adaptations (MIT):\n\n" + Path("LICENSE").read_bytes()
                self.assertEqual((directory / "LICENSE.txt").read_bytes(), expected)
        for name, record in sources["files"].items():
            self.assertEqual(hashlib.sha256((Path("skills") / name).read_bytes()).hexdigest(),
                             record["output_sha256"], name)

    def test_only_allowlisted_fixtures_exist_outside_the_skill_container(self):
        found = set()
        for directory, dirs, files in os.walk("."):
            if directory == ".":
                dirs[:] = [name for name in dirs if name not in {".git", ".agents", "skills"}]
            if "SKILL.md" in files:
                found.add((Path(directory) / "SKILL.md").as_posix())
        self.assertEqual(found, {"evals/fixtures/reflect/dispatch/SKILL.md",
                                 "evals/fixtures/reflect/handoff/SKILL.md"})
        self.assertFalse(Path("dist").exists(), "Old dist output must not be redistributed")
