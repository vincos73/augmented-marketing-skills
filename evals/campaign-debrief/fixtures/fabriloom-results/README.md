# Fixture Fabriloom results

Fixture sintetica e pubblicabile per i test collegati, standalone e di follow-up di `campaign-debrief`.

## Input del generatore

- `user-request.md`
- `campaign-spec.md`
- `campaign-review.md`
- `execution-log.md`
- `results.md`
- `follow-up-request.md` e `results-matured.md`, solo per il turno di aggiornamento

Per il percorso standalone fornisci soltanto `user-request.md`, `execution-log.md` e `results.md`; l'assenza della Campaign Spec fa parte del test.

Non fornire al generatore l'oracolo in `../../oracles/fabriloom-results-expected-debrief.md`, il catalogo eval o run precedenti.

La campagna e tutti i dati sono sintetici. Il test è in sola lettura e non autorizza file canonici, spesa, pubblicazione o modifiche operative.
