---
artifact: design-campaign-question-routing-blueprint
version: 0.1
status: bozza-di-progettazione
last_reviewed: 2026-08-29
implementation_status: roadmap
---

# Routing delle domande di `design-campaign`

Questa guida serve a selezionare il minor numero di domande che renda la campagna coerente, producibile e misurabile. Non è un questionario e non stabilisce un ordine fisso delle sezioni della Campaign Spec.

## Registro privato della campagna

Prima di porre domande, classifica gli elementi rilevanti in dieci aree:

1. esigenza, trigger e risultato aziendale a cui la campagna contribuisce;
2. obiettivo di campagna e cambiamento che può plausibilmente influenzare;
3. pubblico, situazione, ostacolo e azione attesa;
4. offerta, proposta di valore, messaggi, claim e prove;
5. meccanismo e sequenza della campagna;
6. ruolo dei canali e percorso di risposta o conversione;
7. asset, brief specialistici e handoff;
8. tempi, capacità, budget, dipendenze e responsabilità;
9. misurazione, baseline, strumentazione e regole decisionali;
10. rischi, approvazioni e autorità per contenuto ed esecuzione.

Per ogni elemento registra privatamente:

- sostenuto da una fonte o da un artefatto approvato;
- confermato dal responsabile;
- inferito e in attesa di conferma;
- in conflitto;
- sconosciuto o ambiguo;
- esplicitamente non definito, non disponibile, sconosciuto al referente o non applicabile.

Classifica inoltre la conseguenza:

- **bloccante per la Campaign Spec:** impedisce di approvare la logica della campagna;
- **bloccante per l'esecuzione:** permette una spec approvata con dipendenza esplicita, ma impedisce lancio, spesa, invio o pubblicazione;
- **materiale non bloccante:** deve restare visibile e avere un comportamento prudente;
- **rinviabile:** appartiene a un builder, a una piattaforma o a un responsabile successivo.

Non mostrare il registro come una checklist diagnostica. Usalo per formulare la proposta e selezionare le domande.

## Ordine di priorità

Poni al massimo tre domande per turno. Ordina le candidate così:

1. impedire claim falsi o sensibili, uso improprio di dati, azioni non autorizzate o conflitti con contesti approvati;
2. verificare che offerta, disponibilità, prezzo, percorso di risposta e follow-up possano sostenere la domanda generata;
3. chiarire obiettivo di campagna, pubblico, situazione e azione attesa;
4. confermare proposta di valore, messaggio guida e prove utilizzabili;
5. risolvere un vincolo di capacità, tempo, budget o canale che cambia l'architettura;
6. chiarire la misurazione e la decisione che dipenderà dal risultato;
7. classificare una lacuna non bloccante affinché la bozza possa avanzare onestamente;
8. rinviare a builder e strumenti i dettagli che non cambiano la Campaign Spec.

Non chiedere ciò che è già leggibile in una fonte, salvo che esista un conflitto materiale. Uno stato esplicito di non conoscenza è una risposta valida.

## Regole di formulazione

- Parti dalla comprensione provvisoria: «La proposta sembra rivolta a X; confermi o va corretta?».
- Poni una domanda principale per decisione.
- Raggruppa elementi solo quando formano un sistema naturale, come azione attesa, destinazione e follow-up.
- Se la risposta può essere data dal proprietario di un'altra funzione, chiedi lo stato o il proprietario, non costringere il responsabile marketing a inventarla.
- Chiedi la granularità minima che cambia il progetto: un ordine di grandezza o un limite può bastare al posto del budget dettagliato.
- Non chiedere all'utente di selezionare canali prima di avere chiarito la funzione necessaria.
- Non mostrare nomi di campi, codici di stato o serializzazioni nella domanda visibile.
- Offri sempre la possibilità di correggere, dichiarare che l'informazione non è nota o mantenere un'assunzione visibile in una bozza esplorativa.

## Lenti per le domande

Gli esempi seguenti sono una banca di prompt, non una sequenza.

### Obiettivo e cambiamento

- La campagna deve soprattutto generare conoscenza qualificata, comprensione, fiducia, prova o una specifica azione?
- Quale cambiamento può realisticamente influenzare la campagna, distinto dal risultato aziendale più ampio?
- Se il target numerico citato non ha una baseline, preferisci mantenerlo come aspirazione oppure definire prima che cosa osservare?

Non trasformare vendite o ricavi in obiettivi causalmente attribuiti alla campagna senza un modello adeguato.

### Pubblico, situazione e ostacolo

- La proposta sembra destinata a questo pubblico in questa situazione: confermi o la priorità è un'altra?
- Quale ostacolo deve superare la campagna: scarsa conoscenza, incomprensione, sfiducia, inerzia, rischio percepito o difficoltà di accesso?
- Chi usa, decide, paga o può bloccare l'azione e quale ruolo deve svolgere la campagna per ciascuno?

Non inventare personas o fondere ruoli d'acquisto diversi.

### Offerta, valore e prova

- Quale offerta o configurazione è realmente disponibile durante la campagna?
- Quale messaggio può essere sostenuto dalle prove fornite e quale richiede una formulazione più prudente o un'approvazione?
- Il vantaggio centrale deriva da una capacità documentata, da una testimonianza, da un dato o soltanto da un'ipotesi interna?

Non creare sconti, condizioni, garanzie, comparazioni o credenziali.

### Meccanismo e sequenza

