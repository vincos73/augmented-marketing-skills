---
name: campaign-debrief
description: "Interpreta i risultati osservati di una campagna o test e raccomanda il prossimo passo, confrontando attese, esecuzione reale, qualità dei dati e limiti delle conclusioni."
metadata:
  version: "0.1.7"
---

# Leggere i risultati di una campagna

Aiuta il responsabile a decidere che cosa continuare, correggere, estendere con cautela, fermare o attendere. Il risultato è una raccomandazione applicabile a un perimetro, sostenuta dalle osservazioni e accompagnata da condizioni e prossimo controllo. Non è un report periodico automatico né una riparazione del tracking.

## Base della lettura

Lavora con Campaign Spec, eventuale review, note di esecuzione e risultati, oppure con una domanda e materiali autonomi sufficienti. Non bloccare il debrief per l'assenza di documenti della Suite. Se decisione, campagna/periodo o osservazioni non sono identificabili, chiedi ciò che manca; altrimenti fornisci subito la lettura sostenibile.

Dichiara sinteticamente materiali realmente usati, perimetro e limiti materiali. Fonti business, osservazioni, dichiarazioni e inferenze restano distinte; blueprint, eval e istruzioni della skill non sono prove della campagna.

Confronta senza fonderli:

- **atteso:** spec, target, baseline o regola documentati prima dell'esecuzione;
- **eseguito:** configurazione realmente utilizzata, modifiche, interruzioni e attività non avvenute;
- **osservato:** eventi e risultati disponibili, con fonte e finestra.

Non ricostruire a posteriori previsioni o criteri di successo. Leggi `campaign-review.md` quando disponibile e pertinente come fotografia pre-lancio: conserva il significato dei suoi stati probatori, esito e aspetti non verificati. Non dimostra che l'esecuzione sia avvenuta o sia rimasta invariata. Se la configurazione è cambiata e non risulta riesaminata, dichiaralo quando modifica la lettura.

## Misura e confronto

La metrica che governa la decisione deve avere nella risposta definizione operativa, fonte responsabile, cutoff/finestra e denominatore. Se una definizione è dichiarata stabile ma non ne sono forniti i criteri, indica che la definizione completa non è disponibile: non completarla per inferenza.

Valuta maturazione, copertura, volume, segmentazione, tracking, cambi di esecuzione e comparabilità in funzione del costo e della reversibilità della scelta. Non usare una soglia universale di sufficienza. Non aggregare eventi con definizioni diverse né confrontare percentuali senza denominatori compatibili. Con casi pendenti mostra totale e non classificati; il rapporto sui soli valutati non li sostituisce.

Quando viene fornita una baseline pertinente, indica come la usi oppure perché non è utilizzabile, nominando le differenze materiali: pubblico, offerta, periodo, definizione o copertura. Un semplice rinvio allo storico non basta. Un file o campo CRM disponibile non prova qualità o attribuzione; dati non verificabili restano forniti o dichiarati.

Il confronto descrittivo con un target o una regola documentata è possibile con definizione, finestra e osservazioni mature anche senza baseline. Il confronto incrementale o causale richiede un disegno adeguato: lo scarto dal target non dimostra incremento, causalità o ROI.

Distingui output, comportamenti intermedi, risultati di business e capacità operativa. Un click non equivale a una richiesta qualificata; spesa o impression non sono outcome. Quando la capacità limita la scelta, collega il limite dichiarato a carico e ritardi osservati.

## Conclusioni e decisione

Sostieni soltanto conclusioni riferite al perimetro osservato. Senza evidenza causale adeguata descrivi associazioni e risultati nel periodo, evitando di dire che campagna, canale o landing hanno generato domanda, pipeline o ricavi. Considera le spiegazioni alternative capaci di cambiare la decisione e, quando possibile, l'osservazione che le distinguerebbe.

Apri con la decisione operativa e le sue ragioni; rendi visibili atteso, eseguito, osservato e limiti senza imporre un numero di sezioni o parole. Quando mancano prove decisive, chiarisci che cosa si può decidere ora, che cosa resta sospeso e quale osservazione ridurrà l'incertezza. Chiedi poi al massimo tre chiarimenti ad alta conseguenza.

La raccomandazione deve indicare azione, perimetro, evidenza, condizioni, responsabile e prossimo controllo. Conserva i ruoli esatti osservati nei materiali; usa `da confermare` quando non sono noti. Assegna anche il controllo e l'eventuale decisione di test a un responsabile identificabile, senza distribuire attività a un gruppo indistinto.

Se non raccomandi un'estensione, precisa comunque se il perimetro corrente va continuato, corretto, limitato o sospeso. Un test reversibile può basarsi su un segnale indicativo con ipotesi, limite di esposizione e criterio di stop. Per paid, scala o ampliamenti leggi [i criteri per decisioni con dati incompleti](references/decision-routing.md): stabilità della misura, consenso pertinente, maturazione, follow-up, capacità, configurazione e sostenibilità economica devono sostenere la decisione. Un controllo di prontezza non sostituisce il riesame su risultati maturi.

Usa lo stesso riferimento quando definizioni, confronti o divergenze sono ambigui. Evita nuove richieste generiche di dati e, nei turni successivi, aggiorna soltanto decisioni e prove cambiate.

## Conseguenze e confini

Se occorre riprogettare pubblico, offerta, messaggio guida, landing, percorso o regola decisionale, indica esplicitamente `design-campaign` come lavoro pertinente, se disponibile. Non riscrivere la Campaign Spec come effetto collaterale del debrief. Risultati locali non diventano automaticamente nuove regole di Marketing Foundations o del playbook: proponi l'aggiornamento con la sua base e i limiti di trasferibilità.

Problemi di definizione o qualità del tracking vanno al responsabile Analytics o tecnico realmente identificato; non inventare un team né dichiarare una correzione non eseguita. La raccomandazione non autorizza budget, spesa, invio, pubblicazione o modifiche di audience e sistemi. Un'eventuale richiesta di applicarla richiede autorità e strumenti pertinenti, usando le autorizzazioni già presenti senza richiederle di nuovo.

## Conservare il learning

Rispondi in chat salvo richiesta o necessità di un documento condivisibile. Per un record persistente usa [il template del Campaign Learning](references/campaign-learning-template.md), che contiene campi, percorso e versioning. Non creare automaticamente file per ogni metrica o canale.

Approvazione della lettura, salvataggio e modifiche operative sono decisioni distinte, che possono essere autorizzate nella stessa richiesta o in turni precedenti. Completa il file richiesto come bozza se il contenuto non è ancora approvato; chiedi solo l'approvazione o autorizzazione mancante per il prossimo passo. Non assegnare uno stato approvato senza la conferma del contenuto.

Indica file e versione realmente creati. Per contenuto approvato solo in chat usa `contenuto approvato in chat; artefatto non creato`. Se una scrittura autorizzata è impossibile, consegna una versione portabile e il percorso previsto. Test, simulazioni ed eval restano fuori dai percorsi canonici, anche con approvazioni simulate.
