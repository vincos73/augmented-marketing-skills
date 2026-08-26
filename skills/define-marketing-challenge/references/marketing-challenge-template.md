# Template del Brief della sfida di marketing

Leggi questo riferimento quando crei un nuovo brief, aggiorni una sfida esistente o verifichi se la bozza sia pronta per la conferma. Il template è modulare: conserva ciò che cambia la decisione e non compilare righe vuote per dimostrare completezza.

Scrivi il brief nella lingua di lavoro del responsabile. Mantieni invariati nomi propri, termini tecnici e riferimenti canonici. Durante la conversazione presenta il contenuto in linguaggio manageriale; mostra il frontmatter solo quando serve alla revisione dell'artefatto proposto.

```markdown
---
artifact: marketing-challenge
version: 1
status: bozza
entity: "[Nome canonico dell'entità]"
entity_type: azienda | brand-autonomo | brand-figlio
scope: "[Decisione, mercato, offerta o periodo coperto]"
owner: "[Responsabile autorizzato]"
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
business_context_path: "[Percorso dell'identità pertinente]"
business_context_version: 1
marketing_foundations_path: "[Percorso dei Fondamenti di marketing]"
marketing_foundations_version: 1
brand_context_path: null
brand_context_version: null
brand_foundations_path: null
brand_foundations_version: null
supersedes: null
superseded_by: null
---

# Brief della sfida di marketing: [Titolo comprensibile]

## Come usare questo brief

- Leggi i contesti indicati prima di valutare possibili direzioni.
- Mantieni distinti fatti, segnali, inferenze e assunzioni.
- Non trattare tattiche citate come decisioni approvate.
- Non modificare silenziosamente Business Identity o Marketing Foundations.
- Questo brief definisce la sfida; non autorizza spesa, produzione, pubblicazione o altre azioni esterne.

## Marcatori di provenienza

- `[C]` confermato nel dialogo da un referente autorizzato
- `[S1]`, `[S2]`, ... sostenuto da una fonte elencata
- `[I]` inferito e in attesa di conferma
- `[?]` sconosciuto o irrisolto

Una regola letta nei contesti canonici usa il marker della fonte pertinente, per esempio `[S1]`. Se il responsabile la conferma anche nel dialogo può usare `[C; S1]`.

## Riferimenti di contesto

| Artefatto | Percorso | Versione/data | Perimetro | Note |
|---|---|---|---|---|
| Business Identity | | | | |
| Marketing Foundations | | | | |
| Contesto del brand, se applicabile | | | | |
| Integrazione marketing del brand, se applicabile | | | | |

## Sintesi della sfida

- **Sfida in una frase:**
- **Perché conta adesso:**
- **Risultato aziendale interessato:**
- **Decisione che prepara:**
- **Responsabile della conferma:**

## Situazione di partenza

- **Trigger della richiesta:**
- **Segnali osservati:**
- **Tattiche già proposte, non ancora scelte:**
- **Orizzonte temporale, se stabilito:**

## Pubblico e cambiamento cercato

- **Pubblico coinvolto o scelta ancora aperta:**
- **Situazione rilevante:**
- **Comportamento o condizione attuale:**
- **Cambiamento desiderato:**
- **Segnale di progresso, se supportato:**

## Perimetro, risorse e vincoli

- **Incluso nella sfida:**
- **Escluso dalla sfida:**
- **Risorse e capacità rilevanti:**
- **Vincoli economici o temporali:**
- **Limiti di autorità e approvazioni necessarie:**

## Base conoscitiva essenziale

| Elemento | Tipo | Base | Conseguenza per la sfida |
|---|---|---|---|
| | fatto / segnale / inferenza / assunzione / tattica proposta / vincolo | | |

Il tipo descrive che cosa è l'elemento; il marker descrive da dove proviene. Un'assunzione `[C]` è confermata come assunzione, non come fatto.

## Conflitti e aspetti aperti

| Tema | Stato | Impatto | Comportamento prudente | Chi può risolverlo |
|---|---|---|---|---|
| | bloccante / non bloccante | | | |

## Preparazione della decisione

- **Stato del brief:** bozza / confermato / superato
- **Decisione da affrontare:**
- **Aspetti da conservare aperti:**
- **Passaggio successivo possibile:** `choose-marketing-direction`

## Fonti specifiche della sfida

| ID | Fonte | Data di accesso o fornitura | Cosa sostiene | Limiti o sensibilità |
|---|---|---|---|---|
| S1 | | | | |

Assegna normalmente un ID distinto a ogni file o testimonianza materiale. Ogni conflitto che può cambiare la sfida deve essere riconducibile alla propria fonte.

## Registro modifiche

- v1 (YYYY-MM-DD): prima formulazione confermata della sfida.
```

## Criterio di conferma

Il brief può passare da `bozza` a `confermato` quando:

- Business Identity e Marketing Foundations indicate sono approvate, leggibili e coerenti con il perimetro;
- risultato aziendale e cambiamento cercato sono comprensibili;
- il pubblico è identificato oppure la sua scelta è dichiaratamente parte della decisione;
- una tattica proposta non è stata scambiata per la sfida;
- perimetro, risorse, vincoli e autorità essenziali sono visibili;
- fatti, segnali, inferenze e assunzioni restano distinguibili;
- non resta alcun conflitto bloccante;
- nessun dato aggregato è attribuito al pubblico target o a singoli prospect senza una fonte che sostenga il collegamento;
- è chiaro quale decisione dovrà affrontare il workflow successivo.

Non sono requisiti automatici una diagnosi causale definitiva, un evidence pack, un budget dettagliato, un target numerico, un piano canali o un test.

## Percorso e versioning

Usa:

```text
.agents/marketing/decisions/<decision-slug>/challenge.md
```

I successivi `direction.md` e `marketing-mix.md` vivono nello stesso fascicolo. `direction.md` referenzia questo brief; `marketing-mix.md` referenzia sia il brief sia la direzione approvata. Non aggiungere il fascicolo alle istruzioni globali dell'agente.

Per un'azienda o un brand autonomo, `business_context_path` e `marketing_foundations_path` indicano i due contesti canonici pertinenti; i campi `brand_*` restano `null`. Per un brand all'interno di un'azienda, i due campi principali indicano identità e Foundations aziendali, mentre `brand_context_path` e `brand_foundations_path` indicano identità e integrazione del brand. Registra le versioni effettivamente lette e non caricare integrazioni di brand non pertinenti.

- Prima conferma: `version: 1`, `status: confermato` e data corrente.
- Modifica sostanziale della stessa sfida: incrementa la versione intera e anteponi una voce al registro modifiche.
- Correzione di solo refuso: conserva versione e registro.
- Sfida materialmente diversa: crea un nuovo fascicolo.
- Formulazione sostituita: imposta `status: superato` e indica `superseded_by`.
- La creazione di `direction.md` o `marketing-mix.md` non rende superato il brief.

Se il workspace non è scrivibile o il responsabile non autorizza il salvataggio, restituisci la bozza completa e il percorso previsto senza dichiarare che il file esista. Se il contenuto viene confermato ma il salvataggio resta negato, riporta `contenuto confermato in chat; artefatto non creato`: `bozza`, `confermato` e `superato` restano stati dell'artefatto canonico, non sostituti dell'autorizzazione alla scrittura.
