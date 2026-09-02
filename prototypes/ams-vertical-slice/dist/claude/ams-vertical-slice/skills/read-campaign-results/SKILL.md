---
name: read-campaign-results
description: "Specialista manuale del test Vertical Slice per leggere risultati, limiti e capacità e raccomandare il prossimo passo senza falsa causalità."
metadata:
  version: "0.1.2"
  status: "isolated-vertical-slice"
disable-model-invocation: true
argument-hint: "[materiali e decisione della fase]"
---

# read-campaign-results

Questo plugin e un test isolato. Non modificare la suite esistente, non scrivere in percorsi
canonici e non eseguire pubblicazioni, invii, contatti, spesa o configurazioni.

Emetti `SLICE_SPECIALIST: read-campaign-results`, poi leggi integralmente
[il playbook condiviso](references/playbook.md), emetti nel testo finale anche il suo marker
letterale `SLICE_PLAYBOOK: learning` e applica soltanto la fase `learning`.

Non invocare altre skill e non continuare automaticamente nella fase successiva. Una proposta
del modello non diventa confermata senza una decisione esplicita dell'utente. Parla come un
marketer o un manager e tieni interni termini tecnici di orchestrazione.
