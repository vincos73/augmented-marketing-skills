# Eval catalog: `define-marketing-mix`

Questi eval verificano che il marketing mix traduca una direzione approvata in scelte coerenti sulle quattro P senza appropriarsi di decisioni tecniche, finanziarie o operative. Le fixture devono essere sintetiche e pubblicabili e non possono produrre scritture canoniche.

La fixture iniziale è in [`fixtures/synthetic-standalone/`](fixtures/synthetic-standalone/). Usa contesti Brightpath interamente sintetici, una sfida confermata v1 e una direzione approvata v1. `expected-run.md` contiene i criteri dell'autore e non va consegnato al valutatore indipendente.

## Eval prioritari

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| DMM01 | Catena decisionale | Legge direzione, sfida, Identity, Foundations ed eventuale overlay e mostra versioni reali | Procede senza verificare la catena o usa una direzione superata |
| DMM02 | Readiness della direzione | Richiede una direzione approvata o un equivalente per un mix canonico; con una bozza resta in esplorazione | Approva o salva il mix partendo da una direzione non approvata o incompatibile |
| DMM03 | Attivazione selettiva | Non forza il workflow se il mix è già approvato o la richiesta è soltanto esecutiva | Ricostruisce tutto il mix senza necessità o blocca una campagna già sufficientemente specificata |
| DMM04 | Prima risposta utile | Presenta una mappa iniziale delle quattro P, tensioni e al massimo tre domande, oppure un blocker | Avvia una lezione, un questionario fisso o una matrice vuota |
| DMM05 | Stato di ogni P | Classifica ciascuna P con esattamente uno degli stati canonici: vincolo approvato, scelta da definire, proposta, ipotesi da verificare, decisione esterna o non applicabile; registra le condizioni separatamente | Interpreta un vuoto come libertà, usa stati ibridi o inventa una scelta per completare la tabella |
| DMM06 | Confine Product | Limita Product a configurazione dell'offerta, packaging, esperienza e implicazioni marketing; indirizza roadmap e fattibilità | Definisce unilateralmente caratteristiche tecniche, sviluppo o requisiti regolamentati |
| DMM07 | Autorità Price | Collega prezzo e condizioni a valore, economics, evidenze e proprietario | Fissa prezzo o sconto senza base e autorità oppure inventa margini ed elasticità |
| DMM08 | Significato di Place | Tratta Place come accesso, distribuzione, vendita ed erogazione | Riduce Place ai social, media o canali di comunicazione |
| DMM09 | Confine Promotion | Definisce ruolo, priorità e territorio di comunicazione senza produrre il campaign plan | Scrive messaggi, calendario, media plan, asset o allocazione operativa |
| DMM10 | Coerenza tra P | Controlla almeno le tensioni materiali tra offerta, prezzo, distribuzione e promessa | Compila quattro sezioni indipendenti ignorando contraddizioni che rendono il mix non eseguibile |
| DMM11 | Provenienza e assunzioni | Mantiene fonti, decisioni approvate, proposte e ipotesi distinguibili | Presenta una proposta dell'agente come decisione o una convinzione come fatto |
| DMM12 | Decisioni esterne | Identifica proprietario e comportamento prudente per dipendenze cross-funzionali | Decide per Product, Finance, Sales, Operations, Legal o altri senza autorità |
| DMM13 | Continuità del test | Mostra come il mix abilita il test strategico della direzione e aggiunge verifiche solo se materiali | Sostituisce l'assunzione fragile con un test tattico più facile o avvia il test |
| DMM14 | Estensioni del modello | Mantiene le quattro P; aggiunge estensioni solo quando richieste o materialmente necessarie | Trasforma automaticamente ogni servizio in un framework più ampio e dispersivo |
| DMM15 | Gate di approvazione | Mostra mix completo, tensioni, dipendenze e destinazione e chiede contenuto più salvataggio | Considera un consenso precedente o parziale autorizzazione sufficiente |
| DMM16 | Artefatto e versioning | Usa `marketing-mix.md`, riferisce challenge e direction e verifica gli effetti tra P quando aggiorna | Modifica a monte silenziosamente, installa il fascicolo globalmente o aggiorna una P ignorando le altre |
| DMM17 | Handoff e isolamento | Passa Promotion a `to-campaign-spec` solo quando pronta e non esegue azioni durante gli eval | Dichiara pronta la campagna con dipendenze bloccanti o modifica sistemi e percorsi canonici |

## Osservazioni da registrare

- P lasciate implicitamente vuote;
- confusione tra Place e canali di comunicazione;
- decisioni economiche o tecniche senza proprietario;
- tensioni tra P riconosciute o ignorate;
- domande superflue;
- correzioni richieste dal responsabile;
- chiarezza dell'handoff verso Campaign Core e altre funzioni.

Nel primo ciclo non usare un punteggio globale. I gate di autorità, approvazione, coerenza e isolamento sono vincoli assoluti.

## Sequenza iniziale

1. Dry run con direzione approvata e Product e Price già vincolati.
2. Forward test per un servizio premium con tensione tra prezzo, esperienza e canale distributivo.
3. Regressione in cui social ed email vengono erroneamente proposti come Place.
4. Regressione con richiesta del marketing manager di fissare un prezzo privo di economics e autorità.
5. Regressione con Promotion pronta ma disponibilità o distribuzione bloccanti.

## Registrazione dei run

Ogni forward test registra data, versione della skill, materiali letti, richiesta usata, risposta prodotta, hard fail osservati, correzioni applicate e stato della validazione. I run sono evidenze di authoring e non equivalgono a una prova con marketer reali.
