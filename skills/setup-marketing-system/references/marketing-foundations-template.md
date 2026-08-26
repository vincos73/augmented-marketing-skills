# Template per i fondamenti di marketing

Leggi questo riferimento quando crei un nuovo artefatto, ristrutturi un artefatto incompleto, costruisci un'integrazione per un brand figlio o verifichi la preparazione per il primo passaggio di approvazione.

Scrivi l'artefatto canonico nella lingua di lavoro del responsabile. Questo template usa l'italiano: mantieni in inglese solo termini di marketing o business già consolidati, come `branded content`, `claim`, `brief` o `case study`. Non usare l'inglese per intestazioni, spiegazioni, etichette o stati generici. Adatta tabelle e titoli quando serve, ma conserva i campi tecnici in testa, le cinque aree di regole, la governance e le regole di composizione.

```markdown
---
artifact: marketing-foundations
version: 1
status: bozza
entity: "[Nome canonico dell'entità]"
entity_type: azienda | brand-autonomo | brand-figlio
scope: "[Perimetro stabile coperto]"
owner: "[Ruolo o responsabile autorizzato]"
last_reviewed: YYYY-MM-DD
business_context_path: "[Percorso dell'identità canonica]"
business_context_version: 1
parent_foundations_path: null
parent_foundations_version: null
---

# Fondamenti di marketing: [Entità]

## Come gli agenti applicano questo profilo

- Leggi l'identità di business indicata prima di questo profilo.
- Applica solo regole approvate nel perimetro dichiarato.
- Non trasformare decisioni irrisolte in regole.
- Per un brand figlio, leggi nell'ordine l'identità del genitore, l'identità del brand, i fondamenti del genitore e poi questa integrazione.
- Rendi visibili i conflitti rilevanti invece di risolverli in base all'ordine dei file.

## Marcatori di provenienza

- `[C]` confermato da un referente autorizzato
- `[S1]`, `[S2]`, ... supportato da una fonte elencata sotto
- `[I]` inferito e in attesa di conferma
- `[?]` sconosciuto o irrisolto

## Riferimenti di contesto

| Artefatto o autorità | Percorso o riferimento | Versione/data | Perimetro | Note |
|---|---|---|---|---|
| Identità di business | | | | |

## 1. Coerenza tra offerta, pubblico e situazione

| Riferimento all'offerta | Riferimento al pubblico | Situazione o risultato desiderato | Regola applicabile | Non adatto, esclusione o comportamento prudente | Base |
|---|---|---|---|---|---|
| | | | | | |

## 2. Messaggi, claim ed evidenze

| Messaggio o claim | Perimetro | Stato | Riferimento dell'evidenza | Qualificazione, approvazione o comportamento prudente | Base |
|---|---|---|---|---|---|
| | | approvato / condizionato / vietato | | | |

Per evidenza si intende una base esistente e verificabile, come una specifica, una policy, un dataset, uno studio, una certificazione, un case study approvato, una testimonianza autorizzata o una pagina aziendale approvata. Non inventare evidenze né richiedere un nuovo dossier di prove solo per completare la configurazione.

## 3. Ruolo di canali e formati

| Canale o formato | Ruolo stabile | Perimetro adatto | Limiti o uso improprio | Comportamento se non definito | Base |
|---|---|---|---|---|---|
| | | | | | |

## 4. Standard editoriali, visivi e di qualità

| Standard | Si applica a | Riferimento autorevole | Verifica richiesta o pratica vietata | Comportamento prudente | Base |
|---|---|---|---|---|---|
| | | | | | |

## 5. Controlli, autorità e approvazioni

| Attività o output | Livello di autorità | Verifiche richieste | Approvatore autorizzato | Limite di esecuzione o comportamento prudente | Base |
|---|---|---|---|---|---|
| | autonomo / solo proposta / vietato | | | | |

L'approvazione del contenuto non autorizza mai automaticamente a pubblicare, inviare, configurare, acquistare o spendere.

## Conflitti e risoluzioni

| Tema | Resoconti o regole in conflitto | Impatto | Risoluzione | Stato | Base |
|---|---|---|---|---|---|
| | | bloccante / non bloccante | | aperto / risolto | |

## Decisioni aperte

Usa solo: `non stabilito dalle fonti fornite`, `esiste ma non è disponibile`, `non definito`, `sconosciuto al referente` o `non applicabile`.

| Decisione o gap | Stato | Impatto | Comportamento prudente dell'agente | Responsabile o trigger di revisione | Base |
|---|---|---|---|---|---|
| | | bloccante / non bloccante | | | |

## Fonti

| ID | Fonte | Data di accesso o fornitura | Cosa supporta | Note d'uso o sensibilità |
|---|---|---|---|---|
| S1 | | | | |

## Trigger di revisione

| Cambiamento concreto | Regole interessate | Responsabile o prossima verifica |
|---|---|---|
| | | |

## Registro modifiche

- v1 (YYYY-MM-DD): Fondamenti di marketing iniziali approvati.
```

## Schema per scrivere una regola

Preferisci un'istruzione che cambi il comportamento:

> Per le email dedicate al rinnovo dei clienti esistenti, usa risultati di adozione documentati e non far intendere risparmi garantiti. Se il risultato citato è precedente alla versione corrente dell'offerta, chiedi una verifica dell'evidenza prima di usare il dato. `[C; S3]`

Evita note descrittive che lasciano implicita la decisione:

> I clienti sono interessati ai risparmi e l'email è importante.

Non ogni regola richiede una riga in tabella o tutti i campi possibili. Il criterio è che un altro agente riesca a riconoscere comportamento, perimetro, base e comportamento prudente senza inventare una decisione.

## Integrazione per un brand figlio

Per `entity_type: brand-figlio`:

- imposta `business_context_path` sull'identità del brand figlio e registra l'identità del genitore nei Riferimenti di contesto;
- imposta `parent_foundations_path` e `parent_foundations_version` sui fondamenti aziendali;
- includi solo sezioni e righe che aggiungono, restringono o specializzano esplicitamente le regole del genitore;
- non copiare regole aziendali immutate;
- mantieni aperto un conflitto rilevante finché un responsabile autorizzato non lo risolve.

## Preparazione per l'approvazione

Una bozza può essere approvata solo quando:

- l'identità indicata è approvata, leggibile e compatibile con il perimetro;
- tutte e cinque le aree hanno una regola supportata o un gap esplicitamente classificato;
- non resta aperto alcun conflitto bloccante;
- le autorità e le approvazioni essenziali sono definite;
- ogni gap non bloccante ha un comportamento prudente;
- nessun elemento `[I]` opera come regola;
- sono registrate fonti e trigger di revisione concreti.

All'approvazione, cambia `status` in `approvato`. Parti dalla versione `1`, incrementa l'intero per modifiche sostanziali e mantienilo per correzioni di solo refuso.
