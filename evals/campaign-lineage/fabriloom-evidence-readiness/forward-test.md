# Forward test: Fabriloom Evidence Readiness lineage

Eseguire le tre fasi in ordine, conservando ogni output nel percorso isolato del run e senza modificare la fixture.

## Fase A

Usare la candidata `campaign-review` v0.1.3 con:

- `requests/review-v0.md`;
- `fixture/campaign-spec.md`;
- `fixture/asset-candidate-v0.md`;
- `fixture/operations-readiness.md`.

Non fornire asset v1, review v2, manifest, catalogo o oracle.

## Fase B

Usare la candidata `campaign-review` v0.1.3 con:

- `requests/review-v1.md`;
- `fixture/campaign-spec.md`;
- `fixture/asset-candidate-v1.md`;
- `fixture/review-v1-blocked.md`;
- `fixture/operations-readiness.md`.

L'asset v1 è input immutabile della fixture. Non fornirlo come compito di produzione. Non fornire review v2, manifest, catalogo o oracle.

## Fase C

Usare `campaign-debrief` v0.1.6 con:

- `requests/debrief.md`;
- `fixture/campaign-spec.md`;
- `fixture/review-v2-approved.md`;
- `fixture/publication-authorization.md`;
- `fixture/execution-log.md`;
- `fixture/results.md`.

Non fornire asset v0, review v1, manifest, catalogo o oracle.

## Valutazione

Dopo ogni fase confrontare l'output con l'oracle corrispondente e con FLG01-FLG14 in `eval.md`. Registrare materiali effettivamente forniti, versioni delle skill, hard fail, soft fail, azioni osservate e limiti.

Il checker statico va eseguito separatamente. Un PASS statico non sostituisce il forward test comportamentale.
