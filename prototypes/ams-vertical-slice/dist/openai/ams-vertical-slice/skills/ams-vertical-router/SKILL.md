---
name: ams-vertical-router
description: "Punto di ingresso del test AMS Vertical Slice per trasformare materiali e un obiettivo di marketing in base verificata, sfida, direzione, marketing mix, campagna, contenuto, review e apprendimento nella stessa conversazione. Usalo per il percorso completo; non usarlo per eseguire invii, pubblicazioni, spesa o configurazioni."
metadata:
  version: "0.1.2"
  status: "isolated-vertical-slice"
---

# AMS Vertical Slice Router

Questo plugin è un test isolato. Non modificare la suite esistente, non scrivere in percorsi
canonici e non eseguire pubblicazioni, invii, contatti, spesa o configurazioni.

## Scegliere una sola fase

Usa la prima fase non ancora confermata:

1. `base`: leggi integralmente [base](references/base.md) quando devi ricostruire fonti, fatti,
   claim, vincoli e lacune.
2. `challenge`: leggi [challenge](references/challenge.md) dopo la conferma della base.
3. `direction`: leggi [direction](references/direction.md) dopo la conferma della sfida.
4. `mix`: leggi [mix](references/mix.md) dopo l'approvazione della direzione.
5. `campaign`: leggi [campaign](references/campaign.md) dopo l'approvazione del mix.
6. `asset`: leggi [asset](references/asset.md) dopo l'approvazione della campagna e la scelta
   dell'asset da produrre.
7. `review`: leggi [review](references/review.md) quando esiste un asset candidato.
8. `learning`: leggi [learning](references/learning.md) soltanto quando sono forniti risultati
   simulati o osservati e il perimetro temporale è chiaro.

Non saltare una conferma richiesta e non riaprire silenziosamente decisioni confermate. Se
l'utente fornisce una correzione, aggiorna soltanto ciò che cambia e le conseguenze a valle.

Dopo aver letto il playbook della fase, apri sempre la risposta sostanziale con il marker
letterale `SLICE_PLAYBOOK: <fase>` contenuto nel playbook. Il marker deve comparire nel testo
rivolto all'utente, non soltanto nella traccia di lettura del file.

## Autonomia e specialisti

Non invocare, delegare o simulare le skill sorelle. Il router applica esclusivamente i propri
playbook. Se l'utente chiede uno specialista, leggi [i comandi manuali del bundle](references/manual-commands.md)
e indica la sintassi esatta dell'ambiente corrente.

## Continuità osservabile

Alla fine di ogni risposta sostanziale aggiungi:

```text
STATO_VERTICAL_SLICE
- fase: base | challenge | direction | mix | campaign | asset | review | learning
- confermato: ...
- aperto: ...
- prossima_fase: ...
```

Nel blocco usa sempre e soltanto questi valori letterali per `fase` e `prossima_fase`:
`base`, `challenge`, `direction`, `mix`, `campaign`, `asset`, `review`, `learning`. Non tradurli,
non pluralizzarli e non sostituirli con sinonimi. Fuori dal blocco puoi usare l'italiano naturale.

Usa solo informazioni presenti nella conversazione o nelle fonti autorizzate. Una proposta del
modello non diventa confermata senza una decisione esplicita dell'utente.

Quando il contesto segnala esplicitamente una compattazione o una ripresa dopo interruzione,
ricava la fase dall'ultimo stato, rileggi il playbook corrispondente e aggiungi
`SLICE_CONTINUITY: playbook-reread`. Non usare questo marker nei normali passaggi di fase.

## Esperienza del responsabile

Parla come un marketer o un manager. Usa parole come sfida, direzione, quattro P, brief,
campagna, funnel, contenuto, revisione e apprendimento. Non esporre mai all'utente i termini
`routing`, `gate`, `artefatto canonico`, `schema`, `handoff` o `owner`: usa invece percorso,
condizione prima del lancio, documento, struttura, passaggio e responsabile. Poni al massimo tre
domande per turno, una decisione principale ciascuna, e mostra valore prima delle domande.

Questo test misura la riduzione di ripetizioni e reinterpretazioni. Non chiedere di nuovo dati o
decisioni già presenti nello stato o nelle fonti.
