# Risultati del confronto controllato

## Chiave delle condizioni

- **Run A:** orchestratore `augmented-marketing-prototype`
- **Run B:** agente generalista con buon prompt
- **Run C:** tre skill autonome

## Risultato principale

| Condizione | Verdetto cieco | Invocazioni tecniche | Rilavorazione materiale | Conseguenza osservata |
|---|---|---:|---|---|
| Orchestratore | PASS | 1 iniziale, 0 successive | Nessuna | Migliore continuità e minore rilavorazione complessiva |
| Generalista | PASS CON RISERVA | 0 | Due correzioni metodologiche | Più conciso, ma confronto strategico meno discriminante |
| Skill autonome | PASS CON RISERVA | 3 totali, 2 successive | Nessuna sul contenuto | Metodo solido, ma maggiore carico tecnico per l'utente |

Tutte le condizioni hanno completato quattro turni e non hanno prodotto hard fail. Nessuna ha richiesto di ripetere informazioni già fornite.

## Che cosa dimostra

Nel caso sintetico osservato, una sola skill che conserva la continuità e carica internamente il playbook pertinente combina il metodo delle skill autonome con un carico tecnico più basso. Il vantaggio non deriva da una nuova strategia di marketing: deriva dalla riduzione del costo di orientamento e passaggio tra metodi già validati.

Il generalista resta una baseline forte. Non fallisce, ma richiede più revisione nel punto in cui deve costruire alternative strategiche dello stesso livello e distinguere nettamente servizio e dispositivo preliminare di apprendimento.

## Che cosa non dimostra

- Non è un test con un marketer reale.
- Non misura minuti reali di revisione, adozione o risultati di mercato.
- Non prova il comportamento su Claude o altri harness.
- Non dimostra discovery automatica, installazione o aggiornamento del plugin.
- Non giustifica ancora la sostituzione delle skill autonome o dei bundle esistenti.

## Decisione suggerita

**GO per continuare il prototipo come singola skill con playbook interni.**

**NO-GO, allo stato attuale, per un orchestratore che dipenda dal passaggio runtime verso altre skill installate.** Questo trasferirebbe il vantaggio osservato su una capacità dell'harness che non è uniforme.

La fase successiva dovrebbe testare lo stesso pacchetto neutro in almeno un runtime Claude reale, usando una nuova sessione e verificando discovery, caricamento progressivo, continuità dopo più turni e comportamento dopo compaction.

