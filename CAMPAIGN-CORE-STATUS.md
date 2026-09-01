# Campaign Core: punto della situazione

Aggiornato: 1 settembre 2026

## Stato verificato

Il Campaign Core usa la sequenza ufficiale:

```text
design-campaign → campaign-review → campaign-debrief
```

Le tre skill possiedono decisioni diverse e non sono passaggi obbligatori per ogni campagna.

### `design-campaign`

- Sorgente: [`skills/design-campaign/`](skills/design-campaign/)
- Versione candidata: `0.1.4`
- Evidenza: il [retest indipendente Fabriloom](evals/design-campaign/runs/2026-08-31-fabriloom-independent-retest-v0.1.4.md) è PASS, con zero hard fail e zero soft fail sulla prima risposta standalone.
- Limite: non sono ancora provati l'intero dialogo, la Campaign Spec finale, il percorso collegato o l'efficacia sul mercato.

### `campaign-review`

- Sorgente: [`skills/campaign-review/`](skills/campaign-review/)
- Versione candidata locale: `0.1.3`
- Stato GitHub osservato: la v0.1.1 è stata unita su `main` con la PR #4; include contratto, fixture, eval, forward test indipendente PASS e pacchetto candidato.
- Modifica v0.1.2 nel branch corrente: il passaggio post-lancio usa il nome ufficiale `campaign-debrief`.
- Modifica candidata v0.1.3: quando il passo successivo è `campaign-debrief`, la review conserva una baseline decisionale compatta con target o regola, definizione, finestra, stato probatorio, asset, rilievi, autorizzazione ed esecuzione separate. Predispone il confronto descrittivo con il target senza presentarlo come confronto incrementale o causale.
- Evidenza: regressioni statiche PASS, forward Review→Debrief sotto compattazione PASS e run integrato controllato sulla fixture sintetica Fabriloom delle nove skill candidate su Codex Desktop, con provenance verificata e `BEHAVIOR_PASS`. Il run prova la sorgente candidata, non un package installato o una campagna reale.
- Limite: la beta.9 distribuita resta a v0.1.2; la candidata v0.1.3 non è ancora stata pacchettizzata, installata, pubblicata o validata con marketer esterni.

### `campaign-debrief`

- Blueprint: [`blueprints/campaign-debrief/campaign-debrief-blueprint.md`](blueprints/campaign-debrief/campaign-debrief-blueprint.md)
- Sorgente candidata: [`skills/campaign-debrief/`](skills/campaign-debrief/)
- Versione: `0.1.6`, sorgente pronta con suite comportamentale sintetica PASS
- Riferimenti: guida a sufficienza e domande, più template unico di `campaign-learning.md`
- Eval: catalogo esistente e prima fixture longitudinale sintetica [`fabriloom-results`](evals/campaign-debrief/fixtures/fabriloom-results/README.md)

La sorgente è considerata pronta nella versione v0.1.6. Confronta atteso, esecuzione reale e dati osservati; limita causalità e comparazioni; raccomanda un'azione con responsabile e nuovo controllo; non modifica campagne, budget, tracking o playbook. La prima risposta standalone e il follow-up con dati maturati sono PASS con zero hard e zero soft fail. La regressione collegata è PASS con tre soft fail non bloccanti; la persistenza isolata è PASS con un soft fail. Nel confronto matched-input la candidata è prima sulla fixture, con vantaggio stretto sul buon generalista e complementare rispetto ad Analytics.

## Prossimi passaggi

1. Allineare la sorgente v0.1.6 su GitHub tramite pull request.
2. Decidere separatamente se e quando creare package, checksum, release e installazione.
3. In una fase successiva, ripetere il confronto su più fixture e con parità di modello e harness.
4. Provare il workflow con marketer esterni e con il processo reale del responsabile.
5. Valutare i soft fail residui solo se ricompaiono in nuovi scenari.

## Confini

- Tutte le fixture sono sintetiche e restano fuori dai percorsi canonici.
- La presenza di una sorgente non dimostra installazione o caricamento nella sessione.
- Commit, push, pull request, release e installazione non sono impliciti nella validazione locale.
- Gli eval non autorizzano spesa, pubblicazione o modifiche operative.
- Il confronto con il workflow abituale usa un proxy sintetico e non costituisce prova sul workflow reale di Vincenzo.
- Lo stato `pronta` riguarda la sorgente v0.1.6 e non equivale a package, release pubblica, installazione o validazione di mercato.

## Contesto Git

- Branch di lavoro: `codex/campaign-debrief-skill`
- Base: `origin/codex/campaign-core-skill-candidates` integrata con `origin/main`
- Remoto: `https://github.com/vincos73/augmented-marketing-skills.git`
- Il checkout principale con lavoro non correlato non viene modificato.
