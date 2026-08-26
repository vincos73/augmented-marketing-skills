# Install approved Marketing Foundations

Read this reference only after approval gate 1 has produced a canonical Marketing Foundations artifact and the user has selected an agent host.

## Explain the handoff conversationally

Make the handoff feel like a practical next step, not a technical escalation. First acknowledge that the foundations are approved, then explain what installation will change and what it will not change:

> Le tue Marketing Foundations sono approvate e pronte per essere riutilizzate. Il prossimo passaggio è facoltativo: posso aggiungere alle istruzioni del progetto un piccolo blocco gestito, così le attività di marketing future leggeranno automaticamente l'identità e le foundations approvate. Questo guiderà il contesto dell'agente; non gli darà il permesso di pubblicare, spendere o modificare sistemi esterni. Ti mostrerò la modifica esatta prima di salvarla.

After the user approves, explain what was saved and what remains unverified. If runtime loading cannot be observed, say so plainly and give the user the smallest next step, such as starting a fresh task. Do not describe a configured file as proof that the current conversation has already loaded it.

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
## Marketing context

Prima di svolgere attività di marketing specifiche per [Entità], leggi `[identity-path]` e `[foundations-path]` e applica i fatti, le regole, gli aspetti ancora aperti e i confini di approvazione approvati. Per il lavoro su un brand figlio, leggi anche la relativa identità e l'overlay marketing; non caricare brand non pertinenti.

All'inizio di ogni risposta sostanziale che svolge o fa avanzare un'attività di marketing specifica per l'azienda, aggiungi un FYI compatto con l'entità e le versioni effettivamente lette. Se un artefatto necessario non è disponibile, non è approvato, è in conflitto o è materialmente obsoleto, mostra un avviso operativo invece di dichiarare che è stato applicato.
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

Per ogni risposta sostanziale di marketing specifica per l'azienda, indica in un FYI compatto quali entità e versioni degli artefatti sono state effettivamente applicate. Non considerare questi import come un'autorizzazione all'esecuzione.
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
