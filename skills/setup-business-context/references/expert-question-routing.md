# Expert Question Routing

Use this guide when a new identity is materially incomplete, the sources conflict, or the agent must choose which gaps deserve the manager's attention. The goal is not to run a fixed questionnaire. It is to ask the smallest set of questions that makes the identity safer and more useful.

## Build a gap ledger first

Before asking anything, map each consequential identity area to one state:

- supported by a supplied source;
- confirmed by the user;
- inferred and awaiting confirmation;
- conflicting across sources;
- absent or ambiguous;
- explicitly not defined, unknown, unavailable, or not applicable.

Do not ask for information already supported unless confirmation would resolve a material ambiguity. Do not expose this ledger as a long diagnostic report; use it to select the next questions.

## Rank questions by consequence

Select at most three questions per batch. Rank candidate questions in this order:

1. prevent an agent from making a false, unsafe, sensitive, or unauthorized statement;
2. establish the entity, its current scope, its offers, and its company/brand relationships;
3. clarify who receives value, who pays or decides, and what situation creates demand;
4. distinguish the entity from real alternatives and connect distinctive capabilities to customer value and proof;
5. preserve recognizable language, correct common misconceptions, and classify non-blocking identity gaps.

An explicit `unknown`, `not defined`, `exists but unavailable`, or `not applicable` can satisfy the need to classify an essential gap. It does not make the underlying information known.

## Use expert lenses without importing a strategy workshop

The prompts below are a question bank, not a mandatory sequence. Lead with the provisional answer extracted from sources whenever possible.

### Entity and current scope

Ask when the legal entity, operating identity, hierarchy, geography, or current portfolio is ambiguous.

- What exactly are we describing: the company, a standalone brand, or a brand within a company?
- Which offers, markets, geographies, or related brands are covered by this identity?
- What is outside the scope or no longer current?

### Offer, value, and high-level business model

Ask for current facts, not future choices.

- What do you sell today, and what concrete change does it produce for the customer?
- Who pays, what do they pay for, and how is the value delivered?
- Which offers are current, legacy, experimental, or planned and therefore must not be presented as generally available?

Record only the minimum business-model information an agent needs. Do not seek margins, cost structure, confidential revenue, pricing strategy, or trade secrets by default.

### Customer and buying system

Replace a vague request for "the target" with concrete roles and boundaries.

- Who uses the offer, who pays, who decides, and who can block or approve the purchase?
- Which customer characteristics indicate a strong fit?
- Who is not a fit or is deliberately not served?

Do not force a single priority audience when the entity has multiple established offers or buying systems. Preserve the mapping between each offer and its relevant roles.

### Trigger, job, and desired outcome

Ask when the sources name audiences but do not explain why they seek the offer.

- What situation makes a customer start looking for this kind of solution?
- What progress or outcome are they trying to achieve?
- How do they recognize that the result is good enough?

Treat documented customer language as evidence. Treat an internal hypothesis about customer motivation as an inference until confirmed.

### Alternatives, differentiation, and proof

Do not ask only "Who are your competitors?" or "What is your USP?" Use the customer's actual choice set.

- If this offer did not exist, what would the customer probably do instead?
- Which capability is materially different from those alternatives?
- What customer value follows from that capability?
- What evidence supports the capability, value, or claim, and may that evidence be used publicly?

Keep the chain explicit:

> alternative or status quo → distinctive capability → customer value → proof → usage restriction

Do not invent a differentiated position when the organization has not approved one. Record the components that are established and leave the unresolved decision visible.

### Misconceptions, language, and recognizability

Ask when future agents could easily produce generic or misleading descriptions.

- What do customers, partners, or new colleagues most often misunderstand about the entity?
- What must an agent never assume, imply, or promise?
- Which official names, terms, spellings, or customer expressions must be preserved?
- Which real examples best represent the established voice?

Prefer examples over adjective lists. Detailed editorial and visual production rules belong in the applicable content profile, not in this general identity.

### Boundaries and approvals

Ask about the type of statement and its approval route, not merely one universal approver.

- Which claims can be used as documented, which require fresh evidence, and which require human approval?
- Which topics, markets, customer groups, legal entities, or regulated areas need special handling?
- Who owns each relevant approval route?

If no route exists, record `not defined`; do not silently assign one.

### Mission, purpose, and history

Treat these as material but normally non-blocking unless the entity's work makes them operationally necessary.

- Is there an official mission or purpose in an approved source?
- If not found, does it exist but remain unavailable, has it not been defined, is it unknown to the user, or is it not applicable?
- Which historical facts materially change how the entity should be understood today?

Never rewrite an inferred purpose as the official mission. Distinguish current identity, approved aspiration, and historical language.

## Phrase questions for managers

- Use plain language. Avoid unexplained terms such as `ICP`, `USP`, `JTBD`, `positioning statement`, or `value proposition`.
- Ask one primary question per card. Group fields only when they form one natural system, such as user, payer, decision-maker, and blocker.
- Derive suggested choices from supplied sources; do not lead the user with generic answers invented by the agent.
- Always allow correction, a free-form answer, and the applicable missing-information states.
- When presenting a source-backed provisional answer, offer `confirm`, `correct`, and `unknown` rather than asking the user to restate it.
- Echo the captured answer before advancing, especially when the interface is unavailable or the answer changes a prior claim.

## Respect the strategy boundary

Do not use this setup to decide:

- growth objectives or strategic priorities;
- a new target segment or market to enter;
- a new position, mission, promise, or differentiator;
- pricing strategy, investment, budget, or resource allocation;
- campaign goals, channels, content plans, KPIs, or tests;
- product roadmap or organizational redesign.

If one of these is missing, record it only when its absence affects the identity, then route the later decision to the appropriate strategy or execution workflow. An approved current decision supplied by the user may be recorded as context; the setup must not create it.

## Check before approval

Before presenting the identity for approval, verify that:

- every essential area has content or an explicit missing-information state;
- current facts are separated from plans and aspirations;
- audiences are not collapsed when offers or buying roles differ;
- differentiation is not a generic adjective detached from alternatives and proof;
- unsupported claims and inferred customer motives remain visible;
- non-blocking gaps, including an undocumented mission, do not prevent completion;
- concrete review triggers are recorded when the supplied material establishes them;
- no question crossed into strategy creation.
