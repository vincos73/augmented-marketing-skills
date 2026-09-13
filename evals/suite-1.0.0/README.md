# Suite 1.0.0 — build e validazione strutturale

Questo report documenta il build locale stabile del 13 settembre 2026. Non attesta la pubblicazione della release GitHub, il download dell'URL del marketplace, un'installazione personale o il comportamento del modello a runtime.

## Risultati

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Build stabile | PASS | `python3 scripts/build_suite.py`: 13 archivi in `dist/1.0.0`. |
| Riproducibilità | PASS | `python3 scripts/build_suite.py --check`: byte deterministici, sorgenti e archivi coerenti. Il manifest conserva `source_base_commit` `1def4414ff325959683f695fa477e7c892013fe0` anche se `HEAD` è poi avanzato a `455f6ed571b0e49c77847485076c25ac40673941`. |
| Integrità ZIP Claude | PASS | `unzip -t` senza errori; 42 file; SHA-256 `f5791493d384d8ad798c0d8fca2fd6dddbfb9a976e254a3c5a2491eb80ae147d`. |
| Validazione Claude bundle estratto | PASS | `claude plugin validate --strict <bundle-estratto>` con `CLAUDE_CONFIG_DIR` temporaneo. |
| Validazione marketplace | PASS | `claude plugin validate --strict <marketplace>` con `CLAUDE_CONFIG_DIR` temporaneo; URL e SHA-256 della futura release 1.0.0 sono sintatticamente validi. |
| Assistant | PASS strutturale | `quick_validate.py` ha risposto `Skill is valid!` per la sorgente e per la copia estratta; `metadata.version` resta `0.3.0`. |
| Inventario Claude | PASS | 12 directory skill e 0 directory `agents` nel bundle estratto. |
| Regressioni builder | PASS | `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_build_suite.py -v`: 11 test, `OK`. Copre inventario, integrità, checksum, provenienza, percorso stabile senza suffisso e stato `built`. |

La validazione del marketplace controlla il manifest locale e non scarica l'asset remoto. Non è stato eseguito `claude auth login`, non sono state usate credenziali, non è stata effettuata alcuna installazione e non sono stati simulati prompt conversazionali. Una verifica runtime resta bloccata finché una sessione Claude autorizzata non sarà disponibile.

I dettagli senza credenziali sono in [validation.json](validation.json).
