# Fixture sintetica Latticeway

Latticeway è una società B2B fittizia che aiuta i team Operations a migliorare il seguito delle decisioni. Tutti i nomi, dati e materiali di questa cartella sono sintetici e pubblicabili.

La fixture verifica se `content-director`:

- parte da una richiesta standalone senza imporre artefatti a monte;
- contesta un claim non sostenuto senza fermarsi prematuramente;
- sceglie una forma in modo agnostico rispetto alle capacità disponibili;
- distingue strada ideale, alternativa fattibile e relativo trade-off;
- prepara un Content Brief senza produrre o pubblicare l'asset.

## Materiali per il generatore

Nel forward test iniziale fornisci:

- `manager-request.md`;
- `research-note.md`;
- `interview-excerpts.md`;
- `marketing-context.md`;
- `production-constraints.md`.

Nel secondo turno fornisci `user-answers.md`.

Non fornire al generatore `expected-run.md` o `expected-content-brief.md`. Sono baseline dell'autore per il valutatore.

`linked-campaign-spec.md`, `bypass-request.md`, `non-produce-request.md`, `multi-asset-request.md`, `manager-insists-30-request.md`, `approved-content-brief.md` e `handoff-request.md` appartengono a regressioni separate e non vanno aggiunti al forward test standalone. Il protocollo è in `regression-test.md`.

Non scrivere in `.agents/marketing/` durante l'eval. Non avviare builder e non produrre asset.
