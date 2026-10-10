#!/usr/bin/env python3
"""Verify the exact OpenAI 1.0.2 archive against the tracked release source."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / 'releases/1.0.2/openai'
ARCHIVE = RELEASE / 'augmented-marketing-suite-public-1.0.2.zip'
SOURCE = RELEASE / 'source'
EXPECTED_SHA = '8e68e50f92a8aca57786cbf27cf7e3281672a224607d095232fe4d3f75c07da5'


def main():
    actual_sha = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    assert actual_sha == EXPECTED_SHA, f'ZIP SHA-256 mismatch: {actual_sha}'
    files = {str(p.relative_to(SOURCE)): p.read_bytes() for p in SOURCE.rglob('*') if p.is_file()}
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None, 'Corrupt ZIP member'
        names = set(archive.namelist())
        assert names == set(files), f'ZIP/source inventory mismatch: {names ^ set(files)}'
        assert all(archive.read(name) == data for name, data in files.items()), 'ZIP/source byte mismatch'
    assert len(files) == 58, f'Unexpected file count: {len(files)}'
    assert len([name for name in files if name.startswith('skills/') and name.endswith('/SKILL.md')]) == 12
    for name in ('plugin.json', '.codex-plugin/plugin.json'):
        manifest = json.loads(files[name])
        assert manifest['name'] == 'augmented-marketing-suite'
        assert manifest['version'] == '1.0.2'
    assert files['assets/ams-logo-512.png'].startswith(b'\x89PNG\r\n\x1a\n')
    assert files['assets/ams-icon-64.png'].startswith(b'\x89PNG\r\n\x1a\n')
    print('PASS: SHA-256, 58/58 source files, 12 skills, manifests and PNG headers')


if __name__ == '__main__':
    main()
