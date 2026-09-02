# Template del Marketing Mix

Leggi questo riferimento quando crei, aggiorni o verifichi il marketing mix. Il template è modulare: ogni P deve avere uno stato esplicito, ma il dettaglio dipende dalla decisione.

```markdown
---
artifact: marketing-mix
version: 1
status: bozza
entity: "[Nome canonico]"
scope: "[Decisione, offerta, mercato o periodo coperto]"
owner: "[Responsabile autorizzato]"
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
challenge_path: ".agents/marketing/decisions/<decision-slug>/challenge.md"
challenge_version: 1
direction_path: ".agents/marketing/decisions/<decision-slug>/direction.md"
direction_version: 1
supersedes: null
superseded_by: null
---

# Marketing Mix: [Titolo comprensibile]

## Come usare questo mix

- Leggi sfida, direzione e contesti referenziati.
- Usa le quattro P come scelte collegate, non come checklist indipendenti.
- Mantieni distinti vincoli, decisioni approvate, proposte, ipotesi e decisioni esterne.
- Questo documento non autorizza modifiche operative, spesa o pubblicazione.

## Riferimenti

| Artefatto | Percorso | Versione/data | Stato | Note |
|---|---|---|---|---|
| Brief della sfida | | | | |
| Direzione di marketing | | | | |
| Business Identity | | | | |
| Marketing Foundations | | | | |
| Contesto o integrazione del brand, se applicabile | | | | |

## Base strategica

- **Direzione approvata:**
- **Pubblico e situazione:**
- **Cambiamento e posizionamento:**
- **Assunzione strategica più fragile:**
- **Vincoli trasversali:**

## Mappa delle quattro P

| P | Stato | Scelta o vincolo | Base | Autorità | Implicazioni |
|---|---|---|---|---|---|
| Product | | | | | |
| Price | | | | | |
| Place | | | | | |
| Promotion | | | | | |

Usa come stato: `vincolo approvato`, `scelta da definire`, `proposta`, `ipotesi da verificare`, `decisione esterna` oppure `non applicabile`.

## Product

- **Configurazione dell'offerta:**
- **Esperienza, servizio o packaging:**
- **Che cosa resta invariato:**
- **Dipendenze da Product, Operations o altre funzioni:**

## Price

- **Logica di valore e prezzo:**
- **Architettura e condizioni:**
- **Che cosa resta invariato:**
- **Dipendenze economiche e autorità:**

## Place

- **Modalità di accesso, acquisto o distribuzione:**
- **Disponibilità ed erogazione:**
- **Che cosa resta invariato:**
- **Partner e dipendenze operative:**

## Promotion

- **Ruolo strategico della comunicazione:**
- **Territorio di valore e prove:**
- **Sequenza generale dell'attivazione:**
- **Vincoli da passare al Campaign Core:**

## Coerenza e tensioni

| Relazione | Valutazione | Tensione o rischio | Decisione necessaria |
|---|---|---|---|
| Product ↔ Price | | | |
| Product ↔ Place | | | |
| Price ↔ Place | | | |
| Promotion ↔ Product | | | |
| Promotion ↔ Place | | | |

## Assunzioni e verifiche

| Assunzione | P interessate | Base | Verifica proposta | Regola decisionale |
|---|---|---|---|---|
| | | | | |

## Dipendenze, autorità e aspetti aperti

| Tema | Stato | Impatto | Proprietario | Comportamento prudente |
|---|---|---|---|---|
| | bloccante / non bloccante | | | |

## Stato e passaggio successivo

- **Stato:** bozza / approvato / superato
- **Approvato da:**
- **Data dell'approvazione:**
- **Attivazioni possibili:**
- **Passaggio Promotion possibile:** `design-campaign`

## Fonti specifiche

| ID | Fonte | Data | Cosa sostiene | Limiti |
|---|---|---|---|---|
| S1 | | | | |

## Registro modifiche

- v1 (YYYY-MM-DD): primo marketing mix approvato.
```

## Criterio di approvazione

Il mix può diventare `approvato` quando:

- la direzione è approvata, leggibile e compatibile con la sfida vigente;
- tutte le quattro P hanno uno stato esplicito;
- le scelte materiali sostengono la stessa direzione e le tensioni sono visibili;
- Product non maschera una roadmap tecnica non autorizzata;
- Price non presenta come approvato un prezzo privo di autorità o base;
- Place distingue distribuzione e accesso dai canali di comunicazione;
- Promotion definisce il ruolo strategico senza anticipare il piano di campagna;
- decisioni esterne, proprietari e dipendenze bloccanti sono riconoscibili;
- fatti, assunzioni e fonti restano distinguibili;
- il responsabile ha approvato contenuto e salvataggio.

Se il contenuto è approvato soltanto in chat, riporta `contenuto approvato in chat; artefatto non creato`. Non assegnare uno stato canonico a un file inesistente.

## Percorso e versioning

Usa `marketing-mix.md` nello stesso fascicolo di `challenge.md` e `direction.md`. Referenzia le versioni esatte di entrambi. Un aggiornamento sostanziale a una P richiede di verificare gli effetti sulle altre e incrementare la versione del mix.
