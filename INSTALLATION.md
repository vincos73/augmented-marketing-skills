# Installing Augmented Marketing Suite 1.0.0

> English documentation: [README.en.md](README.en.md) · [Overview](docs/en/OVERVIEW.md) · [Examples](docs/en/EXAMPLES.md). Italian guide: [INSTALLAZIONE.md](INSTALLAZIONE.md).

This guide describes the stable public 1.0.0 distribution. The separate [1.0.1-l10n.1 source candidate](LOCALIZATION-CORE-STATUS.md) is unpublished and uninstalled; its files are not stable installation assets.

## Choose the right archive

Suite 1.0.0 contains **13 ZIP archives**:

- one Claude plugin with 12 skills, including Augmented Marketing Assistant v0.3.0;
- one OpenAI/Codex plugin with 12 skills, including Augmented Marketing Assistant v0.3.0;
- 11 portable, single-skill ZIPs, one for each specialist skill.

| Use case | Archive or directory | Contents |
| --- | --- | --- |
| Claude, complete Suite | `dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip` | Claude plugin with 12 skills, including the Assistant |
| One specialist skill | One ZIP from `dist/1.0.0/agent-skills/` | One portable specialist skill |
| ChatGPT, direct skill loading | One ZIP from `dist/1.0.0/agent-skills/`, when available | The selected portable specialist skill |
| ChatGPT or Codex, complete plugin | `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip` | OpenAI/Codex plugin with 12 skills, including the Assistant |
| Claude Project without custom skills | Extracted files as project context | A static document-based alternative, not skill installation |

Use a portable ZIP for one specialist skill and the platform plugin for the complete Suite. The two plugin archives are platform-specific. The portable ZIPs do not include the Assistant.

The public release page is [Augmented Marketing Suite v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0). It contains 15 public assets: 13 ZIPs, `manifest.json`, and `SHA256SUMS`.

## Claude plugin

If your Claude environment exposes a plugin upload flow:

1. Download `augmented-marketing-suite-claude-v1.0.0.zip` from the release page, or use the local file under `dist/1.0.0/claude/`.
2. Open the environment's plugin area and choose its plugin upload action.
3. Select the Claude archive. Its root contains `.claude-plugin/plugin.json` and the `skills/` directory.
4. Start a new chat or session and check that the skills are visible or invocable.

The Claude bundle contains 12 skills and no agents or subagents. It does not add MCP servers, connectors, or hooks. The exact labels and availability of plugin controls depend on the Claude product, plan, workspace, and current interface.

## One custom skill in Claude

If your Claude plan or workspace supports custom skills:

1. Select one ZIP from `dist/1.0.0/agent-skills/` or from the public release.
2. Use the environment's custom-skill upload flow.
3. Check the technical skill name and version shown by the environment.
4. Start a new chat and make a request that belongs clearly to that skill.

Each portable archive has one skill folder, `SKILL.md`, and the references required by that skill. Availability of custom-skill loading is platform-, plan-, and workspace-dependent. A Claude Project can hold the extracted files as instructions or project knowledge, but that is a static alternative rather than automatic custom-skill loading.

For Claude Code, the historical release used the following marketplace commands:

```sh
claude plugin marketplace add vincos73/augmented-marketing-skills
claude plugin install augmented-marketing-suite@augmented-marketing-skills
```

If you validate a local marketplace copy, use a path written as `./`; the recorded CLI limitation was that `.` was rejected by CLI 2.1.266. Validate an extracted bundle with:

```sh
claude plugin validate --strict <extracted-bundle>
```

These commands document the historical adapter; current controls can vary by account, plan, workspace, and interface.

## ChatGPT direct skill loading

If your account or workspace exposes a direct Skills flow:

1. Open the Skills flow.
2. Create or load a skill and select one portable ZIP from `dist/1.0.0/agent-skills/`.
3. Check the name and version declared in `SKILL.md`.
4. Start a new chat and test a request that matches the selected skill.

The availability of direct skill loading depends on the product, plan, and administrator. The portable format is separate from the OpenAI/Codex plugin archive.

## ChatGPT or Codex complete plugin

Use `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip` only where a compatible Plugin Creator, plugin catalogue, or marketplace flow exists. It is not a Claude archive.

1. Open a new chat or session in the target environment.
2. Load the archive through the available plugin creation or update flow.
3. Check that the archive root contains `.codex-plugin/plugin.json` and `skills/`.
4. Check that the manifest declares version `1.0.0` and the `skills` directory.
5. Install or update the plugin through the marketplace or catalogue allowed by that environment, then start a new chat or session.

An ordinary chat attachment can be read as content but does not automatically register a plugin or skill. The local 1.0.0 verification recorded 12 standalone Codex skills and a Claude Code plugin installation; it did not verify every account, current session loading, Claude.ai installation, or a new Codex plugin registration.

## Verify the archive before use

1. Compare each ZIP's SHA-256 digest with `SHA256SUMS` in the same distribution directory.
2. Extract into a temporary directory and check that each portable ZIP has one root folder, `SKILL.md`, and any expected `references/` directory.
3. For the Claude plugin, check `.claude-plugin/plugin.json`; for OpenAI/Codex, check `.codex-plugin/plugin.json` at the archive root.
4. Check the inventory: 12 skills in each complete plugin and 11 individual specialist ZIPs under `agent-skills/`.
5. Start a new chat or session and request a result that clearly belongs to the chosen skill.

The structural report records passing build, archive, checksum, and validation checks for 1.0.0. It does not demonstrate discovery or runtime behaviour in every environment.

## Version boundary

The 1.0.0 paths above refer to the published stable distribution. The 1.0.1-l10n.1 source candidate has no published installation archive and does not replace the 1.0.0 assets.
