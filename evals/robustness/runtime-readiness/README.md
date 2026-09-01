# Matrice runtime e readiness AMS

Questa cartella rende machine-checkable la distinzione tra sorgente validata, comportamento osservato, provenance host, caricamento runtime e pilot reale.

- [SPEC.md](SPEC.md) definisce stati, evidenze e prerequisiti.
- [candidate-readiness.json](candidate-readiness.json) registra lo stato corrente della candidata.
- [READINESS-REPORT.md](READINESS-REPORT.md) offre la lettura manageriale dello stesso stato.
- `scripts/check_readiness.py` valida report ed eventuali evidenze esterne.
- `scripts/self_test_readiness.py` verifica le regressioni negative senza creare receipt positive.

Verifica corrente:

```text
python3 evals/robustness/runtime-readiness/scripts/check_readiness.py
python3 evals/robustness/runtime-readiness/scripts/self_test_readiness.py
```

Il runner unificato usa `--readiness-evidence-index` per inoltrare un indice esterno al checker. Questo indice è separato dagli input comportamentali `--capture-manifest`, `--raw` e `--snapshot`. L'assenza dell'indice è valida soltanto finché la matrice non dichiara stati verified.

Il registro issue esterno accetta `source_system` soltanto come identificatore canonico allowlisted. Attualmente l'unico valore ammesso è `external-issue-tracker-export`; auto-dichiarazioni, differenze di maiuscole, whitespace e sistemi sconosciuti vengono respinti con errore strutturato e non possono promuovere la readiness.

Un PASS del checker significa soltanto che la matrice è coerente e non promuove prove interne. Lo stato corrente resta non pronto per la prossima beta candidata finché mancano run a nove skill con provenance, chiusura P0/P1 e package parity/checksum. Cross-runtime refresh e pilot restano gate successivi.
