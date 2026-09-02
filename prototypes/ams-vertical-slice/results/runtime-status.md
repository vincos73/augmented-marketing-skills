# Stato runtime AMS Vertical Slice v0.1.2

Data: 31 agosto 2026.

## Prototipo

- nucleo comune con otto playbook;
- un router automatico e otto specialisti manuali;
- bundle distinti per OpenAI e Claude generati dalla stessa sorgente;
- nove skill valide per bundle;
- parità dei playbook, isolamento degli adattatori, manifest e ZIP verificati;
- test di regressione del valutatore transcript: `PASS`.

## Runtime Codex

- percorso completo: `PASS`;
- continuità dopo ripresa: `PASS`;
- specialista manuale: `PASS`;
- profilo ordinario non modificato.

Dettagli: `codex/v0.1.2-runtime-results.md`.

## Runtime Claude

- visibilità del router e degli otto specialisti: `PASS`;
- percorso completo: `PASS`;
- continuità dopo `/compact`: `PASS`;
- specialista manuale: `PASS`;
- nessuna collisione misurata perché la suite corrente era temporaneamente disabilitata.

Dettagli: `claude/v0.1.2-runtime-results.md`.

## Ripristino

Ripristino completato e verificato nell'interfaccia dopo il riavvio di Claude Desktop:

- Augmented Marketing Suite `0.1.0-beta.8`: attiva;
- AMS Vertical Slice `0.1.2`: disattivato;
- AMS Probe `0.0.2`: disattivato.

Il prototipo resta installato ma inattivo per consentire verifiche future. Non è stato rimosso.

## Confronti ancora mancanti

Le condizioni `CURRENT` e `GENERALIST` non sono state eseguite. Di conseguenza il collaudo prova
che l'architettura è portabile e funziona nei due harness, ma non prova ancora che riduca rework,
ripetizioni o tempo rispetto alla suite corrente o a un generalista.
