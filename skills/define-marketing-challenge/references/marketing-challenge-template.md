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
business_context_path: null
business_context_version: null
marketing_foundations_path: null
marketing_foundations_version: null
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

| Documento o conferma | Percorso o provenienza | Versione/data, se nota | Perimetro | Note |
|---|---|---|---|---|
| | | | | |

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

Per i punti ereditati, distingui informazione non disponibile, decisione rinviata e scelta esplicita di non fissare un numero; indica prima di quale passaggio serviranno. Non equivalgono a zero, nessun obiettivo o consenso e non riaprono risposte esplicite senza un nuovo conflitto.

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

- l'entità e le regole applicabili sono identificate nei contesti della suite, in materiali aziendali equivalenti o nella sintesi del responsabile;
- risultato aziendale e cambiamento cercato sono comprensibili;
- il pubblico è identificato oppure la sua scelta è dichiaratamente parte della decisione;
- una tattica proposta non è stata scambiata per la sfida;
- perimetro, risorse, vincoli e autorità essenziali sono visibili;
- fatti, segnali, inferenze e assunzioni restano distinguibili;
- non resta alcun conflitto bloccante;
- nessun dato aggregato è attribuito al pubblico target o a singoli prospect senza una fonte che sostenga il collegamento;
- è chiaro quale decisione dovrà affrontare il workflow successivo e il decisore ha confermato questa formulazione, nel brief o in chat.

Non sono requisiti automatici una diagnosi causale definitiva, un evidence pack, un budget dettagliato, un target numerico, un piano canali o un test.

## Percorso e versioning

In assenza di una destinazione richiesta, usa:

```text
.agents/marketing/decisions/<decision-slug>/challenge.md
```

I successivi `direction.md` e `marketing-mix.md` vivono nello stesso fascicolo. `direction.md` referenzia questo brief; `marketing-mix.md` referenzia sia il brief sia la direzione approvata. Non aggiungere il fascicolo alle istruzioni globali dell'agente.

Compila i campi di percorso e versione dei contesti della suite solo per i file pertinenti realmente usati e le versioni note. Per un brand figlio i campi principali si riferiscono al genitore e i campi `brand_*` alle integrazioni del brand. Mantieni `null` negli altri campi. Nei riferimenti identifica i materiali aziendali equivalenti con titolo, percorso o URL se disponibile, e versione o data se nota. Per una conferma in chat riporta il ruolo del decisore e ciò che ha confermato, conservando nel brief i vincoli necessari a riprendere il lavoro.

- Prima conferma: `version: 1`, `status: confermato` e data corrente.
- Modifica sostanziale della stessa sfida: incrementa la versione intera e anteponi una voce al registro modifiche.
- Correzione di solo refuso: conserva versione e registro.
- Sfida materialmente diversa: crea un nuovo fascicolo.
- Formulazione sostituita: imposta `status: superato` e indica `superseded_by`.
- La creazione di `direction.md` o `marketing-mix.md` non rende superato il brief.

Se il workspace non è scrivibile o il responsabile vuole soltanto la risposta in chat, restituisci la formulazione completa. Per una conferma ricevuta nel dialogo usa lo stato `contenuto confermato in chat; artefatto non creato`. Per una conferma documentata cita il decisore e il brief esterno, con versione solo se presente nella fonte. Una consegna in chat lascia il nuovo documento senza file e senza versione.
