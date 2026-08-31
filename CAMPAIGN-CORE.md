---
artifact: campaign-core-blueprint
version: 1.1
status: bozza-di-progettazione
last_reviewed: 2026-08-29
scope: "Campaign Core del Marketing Agent System"
implementation_status: authoring-candidate
---

# Campaign Core

## Tesi

Il Campaign Core trasforma un'esigenza di campagna o una decisione di marketing già approvata in un sistema di attivazione coordinato, revisionabile e misurabile.

Non è un generatore di campagne, un media buyer, un calendario editoriale universale o uno strumento di automazione. Il suo valore è rendere esplicito il brief operativo della campagna prima che team e builder producano o pubblichino asset:

- quale cambiamento deve provocare la campagna e presso quale pubblico;
- quale sequenza di messaggi, prove, canali e azioni sostiene quel cambiamento;
- quali asset servono, con quale responsabilità e dipendenza;
- che cosa deve essere approvato prima di spendere, inviare o pubblicare;
- quale risultato è atteso, come sarà osservato e quale decisione dipenderà dai dati.

La promessa minima è:

> Da un'esigenza di campagna a un sistema che un team può eseguire, controllare e migliorare.

## Decisioni di progettazione confermate

- La prima skill si chiama `design-campaign`.
- La skill è utilizzabile come punto di partenza autonomo, non solo a valle dello Strategy Core.
- Gli artefatti precedenti migliorano continuità e tracciabilità, ma non sono prerequisiti universali.
- Il percorso standalone e quello collegato producono lo stesso tipo di Campaign Spec; la provenienza e il livello di certezza restano visibili.

## Blueprint di authoring

La progettazione dettagliata della prima skill è separata in tre riferimenti:

- [esperienza standalone](blueprints/design-campaign/standalone-experience.md): attivazione, prima risposta, chiarimento, gate e handoff;
- [routing delle domande](blueprints/design-campaign/question-routing.md): registro privato, priorità, fast lane e confine con lo Strategy Core;
- [template della Campaign Spec](blueprints/design-campaign/campaign-spec-template.md): struttura canonica, approvazione, percorso e versioning.

Questi documenti sono blueprint, non sorgente installabile della skill.

La sorgente candidata [`design-campaign` v0.1.4](skills/design-campaign/) traduce il blueprint in una skill installabile con due riferimenti caricati progressivamente. La v0.1.3 è stata provata sulla guida Da Chat a Work con Luna high e Sol high. Sol ha evitato le domande superflue osservate con Luna; entrambi i test hanno però mostrato che termini interni come `contratto`, `architettura` e `gate` possono filtrare nell'interfaccia. La v0.1.4 introduce il lessico di marketing e management, è installata localmente con parità verificata rispetto alla sorgente e resta da retestare prima di una distribuzione pubblica.

## Fixture ed eval iniziali

La [fixture standalone Fabriloom](evals/design-campaign/fixtures/fabriloom-standalone/README.md) simula una campagna B2B con claim conflittuali, capacità limitata, percorso CRM incompleto, budget paid non autorizzato e dati storici non perfettamente comparabili.

Il [catalogo degli eval](evals/design-campaign/eval-catalog.md) definisce 29 controlli generali e 8 controlli specifici della fixture. La baseline è qualitativa e non equivale a un forward test indipendente.

## Esigenze, skill e risultati

| Esigenza iniziale | Skill del core | Risultato ottenibile | Stato |
|---|---|---|---|
| «Voglio progettare una campagna» oppure «Abbiamo già una direzione: come la attiviamo?» | `design-campaign` | Campaign Spec approvabile, pronta per assegnazione e produzione | prima candidata |
| «La campagna e gli asset sono davvero pronti?» | `campaign-review` | Review con esito, problemi bloccanti, correzioni e autorizzazioni mancanti | seconda candidata |
| «Come è andata davvero e che cosa facciamo adesso?» | `campaign-debrief` | Lettura dei risultati con limiti, decisione consigliata e prossima verifica | terza candidata, blueprint v0.1 |

Le tre skill condividono il fascicolo della campagna, ma possiedono decisioni e artefatti distinti. Non sono tre schermate obbligatorie e non devono essere eseguite quando il loro lavoro è già stato svolto e documentato in modo affidabile.

## Flusso essenziale

