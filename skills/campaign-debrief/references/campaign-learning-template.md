# Template del Campaign Learning

Leggi questo riferimento quando il responsabile vuole condividere, approvare o conservare la lettura dei risultati. Il template è una libreria di campi, non un indice da riprodurre integralmente. Mantieni un solo record per campagna e aggiorna lo storico senza creare file separati per canale, metrica o riunione.

Scrivi nella lingua di lavoro del responsabile. La sintesi in chat non deve mostrare il frontmatter.

```markdown
---
artifact: campaign-learning
version: 1
status: bozza
entity: "[Azienda o brand]"
campaign: "[Nome della campagna]"
scope: "[Periodo, pubblico, canali, asset o fasi coperti]"
owner: "[Responsabile autorizzato]"
entry_mode: standalone | collegata
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
campaign_spec_path: null
campaign_spec_version: null
campaign_review_path: null
campaign_review_version: null
observation_cutoff: YYYY-MM-DD
supersedes: null
superseded_by: null
---

# Campaign Learning: [Titolo]

## Decisione e perimetro

- **Decisione da prendere:**
- **Perimetro osservato:**
- **Finestra:**
- **Responsabile:**
- **Costo o reversibilità della scelta:**

## Base utilizzata

| ID | Fonte | Data/finestra | Cosa sostiene | Limiti |
|---|---|---|---|---|
| S1 | | | | |

## Atteso ed eseguito

| Elemento | Atteso prima dell'esecuzione | Eseguito realmente | Conseguenza sulla lettura |
|---|---|---|---|
| Pubblico, offerta, percorso, canale, asset, budget, follow-up o tracking | | | |

Non riscrivere la previsione originaria sulla base del risultato. Registra le divergenze materiali e il momento in cui sono avvenute.

## Risultati osservati

| Livello | Segnale | Valore | Definizione e denominatore | Fonte | Finestra | Limiti |
|---|---|---:|---|---|---|---|
| output / comportamento / business | | | | | | |

## Lettura sostenuta

- **Che cosa i dati sostengono:**
- **Che cosa non sostengono:**
- **Solidità per la decisione:** sufficiente / indicativa per un passo reversibile / insufficiente per la scelta richiesta
- **Perimetro a cui si applica:**

## Limiti e spiegazioni alternative

| Limite o spiegazione | Evidenza disponibile | Come può cambiare la decisione | Osservazione utile |
|---|---|---|---|
| | | | |

## Decisione raccomandata

- **Raccomandazione:** continuare / correggere / estendere con cautela / fermare / attendere / confrontare / riaprire
- **Perimetro:**
- **Motivo:**
- **Condizioni e limiti:**
- **Azione:**
- **Responsabile autorizzato:**
- **Prossima osservazione:**
- **Data o finestra del controllo:**
- **Criterio che cambierà la decisione:**

## Proposte non applicate

| Destinazione | Aggiornamento proposto | Evidenza | Autorità o workflow richiesto | Stato |
|---|---|---|---|---|
| Campaign Spec / direzione / Marketing Foundations / playbook | | | | proposta, non applicata |

## Approvazione e autorizzazioni

- **Lettura approvata da:**
- **Data:**
- **Punti aperti accettati:**
- **Salvataggio autorizzato:** sì / no
- **Modifiche operative autorizzate:** nessuna, salvo evidenza separata

## Registro modifiche

- v1 (YYYY-MM-DD): prima lettura approvata.
```

## Criterio di approvazione

Il record può diventare `approvato` quando:

- decisione, perimetro e finestra sono espliciti;
- atteso, eseguito e osservato non sono confusi;
- metriche decisive hanno definizione, fonte e limiti adeguati;
- conclusioni e causalità sono proporzionate;
- raccomandazione, responsabile e prossima verifica sono utilizzabili;
- proposte verso altri artefatti restano distinte dalle modifiche applicate;
- il responsabile approva la lettura e autorizza separatamente il salvataggio.

## Percorso e versioning

Usa:

```text
.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/campaign-learning.md
```

- Prima approvazione: `version: 1`, `status: approvato` e data corrente.
- Nuova finestra o decisione sostanziale: incrementa la versione intera e conserva il confronto con la lettura precedente.
- Correzione di un refuso o collegamento: conserva la versione e aggiorna il registro.
- Perimetro materialmente diverso: crea un nuovo fascicolo di campagna, non un file per canale.
- Lettura sostituita: imposta `status: superata` e indica `superseded_by`.

Se il contenuto è approvato soltanto in chat, riporta `contenuto approvato in chat; artefatto non creato`. Durante test, simulazioni ed eval non scrivere nei percorsi canonici.
