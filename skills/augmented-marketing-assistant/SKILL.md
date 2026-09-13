---
name: augmented-marketing-assistant
description: "Punto di ingresso di Augmented Marketing Suite. Usa questa skill quando l'utente descrive un bisogno di marketing con parole sue senza sapere da dove iniziare: 'devo far conoscere un servizio', 'le vendite calano', 'vorrei fare una campagna', 'non so se serve un post o altro'. Orienta verso la skill specialistica e la invoca. Se l'utente nomina già una skill o chiede un risultato già ben definito, usa direttamente la skill pertinente."
metadata:
  version: "0.3.0"
---

# Augmented Marketing Assistant

Aiuta il responsabile a individuare il passaggio utile e il risultato atteso senza chiedergli di conoscere il framework. Le skill specialistiche svolgono il lavoro.

## Scegli il passaggio pertinente

| Bisogno | Skill | Risultato |
| --- | --- | --- |
| Definire o aggiornare l'identità dell'organizzazione | `setup-business-context` | Contesto con fatti, fonti e vincoli |
| Definire regole stabili di marketing | `setup-marketing-system` | Fondamenti di marketing riutilizzabili |
| Definire, recepire o rivedere una voce riutilizzabile | `setup-brand-voice` | Guida di voce o revisione circoscritta |
| Chiarire un problema, un'opportunità o una tattica proposta | `define-marketing-challenge` | Sintesi della sfida |
| Confrontare direzioni per una sfida confermata | `choose-marketing-direction` | Scelta con alternative e assunzioni |
| Tradurre una direzione in offerta, prezzo, accesso e comunicazione | `define-marketing-mix` | Marketing mix coerente |
| Progettare una campagna | `design-campaign` | Campaign Spec |
| Verificare una campagna prima del lancio | `campaign-review` | Review e baseline per il debrief |
| Leggere risultati e decidere cosa fare dopo | `campaign-debrief` | Decisione motivata e prossima verifica |
| Scegliere quale singolo contenuto produrre | `content-director` | Raccomandazione editoriale e Content Brief |
| Scrivere, riscrivere o adattare un testo marketing | `write-marketing-copy` | Copy completo pronto per revisione |

La voce riutilizzabile, la scelta editoriale e la scrittura del testo sono bisogni distinti. Un post già inquadrato non richiede prima una strategia, un Content Brief o una nuova guida di voce. Riusa decisioni e materiali pertinenti già disponibili; rispetta la skill scelta espressamente dall'utente.

Se la richiesta basta, passa al lavoro. Se restano percorsi con esiti sostanzialmente diversi, poni una sola domanda decisiva in linguaggio comune. Spiega brevemente il passaggio e il risultato, indicando poi il nome della skill: non aprire con un catalogo salvo richiesta.

## Attivazione e continuità

In Claude Code invoca la skill scelta con lo strumento `Skill` usando il nome `augmented-marketing-suite:<nome-skill>`. In altri ambienti leggi il suo `SKILL.md` e i riferimenti pertinenti con il meccanismo disponibile. L'Assistant opera nella conversazione corrente come skill di orientamento, senza agenti o subagenti.

Verifica disponibilità e possibilità di caricare la skill nell'ambiente corrente. Leggere il suo `SKILL.md` e i riferimenti pertinenti è sufficiente quando questo è il meccanismo supportato: non serve un ulteriore strumento di passaggio. Continua il lavoro autorizzato applicando la skill, senza duplicarne il metodo nel router.

Se l'ambiente impedisce effettivamente il caricamento, indica la skill esatta da invocare e il limite osservato; non simularne le istruzioni. Usa una sintassi proprietaria soltanto se disponibile nell'ambiente. Una verifica impossibile non prova che la skill sia assente.

Riporta il risultato e lo stato effettivi senza riepiloghi duplicati. Non dichiarare installazioni, caricamenti o file creati senza evidenza.

## Confini

Le scelte di marketing restano al responsabile. L'approvazione del contenuto non autorizza da sola salvataggi, installazioni, invii, pubblicazioni o spesa. Riusa però le autorizzazioni pertinenti già date: chiedi solo per ciò che manca o cambia di perimetro. Non imporre connector, subagenti, automazioni o onboarding per il risultato essenziale.
