---
name: design-campaign
description: "Designs or updates a coordinated campaign and its execution brief covering audience, messages, channels, response, and measurement. It is not for a single, already-specified asset."
metadata:
  version: "0.1.8"
---

# Progettare una campagna

Trasforma brief e decisioni disponibili in una proposta di campagna decidibile o in una Campaign Spec utilizzabile per l’esecuzione. Parti dalla consegna richiesta, poi progetta quanto serve a completarla.

## Scegliere la consegna

- **Proposta compatta:** presenta idea e messaggio, percorso con funzione degli asset, misura e decisione. Integra vincoli e dipendenze nel punto in cui incidono; non ripetere gli stessi fatti in sezioni diverse.
- **Spec operativa:** sviluppa anche responsabilità, calendario, capacità, budget e verifiche pertinenti. Usa il [template modulare](references/campaign-spec-template.md) per una spec completa o un file, senza riprodurne ogni campo.
- **Aggiornamento:** mostra ciò che cambia e le conseguenze; ricomponi tutto il documento solo se richiesto o necessario alla consegna.

Un limite massimo guida la stesura dall’inizio: prepara una bozza sensibilmente più corta, indicativamente entro l’80% del massimo, e usa il margine per i dettagli essenziali. Il limite comprende titoli, note e domande appartenenti alla consegna. Senza un limite, usa lo spazio necessario: una specifica completa non deve diventare un riassunto.

Rispondi nella lingua dell’utente; per un documento usa la lingua esplicitamente richiesta. Preserva voce, testi protetti, citazioni originali, terminologia approvata e identificatori tecnici. Usa linguaggio da marketer; non esporre registri o controlli interni. Per un singolo asset già definito usa il builder pertinente; per una review indipendente usa `campaign-review`, se disponibile.

## Stabilire la base e la libertà di proposta

Lavora dal brief autonomo o dai contesti Identity, Marketing Foundations e Strategy disponibili. Riusa le decisioni pertinenti; non imporre nuovi documenti strategici per una campagna standalone. Documentazione della Suite ed esempi spiegano il metodo, non provano fatti sull’azienda.

Prima di formulare il messaggio distingui internamente:

- **Offerta fissata:** fatti, soggetti, requisiti pratici, modalità e vincoli ricevuti. Mantienine il significato in ogni titolo, promessa e CTA; un nome commerciale non aggiunge caratteristiche all’esperienza venduta.
- **Scelte da progettare:** enfasi, formulazione, funzione dei mezzi e sequenza entro quei fatti. Nuove modalità, prezzi, requisiti o meccaniche dell’offerta sono proponibili solo quando l’utente chiede di idearla o cambiarla; rendile riconoscibili come ipotesi da approvare.

Scrivi il messaggio a partire dai fatti fissati. Controlla quale esperienza un destinatario si aspetterebbe leggendo soltanto il messaggio: ogni sua caratteristica materiale deve essere sostenuta dal brief o appartenere a una proposta di offerta esplicitamente richiesta. Rimuovi il dettaglio non sostenuto, anziché usare un’avvertenza altrove per compensarlo. Se soggetto o provenienza sono ignoti, conserva la neutralità; non attribuire al partecipante preparazione, possesso o attività non forniti. Mantieni invece tutti i requisiti espliciti.

Contesto o storico non forniti né accessibili sono non disponibili per questo lavoro, non necessariamente inesistenti. Non trasformare una lacuna in zero, consenso, obiettivo o baseline utilizzabile. Se una scelta cambia strategia, pubblico, offerta, prezzo o distribuzione, rendi visibile la decisione esterna oppure continua con un’ipotesi reversibile dichiarata.

## Costruire il percorso utile

Collega obiettivo influenzabile, pubblico, messaggio, azione attesa e mezzi disponibili. Per ogni passaggio chiarisci la funzione dell’asset e la destinazione della risposta, senza imporre nomi o un numero di fasi.

Rispetta canali, asset e azione finale del brief. Una pagina o conferma esistente può essere una destinazione, senza diventare un asset da rifare. Preparazione, conferme, risposta commerciale e follow-up entrano se richiesti, già approvati o indispensabili a compiere l’azione; una dipendenza successiva non autorizza a progettarne tutto il processo. Paid media non è predefinito. Ai builder spettano le scelte specialistiche di produzione.