- La proposta provvisoria accompagna il pubblico da comprensione a prova e azione: quale passaggio è già coperto e quale manca?
- Serve una campagna concentrata su un'unica occasione oppure una sequenza che costruisca fiducia nel tempo?
- Quale evidenza o comportamento indicherebbe che una fase può passare alla successiva?

Non confondere una sequenza di cambiamento con un calendario editoriale.

### Canali e percorso di risposta

- Quale funzione deve svolgere questo canale: raggiungere, spiegare, dimostrare, convertire, seguire o riattivare?
- Dove arriva concretamente una persona dopo la CTA e chi gestisce il passaggio successivo?
- Esistono limiti di audience, account, consenso, disponibilità o capacità che rendono il canale non utilizzabile?

Non assumere che un canale citato nel brief sia già configurato, autorizzato o adatto.

### Asset e handoff

- Qual è l'asset minimo necessario per svolgere questa funzione nella sequenza?
- Il materiale esistente può essere riusato con una revisione oppure serve un nuovo brief?
- Chi possiede contenuto, prova, approvazione e produzione dell'asset?

Non decidere dettagli specialistici come numero di slide, montaggio o composizione grafica.

### Tempi, capacità e budget

- Quale scadenza è realmente vincolante e quale è una preferenza?
- Quale capacità del team o dipendenza esterna limita il numero di canali e asset gestibili?
- Esiste un limite o ordine di grandezza già autorizzato che esclude alcune architetture?

Non richiedere dati finanziari sensibili o un media plan dettagliato per completare la Campaign Spec.

### Misurazione e decisione

- Quale evento osservabile rappresenta il cambiamento cercato e dove viene registrato?
- Esiste una baseline, un confronto o una finestra temporale utilizzabile?
- Quale decisione prenderete se il segnale è forte, debole, ambiguo o non misurabile?

Se mancano dati sufficienti, formula un obiettivo di apprendimento senza inventare una soglia.

### Autorità e rischio

- Chi può approvare il contenuto della Campaign Spec e chi deve autorizzare separatamente spesa o pubblicazione?
- Quali claim, dati personali, mercati o destinatari attivano una revisione legale, privacy, compliance o brand?
- Questa attività è una bozza interna reversibile o prepara un'azione esterna con conseguenze?

Se il percorso di approvazione non è definito, registralo come tale; non assegnare un approvatore per inferenza.

## Confine con lo Strategy Core

`design-campaign` può risolvere una scelta locale quando:

- riguarda la funzione di un canale o di una fase;
- restringe un messaggio a prove disponibili;
- sceglie l'asset minimo per una funzione già chiara;
- adatta intensità e sequenza a capacità o tempi;
- definisce una modalità prudente per apprendere.

Deve rendere visibile un bivio strategico più ampio quando la scelta cambia:

- quale mercato, segmento o ruolo d'acquisto privilegiare;
- quale offerta o configurazione aziendale portare sul mercato;
- il posizionamento o la proposta di valore di fondo;
- il modello di prezzo, distribuzione o disponibilità;
- l'allocazione sostanziale tra alternative strategiche;
- la diagnosi del problema che la campagna dovrebbe risolvere.

In questi casi può mantenere un'ipotesi per una bozza reversibile oppure proporre il percorso Strategy. Non deve completare silenziosamente una strategia aziendale dentro la Campaign Spec.

## Routing per stato di partenza

### Richiesta minima

Se l'utente fornisce soltanto un'offerta e dice «voglio una campagna», formula ciò che è comprensibile, non inventare pubblico o obiettivo e chiedi prima le decisioni che cambiano tutto: risultato, pubblico/situazione e azione/offerta.

### Brief già maturo

Se il brief copre le decisioni essenziali, non ripetere domande. Mostra direttamente l'architettura provvisoria, i conflitti e le sole autorizzazioni o dipendenze mancanti.

### Percorso collegato

Se esistono Identity, Foundations e Strategy approvati, applicali e non riaprire le decisioni. Chiedi solo ciò che appartiene alla campagna o risolve un conflitto materiale.

### Campagna esistente da ripensare

Se l'utente porta asset o risultati esistenti, separa prima che cosa era previsto, eseguito e osservato. Non attribuire il problema al copy o al canale senza verificare percorso, pubblico, offerta, distribuzione e misurazione.

### Urgenza o contesto incompleto

Se l'utente sceglie una bozza interna, attiva la fast lane con assunzioni dichiarate. Se chiede pubblicazione, spesa o invio, non usare l'urgenza per saltare prove, autorità o dipendenze bloccanti.

## Verifica prima della revisione finale

La Campaign Spec può essere proposta per l'approvazione quando:

- obiettivo di campagna e contributo al risultato aziendale sono distinti;
- pubblico, situazione, ostacolo e azione attesa sono comprensibili;
- offerta, messaggio guida e prove utilizzabili sono confermati o limitati prudentemente;
- la sequenza spiega la funzione dei canali e degli asset;
- il percorso di risposta o conversione è praticabile oppure ha dipendenze esplicite;
- responsabilità, limiti di capacità e autorizzazioni sono visibili;
- la misurazione non promette precisione o causalità non supportate;
- non resta un conflitto bloccante per la logica della campagna;
- i blocchi di esecuzione restano separati dall'approvazione del documento.

Non sono requisiti automatici un budget dettagliato, un media plan, una baseline numerica, un elenco completo di asset o l'esistenza del percorso Strategy Core.
