---
artifact: augmented-marketing-assistant
version: 0.3.1-l10n.1
status: local-candidate-not-published
last_reviewed: 2026-09-22
scope: "Ingresso conversazionale alle skill di Augmented Marketing Suite"
---

# Augmented Marketing Assistant

Aiuta manager, marketer e consulenti a individuare il passaggio utile quando il bisogno non è ancora chiaro. Le istruzioni mantenute e la mappa delle undici skill specialistiche sono in [skills/augmented-marketing-assistant/SKILL.md](../skills/augmented-marketing-assistant/SKILL.md), usato dalla candidata locale Suite 1.0.1-l10n.1. La release 1.0.0 conserva Assistant v0.3.0 nei suoi archivi immutati.

Il router orienta e carica la skill pertinente con il meccanismo disponibile; non ne replica il metodo. Una richiesta già definita va direttamente alla skill specialistica senza passare dall’Assistant. Definire una voce, scegliere un contenuto e scriverne il copy sono tre bisogni distinti, senza una sequenza obbligatoria.

Questo file descrive il ruolo nel repository, non è una seconda fonte di istruzioni da caricare durante ogni conversazione. L’Assistant è una normale skill di orientamento, condivisa nei due plugin: il bundle Claude non contiene agenti o subagenti.
