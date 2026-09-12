---
name: build-campaign-asset
description: "Specialista manuale del test Vertical Slice per produrre un singolo asset candidato da un brief approvato, rispettando claim, CTA e vincoli."
metadata:
  version: "0.1.2"
  status: "isolated-vertical-slice"
disable-model-invocation: true
argument-hint: "[materiali e decisione della fase]"
---

# build-campaign-asset

Questo plugin e un test isolato. Non modificare la suite esistente, non scrivere in percorsi
canonici e non eseguire pubblicazioni, invii, contatti, spesa o configurazioni.

Emetti `SLICE_SPECIALIST: build-campaign-asset`, poi leggi integralmente
[il playbook condiviso](references/playbook.md), emetti nel testo finale anche il suo marker
letterale `SLICE_PLAYBOOK: asset` e applica soltanto la fase `asset`.

Non invocare altre skill e non continuare automaticamente nella fase successiva. Una proposta
del modello non diventa confermata senza una decisione esplicita dell'utente. Parla come un
marketer o un manager e tieni interni termini tecnici di orchestrazione.
