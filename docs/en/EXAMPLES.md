# Examples for marketers

These synthetic examples show how the Suite can preserve sources, separate a decision from a tactic, and handle language and protected text. The language-alignment examples describe the local 1.0.1-l10n.1 source policy to answer in the user's language or the requested document language, including with mixed-language sources. They are not a runtime guarantee for stable 1.0.0 packages or evidence that a campaign will improve performance.

## Example 1: mixed-language sources, English working output

A marketer provides approved Italian notes and asks for an English challenge brief.

**Source A — approved, Italian**

```text
Il servizio aiuta piccoli team a preparare il budget trimestrale.
Il prezzo e il numero di clienti pilota non sono ancora approvati.
```

**Source B — working note, English**

```text
The team is considering a short workshop, but there is no evidence yet that a workshop is the right offer.
```

A useful response keeps the source status visible:

```text
Confirmed facts:
- The service helps small teams prepare a quarterly budget.

Open decisions:
- Price and the number of pilot customers are not approved.

Working hypothesis:
- A short workshop is being considered; its fit has not been demonstrated.

Next decision:
- Clarify the marketing challenge before choosing the format or writing promotion copy.
```

The Italian source can remain quoted in the record, while the working brief is in English. Translation does not turn an unapproved price or a possible workshop into a confirmed fact.

## Example 2: a tactic may hide a challenge

**Request**

```text
Create a LinkedIn campaign for our new training service and collect leads next month.
```

The marketer may already know the tactic, but the decision still needs context. A useful first pass asks or records:

- which audience has the problem and how it is recognised;
- what change the organisation wants to produce;
- which service, price, capacity, and access decisions are approved;
- what evidence supports the need;
- what result would justify continuing, changing, or stopping the test.

The relevant next skill may be `define-marketing-challenge`, followed by `choose-marketing-direction` or `define-marketing-mix`. If the challenge and direction are already approved, `design-campaign` can be used directly. The framework keeps the LinkedIn campaign as a possible activation rather than treating it as proof of demand or purchase intent.

## Example 3: protect exact text while adapting copy

An English product sheet contains a phrase that legal or product has marked as protected.

**Source instruction**

```text
Audience: operations managers in small manufacturing teams.
Approved fact: The service includes a 30-minute setup call.
PROTECTED TEXT — preserve exactly: "Ready in one working session"
Language requested: Italian.
```

The copy task may translate the approved fact and adapt the surrounding sentence, but it preserves the protected string exactly when the instruction requires it:

```text
Include una chiamata di configurazione di 30 minuti.
Ready in one working session
```

If the user asks to translate the protected string too, the skill should surface the conflict and request a decision from the responsible owner. It should not silently alter a protected claim or invent supporting evidence.

## Example 4: Italian and English brand-voice calibration

The marketer supplies an Italian voice guide and asks for an English landing-page paragraph.

**Italian guidance**

```text
Voce: concreta, calma, rispettosa del tempo di chi legge.
Evitare superlativi e promesse di risultato.
```

**English adaptation**

```text
Plan the next marketing decision with the information your team can verify.
Keep the open choices visible before you commit to a campaign.
```

The adaptation carries the approved voice principles across languages without claiming that the product guarantees better decisions or results. A language change changes the wording, not the evidence boundary.

## Example 5: sources that disagree

Suppose an Italian sales note says that the service is available immediately, while an English operations note says capacity is limited to two teams per month. The skill should retain both sources, mark the conflict, and route the capacity decision to the responsible owner. A campaign brief can remain a draft with the availability claim unresolved; it should not choose the more attractive sentence merely because it is easier to market.

## A compact prompt pattern

```text
Use the available sources to [decision or task].
Separate confirmed facts, assumptions, open decisions, and missing evidence.
Keep the following text exact: [protected text, if any].
Return the working document in [language].
Do not publish, send, spend, or change external systems.
```

The prompt helps state the work and its boundaries. The relevant skill still determines the method and the document structure.
