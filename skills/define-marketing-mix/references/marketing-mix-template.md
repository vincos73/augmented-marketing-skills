# Template del Marketing Mix

Leggi questo riferimento quando crei, aggiorni o verifichi il marketing mix. Copri le quattro P e indica lo stato di ciascuna scelta. Compila percorsi e versioni con i riferimenti effettivi; lascia `null` i valori assenti e descrivi nelle fonti l'eventuale conferma ricevuta in chat.

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
challenge_path: null
challenge_version: null
direction_path: null
direction_version: null
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

| Materiale utilizzato | Percorso o riferimento in chat | Versione/data disponibile | Stato | Note |
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

| P | Scelta o vincolo | Stato | Base | Chi decide | Condizioni e uso previsto |
|---|---|---|---|---|---|
| Product | | | | | |
| Price | | | | | |
| Place | | | | | |
| Promotion | | | | | |

Ripeti la P per ogni scelta distinta che contiene. Usa uno stato per scelta tra `vincolo approvato`, `scelta approvata`, `scelta da definire`, `proposta`, `ipotesi da verificare`, `decisione esterna` e `non applicabile`.

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

Per i punti ereditati, distingui informazione non disponibile, decisione rinviata e scelta esplicita di non fissare un numero; indica prima di quale passaggio serviranno. Non equivalgono a zero, nessun obiettivo o consenso e non riaprono risposte esplicite senza un nuovo conflitto.

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
- la mappa copre le quattro P e ogni scelta materiale ha un proprio stato giustificato;
- le scelte materiali sostengono la stessa direzione e le tensioni sono visibili;
- Product non maschera una roadmap tecnica non autorizzata;
- Price non presenta come approvato un prezzo privo di autorità o base;
- Place distingue distribuzione e accesso dai canali di comunicazione;
- Promotion definisce il ruolo strategico senza anticipare il piano di campagna;
- decisioni esterne, proprietari e dipendenze bloccanti sono riconoscibili;
- fatti, assunzioni e fonti restano distinguibili;
- il responsabile ha approvato il contenuto per il perimetro indicato. Le decisioni ancora aperte conservano il proprio stato e le relative condizioni d'uso.

Se il contenuto è approvato soltanto in chat, riporta `contenuto approvato in chat; artefatto non creato`. Il titolo del riepilogo in chat descrive l'aggiornamento, senza un nuovo numero di versione. Puoi ricordare l'ultima versione del file letta o riferita.

## Percorso e versioning

Quando il salvataggio è autorizzato, usa `marketing-mix.md` nel fascicolo della decisione. Riferisci sfida e direzione ai file reali oppure al brief equivalente e alle conferme in chat. Un aggiornamento sostanziale a una scelta richiede di verificare gli effetti sulle scelte collegate e incrementare la versione del mix.
