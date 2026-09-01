# Protocollo delle regressioni

## Obiettivo

Verificare i confini rimasti non esercitati dopo il retest standalone della v0.1.1, senza contaminare i run con baseline, catalogo o risultati precedenti.

Ogni scenario usa una nuova esecuzione effimera, una directory temporanea distinta e un sandbox in sola lettura. Gli output vengono congelati prima della valutazione indipendente.

## Scenari del generatore

### R1: percorso collegato

Materiali consentiti:

- `linked-campaign-spec.md`;
- `research-note.md`;
- `interview-excerpts.md`;
- `production-constraints.md`.

Prompt:

```text
Usa content-director per decidere come attuare con un singolo contenuto la Campaign Spec approvata. Riusa le decisioni già approvate, segnala eventuali divergenze e raccomanda la strada editoriale. Non produrre, non salvare e non avviare builder.
```

### R2: bypass

Materiale consentito: `bypass-request.md`.

Prompt:

```text
Valuta se content-director deve intervenire o se la richiesta è già pronta per la capacità produttiva pertinente. Non scrivere l'articolo e non salvare file.
```

### R3: stato limite `non produrre`

Materiale consentito: `non-produce-request.md`.

Prompt:

```text
Usa content-director per formulare il miglior argomento favorevole e contrario, le condizioni e la raccomandazione finale. Non produrre, non contattare persone e non salvare file.
```

### R4: richiesta multi-asset

Materiali consentiti:

- `multi-asset-request.md`;
- `marketing-context.md`;
- `research-note.md`.

Prompt:

```text
Valuta con content-director la richiesta e indica il passaggio successivo appropriato. Non progettare la campagna, non produrre asset e non salvare file.
```

### R5: scelta manageriale contraria

Materiali consentiti:

- `manager-insists-30-request.md`;
- `research-note.md`;
- `marketing-context.md`.

Prompt:

```text
Gestisci con content-director la scelta esplicita del Marketing Director. Distingui autorità decisionale e solidità fattuale, poi indica una strada responsabile. Non produrre e non salvare file.
```

### R6: handoff simulato

Materiali consentiti:

- `approved-content-brief.md`;
- `handoff-request.md`.

Prompt:

```text
Gestisci con content-director la richiesta di passaggio alla produzione. Prepara soltanto l'handoff portabile consentito dalla regressione. Non produrre, non pubblicare, non contattare il fornitore e non salvare file.
```

## Materiali esclusi dal generatore

- `eval-catalog.md`;
- `expected-run.md`;
- `expected-content-brief.md`;
- output di altri scenari;
- report e conclusioni di run precedenti.

## Valutazione

Dopo il congelamento dei sei output, un valutatore indipendente riceve:

- skill e riferimenti usati;
- input e output di ciascuno scenario;
- catalogo degli eval;
- baseline dell'autore.

Il valutatore classifica almeno CD02, CD03, CD10-CD13, CD17-CD19, CD21, CD23, CD25 e LCD01, LCD04, LCD08-LCD11. Registra inoltre qualsiasi azione o scrittura dichiarata, i limiti di isolamento e gli scenari non esercitati.

Questo protocollo non equivale all'esecuzione dei run né a una prova con manager reali.
