# Regressione collegata: Fabriloom v0.1.6

- Data: 2026-08-31
- Modalità: collegata, prima risposta
- Input: richiesta, Campaign Spec, review pre-lancio, esecuzione e risultati
- Output: 480 parole
- Hard fail: 0
- Soft fail: 3
- Esito: PASS con rilievi
- SHA-256: `d0dd08f38414231b55c69cc15144d8cf31acb964a27ea1ac2595d0b5513787de`

## Risposta del generatore

Base utilizzata: Campaign Spec v1, review pre-lancio, registro di esecuzione e risultati al 1 novembre 2026, per la campagna owned-first in Italia. La review era “pronta con condizioni”, ma descriveva lo stato pre-lancio: landing v2, ampliamento del pubblico e rimozione dei campi di prequalifica non sono stati riesaminati.

### Lettura in breve

Non presenterei la campagna come un successo che giustifica 15.000 euro di paid media. Nel perimetro osservato emerge domanda, ma non sono ancora affidabili configurazione, attribuzione e capacità di follow-up. Domani conviene non chiedere a Finance lo sblocco del budget.

### Atteso ed eseguito

Il target di pianificazione era 20 richieste qualificate, con paid escluso, pubblico circoscritto e form coerente con la definizione di qualifica. Dal 9 ottobre la landing v2 ha ampliato il testo a “fornitori industriali” e rimosso due criteri di prequalifica. Inoltre, 48 account sono stati contattati da Sales e sette richiedenti compaiono anche nell'outbound.

### Risultati osservati

- **Output:** 612 email consegnate, 10 contenuti LinkedIn, 226 registrazioni, 101 partecipanti live e 73 avvii qualificati del replay.
- **Comportamento:** 27 form inviati. La metrica decisiva è “richiesta qualificata” secondo i quattro criteri della Spec, applicati da Sales e registrati nel CRM: al cutoff del 1 novembre sono 17 su 27 form, con 5 non qualificate e 5 ancora da valutare. Sui soli 22 casi valutati, 17 sono qualificati.
- **Business:** 9 proposte e 4 Sprint acquistati e avviati. La finestra di 45 giorni è matura solo per le prime richieste e manca un gruppo di controllo.

### Che cosa si può sostenere

La campagna ha superato il precedente ordine di grandezza di 11 call qualificate, ma marzo non è una baseline equivalente: pubblico e offerta erano diversi e anche allora mancava la sorgente per cinque richieste. I quattro Sprint sono un'associazione osservata nel periodo, non un effetto attribuibile alla campagna.

### Limiti e spiegazioni alternative

Cinque richieste non hanno sorgente; per sette account outbound e campagna non sono separabili; v1 e v2 non sono confrontabili pulitamente. La capacità dichiarata era sei call qualificate a settimana: nel picco di nove richieste, tre follow-up sono slittati da due a cinque giorni. Un aumento di distribuzione rischierebbe quindi di ampliare il ritardo prima di chiarire la qualità della domanda.

### Decisione consigliata

1. **Limitare il perimetro corrente e non attivare paid.** La Marketing Director riapra pubblico, landing e percorso in `design-campaign`, senza modifiche operative implicite.
2. **Controllo intermedio entro il 6 novembre.** Sales classifichi i cinque casi pendenti; `da confermare` verifichi sorgenti, tracking stabile e recupero del backlog. Questo controllo non autorizza il paid.
3. **Nuovo riesame paid:** Marketing Director, solo dopo una nuova coorte owned con configurazione approvata, definizione e tracking stabili, chiusa e interamente qualificata, con follow-up entro capacità. Se la decisione deve includere l'esito business, attendere anche 45 giorni dall'ultima richiesta della coorte.

Salvataggio: nessun artefatto canonico creato; questa è soltanto la risposta dell'eval.

## Valutazione indipendente

Tutti i controlli hard sono superati. Restano tre soft fail:

1. **LR06:** la definizione operativa rinvia ai quattro criteri della Spec senza renderli leggibili nella risposta.
2. **LR07:** registrazioni, partecipanti e replay sono classificati come output anziché comportamento.
3. **FLR02:** la divergenza v1/v2 è registrata, ma mancano i rapporti 12/16 e 5/11.

Review pre-lancio, divergenze, denominatori complessivi, causalità, baseline, capacità, paid, `design-campaign`, controllo intermedio, nuova coorte, owner e confini sono PASS. Sicurezza dichiarata: superiore al 90%.
