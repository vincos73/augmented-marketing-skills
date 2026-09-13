# Suite 1.0.0 — build e validazione strutturale

Questo report separa le verifiche strutturali eseguite sul build locale dalle prove pubbliche della release 1.0.0 del 13 settembre 2026. La release GitHub `augmented-marketing-suite-v1.0.0` è pubblica e Latest, non draft e non prerelease; il tag punta a `386fdea995b8109ed5292a0b6caae705d21c167d`.

## Risultati

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Build stabile | PASS | `python3 scripts/build_suite.py`: 13 archivi in `dist/1.0.0`. |
| Riproducibilità | PASS | `python3 scripts/build_suite.py --check`: byte deterministici, sorgenti e archivi coerenti. Il manifest conserva `source_base_commit` `1def4414ff325959683f695fa477e7c892013fe0`; il controllo post-merge è passato su `386fdea995b8109ed5292a0b6caae705d21c167d`. |
| Integrità ZIP Claude | PASS | `unzip -t` senza errori; 42 file; SHA-256 `f5791493d384d8ad798c0d8fca2fd6dddbfb9a976e254a3c5a2491eb80ae147d`. |
| Validazione Claude bundle estratto | PASS | `claude plugin validate --strict <bundle-estratto>` con `CLAUDE_CONFIG_DIR` temporaneo. |
| Validazione marketplace | PASS | `claude plugin validate --strict <marketplace>` con `CLAUDE_CONFIG_DIR` temporaneo; URL e SHA-256 della release 1.0.0 sono sintatticamente validi. |
| Assistant | PASS strutturale | `quick_validate.py` ha risposto `Skill is valid!` per la sorgente e per la copia estratta; `metadata.version` resta `0.3.0`. |
| Inventario Claude | PASS | 12 directory skill e 0 directory `agents` nel bundle estratto. |
| Regressioni builder | PASS | `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_build_suite.py -v`: 11 test, `OK`. Copre inventario, integrità, checksum, provenienza, percorso stabile senza suffisso e stato `built`. |

## Prova pubblica attuale

Alle `2026-09-13T19:20:12Z` sono stati scaricati anonimamente tutti i 15 asset pubblici dalla release: 13 ZIP, `manifest.json` e `SHA256SUMS`. I file sono stati ricollocati nelle directory indicate dal manifest, perché GitHub li distribuisce come asset piatti. Il controllo `shasum -a 256 -c SHA256SUMS` è passato per 14 voci; i 15 asset pubblici coincidono byte per byte con `dist/1.0.0`, e `zipfile.testzip()` ha verificato tutti i 13 ZIP senza errori. I dettagli, inclusi hash e mapping degli asset, sono in [public-download.json](public-download.json).

## Installazioni locali

| Destinazione | Esito | Evidenza |
| --- | --- | --- |
| Codex | PASS | Sincronizzate le 12 skill personali dall'archivio OpenAI verificato; `diff -qr` è passato per tutte le directory. Non è una registrazione del plugin Codex. |
| Claude Code | PASS | Plugin utente `augmented-marketing-suite@augmented-marketing-skills` 1.0.0 abilitato, con 12 skill e 0 `agents`, hook, server MCP o LSP. La cache coincide con l'archivio Claude salvo il marcatore runtime `.in_use`; il plugin beta.8 precedente è disabilitato e mantenuto come backup. |

Le prove e i percorsi di backup sono in [local-installation.json](local-installation.json). Nessuna applicazione in esecuzione è stata chiusa o riavviata: per verificare il caricamento delle skill in conversazione serve una nuova sessione Codex o Claude Code. Non è stata verificata un'installazione Claude.ai. Non è stato eseguito `claude auth login`, non sono state usate credenziali e non sono stati simulati prompt conversazionali; il comportamento del modello a runtime resta non verificato.

I dettagli senza credenziali sono in [validation.json](validation.json).
