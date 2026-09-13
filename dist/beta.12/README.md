# Augmented Marketing Suite beta.12

> Candidata locale non pubblicata, costruita il 13 settembre 2026. Non corrisponde a una release GitHub e non modifica alcuna installazione personale.

## Pacchetti

- [OpenAI/Codex](openai/augmented-marketing-suite-0.1.0-beta.12.zip): 12 skill, con l'Assistant v0.3.0 e metadati OpenAI.
- [Claude](claude/augmented-marketing-suite-claude-v0.1.0-beta.12.zip): 12 skill, con l'Assistant v0.3.0 e senza metadati `agents`.
- [Skill singole](agent-skills/): 11 archivi portabili, uno per ciascuna skill specialistica; l'Assistant è disponibile nei due plugin completi, non come archivio singolo.
- [Manifest](manifest.json) e [SHA256SUMS](SHA256SUMS): inventario e digest della candidata.

In totale sono 13 archivi: due plugin completi da dodici skill e undici archivi specialistici singoli. L'archivio Claude ha SHA-256 `6cb65bceb5525c8ab7712ac20acade05f0013a60f8c21b4717d038845e18e651`.

## Riproduzione e verifica

```sh
python3 scripts/build_suite.py
python3 scripts/build_suite.py --check
```

Il builder crea ZIP deterministici, legge le versioni dalle skill e verifica i byte di ogni file incluso. `--check` conserva il commit presente nel manifest come provenienza, ma ricostruisce e confronta checksum di sorgenti, pacchetti, manifest e `SHA256SUMS`: un archivio mancante, alterato o aggiuntivo fa fallire il controllo.

La validazione locale del bundle Claude e l'installazione in una configurazione Claude temporanea sono documentate in [evals/suite-beta12/README.md](../../evals/suite-beta12/README.md). L'autenticazione mancava, quindi non esiste una prova di risposta del modello né di instradamento a runtime.
