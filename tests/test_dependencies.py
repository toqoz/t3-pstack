import json
from pathlib import Path
import re
import unittest


NAMED_SKILL = re.compile(
    r"\*\*([a-z0-9-]+)\*\*(?: principle)? skills?"
    r"|`/?([a-z0-9-]+)`(?: principle)? skills?"
    r"|(?<![\w/.-])/([a-z][a-z0-9-]+)(?![\w/.-])"
)


def companions(text, known):
    found = set()
    for match in NAMED_SKILL.finditer(text):
        name = next(value for value in match.groups() if value)
        if name not in known and "principle-" + name in known:
            name = "principle-" + name
        if name in known:
            found.add(name)
    return found


class NamedDependencyTests(unittest.TestCase):
    def test_recognized_companions_are_selected_or_explicitly_deferred(self):
        manifest = json.loads(Path("upstream/transforms.json").read_text())
        lock = json.loads(Path("upstream/lock.json").read_text())
        known = {path.split("/")[1] for path in lock["files"]
                 if path.startswith("skills/") and path.count("/") == 2 and path.endswith("/SKILL.md")}
        dependency = json.loads(Path("upstream/dependencies/cursor-team-kit/transforms.json").read_text())
        dependency_lock = json.loads(Path("upstream/dependencies/cursor-team-kit/lock.json").read_text())
        known |= {path.split("/")[1] for path in dependency_lock["files"]
                  if path.startswith("skills/") and path.count("/") == 2 and path.endswith("/SKILL.md")}
        manifest = {**manifest, **dependency}
        selected = {unit.split("/")[1] for unit in manifest}
        deferred = {
            "setup-pstack": {"create-verification-skill", "create-formal-verification-skill"},
            "principle-prove-it-works": {"show-me-your-work"},
        }
        for unit, spec in manifest.items():
            owner = unit.split("/")[1]
            directory = Path(spec["target"])
            self.assertTrue((directory / "SKILL.md").is_file(), str(directory))
            for path in directory.rglob("*.md"):
                if path.name in {"models.md", "t3.md"}:
                    continue
                missing = companions(path.read_text(), known) - selected - deferred.get(owner, set())
                self.assertFalse(missing, f"{path}: missing named companions {sorted(missing)}")

    def test_missing_unslop_is_detected_from_the_actual_writing_skill(self):
        text = Path("skills/technical-writing/SKILL.md").read_text()
        self.assertEqual(companions(text, {"technical-writing", "unslop"}) - {"technical-writing"}, {"unslop"})

    def test_short_principle_names_resolve_to_bundled_names(self):
        self.assertEqual(
            companions("Apply the **boundary-discipline** principle skill.", {"principle-boundary-discipline"}),
            {"principle-boundary-discipline"},
        )

    def test_an_ordinary_mention_is_not_a_required_companion(self):
        self.assertEqual(companions("Do not paste swarm logs into a PR.", {"swarm"}), set())
