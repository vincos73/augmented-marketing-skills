# Install approved Marketing Foundations

Read this reference only after approval gate 1 has produced a canonical Marketing Foundations artifact and the user has selected an agent host.

## Explain the handoff conversationally

Make the handoff feel like a practical next step, not a technical escalation. First acknowledge that the foundations are approved, then explain what installation will change and what it will not change:

> Your Marketing Foundations are approved and ready to reuse. The next step is optional: I can add a small managed block to the project instructions so future marketing tasks read the approved identity and foundations automatically. This will guide the agent’s context; it will not grant permission to publish, spend, or change external systems. I’ll show you the exact change before saving it.

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

Before company-specific marketing work for [Entity], read `[identity-path]` and `[foundations-path]` and apply their approved facts, rules, unknowns, and approval boundaries. For work about a child brand, also read its matching identity and marketing overlay; do not load unrelated brands.

At the start of every substantive response that performs or advances company-specific marketing work, add one compact FYI naming the entity and versions actually read. If a required artifact is unavailable, unapproved, conflicting, or materially stale, show an actionable warning instead of claiming it was applied.
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

For every substantive company-specific marketing response, state in one compact FYI which entity and artifact versions were actually applied. Do not treat these imports as execution permission.
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
