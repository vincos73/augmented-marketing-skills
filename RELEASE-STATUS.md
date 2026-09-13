# Stato release Suite 1.0.0

**Stato:** pubblicata su GitHub

**Data di aggiornamento:** 2026-09-13
**Release:** [augmented-marketing-suite-v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0)
**Tag/commit:** `augmented-marketing-suite-v1.0.0` / `386fdea995b8109ed5292a0b6caae705d21c167d`
**Pull request:** PR #14, merged in `main`
**Asset pubblicati:** 15 (13 ZIP, manifest, `SHA256SUMS`)

## Scope

La Suite 1.0.0 comprende:

- plugin Claude 1.0.0 con 12 skill, incluso Augmented Marketing Assistant v0.3.0;
- plugin OpenAI/Codex 1.0.0 con 12 skill, incluso Augmented Marketing Assistant v0.3.0;
- 11 ZIP individuali in `dist/1.0.0/agent-skills/`, uno per skill specialistica;
- versioni delle skill specialistiche invariate;
- bundle Claude senza agenti o subagenti.

## Verifiche

| Controllo | Esito |
| --- | --- |
| Build e checker della Suite | PASS: `python3 scripts/build_suite.py --check`; regressioni builder PASS con 11 test |
| Inventario 12/12 per plugin e 11 ZIP singoli | PASS: 13 archivi complessivi |
| Validazione strict del bundle Claude e marketplace locale | PASS |
| Pubblicazione release GitHub e asset remoti | PASS: release pubblica, draft false, prerelease false, 15 asset |
| Download remoto, checksum e archivio attivo | PASS: 15/15 asset scaricati, parità byte 15/15, checksum 14/14, ZIP integrity 13/13 |
| Installazione plugin stabile da marketplace remoto | PASS: Claude Code `augmented-marketing-suite@augmented-marketing-skills` v1.0.0, user scope, enabled |
| Sincronizzazione/backup delle skill Codex locali | PASS: 12 skill sincronizzate dagli ZIP pubblici; diff 12/12 |
| Aggiornamento dell'installazione Claude locale | PASS: 12 skill, 0 agents/hooks/MCP/LSP; parità cache salvo marker runtime `.in_use` |
| Due test conversazionali Claude | NON VERIFICATI: autenticazione mancante |

Il rapporto completo è [`evals/suite-1.0.0/README.md`](evals/suite-1.0.0/README.md). L'evidenza delle installazioni è [`local-installation.json`](evals/suite-1.0.0/local-installation.json). La pubblicazione e il download sono verificati; il comportamento runtime e l'uso con marketer reali restano limiti distinti.

## Note finali sull'installazione

Le installazioni locali sono confermate: Claude Code usa il plugin 1.0.0 abilitato e Codex dispone delle 12 skill standalone sincronizzate dagli ZIP pubblici. Nessuna app è stata riavviata; serve una nuova sessione per verificare il caricamento delle skill nella conversazione. L'installazione cloud Claude.ai non è verificata e non è stato registrato un nuovo plugin Codex.
