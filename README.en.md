# Augmented Marketing Suite

> Turn an uncertain marketing request into a decision a team can review before it commits to a campaign or a piece of copy.

When a team asks an AI agent for “a LinkedIn campaign” or “an email,” it may still be unclear whether the offer, audience, price, access, or message is the real issue. Augmented Marketing Suite helps marketers supply the relevant context, frame the challenge, compare directions, and carry an approved direction into marketing-mix, campaign, or content work.

For example, a training business with fewer online enquiries can ask the Suite to distinguish an offer problem from an audience or communication problem, record the missing evidence, and compare a workshop with other responses before drafting promotion.

The Suite supports the conversation and its decision record. The responsible marketer still approves the decision and any external action.

The stable public distribution is 1.0.0. The separate 1.0.1-l10n.1 source line is a local evaluation candidate.

## What the Suite is for

Many AI marketing workflows start with production: a post, an email, a campaign, or a plan. Faster production does not by itself establish that the problem was framed correctly, that the chosen direction is plausible, or that the work is consistent.

The Suite helps make the following visible and reusable:

- organisational context and approved marketing rules;
- the difference between sources, confirmed facts, inferences, assumptions, and missing information;
- the challenge before a tactic becomes the solution;
- alternatives, trade-offs, risks, and conditions for stopping;
- the relationship between Product, Price, Place, and Promotion;
- review, approval, and learning records that can be reused across conversations.

The framework can recommend a next decision, a narrower test, or a pause. Approval of a document does not automatically authorise publishing, spending, sending, or changing an external system.

## Quick start

After installing a compatible skill or plugin, start with a natural request. For example:

```text
I manage a small training business. Online enquiries have slowed down, but I do not yet know whether the issue is our offer, our audience, or our communication. Help me frame the marketing challenge and list what evidence is missing.
```

The same request can be made in Italian:

```text
Gestisco una piccola attività di formazione. Le richieste online sono diminuite, ma non so ancora se il problema riguarda l'offerta, il pubblico o la comunicazione. Aiutami a formulare la sfida di marketing e a elencare le evidenze mancanti.
```

The local 1.0.1-l10n.1 candidate introduces a language policy to answer in the user's language or the requested document language, including with mixed-language sources. This is an evaluation policy, not a runtime guarantee for the stable packages.

## Release status and evidence

**1.0.0 is the stable public release.** Published on GitHub on 13 September 2026, it contains 13 ZIP archives: one Claude plugin with 12 skills, one OpenAI/Codex plugin with 12 skills, and 11 portable ZIPs for the specialist skills. The release also contains a manifest and `SHA256SUMS`.

Evidence for its build, downloads, checksums, and local installation is in [`evals/suite-1.0.0/README.md`](evals/suite-1.0.0/README.md) and [`RELEASE-STATUS.md`](RELEASE-STATUS.md). It does not prove behaviour in every account or effectiveness with real marketers.

**1.0.1-l10n.1 is a source candidate for evaluation.** It contains English product guidance, activation metadata, and a language rule while retaining the stable campaign and copywriting method. It has not been published, installed, or validated in new application sessions and does not replace the stable archives. See the [candidate status](LOCALIZATION-CORE-STATUS.md). The English guides document the public product and its procedures; the skill instructions and their operational references remain in Italian.

## The 12 skills in Suite 1.0.0

