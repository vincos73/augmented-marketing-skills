# Retest indipendente: Fabriloom results v0.1.3

- Data: 2026-08-31
- Skill osservata: `campaign-debrief` v0.1.3
- Modalità: collegata, prima risposta
- Generatore: nuovo subagent indipendente con contesto vuoto
- Valutatore: nuovo subagent indipendente con contesto vuoto
- Azioni autorizzate: sola lettura; nessun file canonico o azione esterna
- Esito: PASS con rilievi

## Protocollo

Il generatore ha letto soltanto `SKILL.md`, gli eventuali riferimenti indicati dalla skill e i cinque input business della fixture Fabriloom results. Non ha ricevuto catalogo, oracolo, blueprint, run precedenti, documenti di stato, output temporanei o conclusioni attese. Il suo output è stato congelato senza correzioni.

Il valutatore ha poi letto skill, stessi input, output congelato, catalogo eval e oracolo. Non ha letto run precedenti o author self-check.

## Prima risposta del generatore

Base utilizzata: Campaign Spec v1, review pre-lancio, registro dell’esecuzione dal 21 settembre al 1 novembre e risultati con cutoff al 1 novembre. La review dichiarava la campagna pronta con condizioni prima del lancio. La landing v2 non è stata riesaminata. Cinque sorgenti mancanti e sette account coinvolti anche nell’outbound Sales limitano l’attribuzione.

### Lettura in breve

La campagna mostra un segnale di domanda promettente, ma non può ancora essere presentata come un successo né come prova sufficiente per sbloccare 15.000 euro di paid media.

### Atteso ed eseguito

L’obiettivo era ottenere 20 richieste qualificate mantenendo pubblico, prequalifica, tracking e capacità affidabili. Dal 9 ottobre la landing ha ampliato il pubblico a «fornitori industriali» e rimosso due campi necessari alla prequalifica. Inoltre, Sales ha contattato direttamente 48 account. Questa configurazione diverge dalla Campaign Spec e non è stata riesaminata.

### Risultati osservati

Sono stati registrati 27 form, di cui 17 qualificati, 5 respinti e 5 ancora da valutare. La metrica decisiva è la richiesta qualificata secondo la definizione della Campaign Spec, classificata da Sales: 17 su 27 al cutoff del 1 novembre, con 5 casi pendenti.

Gli altri livelli restano distinti:

- Output e comportamento: 612 email consegnate, 226 registrazioni, 101 partecipanti live, 34 click e 27 form.
- Business: 9 proposte e 4 Sprint acquistati e avviati. La finestra di 45 giorni non è ancora matura per le richieste recenti e manca un gruppo di controllo.

### Che cosa possiamo sostenere

Nel periodo osservato esiste interesse coerente con l’offerta. Non possiamo attribuire alla campagna i risultati dei sette account sovrapposti all’outbound, né concludere che il percorso sia scalabile. La campagna di marzo offre solo un ordine di grandezza: pubblico, offerta e copertura della sorgente erano differenti, quindi non costituisce una baseline equivalente.

### Limiti materiali

La landing v1 registra 12 qualificate su 16 form, con 2 pendenti; la v2 5 su 11, con 3 pendenti. Il segnale è compatibile con un peggioramento della qualità, ma volumi, casi pendenti e modifiche simultanee non permettono di isolarne la causa. Nella settimana di picco sono arrivate 9 richieste: il limite di 6 call settimanali ha comportato 3 follow-up dopo cinque giorni.

### Decisione consigliata

Non richiedere ora lo sblocco del paid. Limitare il perimetro corrente al completamento del follow-up, senza nuova distribuzione.

- **Sales:** classificare i 5 casi pendenti e completare il follow-up.
- **Marketing Director:** riaprire pubblico e landing tramite `design-campaign`.
- **Responsabile da confermare:** rendere stabile il tracciamento della sorgente.
- **Marketing Director:** riesaminare la decisione paid dopo la maturazione dei casi recenti, entro il 16 dicembre, verificando qualifica, tempi di follow-up e capacità disponibile.

Nessun file creato e nessuna modifica operativa applicata.

## Valutazione indipendente

- Parole: 443, intestazioni incluse
- Hard fail: 0
- Soft fail: 3 aree
- Esito finale: PASS

### Controlli superati

- decisione prima delle domande;
- spec, review pre-lancio, esecuzione e risultati distinti;
- perimetro e cutoff visibili;
- causalità limitata e spiegazioni alternative materiali;
- baseline di marzo qualificata per pubblico, offerta e copertura;
- denominatori completi v1 e v2 con pendenti;
- capacità collegata a limite di sei call, nove richieste e tre ritardi;
- paid non sostenuto né autorizzato;
- scelta esplicita di limitare il perimetro corrente;
- ritorno a `design-campaign`;
- responsabili osservati o da confermare;
- nessun file o azione esterna.

### Soft fail residui

1. **LR06:** la definizione operativa della richiesta qualificata è rinviata alla Campaign Spec e la fonte CRM non è nominata esplicitamente nella frase decisiva.
2. **LR07:** output e comportamento vengono accorpati in un solo punto, pur senza essere usati impropriamente come outcome.
3. **LR10-LR11:** il controllo del 16 dicembre non richiede esplicitamente una nuova coorte osservata con definizione, landing e tracking stabili prima del riesame paid.

## Limiti del PASS

Il run verifica soltanto la prima risposta collegata sulla fixture Fabriloom results. Non prova il percorso standalone, turni successivi, persistenza di `campaign-learning.md`, confronto con workflow abituale o specialista Analytics, installazione, package, runtime o uso con marketer esterni.
