# Protocollo comparativo — accesso unificato e skill autonome

Data: 2026-08-30

## Obiettivo

Confrontare sullo stesso caso tre modalità di lavoro:

1. **Generalista**: un agente capace riceve un buon prompt operativo, ma non legge skill o playbook di Augmented Marketing Suite.
2. **Skill autonome**: l'utente invoca esplicitamente la skill pertinente a ogni passaggio.
3. **Orchestratore**: l'utente invoca una sola volta `augmented-marketing-prototype` e prosegue nella stessa conversazione in linguaggio naturale.

Il test verifica il comportamento osservabile in Codex e non modifica sorgenti, distribuzioni o artefatti canonici. La portabilità verso altri harness è valutata separatamente: compatibilità strutturale e test runtime non sono equivalenti.

## Controlli comuni

- Modello: `gpt-5.6-sol`.
- Reasoning effort: `high`.
- Entità sintetica: TramaOps.
- Materiali autorizzati: soltanto `company-identity.md`, `marketing-foundations.md` ed `evidence-note.md` nella fixture congelata di questo test.
- Nessuna ricerca, scrittura, installazione, pubblicazione o altra azione esterna.
- Un passaggio per turno: sfida, direzione, marketing mix.
- Massimo tre domande ad alta conseguenza per risposta.
- Le risposte vengono congelate prima che un valutatore legga il catalogo.

## Richiesta iniziale comune

> Dobbiamo decidere come validare e impostare Supplier Readiness Sprint senza trasformare subito il webinar proposto da Sales nella soluzione. Accompagnami dalla sfida alla direzione e poi al marketing mix, un passaggio alla volta. Usa soltanto i tre materiali autorizzati. Non creare file e non svolgere ricerche o azioni esterne. Inizia dal primo passaggio utile e dammi già una lettura sostanziale prima delle eventuali domande.

La condizione Generalista riceve inoltre questa sola istruzione di qualità, equivalente a un buon prompt:

> Distingui fatti, inferenze e decisioni; non superare le autorità indicate; non inventare numeri; mantieni webinar e partner come opzioni finché non vengono approvati.

La condizione Skill autonome antepone l'invocazione tecnica del passaggio corrente. La condizione Orchestratore antepone soltanto la prima volta l'invocazione del prototipo.

## Decisioni simulate comuni

Le risposte dell'utente devono comunicare gli stessi contenuti, adattando solo il minimo necessario alla domanda osservata.

### Dopo il primo turno

- priorità: capire domanda e ruolo prima del lancio;
- Qualità/Compliance e Procurement restano entrambi aperti;
- il webinar è soltanto un'opzione;
- l'utente conferma la formulazione della sfida e chiede di confrontare le direzioni.

### Dopo il confronto delle direzioni

- preferenza per apprendimento circoscritto prima dell'attivazione pubblica;
- accesso assistito dai partner ammesso soltanto con consenso;
- i partner non parlano per TramaOps e non promettono disponibilità;
- l'utente approva questa direzione e chiede di renderla coerente nelle quattro P.

### Durante il marketing mix

- configurazione definitiva del pilot: decisione del CEO;
- prezzo e condizioni: decisione congiunta di CEO e Finance;
- dopo l'introduzione del partner, TramaOps possiede qualifica, accordi e delivery;
- comunicazione educativa possibile, ma nessuna campagna pubblica è approvata.

## Misure osservabili

- passaggio corretto e confini rispettati;
- hard fail e soft fail del catalogo;
- numero di turni e invocazioni tecniche richieste all'utente;
- domande poste e decisioni principali per domanda;
- informazioni già disponibili richieste nuovamente;
- parole per risposta e parole complessive;
- correzioni materiali richieste prima di ottenere un risultato approvabile;
- continuità: uso corretto delle decisioni confermate nei turni precedenti;
- trasparenza: distinzione fra proposta, approvazione e file effettivamente creato.

Non si attribuiscono minuti di revisione umana: senza un marketer reale sarebbero numeri inventati. Il test registra invece correzioni e rilavorazioni osservabili.

## Condizioni di arresto

Una run termina dopo una mappa del marketing mix valutabile oppure dopo un hard fail che rende non confrontabile la prosecuzione. Una run bloccata può ricevere una sola replica chiarificatrice se il blocco dipende da una formulazione non coperta dalle decisioni simulate.

## Limiti dichiarati

- Il caso è sintetico.
- Il test misura Codex, non Claude.
- Non verifica installazione, marketplace o discovery automatica in una nuova sessione Claude.
- Non misura risultati di mercato né adozione da parte di un team reale.