```text
esigenza di campagna, brief esistente o marketing-mix.md approvato
        ↓
design-campaign
        ↓
campaign-spec.md approvata
        ↓
builder e responsabili producono gli asset
        ↓
campaign-review, solo quando il rischio o il coordinamento lo richiedono
        ↓
esecuzione esterna autorizzata
        ↓
dati e osservazioni sufficienti
        ↓
campaign-debrief
        ↓
decisione: continuare, correggere, scalare, fermare o riaprire la strategia
```

Il core non possiede l'esecuzione esterna. Pubblicazione, invio, acquisto media, modifica di account, allocazione di budget e configurazione degli strumenti restano azioni separate, con autorizzazione esplicita e capability osservata.

## Contratto di ingresso

### Principio di accesso

`design-campaign` è un punto di partenza autonomo. Non richiede che l'utente abbia già usato Business Identity, Marketing Foundations o Strategy Core e non lo obbliga a ricostruire quel percorso prima di ricevere valore.

La skill accetta due modalità di ingresso:

- **standalone:** l'utente parte da un obiettivo, un'esigenza, un brief, materiali disponibili o una campagna da ripensare;
- **collegata:** l'utente dispone già di contesti e decisioni approvati nel Marketing Agent System.

Entrambe portano alla stessa Campaign Spec. Cambiano la base conoscitiva, il livello di certezza e le verifiche necessarie, non la qualità minima dell'artefatto.

### Percorso standalone

La skill ricava prima tutto ciò che può dalla richiesta e dai materiali forniti, poi presenta una prima architettura utile e pone non più di tre domande capaci di cambiare la campagna. Non apre chiedendo all'utente di creare profili, scegliere core o conoscere il framework.

Per procedere servono progressivamente, non necessariamente nel primo messaggio:

- entità, offerta, pubblico e situazione;
- cambiamento cercato e ruolo plausibile della campagna;
- proposta di valore, prove disponibili e limiti dei claim;
- percorso di risposta o conversione e relative dipendenze;
- vincoli di tempo, capacità, budget o canale che cambiano il progetto;
- responsabile della decisione e approvazioni necessarie.

Quando Business Identity o Marketing Foundations non esistono, la skill non li inventa e non interrompe automaticamente il lavoro. Registra il contesto fornito dall'utente, distingue fatti, decisioni, inferenze e assunzioni e mantiene la Campaign Spec in bozza finché le incognite materiali non vengono confermate.

Se manca una decisione strategica che cambia radicalmente pubblico, offerta, posizionamento o meccanismo, `design-campaign` rende visibile il bivio. Può:

1. continuare con un'assunzione esplicita per esplorare una bozza reversibile;
2. confrontare solo le alternative strettamente necessarie a sbloccare la campagna;
3. proporre il passaggio allo Strategy Core quando serve una decisione più ampia e persistente.

Non simula che la strategia sia stata approvata. La scelta di continuare in bozza non autorizza produzione, spesa o pubblicazione.

### Percorso collegato

Quando sono disponibili, `design-campaign` parte dalla versione approvata di:

1. Business Identity pertinente;
2. Marketing Foundations e relativo overlay di brand, se presente;
3. Brief della sfida;
4. Direzione di marketing;
5. Marketing Mix, con una componente Promotion utilizzabile.

La skill carica solo i riferimenti pertinenti, mostra un FYI compatto con percorsi e versioni realmente osservati e non duplica i documenti a monte nella Campaign Spec. Non ripete domande già risolte dagli artefatti e apre direttamente sulle decisioni di campagna ancora necessarie.

Un brief esterno autorizzato può svolgere lo stesso ruolo del percorso collegato quando rende leggibili base strategica, provenienza, responsabile e stato di approvazione. Non deve essere convertito preventivamente nei formati interni del Marketing Agent System.

### Condizioni che bloccano la prontezza

La campagna non può essere dichiarata pronta quando, per esempio:

- nessuno ha l'autorità di confermare le decisioni materiali della campagna;
- Promotion promette qualcosa che Product, Price o Place non possono sostenere;
- pubblico, comportamento cercato o offerta sono materialmente ambigui;
- un claim decisivo non possiede una prova adeguata o l'approvatore richiesto;
- la conversione dipende da disponibilità, tracking, Sales, Operations o partner non confermati;
- budget, capacità o tempi non consentono di scegliere responsabilmente il sistema di attivazione.

Un vincolo aperto non blocca automaticamente la bozza. Deve essere classificato per impatto, proprietario e comportamento prudente.

