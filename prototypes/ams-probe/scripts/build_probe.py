#!/usr/bin/env python3
"""Build isolated Claude and OpenAI AMS probe bundles from one neutral source."""

from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
DIST = ROOT / "dist"
VERSION = "0.0.2"
PLUGIN_NAME = "ams-probe"
SPECIALISTS = ("define-marketing-challenge", "choose-marketing-direction")

MANUAL_COMMANDS = {
    "claude": """# Comandi manuali AMS Probe — Claude

Usa sempre il namespace completo del plugin:

- `/ams-probe:define-marketing-challenge`
- `/ams-probe:choose-marketing-direction`
""",
    "openai": """# Comandi manuali AMS Probe — Codex

Usa sempre il nome completo adattato del probe:

- `$ams-probe-define-marketing-challenge`
- `$ams-probe-choose-marketing-direction`
""",
}


def target_skill_name(skill_name: str, target: str) -> str:
    if target == "openai" and skill_name in SPECIALISTS:
        return f"ams-probe-{skill_name}"
    return skill_name


def replace_frontmatter(text: str, additions: list[str]) -> str:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md has no closing frontmatter marker")
    head = text[4:end].rstrip()
    body = text[end + 5 :]
    return "---\n" + head + "\n" + "\n".join(additions) + "\n---\n" + body


def copy_skill(target_root: Path, skill_name: str, target: str) -> None:
    source_skill = SOURCE / "skills" / skill_name / "SKILL.md"
    output_name = target_skill_name(skill_name, target)
    target_skill = target_root / "skills" / output_name
    target_skill.mkdir(parents=True, exist_ok=True)
    text = source_skill.read_text(encoding="utf-8")

    if output_name != skill_name:
        source_name = f"name: {skill_name}\n"
        target_name = f"name: {output_name}\n"
        if source_name not in text:
            raise ValueError(f"Cannot adapt skill name in {source_skill}")
        text = text.replace(source_name, target_name, 1)

    if target == "claude" and skill_name in SPECIALISTS:
        text = replace_frontmatter(
            text,
            [
                "disable-model-invocation: true",
                'argument-hint: "[brief o richiesta di marketing]"',
            ],
        )

    (target_skill / "SKILL.md").write_text(text, encoding="utf-8")

    references = target_skill / "references"
    references.mkdir(exist_ok=True)
    if skill_name == "ams-router":
        shutil.copy2(SOURCE / "playbooks" / "challenge.md", references / "challenge.md")
        shutil.copy2(SOURCE / "playbooks" / "direction.md", references / "direction.md")
        (references / "manual-commands.md").write_text(MANUAL_COMMANDS[target], encoding="utf-8")
    elif skill_name == "define-marketing-challenge":
        shutil.copy2(SOURCE / "playbooks" / "challenge.md", references / "playbook.md")
    elif skill_name == "choose-marketing-direction":
        shutil.copy2(SOURCE / "playbooks" / "direction.md", references / "playbook.md")

    if target == "openai":
        agents = target_skill / "agents"
        agents.mkdir(exist_ok=True)
        display = {
            "ams-router": ("AMS Router Probe", "Instrada un test marketing isolato"),
            "define-marketing-challenge": ("Define Challenge Probe", "Specialista manuale per chiarire la sfida"),
            "choose-marketing-direction": ("Choose Direction Probe", "Specialista manuale per confrontare direzioni"),
        }[skill_name]
        lines = [
            "interface:",
            f'  display_name: "{display[0]}"',
            f'  short_description: "{display[1]}"',
            f'  default_prompt: "Use ${output_name} to run the isolated AMS probe."',
        ]
        if skill_name in SPECIALISTS:
            lines.extend(["policy:", "  allow_implicit_invocation: false"])
        (agents / "openai.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_openai() -> Path:
    root = DIST / "openai" / PLUGIN_NAME
    (root / ".codex-plugin").mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": PLUGIN_NAME,
        "version": VERSION,
        "description": "Probe isolato per verificare router automatico e specialisti manuali su Codex.",
        "author": {"name": "Augmented Marketing Suite"},
        "keywords": ["marketing", "skills", "probe", "portability"],
        "skills": "./skills/",
        "interface": {
            "displayName": "AMS Probe",
            "shortDescription": "Test isolato della portabilità delle skill",
            "longDescription": "Verifica un router conversazionale e due specialisti manuali senza modificare Augmented Marketing Suite.",
            "developerName": "Augmented Marketing Suite",
            "category": "Productivity",
            "capabilities": ["Read"],
            "defaultPrompt": [
                "Ho un obiettivo di marketing ma non so da quale problema partire.",
                "Confronta possibili direzioni per una sfida già confermata.",
            ],
        },
    }
    (root / ".codex-plugin" / "plugin.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    for skill in ("ams-router", *SPECIALISTS):
        copy_skill(root, skill, "openai")
    return root


def build_claude() -> Path:
    root = DIST / "claude" / PLUGIN_NAME
    (root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    manifest = {
        "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
        "name": PLUGIN_NAME,
        "displayName": "AMS Probe",
        "version": VERSION,
        "description": "Probe isolato per verificare router automatico e specialisti manuali su Claude Code.",
        "author": {"name": "Augmented Marketing Suite"},
        "keywords": ["marketing", "skills", "probe", "portability"],
    }
    (root / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    for skill in ("ams-router", *SPECIALISTS):
        copy_skill(root, skill, "claude")
    return root


def zip_bundle(root: Path, target: str) -> Path:
    archive = DIST / f"{PLUGIN_NAME}-{target}-v{VERSION}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            info = zipfile.ZipInfo(path.relative_to(root).as_posix(), date_time=(2026, 8, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())
    return archive


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if ROOT.name != "ams-probe" or ROOT.parent.name != "prototypes":
        raise RuntimeError(f"Refusing to build outside isolated probe: {ROOT}")
    DIST.mkdir(exist_ok=True)
    for generated_tree in (DIST / "openai", DIST / "claude"):
        if generated_tree.exists():
            shutil.rmtree(generated_tree)
    for current_archive in DIST.glob(f"{PLUGIN_NAME}-*-v{VERSION}.zip"):
        current_archive.unlink()

    openai_root = build_openai()
    claude_root = build_claude()
    archives = [zip_bundle(openai_root, "openai"), zip_bundle(claude_root, "claude")]
    report = {
        "probe": PLUGIN_NAME,
        "version": VERSION,
        "source": "source/",
        "generated_targets": ["openai", "claude"],
        "archives": [
            {"file": archive.name, "sha256": sha256(archive), "bytes": archive.stat().st_size}
            for archive in archives
        ],
    }
    (DIST / "build-report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
