---
name: define-marketing-mix
description: "Traduce una direzione approvata in scelte su Product, Price, Place e Promotion. Usala prima di campagne o asset, non per fissare unilateralmente prezzi."
metadata:
  version: "0.1.3"
---

# Definire il marketing mix

Trasforma una **Direzione di marketing** approvata in un **Marketing Mix** approvabile e coerente. Rende esplicito che il marketing non coincide con la sola promozione e chiarisce, per ciascuna delle quattro P, che cosa è già deciso, che cosa deve cambiare, che cosa resta un'ipotesi e chi possiede l'autorità.

La skill definisce scelte strategiche di marketing. Non esegue modifiche a prodotto, listini, distribuzione, account, campagne o asset.

## Verificare input e pertinenza

Usa normalmente:

```text
.agents/marketing/decisions/<decision-slug>/direction.md
```

La direzione deve essere approvata e referenziare una sfida confermata. Accetta una strategia equivalente già approvata quando contiene pubblico, cambiamento, posizionamento o logica di valore, meccanismo, vincoli, assunzioni e proprietario. Non obbligare l'utente a ricreare artefatti già sufficienti.

Se la direzione è soltanto una bozza, puoi esplorare il mix in chat ma non approvarlo né salvarlo come canonico. Se il mix esiste già, riepiloga versione, decisioni interessate e rischi di aggiornamento; intervieni solo sulle P cambiate e sulle dipendenze che ne derivano.

Non usare il workflow per una richiesta limitata alla produzione di una campagna già specificata. Non forzarlo quando tutte le P pertinenti sono già approvate e coerenti.

## Rileggere contesti e catena decisionale

Leggi la direzione, il brief della sfida e i contesti canonici referenziati. Verifica versioni, entità, stato e coerenza. Se una modifica a monte può cambiare il mix, segnala il rischio e non trattare la vecchia direzione come ancora valida.

Ogni risposta sostanziale mostra una nota compatta con entità e versioni realmente lette, per esempio:

> Nota operativa: contesto applicato, Identità Acme v2 + Fondamenti di marketing v1 + Sfida Lancio v1 + Direzione v1.

Non duplicare identità, regole stabili o strategia nei nuovi campi. Referenziali e registra solo le decisioni specifiche del mix.
La nota operativa sostituisce una successiva lista dei percorsi letti: non ripetere nomi di file, versioni o limiti tecnici se non servono a decidere, approvare o salvare. Se l'utente ha già vietato scritture o azioni, rispetta il vincolo senza concludere con formule come `nessun file creato` o `nessuna azione eseguita`.

## Classificare prima di decidere

Per ogni P assegna uno stato operativo:

- **vincolo approvato**: non è una variabile di questa decisione;
- **scelta da definire**: appartiene al perimetro e richiede decisione;
- **proposta**: formulata dall'agente e in attesa di approvazione;
- **ipotesi da verificare**: plausibile ma non ancora sostenuta;
- **decisione esterna**: richiede un'altra funzione o autorità;
- **non applicabile**: esclusa con una ragione concreta.

Usa esattamente uno di questi sei stati nella mappa. Eventuali condizioni, dipendenze o motivi di cautela vanno nella colonna della scelta o nelle sezioni dedicate, non in uno stato ibrido come `proposta condizionata` o `decisione da confermare`.

Non interpretare silenziosamente un vuoto come libertà di decisione. Non compilare quattro sezioni simmetriche quando una P non cambia la strategia; rendi comunque visibile il suo stato e le dipendenze.

Quando il mix è nuovo, incompleto o in conflitto leggi [i confini delle quattro P](references/four-p-boundaries.md) prima di formulare le scelte.

## Produrre valore prima delle domande

Il primo turno sostanziale presenta normalmente:

1. come la direzione si traduce nel mix;
2. una prima mappa delle quattro P con stato e scelta proposta;
3. le incoerenze o dipendenze più importanti;
4. non più di tre domande capaci di cambiare il mix.

Se manca un'autorità o una base essenziale, mostra un blocker concreto. Non iniziare con una lezione sulle quattro P, un questionario fisso o una matrice vuota da far compilare all'utente.

Mantieni questo primo turno compatto: una sola mappa delle quattro P, soltanto le tensioni e le dipendenze materiali e le domande indispensabili. Non duplicare la tabella con quattro spiegazioni estese e non anticipare il template canonico completo, le verifiche secondarie o una spiegazione del metodo. Sviluppa il dettaglio solo dopo le risposte dell'utente o quando presenti il gate.

Per ogni P formula una proposta prioritaria con il relativo trade-off o la decisione esterna necessaria. Presenta più architetture alternative soltanto se la scelta non può ancora essere responsabile e indica quale evidenza, vincolo o autorità permetterà di discriminarle.

