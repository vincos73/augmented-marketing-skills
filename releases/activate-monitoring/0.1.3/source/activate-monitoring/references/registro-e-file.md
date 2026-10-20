# Cartella dell’utente e continuità in Markdown

Usa gli strumenti file disponibili e autorizzati, senza imporre shell, database o software aggiuntivo. La struttura iniziale è:

```text
<cartella scelta>/<monitoraggio>/
  monitoring-plan.md
  registro.md
  report/
    2026-10-19_09-00-00_C0001.md
```

È un esempio di nomi, non una data da usare nell’esecuzione. Usa nomi validi su Windows e macOS, senza due punti negli orari. Registra cartella effettiva e fuso; non presumere che `Documenti` sia il nome reale della directory. La sincronizzazione della chat non trasferisce questa cartella. Non pubblicare i dati del monitoraggio nel repository della skill.

## Un registro autorevole

`monitoring-plan.md` contiene le decisioni approvate. `registro.md` conserva configurazione effettiva e storia dei controlli. I report sono risultati leggibili di quei controlli, non un secondo archivio da riconciliare manualmente. Un eventuale aiuto aggiuntivo consegna prove all’esecutore; un solo esecutore aggiorna i file finali.

Nel registro conserva solo ciò che consente di riprendere il lavoro:

- riferimento a piano, versione e cartella; strumenti scelti e loro limiti; programmazione osservata, se esiste;
- cicli, intervalli richiesti, controlli effettuati per fonte o ricerca, ultimo successo e lacune;
- menzioni ed eventi con identificatori stabili, riferimenti originali, date distinte, prova minima, sintesi ed esito;
- versioni, riprese e rettifiche, senza cancellare ciò che era noto prima;
- piste importanti ancora aperte, motivo e prossima azione utile;
- report prodotti e consegne preparate, riuscite, fallite o incerte.

Usa sezioni Markdown per ciclo e sottosezioni per novità, aggiornamenti, controlli e consegne. Le tabelle sono facoltative: non comprimere testi complessi in celle fragili. Non duplicare il piano né conservare l’intero payload di ogni chiamata. Mantieni i passaggi o localizzatori minimi che sostengono il risultato e rispetta la conservazione stabilita dal piano.

Identificatori semplici come `C0001`, `M0001`, `E0001` sono sufficienti: continua senza un ultimo numero prefissato e riusa gli ID già presenti. Lo stesso contenuto con una rettifica conserva la menzione e aggiunge una versione; articoli distinti sullo stesso sviluppo possono condividere l’evento. Non deduplicare soltanto per titolo e non modificare parametri URL che distinguono contenuti o mercati.

## Salvataggio e ripresa

Prima di aggiornare leggi il registro esistente. Se un ciclo risulta in corso, verifica se è realmente ancora attivo o interrotto; non avviarne un altro in parallelo. Il solo marcatore Markdown non è un blocco tecnico contro scritture concorrenti: la programmazione deve serializzare le esecuzioni. Se l’ambiente non lo consente, usa controlli su richiesta eseguiti uno alla volta e dichiara il limite prima della ricorrenza.

Registra avvio, ID e versione del piano. Durante il lavoro conserva tempestivamente le prove importanti e le piste; contrassegna come provvisorio ciò che non è ancora concluso. Non avanzare l’ultimo successo di una fonte soltanto perché il ciclo è iniziato.

Prepara il report e l’aggiornamento del registro senza distruggere l’ultima versione utilizzabile. Se gli strumenti consentono copia e sostituzione sicura, conserva `registro.precedente.md` e sostituisci il registro soltanto dopo aver verificato la nuova copia. Non dichiarare atomicità se lo strumento non la garantisce.

Rileggi report e registro salvati. Solo allora registra la chiusura del ciclo e i controlli effettivamente conclusi. Il report deve identificare lo stesso ciclo e la stessa versione del piano; un report orfano o una chiusura incompleta richiedono recupero, non provano continuità. Per una ricerca aperta una finestra cercata non significa copertura esaustiva: conserva query e limiti.

In una ripresa leggi ciclo, file e consegne prima di rifare acquisizioni o invii. Completa lo stesso ciclo quando possibile, riusando ID e risultati osservati; non aggiungere gli stessi eventi come nuovi. Se salvataggio o registro non sono verificabili, conserva l’ultima copia utilizzabile e comunica il limite. Non creare silenziosamente uno storico vuoto. Un database della vecchia preview non è un registro Markdown: non modificarlo o dichiararlo importato; una migrazione richiede un incarico distinto.

Un fallimento di fonte conserva ultimo successo e intervallo da recuperare, senza avanzare il controllo come riuscito. Un nuovo ciclo può riuscire parzialmente. Quando la fonte torna accessibile recupera quanto possibile e lascia visibili le lacune residue. Per indicizzazione tardiva applica la finestra del piano e deduplica le sovrapposizioni.

## Risultati e consegne

Il report completo riporta ciclo, piano/versione, periodo richiesto, controlli effettuati e lacune, novità, rettifiche e pendenti. Ogni risultato rinvia a menzione/evento, originale, date, sintesi e limiti. La rilevanza segue il piano, non il numero di articoli ottenuti. Non forzare sezioni vuote.

Il riepilogo in chat rinvia al report reale. Se un file non è stato creato, consegna il contenuto portabile e dichiara `file non creato`: non inventare un percorso cliccabile o una memoria futura. Un file da scaricare non equivale a un file già salvato nella cartella dell’utente.

Tieni separati «osservato», «incluso nel report» e «consegnato». Per un invio autorizzato registra prima l’intenzione con destinatario/canale e riferimento al contenuto, poi l’esito osservabile. Un esito incerto richiede controllo delle prove o intervento umano prima di ripetere. Non dichiarare ricevuta o lettura sulla sola conferma di invio del servizio.

Un'unica esecuzione salva e rilegge report e registro, poi consegna subito il riepilogo del medesimo ciclo. Collega ID, versione del piano, periodo effettivamente cercato, percorso del report, esito del controllo e stato della consegna. Registra avvio e fine effettivi quando osservabili. Un controllo parziale conserva le sue lacune; un controllo non eseguito non diventa «nessuna novità». Non sostituire il risultato del ciclo con un report precedente né creare una routine separata per inviare quello pronto.

Per consultazioni storiche usa ciò che risultava nei cicli richiesti e mostra separatamente le rettifiche successive. Un cambiamento sostanziale del piano conserva il passato e registra la compatibilità dei nuovi confronti. Spostamenti, sincronizzazione su più computer, eliminazione o divisione del registro richiedono una scelta esplicita; evita due esecutori sulla stessa copia sincronizzata.

Quando completi un report già consegnato, conserva una copia precedente e indica data dell'integrazione, nuove prove e conteggi rettificati. Riusa ciclo, periodo e ID già assegnati; distingui il piano e la skill del controllo originario da quelli dell'integrazione. Aggiorna il registro senza inventare una nuova esecuzione completa o una nuova consegna riuscita.