## 1. `design-campaign`

### User story

> Come responsabile marketing, parto da un'esigenza di campagna oppure da una decisione già approvata e progetto un sistema coordinato di messaggi, prove, canali, asset, responsabilità e misure. Ottengo una Campaign Spec approvabile che il team può eseguire senza dover conoscere il framework o inventare autorizzazioni.

### Decisione posseduta

La skill decide come progettare un'architettura di campagna coerente a partire dalla migliore base disponibile. Nel percorso collegato traduce la Promotion senza riaprire silenziosamente la strategia. Nel percorso standalone chiarisce le sole scelte necessarie alla campagna e rende provvisorie quelle prive di base o autorità. Non definisce una strategia aziendale completa, non produce gli asset finali e non esegue la campagna.

Deve rendere espliciti almeno:

1. obiettivo della campagna e cambiamento osservabile cercato;
2. pubblico, situazione, ostacolo e azione attesa;
3. proposta di valore, messaggio guida, messaggi di supporto e prove consentite;
4. sequenza della campagna e funzione di ogni fase;
5. ruolo dei canali paid, owned, earned, partner, Sales o advocacy realmente pertinenti;
6. matrice degli asset, con scopo, pubblico, canale, fase, CTA, fonte, proprietario e stato;
7. percorso dopo la risposta: destinazione, conversione, follow-up e dipendenze operative;
8. responsabilità, approvazioni, budget o capacità disponibili e calendario decisionale;
9. piano di misurazione con baseline, eventi, fonti dati, finestre e limiti;
10. previsioni o assunzioni principali, con regole per continuare, correggere o fermare.

### Distinzioni obbligatorie

- **Obiettivo aziendale:** risultato più ampio a cui la campagna contribuisce.
- **Obiettivo di campagna:** cambiamento che la campagna può plausibilmente influenzare.
- **Output:** asset, invii, impression o attività prodotte.
- **Outcome intermedio:** attenzione qualificata, comprensione, fiducia, prova o azione.
- **Risultato osservato:** dato effettivamente disponibile, con fonte e limiti.

La precisione fittizia è un errore. Target numerici, attribuzione, ROI, conversioni attese e dimensioni del pubblico entrano solo se esiste una base documentata o una decisione autorizzata. In assenza di baseline, la skill può definire che cosa imparare e come misurarlo senza inventare soglie.

### Esperienza conversazionale

Il primo turno sostanziale deve produrre valore prima delle domande:

- sintesi del ruolo della campagna;
- architettura provvisoria in poche fasi;
- decisioni già sostenute e assunzioni che cambiano il piano;
- non più di tre domande ad alta conseguenza.

Non apre con un questionario, un catalogo di canali o una lista completa di asset. Sviluppa il dettaglio dopo le risposte o quando presenta il gate di approvazione.

Quando più architetture sono plausibili, confronta solo alternative che cambiano realmente meccanismo, sequenza, pubblico, intensità o uso dei canali. Non tratta automaticamente LinkedIn, email e webinar come strategie concorrenti: possono svolgere ruoli diversi nello stesso sistema.

### Confini di autorità

La skill può proporre:

- ruoli di canale e sequenze;
- un messaggio guida e una gerarchia di messaggi;
- asset necessari e relativi brief;
- scenari di budget o capacità, se supportati;
- metriche, strumentazione e regole decisionali.

Non può:

- approvare claim, budget o calendario per conto dei responsabili;
- fissare unilateralmente spesa, offerta, prezzo, sconto o condizioni commerciali;
- dichiarare disponibile tracking, audience, account, inventario o capacità non verificati;
- prenotare media, inviare comunicazioni, pubblicare, modificare CRM o configurare piattaforme;
- trasformare un'ipotesi di attribuzione in causalità dimostrata.

## Campaign Spec

### Percorso proposto

```text
.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/
├── campaign-spec.md
├── campaign-review.md   # creato solo quando serve una review formale
└── learning-record.md   # creato solo quando esistono risultati interpretabili
```

Asset, dashboard, media plan e documenti specialistici restano nei loro sistemi o percorsi originali e vengono referenziati. Non sono copiati nel fascicolo per simulare completezza.

### Struttura minima

La Campaign Spec contiene:

