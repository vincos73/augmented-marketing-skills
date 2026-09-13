# Stato release Suite 1.0.0

**Stato:** in preparazione alla pubblicazione GitHub  
**Data di aggiornamento:** 2026-09-13  
**Release prevista:** [augmented-marketing-suite-v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0)

## Scope

La Suite 1.0.0 comprende:

- plugin Claude 1.0.0 con 12 skill, incluso Augmented Marketing Assistant v0.3.0;
- plugin OpenAI/Codex 1.0.0 con 12 skill, incluso Augmented Marketing Assistant v0.3.0;
- 11 ZIP individuali in `dist/1.0.0/agent-skills/`, uno per skill specialistica;
- versioni delle skill specialistiche invariate;
- bundle Claude senza agenti o subagenti.

## Verifiche

| Controllo | Stato iniziale |
| --- | --- |
| Build e checker della Suite | PASS: `python3 scripts/build_suite.py --check`; regressioni builder PASS con 11 test |
| Inventario 12/12 per plugin e 11 ZIP singoli | PASS: 13 archivi complessivi |
| Validazione strict del bundle Claude e marketplace locale | PASS |
| Pubblicazione release GitHub e asset remoti | PENDING |
| Download remoto, checksum e archivio attivo | PENDING |
| Installazione plugin stabile da marketplace remoto | PENDING |
| Sincronizzazione/backup delle skill Codex locali | PENDING |
| Aggiornamento dell'installazione Claude locale | PENDING |
| Due test conversazionali Claude | NON VERIFICATI: autenticazione mancante |

Il rapporto completo è [`evals/suite-1.0.0/README.md`](evals/suite-1.0.0/README.md). La decisione di uscita stabile è distinta dalle verifiche live e non implica un pilot con marketer reali.

## Aggiornamento dopo la pubblicazione

Da aggiornare dopo la pubblicazione con URL e asset effettivamente disponibili, checksum remoto, esito del download e dell'installazione dai due ambienti, oltre agli eventuali limiti residui. Fino a quell'aggiornamento, la release va descritta come in preparazione e il link GitHub come previsto.
