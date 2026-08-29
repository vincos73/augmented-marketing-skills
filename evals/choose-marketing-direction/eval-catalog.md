# Eval catalog: `choose-marketing-direction`

Questi eval misurano decisioni osservabili, confini e transizioni di stato. Le fixture devono essere sintetiche e pubblicabili; durante ogni prova restano vietate scritture canoniche, azioni esterne e modifiche agli instruction file.

La fixture iniziale è in [`fixtures/synthetic-standalone/`](fixtures/synthetic-standalone/). Usa contesti Northline Analytics interamente sintetici, una sfida confermata v1, due ipotesi causali concorrenti e una tattica iniziale non ancora scelta. `expected-run.md` contiene i criteri dell'autore e non va consegnato al valutatore indipendente.

## Eval prioritari

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| CMD01 | Catena di contesto | Legge sfida, Identity, Foundations ed eventuale overlay pertinenti e mostra entità e versioni realmente applicate | Procede senza verificare la catena o dichiara file non letti |
| CMD02 | Attivazione selettiva | Usa il workflow per una scelta strategica; se la direzione è già approvata indirizza al passaggio pertinente | Riapre automaticamente una decisione approvata o forza il workflow su una richiesta esecutiva |
| CMD03 | Readiness del brief | Richiede una sfida confermata o un equivalente approvato per una direzione canonica; permette solo esplorazione provvisoria senza tale base | Salva o approva una direzione basata su un brief non confermato, superato o bloccante |
| CMD04 | Prima risposta utile e proporzionata | Presenta entro 600 parole, salvo complessità eccezionale, diagnosi provvisoria, decisione, criteri, un confronto compatto tra alternative e al massimo tre domande, oppure un blocker concreto; sviluppa solo gli elementi capaci di cambiare la scelta | Inizia con questionario, workshop generico o turno di solo avanzamento, duplica il confronto in più formati, ripete azioni vietate già date o anticipa il documento canonico completo |
| CMD05 | Alternative strategiche | Le opzioni differiscono per pubblico, ostacolo, leva, meccanismo, posizione o sequenza di apprendimento | Presenta canali, formati o asset come direzioni strategiche distinte |
| CMD06 | Alternative non riempitive | Usa solo alternative reali e può includere apprendimento, restringimento o stop quando pertinenti | Inventa opzioni deboli solo per completare una matrice |
| CMD07 | Criteri derivati | Deriva i criteri da risultato, contesto e vincoli della sfida | Applica una checklist universale ignorando ciò che cambia la decisione |
| CMD08 | Provenienza, conflitti e metriche | Mantiene fatti, inferenze, assunzioni e fonti in conflitto distinguibili; descrive separatamente metriche il cui rapporto non è documentato | Trasforma un'opinione in prova, risolve silenziosamente un conflitto o deduce conversione e causalità dalla sola compresenza di metriche scollegate |
| CMD09 | Niente falsa precisione | Motiva il confronto qualitativamente e usa numeri solo con modello e base approvati | Inventa punteggi, pesi, ROI o stime per far sembrare oggettiva la scelta |
| CMD10 | Raccomandazione onesta | Può raccomandare, raccomandare con condizioni oppure concludere che nessuna direzione è pronta o che il problema non è principalmente di marketing | Raccomanda comunque un'opzione quando manca una base o autorità bloccante |
| CMD11 | Trade-off e falsificabilità | Esplicita rinunce, non-scelte, condizione di stop ed evidenza che cambierebbe scelta o diagnosi | Presenta una direzione senza costi, rischi o possibilità di revisione |
| CMD12 | Primo test utile | Collega il test all'assunzione più fragile, formula evidenza, associa gli esiti alle direzioni conseguenti e riapre verso il proprietario competente se emerge un ostacolo non marketing | Lascia gli esiti senza conseguenza decisionale, traduce un problema di prodotto o servizio in comunicazione, progetta una campagna completa, inventa soglie o avvia azioni esterne |
| CMD13 | Confine con le quattro P | Registra implicazioni e dipendenze su Product, Price, Place e Promotion senza definire il mix | Fissa prezzi, roadmap, distribuzione, media mix, messaggi o budget |
| CMD14 | Autorità cross-funzionale | Identifica decisioni di business, Product, Finance, Operations o compliance che devono precedere o condizionare la scelta | Decide unilateralmente per una funzione non autorizzata |
| CMD15 | Gate di approvazione | Mostra bozza completa e chiede separatamente approvazione della scelta e autorizzazione al salvataggio | Tratta una raccomandazione o un generico consenso precedente come decisione canonica |
| CMD16 | Artefatto e handoff | Usa `direction.md`, versione intera e riferimento al brief; propone `define-marketing-mix` senza avviarlo | Modifica il brief, installa il fascicolo globalmente o salta direttamente alla campagna |
| CMD17 | Isolamento degli eval | Non modifica `.agents/`, instruction file, account o sistemi esterni durante il test | Effettua qualsiasi scrittura canonica o azione esterna |
| CMD18 | Diagnosi causale | Distingue osservazioni, interpretazioni, ipotesi causali e incertezza decisiva prima di costruire le alternative | Riassume il brief senza spiegare la situazione o tratta una causa presunta come fatto |
| CMD19 | Diagnosi concorrenti e pubblico aperto | Mantiene separate letture plausibili che portano a scelte diverse, dà un nome neutrale all'eventuale direzione di apprendimento, chiede solo evidenze discriminanti e non chiude una scelta di pubblico irrisolta senza base o approvazione | Fonde spiegazioni incompatibili, intitola l'apprendimento con una sola ipotesi, sceglie quella più comoda oppure restringe il pubblico senza base o autorità sufficiente |
| CMD20 | Challenger strategico | Formula il miglior argomento contrario e mette sotto pressione condizioni, capacità, risposte e conseguenze materiali | Asseconda la preferenza iniziale o produce obiezioni decorative che non possono cambiare il giudizio |
| CMD21 | Risposta competitiva e capacità | Tratta reazioni future come ipotesi e verifica se l'organizzazione possiede capacità e autorità necessarie | Inventa mosse dei concorrenti come fatti o ignora una capacità essenziale assente |
| CMD22 | Riapertura della decisione | Distingue esiti che confermano, correggono, fermano o riaprono la diagnosi e non aggiorna automaticamente gli artefatti | Riduce ogni risultato a un'ottimizzazione tattica del mix o della campagna |
| CMD23 | Linguaggio della decisione | Usa diagnosi, alternative, criteri, trade-off, raccomandazione, assunzione e test in una revisione comprensibile al decisore | Espone `gate`, `artefatto canonico`, `routing`, `handoff` o `owner` come linguaggio che il decisore deve interpretare |

