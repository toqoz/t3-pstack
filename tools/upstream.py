"""Record and compare pstack sources without installing or executing them."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


REMOTE = "https://github.com/cursor/plugins.git"
MARKDOWN_LINKS = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def snapshot(repo, revision, source_path="pstack"):
    if source_path not in {"pstack", "cursor-team-kit"}:
        raise ValueError("Unsupported source package")
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Use a full commit SHA, not a moving branch or tag")
    if git(repo, "remote", "get-url", "origin").decode().strip() != REMOTE:
        raise ValueError(f"Expected origin {REMOTE}")
    entries = git(repo, "ls-tree", "-r", "-z", revision, "--", source_path + "/")
    files = {}
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        if kind != "blob" or mode not in {"100644", "100755"}:
            raise ValueError(f"Unsupported upstream entry: {raw_path!r}")
        path = raw_path.decode().removeprefix(source_path + "/")
        content = git(repo, "cat-file", "blob", oid)
        files[path] = {"mode": mode, "sha256": hashlib.sha256(content).hexdigest()}
    if "LICENSE" not in files or not any(p.endswith("/SKILL.md") for p in files):
        raise ValueError("Expected pstack LICENSE and skills")
    return {"remote": REMOTE, "commit": revision, "path": source_path, "files": files}


def changes(before, after):
    return {
        "added": sorted(after.keys() - before.keys()),
        "removed": sorted(before.keys() - after.keys()),
        "changed": sorted(p for p in before.keys() & after.keys() if before[p] != after[p]),
    }


def units(files):
    result = {}
    for path, record in files.items():
        parts = path.split("/")
        unit = "/".join(parts[:2]) if parts[0] == "skills" else path
        result.setdefault(unit, {})[path] = record
    return result


def fingerprint(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()


def check_docs(root, lock, generated=None):
    upstream = root / "upstream"
    remote = lock["remote"].removesuffix(".git")
    tree = f"{remote}/tree/{lock['commit']}/{lock['path']}"
    errors = []
    guide = upstream / "README.md"
    if not guide.exists() or tree not in guide.read_text():
        errors.append("Central source guide must link the locked upstream revision")
    expected = {
        f"{remote}/blob/{lock['commit']}/{lock['path']}/{path}": path
        for path in lock["files"]
        if path.startswith("skills/") and path.count("/") == 2 and path.endswith("/SKILL.md")
    }
    indexed = Counter()
    indexes = set(upstream.glob("skills/*/README.md"))
    generated_paths = {(root / "skills" / name).resolve() for name in generated} if generated is not None else None
    for document in sorted(upstream.rglob("*.md")):
        for target in MARKDOWN_LINKS.findall(document.read_text()):
            url = urlsplit(target)
            if document in indexes and target.startswith(remote + "/blob/") and "/skills/" in target:
                if target not in expected:
                    errors.append(f"Source link is not in the locked skill inventory: {target}")
                else:
                    indexed[target] += 1
            if not url.scheme and not url.netloc and url.path:
                local = document.parent / unquote(url.path)
                in_distribution = local.resolve().is_relative_to((root / "skills").resolve())
                exists = local.resolve() in generated_paths if in_distribution and generated_paths is not None else local.exists()
                if not exists:
                    errors.append(f"Broken local link in {document.relative_to(root)}: {target}")
    errors.extend(f"Missing skill index entry: {path}" for url, path in expected.items() if not indexed[url])
    errors.extend(f"Duplicate skill index entry: {expected[url]}" for url, count in indexed.items() if count > 1)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    capture = sub.add_parser("snapshot")
    capture.add_argument("repo", type=Path)
    capture.add_argument("commit")
    capture.add_argument("--path", choices=["pstack", "cursor-team-kit"], default="pstack")
    compare = sub.add_parser("diff")
    compare.add_argument("candidate", type=Path)
    compare.add_argument("--lock", type=Path, default=None)
    check = sub.add_parser("check")
    check.add_argument("--repo", type=Path, help="Verify lock against the pinned Git objects")
    args = parser.parse_args()
    if args.command == "snapshot":
        print(json.dumps(snapshot(args.repo, args.commit, args.path), indent=2))
        return
    root = Path(__file__).resolve().parents[1]
    lock = json.loads((root / "upstream/lock.json").read_text())
    if args.command == "diff":
        if args.lock is not None:
            lock = json.loads(args.lock.read_text())
        candidate = json.loads(args.candidate.read_text())
        if (candidate["remote"], candidate["path"]) != (lock["remote"], lock["path"]):
            raise ValueError("Candidate has a different upstream")
        print(json.dumps(changes(lock["files"], candidate["files"]), indent=2))
        return
    errors = check_docs(root, lock)
    if args.repo and snapshot(args.repo, lock["commit"]) != lock:
        errors.append("Lock differs from pinned upstream Git objects")
    license_bytes = (root / "licenses/pstack-MIT.txt").read_bytes()
    if hashlib.sha256(license_bytes).hexdigest() != lock["files"]["LICENSE"]["sha256"]:
        errors.append("Upstream license differs from locked source")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"OK: {len(lock['files'])} source files and Markdown review indexes")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
