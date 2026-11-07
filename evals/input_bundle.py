"""Exercise the documented two-patch input protocol in disposable Git fixtures."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / '.agents/cache/input-bundle-eval'


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.STDOUT)


def state(repo, paths, index=False):
    result = {}
    for name in paths:
        if index:
            entry = git(repo, 'ls-files', '--stage', '--', name).decode().strip()
            if not entry:
                result[name] = None
                continue
            mode, oid, _ = entry.split('\t')[0].split()
            content = git(repo, 'cat-file', 'blob', oid)
        else:
            path = repo / name
            if not path.exists() and not path.is_symlink():
                result[name] = None
                continue
            mode = '120000' if path.is_symlink() else ('100755' if path.stat().st_mode & 0o111 else '100644')
            content = os.readlink(path).encode() if path.is_symlink() else path.read_bytes()
        result[name] = {'mode': mode, 'sha256': hashlib.sha256(content).hexdigest()}
    return result


def main():
    if RUN.exists():
        shutil.rmtree(RUN)
    parent, replay, bundle = (RUN / name for name in ('parent', 'replay', 'inputs'))
    parent.mkdir(parents=True)
    bundle.mkdir()
    git(parent, 'init', '-q')
    git(parent, 'config', 'user.name', 'Input Fixture')
    git(parent, 'config', 'user.email', 'fixture@example.invalid')
    git(parent, 'config', 'core.filemode', 'true')
    for name, content in {'mixed.txt': b'base\n', 'deleted.txt': b'gone\n', 'rename.txt': b'rename\n', 'exec.sh': b'echo fixture\n', 'binary.dat': bytes(range(256)), '.gitignore': b'.ignored/\n'}.items():
        (parent / name).write_bytes(content)
    git(parent, 'add', '.')
    git(parent, 'commit', '-qm', 'Fixture baseline')
    base = git(parent, 'rev-parse', 'HEAD').decode().strip()
    (parent / 'mixed.txt').write_text('staged\n')
    git(parent, 'add', 'mixed.txt')
    (parent / 'mixed.txt').write_text('unstaged after staged\n')
    git(parent, 'mv', 'rename.txt', 'renamed.txt')
    (parent / 'deleted.txt').unlink()
    (parent / 'exec.sh').chmod(0o755)
    (parent / 'binary.dat').write_bytes(b'\x00\xffmodified\x00')
    (parent / 'untracked.txt').write_text('new input\n')
    (parent / '.ignored').mkdir()
    (parent / '.ignored/sketch.md').write_text('required grounding\n')
    (parent / 'link').symlink_to('mixed.txt')
    paths = ['mixed.txt', 'deleted.txt', 'rename.txt', 'renamed.txt', 'exec.sh', 'binary.dat', 'untracked.txt', '.ignored/sketch.md', 'link', '.gitignore']
    options = ['--binary', '--full-index', '--no-ext-diff', '--no-textconv']
    patches = {'staged.patch': git(parent, 'diff', '--cached', *options, '--', *paths), 'unstaged.patch': git(parent, 'diff', *options, '--', *paths)}
    for name, content in patches.items():
        (bundle / name).write_bytes(content)
    payloads = ['untracked.txt', '.ignored/sketch.md', 'link']
    for name in payloads:
        dest = bundle / 'payloads' / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(parent / name, dest, follow_symlinks=False)
    manifest = {'base': base, 'index': state(parent, paths, True), 'worktree': state(parent, paths), 'patches': {name: hashlib.sha256(data).hexdigest() for name, data in patches.items()}}
    (bundle / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    # This is a disposable repository fixture, not a child agent checkout.
    subprocess.run(['git', 'clone', '-q', '--no-hardlinks', str(parent), str(replay)], check=True)
    git(replay, 'config', 'core.filemode', 'true')
    assert git(replay, 'rev-parse', 'HEAD').decode().strip() == base
    assert not git(replay, 'status', '--porcelain')
    for name, expected in manifest['patches'].items():
        assert hashlib.sha256((bundle / name).read_bytes()).hexdigest() == expected
    git(replay, 'apply', '--index', '--binary', str(bundle / 'staged.patch'))
    git(replay, 'apply', '--binary', str(bundle / 'unstaged.patch'))
    for name in payloads:
        dest = replay / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(bundle / 'payloads' / name, dest, follow_symlinks=False)
    assert state(replay, paths, True) == manifest['index']
    assert state(replay, paths) == manifest['worktree']
    (replay / 'mixed.txt').write_text('wrong input\n')
    assert state(replay, paths) != manifest['worktree']
    assert state(parent, paths, True) == manifest['index']
    assert state(parent, paths) == manifest['worktree']
    result = {'verdict': 'PASS', 'paths': paths, 'cases': ['staged plus unstaged on one path', 'rename', 'deletion', 'executable mode', 'binary data', 'untracked input', 'relevant ignored input', 'symlink', 'tamper rejected'], 'scope': 'local Git fixture; no T3 child checkout or dispatch'}
    (RUN / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
