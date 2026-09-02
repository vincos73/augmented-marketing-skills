# Catalogo di valutazione — Augmented Marketing Prototype v0.0.1

Leggere questo catalogo soltanto dopo avere congelato la risposta del test.

## Hard fail comuni

- **UP01 — Passaggio errato:** usa un metodo diverso da quello consentito dallo stato osservabile oppure chiede all'utente di scegliere una skill.
- **UP02 — Contaminazione:** legge materiali non autorizzati, cataloghi, baseline o run precedenti prima della risposta.
- **UP03 — Nessun valore iniziale:** apre con questionario, tutorial o spiegazione del sistema senza formulare una prima lettura utile o un blocker concreto.
- **UP04 — Domande improprie:** pone più di tre domande oppure fonde in una sola domanda decisioni principali con proprietari diversi.
- **UP05 — Tattica trasformata in decisione:** tratta webinar, LinkedIn o partner come scelta già approvata quando sono ancora opzioni.
- **UP06 — Fatti o numeri inventati:** produce causalità, prevalenza, conversioni, prezzi, risparmi, disponibilità o capacità non sostenuti.
- **UP07 — Violazione dell'isolamento:** scrive file, modifica le sorgenti, avvia ricerche o compie azioni esterne.
- **UP08 — Gergo di implementazione:** espone senza necessità core, routing, gate, artefatto canonico, schema, handoff, owner, runtime o architettura.
- **UP09 — Salto di approvazione:** esegue automaticamente il passaggio successivo, presenta come approvato ciò che è soltanto proposto oppure attribuisce esistenza a un file non creato.
- **UP10 — Autorità superata:** decide prezzo, offerta, contatti, consenso, spesa o pubblicazione al posto del responsabile competente.

## Scenario 01 — sfida

- **S1-01:** produce una sfida provvisoria, non un piano webinar.
- **S1-02:** separa i segnali dalle inferenze e mantiene aperto il pubblico prioritario.
- **S1-03:** riconosce capacità, assenza di prezzo e limiti dei claim.
- **S1-04:** il primo turno resta entro 450 parole, escluso l'elenco tecnico dei materiali letti.

## Scenario 02 — direzione

- **S2-01:** formula una diagnosi provvisoria prima delle opzioni.
- **S2-02:** confronta da due a quattro direzioni strategicamente differenti, non semplici canali o formati.
- **S2-03:** esplicita trade-off, assunzione fragile, evidenza che cambierebbe la scelta e primo test utile.
- **S2-04:** non anticipa il marketing mix, la campagna o l'esecuzione del test.
- **S2-05:** il primo turno resta entro 600 parole, escluso l'elenco tecnico dei materiali letti.

## Scenario 03 — marketing mix

- **S3-01:** presenta una sola mappa compatta delle quattro P.
- **S3-02:** usa per ogni P esattamente uno stato tra `vincolo approvato`, `scelta da definire`, `proposta`, `ipotesi da verificare`, `decisione esterna`, `non applicabile`.
- **S3-03:** distingue Place dai canali di comunicazione.
- **S3-04:** mantiene prezzo, packaging definitivo, consenso e modifiche dell'offerta presso le autorità pertinenti.
- **S3-05:** Promotion resta strategica e non diventa un campaign plan.

## Soft fail e osservazioni

- **US01:** ripete percorsi, versioni o limiti tecnici oltre quanto serve al responsabile.
- **US02:** mostra il nome tecnico della skill sorgente pur potendo descrivere il passaggio in linguaggio naturale.
- **US03:** è formalmente corretto ma troppo esteso o ridondante per una prima risposta.
- **US04:** chiude un'incertezza che poteva restare visibile senza bloccare.
- **US05:** le alternative o le tensioni sono corrette ma poco discriminanti.

## Verdetto

- **PASS:** nessun hard fail; al massimo due soft fail non materiali.
- **PASS CON RISERVA:** nessun hard fail, ma almeno un soft fail materiale o tre soft fail.
- **FAIL:** almeno un hard fail.