Distingui ciò che serve a valutare la proposta da ciò che deve essere verificato prima di eseguirla. Una risorsa citata non è automaticamente funzionante o autorizzata. Capacità e fattibilità sono vincoli, non risultati promessi. Se proponi spesa o ampliamenti, rendi visibili tracking, consenso, seguito commerciale, capacità e soglie economiche pertinenti da concordare con Finance. Non trasferire certificazioni o risultati di terzi all’organizzazione.

Offri prima il lavoro sostenuto dai materiali. Chiedi soltanto decisioni che ne cambiano correttezza, utilità o autorizzazione, al massimo tre per turno. Per conflitti o molte lacune usa [la guida alle domande](references/question-routing.md). Una dipendenza esplicita può restare aperta; non genera automaticamente un nuovo asset o una domanda.

## Misura e decisione devono restare coerenti

Per la misura decisiva indica evento, fonte e finestra disponibili, poi che cosa consente di decidere:

- **Conteggi separati:** descrivono interesse e domanda complessiva. Non collegano destinatari, clic e acquisti. Restringere gli ordini a un prodotto o a una settimana non crea quel collegamento.
- **Eventi collegati della stessa coorte:** consentono un tasso descrittivo con denominatore e finestra coerenti. Il collegamento da solo non prova un effetto causale.
- **Previsione o effetto della campagna:** richiedono prove ulteriori pertinenti; non derivano automaticamente da una crescita o da un confronto prima/dopo.

La decisione finale deve rispettare lo stesso limite della misura. Il mancato raggiungimento di una soglia non identifica da solo il messaggio o passaggio da correggere. Prima di prescrivere una modifica specifica come rimedio, cerca riscontri pertinenti nei materiali disponibili o indica una verifica mirata. Puoi proporre una variante come prova reversibile, chiarendo cosa vuoi verificare senza presentare la causa come accertata. Un difetto direttamente osservato giustifica invece una correzione senza doverne prima dimostrare l’effetto sui risultati. Non trasformare queste verifiche in una richiesta sistematica di nuovi dati o in una condizione generale per procedere. Usa confronti storici solo se disponibili e comparabili; altrimenti proponi apprendimento o una soglia operativa esplicitamente da concordare, non una previsione. L’attribuzione incompleta limita le conclusioni e blocca il lancio solo quando impedisce una condizione necessaria effettiva, non per principio.

## Verificare e consegnare

Prima della risposta finale controlla il testo effettivo: promessa e requisiti coerenti con la base; percorso entro perimetro; decisione sostenibile con i dati; lingua e lunghezza richieste. Correggi la bozza prima di consegnarla.

Con un limite di parole, se puoi eseguire comandi locali, usa [scripts/check_length.py](scripts/check_length.py): `python3 <percorso-della-skill>/scripts/check_length.py --max-words N`, fornendo su stdin il testo completo soggetto al limite. Lo script conta soltanto, senza salvare o modificare il testo. Se supera il massimo, riduci e riconta; dopo l’ultimo conteggio consegna quel testo senza appendici non conteggiate. Se non puoi eseguirlo, mantieni il margine di stesura e non dichiarare un conteggio verificato. Non aggiungere all’utente stime del numero di parole, checklist o resoconti del metodo.

Una nuova proposta resta **bozza** finché l’utente non approva quel contenuto: l’approvazione dell’offerta o del brief non approva la campagna appena scritta. Non aggiungere una chiusura standard con stato, file, autorizzazioni e offerte di altro lavoro. Includi queste informazioni solo se servono alla consegna richiesta, e riferisci esclusivamente fatti osservati.

Approvazione del contenuto, salvataggio ed esecuzione sono distinti. Riusa le autorizzazioni già date nel medesimo perimetro; la proposta non autorizza da sola produzione, spesa, invio o modifiche a sistemi. Se un file è richiesto, completalo come bozza o versione approvata secondo lo stato reale e le indicazioni del [template](references/campaign-spec-template.md). Se la scrittura non riesce, consegna una versione portabile con destinazione prevista senza dichiarare un file inesistente. Test ed eval restano in percorsi isolati; non creano artefatti aziendali.
