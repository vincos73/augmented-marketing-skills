# Baseline decisionale per il debrief

Leggi questo riferimento quando la review passa a `campaign-debrief`, anche se non viene creato un file. Trasferisci una sintesi compatta senza duplicare la Campaign Spec né interpretare risultati.

- **Campaign Spec:** id; versione; stato (`bozza`, `approvata`, `confirmed_in_chat`, `missing` o altro stato osservato)
- **Obiettivo o metrica decisionale:**
- **Definizione operativa:**
- **Target:**
- **Finestra:**
- **Cutoff:**
- **Maturità del dato:**
- **Baseline o comparatore:** valore o regola; stato probatorio
- **Asset revisionati:** id; versione; canale
- **Esito e rilievi aperti:**
- **Decisione di autorizzazione:** stato; evidenza
- **Esecuzione osservata:** stato; evidenza
- **Riferimenti alle evidenze:**
- **Unknowns:**
- **Confronto descrittivo con target o regola:** predisposto / non disponibile; dati già disponibili; dati ancora richiesti
- **Confronto incrementale, causale o controfattuale:** predisposto / non disponibile; motivo e stato di baseline, comparatore o controllo

Il confronto descrittivo è predisposto quando sono disponibili target o regola, definizione operativa e finestra o maturità. Sarà eseguito da `campaign-debrief` soltanto dopo l'arrivo di risultati osservati maturi. Una baseline mancante non blocca questo confronto. Il confronto incrementale, causale o controfattuale richiede invece una base comparabile adeguata e non può essere dedotto dallo scarto rispetto al target.

## Fedeltà al momento della decisione

Conserva identità, versione e stato della spec anche quando esiste solo in conversazione. Campi mancanti restano `missing` o `unknown`: non completarli da risultati, benchmark o obiettivi vicini. Una regola qualitativa, un cutoff o una condizione di maturità vanno trasferiti fedelmente, senza ridurli a un target numerico più semplice.

Autorizzazione ed esecuzione osservata sono stati separati. Se manca una base sufficiente, indica quali confronti non sono predisposti e quali dati servono: non dichiarare indisponibile anche il confronto descrittivo quando target/regola, definizione e finestra sono già disponibili.
