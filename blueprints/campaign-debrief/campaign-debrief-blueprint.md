---
artifact: campaign-debrief-blueprint
version: 0.1
status: pronta
last_reviewed: 2026-09-01
implementation_status: source-v0.1.6-ready
---

# Blueprint di `campaign-debrief`

## Decisione

`campaign-debrief` è il terzo modulo del Campaign Core. Si attiva quando una campagna, una fase o un test hanno prodotto abbastanza osservazioni per sostenere una decisione, anche se non bastano a dimostrare una causa.

Il nome rende memorabile la sequenza `design-campaign` → `campaign-review` → `campaign-debrief`. La promessa visibile è: **leggere i risultati e decidere il prossimo passo**.

Non è una dashboard, un generatore di report, un sostituto di Analytics o un rituale di chiusura. Risponde alla domanda: alla luce di ciò che è stato realmente eseguito e osservato, che cosa conviene continuare, correggere, approfondire, ampliare o fermare?

## User story e decisione posseduta

Come responsabile marketing, confronto ciò che volevamo ottenere, ciò che abbiamo realmente fatto e ciò che i dati permettono di sostenere. Rendo visibili limiti e spiegazioni alternative e approvo una decisione successiva proporzionata alla qualità delle osservazioni.

La skill raccomanda che cosa fare dopo rispetto a uno specifico periodo, pubblico, canale, asset o passaggio della campagna. Non dichiara se la campagna ha funzionato in assoluto.

Ogni risposta chiarisce perimetro e finestra, atteso e osservato, esecuzione reale, limiti dei dati, conclusioni sostenute, decisione consigliata e prossima verifica. Le decisioni possono essere continuare, correggere, estendere con cautela, fermare, attendere una finestra più matura, fare un confronto più informativo o riaprire una scelta.

## Confini

`design-campaign` definisce obiettivo, pubblico, percorso, messaggi, misure e regole prima dell'esecuzione. `campaign-debrief` usa quella base ma non la riscrive per far coincidere previsione e risultato. Se cambia una scelta fondamentale, propone il ritorno a `design-campaign`.

`campaign-review` verifica la prontezza prima dell'azione. `campaign-debrief` verifica che cosa è accaduto dopo e ricostruisce sempre l'esecuzione effettiva, comprese modifiche a landing, pubblico, budget, timing, follow-up o tracking.

Analytics, CRM, piattaforme media, vendite e ricerca forniscono eventi e osservazioni. La skill non inventa dati, non corregge tracking e non sostituisce il QA analitico: possiede la sintesi decisionale.

Un risultato locale non diventa automaticamente una regola stabile. La skill può proporre aggiornamenti a Campaign Spec, direzione o Marketing Foundations, ma non modifica materiali approvati e non generalizza oltre condizioni, pubblico e periodo osservati.

## Input e modalità di ingresso

Per iniziare bastano decisione o domanda, campagna o periodo e risultati o materiali autorizzati. Progressivamente possono servire obiettivo originario, pubblico, offerta, percorso reale, date, versioni, budget, capacità, metriche con definizione e fonte, baseline comparabile, modifiche, anomalie e Campaign Spec o review.

Nel percorso standalone ricostruisce una base minima da brief, materiali, note, risultati e dichiarazioni del responsabile. Chiede al massimo tre conferme e non ricostruisce a posteriori una previsione originaria.

Nel percorso collegato usa la Campaign Spec approvata, il perimetro della review, il registro dell'esecuzione, i dati osservati e la decisione attuale. Non riapre la catena strategica senza un conflitto materiale.

## Sufficienza dei dati

La sufficienza dipende dalla decisione, non da una soglia universale. Verifica maturità della finestra, definizioni, tracking, denominatori, volume, segmentazione, comparabilità, modifiche, distanza tra piano ed esecuzione e costo o reversibilità della scelta.

Se i dati non bastano, indica che cosa si può decidere ora, che cosa resta sospeso e quale osservazione ha il maggior valore informativo. Non risponde soltanto “servono più dati”.

## Prima risposta e metodo

La prima risposta utile presenta lettura del risultato, conclusioni sostenute, incertezze, decisione consigliata, azione, responsabile e momento del nuovo controllo. Resta entro 500 parole e pone da zero a tre richieste decisive.

Il metodo è: fissare la decisione; ricostruire l'esecuzione effettiva; verificare definizioni e copertura; confrontare atteso e osservato; separare output, comportamenti e risultati di business; valutare spiegazioni alternative; raccomandare il passo successivo in proporzione a solidità, costo e reversibilità.

Non trasformare correlazioni in causalità. Considerare, quando plausibili, pubblico, offerta, stagionalità, attività commerciali, eventi esterni, tracking, campione e cambiamenti intervenuti.

## Output e persistenza

Per default produce in chat una decisione sui risultati con fonti, perimetro, osservazioni, limiti, raccomandazione e prossima verifica. Un file è utile solo se la decisione deve essere condivisa, approvata o conservata oltre la conversazione; dopo autorizzazione aggiorna un solo `campaign-learning.md` nel fascicolo della campagna. Non crea un documento per metrica, canale o riunione.

L'approvazione della lettura non autorizza modifiche a campagne, budget, piattaforme, Campaign Spec, Marketing Foundations o playbook.

## Fixture ed eval da validare

La prima fixture deve includere almeno quattro-sei settimane, previsione datata, esecuzione reale, risultati per più fasi, modifica a metà periodo, limite di tracking, fattore alternativo plausibile e vincolo di capacità o costo.

Gli eval coprono percorso collegato e standalone, dati insufficienti, confronto improprio, esecuzione divergente, segnale misto, tracking cambiato, decisione reversibile, richiesta di scalare senza autorità e proposta di aggiornamento stabile non applicata. Prima di impacchettare, installare o proporre la pubblicazione della candidata vanno confrontati buon agente generalista, workflow abituale e Analytics specialist.
