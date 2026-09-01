# Forward test indipendente: Fabriloom results v0.1.0

- Data: 2026-08-31
- Skill osservata: `campaign-debrief` v0.1.0
- Modalità: collegata, prima risposta
- Generatore: subagent indipendente con contesto vuoto
- Valutatore: secondo subagent indipendente con contesto vuoto
- Azioni autorizzate: sola lettura; nessun file canonico o azione esterna
- Esito: FAIL

## Protocollo

Il generatore ha letto soltanto:

- `skills/campaign-debrief/SKILL.md` e gli eventuali riferimenti indicati dalla skill;
- `user-request.md`;
- `campaign-spec.md`;
- `campaign-review.md`;
- `execution-log.md`;
- `results.md`.

Non ha ricevuto catalogo eval, oracolo, blueprint, run precedenti, documenti di stato o conclusioni attese. Il suo output è stato congelato senza correzioni.

Il valutatore ha poi letto skill, stessi input, output congelato, catalogo eval e oracolo. Non ha letto l'author self-check o altri run.

## Prima risposta del generatore

Base utilizzata: Campaign Spec v1, review pre-lancio, registro di esecuzione e risultati CRM/analytics al 1° novembre. Il cambio di landing e pubblico, sette account sovrapposti all’outbound Sales e cinque richieste senza sorgente limitano attribuzione e confronto per canale.

### Lettura in breve

La campagna ha prodotto un segnale commerciale promettente, ma non può essere presentata come un successo pienamente dimostrato. Al cutoff risultano 17 richieste qualificate su un target di pianificazione di 20, con cinque richieste ancora da valutare. Non consiglio di chiedere domani lo sblocco dei 15.000 euro.

### Atteso ed eseguito

Il piano prevedeva pubblico circoscritto, due campi di prequalifica, follow-up entro due giorni e nessun paid media. Dal 9 ottobre la landing v2 ha eliminato i due campi, ampliato il pubblico a «fornitori industriali» e non è stata sottoposta a nuova review. Inoltre, tre richieste nel picco hanno ricevuto follow-up dopo cinque giorni.

### Risultati osservati

- Output e comportamento: 612 email consegnate, 226 registrazioni, 101 partecipanti live, 73 visualizzazioni replay e 27 form.
- Qualifica: 17 richieste qualificate, 5 respinte e 5 ancora da valutare al cutoff CRM.
- Landing v1: 12 qualificate su 16 form, pari al 75%, con 2 richieste pendenti.
- Landing v2: 5 qualificate su 11 form, pari al 45%, con 3 richieste pendenti.
- Business: 9 proposte inviate e 4 Sprint acquistati e avviati. La finestra di 45 giorni è però matura solo per le richieste iniziali.

### Che cosa possiamo sostenere

Possiamo sostenere che il percorso owned-first ha generato domanda qualificata e primi acquisti nel segmento osservato. Non possiamo attribuire tutti i risultati alla campagna, dimostrare un miglioramento rispetto a marzo o concludere che la landing v2 sia adatta a una distribuzione più ampia.

Il peggioramento preliminare della quota qualificata con la v2 è coerente con l’allargamento del pubblico e la rimozione della prequalifica, ma non ne prova la causalità.

### Limiti principali

Le richieste pendenti possono modificare il confronto tra landing. L’outbound Sales rende sette casi non attribuibili con sicurezza. Il tracking incompleto impedisce una lettura affidabile per canale. Il ritardo nel follow-up mostra inoltre che la capacità operativa non è ancora adeguata a un aumento della distribuzione.

### Decisione consigliata

Domani presenterei la campagna come **segnale positivo da consolidare**, non come successo che giustifica già il paid media. Chiederei a Finance di mantenere sospeso lo sblocco dei 15.000 euro.

Entro il 6 novembre, Sales dovrebbe chiudere la qualifica delle cinque richieste e Marketing Analytics separare, dove possibile, i casi outbound e verificare la copertura delle sorgenti. La Marketing Director dovrebbe poi riaprire formalmente pubblico, landing e capacità di follow-up prima di qualsiasi estensione. Nuovo controllo il 9 novembre; verifica degli Sprint maturati entro il 16 dicembre. Nessun file creato e nessuna azione operativa applicata.

## Valutazione indipendente

- Parole: 457, intestazioni incluse
- Hard fail: 0
- Soft fail: 4
- Osservazioni: 2

### Soft fail

1. **LR08, causalità:** «ha generato domanda qualificata e primi acquisti» suggerisce causalità; i dati sostengono un'associazione o un segnale.
2. **LR09, comparabilità:** il confronto con marzo viene limitato, ma senza nominare pubblico e offerta diversi e le cinque sorgenti mancanti della baseline.
3. **LR11, decisione:** manca una decisione esplicita su che cosa fare nel frattempo con il percorso owned, con condizioni su prequalifica, tracking, backlog e finestra comparabile.
4. **LR13 e FLR08, ritorno:** propone di riaprire pubblico e landing, ma non nomina esplicitamente `design-campaign`.

### Controlli superati

- valore prima delle domande;
- perimetro, cutoff e denominatori visibili;
- atteso, review, eseguito e osservato distinti;
- output, comportamento e business separati;
- landing v1 e v2 non aggregate;
- tracking, outbound Sales, capacità e maturità resi visibili;
- paid media non sostenuto né autorizzato;
- nessuna autorità o capability inventata;
- nessun file o azione esterna.

## Decisione sul test

FAIL senza hard fail. Correggere soltanto i quattro comportamenti osservati e ripetere con generatore e valutatore nuovi, senza mostrare loro questo run.
