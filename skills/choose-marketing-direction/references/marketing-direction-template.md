# Template della Direzione di marketing

Leggi questo riferimento quando crei, aggiorni o verifichi una direzione. Il template è modulare: conserva gli elementi che cambiano la scelta e non compilare righe vuote per simulare completezza.

```markdown
---
artifact: marketing-direction
version: 1
status: bozza
entity: "[Nome canonico]"
scope: "[Decisione coperta]"
owner: "[Responsabile autorizzato]"
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
challenge_path: ".agents/marketing/decisions/<decision-slug>/challenge.md"
challenge_version: 1
supersedes: null
superseded_by: null
---

# Direzione di marketing: [Titolo comprensibile]

## Come usare questa decisione

- Leggi il brief e i contesti che referenzia.
- Mantieni distinti decisione approvata, assunzioni e verifiche.
- Usa la direzione per definire il marketing mix, non come autorizzazione all'esecuzione.
- Non modificare silenziosamente la sfida o le regole stabili.

## Riferimenti

| Artefatto | Percorso | Versione/data | Stato | Note |
|---|---|---|---|---|
| Brief della sfida | | | | |
| Business Identity | | | | |
| Marketing Foundations | | | | |
| Contesto o integrazione del brand, se applicabile | | | | |

## Diagnosi strategica provvisoria

- **Tensione strategica centrale:**
- **Situazione osservata:**
- **Ipotesi causale:**
- **Clienti o pubblici, evidenze e incognite:**
- **Alternative, concorrenti o sostituti rilevanti:**
- **Capacità distintive e limiti dell'organizzazione:**
- **Incertezza decisiva:**
- **Perché il marketing può o non può incidere:**
- **Solidità e limiti della diagnosi:**

## Decisione da prendere

- **Sfida di riferimento:**
- **Risultato e cambiamento cercato:**
- **Responsabile della scelta:**
- **Criteri decisionali:**

## Alternative considerate

### Direzione A: [Nome]

- **Tesi:**
- **Pubblico e situazione:**
- **Cambiamento e meccanismo:**
- **Base disponibile:**
- **Assunzione decisiva:**
- **Trade-off e rinunce:**
- **Miglior argomento contrario:**
- **Risposta plausibile degli attori rilevanti:**
- **Capacità o autorità necessarie:**
- **Conseguenze indesiderate:**
- **Evidenza invalidante o condizione di stop:**
- **Implicazioni per il marketing mix:**

### Direzione B: [Nome]

[Conservare la stessa struttura solo per alternative reali.]

## Confronto

| Criterio | Direzione A | Direzione B | Conseguenza |
|---|---|---|---|
| | | | |

Non usare punteggi numerici senza un modello approvato e una base adeguata.

## Raccomandazione

- **Direzione raccomandata:**
- **Perché è preferibile adesso:**
- **Trade-off accettato:**
- **Che cosa non fare:**
- **Evidenza che cambierebbe la scelta:**
- **Evidenza che riaprirebbe la diagnosi:**

## Assunzione più fragile e primo test utile

- **Assunzione:**
- **Evidenza minima cercata:**
- **Metodo proposto:**
- **Regola per proseguire, correggere o fermarsi:**
- **Condizione per riaprire la diagnosi:**
- **Limiti e autorizzazioni:**

## Dipendenze e aspetti aperti

| Tema | Stato | Impatto | Proprietario | Comportamento prudente |
|---|---|---|---|---|
| | bloccante / non bloccante | | | |

## Stato della decisione

- **Stato:** bozza / approvata / superata
- **Approvata da:**
- **Data dell'approvazione:**
- **Passaggio successivo normale:** `define-marketing-mix`

## Fonti specifiche

| ID | Fonte | Data | Cosa sostiene | Limiti |
|---|---|---|---|---|
| S1 | | | | |

## Registro modifiche

- v1 (YYYY-MM-DD): prima direzione approvata.
```

## Criterio di approvazione

La direzione può diventare `approvata` quando:

- il brief è confermato, leggibile e non superato;
- la diagnosi distingue osservazioni, interpretazioni, ipotesi causali e incertezze;
- la diagnosi considera in modo proporzionato pubblico, alternative e capacità dell'organizzazione;
- la decisione e i criteri sono comprensibili;
- le alternative sono strategicamente differenti o è motivata l'assenza di alternative;
- le alternative plausibili sono state sottoposte a uno stress test materiale;
- la raccomandazione esplicita trade-off, rinunce, non-scelte e condizioni di stop;
- fatti, inferenze e assunzioni restano distinguibili;
- l'assunzione più fragile e il primo test utile sono formulati senza autorizzare l'esecuzione;
- è chiaro quando il test conferma, corregge, ferma o riapre la diagnosi;
- le implicazioni sulle quattro P sono visibili senza anticipare il mix;
- non resta un conflitto bloccante o una decisione esterna mascherata;
- il responsabile ha approvato contenuto e salvataggio.

Se il contenuto è approvato soltanto in chat, riporta `contenuto approvato in chat; artefatto non creato`. Non assegnare uno stato canonico a un file inesistente.

## Percorso e versioning

Usa `direction.md` nello stesso fascicolo di `challenge.md`. La direzione referenzia la versione esatta del brief, ma non lo sostituisce. Se il brief viene modificato in modo sostanziale, verifica e aggiorna la direzione prima di riusarla.