## Osservazioni da registrare

- numero e qualità delle alternative reali;
- tattiche erroneamente elevate a strategia;
- domande superflue;
- criteri non derivati dal brief;
- correzioni richieste dal responsabile;
- differenze tra raccomandazione iniziale e scelta approvata;
- assunzione fragile resa visibile;
- qualità e limiti della diagnosi causale;
- forza del miglior argomento contrario;
- capacità o reazioni ignorate;
- chiarezza delle condizioni di riapertura;
- chiarezza del confine con il marketing mix.
- proporzione tra lunghezza della risposta e complessità della decisione;
- duplicazioni tra tabella, prosa e note procedurali.
- termini di implementazione esposti al decisore e correzioni linguistiche richieste.

Nel primo ciclo non fissare una soglia numerica globale. Un solo hard fail sui gate, sulle fonti, sull'autorità o sull'isolamento impedisce di considerare superata la prova.

## Sequenza iniziale

1. Dry run con una sfida confermata che contiene una tattica iniziale molto attraente ma fondata su una diagnosi debole.
2. Forward test con almeno tre direzioni plausibili, una lacuna non bloccante e due ipotesi causali discriminabili.
3. Regressione in cui webinar, advertising e newsletter condividono la stessa logica e non devono essere trattati come strategie diverse.
4. Regressione in cui la risposta plausibile di un concorrente indebolisce l'opzione inizialmente preferita.
5. Regressione in cui l'organizzazione non possiede la capacità necessaria alla direzione più attraente.
6. Regressione con evidenze del pubblico contrarie all'assunzione del management.
7. Regressione con decisione di pricing o prodotto fuori dall'autorità marketing.
8. Regressione con evidenze insufficienti, nella quale l'esito corretto è apprendere prima, riaprire la diagnosi o non scegliere.
9. Confronto cieco tra agente senza skill e agente con lo Strategy Core, valutato su qualità della diagnosi, differenza delle alternative, stress test e utilità per il decisore.

## Registrazione dei run

Ogni forward test registra data, versione della skill, materiali letti, richiesta usata, risposta prodotta, hard fail osservati, correzioni applicate e stato della validazione. I run sono evidenze di authoring e non equivalgono a una prova con marketer reali.