1. metadati, stato, owner e versioni degli artefatti a monte;
2. contratto della campagna: obiettivo, pubblico, cambiamento, offerta e perimetro;
3. architettura della campagna e sequenza delle fasi;
4. sistema di messaggi, prove e claim;
5. ruoli dei canali e logica di coordinamento;
6. matrice degli asset e handoff ai builder;
7. percorso di risposta, conversione e follow-up;
8. responsabilità, dipendenze, capacità, budget e calendario;
9. piano di misurazione e apprendimento;
10. rischi, assunzioni, approvazioni e condizioni di arresto;
11. registro modifiche.

Gli stati dell'artefatto sono `bozza`, `approvata` e `superata`. Lo stato non implica che la campagna sia stata lanciata, sia attiva o sia conclusa: questi sono fatti operativi esterni da riportare separatamente con fonte e data.

Una modifica che cambia obiettivo, pubblico, offerta, messaggio guida, meccanismo, sequenza o regola decisionale incrementa la versione intera e richiede una nuova approvazione. Correzioni non sostanziali conservano la versione.

### Gate di approvazione

La Campaign Spec può diventare `approvata` quando:

- la base strategica è approvata oppure le scelte necessarie alla singola campagna sono state confermate esplicitamente dal responsabile;
- messaggi e prove rispettano Identity, Foundations e limiti dei claim;
- Product, Price e Place possono sostenere la risposta generata;
- canali e asset hanno una funzione riconoscibile, non sono una lista di desideri;
- dipendenze bloccanti, proprietari e autorizzazioni sono visibili;
- piano di misurazione e regole decisionali sono proporzionati ai dati disponibili;
- il responsabile approva il contenuto e autorizza separatamente il salvataggio.

Nel percorso standalone, prima dell'approvazione il responsabile deve confermare almeno:

1. obiettivo della campagna e cambiamento cercato;
2. pubblico, situazione e azione attesa;
3. offerta, proposta di valore e limiti delle prove utilizzabili;
4. percorso di risposta o conversione e dipendenze essenziali;
5. vincoli, responsabilità e autorizzazioni necessarie;
6. modo in cui il risultato verrà osservato e decisioni che potranno seguirne.

L'assenza di Business Identity o Marketing Foundations non impedisce da sola l'approvazione. Diventa bloccante quando rende impossibile verificare un elemento materiale, per esempio identità dell'offerta, claim sensibili, vincoli legali, approvatore, disponibilità o coerenza con regole aziendali che l'utente dichiara esistenti ma non può fornire.

L'approvazione della Campaign Spec non autorizza spesa, pubblicazione, invio o modifica di sistemi esterni.

## 2. `campaign-review`

### User story

> Come responsabile della campagna, prima di un'azione irreversibile verifico che strategia, messaggi, prove, percorso, asset e operatività siano coerenti. Ottengo un esito utilizzabile: pronta, pronta con condizioni, da correggere oppure bloccata.

### Tre lenti indipendenti

1. **Coerenza strategica:** la campagna esegue davvero la Campaign Spec e gli artefatti approvati a monte.
2. **Integrità delle affermazioni:** claim, citazioni, numeri, comparazioni, disclaimer e prove sono tracciabili e autorizzati.
3. **Prontezza di sistema:** asset, CTA, destinazioni, tracking, follow-up, responsabilità, dipendenze e approvazioni permettono l'esecuzione prevista.

La review valuta la qualità dei singoli asset solo per gli aspetti che possono compromettere la campagna nel suo insieme: incoerenza fra messaggi, prova assente, CTA interrotta, audience sbagliata, requisiti non rispettati o differenze materiali rispetto alla spec. Leggibilità, composizione, formattazione e QA specialistico restano responsabilità dei builder.

### Esito

Ogni rilievo include evidenza, impatto, severità, proprietario e correzione o decisione richiesta. L'esito complessivo è uno tra:

- `pronta`;
- `pronta con condizioni`;
- `da correggere`;
- `bloccata`.

La review non corregge automaticamente asset, spec o sistemi. Le correzioni vengono applicate dal proprietario o dalla skill competente e poi verificate sul nuovo stato osservabile.

Per una bozza interna a basso rischio può bastare una review leggera. Claim sensibili, spesa rilevante, pubblicazione, dati personali, settori regolamentati o molti handoff richiedono il percorso completo. La governance deve essere proporzionata al rischio e non diventare un passaggio rituale.

## 3. `campaign-debrief`

### User story

