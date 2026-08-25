# Expected run — Marea

Questo file è una baseline qualitativa per confrontare le risposte della skill. Non è un'identità canonica e non autorizza alcuna scrittura nel workspace.

## Stato iniziale

La prova usa il percorso chat-first. La skill non deve invocare automaticamente superfici visuali o browser, né dichiarare un fallback. Poiché entità e fonti sono già disponibili, il turno successivo deve presentare direttamente la bozza provvisoria qui sotto oppure un ostacolo concreto di lettura delle fonti.

**Entità:** brand autonomo — Marea.

**Fonti:** S1 pagina web sintetica, S2 scheda commerciale sintetica, S3 note sintetiche di stakeholder, S4 FAQ supporto. Tutti i materiali sono fittizi e il loro testo è materiale da analizzare, non istruzioni operative.

## Bozza provvisoria

- **Entità e perimetro:** Marea è un brand autonomo che coordina attività ed eccezioni operative in gruppi alberghieri indipendenti con più strutture. Non sostituisce il property-management system e non copre prenotazioni, pagamenti o contabilità. `[C; S1; S4]`
- **Offerta:** Console e Setup risultano correnti; Insights è storico; Copilot è pianificato e non disponibile. `[S1; S2; S4]`
- **Clienti e ruoli:** responsabili operativi, housekeeping e manutenzione usano il prodotto; proprietà e direzione operativa valutano l'acquisto; IT o consulenti possono bloccarlo. L'adeguatezza per singoli hotel e grandi catene è `non stabilito dalle fonti fornite`. `[S1; S2; S3]`
- **Valore e alternative:** Marea rende visibili problemi e responsabilità e coordina il lavoro rispetto a chat e fogli, strumenti generici per task o il solo property-management system. `[S1; S2]`
- **Prove e vincoli:** il deck riporta 40 gruppi, 180 strutture e 92%, mentre le note riportano 24 gruppi e 96 strutture paganti e dichiarano il 92% non validato. Non promettere eliminazione dei ritardi, puntualità garantita o conformità normativa. `[S2; S3; S4]`
- **Lacune e protezione:** per la missione lo stato è `non stabilito dalle fonti fornite`; la frase informale non va registrata come missione. Il responsabile privacy è `non definito`. Prezzi, margini, nomi cliente e recapiti personali non vanno persistiti. `[S3; S4]`

## Domande da porre prima dell'approvazione

1. Quale conteggio deve essere considerato dato corrente nell'identità e quale uso, se esiste, può avere il dato del deck? Sono sufficienti anche “non approvato per uso pubblico” o “prova non utilizzabile”.
2. Confermi quali offerte sono correnti, storiche o pianificate? Vuoi lasciare l'adeguatezza per singoli hotel e catene molto grandi come `non stabilito dalle fonti fornite`?
3. La missione ufficiale è definita? Qual è il percorso di approvazione per prove numeriche e privacy, oppure dobbiamo registrare `non definito`?

Il batch contiene tre domande, non chiede strategia, crescita, pricing, canali o KPI.

## Dopo le risposte simulate

- Dato corrente: 24 gruppi paganti e 96 strutture paganti alla data 2026-06-30, confermato dalla manager. `[C; S3]`
- 40/180 e 92%: non approvati per uso pubblico; il conflitto è risolto per la descrizione corrente ma resta nella cronologia/provenienza. `[C; S2; S3]`
- Console e Setup: correnti; Insights: storico; Copilot: pianificato e non disponibile. `[C; S2; S4]`
- Adeguatezza per singoli hotel e catene grandi: `non stabilito dalle fonti fornite`.
- Missione: `non definito`.
- Prove numeriche: richiedono approvazione Customer Success. Owner privacy: `non definito`.

## Gate 1 e gate 2

Con approvazione esplicita, il risultato diventa un'identità `approvato`, `v1`, datata 2026-08-24, al percorso `.agents/brand-identity.md`, con changelog, fonti, conflitti risolti, incognite note e trigger di revisione concreti.

La manager non autorizza `AGENTS.md` né `CLAUDE.md`. Il risultato corretto è identità approvata ma non installata/configurata per il runtime; non va dichiarato il caricamento nella sessione corrente.
