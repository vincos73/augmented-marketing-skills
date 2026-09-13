#!/usr/bin/env python3
"""Build or check reproducible local suite archives without installing or publishing."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAMES = (
    'augmented-marketing-assistant', 'setup-business-context', 'setup-marketing-system',
    'setup-brand-voice', 'define-marketing-challenge', 'choose-marketing-direction',
    'define-marketing-mix', 'design-campaign', 'campaign-review', 'campaign-debrief',
    'content-director', 'write-marketing-copy',
)

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def encoded(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()

def checksums(files: dict[str, bytes]) -> bytes:
    return ''.join(f'{sha(data)}  {rel}\n' for rel, data in sorted(files.items()) if rel != 'SHA256SUMS').encode()

def build_state(version: str) -> str:
    """Keep prerelease candidates distinct from a completed stable build."""
    return 'local-candidate-not-published' if '-' in version else 'built'

def skill_files(name: str, openai: bool) -> dict[str, bytes]:
    folder = ROOT / 'skills' / name
    result = {}
    for p in sorted(folder.rglob('*')):
        rel = p.relative_to(folder)
        if any(part.startswith('.') or part == '__pycache__' for part in rel.parts):
            continue
        if p.is_symlink():
            raise ValueError(f'Symlink not portable: {p}')
        if not p.is_file() or p.name == 'INSTALL.md':
            continue
        if rel.parts[0] == 'agents' and not openai:
            continue
        if rel.parts[0] not in {'SKILL.md', 'references', 'scripts', 'assets', 'agents'}:
            raise ValueError(f'Unclassified package resource: {p}')
        result[str(rel)] = p.read_bytes()
    if 'SKILL.md' not in result:
        raise ValueError(f'Missing entrypoint: {name}')
    return result

def archive(files: dict[str, bytes]) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 9, 12, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if '/scripts/' in name else 0o100644) << 16
            z.writestr(info, content)
    data = stream.getvalue()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        if z.testzip() or set(z.namelist()) != set(files):
            raise ValueError('Archive integrity failure')
        for name, content in files.items():
            if z.read(name) != content:
                raise ValueError(f'Archive/source mismatch: {name}')
    return data

def build() -> tuple[str, dict[str, bytes]]:
    codex = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
    claude = json.loads((ROOT / 'claude/.claude-plugin/plugin.json').read_text())
    version = codex['version']
    if version != claude['version']:
        raise ValueError('Plugin versions differ')
    actual_names = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
    if actual_names != set(NAMES):
        raise ValueError(f'Skill inventory differs: {actual_names ^ set(NAMES)}')
    source = {}
    versions = {}
    for name in NAMES:
        folder = ROOT / 'skills' / name
        text = (folder / 'SKILL.md').read_text()
        match = re.search(r'(?m)^  version: "([^"]+)"$', text)
        if not match:
            raise ValueError(f'Missing version: {name}')
        versions[name] = match[1]
        for p in sorted(folder.rglob('*')):
            if p.is_file() and not any(x.startswith('.') or x == '__pycache__' for x in p.relative_to(folder).parts):
                source[str(p.relative_to(ROOT))] = sha(p.read_bytes())
    for rel in ('.codex-plugin/plugin.json', 'claude/.claude-plugin/plugin.json'):
        source[rel] = sha((ROOT / rel).read_bytes())
    output = {}
    package_records = []
    for kind, manifest in [('openai', codex), ('claude', claude)]:
        selected = NAMES
        prefix = '.codex-plugin' if kind == 'openai' else '.claude-plugin'
        files = {f'{prefix}/plugin.json': encoded(manifest)}
        for name in selected:
            files.update({f'skills/{name}/{rel}': data for rel, data in skill_files(name, kind == 'openai').items()})
        filename = f'augmented-marketing-suite-{version}.zip' if kind == 'openai' else f'augmented-marketing-suite-claude-v{version}.zip'
        rel = f'{kind}/{filename}'
        output[rel] = archive(files)
        package_records.append({'archive': rel, 'sha256': sha(output[rel]), 'skills': {n: versions[n] for n in selected}})
    for name in NAMES[1:]:
        rel = f'agent-skills/{name}-{versions[name]}.zip'
        output[rel] = archive({f'{name}/{p}': data for p, data in skill_files(name, False).items()})
        package_records.append({'archive': rel, 'sha256': sha(output[rel]), 'skills': {name: versions[name]}})
    base_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    output['manifest.json'] = encoded({
        'suite_version': version, 'state': build_state(version),
        'source_base_commit': base_commit, 'source_state': 'working-tree; source_sha256 identifies the actual files',
        'source_sha256': source, 'packages': package_records,
        'policy': {'openai': '12 skills, including Assistant and agents metadata',
                   'claude': '12 skills, including Assistant; no agents metadata',
                   'portable': 'one specialist folder; no agents metadata or INSTALL.md'},
    })
    output['SHA256SUMS'] = checksums(output)
    return version, output

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify existing files against current sources; do not write.')
    parser.add_argument('--output', type=Path, help='Destination; defaults to dist/<version or prerelease suffix>.')
    args = parser.parse_args()
    version, files = build()
    destination = args.output or ROOT / 'dist' / version.split('-', 1)[-1]
    if args.check:
        manifest_path = destination / 'manifest.json'
        if not manifest_path.is_file():
            raise SystemExit(f'FAIL stale or missing: {manifest_path}')
        try:
            recorded = json.loads(manifest_path.read_text())
        except (ValueError, UnicodeError):
            raise SystemExit(f'FAIL invalid manifest: {manifest_path}')
        base_commit = recorded.get('source_base_commit') if isinstance(recorded, dict) else None
        if not isinstance(base_commit, str) or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', base_commit):
            raise SystemExit(f'FAIL invalid source_base_commit: {manifest_path}')
        # The build's base commit is provenance, not a fingerprint of its content.
        # Keep it while comparing every source/package hash and all other metadata.
        expected = json.loads(files['manifest.json'])
        expected['source_base_commit'] = base_commit
        files['manifest.json'] = encoded(expected)
        files['SHA256SUMS'] = checksums(files)
    extra = {str(p.relative_to(destination)) for p in destination.rglob('*.zip')} - set(files)
    if extra:
        manifest = destination / 'manifest.json'
        previous = json.loads(manifest.read_text()) if manifest.is_file() else {}
        known = {p['archive']: p['sha256'] for p in previous.get('packages', [])}
        if args.check or previous.get('state') != 'local-candidate-not-published':
            raise SystemExit(f'FAIL archives outside current inventory: {sorted(extra)}')
        # Remove only unchanged archives produced by the previous local build.
        for rel in extra:
            if rel not in known or sha((destination / rel).read_bytes()) != known[rel]:
                raise SystemExit(f'FAIL unrecognized or modified archive: {rel}')
        for rel in extra:
            (destination / rel).unlink()
    for rel, data in files.items():
        p = destination / rel
        if args.check:
            if not p.is_file() or p.read_bytes() != data:
                raise SystemExit(f'FAIL stale or missing: {p}')
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
    print(f'PASS {"checked" if args.check else "built"}: {len([p for p in files if p.endswith(".zip")])} archives; integrity, exact source parity and deterministic bytes; {destination}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
