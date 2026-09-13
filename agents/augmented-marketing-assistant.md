---
artifact: augmented-marketing-assistant
version: 0.3.0
status: stable
last_reviewed: 2026-09-13
scope: "Ingresso conversazionale alle skill di Augmented Marketing Suite"
---

# Augmented Marketing Assistant

Aiuta manager, marketer e consulenti a individuare il passaggio utile quando il bisogno non è ancora chiaro. Le istruzioni mantenute e la mappa delle undici skill specialistiche sono in [skills/augmented-marketing-assistant/SKILL.md](../skills/augmented-marketing-assistant/SKILL.md), distribuito nei plugin Claude e OpenAI/Codex della Suite 1.0.0.

Il router orienta e carica la skill pertinente con il meccanismo disponibile; non ne replica il metodo. Una richiesta già definita va direttamente alla skill specialistica senza passare dall’Assistant. Definire una voce, scegliere un contenuto e scriverne il copy sono tre bisogni distinti, senza una sequenza obbligatoria.

Questo file descrive il ruolo nel repository, non è una seconda fonte di istruzioni da caricare durante ogni conversazione. L’Assistant è una normale skill di orientamento, condivisa nei due plugin 1.0.0: il bundle Claude non contiene agenti o subagenti.
