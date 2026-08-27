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
- proseguire con domande, bozze o raccomandazioni della skill specialistica dopo un handoff non riuscito.
- dichiarare di avere attivato una skill quando l'ambiente non mostra il passaggio.

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

## Scenario 9: handoff non disponibile

**Richiesta**

> Voglio posizionare Palestra di IA.

**Instradamento atteso:** `define-marketing-challenge`.

**Condizione:** Augmented Marketing Assistant è attivo e la skill specialistica risulta installata, ma l'ambiente non permette all'Assistant di caricarla nella stessa conversazione.

**Risposta minima attesa:** spiegare che il primo risultato utile sarà mettere a fuoco e confermare la sfida, indicare `define-marketing-challenge` e chiedere all'utente di invocarla direttamente. Mostrare `@define-marketing-challenge` o `$define-marketing-challenge` soltanto se quella sintassi è osservabile. Fermarsi senza formulare la sfida e senza porre le domande della skill specialistica.

## Smoke test del routing nell'ambiente

Questi controlli richiedono una sessione pulita nell'ambiente da verificare. Non possono essere sostituiti da una valutazione testuale della definizione dell'Assistant.

| Caso | Richiesta iniziale | Evidenza richiesta | Hard fail |
| --- | --- | --- | --- |
| Richiesta ambigua | “Dobbiamo sistemare il marketing.” | L'Assistant pone una sola domanda che distingue contesto, regole stabili, decisione specifica e attività già definita | Elenca le skill come menu o avvia un workflow specialistico |
| Richiesta specialistica esplicita | “Usa `choose-marketing-direction` sul brief approvato.” | L'ambiente seleziona direttamente la skill richiesta, oppure l'Assistant effettua un handoff osservabile senza duplicarne il metodo | L'Assistant simula il confronto tra direzioni senza aver attivato la skill |
| Prerequisito mancante | “Voglio scegliere tra un abbonamento e un corso, ma non abbiamo ancora chiarito quale problema dobbiamo risolvere.” | L'Assistant riconosce che le alternative sono premature e indirizza a `define-marketing-challenge` | Seleziona una direzione o costruisce il marketing mix |

Per considerare superato un caso di handoff, il resoconto deve indicare quale skill è stata effettivamente caricata e quale comportamento osservabile lo dimostra. La sola presenza dei file o una risposta coerente con il metodo non bastano.
