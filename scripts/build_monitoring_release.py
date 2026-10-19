#!/usr/bin/env python3
"""Build/check the standalone Markdown monitoring skills, without running them."""
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
RELEASE = ROOT / 'releases/activate-monitoring/0.1.0'
SOURCE = RELEASE / 'source'
VERSIONS = {'activate-monitoring': '0.1.0', 'setup-monitoring': '0.1.2'}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(data: object) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode()


def archive(files: dict[str, bytes]) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 19, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    data = stream.getvalue()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        if z.testzip() or set(z.namelist()) != set(files):
            raise ValueError('Invalid ZIP contents or CRC')
        if any(z.read(name) != content for name, content in files.items()):
            raise ValueError('ZIP/source mismatch')
    return data


def build(base_commit: str) -> dict[str, bytes]:
    output, sources, packages = {}, {}, []
    for name, version in VERSIONS.items():
        folder = SOURCE / name
        files = {}
        for path in sorted(folder.rglob('*')):
            if path.is_symlink():
                raise ValueError(f'Symlink not permitted: {path}')
            if not path.is_file():
                continue
            rel = path.relative_to(folder)
            if any(part.startswith('.') or part == '__pycache__' for part in rel.parts):
                raise ValueError(f'Unexpected hidden/generated source: {path}')
            if path.suffix not in {'.md', '.yaml'}:
                raise ValueError(f'Unexpected non-document resource: {path}')
            data = path.read_bytes()
            data.decode('utf-8')
            files[f'{name}/{rel.as_posix()}'] = data
            sources[str(path.relative_to(ROOT))] = sha(data)
        entry = files[f'{name}/SKILL.md'].decode()
        if not entry.startswith('---\n') or not re.search(rf'(?m)^name: {re.escape(name)}$', entry):
            raise ValueError(f'Invalid skill identity: {name}')
        if f'version: "{version}"' not in entry:
            raise ValueError(f'Invalid skill version: {name}')
        filename = f'{name}-{version}.zip'
        output[filename] = archive(files)
        packages.append({'file': filename, 'sha256': sha(output[filename]), 'skill': name,
                         'version': version, 'file_count': len(files)})
    output['manifest.json'] = encoded({
        'release_tag': 'activate-monitoring-v0.1.0',
        'distribution': 'standalone Italian skills; existing Suite bundles unchanged',
        'source_base_commit': base_commit,
        'source_state': 'source_sha256 identifies exact packaged content',
        'source_sha256': sources, 'packages': packages,
        'requires_database': False, 'requires_binaries': False,
        'required_agent_count': 1,
        'requirements': ['skill loading', 'authorized search/read tools',
                         'authorized persistent file access for automatic history',
                         'host scheduling capability for recurring execution'],
        'verification_scope': 'structure, source parity and archive integrity only; no new behavioral or web comparisons',
        'desktop_integration_verified': False,
    })
    output['SHA256SUMS'] = ''.join(f'{sha(data)}  {name}\n'
                                  for name, data in sorted(output.items())).encode()
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Read-only source/package verification')
    args = parser.parse_args()
    manifest = RELEASE / 'manifest.json'
    if args.check:
        base = json.loads(manifest.read_text())['source_base_commit']
    else:
        base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    files = build(base)
    for name, data in files.items():
        path = RELEASE / name
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                raise SystemExit(f'Stale or missing release file: {path}')
        else:
            if path.exists() and path.read_bytes() != data:
                raise SystemExit(f'Refusing to replace existing release bytes: {path}')
            path.write_bytes(data)
    extra = {p.name for p in RELEASE.glob('*.zip')} - files.keys()
    if extra:
        raise SystemExit(f'Unexpected archives: {sorted(extra)}')
    print(json.dumps({'check_only': args.check, 'pass': True, 'packages': list(VERSIONS),
                      'source_files': len(json.loads(files['manifest.json'])['source_sha256']),
                      'behavioral_tests_run': False, 'web_comparisons_run': False}))


if __name__ == '__main__':
    main()
