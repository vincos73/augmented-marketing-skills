# Routing delle domande

Leggi questa guida quando la campagna è nuova o incompleta, le fonti sono in conflitto oppure più lacune competono per l'attenzione del responsabile. L'obiettivo è porre il minor numero di domande che renda la campagna coerente, producibile e misurabile, non condurre un workshop completo.

## Costruire privatamente il registro della campagna

Classifica gli elementi rilevanti in dieci aree:

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

Per ogni elemento registra privatamente se è:

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

Non mostrare il registro come una checklist diagnostica.

## Ordinare le domande per conseguenza

Poni al massimo tre domande per turno. Ordina le candidate così:

1. impedire claim falsi o sensibili, uso improprio di dati, azioni non autorizzate o conflitti con contesti approvati;
2. verificare che offerta, disponibilità, prezzo, percorso di risposta e follow-up possano sostenere la domanda generata;
3. chiarire obiettivo di campagna, pubblico, situazione e azione attesa;
4. confermare proposta di valore, messaggio guida e prove utilizzabili;
5. risolvere un vincolo di capacità, tempo, budget o canale che cambia l'architettura;
6. chiarire misurazione e decisione che dipenderà dal risultato;
7. classificare una lacuna non bloccante;
8. rinviare a builder e strumenti i dettagli che non cambiano la spec.

Non chiedere ciò che è già leggibile, salvo che esista un conflitto materiale. Uno stato esplicito di non conoscenza è una risposta valida.

## Formulare le domande

Prima di renderle visibili, esegui un controllo finale: per ogni domanda identifica privatamente decisione principale e proprietario responsabile. Se non puoi indicarne uno solo per entrambi, separa la domanda. Non spendere due domande nello stesso turno solo per esaurire un flusso end-to-end: il secondo proprietario resta una dipendenza visibile da affrontare dopo.

- Parti dalla comprensione provvisoria: «La proposta sembra rivolta a X; confermi o va corretta?».
- Poni una domanda principale per decisione.
- Raggruppa elementi solo quando formano un sistema naturale, appartengono allo stesso proprietario e richiedono una sola decisione. Se coinvolgono funzioni o autorità diverse, poni una sola domanda e mantieni gli altri elementi come blocchi visibili da affrontare in un turno successivo.
- Se la risposta appartiene a un'altra funzione, chiedi stato o proprietario; non costringere il marketing a inventarla.
- Chiedi la granularità minima che cambia il progetto: un limite o ordine di grandezza può bastare al posto del budget dettagliato.
- Non chiedere di selezionare canali prima di averne chiarito la funzione.
- Offri sempre la possibilità di correggere, dichiarare che l'informazione non è nota o mantenere un'assunzione visibile in una bozza.

## Lenti per le domande

Gli esempi seguenti sono una banca di prompt, non una sequenza.

### Obiettivo e cambiamento

- La campagna deve soprattutto generare conoscenza qualificata, comprensione, fiducia, prova o una specifica azione?
- Quale cambiamento può realisticamente influenzare, distinto dal risultato aziendale più ampio?
- Se il target numerico non ha una baseline, preferisci mantenerlo come aspirazione o definire prima che cosa osservare?

Non attribuire automaticamente vendite o ricavi alla campagna.

### Pubblico, situazione e ostacolo

- La proposta sembra destinata a questo pubblico in questa situazione: confermi o la priorità è un'altra?
- Quale ostacolo deve superare: scarsa conoscenza, incomprensione, sfiducia, inerzia, rischio percepito o difficoltà di accesso?
- Chi usa, decide, paga o può bloccare l'azione e quale ruolo deve svolgere la campagna per ciascuno?

Non inventare personas o fondere ruoli diversi.

### Offerta, valore e prova

- Quale offerta o configurazione è realmente disponibile durante la campagna?
- Quale messaggio è sostenuto dalle prove e quale richiede una formulazione più prudente o un'approvazione?
- Il vantaggio centrale deriva da una capacità documentata, da un dato o soltanto da un'ipotesi interna?

