# AMS Vertical Slice

Prototipo isolato per verificare un percorso marketing completo con una skill centrale
auto-invocabile e capacità specialistiche richiamabili singolarmente dall'utente.

Il nucleo comune comprende otto playbook: base, sfida, direzione, marketing mix, campagna,
asset, review e apprendimento. Lo script di build genera due bundle senza modificare la suite
esistente:

- `dist/openai/ams-vertical-slice/` per Codex;
- `dist/claude/ams-vertical-slice/` per Claude.

La fixture Fabriloom è sintetica. I risultati del test non autorizzano pubblicazione, invio,
spesa, configurazione o modifica di artefatti canonici.

## Comandi locali

```bash
python3 scripts/build_vertical_slice.py
python3 scripts/verify_vertical_slice.py
```