## Definire Product, Price, Place e Promotion

Mantieni il significato strategico delle quattro P:

- **Product**: configurazione dell'offerta, componenti, packaging, esperienza, servizio, garanzie e adattamenti necessari per sostenere la direzione;
- **Price**: logica di valore e prezzo, architettura, condizioni, soglie, sconti e implicazioni di posizionamento, nei limiti dell'autorità e delle evidenze economiche disponibili;
- **Place**: accesso, disponibilità, distribuzione, percorso di vendita, partner e modalità di erogazione; non confonderla con i canali di comunicazione;
- **Promotion**: ruolo della comunicazione e dell'attivazione della domanda, priorità, territorio di messaggio e criteri generali; non è ancora un campaign plan.

Le quattro P devono sostenersi a vicenda. Verifica incompatibilità come promessa premium con esperienza o prezzo incoerenti, domanda stimolata senza disponibilità, canale distributivo inadatto al pubblico oppure promozione che promette caratteristiche non offerte.

Usa il modello classico delle quattro P. Aggiungi People, Process, Physical Evidence o altre estensioni soltanto se l'utente lo chiede o se una caratteristica del servizio cambia materialmente la decisione; in quel caso trattale come implicazioni esplicite, non come espansione automatica del framework.

## Rispettare i confini di autorità

La P di Product non autorizza l'agente a definire roadmap tecnica, fattibilità, sviluppo o qualità regolamentata. La P di Price non autorizza la fissazione di prezzi senza proprietario, economics e controlli pertinenti. La P di Place non autorizza accordi, aperture di canale o configurazioni. La P di Promotion non autorizza campagne, pubblicazione o spesa.

Quando una scelta supera l'autorità marketing, formula l'implicazione, identifica il proprietario e registra la decisione come esterna. Non mascherare una dipendenza cross-funzionale come assunzione approvata.

Non richiedere dettagli finanziari, personali o commerciali sensibili oltre il minimo necessario. Non inventare margini, elasticità, disponibilità, conversioni o capacità operative.

## Collegare assunzioni e verifiche

Per ogni scelta materiale registra base, assunzione e conseguenza. Mantieni i marcatori `[C]`, `[S1]`, `[S2]`, ... `[I]` e `[?]` usati dagli artefatti a monte.

Collega le verifiche all'assunzione più fragile della singola P o alla coerenza tra P. Non trasformare il mix in un piano completo di sperimentazione. Se la direzione contiene già un primo test strategico, mostra come il mix lo abilita senza sostituirlo con un test tattico più comodo.

## Presentare il gate e salvare

Quando costruisci, aggiorni o revisioni il mix leggi [il template del Marketing Mix](references/marketing-mix-template.md).

Prima del salvataggio mostra:

- sintesi della direzione applicata;
- stato e scelta per ciascuna P;
- coerenza e tensioni tra le P;
- assunzioni, dipendenze, autorità e verifiche;
- implicazioni operative senza dettagliare la campagna;
- stato, versione, proprietario, destinazione, contesti e fonti.

Chiedi in modo inequivocabile sia l'approvazione del mix sia l'autorizzazione al salvataggio. Un consenso precedente alla bozza completa non basta. Durante gli eval non scrivere mai in percorsi canonici.

Dopo l'autorizzazione salva in:

```text
.agents/marketing/decisions/<decision-slug>/marketing-mix.md
```

La prima versione approvata è `v1`. Una modifica sostanziale di una o più P incrementa la versione intera e rende visibili gli effetti sulle altre; un refuso conserva la versione; un mix sostituito diventa `superato`. Non modificare silenziosamente `challenge.md` o `direction.md` e non installare il fascicolo nelle istruzioni globali.

## Concludere e instradare l'attivazione

Riporta che cosa è stato proposto, approvato e salvato e quali decisioni esterne restano necessarie. Il mix non implica che ogni P debba essere attivata attraverso una campagna.

- Per la componente Promotion e le attivazioni coordinate, proponi `to-campaign-spec` quando disponibile.
- Per cambiamenti di prodotto, prezzo o distribuzione, indica proprietari e workflow competenti senza inventarli se non esistono.
- Se una dipendenza bloccante resta aperta, non presentare la campagna come pronta.

Non avviare automaticamente campagne, modifiche operative o azioni esterne.

## Versioning della skill

- Aggiorna `metadata.version` quando cambia il comportamento o il contratto della skill.
- Usa Semantic Versioning: patch per correzioni compatibili, minor per nuove capacità compatibili, major per cambiamenti incompatibili.
- Aggiorna documentazione ed eval interessati; la presenza della sorgente non dimostra approvazione, installazione o release.
