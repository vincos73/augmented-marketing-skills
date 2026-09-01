# Confronto indipendente: `campaign-debrief` v0.1.6

- Data: 2026-08-31
- Scenario: stessa richiesta e stessi tre input standalone
- Baseline: buon agente generalista, workflow proxy prestabilito, specialista Analytics
- Valutatore: indipendente dai quattro generatori
- Esito: vantaggio comparativo parziale, osservato su questa fixture

## Output confrontati

| Risposta | Parole | SHA-256 |
|---|---:|---|
| `campaign-debrief` v0.1.6 | 459 | `104b12db029f4a30ab18b0d055a9212e5ad51edb2760451c39c4618e6c218bd0` |
| Buon generalista | 422 | `ac882496538116e7804ac26a7a93374764c6fed0f4a865c34b522cd9a40927c4` |
| Workflow proxy | 524 | `4367c8dc42d16b9f1fedecce7aa0b152917a99c59832f34f7cefa79bed53f8a8` |
| Analytics | 496 | `00ff94cb52606b1a8ee74de5e24b4f71f217bc5dc9c635d8828b422204de3522` |

## Graduatoria qualitativa

| Posizione | Risposta | Totale indicativo | Hard fail | Soft fail |
|---:|---|---:|---:|---:|
| 1 | `campaign-debrief` v0.1.6 | 39/40 | 0 | 2 |
| 2 | Buon generalista | 38/40 | 0 | 2 |
| 3 | Analytics | 36/40 | 0 | 4 |
| 4 | Workflow proxy | 33/40 | 0 | 4 |

I punteggi rendono leggibili le differenze e non sono una misura statistica. Il valutatore separato del test standalone ha classificato lo stesso output v0.1.6 con zero soft fail; nel confronto sono stati applicati due rilievi più fini: registrazioni e partecipazione collocate tra gli output, e mancata menzione esplicita che spec e review non furono riaperte.

## Valore incrementale osservato

Rispetto al buon generalista, la candidata aggiunge soprattutto governance del workflow: criteri della definizione dichiarati non disponibili, separazione dei livelli, routing esplicito a `design-campaign`, controllo intermedio distinto dal gate di spesa e nuova coorte osservata prima del riesame.

Rispetto allo specialista Analytics, mantiene denominatori, copertura, coorti e maturità, aggiungendo atteso/eseguito, capacità, owner e continuità con il Campaign Core. Analytics resta più naturale nella disciplina di misura.

Rispetto al workflow proxy, evita un passaggio prematuro a Finance e riduce l'impostazione KPI-first. Questa baseline è sintetica e non rappresenta il workflow reale di Vincenzo.

## Limite del confronto

La superiorità è osservata soltanto su una fixture e con singoli output. Il margine sul buon generalista è stretto e riguarda la governance, non la qualità generale della scrittura. Mancano ripetizioni cieche, più scenari e parità completa di modello e harness. Sicurezza dichiarata dal valutatore: 88% sulla graduatoria della fixture; inferiore all'80% sulla superiorità generale.
