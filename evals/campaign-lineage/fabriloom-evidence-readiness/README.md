# Eval isolato: Fabriloom Evidence Readiness lineage

Profilo comune: `integrated-postexecution-v1`, scenario `FABRILOOM-ERS-INTEGRATED-POSTEXEC-V1`, evidenza `synthetic_fixture`. Il profilo statico pre-execution è distinto e il passaggio dal profilo `chat-v1` richiede il boundary esplicito dei nove passaggi.

Questa fixture sintetica e pubblicabile verifica il passaggio osservabile tra un asset candidato bloccato, una versione successiva fornita come input, una nuova review, l'esecuzione e il debrief.

Il caso riguarda soltanto la campagna Fabriloom `Evidence Readiness Sprint owned-first`. Non definisce un ledger autorizzativo generale e non introduce regole cross-Core.

## Catena attesa

1. `SPEC-FAB-ERS@1` è la Campaign Spec approvata di riferimento, fornita tramite `provided_by_external_evidence` con file e digest verificati. Non deriva dal salvataggio della conversazione `chat-v1`.
2. `ASSET-FAB-ERS-CAROUSEL@0` è il candidato intenzionalmente difettoso.
3. `REVIEW-FAB-ERS-PRELAUNCH@1` osserva esattamente il candidato v0 e blocca l'azione con il rilievo `CR-LIN-01`.
4. `ASSET-FAB-ERS-CAROUSEL@1` è un file distinto già presente nella fixture. Il test non deve produrlo, riscriverlo o dedurne automaticamente l'approvazione.
5. `REVIEW-FAB-ERS-PRELAUNCH@2` osserva esattamente il candidato v1, registra la chiusura del rilievo e sostituisce la review v1.
6. `AUTH-FAB-ERS-ORGANIC@1` autorizza soltanto asset v1 e review v2 per la pubblicazione organica.
7. `EXEC-FAB-ERS@1` cita soltanto l'asset v1, la review v2 e l'autorizzazione specifica effettivamente approvati.
8. `RESULTS-FAB-ERS@1` registra i risultati osservati con tracking e denominatori.
9. `DEBRIEF-FAB-ERS@1` confronta atteso, eseguito e osservato senza attribuire causalità.

## Contenuto

- `fixture/`: artefatti sintetici usati dalla catena;
- `requests/`: richieste isolate per le due review e il debrief;
- `oracles/`: esiti minimi attesi per le due review e il debrief, da non fornire al generatore;
- `negative-cases/`: quattro mutazioni del manifest positivo che devono essere respinte;
- `runs/`: evidenza riproducibile delle verifiche eseguite;
- `lineage-manifest.json`: riferimenti, versioni e digest osservabili della sola fixture;
- `scripts/check_lineage.py`: checker specifico della lineage Fabriloom;
- `eval.md`: protocollo, rubric e punti di integrazione.
- `forward-test.md`: pacchetti di input separati per l'esecuzione comportamentale.

## Isolamento

Il test non autorizza scritture in `.agents/marketing/decisions/`, produzione di asset, pubblicazione, invio, configurazione di sistemi, paid media o spesa. `publication-authorization.md` è una prova sintetica interna alla fixture, non un'autorizzazione reale. Il claim `60% più velocemente` resta vietato. La testimonianza resta anonima. Paid media richiede una decisione e un'autorizzazione separate.

La presenza di `asset-candidate-v1.md` non dimostra da sola che il rilievo sia chiuso. La chiusura è valida soltanto se una nuova review osserva l'identificatore, la versione e il digest di quel file e registra il criterio verificato.

## Verifica rapida

```bash
python3 evals/campaign-lineage/fabriloom-evidence-readiness/scripts/check_lineage.py
```

Il comando deve validare il manifest positivo e respingere i sette casi negativi con il motivo atteso.
