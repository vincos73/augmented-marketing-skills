# Eval comparativa cieca: `setup-business-context` e `setup-marketing-system`

Data: 2026-08-27

Questo pacchetto documenta un confronto sintetico, neutrale e pubblicabile tra una risposta generata senza la skill e una risposta generata con la skill. Non contiene casi, identità, dati o risultati reali di Vincos e non autorizza scritture canoniche, installazioni, pubblicazione, spesa o commit.

## Perimetro

- `setup-business-context` usa la fixture sintetica `fixtures/setup-business-context/`.
- `setup-marketing-system` usa la fixture sintetica `fixtures/setup-marketing-system/`.
- Ogni coppia è prodotta sullo stesso prompt e valutata alla cieca da un agente terzo, descritto nel protocollo come marketer strategico senior con almeno 15 anni di esperienza.
- La valutazione è ripetuta invertendo l'ordine A/B. Il valutatore non riceve l'informazione su quale risposta abbia usato la skill.

## Struttura

- `protocol.md`: prompt, rubriche, procedura di anonimizzazione e formula del gap.
- `fixtures/`: fonti sintetiche e prompt di generazione.
- `outputs/`: risposte baseline e con skill, conservate integralmente.
- `blind-packets/`: coppie anonime consegnate ai valutatori.
- `evaluations/`: giudizi dei due passaggi controbilanciati.
- `report.md`: risultati aggregati, limiti e distinzione tra eval sintetico e validazione reale.

Gli output sono artefatti di test, non artefatti canonici: non devono essere copiati in `.agents/`.
