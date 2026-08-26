# Install approved Marketing Foundations

Read this reference only after approval gate 1 has produced a canonical Marketing Foundations artifact and the user has selected an agent host.

## Shared safeguards

Before proposing a change:

1. Inspect applicable root-level `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`, `.claude/CLAUDE.md`, and `CLAUDE.local.md` files read-only.
2. Identify existing business-identity or marketing-foundations instructions and imports. Update compatible guidance instead of adding duplicates or competing blocks.
3. Preserve all unrelated instructions. Never replace a whole instruction file to install the profile.
4. Show the exact proposed diff and explain which identity, foundations, and conditional brand overlays it will load.
5. Explain that instruction files guide behavior but do not grant new permissions or authorize external actions.
6. Apply only the host changes explicitly approved.

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

Prima di svolgere attività di marketing per [Entità], leggi `[identity-path]` e `[foundations-path]` e applicane fatti approvati, regole, aspetti aperti e limiti di approvazione. Per un brand figlio, leggi anche l'identità e l'integrazione di marketing corrispondenti; non caricare brand non pertinenti.

All'inizio di ogni risposta sostanziale che svolge o fa avanzare attività di marketing per l'entità, aggiungi una breve nota operativa con entità e versioni effettivamente lette. Se un artefatto necessario non è disponibile, approvato, coerente o aggiornato, mostra un avviso operativo invece di dichiarare di averlo applicato.
<!-- setup-marketing-system:end -->
```

If `setup-business-context` already manages a compatible identity block, preserve it. The marketing block may reference it, but must still name the exact foundations path and brand-selection behavior.

After editing, read the saved block back from disk. Report configuration observed on disk, not runtime loading. Codex normally discovers project instructions on a new run; ask the user to start a fresh task before testing. If the host exposes loaded instruction sources, verify them read-only; otherwise do not claim they loaded.

## Claude Code adapter

Prefer an existing applicable root `CLAUDE.md`; if none exists, propose creating one. Preserve existing `.claude/CLAUDE.md`, `CLAUDE.local.md`, and `@AGENTS.md` conventions.

For a company or standalone brand, propose direct imports when compatible:

```markdown
<!-- setup-marketing-system:start -->
@[identity-path]
@[foundations-path]

Per ogni risposta sostanziale di marketing relativa all'entità, indica in una breve nota operativa quali entità e versioni degli artefatti sono state effettivamente applicate. Non trattare questi import come autorizzazione all'esecuzione.
<!-- setup-marketing-system:end -->
```

Replace placeholders with real relative paths. For a multi-brand company, import the parent identity and company foundations, then add a concise instruction to read only the relevant child identity and `.agents/marketing/brands/<brand-slug>.md` overlay. Do not import every brand by default.

After editing, read the imports and referenced files back from disk. Explain that first-use import approval or a new session may be required. An import observed on disk is configured; it is not proof that the running session loaded or accepted it.

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
