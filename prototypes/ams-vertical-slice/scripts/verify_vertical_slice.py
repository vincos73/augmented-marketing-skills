#!/usr/bin/env python3
"""Verify generated AMS Vertical Slice bundles without installing them."""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
DIST = ROOT / "dist"
VERSION = "0.1.2"
PLUGIN_NAME = "ams-vertical-slice"
ROUTER_NAME = "ams-vertical-router"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def specialists() -> list[dict[str, str]]:
    return json.loads((SOURCE / "specialists.json").read_text(encoding="utf-8"))


def target_skill_name(name: str, target: str) -> str:
    return f"ams-vs-{name}" if target == "openai" and name != ROUTER_NAME else name


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, "missing YAML frontmatter")
    return match.group(1)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_tree(target: str, items: list[dict[str, str]]) -> None:
    root = DIST / target / PLUGIN_NAME
    manifest_dir = ".codex-plugin" if target == "openai" else ".claude-plugin"
    manifest_path = root / manifest_dir / "plugin.json"
    require(manifest_path.is_file(), f"missing {target} manifest")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    require(manifest["name"] == PLUGIN_NAME, f"wrong {target} plugin name")
    require(manifest["version"] == VERSION, f"wrong {target} version")

    router = root / "skills" / ROUTER_NAME
    router_text = (router / "SKILL.md").read_text(encoding="utf-8")
    router_fm = frontmatter(router_text)
    require(f"name: {ROUTER_NAME}" in router_fm, f"wrong {target} router name")
    require("non sostituirli con sinonimi" in router_text, f"missing canonical state enum contract in {target}")
    require("Non esporre mai all'utente" in router_text, f"missing marketer-language contract in {target}")
    for playbook in sorted((SOURCE / "playbooks").glob("*.md")):
        copied = router / "references" / playbook.name
        require(copied.is_file(), f"missing router playbook {target}/{playbook.name}")
        require(digest(copied) == digest(playbook), f"router playbook drift {target}/{playbook.name}")

    if target == "openai":
        router_adapter = (router / "agents" / "openai.yaml").read_text(encoding="utf-8")
        require("allow_implicit_invocation: false" not in router_adapter, "OpenAI router must remain automatic")
    else:
        require("disable-model-invocation" not in router_fm, "Claude router must remain automatic")
        require(not (router / "agents").exists(), "Claude router leaked OpenAI adapter")

    commands = (router / "references" / "manual-commands.md").read_text(encoding="utf-8")
    for item in items:
        output_name = target_skill_name(item["name"], target)
        skill = root / "skills" / output_name
        skill_text = (skill / "SKILL.md").read_text(encoding="utf-8")
        fm = frontmatter(skill_text)
        require(f"name: {output_name}" in fm, f"wrong adapted name for {target}/{item['name']}")
        require(f"SLICE_SPECIALIST: {item['name']}" in skill_text, f"missing specialist marker {target}/{item['name']}")
        require(f"SLICE_PLAYBOOK: {item['stage']}" in skill_text, f"missing playbook emission contract {target}/{item['name']}")
        playbook = skill / "references" / "playbook.md"
        source_playbook = SOURCE / "playbooks" / f"{item['stage']}.md"
        require(digest(playbook) == digest(source_playbook), f"specialist playbook drift {target}/{item['name']}")
        require(not list((skill / "references").rglob("SKILL.md")), "nested SKILL.md leaked into references")
        if target == "claude":
            require("disable-model-invocation: true" in fm, f"Claude specialist is not manual-only: {item['name']}")
            require(f"/{PLUGIN_NAME}:{item['name']}" in commands, f"Claude command missing namespace: {item['name']}")
            require(not (skill / "agents").exists(), f"Claude specialist leaked OpenAI adapter: {item['name']}")
        else:
            adapter = (skill / "agents" / "openai.yaml").read_text(encoding="utf-8")
            require("allow_implicit_invocation: false" in adapter, f"OpenAI specialist is not manual-only: {item['name']}")
            require(f"${output_name}" in commands, f"OpenAI command missing prefix: {item['name']}")

    require(len(list((root / "skills").glob("*/SKILL.md"))) == 1 + len(items), f"wrong skill count in {target}")


def verify_archive(target: str) -> None:
    archive = DIST / f"{PLUGIN_NAME}-{target}-v{VERSION}.zip"
    require(archive.is_file(), f"missing {target} archive")
    expected = ".codex-plugin/plugin.json" if target == "openai" else ".claude-plugin/plugin.json"
    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()
        require(expected in names, f"{target} archive has wrong root")
        require(all(not name.startswith(f"{PLUGIN_NAME}/") for name in names), f"{target} archive has extra root")
        require(zf.testzip() is None, f"{target} archive is corrupt")


def main() -> None:
    require(ROOT.name == "ams-vertical-slice", "verification must run inside isolated prototype")
    items = specialists()
    require(len(items) == 8, "expected eight manual specialists")
    require({item["stage"] for item in items} == {p.stem for p in (SOURCE / "playbooks").glob("*.md")}, "stage/playbook mismatch")
    for target in ("openai", "claude"):
        verify_tree(target, items)
        verify_archive(target)
    report = json.loads((DIST / "build-report.json").read_text(encoding="utf-8"))
    require(report["version"] == VERSION, "build report has wrong version")
    require(report["skills"] == 9, "build report has wrong skill count")
    require(len(report["archives"]) == 2, "build report must contain two archives")
    print("PASS: nine skills, playbook parity, adapter isolation, manifests, archive roots and ZIP integrity")


if __name__ == "__main__":
    main()
