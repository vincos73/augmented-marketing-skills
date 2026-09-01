# Runner di robustezza AMS

Il runner è behavior-blocking per default. Senza capture esterna termina con codice diverso da zero e lascia `PROVENANCE_VERIFIED` e `ADAPTER_GROUNDED` non eseguiti.

Suite statica esplicita:

```text
python3 evals/robustness/run_robustness.py --static-only
```

Questa modalità verifica fixture, lineage, boundary, invarianti, baseline decisionale review-to-debrief, ledger, adattatore, regressioni di provenance e validità della [matrice runtime/readiness](runtime-readiness/). Non produce `BEHAVIOR_PASS`.

`READINESS_MATRIX_VALID: pass` significa soltanto che stati, evidenze e prerequisiti sono rappresentati senza promozioni indebite. Non significa che la candidata sia pronta, installata o caricata. Il report corrente mantiene `candidate_ready: false`, le superfici non provate a `not_run` e il pilot separato.

Quando la matrice contiene stati verified, il runner riceve e inoltra l'indice esterno con:

```text
python3 evals/robustness/run_robustness.py --static-only \
  --readiness-evidence-index /percorso/esterno/readiness-evidence-index.json
```

`--readiness-evidence-index` risolve envelope di provenance, package, runtime, issue register e pilot. È distinto da `--capture-manifest`, `--raw` e `--snapshot`, che alimentano il gate comportamentale unificato. Senza indice il runner continua a validare la matrice canonica prudente, nella quale nessuno stato verified è dichiarato.

Gate comportamentale:

```text
python3 evals/robustness/run_robustness.py \
  --capture-manifest /percorso/esterno/capture-manifest.json \
  --raw /percorso/esterno/raw-manifest.json \
  --snapshot /percorso/esterno/snapshot.json
```

I tre file devono essere esterni al repository. La capture deve risolvere nove receipt esterne, nove input raw e nove output raw distinti. `BEHAVIOR_PASS` include, nell'ordine logico, `RUN_CAPTURED`, `PROVENANCE_VERIFIED`, `ADAPTER_GROUNDED` e tutti i gate statici. Il solo campo `evidence_mode: behavioral_run` viene respinto.

Il formato di cattura è definito in [behavioral-provenance](../behavioral-provenance/README.md).
