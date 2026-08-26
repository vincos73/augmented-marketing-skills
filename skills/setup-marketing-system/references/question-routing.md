# Marketing Foundations question routing

Read this guide when a new or existing profile has several gaps, conflicts, or proposed rules and the agent must choose what deserves the marketing leader's attention. Do not run it as a fixed questionnaire.

## Build a rule ledger privately

For each of the five areas, classify consequential items as:

- supported by a supplied source;
- confirmed by an authorized user;
- inferred and awaiting confirmation;
- conflicting across sources or with the business identity;
- missing and not yet classified;
- explicitly unavailable, not defined, unknown, or not applicable.

Also classify whether the gap is blocking, material but non-blocking, or enrichment/task-specific. Do not expose a long ledger; use it to draft the first useful proposal and select questions.

## Keep the conversation oriented

The manager should always understand where the work stands and what will happen next. Add a short bridge whenever the conversation moves from reading to synthesis, from synthesis to questions, or from questions to approval. Adapt the wording to the evidence; do not repeat a fixed script.

Useful patterns:

- **Opening:** “Thanks — I have enough to start. I’ll first map the stable rules already supported by your materials, then I’ll bring back only the decisions that could change the draft.”
- **After reading:** “Here’s where we are: the sources support these rules, while this point is still ambiguous. Next I’ll turn that into a compact proposal and focus on the one choice that affects approval.”
- **Before a question:** “This matters because the answer changes how the agent should handle [situation]. Which of these reflects your standing practice?”
- **After an answer:** “That settles the main ambiguity. I’ll incorporate it, check the remaining areas for conflicts, and then show you the version ready for approval.”
- **At approval:** “The draft is ready to approve. You are approving the content at this path and version; installation in the agent’s instructions remains a separate choice.”
- **At a blocker:** “I can’t responsibly turn this into an approved rule yet because [specific reason]. We can leave it unresolved with a cautious fallback, or you can confirm the missing decision.”

These bridges are part of the user experience, not progress reports. Do not expose internal ledgers, core names, schemas, or raw state while orienting the manager.

## Rank by consequence

Ask at most three questions per batch. Prefer questions that:

1. prevent an unauthorized action, unsafe claim, privacy/compliance issue, or material identity conflict;
2. clarify a high-use offer–audience–situation rule;
3. determine whether an important claim is approved, supportable, conditional, or prohibited;
4. establish a default channel role or quality rule that would change frequent work;
5. classify a non-blocking gap so the profile can be approved honestly.

Do not ask for a detail that is already supported unless confirmation resolves a real ambiguity. An explicit missing-information state is a valid answer; it does not make the underlying rule known.

## Shape the first useful response

Lead with a compact provisional proposal derived from the identity and marketing materials. Normally include:

- entity and scope being used;
- strongest stable rules already supported across the five areas;
- material conflicts, unsupported claims, or authority risks;
- no more than three questions that could change approval readiness;
- a compact source key.

Do not mirror the full artifact template, show raw YAML/JSON, generate a wizard, or spend a turn only describing progress. Defer the complete profile to approval gate 1.

## Question lenses

The prompts below are examples for selection, not a sequence.

### Offer–Audience–Situation Fit

- For this offer, which documented audience and situation should agents treat as a valid fit?
- Which conditions indicate poor fit or require qualification?
- If the sources mention several audiences, is the relationship stable or only a current campaign choice?

Do not ask the manager to choose a new growth market or campaign segment.

### Messaging, Claims & Evidence

- Which of these source-backed messages are approved for routine use, and which need review?
- What existing source supports this numerical or comparative claim, and where may it be used?
- If evidence is insufficient, should agents use a weaker qualitative formulation or avoid the claim?

Do not request a new study or evidence pack merely to finish onboarding.

### Channel & Format Roles

- What stable job does this channel perform, if any, across marketing work?
- Which audience, situation, or format is it generally suited or unsuited for?
- Is the documented cadence a durable rule or only a current operating plan?

Do not build a media plan, content calendar, or account configuration.

### Editorial, Visual & Quality Standards

- Which existing guideline, template, or representative output is authoritative?
- Which minimum check must every output pass before it is ready for review?
- Which common error or off-brand practice must agents avoid?

Do not create a new identity or detailed style system under the guise of setup.

### Controls, Authority & Approvals

- Which work may an agent complete autonomously, and which must remain a proposal?
- Who may approve this kind of claim or output, and is that approval content-only or also execution authority?
- Which legal, privacy, compliance, or brand review is triggered by this topic or action?

If the route is absent, record `not defined`; do not appoint an owner.

## Proposing a missing stable rule

When a necessary rule is genuinely `not defined`, the skill may offer a concise recommendation or two meaningful alternatives. Label the basis as `[I]`, explain the consequence, and ask the authorized leader to approve, correct, or leave it unresolved. Never smuggle the recommendation into the approved profile as an existing practice.

## Update mode

For an approved profile, ask what materially changed, inspect the affected sources, and show the impacted rules and downstream consequences. Do not reopen all five areas unless the change creates a cross-cutting conflict. Preserve unaffected rules, source history, unresolved decisions, and prior changelog entries.

## Check before approval

Verify that:

- every area has supported rules or an explicit gap state;
- temporary priorities have not become stable foundations;
- evidence usage is narrower than or equal to what the sources support;
- content approval is not confused with execution authority;
- no inferred rule is active;
- no blocking conflict remains;
- every non-blocking gap has a cautious fallback;
- the complete draft references rather than duplicates business identity and external guidelines.
