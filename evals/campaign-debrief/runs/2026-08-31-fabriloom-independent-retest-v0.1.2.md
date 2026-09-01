# Retest indipendente: Fabriloom results v0.1.2

- Data: 2026-08-31
- Skill osservata: `campaign-debrief` v0.1.2
- Modalità: collegata, prima risposta
- Generatore: nuovo subagent indipendente con contesto vuoto
- Valutatore: nuovo subagent indipendente con contesto vuoto
- Azioni autorizzate: sola lettura; nessun file canonico o azione esterna
- Esito: FAIL

## Protocollo

Il generatore ha letto soltanto `SKILL.md`, gli eventuali riferimenti indicati dalla skill e i cinque input business della fixture Fabriloom results. Non ha ricevuto catalogo, oracolo, blueprint, run precedenti, documenti di stato, output temporanei o conclusioni attese. Il suo output è stato congelato senza correzioni.

Il valutatore ha poi letto skill, stessi input, output congelato, catalogo eval e oracolo. Non ha letto run precedenti o author self-check.

## Prima risposta del generatore

Base utilizzata: Campaign Spec v1, review pre-lancio, registro di esecuzione e risultati al 1° novembre 2026. La review era “pronta con condizioni”, ma la landing v2, il pubblico ampliato, l’attività outbound concomitante e il problema CRM non sono stati riesaminati e limitano il confronto.

### Lettura in breve

Non presenterei la campagna come un successo pienamente dimostrato e domani non chiederei lo sblocco dei 15.000 euro. Nel perimetro osservato emerge un segnale commerciale positivo, ma il target di 20 richieste qualificate non è ancora raggiunto: risultano 17 qualificate su 27 form, con 5 richieste ancora da valutare.

### Atteso ed eseguito

L’esecuzione ha rispettato esclusione del paid, offerta, prezzo e claim qualitativo. Dal 9 ottobre, però, la landing v2 ha rimosso due campi di prequalifica e ampliato il pubblico a “fornitori industriali”. Inoltre, 48 account sono stati contattati direttamente da Sales e 7 aziende richiedenti compaiono anche nell’outbound. Questa configurazione diverge materialmente dalla spec approvata.

### Risultati osservati

- Output: 612 email consegnate, 10 contenuti LinkedIn, 226 registrazioni e 101 partecipanti live.
- Comportamento: 27 form inviati; 17 qualificati, 5 non qualificati e 5 pendenti.
- Business: 9 proposte inviate e 4 Sprint acquistati e avviati. La finestra di 45 giorni non è ancora matura per le richieste più recenti.
- Operatività: nella settimana di picco, 3 richieste su 9 hanno ricevuto follow-up dopo cinque giorni anziché entro due.

### Che cosa si può sostenere

La campagna è associata a domanda qualificata e a primi esiti commerciali nel periodo. Non possiamo attribuirle causalmente i quattro acquisti, né distinguere l’apporto dei singoli canali: 5 richieste su 27 non hanno sorgente e per 7 account l’effetto della campagna non è separabile dall’outbound Sales.

Il confronto tra landing v1 e v2 è solo indicativo: v1 registra 12 qualificate su 16 form, con 2 pendenti; v2 5 su 11, con 3 pendenti. Pubblico, form, periodo e attività commerciale concomitante non sono comparabili.

### Decisione consigliata

Domani: presentare il risultato come segnale promettente ma inconclusivo e non richiedere ancora il paid.

Entro il 6 novembre, il Sales Lead dovrebbe classificare le 5 richieste pendenti e verificare il backlog. La Marketing Director dovrebbe riaprire `design-campaign` per riesaminare pubblico, promessa, landing e prequalifica. Il responsabile Analytics, da confermare, dovrebbe verificare stabilità e copertura dell’attribuzione.

Nuovo controllo il 17 dicembre, con finestra business maturata, tracking stabile, capacità Sales sotto controllo e configurazione nuovamente approvata. Solo allora valutare un test paid limitato e reversibile.

Nessun file creato e nessuna azione operativa applicata.

## Valutazione indipendente

- Parole: 414, intestazioni incluse
- Hard fail: 0
- Soft fail: 4 aree materiali

### Soft fail

1. **LR06:** per le 17 richieste qualificate non indica nella risposta definizione e fonte Sales/CRM insieme a cutoff e denominatore.
2. **LR09:** omette la baseline di marzo e le ragioni osservate della non comparabilità, cioè pubblico, offerta e copertura della sorgente.
3. **LR11:** non decide se continuare, correggere, limitare o sospendere il perimetro owned corrente; il controllo finale e l'eventuale test paid non hanno un responsabile unico.
4. **FLR05:** rende visibili i tre follow-up tardivi, ma non li collega al limite documentato di sei call qualificate a settimana.

### Osservazione di autorità

`Sales Lead` non è un ruolo osservato nei materiali; la fixture identifica `Sales Director`. Un ruolo non osservato deve restare `da confermare` e non può essere normalizzato o inventato.

## Decisione sul test

FAIL senza hard fail. La v0.1.2 supera causalità, fotografia pre-lancio, denominatori completi e ritorno a `design-campaign`. Correggere provenienza della metrica decisiva, baseline, decisione sul perimetro corrente, capacità numerica e owner esatti prima di un nuovo retest.