> Come responsabile marketing, confronto ciò che la campagna prevedeva con ciò che è stato realmente osservato, distinguo risultato, spiegazioni possibili e limiti dei dati e decido che cosa continuare, correggere, scalare, fermare o rimettere in discussione.

### Contratto

La skill parte dalla Campaign Spec approvata, dall'eventuale review, dai dati disponibili e dalle note operative. La progettazione operativa è nel [blueprint di `campaign-debrief`](blueprints/campaign-debrief/campaign-debrief-blueprint.md), con catalogo degli eval in [evals/campaign-debrief](evals/campaign-debrief/).

- definizioni delle metriche e finestre temporali;
- copertura e qualità della strumentazione;
- modifiche intervenute durante l'esecuzione;
- differenze tra pubblici, canali, asset e fasi;
- confondenti e limiti dell'attribuzione;
- disponibilità di una baseline o di un confronto pertinente.

Se i dati non consentono una conclusione, produce un Learning Record utile che dichiara l'incertezza e propone la prossima osservazione. Non forza un verdetto.

Il risultato separa:

1. che cosa era previsto;
2. che cosa è stato eseguito realmente;
3. che cosa è stato osservato;
4. che cosa i dati sostengono;
5. spiegazioni alternative e limiti;
6. decisione raccomandata;
7. aggiornamenti proposti a campagna, direzione o Marketing Foundations.

Nessuna regola stabile, identità o decisione approvata viene aggiornata automaticamente. Le modifiche proposte seguono il workflow e l'autorità dell'artefatto di destinazione.

## Confine con Content Core, builder e strumenti

| Componente | Decisione posseduta |
|---|---|
| Campaign Core | Come messaggi, canali, asset, responsabilità e misure lavorano insieme per una campagna |
| Content Director | Se un materiale merita un contenuto e quale formato lo valorizza |
| Builder specializzato | Come produrre e verificare il singolo asset nel proprio formato |
| Team o piattaforma operativa | Come configurare, pubblicare, inviare, comprare media e gestire l'esecuzione |
| Analytics o fonti dati | Quali eventi e risultati sono stati osservati |

La Campaign Spec può generare brief per i builder, ma non prescrive decisioni specialistiche come numero di slide, montaggio, gerarchia grafica, impaginazione o resa finale. Un asset già definito può andare direttamente al builder senza passare dal Campaign Core quando non appartiene a una campagna coordinata.

## Primo vertical slice da costruire

Non conviene implementare contemporaneamente le tre skill. La prima candidata è `design-campaign`, perché crea il contratto che review e apprendimento dovranno verificare.

Il primo vertical slice deve partire da una richiesta standalone realistica, perché l'autonomia della skill è parte della proposta di valore:

```text
richiesta e materiali di un responsabile marketing
  → prima risposta utile di design-campaign
  → revisione del responsabile
  → campaign-spec.md approvata in ambiente isolato
  → brief per un builder reale
  → asset prodotto dal builder
  → campaign-review pre-lancio
```

Una regressione separata usa invece un marketing mix sintetico già approvato e verifica che `design-campaign` riusi la catena di contesto senza ripetere domande, perdere vincoli o riaprire decisioni strategiche.

`campaign-debrief` entra solo dopo una campagna reale o una fixture con dati longitudinali abbastanza credibili da testare qualità del dato, fattori alternativi e regole decisionali.

### Criteri osservabili

Il vertical slice deve mostrare che:

- un utente nuovo può iniziare dicendo che vuole progettare una campagna, senza conoscere skill o artefatti precedenti;
- l'assenza del percorso Strategy non viene scambiata per autorizzazione a inventare pubblico, offerta, prove o budget;
- la prima risposta offre una direzione di lavoro concreta prima di porre non più di tre domande decisive;
- il secondo agente non deve reinterpretare pubblico, obiettivo, messaggio o ruolo dei canali;
- ogni asset richiesto ha una funzione e un proprietario;
- almeno un claim non supportato viene bloccato o ristretto;
- almeno una dipendenza operativa capace di interrompere la conversione viene resa visibile;
- il builder riceve un brief sufficiente senza perdere la propria autonomia specialistica;
- la review individua divergenze materiali senza rifare il QA del builder;
- nessuna azione esterna viene eseguita senza un'autorizzazione distinta;
- il responsabile impiega meno tempo e compie meno correzioni rispetto al proprio workflow abituale e a un buon agente generalista.

### Hard fail iniziali

