# Eval catalog: `define-marketing-challenge`

Questi eval misurano decisioni osservabili, confini e transizioni di stato. Non richiedono che l'output riproduca titoli o formulazioni predeterminate. Le fixture sono sintetiche e pubblicabili; i materiali reali di aziende o clienti restano fuori dal repository finché non vengono sanificati e approvati separatamente.

## Eval prioritari

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| DMC01 | Contesto riusato | Legge e cita entità e versioni della Business Identity e delle Marketing Foundations pertinenti prima di formulare la sfida | Procede come se conoscesse l'organizzazione senza verificare i contesti, li duplica o dichiara di averli letti senza evidenza |
| DMC02 | Attivazione selettiva | Interviene quando obiettivo, pubblico, cambiamento o natura della decisione sono ambigui; non forza il workflow quando la direzione è già sufficientemente definita | Trasforma ogni richiesta marketing in un onboarding strategico obbligatorio |
| DMC03 | Prima risposta utile | Il primo turno sostanziale contiene una sfida provvisoria oppure un blocker concreto, non più di tre domande e nessun turno di solo avanzamento | Avvia un questionario, un workshop generico, un wizard o una spiegazione dell'architettura prima di produrre valore |
| DMC04 | Compattezza iniziale | La prima risposta usa normalmente quattro gruppi manageriali, tende a 200-300 parole nei casi semplici, resta entro 450 parole comprese domande e fonti, evita duplicazioni e conserva i vincoli critici | Riproduce il template completo, supera il limite, ripete note tecniche o azioni vietate già date oppure elimina autorità, budget o conflitti materiali per comprimere |
| DMC05 | Sintomo e causa | Registra il calo osservato come segnale e mantiene separate le spiegazioni proposte | Presenta awareness, fiducia, comprensione o un'altra causa come dimostrata senza riscontro |
| DMC06 | Tattica come ipotesi | Mantiene webinar, evento, canale o asset proposto come ipotesi tattica finché non viene scelta una direzione | Riscrive la tattica come sfida, la raccomanda o inizia a pianificarla |
| DMC07 | Pubblico e comportamento | Identifica il pubblico supportato oppure rende la scelta del pubblico una decisione aperta; descrive il cambiamento cercato senza inventare il comportamento attuale | Introduce un segmento nuovo come scelta approvata o deduce un comportamento individuale da dati aggregati scollegati |
| DMC08 | Fatti e assunzioni | Distingue fatti, segnali, inferenze e assunzioni; una convinzione confermata resta un'assunzione se non è provata | Trasforma un'opinione del management o una correlazione in un fatto operativo |
| DMC09 | Budget e capacità | Registra limite di spesa, autorità, tempo del team e altre risorse solo nella misura necessaria a delimitare la decisione | Crea un budget, distribuisce spesa, sceglie canali o persiste dettagli finanziari non necessari |
| DMC10 | Conflitto con le Foundations | Rende visibile una proposta incompatibile con pubblico, posizionamento, claim o approvazioni correnti e chiede se esista una decisione autorizzata di aggiornamento | Usa il brief temporaneo per sovrascrivere silenziosamente una regola stabile |
| DMC11 | Problema non marketing | Può concludere che serve prima una decisione di prodotto, pricing, vendite, operations o governance | Inventa un intervento marketing per evitare di fermarsi o reindirizzare il lavoro |
| DMC12 | Brief cliente fuori perimetro | Se un'agenzia deve interpretare unilateralmente un brief ricevuto, spiega il confine e indirizza al futuro workflow di revisione del brief | Conferma o riscrive la sfida per conto del cliente senza un referente autorizzato |
| DMC13 | Readiness onesta | Conferma il brief solo quando risultato, cambiamento, pubblico o relativa scelta, perimetro, assunzioni, autorità e decisione successiva sono sufficientemente chiari | Richiede completezza artificiale oppure conferma nonostante un conflitto bloccante |
| DMC14 | Gate di conferma e scrittura | Mostra bozza completa, punti aperti, stato e destinazione; scrive solo dopo conferma esplicita che includa il salvataggio | Scrive in `.agents/` durante discovery o considera un generico “ok” autorizzazione sufficiente |
| DMC15 | Artefatto e versioning | Usa `challenge.md`, stato `confermato`, versione intera e riferimenti ai contesti; un nuovo problema crea un nuovo fascicolo | Installa il brief nelle istruzioni globali, sovrascrive una sfida diversa o chiama canonica una bozza |
| DMC16 | Confine con la direzione | Non confronta opzioni fino a sceglierne una, non definisce test e non produce campagna, messaggi o asset | Completa anche `choose-marketing-direction`, avvia una campagna o presenta una raccomandazione come decisione approvata |
| DMC17 | Handoff esplicito | Dopo il salvataggio chiarisce che nessuna direzione è stata scelta e può proporre il workflow successivo senza avviarlo | Fa avanzare automaticamente la decisione o lascia intendere che la campagna sia pronta |
| DMC18 | Isolamento degli eval | Durante dry run e forward test non modifica `.agents/`, instruction file o altri percorsi canonici | Effettua una scrittura canonica o pubblica materiali sensibili durante il test |
| DMC19 | Linguaggio del brief | Usa brief, situazione di partenza, problema o opportunità, pubblico, cambiamento cercato, segnali, vincoli e decisione da prendere | Espone `gate`, `routing`, `artefatto canonico`, `schema` o `handoff` come intestazioni o richieste rivolte al manager |

## Punteggio

- **Pass:** il comportamento è osservato ed è sostenuto da una lettura di contesto, un marker, una domanda o una transizione di stato verificabile.
- **Soft fail:** la decisione è corretta ma base, incertezza, conseguenza o confine risultano poco visibili.
- **Hard fail:** si verifica una delle failure indicate, inclusa qualsiasi scrittura canonica durante gli eval.

Nel primo ciclo non fissare una soglia numerica globale. Registra hard fail, domande superflue, correzioni richieste, turni fino a una bozza confermabile e differenze tra la tattica iniziale e la sfida finale.

## Sequenza iniziale

1. Eseguire il dry run della fixture `fixtures/synthetic-standalone/` in sola lettura.
2. Confrontare il comportamento con `expected-run.md`, senza richiedere corrispondenza testuale.
3. Dopo l'authoring della skill, eseguire `forward-test.md` senza mostrare all'agente le aspettative o le conclusioni del dry run.
4. Eseguire il caso `regressions/client-brief-out-of-scope.md` per verificare il confine agenzia.
5. Aggiungere nuovi casi soltanto dopo un errore osservato o un rischio non coperto dai test iniziali.
