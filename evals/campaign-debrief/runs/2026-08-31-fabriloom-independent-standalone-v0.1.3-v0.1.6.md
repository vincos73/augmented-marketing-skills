# Percorso standalone indipendente: Fabriloom v0.1.3-v0.1.6

- Data: 2026-08-31
- Modalità: standalone, prima risposta
- Input del generatore: `user-request.md`, `execution-log.md`, `results.md`
- Input esclusi: Campaign Spec, review, catalogo, oracolo, blueprint e run precedenti
- Azioni autorizzate: sola lettura; output congelati in `/tmp`

## Progressione osservata

| Versione | Parole | Hard fail | Soft fail | Esito | Correzione successiva |
|---|---:|---:|---:|---|---|
| 0.1.3 | 479 | 0 | 1 | FAIL | Separare controllo intermedio e riesame paid |
| 0.1.4 | 500 | 0 | 1 | FAIL | Rendere la coorte osservata prerequisito esplicito |
| 0.1.5 | 480 | 0 | 5 sui criteri, 4 difetti distinti | FAIL | Portare nel preflight definizione disponibile, livelli e `design-campaign` |
| 0.1.6 | 459 | 0 | 0 | PASS | Nessuna correzione |

Le valutazioni sono state svolte da agenti distinti dai generatori. La v0.1.3 anticipava il riesame paid al 9 novembre, prima della finestra business. La v0.1.4 non rendeva inequivocabile che la nuova coorte dovesse essere realmente eseguita e osservata. La v0.1.5 risolveva il gate, ma perdeva il routing esplicito a `design-campaign`, la disponibilità reale della definizione e la separazione dei livelli.

SHA-256 degli output congelati:

- v0.1.3: `f4140f3bbe91aae85f6cf59736d956e8fff32ab1a8d5d36cb8d124efd97fdd77`
- v0.1.4: `917f910d20d30ff9fa2d6cc224460fb4bd6f8977899d3977fab18abcd63ea1c2`
- v0.1.5: `f3a4619ea299fa2af1c9a9cb0c0850bb66d19aac8c9888ee3264faad2c2f0d22`
- v0.1.6: `104b12db029f4a30ab18b0d055a9212e5ad51edb2760451c39c4618e6c218bd0`

## Risposta finale v0.1.6

Base utilizzata: richiesta del 2 novembre, esecuzione del 21 settembre-1 novembre e risultati con cutoff 1 novembre. Mancano la previsione originaria completa e una finestra di acquisto matura. Cambio di landing, outbound sovrapposto e cinque sorgenti mancanti limitano attribuzione e confronto.

### Lettura in breve

Presenterei la campagna come **segnale promettente, non come successo dimostrato né prova sufficiente per scalare**. Al cutoff risultano 17 richieste qualificate su 27 form, 5 non qualificate e 5 pendenti. Il target dichiarato di 20 non è raggiunto; la sua base originaria non è disponibile. Domani non chiederei a Finance i 15.000 euro.

### Atteso ed eseguito

L'atteso leggibile è un percorso owned-first e un target di 20 qualificate. L'eseguito comprende email, LinkedIn, webinar e replay, senza paid né cambi di prezzo. Dal 9 ottobre la landing v2 ha ampliato il pubblico e rimosso due campi di prequalifica; dal 12 ottobre Sales ha svolto outbound sullo stesso segmento. La definizione Sales è dichiarata stabile, ma i criteri completi non sono disponibili.

### Risultati osservati

- **Output:** 612 email, 10 post, 226 registrazioni, 101 partecipanti live, 73 avvii replay.
- **Comportamento:** nel CRM al cutoff, 17/27 qualificate secondo Sales, oppure 17/22 tra i casi valutati; 5 restano pendenti. V1: 12/16, 2 pendenti; v2: 5/11, 3 pendenti. Sorgente disponibile per 22/27.
- **Business:** 9 proposte e 4 Sprint acquistati e avviati. Manca il denominatore che ha completato la finestra di 45 giorni, quindi non è calcolabile un tasso maturo.

### Che cosa si può sostenere

Nel periodo esistono domanda qualificata e acquisti associati al percorso. Non si può attribuire il risultato all'owned, isolare il contributo dei canali o concludere che il paid lo replicherebbe. Marzo, con 11 call qualificate e 3 acquisti, è solo un ordine di grandezza: pubblico, offerta e copertura della sorgente erano diversi.

### Limiti e alternative

Il mix della v2 può spiegare la diversa qualità; i pendenti possono cambiare il target; outbound e campagna non sono separabili per sette aziende. Nella settimana di picco, 3 richieste su 9 hanno atteso cinque giorni: la capacità dichiarata di 6 call settimanali non ha sostenuto il carico tempestivamente.

### Decisione consigliata

Limitare il perimetro corrente alla chiusura e maturazione dei casi acquisiti. Entro il 6 novembre, un responsabile Sales **da confermare** chiuda i cinque pendenti e aggiorni proposte e follow-up. Entro il 9 novembre, la Marketing Director controlli classificazione completa, backlog, sorgenti e capacità: non è un gate di spesa.

Prima di estendere, la Marketing Director riapra `design-campaign` per approvare pubblico, landing, qualifica, separazione dall'outbound ed eventuale pilot paid reversibile con tetto e stop; il tracking spetta a un responsabile **da confermare**. La Marketing Director riesamini i 15.000 euro solo dopo una nuova coorte stabile, chiusa e osservata per 45 giorni dall'ultima richiesta.

## Valutazione finale

Tutti i controlli LR applicabili e FLR01-FLR08 sono PASS. Il valutatore ha verificato assenza di spec, definizione non disponibile, causalità, denominatori, capacità, controllo intermedio, coorte osservata, `design-campaign`, owner e confini. Sicurezza dichiarata: 95%.
