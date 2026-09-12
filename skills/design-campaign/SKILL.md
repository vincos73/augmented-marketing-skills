---
name: design-campaign
description: "Progetta o aggiorna una campagna coordinata e il suo brief esecutivo: pubblico, messaggi, canali, risposta e misurazione. Non serve per un singolo asset già specificato."
metadata:
  version: "0.1.7"
---

# Progettare una campagna

Trasforma un'esigenza, un brief o decisioni approvate in una **Campaign Spec** utilizzabile dal team: deve chiarire il cambiamento cercato, come la campagna lo sostiene e che cosa serve per eseguirla e valutarla. Completa il lavoro richiesto fino a una proposta decidibile o al documento richiesto; chiedi solo le decisioni che non puoi risolvere dai materiali.

## Base e perimetro

Lavora sia da un brief autonomo sia da contesti Identity, Marketing Foundations o Strategy disponibili. Non imporre il percorso Strategy Core né creare i suoi documenti per completare una campagna standalone. Riusa le decisioni pertinenti e approvate senza riaprirle in assenza di un conflitto materiale. Un marketing mix deve avere una Promotion utilizzabile; un brief esterno autorizzato può fornire una base equivalente.

Riprendi gli aspetti aperti a monte quando cambiano la campagna e riconcilia prima date e fatti disponibili. Distingui informazione non disponibile, decisione rinviata e scelta esplicita di non fissare un numero: una lacuna non equivale a zero, assenza di target o consenso. Se una questione non serve ancora, conserva il momento in cui andrà risolta.

Dichiara in modo compatto i materiali di business realmente usati, versione/stato quando rilevanti e limiti che cambiano il progetto. Distingui fonti, decisioni confermate, inferenze e sconosciuti. Un contesto non fornito o non accessibile non è necessariamente inesistente. Blueprint, eval e documentazione della Suite spiegano il metodo, non provano fatti sulla campagna.

Questa skill progetta la campagna e i brief per il team. Per un singolo asset già definito usa il builder pertinente; per una review indipendente di campagna e asset esistenti usa `campaign-review`, se disponibile. Produzione, analisi e azioni operative eventualmente richieste mantengono i propri strumenti e requisiti.

## Decisioni che rendono utile la spec

Rendi leggibili, con profondità proporzionata al caso:

- obiettivo influenzabile dalla campagna, pubblico, situazione, ostacolo e azione attesa;
- offerta, proposta di valore, messaggio guida e prove utilizzabili;
- sequenza, funzione dei canali e asset necessari, con messaggio, CTA, fonte, responsabile e stato;
- percorso dopo la risposta: destinazione, consenso, tracking, assegnazione e follow-up;
- vincoli di tempo, capacità e budget, responsabilità e dipendenze;
- misurazione e regole per continuare, correggere, fermare o apprendere.

Deriva canali e asset dalle funzioni necessarie. Paid media non è predefinito. Usa le fasi del funnel che descrivono il comportamento reale senza imporre nomi o numero di fasi. I brief per i builder definiscono funzione e vincoli; le scelte specialistiche del formato spettano al relativo lavoro di produzione.

Distingui risultato aziendale, obiettivo di campagna, output, comportamento intermedio e risultato osservato. Non inventare target, audience, ROI o causalità. Quando lo storico cambia una decisione, mostra valori essenziali, definizioni e limiti di comparabilità. Se volumi, baseline o tracking non sostengono una previsione, formula un obiettivo di apprendimento e la decisione conseguente. Per la metrica decisiva chiarisci evento, fonte, finestra e regola decisionale, lasciando esplicito ciò che manca.

## Claim e fattibilità

Ogni claim materiale deve avere prova, provenienza, limiti d'uso e stato dell'approvazione. Restringi o blocca quelli non sostenuti; non trasferire all'organizzazione certificazioni o risultati dei fornitori.

