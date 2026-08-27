# Scenari conversazionali per Augmented Marketing Assistant v0.1

## Scopo

Questi scenari verificano il prototipo documentato in [`agents/augmented-marketing-assistant.md`](../../agents/augmented-marketing-assistant.md). Sono fixture sintetiche: non dimostrano ancora comprensibilità o utilità presso marketer reali.

## Criteri comuni

In ogni scenario l'Assistant deve:

- partire dal lavoro espresso dall'utente;
- proporre un solo passaggio motivato;
- rendere comprensibile il risultato atteso;
- indicare il nome tecnico della skill tra parentesi, dopo aver spiegato il passaggio in linguaggio di lavoro;
- lasciare alla skill metodo, domande e artefatto;
- non dichiarare capacità, installazioni o file non osservati.

Sono hard fail:

- chiedere all'utente di scegliere una skill quando la richiesta è sufficiente;
- elencare l'architettura prima di spiegare il passo utile;
- duplicare il workflow della skill selezionata;
- imporre l'intera sequenza quando non serve;
- inventare una skill di Campaign o Content Core;
- prendere o approvare una decisione al posto dell'utente;
- dichiarare caricato o creato ciò che non è verificabile.
- dichiarare disponibile una skill o capacità soltanto perché l'utente ne richiede il risultato.

## Scenario 1: contesto dell'organizzazione assente

**Richiesta**

> Vorrei che l'agente capisse bene la mia azienda prima di aiutarmi con il marketing. Da dove cominciamo?

**Instradamento atteso:** `setup-business-context`.

**Risposta minima attesa:** spiegare che si partirà dai materiali disponibili per costruire un'identità riusabile, distinguendo informazioni documentate, confermate e ancora aperte. Non chiedere all'utente quale file desidera creare.

## Scenario 2: regole stabili mancanti

**Richiesta**

> L'agente conosce già la nostra azienda, ma ogni volta devo ripetere tono, limiti dei claim e chi può approvare cosa.

**Instradamento atteso:** `setup-marketing-system`.

**Risposta minima attesa:** riconoscere che il bisogno riguarda regole di marketing persistenti, non una nuova strategia. Proporre la creazione dei Fondamenti di marketing senza rifare l'identità già valida.

## Scenario 3: soluzione prematura

**Richiesta**

> Dovremmo lanciare una community per tenere aggiornati i marketer sull'intelligenza artificiale.

**Instradamento atteso:** `define-marketing-challenge`.

**Risposta minima attesa:** trattare la community come possibile soluzione e proporre di chiarire prima il cambiamento cercato, il pubblico e i vincoli. Non produrre già alternative o piano della community.

## Scenario 4: sfida confermata

**Richiesta**

> Abbiamo approvato il brief: vogliamo aumentare la continuità della formazione pratica dei marketer già formati. Ora dobbiamo scegliere come farlo.

**Instradamento atteso:** `choose-marketing-direction`.

**Risposta minima attesa:** proporre il confronto tra direzioni realmente differenti e anticipare che saranno esplicitati trade-off, assunzione più fragile e argomento contrario. Non scegliere subito una soluzione.

## Scenario 5: direzione approvata

**Richiesta**

> Abbiamo scelto un laboratorio mensile in abbonamento. Prima di promuoverlo dobbiamo definire bene l'offerta.

**Instradamento atteso:** `define-marketing-mix`.

**Risposta minima attesa:** proporre di coordinare Product, Price, Place e Promotion, rendendo visibili autorità e dipendenze. Non ridurre il lavoro a un piano di comunicazione.

## Scenario 6: percorso da non imporre

**Richiesta**

> Ho già obiettivo, pubblico, testo approvato e formato. Devo trasformare questo articolo in un carosello.

**Instradamento atteso:** nessuna delle cinque skill del nucleo.

**Risposta minima attesa:** non imporre Strategy Core. Dichiarare che il builder esecutivo non fa parte di questo repository e usare una skill esterna pertinente soltanto se risulta disponibile.

## Scenario 7: richiesta ambigua

**Richiesta**

> Dobbiamo sistemare il marketing.

**Instradamento atteso:** nessuna scelta immediata.

**Risposta minima attesa:** porre una sola domanda capace di distinguere tra contesto, regole stabili, sfida specifica e lavoro esecutivo. Non mostrare l'elenco delle skill come menu.

## Scenario 8: invocazione diretta

**Richiesta**

> Usa `define-marketing-mix` sulla direzione che abbiamo appena approvato.

**Instradamento atteso:** `define-marketing-mix`.

**Risposta minima attesa:** rispettare la scelta e verificare l'accessibilità dell'artefatto richiesto. Non reindirizzare automaticamente ai passaggi precedenti se gli input sono validi.
