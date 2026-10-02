# Augmented Marketing Suite overview

Augmented Marketing Suite helps when an AI request begins with an output but the marketing decision is still open. Instead of moving straight from “write a campaign” to production, a marketer can provide context, clarify the challenge, compare directions, coordinate the four Ps, and prepare campaign or content work for review.

For example, if a team wants LinkedIn leads for a new training service, the Suite can keep price, capacity, audience evidence, and access decisions visible before the team commits to the campaign. It structures the work and preserves the decision record; the responsible marketer remains accountable for the decision and any external action.

## Who it is for

The primary audience is marketers and communication managers introducing AI agents into their work, marketing professionals who want more than one-off prompts, consultants and agencies working with an authorised client representative, and teams that need to share context and decisions across people and agents. This audience is a product focus, not a claim that a real-world segment has already been validated.

## How the parts fit together

```text
Assistant
   ↓ orientation
Business identity and marketing foundations
   ↓ reusable context and rules
Brand voice, when needed
   ↓
Marketing challenge
   ↓
Marketing direction
   ↓
Product · Price · Place · Promotion
   ↓
Campaign and content work
   ↓
Review, results, and learning
```

The sequence is modular. A team can invoke a specialist directly when the necessary decision and inputs already exist. The Assistant helps a user who describes a need without knowing the technical skill name. It does not duplicate the specialist methods or make the marketing decision.

## The decision areas

| Decision area | Skills | What the marketer receives |
| --- | --- | --- |
| Orientation | `augmented-marketing-assistant` | A suggested next skill, when the environment supports the next step |
| Business context | `setup-business-context` | A reusable identity with confirmed facts, constraints, and open questions |
| Marketing rules | `setup-marketing-system` | Shared foundations with sources, boundaries, and responsibilities |
| Brand voice | `setup-brand-voice` | A reusable voice guide or a focused review |
| Challenge | `define-marketing-challenge` | A clear problem, audience, desired change, evidence, and success criteria |
| Direction | `choose-marketing-direction` | A comparison of alternatives, trade-offs, risks, assumptions, and recommendation |
| Marketing mix | `define-marketing-mix` | Coordinated choices for Product, Price, Place, and Promotion |
| Campaign | `design-campaign`, `campaign-review`, `campaign-debrief` | A campaign specification, pre-launch review, and result-based next decision |
| Content | `content-director`, `write-marketing-copy` | A content recommendation or review-ready copy grounded in available facts |

## Working principles

### Context before execution

The agent should know the organisation's identity, approved facts, constraints, and relevant rules before producing a specific campaign or text. A context file is useful because it can be reused and reviewed; it is not a substitute for keeping the underlying information current.

### Decisions before production

A request for a webinar, a LinkedIn post, or a lead signal may be a tactic rather than a validated direction. The skills can clarify the challenge and compare options before production, while still allowing a direct builder when the strategic work is already complete.

### Evidence before confidence

Sources, confirmed facts, inferences, assumptions, conflicts, and missing information should remain distinguishable. A fluent sentence does not make an unverified claim true.

### Four Ps, not promotion alone

Product, Price, Place, and Promotion are connected decisions. A communication idea can expose an unresolved product, pricing, access, capacity, or ownership decision; the Suite can make that dependency visible without deciding for another function.

### Human approval for consequential choices

The skills propose and structure. A responsible person approves. Content approval does not automatically authorise saving a document, publishing, media spend, sending, or changes in an external system.

## Working in different environments

The method can be used in a conversation with the relevant sources and a person who can review the proposed decisions. File access, web research and visual tools can help when available, but they are not required for every task. If the environment cannot save a document or continue a step, the assistant should explain the practical limit and provide the work that can be completed.


## Release status and evidence

Suite 1.0.0 is the stable public reference. Repository reports record a reproducible build, 13 archives, strict bundle validation, public asset downloads, checksums, and ZIP integrity checks. This evidence does not prove behaviour in every runtime or effectiveness with real marketers.

The [1.0.1-l10n.1 source candidate](../../LOCALIZATION-CORE-STATUS.md) is separate from 1.0.0. It is not published or installed and must not be used to strengthen a claim about the stable release.

## What to expect

Expect a clearer decision record, explicit alternatives, visible assumptions, and review-ready documents when the relevant sources are available. Do not expect a replacement for a marketing leader, a guarantee of better results, autonomous execution, or a proven equivalent of an experienced strategist. Those claims require evidence beyond the current repository reports.

For installation, see [`INSTALLATION.md`](../../INSTALLATION.md). For project communication, portability policy, and historical release evidence, see [`OFFERTA-COMUNICAZIONE.md`](../../OFFERTA-COMUNICAZIONE.md), [`PORTABILITA.md`](../../PORTABILITA.md), [`RELEASE-STATUS.md`](../../RELEASE-STATUS.md), and [`evals/suite-1.0.0/README.md`](../../evals/suite-1.0.0/README.md). Those Italian documents provide project context; they are not runtime dependencies of an installed skill.
