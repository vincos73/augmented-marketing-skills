# Report del forward test old-vs-candidate

Data: 2026-08-27

## Verdetto

Entrambe le candidate superano la soglia sintetica definita nel protocollo.

- `setup-business-context` v0.6.3: **+0,67 punti su 5** rispetto alla v0.6.2.
- `setup-marketing-system` v0.3.0: **+0,83 punti su 5** rispetto alla v0.2.1.
- Gap aggregato non ponderato: **+0,75 punti su 5**.
- Preferenze cieche: **12 su 12** per la candidata, inclusi tutti i passaggi con ordine A/B invertito.
- Hard fail: **0** per controlli e candidate.

Il risultato corregge i problemi bersaglio osservati nel retest precedente. Non costituisce una validazione con utenti reali e non autorizza claim pubblici di efficacia.

## Cambiamenti sottoposti al test

### Business v0.6.3

- una domanda deve riguardare una decisione principale;
- privacy, pagatore e approvazione claim non devono essere accorpati se richiedono percorsi diversi;
- quando percorso o versione sono proposti, la risposta deve chiarire che nulla è stato salvato o installato.

### Marketing v0.3.0

- nuovo registro privato di riconciliazione: regola stabile, conflitto, gap, elemento temporaneo rinviato o istruzione incorporata respinta;
- conservazione di alternative reali e divieti identitari che cambiano il comportamento di marketing;
- conflitti temporanei visibili e indirizzati al brief pertinente senza diventare Fondamenti permanenti;
- divieto di ripetere domande sulla disponibilità di materiali già classificati;
- contratto della prima revisione con tetto di 650 parole e controllo della perdita di significato.

## Risultati per dimensione

### `setup-business-context`

| Dimensione | Controllo v0.6.2 | Candidata v0.6.3 | Gap |
|---|---:|---:|---:|
| Qualità strategica | 4,00 | 4,83 | +0,83 |
| Disciplina delle evidenze | 4,83 | 5,00 | +0,17 |
| Utilità decisionale | 3,83 | 5,00 | +1,17 |
| Perimetro e autorità | 4,17 | 5,00 | +0,83 |
| Chiarezza | 4,83 | 5,00 | +0,17 |
| Proporzione | 4,00 | 4,83 | +0,83 |
| **Media** | **4,28** | **4,94** | **+0,67** |

### `setup-marketing-system`

| Dimensione | Controllo v0.2.1 | Candidata v0.3.0 | Gap |
|---|---:|---:|---:|
| Qualità strategica | 3,83 | 5,00 | +1,17 |
| Disciplina delle evidenze | 4,00 | 5,00 | +1,00 |
| Utilità decisionale | 3,33 | 4,83 | +1,50 |
| Perimetro e autorità | 4,33 | 4,83 | +0,50 |
| Chiarezza | 4,67 | 5,00 | +0,33 |
| Proporzione | 4,33 | 4,83 | +0,50 |
| **Media** | **4,08** | **4,92** | **+0,83** |

La dimensione che aveva mostrato il problema maggiore, utilità decisionale del marketing, passa da 3,33 a 4,83 nel campione sintetico.

## Risultati per fixture

| Fixture | Controllo | Candidata | Gap |
|---|---:|---:|---:|
| B1, separazione delle decisioni | 4,25 | 5,00 | +0,75 |
| B2, materiale non disponibile | 4,33 | 4,92 | +0,58 |
| B3, gerarchia e autorità | 4,25 | 4,92 | +0,67 |
| M1, conflitto temporaneo | 3,83 | 5,00 | +1,17 |
| M2, fonti già classificate | 4,33 | 4,75 | +0,42 |
| M3, alternative e autorità | 4,08 | 5,00 | +0,92 |

## Lunghezza

| Fixture | Controllo, parole | Candidata, parole |
|---|---:|---:|
| B1 | 274 | 288 |
| B2 | 262 | 304 |
| B3 | 293 | 249 |
| M1 | 478 | 468 |
| M2 | 437 | 459 |
| M3 | 434 | 465 |

Tutti gli output rispettano i limiti. Il miglioramento non dipende da un aumento sistematico della lunghezza: in B3 e M1 la candidata è più corta.

## Criticità e residui

- Soft fail business: controllo 8, candidata 1.
- Soft fail marketing: controllo 13, candidata 1.
- Nessun hard fail.
- B3 candidata: una formulazione può confondere il responsabile sicurezza con l'approvatore delle affermazioni sulla sicurezza.
- M2 candidata: una domanda accorpa responsabile dei Fondamenti e percorso dell'identità. È il principale residuo di chiarezza decisionale.

Non aggiungiamo altre regole universali sulla base di questi due episodi. Vanno osservati in un pilot reale e in futuri eval prima di ampliare ancora le istruzioni.

## Metodo e limiti

Il test usa sei fixture nuove, sintetiche e pubblicabili. Per ogni fixture, controllo e candidata sono stati generati da agenti separati. Dodici valutatori distinti, descritti come marketer strategici senior con almeno 15 anni di esperienza, hanno giudicato coppie anonime con ordine invertito.

La generazione con agenti separati riduce la contaminazione tra versioni ma introduce varianza tra generatori. Il controbilanciamento controlla il bias d'ordine della valutazione, non la varianza di generazione. Il campione resta piccolo e costruito attorno a invarianti noti.

Non sono stati coinvolti marketer reali. Non sono stati misurati tempo di lavoro, correzioni in contesti autentici, adozione, qualità percepita o risultati di business. Non sono stati usati dati o casi reali di Vincos.

## Tracciabilità

- [`protocol.md`](./protocol.md)
- [`rubric.md`](./rubric.md)
- [`source-manifest.md`](./source-manifest.md)
- [`fixtures/`](./fixtures/)
- [`outputs/`](./outputs/)
- [`blind-packets/`](./blind-packets/)
- [`mapping.md`](./mapping.md), non fornita ai valutatori
- [`evaluations/scores.csv`](./evaluations/scores.csv)
- [`evaluations/observations.md`](./evaluations/observations.md)
- [`evaluations/agents.md`](./evaluations/agents.md)
- [`generators.md`](./generators.md)

Le versioni candidate sono presenti soltanto nella sorgente. Non sono state installate, pubblicate, committate o inviate a un remote.
