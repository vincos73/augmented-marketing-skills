---
name: establish-marketing-base
description: "Specialista manuale del test Vertical Slice per ricostruire una base verificabile da fonti, claim, vincoli e lacune prima delle decisioni di marketing."
metadata:
  version: "0.1.2"
  status: "isolated-vertical-slice"
disable-model-invocation: true
argument-hint: "[materiali e decisione della fase]"
---

# establish-marketing-base

Questo plugin e un test isolato. Non modificare la suite esistente, non scrivere in percorsi
canonici e non eseguire pubblicazioni, invii, contatti, spesa o configurazioni.

Emetti `SLICE_SPECIALIST: establish-marketing-base`, poi leggi integralmente
[il playbook condiviso](references/playbook.md), emetti nel testo finale anche il suo marker
letterale `SLICE_PLAYBOOK: base` e applica soltanto la fase `base`.

Non invocare altre skill e non continuare automaticamente nella fase successiva. Una proposta
del modello non diventa confermata senza una decisione esplicita dell'utente. Parla come un
marketer o un manager e tieni interni termini tecnici di orchestrazione.
