# Forward test end-to-end in sola lettura

Usa, nell'ordine, le cinque skill correnti:

1. `setup-business-context`;
2. `setup-marketing-system`;
3. `define-marketing-challenge`;
4. `choose-marketing-direction`;
5. `define-marketing-mix`.

## Materiale che il generatore può leggere

- questo file;
- [materials.md](materials.md);
- [handoff-contract.md](handoff-contract.md);
- [conversation-script.md](conversation-script.md);
- le sole cinque fonti S1-S5 indicate in `materials.md`;
- i cinque `SKILL.md` corrispondenti e i riferimenti strettamente necessari delle skill.

## Materiale escluso

Non leggere `expected-run.md`, `isolation.md`, il checker, gli eval catalog, le fixture specialistiche, gli expected run Fabriloom già esistenti, `user-answers.md` o alcun run storico.

## Compito

Simula i turni del copione. Per ogni skill, genera in chat l'output completo necessario a quel turno, ricevi la conferma/rifiuto simulati e produci il riepilogo strutturato. Fornisci alla skill successiva soltanto quel riepilogo, non l'output completo precedente.

## Vincoli non negoziabili

- Non scrivere file e non eseguire azioni esterne.
- Non chiamare un contenuto conversazionale file canonico, `v1`, `approvato`, installato o caricato.
- Mantieni separati approvazione del contenuto, salvataggio, installazione nelle istruzioni quando applicabile e autorizzazione all'esecuzione.
- Conserva tutti gli invarianti elencati in `materials.md`.
- Non trasformare target, assunzioni, limiti di capacità o dati sintetici in fatti, previsioni, conversioni o causalità.

## Valutazione

Confronta il transcript contro l'oracolo soltanto dopo la generazione. Esegui il checker locale in modalità lettura con un percorso temporaneo del transcript; il suo esito non sostituisce la lettura dell'oracolo.
