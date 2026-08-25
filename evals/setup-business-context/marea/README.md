# Test fixture — Marea

Questo fixture sintetico simula il primo invio di una manager che vuole configurare il contesto di un brand autonomo. Tutti i nomi, numeri e materiali sono inventati per l'eval: non contiene dati personali, clienti reali o informazioni confidenziali. Le fonti sono volutamente eterogenee e contengono conflitti e materiale che non deve finire nell'identità persistente.

## Scenario utente

> Voglio impostare il contesto del brand autonomo Marea per gli agenti. Ti allego il sito, una vecchia scheda commerciale, alcune note di stakeholder e le FAQ del supporto. Parti da quello che trovi, dimmi cosa è già sostenuto dalle fonti e fammi solo le domande che possono cambiare il modo in cui descriviamo o limitiamo Marea. Non inventare una missione o una strategia.

## Materiali forniti

- `sources/website.md` — pagina pubblica, fonte primaria per nomi e offerta presentata al mercato.
- `sources/sales-deck.md` — scheda commerciale sintetica con formulazioni miste: fatti correnti, dati non verificati e roadmap.
- `sources/stakeholder-notes.md` — note sintetiche con aggiornamenti, conflitti e contenuti da non persistere.
- `sources/support-faq.md` — linguaggio approvato, misconcezioni e vincoli di comunicazione.

## Turni successivi simulati

- `user-answers.md` contiene le risposte della manager alle tre domande ad alta conseguenza che il router dovrebbe selezionare.
- `approval-and-installation.md` contiene due decisioni separate: approvazione dell'identità e rifiuto dell'installazione nei file di istruzioni.

Il test non autorizza la scrittura di `.agents/brand-identity.md` né di `AGENTS.md`.
