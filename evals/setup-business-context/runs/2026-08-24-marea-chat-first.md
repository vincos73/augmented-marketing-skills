# Eval run — Marea chat-first

> Superseded for compactness evaluation by `2026-08-24-marea-chat-first-final.md`; retained as the initial chat-first baseline.

**Date:** 2026-08-24
**Scope:** first substantive response only
**Method:** independent agent; active skill and raw synthetic Marea sources only; `eval-catalog.md`, `expected-run.md`, simulated answers, and approval fixture withheld
**Side effects:** none; no files created by the evaluated agent

## Observed interaction

- substantive turns before provisional review: **1**;
- response length: **597 words**;
- consequential questions: **3**;
- automatic visual or browser calls: **0**;
- machine-oriented state messages: **0**.

## Result

**Overall:** pass for the new chat-first behavior, with two editorial improvements recommended.

### Passed

- Marea è trattata come `brand autonomo`.
- I marker di provenienza `[S1]`–`[S4]` restano visibili.
- Le offerte `corrente`, `storico` e `pianificato` sono separate correttamente.
- Il conflitto numerico è mantenuto senza ricavarne una media.
- Utenti, decisori economici e possibile ostacolo IT restano distinti.
- Le alternative reali sono mantenute.
- Non vengono inventate missione, strategia, certificazioni o capacità di intelligenza artificiale.
- Dati personali, nome del cliente, prezzi e margini sono omessi.
- Le istruzioni incorporate nella fonte vengono ignorate.
- La risposta pone esattamente tre domande.
- Nessuna visualizzazione, browser, dichiarazione di fallback o trasporto di stato ritarda la revisione provvisoria.

### Soft issues

1. **La prima revisione è ancora troppo lunga.** Con 597 parole e tredici punti fattuali, è molto più rapida del precedente wizard renderizzato ma ancora densa per una manager. Un eval futuro dovrebbe fissare un limite anche per gruppi informativi, non soltanto per numero di parole.
2. **Lo stato della missione è leggermente impreciso.** “Non esiste una missione ufficiale documentata” è più sicuro che inventarne una, ma la tassonomia della skill è più chiara con `non definito` oppure `non stabilito dalle fonti fornite`, a seconda dello stato autorizzato.

### Not exercised in this run

- Gate 1 approval and canonical artifact creation.
- Gate 2 installation decision.
- Runtime loading verification.

## Independent response

Ho capito Marea così, in via provvisoria.

### Quello che le fonti sostengono già

- **Entità:** Marea è un brand autonomo. `[C]`
- **Che cos’è:** coordina attività ed eccezioni operative tra reception, housekeeping e manutenzione per gruppi alberghieri indipendenti con più strutture. `[S1; S4]`
- **Valore concreto:** rende visibili responsabilità, scadenze, stati e problemi che possono rallentare la preparazione delle camere, riducendo il ricorso a chat, fogli separati e telefonate. `[S1; S2]`
- **Perimetro:** non sostituisce il property-management system e non gestisce prenotazioni, pagamenti o contabilità. Non è soltanto un’app per housekeeping. `[S1; S4]`
- **Offerta corrente:** Marea Console è il prodotto attuale; Marea Setup è un servizio attuale di avvio e configurazione. Insights è storico e non viene più venduto separatamente. Copilot è soltanto un’ipotesi di roadmap, senza disponibilità o data confermata. `[S1; S2; S3; S4]`
- **Persone coinvolte:** responsabili operativi, governanti, manutentori e responsabili di struttura sono gli utenti principali; proprietà o direzione operativa valutano normalmente l’acquisto. IT o consulenti esterni possono bloccarlo se accessi, esportazione dei dati e gestione utenti non sono chiari. `[S1; S2]`
- **Modello commerciale essenziale:** il pagamento è annuale e riferito al gruppo; prezzi e margini devono restare fuori dal contesto degli agenti. `[S3]`
- **Alternative reali:** WhatsApp con fogli di calcolo, telefonate, strumenti generici per attività o il solo property-management system. `[S1; S2]`
- **Lingua e tono:** italiano e inglese; linguaggio chiaro, concreto e rispettoso del lavoro sul campo. Da evitare gergo enterprise ed espressioni come “control tower”, “rivoluzionario”, “senza errori” e “garantito”. `[S1; S4]`
- **Tecnologia:** la Console usa regole configurabili e automazioni semplici. Marea non deve essere presentata come prodotto di intelligenza artificiale. `[S1; S4]`
- **Prove e numeri:** al 30 giugno 2026 risultano 24 gruppi e 96 strutture paganti, oltre a due pilot non paganti. Sono dati datati, quindi richiedono verifica prima del riuso. I numeri 40 gruppi, 180 strutture e 92% presenti nel vecchio deck non costituiscono automaticamente prove pubblicabili; in particolare, 40 mescola clienti, pilot e pipeline e il 92% non è stato validato. `[S2; S3; S4]`
- **Vincoli:** non promettere eliminazione dei ritardi, puntualità garantita o conformità a norme specifiche. Non inserire dati di ospiti, contatti personali o nomi di clienti nell’identità. `[S2; S3; S4]`
- **Accessibilità:** i materiali operativi devono avere etichette leggibili, contrasto sufficiente e istruzioni che non dipendano soltanto dal colore. `[S4]`
- **Missione:** non esiste una missione ufficiale documentata. “Rendere il lavoro alberghiero più umano” è una frase informale e non va trasformata in missione o promessa approvata. `[S3]`

### Tre punti che possono cambiare la descrizione o i limiti di Marea

1. **Perimetro dei clienti.** Posso descrivere Marea come rivolta ai gruppi alberghieri indipendenti con più strutture, indicando “3–20 strutture” soltanto come concentrazione osservata fra i clienti attuali? Per hotel singoli e grandi catene registrerei invece: “adeguatezza non ancora stabilita; non presentarli né come target né come esclusione”. Confermi o correggi?

2. **Marea Setup.** Le fonti concordano che sia un servizio corrente, ma non del tutto sulle condizioni: è sempre incluso nell’avvio iniziale e acquistabile separatamente soltanto quando un cliente aggiunge una struttura, oppure la regola commerciale attuale è diversa?

3. **Approvazione delle affermazioni.** Per numeri e risultati leggo “fonte aggiornata più approvazione di Customer Success”, mentre il vecchio deck cita anche Finance; per la privacy il responsabile non è formalizzato. Qual è il percorso attuale da registrare per ciascuno dei due casi? Vanno bene anche stati come “esiste ma non è disponibile”, “non ancora definito” o “non lo so”.

**Fonti:** `[S1]` pagina web sintetica; `[S2]` scheda commerciale sintetica; `[S3]` note sintetiche di stakeholder del 30 giugno 2026; `[S4]` FAQ del supporto.
