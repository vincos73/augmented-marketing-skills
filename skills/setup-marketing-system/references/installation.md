# Install approved Marketing Foundations

Read this reference when preparing or applying a requested installation for the selected host. Configure only approved Marketing Foundations.

## Shared safeguards

Before proposing a change:

1. Inspect applicable root-level `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`, `.claude/CLAUDE.md`, and `CLAUDE.local.md` files read-only.
2. Identify existing business-identity or marketing-foundations instructions and imports. Update compatible guidance instead of adding duplicates or competing blocks.
3. Preserve all unrelated instructions. Never replace a whole instruction file to install the profile.
4. Show the exact proposed diff and explain which identity, foundations, and conditional brand overlays it will load.
5. Explain that instruction files guide behavior but do not grant new permissions or authorize external actions.
6. Apply changes covered by the user's authorization for this host and scope. Reuse existing authorization; ask only for missing permission after preparing the concrete diff.

Use stable markers around the marketing block:

```markdown
<!-- setup-marketing-system:start -->
[managed instructions]
<!-- setup-marketing-system:end -->
```

If a matching block exists, replace only its contents. If equivalent unmarked instructions exist, adapt them carefully rather than creating a duplicate.

## Codex adapter

Prefer the applicable root `AGENTS.md`. If an `AGENTS.override.md` changes precedence at that level, explain the issue and do not edit an inactive file as if installation succeeded.

Use a concise block adapted to the real entity and paths:

```markdown
<!-- setup-marketing-system:start -->
## Contesto di marketing

Quando il compito dipende da fatti identitari, consulta le sezioni pertinenti di `[identity-path]`; per scelte o regole di marketing usa `[foundations-path]`. Applica fatti approvati, regole, aspetti aperti e limiti pertinenti. Riusa ciò che è già stato letto e resta valido; non rileggere l'intero contesto per una correzione locale che non lo coinvolge. Per un brand figlio consulta l'identità e l'integrazione pertinenti, senza caricare gli altri brand.

Quando serve alla tracciabilità della decisione, indica entità e versioni effettivamente applicate. Segnala l'indisponibilità o il conflitto di un documento quando cambia il lavoro, senza ripetere avvisi invariati.
<!-- setup-marketing-system:end -->
```

If `setup-business-context` already manages a compatible identity block, preserve it. The marketing block may reference it, but must still name the exact foundations path and brand-selection behavior.

After editing, read the saved block back from disk. Report configuration observed on disk, not runtime loading. Codex normally discovers project instructions on a new run; ask the user to start a fresh task before testing. If the host exposes loaded instruction sources, verify them read-only; otherwise do not claim they loaded.

## Claude Code adapter

Prefer an existing applicable root `CLAUDE.md`; if none exists, propose creating one. Preserve existing `.claude/CLAUDE.md`, `CLAUDE.local.md`, and `@AGENTS.md` conventions.

Prefer the same conditional references as the Codex block, using real relative paths. Preserve an existing approved direct-import setup or an explicit user request for always-loaded context; do not introduce full-profile imports by default. For a multi-brand company, read parent identity and foundations when needed for the relevant child, plus only that child's identity and marketing overlay. Do not import every brand.

After editing, read the saved references or imports and verify their target files. Explain that first-use import approval or a new session may be required. An import observed on disk is configured; it is not proof that the running session loaded or accepted it.

## Other agent hosts

Do not guess proprietary instruction filenames or claim compatibility. Explain what must be verified: the project instruction file, load scope and precedence, ability to reference the identity and foundations, conditional brand loading, and whether runtime-loaded sources can be observed.

## Finish the installation report

State:

- host and instruction file changed;
- exact identity and foundations paths referenced;
- child-brand behavior, if applicable;
- whether the saved block was read back;
- whether runtime loading was observed or remains unverified;
- that downstream actions still require their own permissions and approvals.
