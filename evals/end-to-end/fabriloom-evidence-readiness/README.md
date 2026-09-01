# Fixture end-to-end sintetica: Fabriloom Evidence Readiness Sprint

Profilo comune: chat-v1, evidenza synthetic_fixture. Questo profilo è conversazionale e non persistente.

Questa fixture valuta il passaggio conversazionale, in ordine, fra `setup-business-context`, `setup-marketing-system`, `define-marketing-challenge`, `choose-marketing-direction` e `define-marketing-mix`.

Fabriloom, l'offerta, le persone, i dati e le decisioni sono sintetici e pubblicabili. La fixture riusa in sola lettura i materiali della fixture Fabriloom di `design-campaign`: non ne crea una copia divergente.

## Obiettivo

Verificare che la Suite possa mantenere una catena di decisioni utile quando il responsabile:

- approva il contenuto necessario a proseguire in chat;
- nega ogni salvataggio canonico;
- nega l'installazione nelle istruzioni quando questa sarebbe applicabile;
- nega test esterni, spesa, modifiche operative, configurazioni, pubblicazioni e contatti.

Ogni risposta completa resta nel turno in cui è stata prodotta. Il passaggio successivo riceve soltanto il [riepilogo strutturato](handoff-contract.md), non una copia del contenuto integrale e non un file `.agents/` implicito.

## Contenuto della fixture

- [Materiali di input](materials.md): fonti riusate e loro stato;
- [copione multi-turno](conversation-script.md): turni, approvazioni e rifiuti simulati;
- [contratto di handoff](handoff-contract.md): formato minimo e regole di stato;
- [oracolo](expected-run.md): comportamento, hard fail e soft fail;
- [forward test](forward-test.md): istruzioni eseguibili in sola lettura;
- [isolamento](isolation.md): confini non negoziabili;
- `scripts/check_fixture.py`: controllo locale senza rete né scritture.

## Limite deliberato

Una conferma in chat non crea un'identità, Fondamenti, brief, direzione o marketing mix canonici. `chat-v1` è una versione conversazionale della simulazione, non una versione `v1` di un artefatto salvato. I passaggi successivi possono usare il riepilogo come input equivalente soltanto con questo limite esplicito e devono mantenere il proprio output non canonico.

## Esecuzione locale

```text
python3 evals/end-to-end/fabriloom-evidence-readiness/scripts/check_fixture.py \
  --fixture evals/end-to-end/fabriloom-evidence-readiness
```

Per un forward test, consegna solo i file autorizzati da [forward-test.md](forward-test.md) al generatore. Cattura raw e snapshot JSON fuori dal repository e usa il runner comportamentale. Una risposta in prosa o una riga-token non è accettata:

```text
python3 evals/robustness/run_robustness.py \
  --raw /percorso/temporaneo/raw.json \
  --snapshot /percorso/temporaneo/snapshot.json \
  --require-behavior
```

Il checker E2E verifica soltanto la fixture statica. Il runner comportamentale applica grounding, invarianti, lineage e autorità; non dimostra installazione, caricamento runtime o efficacia con marketer reali.
