# Install the approved business identity

Read this reference only after the identity has passed approval gate 1 and the user has chosen an agent host.

## Shared safeguards

Before proposing a change:

1. Inspect existing root-level `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`, `.claude/CLAUDE.md`, and `CLAUDE.local.md` files that are relevant to the selected host.
2. Identify any existing business-context instruction or import. Update it instead of adding a duplicate.
3. Preserve all unrelated content. Never replace an entire instruction file to install this context.
4. Show the exact proposed addition or diff and explain that instruction files guide agent behavior; they do not grant new permissions or authorize external actions.
5. Apply only the host changes the user explicitly approved.

Use stable comments around an inserted block so later updates can target it safely:

```markdown
<!-- setup-business-context:start -->
[managed instructions]
<!-- setup-business-context:end -->
```

If an existing block with these markers is present, replace only its contents. If semantically equivalent instructions exist without markers, adapt them carefully rather than creating competing rules.

## Codex adapter

Codex reads project `AGENTS.md` guidance before working. Prefer the root `AGENTS.md` that applies to the workspace. If an `AGENTS.override.md` is active at that level, explain the precedence issue and do not edit the inactive file as if installation succeeded.

Use a concise block such as:

```markdown
<!-- setup-business-context:start -->
## Business identity

Before doing work for or about [Entity], read `[identity-path]` and apply its approved facts, terminology, and guardrails. Do not treat its known unknowns as facts. For work about a child brand, also read the matching file under `.agents/brands/`.
<!-- setup-business-context:end -->
```

Keep the canonical identity in its own file. Do not duplicate the full document inside `AGENTS.md`.

After editing, read the saved block back from disk. Report that the instruction was configured on disk, not that the current session loaded it or that every future model response is guaranteed to comply.

Codex discovers project instructions once per run. Explain that the new block is configured on disk for subsequent runs and that the user should start a new Codex task or session before testing it. If the host can report its loaded instruction sources, use that read-only check; otherwise do not claim that the current session reloaded the change.

## Claude Code adapter

Claude Code reads project `CLAUDE.md` files, not `AGENTS.md` directly. Prefer an existing root `CLAUDE.md`; if none exists, propose creating one. Preserve `.claude/CLAUDE.md` or `CLAUDE.local.md` choices already made by the project instead of silently moving them.

Claude Code supports file imports with `@path`. For a single company or standalone brand, use a direct import so the approved identity is loaded with project instructions:

```markdown
<!-- setup-business-context:start -->
@[identity-path]
<!-- setup-business-context:end -->
```

Replace `[identity-path]` with the real relative path, for example `@.agents/company-identity.md`; do not leave brackets in the installed line.

When the workspace also uses Codex, Claude's file may import the shared agent instructions as well:

```markdown
@AGENTS.md
```

Do not add this line twice. A symlink is not necessary.

For a multi-brand company, import the company identity as the always-loaded parent. Add a concise instruction to read the relevant `.agents/brands/<brand-slug>.md` file when a task concerns a child brand; do not import every brand by default.

After editing, read the saved import and referenced identity path back from disk. Explain that Claude treats these files as persistent project context, not as enforced security controls.

Claude Code may show a first-use approval dialog for file imports. Tell the user to review and accept the exact identity path before relying on the import. When available, verify the loaded files with Claude's `/memory` view in a fresh session; an import observed on disk is configured, but it is not proof that the running session loaded or approved it.

## Other agent hosts

Do not guess proprietary instruction filenames or claim compatibility. Keep the approved identity portable and tell the user what needs verification for their host: the project instruction file, its load scope, and whether it can reference or import the identity artifact.
