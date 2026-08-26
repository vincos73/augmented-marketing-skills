# Marketing Foundations question routing

Read this guide when a new or existing profile has several gaps, conflicts, or proposed rules and the agent must choose what deserves the marketing leader's attention. Do not run it as a fixed questionnaire.

## Build a rule ledger privately

For each of the five areas, classify consequential items as:

- supported by a supplied source;
- confirmed by an authorized user;
- inferred and awaiting confirmation;
- conflicting across sources or with the business identity;
- missing and not yet classified;
- esplicitamente non disponibile, non definito, sconosciuto o non applicabile.

Also classify whether the gap is `bloccante`, `non bloccante ma materiale`, or `di arricchimento o specifico del task`. Do not expose a long ledger; use it to draft the first useful proposal and select questions.

## Keep the conversation oriented

The manager should always understand where the work stands and what will happen next. Add a short bridge whenever the conversation moves from reading to synthesis, from synthesis to questions, or from questions to approval. Adapt the wording to the evidence; do not repeat a fixed script.

Useful patterns:

- **Apertura:** “Bene, ho abbastanza per iniziare. Prima mapperò le regole stabili già sostenute dai tuoi materiali, poi ti sottoporrò soltanto le decisioni che potrebbero cambiare la bozza.”
- **Dopo la lettura:** “Ecco dove siamo: le fonti sostengono queste regole, mentre questo punto resta ambiguo. Ora lo trasformerò in una proposta compatta e mi concentrerò sulla scelta che incide sull'approvazione.”
- **Prima di una domanda:** “Questo è importante perché la risposta cambia il modo in cui l'agente dovrebbe gestire [situazione]. Quale di queste opzioni riflette la vostra prassi stabile?”
- **Dopo una risposta:** “Abbiamo risolto l'ambiguità principale. La integrerò, controllerò le aree restanti per individuare eventuali conflitti e poi ti mostrerò la versione pronta per l'approvazione.”
- **All'approvazione:** “La bozza è pronta per l'approvazione. Stai approvando il contenuto in questo percorso e a questa versione; l'installazione nelle istruzioni dell'agente resta una scelta separata.”
- **In caso di blocco:** “Non posso trasformare responsabilmente questo punto in una regola approvata perché [motivo specifico]. Possiamo lasciarlo irrisolto con un fallback prudente, oppure puoi confermare la decisione mancante.”

These bridges are part of the user experience, not progress reports. Do not expose internal ledgers, core names, schemas, or raw state while orienting the manager.

## Rank by consequence

Ask at most three questions per batch. Prefer questions that:

1. prevent an unauthorized action, unsafe claim, privacy/compliance issue, or material identity conflict;
2. clarify a high-use offer–audience–situation rule;
3. determinare se un claim importante è approvato, sostenibile, condizionale o vietato;
4. establish a default channel role or quality rule that would change frequent work;
5. classificare una lacuna non bloccante, così il profilo può essere approvato correttamente.

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

- Quali di questi messaggi sostenuti dalle fonti sono approvati per l'uso ordinario e quali richiedono una revisione?
- Quale fonte esistente sostiene questo claim numerico o comparativo e dove può essere utilizzato?
- Se le prove non sono sufficienti, l'agente dovrebbe usare una formulazione qualitativa più prudente o evitare il claim?

Do not request a new study or evidence pack merely to finish onboarding.

### Channel & Format Roles

- Quale ruolo stabile svolge questo canale, se ne svolge uno, nelle attività di marketing?
- Per quale pubblico, situazione o formato è generalmente adatto o non adatto?
- La frequenza documentata è una regola durevole o soltanto un piano operativo attuale?

Do not build a media plan, content calendar, or account configuration.

### Editorial, Visual & Quality Standards

- Quale linea guida, template o output rappresentativo esistente è autorevole?
- Quale controllo minimo deve superare ogni output prima di essere pronto per la revisione?
- Quale errore ricorrente o pratica fuori brand devono evitare gli agenti?

Do not create a new identity or detailed style system under the guise of setup.

### Controls, Authority & Approvals

- Quale lavoro può completare autonomamente un agente e quale deve restare una proposta?
- Chi può approvare questo tipo di claim o output, e l'approvazione riguarda solo il contenuto oppure anche l'autorizzazione all'esecuzione?
- Quale revisione legale, privacy, di conformità o di brand viene attivata da questo tema o azione?

If the route is absent, record `non definito`; do not appoint an owner.

## Proposing a missing stable rule

When a necessary rule is genuinely `non definito`, the skill may offer a concise recommendation or two meaningful alternatives. Label the basis as `[I]`, explain the consequence, and ask the authorized leader to approve, correct, or leave it unresolved. Never smuggle the recommendation into the approved profile as an existing practice.

## Update mode

For an approved profile, ask what materially changed, inspect the affected sources, and show the impacted rules and downstream consequences. Do not reopen all five areas unless the change creates a cross-cutting conflict. Preserve unaffected rules, source history, unresolved decisions, and prior changelog entries.

## Check before approval

Verify that:

- every area has supported rules or an explicit gap state;
- temporary priorities have not become stable foundations;
- evidence usage is narrower than or equal to what the sources support;
- content approval is not confused with execution authority;
- no inferred rule is active;
- nessun conflitto bloccante resta aperto;
- ogni lacuna non bloccante ha un fallback prudente;
- the complete draft references rather than duplicates business identity and external guidelines.
