"""Regression coverage for the local suite archive builder."""
from __future__ import annotations

from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "build_suite.py"
SPEC = importlib.util.spec_from_file_location("build_suite_under_test", SCRIPT_PATH)
assert SPEC and SPEC.loader
BUILD_SUITE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILD_SUITE)


class BuildSuiteTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name) / "suite"
        self.destination = self.root / "dist" / "candidate"
        self._create_source_repository()
        self._run("--output", str(self.destination))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _git(self, *args: str) -> None:
        subprocess.run(
            ["git", *args], cwd=self.root, check=True, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )

    def _commit(self, message: str) -> None:
        self._git(
            "-c", "user.name=Build Suite Test",
            "-c", "user.email=build-suite@example.invalid",
            "commit", "-qm", message,
        )

    def _create_source_repository(self) -> None:
        (self.root / ".codex-plugin").mkdir(parents=True)
        (self.root / "claude" / ".claude-plugin").mkdir(parents=True)
        manifest = {"name": "augmented-marketing-suite", "version": "0.3.0"}
        (self.root / ".codex-plugin" / "plugin.json").write_text(json.dumps(manifest))
        (self.root / "claude" / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest))
        for name in BUILD_SUITE.NAMES:
            skill = self.root / "skills" / name
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: " + name + "\nmetadata:\n  version: \"0.3.0\"\n---\n"
            )
            (skill / "agents" / "openai.yaml").write_text("interface: test\n")
        self._git("init", "-q")
        self._git("add", ".")
        self._commit("source fixture")

    def _run(self, *arguments: str) -> int:
        output = io.StringIO()
        with patch.object(BUILD_SUITE, "ROOT", self.root), patch.object(
            sys, "argv", [str(SCRIPT_PATH), *arguments]
        ), redirect_stdout(output):
            return BUILD_SUITE.main()

    def _assert_check_fails(self) -> None:
        with self.assertRaisesRegex(SystemExit, r"FAIL"):
            self._run("--check", "--output", str(self.destination))

    def test_build_inventory_contains_assistant_on_both_platforms(self) -> None:
        manifest = json.loads((self.destination / "manifest.json").read_text())
        archives = sorted(self.destination.rglob("*.zip"))
        self.assertEqual(13, len(archives))
        self.assertEqual(13, len(manifest["packages"]))

        openai, claude = manifest["packages"][:2]
        assistant = "augmented-marketing-assistant"
        self.assertEqual("0.3.0", openai["skills"][assistant])
        self.assertEqual("0.3.0", claude["skills"][assistant])
        self.assertEqual(set(BUILD_SUITE.NAMES), set(openai["skills"]))
        self.assertEqual(set(BUILD_SUITE.NAMES), set(claude["skills"]))

        with zipfile.ZipFile(self.destination / openai["archive"]) as archive:
            names = set(archive.namelist())
        self.assertIn(f"skills/{assistant}/SKILL.md", names)
        self.assertIn(f"skills/{assistant}/agents/openai.yaml", names)

        with zipfile.ZipFile(self.destination / claude["archive"]) as archive:
            names = set(archive.namelist())
        self.assertIn(f"skills/{assistant}/SKILL.md", names)
        self.assertFalse(any("/agents/" in name for name in names))

        portable = manifest["packages"][2:]
        self.assertEqual(11, len(portable))
        self.assertEqual(set(BUILD_SUITE.NAMES[1:]), {next(iter(item["skills"])) for item in portable})

    def test_stable_version_uses_unsuffixed_default_path_and_built_state(self) -> None:
        self.assertEqual(0, self._run())
        stable_destination = self.root / "dist" / "0.3.0"
        manifest = json.loads((stable_destination / "manifest.json").read_text())
        self.assertEqual("built", manifest["state"])
        self.assertTrue((stable_destination / "openai" / "augmented-marketing-suite-0.3.0.zip").is_file())

    def test_check_allows_publication_and_unrelated_commits(self) -> None:
        self._git("add", "dist/candidate")
        self._commit("publish local candidate")
        (self.root / "publication-notes.md").write_text("The archive was reviewed locally.\n")
        self._git("add", "publication-notes.md")
        self._commit("add unrelated publication note")

        self.assertEqual(0, self._run("--check", "--output", str(self.destination)))

    def test_check_fails_after_source_change(self) -> None:
        skill = self.root / "skills" / BUILD_SUITE.NAMES[1] / "SKILL.md"
        skill.write_text(skill.read_text() + "Changed after the build.\n")
        self._assert_check_fails()

    def test_check_fails_when_archive_is_missing(self) -> None:
        (self.destination / "openai" / "augmented-marketing-suite-0.3.0.zip").unlink()
        self._assert_check_fails()

    def test_check_fails_when_archive_is_modified(self) -> None:
        archive = self.destination / "openai" / "augmented-marketing-suite-0.3.0.zip"
        archive.write_bytes(archive.read_bytes() + b"tampered")
        self._assert_check_fails()

    def test_check_fails_when_extra_archive_exists(self) -> None:
        extra = self.destination / "agent-skills" / "unrecognized-0.0.0.zip"
        extra.write_bytes(b"not a suite archive")
        self._assert_check_fails()

    def test_check_fails_when_manifest_state_changes(self) -> None:
        manifest_path = self.destination / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["state"] = "published"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        self._assert_check_fails()

    def test_check_fails_when_manifest_source_hash_changes(self) -> None:
        manifest_path = self.destination / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        source_path = next(iter(manifest["source_sha256"]))
        manifest["source_sha256"][source_path] = "0" * 64
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        self._assert_check_fails()

    def test_check_fails_when_manifest_package_hash_changes(self) -> None:
        manifest_path = self.destination / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["packages"][0]["sha256"] = "0" * 64
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        self._assert_check_fails()

    def test_check_fails_when_checksums_change(self) -> None:
        sums = self.destination / "SHA256SUMS"
        sums.write_text("0" * 64 + "  manifest.json\n")
        self._assert_check_fails()


if __name__ == "__main__":
    unittest.main()
