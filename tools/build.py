"""Generate the selected T3 skills from pinned upstream Git objects."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import posixpath
import subprocess
import sys
from urllib.parse import urlsplit

from tools.upstream import MARKDOWN_LINKS, fingerprint, git, snapshot, units, check_docs


def safe_path(value):
    if not isinstance(value, str):
        raise ValueError(f"Relative path must be a string: {value!r}")
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(p in {"", ".", ".."} for p in value.split("/")) or "\\" in value:
        raise ValueError(f"Invalid relative path: {value}")
    return path


def transform(text, replacements):
    spans = []
    for rule in replacements:
        before = rule["before"]
        start = text.find(before)
        if not before or start < 0 or text.find(before, start + 1) >= 0:
            raise ValueError("Transformation must match exactly once: " + rule["reason"])
        spans.append((start, start + len(before), rule["after"]))
    spans.sort()
    if any(left[1] > right[0] for left, right in zip(spans, spans[1:])):
        raise ValueError("Transformation source spans overlap")
    for start, end, after in reversed(spans):
        text = text[:start] + after + text[end:]
    return text


def check_generated_links(output):
    for name, content in output.items():
        if not name.endswith(".md"):
            continue
        for target in MARKDOWN_LINKS.findall(content.decode()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path.endswith(".md"):
                continue
            destination = posixpath.normpath(f"{PurePosixPath(name).parent}/{url.path}")
            if destination not in output:
                raise ValueError(f"Broken generated Markdown link in {name}: {target}")


def render(lock, transforms, read_source, adapter, models, project_license):
    if not isinstance(transforms, dict):
        raise ValueError("Transformations must be an object")
    for unit, spec in transforms.items():
        if not isinstance(spec, dict) or not isinstance(spec.get("replacements"), list):
            raise ValueError(f"Expected target and replacements list: {unit}")
        safe_path(spec.get("target"))
        if not isinstance(spec.get("imports", {}), dict):
            raise ValueError(f"Imports must map relative destinations to pinned sources: {unit}")
        for relative, source in spec.get("imports", {}).items():
            safe_path(relative)
            safe_path(source)
            if source not in lock["files"]:
                raise ValueError(f"Imported source is not pinned: {source}")
        for rule in spec["replacements"]:
            if not isinstance(rule, dict) or any(
                not isinstance(rule.get(key), str) for key in ("file", "before", "after", "reason")
            ):
                raise ValueError(f"Replacement requires string file, before, after, reason: {unit}")
            safe_path(rule["file"])
    upstream_license = read_source("LICENSE")
    if hashlib.sha256(upstream_license).hexdigest() != lock["files"]["LICENSE"]["sha256"]:
        raise ValueError("Source hash mismatch: LICENSE")
    source_name = lock.get("path", "pstack")
    output = {}
    provenance = {"remote": lock["remote"], "commit": lock["commit"], "files": {}}
    source_units = units(lock["files"])
    for unit, spec in sorted(transforms.items()):
        if unit not in source_units or not unit.startswith("skills/"):
            raise ValueError(f"Selected source is not an upstream skill: {unit}")
        target = str(safe_path(spec["target"]))
        if not target.startswith("skills/"):
            raise ValueError(f"Target must be within skills/: {unit}")
        target = target.removeprefix("skills/")
        rules = spec["replacements"]
        matched_files = set()
        needs_adapter = False
        needs_models = False
        files = {str(PurePosixPath(path).relative_to(unit)): path for path in source_units[unit]}
        for relative, source in spec.get("imports", {}).items():
            if relative in files:
                raise ValueError(f"Imported destination collision: {relative}")
            files[relative] = source
        for relative, path in sorted(files.items()):
            if lock["files"][path]["mode"] not in {"100644", "100755"}:
                raise ValueError(f"Unsupported source mode: {path}")
            destination = str(safe_path(target + "/" + relative))
            content = read_source(path)
            if hashlib.sha256(content).hexdigest() != lock["files"][path]["sha256"]:
                raise ValueError(f"Source hash mismatch: {path}")
            applicable = [rule for rule in rules if rule["file"] == relative]
            if applicable:
                content = transform(content.decode(), applicable).encode()
                matched_files.add(relative)
            if path.endswith(".md"):
                needs_adapter |= b"references/t3.md" in content
                needs_models |= b"references/models.md" in content
            if destination in output:
                raise ValueError(f"Output collision: {destination}")
            output[destination] = content
            provenance["files"][destination] = {
                "source": path,
                "source_sha256": lock["files"][path]["sha256"],
                "source_mode": lock["files"][path]["mode"],
            }
        if matched_files != {rule["file"] for rule in rules}:
            raise ValueError(f"Transformation references missing file: {unit}")
        if needs_adapter:
            adapter_path = target + "/references/t3.md"
            if adapter_path in output:
                raise ValueError(f"Adapter collision: {adapter_path}")
            output[adapter_path] = adapter
            provenance["files"][adapter_path] = {"generated_from": "adapters/t3.md", "source_mode": "100644"}
        if needs_models or needs_adapter:
            models_path = target + "/references/models.md"
            if models_path in output:
                raise ValueError(f"Model defaults collision: {models_path}")
            output[models_path] = models
            provenance["files"][models_path] = {"generated_from": "models.md", "source_mode": "100644"}
        license_path = target + "/LICENSE.txt"
        if license_path in output:
            raise ValueError(f"License sidecar collision: {license_path}")
        output[license_path] = upstream_license
        license_sources = [f"{source_name}/LICENSE"]
        if rules or spec.get("imports") or needs_adapter or needs_models:
            output[license_path] += b"\nLocal adaptations (MIT):\n\n" + project_license
            license_sources.append("LICENSE")
        provenance["files"][license_path] = {"generated_from": license_sources, "source_mode": "100644"}
    check_generated_links(output)
    provenance["transforms"] = fingerprint(transforms)
    provenance["adapter"] = hashlib.sha256(adapter).hexdigest()
    provenance["models"] = hashlib.sha256(models).hexdigest()
    for name, content in output.items():
        provenance["files"][name]["output_sha256"] = hashlib.sha256(content).hexdigest()
    output["SOURCES.json"] = (json.dumps(provenance, indent=2) + "\n").encode()
    return output


def merge_dependency(output, dependency, lock):
    """Merge one pinned package without losing source identity or file modes."""
    provenance = json.loads(output["SOURCES.json"])
    incoming = json.loads(dependency["SOURCES.json"])
    for name, content in dependency.items():
        if name == "SOURCES.json":
            continue
        if name in output:
            raise ValueError(f"Dependency output collision: {name}")
    for name, content in dependency.items():
        if name != "SOURCES.json":
            output[name] = content
    for name, record in incoming["files"].items():
        provenance["files"][name] = {**record, "source_root": lock["path"]}
    provenance.setdefault("dependencies", {})[lock["path"]] = {
        "remote": lock["remote"], "commit": lock["commit"],
        "lock": fingerprint(lock), "transforms": incoming["transforms"],
    }
    output["SOURCES.json"] = (json.dumps(provenance, indent=2) + "\n").encode()


def materialize(directory, output, check):
    for name in output:
        safe_path(name)
    if directory.is_symlink():
        raise ValueError("Generated directory must not be a symlink")
    actual = {}
    actual_executable = {}
    sources = json.loads(output.get("SOURCES.json", b'{"files": {}}'))["files"]
    executable = {name: 0o100 if sources.get(name, {}).get("source_mode") == "100755" else 0 for name in output}
    if directory.exists():
        for path in directory.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Generated path must not be a symlink: {path}")
            if path.is_file():
                actual[path.relative_to(directory).as_posix()] = path.read_bytes()
                # Git records the executable flag, not group/other permissions under the checkout umask.
                actual_executable[path.relative_to(directory).as_posix()] = path.stat().st_mode & 0o100
    if check:
        if actual != output or actual_executable != executable:
            raise ValueError("Generated files differ; run python3 -m tools.build --repo <upstream> --write")
        return
    if actual:
        previous = json.loads(actual["SOURCES.json"]).get("files") if "SOURCES.json" in actual else {}
        if not isinstance(previous, dict):
            raise ValueError("Invalid generated ownership manifest")
        owned = {str(safe_path(name)) for name in previous} | {"SOURCES.json"}
        # Completed new files from an interrupted write can be safely adopted.
        unknown = {name for name in actual.keys() - owned if actual[name] != output.get(name)}
        if unknown:
            raise ValueError("Unmanaged generated files; refusing to overwrite: " + ", ".join(sorted(unknown)))
        stale_parents = set()
        for name in actual.keys() - output.keys():
            path = directory / name
            path.unlink()
            parent = path.parent
            while parent != directory:
                stale_parents.add(parent)
                parent = parent.parent
        for path in sorted(stale_parents, key=lambda p: len(p.parts), reverse=True):
            if path.is_dir() and not any(path.iterdir()):
                path.rmdir()
    for name in sorted(output, key=lambda name: name == "SOURCES.json"):
        content = output[name]
        path = directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        path.chmod(0o755 if executable[name] else 0o644)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    lock = json.loads((root / "upstream/lock.json").read_text())
    if snapshot(args.repo, lock["commit"]) != lock:
        raise ValueError("Lock differs from pinned upstream Git objects")
    if git(args.repo, "show", f"{lock['commit']}:pstack/LICENSE") != (root / "licenses/pstack-MIT.txt").read_bytes():
        raise ValueError("Primary license differs from pinned source")
    output = render(
        lock,
        json.loads((root / "upstream/transforms.json").read_text()),
        lambda path: git(args.repo, "show", f"{lock['commit']}:pstack/{path}"),
        (root / "adapters/t3.md").read_bytes(),
        (root / "models.md").read_bytes(),
        (root / "LICENSE").read_bytes(),
    )
    dependency_dir = root / "upstream/dependencies/cursor-team-kit"
    dependency_lock = json.loads((dependency_dir / "lock.json").read_text())
    if snapshot(args.repo, dependency_lock["commit"], dependency_lock["path"]) != dependency_lock:
        raise ValueError("Dependency lock differs from pinned upstream Git objects")
    dependency = render(
        dependency_lock, json.loads((dependency_dir / "transforms.json").read_text()),
        lambda path: git(args.repo, "show", f"{dependency_lock['commit']}:cursor-team-kit/{path}"),
        (root / "adapters/t3.md").read_bytes(), (root / "models.md").read_bytes(),
        (root / "LICENSE").read_bytes(),
    )
    if git(args.repo, "show", f"{dependency_lock['commit']}:cursor-team-kit/LICENSE") != (root / "licenses/cursor-team-kit-MIT.txt").read_bytes():
        raise ValueError("Dependency license differs from pinned source")
    merge_dependency(output, dependency, dependency_lock)
    check_generated_links(output)
    errors = check_docs(root, lock, output)
    if errors:
        raise ValueError("\n".join(errors))
    materialize(root / "skills", output, args.check)
    print(f"OK: {len(output)} generated files")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