Verifica la disponibilità dell'offerta e la praticabilità del percorso di risposta. La citazione di una landing, un account, una lista, un'audience o un budget non ne prova disponibilità, funzionamento o autorizzazione. Capacità commerciale e operativa sono vincoli, non risultati da promettere. Se proponi paid o ampliamenti, rendi visibili tracking, consenso, follow-up, capacità e soglie economiche da concordare con Finance quando incidono sulla decisione; un costo per contatto da solo non dimostra convenienza. Chiedi risultato economico, clienti necessari, costo accettabile o budget solo per confrontare paid e alternative, dimensionare la campagna o definirne la regola decisionale. Una scelta esplicita di non fissare un numero o non usare nuova spesa va applicata; una decisione soltanto rinviata va chiesta quando diventa necessaria, entro il limite di tre domande.

Non presentare prezzi, sconti, garanzie, spesa, scadenze o responsabilità proposti come decisioni aziendali approvate. Se una scelta cambia mercato, segmento, offerta, posizionamento, prezzo, distribuzione o diagnosi, esplicita il bivio strategico. Puoi continuare una bozza reversibile con l'ipotesi dichiarata, ma non confermare quella scelta al posto del responsabile.

## Dialogo e completamento

Offri prima la campagna che i materiali permettono di delineare: pubblico, cambiamento, percorso e limite decisivo. Usa linguaggio da marketer, senza registri interni o gergo di authoring. Adatta lunghezza e forma alla richiesta; evita di duplicare il percorso in più rappresentazioni.

Se servono chiarimenti, poni al massimo tre domande ad alta conseguenza per turno, ciascuna con una decisione principale e un responsabile. Non accorpare, per esempio, proprietà del tracking e follow-up Sales. Per fonti conflittuali o molte lacune leggi [la guida alle domande](references/question-routing.md). Aggiorna poi soltanto ciò che cambia, senza ripetere la spec a ogni risposta.

La spec è decidibile quando le scelte essenziali sono comprensibili, i claim sono sostenuti o limitati, il percorso e la misura sono definiti e non resta un conflitto che invalida la logica. L'assenza di Identity o Foundations non blocca da sola il lavoro. Una dipendenza di esecuzione può restare aperta in una spec approvata, se esplicita.

Per presentare o salvare la spec completa, usa [il template modulare](references/campaign-spec-template.md). Mostra le decisioni e i punti aperti necessari a una revisione, senza duplicare sintesi e documento integrale. Se l'utente ha chiesto un file, completa il documento nel perimetro autorizzato, mantenendo lo stato di bozza finché il contenuto non è approvato.

## Autorizzazioni e risultato

Approvazione del contenuto, salvataggio e azioni operative hanno significati diversi; possono essere già autorizzati nella richiesta o nella conversazione. Riusa le autorizzazioni pertinenti allo stesso oggetto, destinazione e perimetro; se questi cambiano, verifica che la nuova richiesta autorizzi il cambiamento o chiedi ciò che manca dopo aver preparato un risultato concreto. Una modifica sostanziale richiede una nuova approvazione del contenuto cambiato, non una ripetizione delle autorizzazioni ancora valide.

La spec approvata non prova la prontezza al lancio e non autorizza da sola produzione, spesa, invio, pubblicazione, contatti o modifiche a sistemi. Per eseguirli occorrono l'autorizzazione pertinente e strumenti effettivamente disponibili. Non presentare una proposta o una simulazione come esecuzione.

Il percorso abituale è `.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/campaign-spec.md`; rispetta una destinazione esplicita dell'utente. Il riferimento contiene schema, stati e versioning. Test ed eval restano in percorsi isolati: approvazioni simulate non autorizzano documenti canonici.

Concludi con decisioni chiuse, dipendenze residue, prossimo passaggio e file/versione effettivamente creati. Se il contenuto è approvato solo in chat, indica `contenuto approvato in chat; artefatto non creato`. Se una scrittura autorizzata non è possibile, consegna una versione portabile completa con il percorso previsto, senza dichiarare un salvataggio inesistente.