Non creare sconti, garanzie, comparazioni o credenziali.

### Meccanismo e sequenza

- Quale passaggio tra riconoscimento, comprensione, fiducia, prova e azione è già coperto e quale manca?
- Serve una campagna concentrata su un'occasione o una sequenza che costruisca fiducia nel tempo?
- Quale evidenza o comportamento indicherebbe che una fase può passare alla successiva?

Non confondere sequenza e calendario editoriale.

### Canali, risposta e asset

- Quale funzione deve svolgere questo canale: raggiungere, spiegare, dimostrare, convertire, seguire o riattivare?
- Dove arriva concretamente una persona dopo la CTA e chi gestisce il passaggio successivo?
- Qual è l'asset minimo necessario e chi possiede contenuto, prova, approvazione e produzione?

Non assumere che account, audience, consenso o configurazioni siano disponibili.

### Tempi, capacità e budget

- Quale scadenza è vincolante e quale è una preferenza?
- Quale capacità del team o dipendenza esterna limita canali e asset gestibili?
- Esiste un limite o ordine di grandezza già autorizzato che esclude alcune architetture?

Non richiedere dati sensibili o un media plan dettagliato per completare la spec.

### Misurazione e decisione

- Quale evento osservabile rappresenta il cambiamento cercato e dove viene registrato?
- Esiste una baseline, un confronto o una finestra utilizzabile?
- Quale decisione prenderete se il segnale è forte, debole, ambiguo o non misurabile?

Se i dati non bastano, formula un obiettivo di apprendimento senza inventare soglie.

### Autorità e rischio

- Chi può approvare la Campaign Spec e chi deve autorizzare separatamente spesa o pubblicazione?
- Quali claim, dati personali, mercati o destinatari attivano una revisione Legal, privacy, compliance o brand?
- Questa è una bozza interna reversibile o prepara un'azione esterna?

Se il percorso non è definito, registralo; non assegnare un approvatore per inferenza.

## Riconoscere il bivio strategico

`design-campaign` può risolvere una scelta locale quando riguarda funzione di un canale o fase, formulazione sostenibile, asset minimo, intensità, sequenza o apprendimento.

Rendi visibile una decisione più ampia quando cambia:

- mercato, segmento o ruolo d'acquisto prioritario;
- offerta o configurazione da portare sul mercato;
- posizionamento o proposta di valore di fondo;
- prezzo, distribuzione o disponibilità;
- allocazione sostanziale tra alternative strategiche;
- diagnosi del problema che la campagna dovrebbe risolvere.

Mantieni un'ipotesi per una bozza reversibile oppure proponi il percorso Strategy. Non completare silenziosamente la strategia.

## Adattare il percorso allo stato iniziale

- **Richiesta minima:** formula ciò che è comprensibile e chiedi prima risultato, pubblico/situazione e azione/offerta.
- **Brief maturo:** non ripetere domande; mostra architettura, tensioni e sole dipendenze mancanti.
- **Percorso collegato:** applica gli artefatti approvati e chiedi soltanto decisioni di campagna.
- **Campagna da ripensare:** separa previsto, eseguito e osservato prima di attribuire il problema a copy o canale.
- **Urgenza:** usa la fast lane solo per bozze; non saltare prove, autorità o blocchi per azioni esterne.

## Verificare prima della revisione finale

La Campaign Spec è proponibile per l'approvazione quando:

- obiettivo e contributo al risultato aziendale sono distinti;
- pubblico, situazione, ostacolo e azione attesa sono comprensibili;
- offerta, messaggio e prove sono confermati o limitati prudentemente;
- la sequenza spiega funzione di canali e asset;
- il percorso di risposta è praticabile oppure ha blocchi di esecuzione espliciti;
- responsabilità, capacità e autorizzazioni sono visibili;
- la misurazione non promette precisione o causalità non supportate;
- non resta un conflitto bloccante per la logica della campagna.

Non sono requisiti automatici un budget dettagliato, un media plan, una baseline numerica, un elenco completo di asset o il percorso Strategy Core.
