# Beta.12 — build e prova Claude locale

Questo report registra una candidata locale non pubblicata costruita il 13 settembre 2026. Le prove Claude hanno usato esclusivamente `CLAUDE_CONFIG_DIR=/private/tmp/ams-beta12.ISxjpr/claude-config`; non hanno letto credenziali, cambiato `~/.claude`, installato il plugin nella configurazione personale o pubblicato file.

## Risultati

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Build candidata | PASS | `python3 scripts/build_suite.py`: 13 archivi creati. |
| Riproducibilità | PASS | `python3 scripts/build_suite.py --check`: byte deterministici, sorgente e archivi coerenti. |
| Integrità ZIP Claude | PASS | `unzip -t` ha completato senza errori; SHA-256 `6cb65bceb5525c8ab7712ac20acade05f0013a60f8c21b4717d038845e18e651`. |
| Validazione Claude bundle estratto | PASS | `claude plugin validate --strict <temp>/local-marketplace/plugin`. |
| Validazione marketplace locale | PASS | `claude plugin validate --strict <temp>/local-marketplace`. Il sorgente di prova era `"./plugin"`. |
| Marketplace e installazione | PASS, isolato | `claude plugin marketplace add ./ --scope user` e `claude plugin install augmented-marketing-suite@augmented-marketing-skills --scope user` nel solo `CLAUDE_CONFIG_DIR` temporaneo. Versione installata `0.1.0-beta.12`, abilitata. |
| Parità cache/installazione | PASS | `diff -qr` tra bundle estratto e cache installata: nessuna differenza; 42 file per lato, 12 directory skill e 0 directory `agents`. |
| Assistant | PASS statico/installato | `metadata.version: "0.3.0"` nella cache installata; `quick_validate.py` ha risposto `Skill is valid!` sia sulla sorgente sia sulla copia in cache. |
| Regressioni builder | PASS | Esecuzione del subagent Terra: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_build_suite.py -v`, 10 test, `OK`. Copre inventario (13 archivi, 12 skill per plugin, 11 singole), e fallimenti attesi per sorgenti/ZIP mancanti o alterati, archivi extra, manifest e `SHA256SUMS`. |

Il primo invio letterale richiesto, `claude plugin marketplace add . --scope user`, è stato rifiutato dalla CLI 2.1.266: `Invalid marketplace source format. Try: owner/repo, https://..., or ./path`. Il retry minimale `./` ha mantenuto la stessa directory e ha consentito la prova; non è stato usato alcun marketplace remoto.

## Invio runtime limitato dall'autenticazione

È stato tentato soltanto il primo prompt, con stream JSON e verbose:

```sh
CLAUDE_CONFIG_DIR=<temporaneo> claude -p 'Ho un negozio e le vendite online calano, non so cosa fare' --output-format stream-json --verbose
```

La traccia di inizializzazione ha caricato il plugin `augmented-marketing-suite@augmented-marketing-skills`, versione `0.1.0-beta.12`, e ha elencato tutte le dodici skill, incluso `augmented-marketing-assistant`. La chiamata non ha generato una risposta: `authentication_failed`, `Not logged in · Please run /login`, con zero token di input e output. La traccia finale riporta `subagent_stats.spawned: 0`.

Per questa ragione il comportamento atteso dell'Assistant verso `define-marketing-challenge` non è verificato. Il secondo prompt — `Usa define-marketing-challenge per chiarire il calo delle vendite online del mio negozio` — è `not_run`: non è stato ritentato dopo il medesimo impedimento di autenticazione. Non ci sono prove di risposta autenticata, instradamento conversazionale o uso delle skill da parte del modello.

I dettagli strutturati, privi di credenziali, sono in [validation.json](validation.json). Il path temporaneo può essere eliminato dal sistema operativo senza influire su una configurazione Claude personale.

Per autenticare in futuro la CLI locale e ripetere la prova in una sessione autorizzata, il comando è:

```sh
'/Users/vincos/Library/Application Support/Claude/claude-code/2.1.266/claude.app/Contents/MacOS/claude' auth login
```

Questa verifica non ha eseguito quel comando né ha consultato credenziali.