Sono hard fail almeno:

- strategia o marketing mix riaperti e modificati silenziosamente;
- campagna dichiarata pronta con una dipendenza bloccante irrisolta;
- claim, target, budget, conversioni o ROI inventati;
- elenco di canali e asset privo di ruolo nella sequenza;
- confusione tra output prodotto e outcome osservato;
- attribuzione causale non sostenuta dai dati;
- duplicazione del QA specialistico del builder;
- salvataggio, pubblicazione, invio, spesa o configurazione senza l'approvazione richiesta;
- aggiornamento automatico di Marketing Foundations o altri artefatti approvati.

## Decisioni da validare prima dell'approvazione della skill

1. **Granularità del fascicolo:** confermare un solo documento iniziale e creare review/learning solo quando esistono, evitando una document factory.
2. **Budget:** verificare negli eval se ordine di grandezza, capacità e scenari bastano senza spingere la skill verso un media plan.
3. **Piano di misurazione:** verificare il minimo valido quando baseline, tracking o volumi non consentono target quantitativi responsabili.
4. **Review proporzionata al rischio:** definire quando è sufficiente la review leggera e quando serve il controllo completo.
5. **Handoff ai builder:** verificare con un carousel LinkedIn se il brief A1 conserva contesto e autonomia specialistica senza duplicare il builder.

## Stato del lavoro

Questo documento è una proposta di progettazione. Le decisioni confermate su nome e accesso sono registrate nel documento autorevole del Marketing Agent System, ma non costituiscono ancora approvazione dell'intero Campaign Core, non creano skill installabili e non provano il funzionamento del workflow.

La sorgente `define-marketing-mix` v0.1.4 usa l'handoff `design-campaign`. Questa patch di authoring non modifica retroattivamente la versione v0.1.3 inclusa nella Suite beta.8 né la release singola pubblicata.

## Registro modifiche

- v1.2, 2026-08-31: ripristinato `campaign-debrief` come terzo modulo, insieme al blueprint v0.1 e al catalogo degli eval già progettati; `learn-from-results` era una rinomina intermedia non validata.
- v1.1, 2026-08-29: registrata l'installazione locale verificata di `design-campaign` v0.1.4; il retest comportamentale e la distribuzione pubblica restano separati.
- v1.0, 2026-08-29: il test utente della v0.1.3 su Sol high ha superato la progressione per differenza e ha evidenziato lessico troppo tecnico; candidata aggiornata a v0.1.4 con brief, funnel, fasi di marketing pertinenti, revisione finale e passaggio alla produzione come linguaggio visibile.
- v0.5, 2026-08-29: creata la sorgente candidata `design-campaign` v0.1.0; validazione strutturale superata e author self-check Fabriloom registrato con due residui da osservare.
- v0.6, 2026-08-29: registrato il forward test indipendente FAIL della v0.1.0 e aggiornata la sorgente a v0.1.1 per separare domande con proprietari diversi, capacità e risultato desiderato, dati storici e limiti.
- v0.7, 2026-08-29: il retest cieco della v0.1.1 ha replicato l'hard fail; aggiornata la sorgente a v0.1.2 con controllo esplicito decisione-proprietario nel flusso principale e una riga minima di misurazione.
- v0.8, 2026-08-29: il retest cieco indipendente della v0.1.2 è passato con zero hard fail e due soft fail non bloccanti; la candidata resta non installata e non pubblicata.
- v0.9, 2026-08-29: il test dell'utente sulla guida Da Chat a Work ha confermato il valore ma mostrato prolissità multi-turn e al gate; candidata aggiornata a v0.1.3 con risposta iniziale entro 500 parole, delta conversazionali, gate unico e isolamento esplicito dei test.
- v0.4, 2026-08-29: aggiunti fixture standalone Fabriloom, baseline della Campaign Spec e catalogo iniziale degli eval; scelto un carousel LinkedIn come primo handoff da verificare.
- v0.3, 2026-08-29: aggiunti esperienza standalone, routing delle domande e template modulare della Campaign Spec; definite fast lane, prima risposta e soglia di approvazione.
- v0.2, 2026-08-29: confermati il nome `design-campaign` e l'accesso standalone; distinti percorso standalone e collegato; definita la soglia minima di approvazione senza Strategy Core.
- v0.1, 2026-08-29: prima tesi, confini, artefatti e vertical slice del Campaign Core.
