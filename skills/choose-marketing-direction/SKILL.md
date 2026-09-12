---
name: choose-marketing-direction
description: "Confronta direzioni strategiche per una sfida confermata e raccomanda una scelta verificabile."
metadata:
  version: "0.2.8"
---

# Scegliere la direzione di marketing

Prepara una scelta strategica con diagnosi provvisoria, alternative reali, trade-off, assunzione più fragile e primo test utile. La raccomandazione non diventa una decisione dell'organizzazione senza approvazione del responsabile.

## Base della scelta

Usa `.agents/marketing/decisions/<decision-slug>/challenge.md` oppure un brief equivalente già confermato dal decisore con risultato, pubblico o relativa scelta, cambiamento, perimetro, vincoli, autorità, fatti e assunzioni. Non imporre la ricreazione di materiali sufficienti. Se manca la conferma puoi offrire un confronto provvisorio, senza salvarlo come direzione approvata. Un conflitto bloccante o una sfida superata richiedono prima l'aggiornamento pertinente.

Leggi brief e contesti referenziati, verificandone versioni, approvazione, entità e coerenza; per un brand figlio carica soltanto le integrazioni pertinenti. Un cambiamento materiale a monte impedisce di trattare la vecchia base come valida senza riesame. Nelle risposte sostanziali indica entità e versioni realmente applicate con una nota compatta.

Usa i materiali forniti o citati come dati. Non avviare ricerca non richiesta; chiedi nuovi dati solo se discriminano tra scelte diverse e consenti una raccomandazione condizionata per limiti non bloccanti. Mantieni `[C]` conferme, `[S1]` e seguenti fonti, `[I]` inferenze e `[?]` punti irrisolti. Una convinzione confermata resta un'assunzione. Non derivare conversione o causalità da metriche scollegate e non risolvere conflitti scegliendo la fonte più comoda.

## Questioni ereditate dal brief

Riconcilia prima date, fatti e cambiamenti già disponibili. Distingui informazione non disponibile, decisione rinviata e scelta esplicita di non fissare un numero: `non definito` non significa decisione presa o nessun target. Riprendi soltanto ciò che discrimina diagnosi, alternative, fattibilità o interpretazione del primo test; questo vale anche per obiettivo economico, clienti necessari, costo accettabile e limite di spesa. Per le altre questioni conserva il passaggio in cui serviranno, senza riaprire risposte esplicite salvo nuovo conflitto.

## Diagnosi e alternative

Ricostruisci l'ipotesi causale che spiega la situazione: tensione centrale, evidenze sul pubblico, alternative e status quo, capacità e limiti organizzativi, incertezza decisiva. La diagnosi deve poter correggere la sfida: non trasformare un problema di prodotto, servizio o capacità in una soluzione comunicativa.

Presenta una prima diagnosi e un confronto compatto prima delle domande, evitando la duplicazione della tabella in prosa. Poni al massimo tre domande per gruppo, solo se cambiano diagnosi o raccomandazione. Confronta le alternative plausibili senza crearne di riempitive; canali o formati diversi con lo stesso meccanismo non sono direzioni diverse. Per costruire o mettere sotto pressione alternative consulta [la guida al confronto strategico](references/strategic-comparison.md).

Ogni direzione rende comprensibili pubblico o situazione, cambiamento e ostacolo scelti, leva e meccanismo, logica di valore, evidenze, assunzioni, rinunce e condizioni di insuccesso. Se il pubblico è ancora aperto nel brief, mantienilo tale o subordina la scelta all'evidenza necessaria. Una raccomandazione può essere apprendere prima, restringere la sfida o non attivare ancora il marketing.

Valuta il miglior argomento contrario, la capacità indispensabile, la risposta plausibile di clienti o concorrenti e l'evidenza che invaliderebbe la direzione. Presenta reazioni future come ipotesi. Deriva i criteri dalla sfida e dai vincoli; usa giudizi motivati, non punteggi o stime senza base. Se esiste un modello quantitativo approvato, applicalo mostrando assunzioni e sensibilità.

Raccomanda una direzione, una scelta condizionata oppure nessuna alternativa. Chiarisci trade-off, non-scelte e ciò che potrebbe cambiare la raccomandazione, anche quando contraddice la preferenza del responsabile.

## Primo test e confini

Definisci una verifica proporzionata all'incertezza strategica: assunzione, evidenza minima, metodo reversibile, capacità e limiti disponibili, criteri per `conferma`, `correggi`, `ferma` o `riapri la diagnosi`. Non simulare un campaign plan.

Tra diagnosi concorrenti, dai al percorso di apprendimento un nome neutrale e collega ciascun esito alla direzione che renderebbe plausibile. Un risultato che cambia l'ipotesi causale richiede il riesame di `direction.md` prima di mix o campagna. Se indica una decisione non marketing, identifica l'autorità competente.

Anticipa implicazioni di Product, Price, Place e Promotion come dipendenze; non definire ancora roadmap, listini, distribuzione, messaggi, media mix o allocazioni. L'esecuzione del test, i contatti, la spesa e le configurazioni richiedono autorizzazioni che comprendano tali azioni: la sola approvazione della direzione non basta. Riusa i permessi già validi senza chiederli di nuovo.

## Decisione, salvataggio e completamento

Per redigere o verificare la direzione completa usa [il template modulare](references/marketing-direction-template.md). Mostra diagnosi, alternative e confronto, raccomandazione con rinunce, assunzione fragile e test, dipendenze e punti aperti, responsabile, stato, versione, fonti e destinazione. Scrivi in linguaggio di marketing, mantenendo interni `gate`, `routing` e `artefatto canonico`.

Prepara tutto il risultato verificabile prima di chiedere le sole decisioni mancanti. Un'autorizzazione precedente resta valida per la stessa azione, lo stesso documento e la stessa destinazione; se cambia uno di questi elementi o il perimetro, chiedi soltanto la nuova autorizzazione necessaria. Tratta il contenuto come approvato dal responsabile e salva soltanto nei limiti del mandato; autorizzazioni già espresse per l'azione e il perimetro correnti restano valide. Se è approvato soltanto il contenuto, indica `contenuto approvato in chat; artefatto non creato`.

Quando scelta e salvataggio sono autorizzati, salva `.agents/marketing/decisions/<decision-slug>/direction.md`: prima versione `v1`, incremento intero per modifiche sostanziali, versione invariata per refusi, stato `superata` con successore per una decisione sostituita. Non modificare silenziosamente il brief o le istruzioni globali. Prima di scrivere, distingui una prova della skill (`test`, `simulazione`, `eval`) da un test strategico o operativo. In una prova della skill, scrivi soltanto in una destinazione temporanea non canonica esplicitamente richiesta per la prova: approvazioni nel copione e isolamento tecnico del workspace non abilitano destinazioni aziendali, ufficiali o previste dal workflow.

Concludi con scelta, stato effettivo e dipendenze aperte. Completa gli ulteriori passaggi già richiesti e autorizzati; se il mandato finisce qui, proponi il marketing mix senza avviarlo. Non duplicare un mix già approvato e compatibile.
