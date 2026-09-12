---
name: define-marketing-mix
description: "Traduce una direzione approvata in scelte coerenti su Product, Price, Place e Promotion."
metadata:
  version: "0.1.9"
---

# Definire il marketing mix

Rendi una direzione approvata attuabile attraverso scelte coerenti sulle quattro P, distinguendo decisioni, proposte, ipotesi e autorità. Il risultato è un Marketing Mix approvabile; la sua approvazione non esegue modifiche a prodotto, listini, distribuzione o campagne.

## Base e aggiornamenti

Usa `.agents/marketing/decisions/<decision-slug>/direction.md`, riferito a una sfida confermata, oppure una strategia equivalente già approvata con pubblico, cambiamento, logica di valore, meccanismo, vincoli, assunzioni e responsabile. Non ricreare artefatti sufficienti. Una direzione in bozza consente solo un'esplorazione provvisoria, non un mix canonico approvato.

Leggi direzione, sfida e contesti referenziati, verificando versioni, stato, entità e coerenza. Una modifica materiale a monte richiede il riesame delle scelte dipendenti. Se il mix esiste, aggiorna solo le P cambiate e gli effetti sulle altre. Non forzare questa fase per una campagna già specificata con P approvate e coerenti.

Nelle risposte sostanziali indica entità e versioni realmente lette con una nota compatta. Referenzia fatti identitari e regole stabili senza duplicarli. Usa linguaggio di marketing, mantenendo interni `gate`, `routing`, `artefatto canonico` e `owner`.

## Questioni ereditate dalla direzione

Riconcilia prima date e fatti già disponibili. Riprendi solo i punti aperti che cambiano una P, la coerenza o la fattibilità. Distingui informazione non disponibile, decisione rinviata e scelta esplicita di non fissare un numero: una lacuna non equivale a zero, nessun target o consenso. Conserva per gli altri punti il passaggio in cui serviranno, senza ripetere scelte esplicite salvo nuovo conflitto.

Chiedi obiettivo economico, clienti necessari, costo accettabile o limite di spesa soltanto se cambiano Price, la sostenibilità delle altre P o la preparazione di Promotion per una campagna. Uno scenario economico non è una decisione approvata.

## Mappa delle quattro P

Presenta una prima mappa utile, con scelte e tensioni materiali, prima delle domande. Evita quattro spiegazioni che duplicano la tabella; chiedi solo informazioni capaci di cambiare il mix, massimo tre domande per gruppo. Per P incomplete, conflitti o autorità diverse consulta [i confini delle quattro P](references/four-p-boundaries.md).

Assegna a ciascuna P **esattamente uno** di questi stati:

- **vincolo approvato:** non è una variabile della decisione;
- **scelta da definire:** nel perimetro, ancora da decidere;
- **proposta:** formulata e in attesa di approvazione;
- **ipotesi da verificare:** plausibile, senza sostegno sufficiente;
- **decisione esterna:** compete a un'altra funzione o autorità;
- **non applicabile:** esclusa con motivazione concreta.

Condizioni e dipendenze appartengono alla scelta o a una colonna dedicata, mai a stati ibridi. Un vuoto non concede libertà decisionale. Anche una P invariata deve avere stato e dipendenze visibili, senza imporre quattro sezioni simmetriche.

Mantieni i significati:

- **Product:** configurazione dell'offerta, componenti, packaging, esperienza, servizio e garanzie necessari a sostenere la direzione.
- **Price:** logica di valore e prezzo, architettura e condizioni compatibili con evidenze economiche e autorità disponibili.
- **Place:** accesso, disponibilità, distribuzione, vendita, partner ed erogazione; un canale di comunicazione appartiene a Promotion.
- **Promotion:** ruolo della comunicazione e attivazione della domanda, priorità e territorio di messaggio, prima del campaign plan.

Formula una proposta prioritaria per ogni P che richiede scelta, con trade-off o decisione esterna. Più configurazioni alternative servono solo quando manca una base per scegliere: indica ciò che le discrimina. Usa le quattro P classiche; estensioni come People o Process sono implicazioni solo quando richieste o decisive per il servizio.

## Coerenza, evidenze e autorità

Verifica che promessa, offerta, prezzo, accesso e capacità si sostengano: domanda stimolata senza disponibilità, claim su caratteristiche assenti o canali distributivi inadatti cambiano l'approvabilità del mix.

Product non concede autorità su roadmap, fattibilità o qualità regolamentata; Price richiede responsabile ed evidenze economiche pertinenti; Place non conclude accordi o apre canali; Promotion non autorizza pubblicazione o spesa. Se una scelta eccede l'autorità marketing, identifica la funzione competente e mantieni `decisione esterna`; non mascherarla come assunzione approvata. Non inventare margini, elasticità, conversioni, disponibilità o capacità e chiedi solo i dati sensibili indispensabili.

Collega ogni scelta materiale a base, assunzione e conseguenza. Conserva `[C]` conferme autorizzate, `[S1]` e seguenti fonti, `[I]` inferenze e `[?]` punti irrisolti; confermare un'assunzione non la dimostra. Le verifiche riguardano l'assunzione fragile della P o la coerenza tra P. Se esiste un primo test strategico, spiega come il mix lo abilita senza sostituirlo con un test tattico più comodo.

## Approvazione, salvataggio e completamento

Per redigere o verificare il mix completo usa [il template modulare](references/marketing-mix-template.md). Mostra direzione applicata, mappa, tensioni, assunzioni e verifiche, decisioni esterne, implicazioni operative, responsabile, stato, versione, fonti e destinazione. Una dipendenza bloccante impedisce di dichiarare pronta la campagna.

Prepara il risultato concreto prima di chiedere le sole decisioni mancanti. Un'autorizzazione precedente resta valida per la stessa azione, lo stesso documento e la stessa destinazione; se cambia uno di questi elementi o il perimetro, chiedi soltanto la nuova autorizzazione necessaria. Mantieni distinte approvazione del mix, salvataggio e attivazione; possono essere autorizzati insieme. Rispetta le autorizzazioni già date per il perimetro corrente senza riconferme rituali. Se è approvato solo il contenuto, indica `contenuto approvato in chat; artefatto non creato`.

Con approvazione e autorizzazione alla scrittura salva `.agents/marketing/decisions/<decision-slug>/marketing-mix.md`: prima versione `v1`, incremento intero per modifiche sostanziali, stessa versione per refusi e stato `superato` per un mix sostituito. Non modificare silenziosamente sfida, direzione o istruzioni globali. Prima di scrivere, distingui una prova della skill (`test`, `simulazione`, `eval`) da un test strategico o operativo. In una prova della skill, scrivi soltanto in una destinazione temporanea non canonica esplicitamente richiesta per la prova: approvazioni nel copione e isolamento tecnico del workspace non abilitano destinazioni aziendali, ufficiali o previste dal workflow.

Concludi con scelte, stato effettivo e decisioni esterne ancora necessarie. Completa l'eventuale lavoro successivo già richiesto e autorizzato: Promotion può alimentare una campagna, le altre P richiedono i responsabili competenti. Senza quel mandato, proponi il passaggio pertinente senza avviare campagne, cambiamenti operativi o azioni esterne.
