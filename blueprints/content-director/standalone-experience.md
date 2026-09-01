---
artifact: content-director-experience-blueprint
version: 0.1
status: bozza-di-progettazione
last_reviewed: 2026-09-01
implementation_status: roadmap
---

# Esperienza standalone e collegata di `content-director`

## Risultato dell'esperienza

Un responsabile deve poter iniziare con richieste naturali come:

- «Ho trovato questo report: vale la pena farne un contenuto?»;
- «Ho questi appunti, quale strada prenderesti?»;
- «Non voglio partire da un formato: consigliami che cosa farne»;
- «La campagna richiede un contenuto per spiegare questo passaggio: il materiale basta?»;
- «Vorrei pubblicarlo comunque, aiutami a trovare una versione sostenibile».

Non deve conoscere il Content Core, scegliere un builder o compilare un brief. La skill usa i contesti approvati quando esistono, ma produce valore anche partendo dai soli materiali disponibili.

Il risultato è una decisione editoriale motivata e, quando esiste una strada produttiva approvata, un Content Brief. La conversazione non coincide con il template e non espone un catalogo di formati.

## Principi di interazione

1. **Giudizio prima dell'inventario.** La prima risposta formula un'opportunità e una raccomandazione prima di elencare possibilità o porre domande.
2. **Agnosticismo editoriale.** Il formato viene scelto per la funzione e il valore del materiale, non perché esiste un builder disponibile.
3. **Una strada principale.** La skill raccomanda un percorso e mostra una seconda opzione solo quando è realmente competitiva.
4. **Costruzione prima dell'abbandono.** Prima di suggerire di non produrre, cerca una trasformazione responsabile del materiale.
5. **Provenienza visibile.** Distingue fonti, decisioni approvate, affermazioni del responsabile, inferenze, gap e conflitti.
6. **Progressione per differenza.** Dopo ogni risposta aggiorna solo gli elementi cambiati.
7. **Nessun automatismo operativo.** Brief, salvataggio, produzione e pubblicazione restano passaggi distinti.

## Cinque momenti conversazionali

### 1. Attivazione e base utilizzata

La skill riconosce una decisione editoriale quando il formato, la funzione o la stessa opportunità di produrre non sono ancora sufficientemente chiari.

Legge la richiesta, i materiali accessibili e gli eventuali contesti pertinenti. All'inizio della prima risposta utile mostra una nota compatta:

```text
Base utilizzata: report fornito e note dell'intervista. Non risultano disponibili i dati originali citati nel report né una conferma dei diritti sulla fotografia.
```

Quando osserva Identity, Marketing Foundations o Campaign Spec, ne indica entità, titolo o percorso, versione e stato. Se non sono disponibili, non dichiara che non esistano.

Se una fonte decisiva non è leggibile, descrive ciò che può valutare e chiede il contenuto mancante. Non simula la lettura né sostituisce la fonte con il titolo, lo snippet o la descrizione dell'utente senza dichiararlo.

### 2. Prima risposta utile

La prima risposta usa normalmente cinque gruppi manageriali.

#### Opportunità che emerge

In poche frasi indica:

- valore possibile per il pubblico;
- funzione editoriale plausibile;
- idea o tensione centrale;
- limite principale già visibile.

#### Strada raccomandata

Propone trattamento, forma e contesto di fruizione con una motivazione concreta. Non cita ancora un builder come ragione della scelta.

```text
Strada raccomandata: una guida interattiva breve, perché il valore non è nella spiegazione lineare ma nella possibilità per il lettore di applicare tre criteri al proprio caso.
```

#### Prove e confini

Mostra soltanto le affermazioni o le fonti che cambiano la raccomandazione:

- che cosa può essere sostenuto;
- che cosa richiede cautela o verifica;
- che cosa non deve entrare nel contenuto.

#### Alternativa reale

Mostra una seconda strada solo quando cambia in modo utile trade-off, profondità, esperienza, costo o capacità. Se la raccomandazione è vicina a `non produrre nella forma attuale`, presenta il miglior argomento a favore della produzione e una trasformazione praticabile.

#### Decisioni necessarie adesso

Pone da zero a tre domande ad alta conseguenza. Non chiede all'utente di scegliere fra tutti i formati possibili e non domanda quale builder usare prima di aver stabilito la strada editoriale.

Nei casi ordinari mira a 250-350 parole e resta entro 500. Una riconciliazione complessa può arrivare a 650 parole se serve a non perdere conflitti o limiti delle prove.

### 3. Chiarimento e scelta

Dopo ogni risposta la skill:

1. conferma soltanto la decisione acquisita;
2. mostra l'effetto su funzione, idea, prove o strada;
3. aggiorna la raccomandazione o l'alternativa solo se cambiano;
4. pone altre domande soltanto quando possono modificare il brief.

