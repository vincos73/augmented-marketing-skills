#!/usr/bin/env python3
"""Build isolated Claude and OpenAI AMS Vertical Slice bundles from one source."""

from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
DIST = ROOT / "dist"
VERSION = "0.1.2"
PLUGIN_NAME = "ams-vertical-slice"
ROUTER_NAME = "ams-vertical-router"


def load_specialists() -> list[dict[str, str]]:
    return json.loads((SOURCE / "specialists.json").read_text(encoding="utf-8"))


def target_skill_name(skill_name: str, target: str) -> str:
    if target == "openai" and skill_name != ROUTER_NAME:
        return f"ams-vs-{skill_name}"
    return skill_name


def manual_commands(target: str, specialists: list[dict[str, str]]) -> str:
    if target == "claude":
        commands = [f"- `/{PLUGIN_NAME}:{item['name']}`" for item in specialists]
        heading = "# Comandi manuali AMS Vertical Slice - Claude"
        lead = "Usa sempre il namespace completo del plugin:"
    else:
        commands = [f"- `${target_skill_name(item['name'], target)}`" for item in specialists]
        heading = "# Comandi manuali AMS Vertical Slice - Codex"
        lead = "Usa sempre il nome completo adattato del prototipo:"
    return "\n\n".join((heading, lead, "\n".join(commands))) + "\n"


def write_openai_adapter(skill_root: Path, output_name: str, title: str, summary: str, manual: bool) -> None:
    agents = skill_root / "agents"
    agents.mkdir(exist_ok=True)
    lines = [
        "interface:",
        f'  display_name: "{title}"',
        f'  short_description: "{summary}"',
        f'  default_prompt: "Use ${output_name} for the isolated AMS Vertical Slice test."',
    ]
    if manual:
        lines.extend(("policy:", "  allow_implicit_invocation: false"))
    (agents / "openai.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def copy_router(target_root: Path, target: str, specialists: list[dict[str, str]]) -> None:
    skill_root = target_root / "skills" / ROUTER_NAME
    references = skill_root / "references"
    references.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE / "skills" / ROUTER_NAME / "SKILL.md", skill_root / "SKILL.md")
    for playbook in sorted((SOURCE / "playbooks").glob("*.md")):
        shutil.copy2(playbook, references / playbook.name)
    (references / "manual-commands.md").write_text(
        manual_commands(target, specialists), encoding="utf-8"
    )
    if target == "openai":
        write_openai_adapter(
            skill_root,
            ROUTER_NAME,
            "AMS Vertical Slice",
            "Percorso marketing completo e verificabile",
            manual=False,
        )


def specialist_markdown(item: dict[str, str], target: str) -> str:
    name = target_skill_name(item["name"], target)
    extra = ""
    if target == "claude":
        extra = "disable-model-invocation: true\nargument-hint: \"[materiali e decisione della fase]\"\n"
    return f"""---
name: {name}
description: \"{item['description']}\"
metadata:
  version: \"{VERSION}\"
  status: \"isolated-vertical-slice\"
{extra}---

# {item['name']}

Questo plugin e un test isolato. Non modificare la suite esistente, non scrivere in percorsi
canonici e non eseguire pubblicazioni, invii, contatti, spesa o configurazioni.

Emetti `SLICE_SPECIALIST: {item['name']}`, poi leggi integralmente
[il playbook condiviso](references/playbook.md), emetti nel testo finale anche il suo marker
letterale `SLICE_PLAYBOOK: {item['stage']}` e applica soltanto la fase `{item['stage']}`.

Non invocare altre skill e non continuare automaticamente nella fase successiva. Una proposta
del modello non diventa confermata senza una decisione esplicita dell'utente. Parla come un
marketer o un manager e tieni interni termini tecnici di orchestrazione.
"""


def copy_specialist(target_root: Path, target: str, item: dict[str, str]) -> None:
    output_name = target_skill_name(item["name"], target)
    skill_root = target_root / "skills" / output_name
    references = skill_root / "references"
    references.mkdir(parents=True, exist_ok=True)
    (skill_root / "SKILL.md").write_text(specialist_markdown(item, target), encoding="utf-8")
    shutil.copy2(SOURCE / "playbooks" / f"{item['stage']}.md", references / "playbook.md")
    if target == "openai":
        write_openai_adapter(
            skill_root,
            output_name,
            item["name"].replace("-", " ").title(),
            f"Specialista manuale: fase {item['stage']}",
            manual=True,
        )


def manifest(target: str) -> dict[str, object]:
    common: dict[str, object] = {
        "name": PLUGIN_NAME,
        "version": VERSION,
        "description": "Vertical Slice isolata dal contesto ai risultati con router automatico e specialisti manuali.",
        "author": {"name": "Augmented Marketing Suite"},
        "keywords": ["marketing", "skills", "vertical-slice", "portability"],
    }
    if target == "claude":
        return {
            "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
            "displayName": "AMS Vertical Slice",
            **common,
        }
    return {
        **common,
        "skills": "./skills/",
        "interface": {
            "displayName": "AMS Vertical Slice",
            "shortDescription": "Test completo di un flusso marketing",
            "longDescription": "Verifica il passaggio da fonti e decisioni a campagna, asset, review e apprendimento senza modificare la suite esistente.",
            "developerName": "Augmented Marketing Suite",
            "category": "Productivity",
            "capabilities": ["Read"],
            "defaultPrompt": [
                "Trasforma questi materiali in una Vertical Slice marketing verificabile.",
                "Continua il percorso dalla fase confermata senza ripetere le decisioni.",
            ],
        },
    }


def build_target(target: str, specialists: list[dict[str, str]]) -> Path:
    root = DIST / target / PLUGIN_NAME
    manifest_dir = ".codex-plugin" if target == "openai" else ".claude-plugin"
    (root / manifest_dir).mkdir(parents=True, exist_ok=True)
    (root / manifest_dir / "plugin.json").write_text(
        json.dumps(manifest(target), indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    copy_router(root, target, specialists)
    for item in specialists:
        copy_specialist(root, target, item)
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
    if ROOT.name != "ams-vertical-slice" or ROOT.parent.name != "prototypes":
        raise RuntimeError(f"Refusing to build outside isolated prototype: {ROOT}")
    specialists = load_specialists()
    DIST.mkdir(exist_ok=True)
    for generated_tree in (DIST / "openai", DIST / "claude"):
        if generated_tree.exists():
            shutil.rmtree(generated_tree)
    for current_archive in DIST.glob(f"{PLUGIN_NAME}-*-v{VERSION}.zip"):
        current_archive.unlink()

    roots = {target: build_target(target, specialists) for target in ("openai", "claude")}
    archives = [zip_bundle(roots[target], target) for target in ("openai", "claude")]
    report = {
        "prototype": PLUGIN_NAME,
        "version": VERSION,
        "source": "source/",
        "generated_targets": ["openai", "claude"],
        "skills": 1 + len(specialists),
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
