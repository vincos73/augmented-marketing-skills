# Author self-check: Fabriloom results v0.1.0

- Data: 2026-08-31
- Skill osservata: `campaign-debrief` v0.1.0
- Modalità: collegata, prima risposta
- Indipendenza: no; l'autore ha progettato skill, fixture e oracolo
- Azioni autorizzate: sola lettura; nessun file canonico o azione esterna

Questo controllo serve a verificare coerenza interna e copertura iniziale. Non sostituisce un forward test cieco con un valutatore indipendente.

## Materiali usati

- `user-request.md`
- `campaign-spec.md`
- `campaign-review.md`
- `execution-log.md`
- `results.md`

## Prima risposta formulata

Base utilizzata: Campaign Spec v1, review pre-lancio del 18 settembre, registro dell'esecuzione e risultati con cutoff 1 novembre. Il cambio non approvato della landing, cinque richieste senza sorgente e l'outbound Sales su sette account limitano il confronto per configurazione e canale.

### Lettura in breve

La campagna mostra un segnale commerciale promettente nel perimetro owned, ma oggi non va presentata come successo assoluto né usata per sostenere l'estensione da 15.000 euro. Le 17 richieste qualificate sono inferiori al target di pianificazione di 20; altre cinque non sono ancora valutate. I quattro Sprint avviati non hanno ancora una finestra a 45 giorni matura per tutte le coorti e non sono attribuibili causalmente alla campagna.

### Atteso, eseguito e osservato

| Tema | Atteso | Eseguito e osservato |
|---|---|---|
| Pubblico e landing | Ruoli qualificati, richiesta ESG attiva e disponibilità allo Sprint | Dal 9 ottobre pubblico ampliato e due campi di prequalifica rimossi |
| Richieste qualificate | Target 20 | 12 su 16 form con v1; 5 su 11 con v2; 5 form ancora da valutare |
| Misura e follow-up | Sorgente affidabile, contatto entro 2 giorni, massimo 6 call/settimana | 5 sorgenti mancanti; 3 follow-up dopo 5 giorni nella settimana di picco |

La quota qualificata più bassa nella v2 è coerente con un pubblico e un form più larghi, ma non ne dimostra l'effetto: periodi e volumi sono piccoli, sette account hanno ricevuto anche contatto Sales e la provenienza manca per cinque richieste. La campagna di marzo non è una baseline equivalente.

### Decisione consigliata

Non richiedere ora lo sblocco del paid. Continuare soltanto il perimetro owned già autorizzato, senza aumentarne la distribuzione, e riaprire `design-campaign` se si vuole mantenere la landing v2 o il pubblico ampliato.

Prima del nuovo controllo:

1. **Sales Director:** classificare le cinque richieste aperte e verificare l'impatto dei ritardi entro il 6 novembre.
2. **Growth Operations:** ripristinare una sorgente stabile e definizioni invarianti prima di una nuova finestra comparabile.
3. **Marketing Director:** riesaminare l'estensione il 16 dicembre, quando anche le richieste finali avranno raggiunto la finestra a 45 giorni, tenendo separate v1, v2 e account toccati dall'outbound.

Nessuna spesa, modifica della landing o del tracking è autorizzata da questa lettura. Nessun artefatto è stato creato.

## Valutazione dell'autore

- Parole della risposta: 375
- Domande: 0
- Hard fail: 0
- Soft fail: 0 osservati dall'autore
- Copertura: decisione prima delle domande; atteso, eseguito e osservato separati; denominatori visibili; output, richieste e business distinti; causalità limitata; confronto di marzo qualificato; capacità Sales considerata; ritorno a `design-campaign`; nessuna autorizzazione o scrittura.

## Limiti

Il controllo non è cieco e non confronta la candidata con un buon agente generalista, il workflow abituale del responsabile o uno specialista Analytics. Il conteggio parole e la classificazione devono essere ricontrollati automaticamente e poi verificati in un forward test indipendente.