| If you need to… | Use | Version | Result |
| --- | --- | --- | --- |
| Start from a marketing need without knowing which step applies | `augmented-marketing-assistant` | 0.3.0 | Orientation toward the relevant skill when the environment supports it |
| Give the agent a reusable picture of the organisation | `setup-business-context` | 0.6.7 | Business identity, approved facts, constraints, and open questions |
| Define durable marketing rules | `setup-marketing-system` | 0.3.4 | Marketing foundations with sources, rules, limits, and responsibilities |
| Define or review a reusable brand voice | `setup-brand-voice` | 0.1.2 | A voice guide or a scoped review |
| Decide whether a request is a marketing challenge | `define-marketing-challenge` | 0.1.8 | Challenge brief with audience, desired change, evidence, and success criteria |
| Compare possible strategic directions | `choose-marketing-direction` | 0.2.8 | Alternatives with benefits, drawbacks, risks, assumptions, and a recommendation |
| Turn an approved direction into marketing choices | `define-marketing-mix` | 0.1.9 | Coherent choices across Product, Price, Place, and Promotion |
| Design a coordinated campaign | `design-campaign` | 0.1.7 | Campaign specification with journey, messages, channels, assets, ownership, and measurement |
| Check a campaign before publication or sending | `campaign-review` | 0.1.4 | Review of strategic consistency, claims, operational readiness, and a debrief baseline |
| Interpret results and choose the next step | `campaign-debrief` | 0.1.7 | Observed results, limits, a recommended decision, and the next verification |
| Choose the most useful single content format | `content-director` | 0.1.2 | Editorial recommendation and, after approval, a content brief |
| Write, rewrite, or adapt one marketing text | `write-marketing-copy` | 0.1.5 | Review-ready copy grounded in available facts and voice |

`Augmented Marketing Assistant` is a normal orientation skill shared by both complete plugins. It does not add a separate marketing discipline, agent, subagent, MCP server, or connector. If the environment cannot load the specialist in the same conversation, the Assistant should name the technical skill and stop; you can invoke that skill directly.

## A practical path

```text
Business context
        ↓
Marketing foundations and brand voice, when needed
        ↓
Challenge brief
        ↓
Direction and trade-offs
        ↓
Product · Price · Place · Promotion
        ↓
Campaign or content
        ↓
Review, results, and next decision
```

This is a reusable path, not a mandatory sequence. If the challenge and direction are already documented, use a campaign or content skill directly. If the request is still vague, start with the Assistant or `define-marketing-challenge`.

## A short example

A training company wants to introduce a service but has not approved its price or pilot capacity. The marketer can document those open decisions, compare a short course, a recurring workshop, and a more structured service, then translate the selected direction into the four Ps before drafting a campaign or copy. The example illustrates a method; it does not predict sales, conversion, speed, or cost.

## Installation

For one specialist skill, use one portable ZIP from `dist/1.0.0/agent-skills/`. For the complete set, use the plugin made for the target platform:

| Environment | One skill | Complete Suite |
| --- | --- | --- |
| Claude | A portable ZIP | `dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip` |
| ChatGPT | A portable ZIP when direct skill loading is available | `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip` when a compatible plugin flow is available |
| Codex | A portable ZIP when the local flow supports it | `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip` when a compatible plugin catalogue or marketplace is available |

The portable ZIPs contain the 11 specialist skills. The Assistant is included in both complete plugins. Do not use a Claude plugin archive in an OpenAI/Codex flow or an OpenAI/Codex archive in a Claude flow. A ZIP attached to an ordinary chat is readable content; it is not automatically registered as a skill or plugin.

See the [English installation guide](INSTALLATION.md), the [English overview](docs/en/OVERVIEW.md), and the [English examples](docs/en/EXAMPLES.md). The Italian installation guide remains [`INSTALLAZIONE.md`](INSTALLAZIONE.md).

## Limits and source boundaries

The quality of a result depends on the sources supplied, the model and environment, and the responsible marketer's judgement. A repository file proves that an authoring source exists; it does not prove approval, session loading, or production reliability. Keep the stable release and the local candidate separate when describing version, features, or installation state.

For the architecture and communication policy, see [`OFFERTA-COMUNICAZIONE.md`](OFFERTA-COMUNICAZIONE.md), [`PORTABILITA.md`](PORTABILITA.md), and [`STANDARD-PROGETTAZIONE-SKILL.md`](STANDARD-PROGETTAZIONE-SKILL.md). These Italian documents record product and authoring decisions. Each installed skill carries its operational instructions in its own folder; these repository guides are not runtime dependencies.
