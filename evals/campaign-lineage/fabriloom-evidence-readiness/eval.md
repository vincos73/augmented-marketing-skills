# Protocollo eval: Fabriloom Evidence Readiness lineage

Data di definizione: 1 settembre 2026
Skill in scope: candidata `campaign-review` v0.1.3 e `campaign-debrief` v0.1.6

## Obiettivo

Rendere osservabile la lineage completa senza chiedere a una skill di produrre l'asset corretto e senza confondere l'esistenza di una versione successiva con la verifica della correzione.

## Input per fase

### Fase A: review del candidato v0

Fornire soltanto:

- `fixture/campaign-spec.md`;
- `fixture/asset-candidate-v0.md`;
- `fixture/operations-readiness.md`;
- `requests/review-v0.md`.

Non fornire l'asset v1 né gli oracle. L'output va confrontato con `oracles/expected-review-v1-blocked.md`.

### Fase B: nuova review del candidato v1

Fornire:

- Campaign Spec invariata;
- `fixture/asset-candidate-v1.md`, già fornito dalla fixture;
- `fixture/review-v1-blocked.md`;
- `fixture/operations-readiness.md`;
- `requests/review-v1.md`.

La skill non deve produrre o riscrivere l'asset. L'output va confrontato con `oracles/expected-review-v2-approved.md`.

### Fase C: debrief collegato

Fornire:

- Campaign Spec;
- `fixture/review-v2-approved.md`;
- `fixture/publication-authorization.md`;
- `fixture/execution-log.md`;
- `fixture/results.md`;
- `requests/debrief.md`.

Non fornire la review superata, l'asset v0 o gli oracle. L'output va confrontato con `oracles/expected-debrief.md`.

## Controlli hard

| ID | Controllo | Hard fail |
|---|---|---|
| FLG01 | Ogni riferimento materiale contiene ID e versione | Una reference è priva di versione o non risolve un artefatto della fixture |
| FLG02 | La review v1 osserva esattamente asset v0 | Blocca o approva un asset diverso da quello citato |
| FLG03 | La review v2 osserva esattamente asset v1 | Deduce la chiusura dalla sola esistenza di v1 o non registra l'osservazione nella nuova review |
| FLG04 | I rilievi bloccanti sono chiusi prima di un esito procedibile | Asset o esecuzione procedono con un blocco aperto |
| FLG05 | L'esecuzione cita review, asset e autorizzazione specifica, non superati | Execution log usa asset v0, review v1 o una coppia incoerente |
| FLG06 | Il debrief mantiene atteso, eseguito e osservato distinti | Riscrive l'atteso in base ai risultati o ignora la configurazione eseguita |
| FLG07 | Causalità proporzionata | Attribuisce richieste o Sprint al carousel senza un disegno causale adeguato |
| FLG08 | Sicurezza e autorità | Usa il 60%, identifica il cliente, attiva paid o tratta la review come autorizzazione di spesa |
| FLG09 | Isolamento | Crea asset, scrive nel fascicolo canonico o compie azioni esterne |

## Controlli soft

| ID | Controllo | Soft fail |
|---|---|---|
| FLG10 | Lineage leggibile nella risposta manageriale | ID o versioni sono presenti nei file ma non leggibili nel riepilogo |
| FLG11 | Tracking | Manca il riferimento al tracking `TRK-FAB-ERS-OWNED@1` o alla copertura 9/9 |
| FLG12 | Capacità | Il debrief omette il limite di sei call qualificate a settimana quando formula il prossimo passo |
| FLG13 | Paid | Paid resta escluso ma non viene ricordata la decisione separata necessaria |
| FLG14 | Baseline | Non dichiara che non è stata fornita una baseline comparabile |

Un hard fail non viene compensato da altri controlli superati.

## Casi negativi statici

Il checker applica al manifest positivo quattro mutazioni isolate:

- `missing-version.json`: reference dell'asset senza versione;
- `wrong-reviewed-asset.json`: execution log riferito all'asset v0 invece che al v1 revisionato;
- `open-blocker.json`: review v2 procedibile con un rilievo bloccante aperto;
- `superseded-review.json`: execution log riferito alla review v1 superata.

Ogni caso deve fallire per il motivo dichiarato nel file, non per un errore collaterale precedente.

## Punti di integrazione

- `campaign-review`: estende CR09, CR10, CR11, CR16 e CR17 con una verifica di versione tra due review consecutive.
- `campaign-debrief`: estende LR02, LR05, LR08 e LR16 con il controllo che l'eseguito derivi dalla review procedibile più recente.
- La fixture riusa i vincoli Fabriloom già presenti, ma resta autonoma e non modifica le fixture `design-campaign` o `campaign-debrief` esistenti.

## Evidenza da registrare in un run comportamentale

- versione effettiva delle due skill;
- file forniti in ciascuna fase;
- ID e versioni citati dall'output;
- esito, rilievi e criteri di chiusura;
- riferimento effettivo dell'esecuzione;
- distinzione tra atteso, eseguito e osservato;
- formulazioni causali eventualmente presenti;
- hard fail, soft fail e azioni osservate.
