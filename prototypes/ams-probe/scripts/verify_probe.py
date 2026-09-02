#!/usr/bin/env python3
"""Verify the generated AMS probe without installing either plugin."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = "0.0.2"
SKILLS = ("ams-router", "define-marketing-challenge", "choose-marketing-direction")
SPECIALISTS = SKILLS[1:]


def target_skill_name(skill_name: str, target: str) -> str:
    if target == "openai" and skill_name in SPECIALISTS:
        return f"ams-probe-{skill_name}"
    return skill_name


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    require(match is not None, "missing YAML frontmatter")
    return match.group(1)


def verify_tree(target: str) -> None:
    root = DIST / target / "ams-probe"
    manifest_dir = ".codex-plugin" if target == "openai" else ".claude-plugin"
    manifest_path = root / manifest_dir / "plugin.json"
    require(manifest_path.is_file(), f"missing {target} manifest")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    require(manifest["name"] == "ams-probe", f"wrong {target} plugin name")

    for skill in SKILLS:
        output_name = target_skill_name(skill, target)
        skill_path = root / "skills" / output_name / "SKILL.md"
        require(skill_path.is_file(), f"missing {target}/{skill}")
        fm = frontmatter(skill_path.read_text(encoding="utf-8"))
        require(f"name: {output_name}" in fm, f"wrong adapted name for {target}/{skill}")
        if target == "claude":
            require(not (root / "skills" / output_name / "agents").exists(), "Claude bundle leaked OpenAI adapter")
            if skill in SPECIALISTS:
                require("disable-model-invocation: true" in fm, f"Claude specialist {skill} is not manual-only")
            else:
                require("disable-model-invocation" not in fm, "Claude router must remain model-invocable")
        else:
            yaml_path = root / "skills" / output_name / "agents" / "openai.yaml"
            require(yaml_path.is_file(), f"missing OpenAI adapter for {skill}")
            policy = yaml_path.read_text(encoding="utf-8")
            if skill in SPECIALISTS:
                require("allow_implicit_invocation: false" in policy, f"OpenAI specialist {skill} is not manual-only")
            else:
                require("allow_implicit_invocation: false" not in policy, "OpenAI router must remain model-invocable")

    router_refs = root / "skills" / "ams-router" / "references"
    require((router_refs / "challenge.md").read_bytes() == (ROOT / "source" / "playbooks" / "challenge.md").read_bytes(), "challenge playbook drift")
    require((router_refs / "direction.md").read_bytes() == (ROOT / "source" / "playbooks" / "direction.md").read_bytes(), "direction playbook drift")
    manual_commands = (router_refs / "manual-commands.md").read_text(encoding="utf-8")
    if target == "claude":
        require("/ams-probe:define-marketing-challenge" in manual_commands, "Claude manual command lost plugin namespace")
        require("$ams-probe-define-marketing-challenge" not in manual_commands, "Claude bundle leaked OpenAI command syntax")
    else:
        require("$ams-probe-define-marketing-challenge" in manual_commands, "OpenAI manual command lost probe prefix")
        require("/ams-probe:define-marketing-challenge" not in manual_commands, "OpenAI bundle leaked Claude command syntax")
    require(not list(router_refs.rglob("SKILL.md")), "nested SKILL.md leaked into router references")


def verify_archive(target: str) -> None:
    archive = DIST / f"ams-probe-{target}-v{VERSION}.zip"
    require(archive.is_file(), f"missing {target} archive")
    expected = ".codex-plugin/plugin.json" if target == "openai" else ".claude-plugin/plugin.json"
    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()
        require(expected in names, f"{target} archive has wrong root")
        require(all(not name.startswith("ams-probe/") for name in names), f"{target} archive has an extra root folder")
        require(zf.testzip() is None, f"{target} archive is corrupt")


def main() -> None:
    require(ROOT.name == "ams-probe", "verification must run inside isolated probe")
    for target in ("openai", "claude"):
        verify_tree(target)
        verify_archive(target)
    report = json.loads((DIST / "build-report.json").read_text(encoding="utf-8"))
    require(report["version"] == VERSION, "build report has wrong probe version")
    require(len(report["archives"]) == 2, "build report must contain two archives")
    print("PASS: source parity, adapter isolation, manifests, archive roots and ZIP integrity")


if __name__ == "__main__":
    main()
