# Marketing Foundations template

Read this reference when creating a new artifact, restructuring an incomplete artifact, building a child-brand overlay, or checking whether a draft can pass approval gate 1.

Use Italian throughout the human-readable canonical artifact, including headings, table labels, rules, explanations, sources, conflicts, review triggers, changelog entries, and status values. Keep the canonical name **Marketing Foundations**, the frontmatter keys, technical identifiers, file paths, official names, and source quotations unchanged when needed for schema stability or fidelity. The `status` value in frontmatter is also Italian: use `bozza` before approval and `approvato` after approval. Adapt tables and headings when natural, but preserve the frontmatter fields, five rule areas, governance, and composition rules.

```markdown
---
artifact: marketing-foundations
version: 1
status: bozza
entity: "[Nome canonico dell'entità]"
entity_type: company | standalone-brand | child-brand
scope: "[Ambito stabile coperto]"
owner: "[Ruolo o responsabile autorizzato]"
last_reviewed: YYYY-MM-DD
business_context_path: "[Percorso dell'identità canonica]"
business_context_version: 1
parent_foundations_path: null
parent_foundations_version: null
---

# Marketing Foundations — [Entità]

## Come gli agenti applicano questo profilo

- Leggere l'identità aziendale referenziata prima di questo profilo.
- Applicare soltanto le regole approvate nello scope indicato.
- Non trasformare le decisioni irrisolte in regole.
- Per un brand figlio, leggere l'identità dell'azienda, l'identità del brand, le foundations aziendali e infine questo overlay.
- Rendere visibili i conflitti materiali invece di risolverli in base all'ordine dei file.

## Marcatori di base

- `[C]` confermato da un responsabile autorizzato
- `[S1]`, `[S2]`, ... sostenuto da una fonte elencata sotto
- `[I]` inferito e in attesa di conferma
- `[?]` sconosciuto o irrisolto

## Riferimenti al contesto

| Artefatto o autorità | Percorso o riferimento | Versione/data | Ambito | Note |
|---|---|---|---|---|
| Identità aziendale | | | | |

## 1. Corrispondenza tra offerta, pubblico e situazione

| Riferimento all'offerta | Riferimento al pubblico | Situazione o risultato desiderato | Regola applicabile | Scarso fit, esclusione o fallback prudente | Base |
|---|---|---|---|---|---|
| | | | | | |

## 2. Regole per messaggi, claim e prove

| Messaggio o claim | Ambito | Stato | Riferimento alla prova | Qualificazione, approvazione o fallback | Base |
|---|---|---|---|---|---|
| | | approvato / condizionale / vietato | | | |

Per prova si intende una base verificabile già esistente, come una specifica, una policy, un dataset, uno studio, una certificazione, un case study approvato, una testimonianza autorizzata o una pagina aziendale approvata. Non inventare prove e non richiedere un nuovo evidence pack soltanto per completare il setup.

## 3. Ruoli di canali e formati

| Canale o formato | Ruolo stabile | Ambito adatto | Limiti o uso improprio | Fallback per stato non definito | Base |
|---|---|---|---|---|---|
| | | | | | |

## 4. Standard editoriali, visivi e qualitativi

| Standard | Si applica a | Riferimento autorevole | Controllo richiesto o pratica vietata | Fallback | Base |
|---|---|---|---|---|---|
| | | | | | |

## 5. Controlli, autorità e approvazioni

| Attività o output | Livello di autorità | Controlli richiesti | Responsabile autorizzato | Confine di esecuzione o fallback | Base |
|---|---|---|---|---|---|
| | autonoma / solo proposta / vietata | | | | |

L'approvazione del contenuto non autorizza mai a pubblicare, inviare, configurare, acquistare o spendere.

## Conflitti e risoluzioni

| Tema | Resoconti o regole in conflitto | Impatto | Risoluzione | Stato | Base |
|---|---|---|---|---|---|
| | | bloccante / non bloccante | | aperto / risolto | |

## Decisioni irrisolte

Usare soltanto: `non stabilito dalle fonti fornite`, `esiste ma non è disponibile`, `non definito`, `sconosciuto all'utente` o `non applicabile`.

| Decisione o vuoto | Stato | Impatto | Comportamento prudente dell'agente | Responsabile o trigger di revisione | Base |
|---|---|---|---|---|---|
| | | bloccante / non bloccante | | | |

## Fonti

| ID | Fonte | Data di accesso o consegna | Che cosa sostiene | Note d'uso o sensibilità |
|---|---|---|---|---|
| S1 | | | | |

## Trigger di revisione

| Cambiamento concreto | Regole interessate | Responsabile o prossimo controllo |
|---|---|---|
| | | |

## Registro delle modifiche

- v1 (YYYY-MM-DD) — Prime Marketing Foundations approvate.
```

## Modello di scrittura delle regole

Prefer an instruction that can change behavior:

> Per le email rivolte al rinnovo di clienti esistenti, usare risultati documentati sull'adozione e non suggerire risparmi garantiti. Se il risultato citato è precedente alla versione attuale dell'offerta, richiedere una revisione delle prove prima di usare un numero. `[C; S3]`

Avoid a descriptive note that leaves the decision implicit:

> I clienti sono interessati ai risparmi e l'email è importante.

Not every rule needs a table row or every possible field. The test is whether another agent can identify the behavior, scope, basis, and relevant fallback without inventing a decision.

## Overlay di brand figlio

Per `entity_type: child-brand`:

- impostare `business_context_path` sull'identità del brand figlio e registrare l'identità dell'azienda nei Riferimenti al contesto;
- impostare `parent_foundations_path` e `parent_foundations_version` sulla base aziendale;
- includere soltanto sezioni e righe che aggiungono, restringono o specializzano esplicitamente il profilo del genitore;
- non copiare le regole aziendali invariate;
- mantenere aperto un conflitto materiale finché non viene risolto da un responsabile autorizzato.

## Prontezza per l'approvazione

Una bozza può essere approvata soltanto quando:

- l'identità referenziata è approvata, leggibile e compatibile con lo scope;
- tutte e cinque le aree hanno una regola o un vuoto classificato con precisione;
- non restano conflitti bloccanti aperti;
- autorità e approvazioni essenziali sono definite;
- ogni vuoto non bloccante ha un comportamento prudente dell'agente;
- nessun elemento `[I]` opera come regola;
- fonti e trigger concreti di revisione sono registrati.

Al momento dell'approvazione, impostare `status` su `approvato`. Prima dell'approvazione usare `status: bozza`. Iniziare dalla versione `1`, incrementare il numero intero per gli aggiornamenti sostanziali e mantenerlo per le sole correzioni tipografiche.
