# Retest indipendente: Fabriloom results v0.1.1

- Data: 2026-08-31
- Skill osservata: `campaign-debrief` v0.1.1
- Modalità: collegata, prima risposta
- Generatore: nuovo subagent indipendente con contesto vuoto
- Valutatore: nuovo subagent indipendente con contesto vuoto
- Azioni autorizzate: sola lettura; nessun file canonico o azione esterna
- Esito: FAIL

## Protocollo

Il generatore ha letto soltanto `SKILL.md`, gli eventuali riferimenti indicati dalla skill e i cinque input business della fixture Fabriloom results. Non ha ricevuto catalogo, oracolo, blueprint, run precedenti, documenti di stato, output temporanei o conclusioni attese. Il suo output è stato congelato senza correzioni.

Il valutatore ha poi letto skill, stessi input, output congelato, catalogo eval e oracolo. Non ha letto run precedenti o author self-check.

## Prima risposta del generatore

Base utilizzata: Campaign Spec v1, review pre-lancio, registro di esecuzione del 21 settembre-1 novembre e risultati CRM/analytics al 1 novembre. Il cambio di landing, l’outbound Sales concomitante e cinque richieste senza sorgente limitano attribuzione e confrontabilità.

### Lettura in breve

Non è ancora difendibile presentare l’iniziativa come un successo complessivo né chiedere lo sblocco dei 15.000 euro. Nel perimetro owned-first emerge però un segnale commerciale promettente: 17 richieste qualificate e 4 Sprint avviati, con risultati business ancora immaturi.

### Atteso ed eseguito

Il target era 20 richieste qualificate, con pubblico ristretto e prequalifica nel form. Dal 9 ottobre la landing v2 ha ampliato il pubblico a «fornitori industriali» e rimosso due campi decisivi. Inoltre, 48 account sono stati contattati da Sales e sette richiedenti appartengono anche a questa attività outbound. Queste divergenze impediscono di leggere i risultati come verifica pulita della Campaign Spec.

### Risultati osservati

- Output: 612 email consegnate, 10 contenuti LinkedIn, 226 registrazioni webinar.
- Comportamenti: 101 partecipanti live, 73 visualizzazioni replay, 34 click alla landing e 27 form inviati.
- Qualifica CRM al cutoff: 17 richieste qualificate su 27, 5 respinte e 5 ancora da valutare. Il target di 20 non è quindi raggiunto, ma potrebbe esserlo solo dopo la qualifica delle richieste pendenti.
- Business: 9 proposte inviate e 4 Sprint acquistati e avviati. La finestra di 45 giorni è matura soltanto per le prime richieste.
- Capacità: nel picco del 19-25 ottobre, 3 richieste su 9 hanno ricevuto follow-up dopo cinque giorni.

### Che cosa si può sostenere

Il percorso owned-first ha intercettato domanda compatibile con l’offerta e ha prodotto un segnale economico iniziale. La qualità appare migliore con landing v1: 12 qualificate su 14 già valutate, contro 5 su 8 con v2. È un’associazione indicativa, non una prova che la v2 abbia causato il peggioramento.

### Limiti e spiegazioni alternative

La riduzione della quota qualificata può dipendere dall’ampliamento del pubblico e dalla minore prequalifica, ma cinque casi sono ancora pendenti. Per sette account non è distinguibile l’effetto dell’outbound Sales; per cinque richieste manca il canale. Il confronto con marzo non è equivalente per pubblico, offerta e copertura della sorgente.

### Decisione consigliata

Domani: non richiedere ancora il budget paid. Continuare soltanto qualifica e follow-up dell’attuale coorte. Marketing Director, Sales e Analytics dovrebbero entro il 16 novembre:

1. chiudere le cinque qualifiche pendenti;
2. ricostruire, dove possibile, la sequenza dei sette account outbound;
3. verificare capacità e tempi di risposta;
4. tornare a `design-campaign` per decidere pubblico, prequalifica e landing da sottoporre a un test controllato.

Riesame il 16 novembre; nuova valutazione business alla maturazione dei 45 giorni. Nessun file creato e nessuna azione operativa applicata.

## Valutazione indipendente

- Parole: 444, intestazioni incluse
- Hard fail: 1
- Soft fail: 3
- Osservazioni: 3

### Hard fail

- **LR08, causalità:** «ha prodotto un segnale economico iniziale» collega il percorso al risultato economico senza disegno causale; outbound Sales e assenza di controllo impediscono l'attribuzione.

### Soft fail

1. **LR02:** non qualifica la review `pronta con condizioni` come fotografia pre-lancio né esplicita che la divergenza successiva non è stata riesaminata.
2. **FLR02:** usa 12/14 e 5/8 tra i casi valutati senza mostrare anche i denominatori totali 12/16 e 5/11, rendendo meno visibile la distribuzione dei pendenti.
3. **LR11:** assegna collettivamente quattro attività a Marketing Director, Sales e Analytics; mancano un responsabile per azione e criteri osservabili per tracking e capacità prima di un futuro paid test.

## Decisione sul test

FAIL. La v0.1.1 risolve comparabilità con marzo, decisione sul perimetro corrente e ritorno esplicito a `design-campaign`, ma non supera il controllo causale. Correggere solo i comportamenti osservati e ripetere con agenti nuovi.