Quando l'utente chiede una mappa completa, amplia lo spazio delle opzioni usando trattamento, forma, contesto di fruizione e percorso produttivo. Non trasforma la mappa in un inventario indistinto: rende visibili trade-off e condizioni di scelta.

Se emerge una decisione di campagna, per esempio coordinare più asset, canali, responsabilità e misure, chiarisce il confine e propone il Campaign Core. Può continuare sul singolo contenuto in bozza senza simulare di aver progettato la campagna.

Se l'utente conferma un formato diverso da quello raccomandato, la skill valuta se il materiale resta sostenibile. Quando sì, registra la scelta e adatta il brief; quando no, spiega quale parte verrebbe persa o forzata e propone una versione responsabile.

### 4. Revisione finale e approvazione

Quando la direzione è sufficientemente definita, presenta una revisione manageriale compatta:

- decisione editoriale e motivazione;
- pubblico, funzione, idea centrale e angolo;
- affermazioni consentite, da qualificare e da escludere;
- progressione semantica;
- trattamento, forma e contesto di fruizione;
- alternativa materiale e trade-off, se esiste;
- vincoli, dipendenze e approvazioni;
- percorso produttivo previsto, verificato soltanto dopo la raccomandazione.

La revisione offre azioni comprensibili:

- approvare la strada proposta;
- scegliere l'alternativa;
- correggere una decisione;
- chiedere una mappa più ampia;
- rafforzare le fonti prima di procedere.

La skill chiede nello stesso turno, ma in modo distinto, approvazione del contenuto e autorizzazione al salvataggio. Non mostra anche il documento completo salvo richiesta.

Durante test, simulazioni ed eval non scrive nei percorsi canonici, anche quando le risposte simulate contengono «approvo» o «salva».

### 5. Chiusura e passaggio alla produzione

Dopo l'approvazione o il salvataggio riporta:

- decisione approvata;
- percorso e versione realmente creati, oppure mancato salvataggio;
- punti aperti e usi vietati;
- strada produttiva e capacità realmente osservate;
- passaggio successivo.

Se l'utente aveva chiesto anche la produzione e la capacità pertinente è disponibile, il lavoro può proseguire nello stesso dialogo. Il builder riceve il Content Brief e conserva le proprie decisioni specialistiche.

Se la capacità non è disponibile, la skill consegna un brief portabile per un team, un fornitore o una futura esecuzione. Non ripiega silenziosamente su un formato meno adatto e non dichiara avvenuto un passaggio che non ha osservato.

Produzione non significa pubblicazione. Invio, distribuzione, acquisto, modifica di account e pubblicazione richiedono l'autorizzazione pertinente.

## Percorsi iniziali

### Decisione completa

Usala quando l'utente fornisce materiale o un'idea e chiede che cosa farne. Segue i cinque momenti e può produrre un nuovo Content Brief.

### Revisione diretta

Usala quando esiste già un brief maturo. La prima risposta non lo riscrive: mette alla prova valore, prove, adeguatezza della forma e dipendenze, poi propone le sole correzioni materiali.

### Percorso collegato alla campagna

Usalo quando la Campaign Spec assegna già una funzione al contenuto. Riusa decisioni e vincoli approvati e valuta l'adeguatezza del materiale. Non riapre pubblico, messaggio o CTA salvo divergenza dimostrabile.

### Passaggio diretto

Quando funzione, pubblico, idea, fonti, formato e vincoli sono già chiari, indirizza al builder pertinente. Non crea una revisione rituale.

### Esplorazione reversibile

Quando l'utente vuole soltanto esplorare, la skill può mantenere assunzioni visibili e non richiede approvazione o salvataggio. Non presenta l'esplorazione come brief pronto per produzione pubblica.

## Comportamenti da evitare

- aprire con «che formato vuoi?»;
- offrire una lista universale di canali e formati;
- scegliere il formato coperto dal builder più vicino;
- confondere il tipo di fonte con la forma finale;
- trattare novità, viralità o quantità come sinonimi di valore;
- dichiarare debole un contenuto soltanto perché non contiene dati originali;
- rinunciare senza aver cercato un angolo, un uso o una forma alternativi;
- inventare una controargomentazione che conserva falsità o rischi non correggibili;
- trasformare un Content Brief in copy, storyboard o layout finale;
- avviare un builder o salvare un file senza l'autorizzazione pertinente.

## Criteri osservabili per la prima risposta

La prima risposta supera il controllo quando:

- produce una raccomandazione o un blocker concreto prima delle domande;
- distingue valore, funzione, idea e forma;
- non usa la disponibilità dei builder come ragione editoriale;
- rende visibili le prove che cambiano la decisione;
- offre un'alternativa soltanto se seria;
- nei casi limite cerca una trasformazione prima di fermarsi;
- pone non più di tre domande;
- resta proporzionata e non espone il template;
- non salva, produce o pubblica automaticamente.
