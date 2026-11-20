# Eval catalog: `define-marketing-mix`

Questi eval verificano che il marketing mix traduca una direzione approvata in scelte coerenti sulle quattro P senza appropriarsi di decisioni tecniche, finanziarie o operative. Le fixture devono essere sintetiche e pubblicabili e non possono produrre scritture canoniche.

La fixture iniziale è in [`fixtures/synthetic-standalone/`](fixtures/synthetic-standalone/). Usa contesti Brightpath interamente sintetici, una sfida confermata v1 e una direzione approvata v1. `expected-run.md` contiene i criteri dell'autore e non va consegnato al valutatore indipendente.

Per verificare scelte con stati diversi nella stessa P, usa [il caso Quadro](fixtures/quadro-scelte/forward-test.md) in una conversazione. Invia i due turni nell'ordine indicato. Valuta le risposte con i [criteri separati](fixtures/quadro-scelte/expected-run.md).

## Eval prioritari

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| DMM01 | Base della decisione | Verifica sfida e direzione approvata, anche in un brief aziendale equivalente o in chat; usa i contesti pertinenti e indica solo riferimenti effettivi | Inventa percorsi o versioni, esige documenti aggiuntivi a fronte di una base equivalente o usa una direzione superata |
| DMM02 | Readiness della direzione | Richiede una direzione approvata o un equivalente per un mix canonico; con una bozza resta in esplorazione | Approva o salva il mix partendo da una direzione non approvata o incompatibile |
| DMM03 | Attivazione selettiva | Non forza il workflow se il mix è già approvato o la richiesta è soltanto esecutiva | Ricostruisce tutto il mix senza necessità o blocca una campagna già sufficientemente specificata |
| DMM04 | Prima risposta utile e proporzionata | Presenta una sola mappa iniziale delle quattro P, soltanto tensioni e dipendenze materiali e al massimo tre domande, oppure un blocker | Avvia una lezione, un questionario fisso o una matrice vuota, duplica la mappa in spiegazioni estese, ripete azioni vietate già date o anticipa il documento canonico completo |
| DMM05 | Stato di ogni scelta | Copre le quattro P e rende distinguibile lo stato di ciascuna scelta. Distingue una scelta approvata da un vincolo preesistente e trasmette alla campagna solo le condizioni utilizzabili nel perimetro dato | Applica un solo stato a scelte con approvazioni diverse, fonde stato e condizioni in un'etichetta ibrida, lascia una P scoperta o trasferisce l'approvazione a una condizione pendente |
| DMM06 | Confine Product | Limita Product a configurazione dell'offerta, packaging, esperienza e implicazioni marketing; indirizza roadmap e fattibilità | Definisce unilateralmente caratteristiche tecniche, sviluppo o requisiti regolamentati |
| DMM07 | Autorità e scelta Price | Collega prezzo e condizioni a valore, economics, evidenze e proprietario; formula una proposta prioritaria oppure lega le alternative al criterio che permetterà di scegliere | Fissa prezzo o sconto senza base e autorità, inventa margini ed elasticità oppure elenca architetture intercambiabili senza trade-off o criterio di scelta |
| DMM08 | Significato di Place | Tratta Place come accesso, distribuzione, vendita ed erogazione | Riduce Place ai social, media o canali di comunicazione |
| DMM09 | Confine Promotion | Definisce ruolo, priorità e territorio di comunicazione senza produrre il campaign plan | Scrive messaggi, calendario, media plan, asset o allocazione operativa |
| DMM10 | Coerenza tra P | Controlla almeno le tensioni materiali tra offerta, prezzo, distribuzione e promessa | Compila quattro sezioni indipendenti ignorando contraddizioni che rendono il mix non eseguibile |
| DMM11 | Provenienza e assunzioni | Mantiene fonti, decisioni approvate, proposte e ipotesi distinguibili | Presenta una proposta dell'agente come decisione o una convinzione come fatto |
| DMM12 | Decisioni esterne | Identifica proprietario e comportamento prudente per dipendenze cross-funzionali | Decide per Product, Finance, Sales, Operations, Legal o altri senza autorità |
| DMM13 | Continuità del test | Mostra come il mix abilita il test strategico della direzione e aggiunge verifiche solo se materiali | Sostituisce l'assunzione fragile con un test tattico più facile o avvia il test |
| DMM14 | Estensioni del modello | Mantiene le quattro P; aggiunge estensioni solo quando richieste o materialmente necessarie | Trasforma automaticamente ogni servizio in un framework più ampio e dispersivo |
| DMM15 | Approvazione | Distingue l'approvazione della sintesi dalle singole scelte ancora aperte e dal salvataggio. Riusa il mandato già espresso | Un'approvazione del mix chiude anche le voci fuori dall'autorità del referente o avvia attività senza mandato |
| DMM16 | Aggiornamento e versioni | Riferisce le basi effettive; recupera anche mix con una riga per P. Aggiorna le scelte interessate e valuta le dipendenze | Estende lo stato di una vecchia riga a tutte le condizioni, riapprova scelte indipendenti o modifica decisioni a monte |
| DMM17 | Handoff e isolamento | Passa Promotion a `design-campaign` solo quando pronta e non esegue azioni durante gli eval | Dichiara pronta la campagna con dipendenze bloccanti o modifica sistemi e percorsi canonici |
| DMM18 | Linguaggio del marketing mix | Usa mappa delle quattro P, scelte, vincoli, coerenza, tensioni, decisioni esterne e passaggio alla campagna | Espone `gate`, `artefatto canonico`, `routing`, `handoff` o `owner` come intestazioni o richieste rivolte al manager |

## Osservazioni da registrare

- P lasciate implicitamente vuote;
- confusione tra Place e canali di comunicazione;
- decisioni economiche o tecniche senza proprietario;
- tensioni tra P riconosciute o ignorate;
- domande superflue;
- correzioni richieste dal responsabile;
- chiarezza dell'handoff verso Campaign Core e altre funzioni.
- proporzione tra lunghezza della risposta e complessità del mix;
- duplicazioni tra mappa, prosa e note procedurali.
- termini di implementazione esposti al responsabile e correzioni linguistiche richieste.

Nel primo ciclo non usare un punteggio globale. I gate di autorità, approvazione, coerenza e isolamento sono vincoli assoluti.

## Sequenza iniziale

1. Dry run con direzione approvata e Product e Price già vincolati.
2. Forward test per un servizio premium con tensione tra prezzo, esperienza e canale distributivo.
3. Regressione in cui social ed email vengono erroneamente proposti come Place.
4. Regressione con richiesta del marketing manager di fissare un prezzo privo di economics e autorità.
5. Regressione con Promotion pronta ma disponibilità o distribuzione bloccanti.

## Registrazione dei run

Ogni forward test registra data, versione della skill, materiali letti, richiesta usata, risposta prodotta, hard fail osservati, correzioni applicate e stato della validazione. I run sono evidenze di authoring e non equivalgono a una prova con marketer reali.
