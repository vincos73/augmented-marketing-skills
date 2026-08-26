# Retest indipendente di `define-marketing-challenge` v0.1.1

**Data:** 2026-08-26
**Valutatore:** nuovo agente separato con contesto vuoto
**Esito:** pass, nessun errore sostanziale

## Isolamento

Il valutatore ha letto soltanto la skill candidata, i reference collegati e gli input grezzi autorizzati per i tre casi. Non ha letto catalogo degli eval, comportamento atteso, run precedenti, README, architettura o conversazione di authoring. Tutti gli output sono stati scritti in una directory temporanea; non ha modificato il repository né `.agents/`.

Le modifiche già presenti nel worktree appartenevano all'authoring in corso e non sono state attribuite al valutatore.

## Casi

1. Relaybird, prima risposta e bozza completa dopo le risposte della Marketing Director.
2. Sponsorship da 18.000 euro non approvata, con pubblico dell'evento non documentato.
3. Brief cliente ricevuto da un'agenzia senza referente autorizzato presente e senza contesti canonici.

## Misure

| Output iniziale | Parole | Domande | Gruppi |
|---|---:|---:|---:|
| Caso Relaybird principale | 436 | 3 | 4 |
| Forward test sponsorship | 411 | 3 | 4 |
| Fallback agenzia | 374 | 3 | 3 componenti previste dal fallback |

La bozza completa del secondo turno misura 943 parole. Il tetto di 450 parole riguarda la prima risposta, quindi non si applica alla presentazione completa dell'artefatto.

## Verifica delle correzioni

- **Dati aggregati:** pass. Il calo delle demo non viene attribuito al pubblico operations e le testimonianze limitate non vengono generalizzate.
- **Provenienza:** pass. Ogni file materiale riceve un ID distinto; `[C]` è usato per le conferme del dialogo e viene combinato con `[Sx]` quando esiste anche una fonte.
- **Conferma senza salvataggio:** pass. La bozza resta un contenuto in chat e il percorso è soltanto proposto; una futura conferma senza scrittura produrrebbe la formula `contenuto confermato in chat; artefatto non creato`.
- **Fallback agenzia:** pass. L'output contiene inventario delle ambiguità, domande per il referente e bozza della richiesta di chiarimento; non produce un brief canonico per conto del cliente.
- **Confine con la direzione:** pass. Nessun caso raccomanda canali, progetta campagne, distribuisce budget o avvia `choose-marketing-direction`.
- **Isolamento:** pass. Nessuna scrittura canonica o modifica delle istruzioni.

## Ambiguità minori accettate

1. Nella fixture, `manager-request.md` rappresenta sia una fonte documentale sia il turno simulato della responsabile. Il marker combinato `[C; S3]` è coerente, ma un futuro eval potrà stabilire una convenzione specifica per i file che simulano dialoghi.
2. Il contratto limita esplicitamente a 450 parole la prima risposta ordinaria, non il fallback agenzia. Il fallback testato resta comunque compatto a 374 parole e utile.

Non emergono motivi per ampliare ulteriormente la patch. La candidata `v0.1.1` è validata sulla suite iniziale, ma non è installata, pacchettizzata o pubblicata.
