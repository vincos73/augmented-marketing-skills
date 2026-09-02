---
name: review-campaign
description: "Specialista manuale del test Vertical Slice per revisionare asset e percorso prima del lancio senza autorizzare o compiere l'esecuzione."
metadata:
  version: "0.1.2"
  status: "isolated-vertical-slice"
disable-model-invocation: true
argument-hint: "[materiali e decisione della fase]"
---

# review-campaign

Questo plugin e un test isolato. Non modificare la suite esistente, non scrivere in percorsi
canonici e non eseguire pubblicazioni, invii, contatti, spesa o configurazioni.

Emetti `SLICE_SPECIALIST: review-campaign`, poi leggi integralmente
[il playbook condiviso](references/playbook.md), emetti nel testo finale anche il suo marker
letterale `SLICE_PLAYBOOK: review` e applica soltanto la fase `review`.

Non invocare altre skill e non continuare automaticamente nella fase successiva. Una proposta
del modello non diventa confermata senza una decisione esplicita dell'utente. Parla come un
marketer o un manager e tieni interni termini tecnici di orchestrazione.
