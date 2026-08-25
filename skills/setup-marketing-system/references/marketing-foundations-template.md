# Marketing Foundations template

Read this reference when creating a new artifact, restructuring an incomplete artifact, building a child-brand overlay, or checking whether a draft can pass approval gate 1.

Use English in the canonical artifact. Adapt tables and headings when natural, but preserve the frontmatter fields, five rule areas, governance, and composition rules.

```markdown
---
artifact: marketing-foundations
version: 1
status: draft
entity: "[Canonical entity name]"
entity_type: company | standalone-brand | child-brand
scope: "[Stable scope covered]"
owner: "[Authorized role or owner]"
last_reviewed: YYYY-MM-DD
business_context_path: "[Canonical identity path]"
business_context_version: 1
parent_foundations_path: null
parent_foundations_version: null
---

# Marketing Foundations — [Entity]

## How agents apply this profile

- Read the referenced business identity before this profile.
- Apply only approved rules within the stated scope.
- Do not turn unresolved decisions into rules.
- For a child brand, read the parent identity, child identity, parent foundations, then this overlay.
- Surface material conflicts instead of resolving them by file order.

## Basis markers

- `[C]` confirmed by an authorized stakeholder
- `[S1]`, `[S2]`, ... supported by a source listed below
- `[I]` inferred and awaiting confirmation
- `[?]` unknown or unresolved

## Context references

| Artifact or authority | Path or reference | Version/date | Scope | Notes |
|---|---|---|---|---|
| Business identity | | | | |

## 1. Offer–Audience–Situation Fit

| Offer reference | Audience reference | Situation or desired outcome | Applicable rule | Poor fit, exclusion, or cautious fallback | Basis |
|---|---|---|---|---|---|
| | | | | | |

## 2. Messaging, Claims & Evidence Rules

| Message or claim | Scope | Status | Evidence reference | Qualification, approval, or fallback | Basis |
|---|---|---|---|---|---|
| | | approved / conditional / prohibited | | | |

Evidence means an existing verifiable basis such as a specification, policy, dataset, study, certification, approved case study, authorized testimonial, or approved company page. Do not invent evidence or require a new evidence pack merely to complete setup.

## 3. Channel & Format Roles

| Channel or format | Stable role | Suitable scope | Limits or misuse | Undefined-state fallback | Basis |
|---|---|---|---|---|---|
| | | | | | |

## 4. Editorial, Visual & Quality Standards

| Standard | Applies to | Authoritative reference | Required check or prohibited practice | Fallback | Basis |
|---|---|---|---|---|---|
| | | | | | |

## 5. Controls, Authority & Approvals

| Activity or output | Authority level | Required checks | Authorized approver | Execution boundary or fallback | Basis |
|---|---|---|---|---|---|
| | autonomous / propose-only / prohibited | | | | |

Content approval never implies authorization to publish, send, configure, purchase, or spend.

## Conflicts and resolutions

| Topic | Conflicting accounts or rules | Impact | Resolution | Status | Basis |
|---|---|---|---|---|---|
| | | blocking / non-blocking | | open / resolved | |

## Unresolved decisions

Use only: `not established from supplied sources`, `exists but unavailable`, `not defined`, `unknown to user`, or `not applicable`.

| Decision or gap | State | Impact | Cautious agent behavior | Owner or review trigger | Basis |
|---|---|---|---|---|---|
| | | blocking / non-blocking | | | |

## Sources

| ID | Source | Date accessed or supplied | What it supports | Usage or sensitivity notes |
|---|---|---|---|---|
| S1 | | | | |

## Review triggers

| Concrete change | Rules affected | Owner or next check |
|---|---|---|
| | | |

## Changelog

- v1 (YYYY-MM-DD) — Initial approved Marketing Foundations.
```

## Rule-writing pattern

Prefer an instruction that can change behavior:

> For renewal-focused email to existing customers, use documented adoption outcomes and do not imply guaranteed savings. If the cited result is older than the current offer version, request evidence review before using a number. `[C; S3]`

Avoid a descriptive note that leaves the decision implicit:

> Customers care about savings and email is important.

Not every rule needs a table row or every possible field. The test is whether another agent can identify the behavior, scope, basis, and relevant fallback without inventing a decision.

## Child-brand overlay

For `entity_type: child-brand`:

- set `business_context_path` to the child identity and record the parent identity under Context references;
- set `parent_foundations_path` and `parent_foundations_version` to the company base;
- include only sections and rows that add, narrow, or explicitly specialize the parent;
- do not copy unchanged company rules;
- keep a material conflict open until an authorized owner resolves it.

## Approval readiness

A draft can be approved only when:

- the referenced identity is approved, readable, and scope-compatible;
- all five areas have a rule or a precisely classified gap;
- no blocking conflict remains open;
- essential authority and approvals are defined;
- every non-blocking gap has a cautious agent behavior;
- no `[I]` item operates as a rule;
- sources and concrete review triggers are recorded.

At approval, change `status` to `approved`. Start at version `1`; increment the integer for substantive updates and preserve it for typo-only corrections.
