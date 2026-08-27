# Marketing Agent System

Documento autorevole per progettare il sistema di regole, decisioni e skill che permette agli agenti AI di lavorare sul marketing di un'organizzazione. Deriva dal framework emerso nella conversazione **“Analisi framework marketer”** (20 agosto 2026) e registra progressivamente le decisioni approvate durante la progettazione.

## Tesi di prodotto

Il progetto non dovrebbe essere una raccolta di generatori per canale, né un “CMO artificiale” generico. Il suo valore distintivo è rendere installabile il processo decisionale di un marketer senior:

- capire se un’idea merita di essere eseguita;
- distinguere evidenze, inferenze e assunzioni;
- scegliere il formato e il test più adatti;
- trasformare una decisione in una campagna verificabile;
- controllare strategia, contenuti e asset;
- imparare dai risultati e aggiornare il playbook.

Promessa provvisoria:

> Install the decision process of a senior marketer.

Nome di lavoro: **Marketing Decision Skills**. Alternativa editoriale: **Marketing Workflows for Real Teams**.

## Principi architetturali

1. **Decisioni prima della produzione.** Una bella esecuzione non deve nascondere una strategia debole.
2. **Evidenze separate dalle ipotesi.** Ogni affermazione rilevante deve avere fonte, livello di certezza o indicazione esplicita di verifica necessaria.
3. **Approvazione umana nei punti irreversibili.** La skill propone e struttura; la scelta strategica finale resta dell’utente.
4. **Artefatti persistenti.** Contesto, profili, decisioni, brief e risultati diventano documenti riutilizzabili, non restano solo nella chat.
5. **Moduli esecutivi a valle.** Carousel Builder, Quote Card Builder, diagrammi, scrittura e brand skill producono gli asset dopo la decisione.
6. **Controlli integrati.** Review, test e confronto tra previsione e risultato fanno parte del metodo.
7. **Friction minima.** L’utente deve poter usare direttamente un builder quando formato e obiettivo sono già chiari.

## Architettura proposta

```text
Augmented Marketing Suite
        └── Augmented Marketing Assistant  (ingresso conversazionale e orientamento)
                ├── setup-business-context  (identità durevole di azienda o brand)
                ├── setup-marketing-system  (Fondamenti di marketing)
                ├── Strategy Core  → define-marketing-challenge → choose-marketing-direction → define-marketing-mix
                ├── Campaign Core  → to-campaign-spec → campaign-review → learn-from-results
                └── Content Core   → Content Director → builder specializzati
```

**Augmented Marketing Assistant** è un agente sottile e non un nuovo core. Riceve il bisogno nel linguaggio dell'utente, verifica soltanto stati e artefatti osservabili, spiega il passaggio utile e attiva la skill pertinente quando l'ambiente lo consente. Se non può effettuare il passaggio, indica all'utente la skill da invocare e si ferma senza simularne il metodo. Non possiede logica strategica, artefatti o approvazioni propri e non impone il percorso completo quando l'input necessario esiste già. Nel plugin OpenAI compare tecnicamente come sesta skill (`augmented-marketing-assistant`), ma questa forma è soltanto un adattatore di caricamento e non una nuova competenza di marketing.

La [definizione canonica stabile v0.1.0](agents/augmented-marketing-assistant.md) resta indipendente da comandi e manifest proprietari. Il [relativo adattatore OpenAI](skills/augmented-marketing-assistant/SKILL.md) ne preserva ruolo e confini nel formato caricato da ChatGPT e Codex ed è incluso nella Suite beta 0.1.0-beta.5. Gli [scenari conversazionali sintetici](evals/augmented-marketing-assistant/scenarios-v0.1.md), il [test cieco in una sessione Codex separata](evals/augmented-marketing-assistant/runs/2026-08-27-blind-codex-v0.1.md), il [regression test runtime Codex della beta.5](evals/augmented-marketing-assistant/runs/2026-08-27-codex-runtime-smoke-beta5.md) e il test reale su ChatGPT Web verificano aspetti diversi, ma non equivalgono a un pilot con marketer esterni. Il regression test ha superato con tre PASS richiesta ambigua, selezione diretta e handoff effettivo.

I tre core non sono cartelle decorative e non devono diventare tre agenti generalisti. Sono famiglie di decisioni con artefatti e confini diversi:

- **Strategy Core:** definisce quale problema, pubblico, comportamento o opportunità richiedono una decisione, sceglie la direzione e la traduce in un marketing mix coerente su Product, Price, Place e Promotion;
- **Campaign Core:** traduce la componente Promotion e le attivazioni pertinenti di un marketing mix approvato in un sistema coordinato di messaggi, canali, asset, responsabilità, misure e apprendimento;
- **Content Core:** valuta e produce singoli contenuti o famiglie di contenuti, mantenendo il giudizio specifico nei builder.

Nel nucleo minimo non è previsto un agente **Strategist** separato. Il lavoro strategico appartiene alle tre skill dello Strategy Core, mentre l'Assistant conserva soltanto orientamento e continuità. Un eventuale componente trasversale potrà essere valutato soltanto se l'uso reale farà emergere un compito distinto, con una propria user story e un proprio artefatto, per esempio una revisione di coerenza tra sfida, direzione e marketing mix. Non dovrà duplicare il routing dell'Assistant né il metodo delle skill specialistiche.

`setup-marketing-system` è l'onboarding delle Marketing Foundations, non il punto d'ingresso generale e non un quarto core. Aiuta l'organizzazione a definire e approvare le regole di marketing stabili che un agente deve conoscere prima di qualsiasi attività di marketing. Parte dal business context canonico e dalle regole, decisioni, materiali e pratiche reali già disponibili; quando una regola operativa essenziale manca, può guidarne la formulazione invece di limitarsi a registrare il vuoto. Costruisce un profilo operativo riusabile dai tre core. Per aziende multi-brand può mantenere un livello aziendale e overlay di brand, sempre referenziando le identità canoniche create da `setup-business-context` invece di copiarle.

Ogni regola formulata con l'aiuto dell'agente resta una proposta finché un responsabile non la approva esplicitamente. La skill può facilitare la definizione di standard operativi persistenti, ma non deve trasformare il setup in una strategia completa, scegliere autonomamente obiettivi, segmenti, posizionamento, budget o campagne, né presentare una raccomandazione come decisione aziendale già adottata.

Le regole editoriali, visive e qualitative minime fanno parte delle **Marketing Foundations**. Manuali, template, asset e brand guideline dettagliati restano documenti esterni referenziati, non un secondo profilo prodotto automaticamente. Una skill autonoma sarà giustificata solo se l'uso reale dimostrerà che importazione, portabilità o manutenzione di questi materiali costituiscono un lavoro distinto.

Un modulo opzionale di ascolto può alimentare il sistema prima di una decisione o in modo continuativo:

```text
monitoring-setup  (autonomo e opzionale)
        ↓
fonti, query, segnali e digest
        ↓
raccolta di evidenze opzionale → Strategy Core / Campaign Core / Content Director
```

`monitoring-setup` deve conservare valore anche fuori dal framework, per esempio per un giornalista o un ricercatore che desidera monitorare un tema senza usare gli altri moduli.

Il percorso non è sempre lineare:

- fonte o idea con formato incerto → **Content Director** → builder consigliato;
- formato già deciso → builder direttamente;
- contenuto prodotto altrove → **Editorial Review** autonoma, eventualmente futura.

## Skill di monitoraggio web

La skill discussa nella conversazione **“Esplora skill per monitoraggio web”** può entrare nel framework come **`monitoring-setup`** (nome alternativo: `web-radar-setup`). Non dovrebbe essere un generico monitoratore del web e non dovrebbe sostituire gli strumenti di raccolta già esistenti.

Il suo ruolo è progettare e configurare un sistema di monitoraggio per uno specifico caso d’uso, trasformando:

> “Voglio sapere cosa succede su questo argomento”

in:

> “Queste sono le fonti, le query, i criteri di rilevanza, la frequenza, gli alert e il digest operativo”.

### Responsabilità

- chiarire l’obiettivo: competitor, reputazione, normativa, innovazione, bandi, prezzi, clienti o ricerca;
- costruire tassonomia, sinonimi e query;
- individuare e classificare le fonti;
- scegliere il metodo adatto per ogni fonte;
- definire frequenza, urgenza, soglie e regole anti-rumore;
- produrre configurazione, digest, checklist di test e runbook di manutenzione;
- documentare privacy, accessi, paywall, CAPTCHA, limiti e affidabilità.

### Strumenti e livello di astrazione

La skill deve restare agnostica rispetto allo strumento e proporre una configurazione minima funzionante:

- Google Alerts o RSS per i casi semplici;
- changedetection.io per pagine, documenti e cambiamenti puntuali;
- RSSHub per fonti prive di feed;
- Huginn o n8n per flussi con condizioni, webhook e distribuzione;
- dashboard o sintesi AI solo quando aggiungono valore reale.

Il mercato offre già motori potenti; il vuoto interessante è la metodologia di installazione. La skill deve quindi operare sopra questi strumenti, non competere con loro.

### Output standard

- brief del problema;
- mappa delle fonti;
- keyword e query booleane;
- matrice fonte/metodo/frequenza;
- schema degli alert;
- configurazione tecnica;
- template del digest giornaliero o settimanale;
- checklist di test;
- runbook di manutenzione;
- dichiarazione dei limiti.

### Relazione con il framework

`monitoring-setup` non decide ancora quale contenuto produrre. Fornisce segnali e materiali ai workflow Strategy, a `Content Director` o direttamente a un sistema di briefing. Un eventuale `build-evidence-pack` resta una capacità opzionale futura per i casi in cui fonti numerose, conflittuali o riusate da più workflow giustifichino un artefatto autonomo; non è un passaggio obbligatorio dello Strategy Core. Il Content Director continua a valutare rilevanza, solidità, obiettivo e formato; i builder producono l’asset.

Per questo è una skill **abilitante e opzionale**, non un passaggio obbligatorio di ogni campagna.

### Distribuzione

È adatta come asset gratuito per clienti, lead magnet e strumento di reputazione. Si può articolare in tre livelli:

1. **Starter:** Google Alerts, RSS e digest manuale;
2. **Pro:** changedetection.io, filtri, notifiche e fonti personalizzate;
3. **Advanced:** RSSHub, Huginn/n8n, sintesi AI e archivio storico.

La promessa concreta può essere:

> Costruisci il tuo radar informativo personalizzato e smetti di controllare manualmente decine di siti.

## Nucleo iniziale delle skill

### Fondazione consolidata e Strategy Core

Al momento il repository contiene cinque skill sorgente approvate:

- `setup-business-context`: identità aziendale o di brand persistente, verificabile e riusabile.
- `setup-marketing-system`: regole di marketing stabili, verificabili e riusabili dai workflow a valle.
- `define-marketing-challenge`: Brief della sfida confermato e pronto al confronto strategico, disponibile come release stabile `v0.1.1`.
- `choose-marketing-direction`: confronto strategico e Direzione di marketing approvabile, disponibile come release stabile `v0.2.0`.
- `define-marketing-mix`: traduzione della direzione approvata nelle quattro P, disponibile come release stabile `v0.1.1`.

Le due skill di Strategy Core sono approvate e disponibili come release stabili, con istruzioni di installazione, fixture sintetiche e forward test indipendenti senza hard fail. Non sono automaticamente installate o attive nell'ambiente dell'utente. Gli altri core e le relative competenze restano roadmap o ipotesi da validare. Il set resta intenzionalmente incompleto: non produce campagne complete e non automatizza la pubblicazione.

Le cartelle sotto `skills/` sono sorgenti di authoring, non prova di installazione attiva. Ogni ambiente che supporta skill può richiedere una destinazione, un pacchetto o un adattatore specifico. Authoring, installazione locale e distribuzione restano tre gate distinti, e la presenza della sorgente non dimostra il caricamento nella sessione.

Il nucleo è indipendente dall'adattatore di distribuzione. Il [contratto di portabilità](PORTABILITA.md) definisce capability obbligatorie e opzionali, comportamento degli artefatti quando il workspace non è scrivibile, limiti dei connector e scenari minimi di verifica. Comandi, hook, manifest, marketplace e instruction file specifici non appartengono al contratto essenziale delle skill.

### Supporto visuale opzionale all'onboarding

Le skill di setup possono usare una capability visuale dedicata, quando è disponibile e migliora concretamente la comprensione, per generare una vista interattiva singola di revisione. Questa composizione è un miglioramento progressivo e capability-gated, non una dipendenza necessaria: il percorso chat-first deve restare completo e produrre lo stesso risultato canonico anche senza interfaccia visuale.

La superficie visuale può aiutare a esplorare una proposta, confrontare alternative e individuare conflitti o vuoti. Non possiede lo stato del processo, non trasporta input essenziali tra i turni, non raccoglie approvazioni canoniche e non autorizza scritture. Ogni scelta conseguente viene riportata in chat in forma comprensibile e confermata esplicitamente prima di modificare un artefatto persistente; JSON, YAML e altri envelope tecnici non vengono esposti come stato visibile all'utente.

Se la capability non è disponibile, fallisce o perde continuità, l'agente prosegue dall'ultimo stato confermato in chat senza chiedere di reinserire informazioni già acquisite e senza ridurre la qualità dell'output. Un wizard multi-step deterministico, con stato persistente e input/output tipizzati, richiederebbe un'applicazione o uno strumento dedicato e resta fuori dal perimetro iniziale delle skill di setup.

Per `setup-business-context`, l'eventuale vista serve a revisionare identità provvisoria, provenienza, conflitti e incognite. Per `setup-marketing-system`, serve a revisionare in modo compatto regole stabili, scope, overlay di brand e decisioni ancora aperte. In entrambi i casi è una superficie di revisione opzionale, non il processo autorevole.

### 1. Fondazione — `setup-business-context`

Costruisce e installa la carta d'identità persistente che gli agenti devono conoscere prima di lavorare per o su un'azienda o un brand. Parte soltanto dalle fonti fornite, allegate o citate dall'utente; prepara prima una bozza e pone poche domande sui vuoti realmente decisivi.

La skill distingue le informazioni confermate dal responsabile, documentate da una fonte, inferite dall'agente o ancora ignote. Mantiene visibili le contraddizioni e non trasforma un'inferenza in un fatto attraverso la riscrittura.

L'onboarding conserva quattro macro-fasi — entità e fonti, revisione della bozza, risoluzione dei vuoti decisivi, approvazioni — ma il numero di domande varia in base ai materiali. Nel primo ciclo la chat testuale è l'interfaccia primaria: dopo l'invio delle fonti, il turno successivo deve produrre direttamente una comprensione provvisoria utile o un blocker concreto, senza renderizzazioni o trasferimenti di stato intermedi.

La precedente card interattiva continua a essere un esperimento fuori dal pacchetto attivo. Un'eventuale nuova vista viene generata soltanto come supporto opzionale alla revisione, secondo la policy visuale comune: input essenziali, stato confermato e approvazioni restano in chat.

Un elemento non trovato nelle fonti non viene dichiarato inesistente. La skill distingue tra informazione disponibile, esistente ma non disponibile, non definita dall'organizzazione, ignota all'utente e non applicabile. I vuoti essenziali richiedono uno stato esplicito; quelli importanti ma non bloccanti, come una missione non documentata, restano visibili nell'identità senza essere inventati.

La selezione delle domande applica due lenti complementari — marketing e modello di business — senza trasformarsi in un workshop strategico. Dopo aver estratto ciò che le fonti già sostengono, l'agente privilegia al massimo tre vuoti per volta: perimetro e offerta corrente, sistema cliente/utente/pagatore/decisore, situazione che genera la domanda, alternative reali, capacità distintiva, valore, prova, fraintendimenti e vincoli. Obiettivi di crescita, nuovi segmenti, pricing, canali e posizionamento futuro restano fuori dal setup.

L'output canonico è separato dalla skill:

- `.agents/company-identity.md` per un'azienda;
- `.agents/brand-identity.md` per un brand autonomo;
- `.agents/brands/<brand>.md` per un brand appartenente a un'azienda.

Un contesto di brand figlio viene usato insieme all'identità dell'azienda, non al suo posto. I workflow a valle referenziano entità, percorso, versione e data di revisione invece di duplicare i fatti in nuovi profili. La freschezza viene verificata attraverso cambiamenti concreti — offerte, perimetro, relazioni di brand, prove o vincoli — non con una scadenza generica.

Il flusso ha due approvazioni distinte: la prima autorizza il salvataggio dell'identità; la seconda autorizza l'eventuale modifica spiegata e circoscritta di `AGENTS.md`, `CLAUDE.md` o di entrambi. La skill documenta l'identità esistente: non definisce la strategia, non produce campagne, non configura strumenti e non inventa un posizionamento o una brand identity mancanti.

### 2. Punto d'ingresso — `setup-marketing-system`

Aiuta un'organizzazione a definire le regole di marketing stabili che gli agenti devono conoscere prima di svolgere qualsiasi attività di marketing. Parte dal business context canonico e dalle evidenze disponibili sul modo in cui l'organizzazione opera, non da una scelta fra nomi interni di skill. Verifica il business context e crea un profilo operativo riusabile dai tre core.

La prima versione si limita alle regole che devono valere trasversalmente nel tempo e nelle diverse attività. Non include nell'onboarding obiettivi trimestrali, priorità di periodo, campagne attive, budget, KPI temporanei o piani di canale legati a una singola iniziativa. Questi elementi appartengono ai workflow a valle o a un eventuale overlay temporaneo futuro; non devono allungare il setup iniziale.

Il nucleo minimo approvato della prima versione comprende cinque aree:

1. regole per collegare offerte, pubblici e situazioni d'uso;
2. messaggi, claim e prove che possono essere utilizzati;
3. ruolo generale di canali e formati;
4. standard editoriali, visivi e qualitativi;
5. controlli e approvazioni necessari.

Queste aree definiscono il risultato del setup, non un questionario fisso. L'agente deve prima ricavare quanto può dal business context e dai materiali disponibili, quindi chiedere soltanto ciò che serve per formulare o approvare le regole mancanti. Se esistono più brand, il profilo mantiene una base aziendale e overlay espliciti; non fonde automaticamente contesti diversi.

#### Esperienza di onboarding

L'utente di riferimento è un responsabile interno autorizzato a definire o approvare le regole di marketing. Conosce l'organizzazione e possiede competenze di business e marketing, ma non è tenuto a conoscere skill, agenti, file di configurazione o l'architettura interna del framework.

La skill deve quindi parlare il linguaggio del lavoro e delle decisioni: offerte, pubblici, messaggi, prove, canali, qualità e approvazioni. Non deve chiedere all'utente di scegliere core, moduli, percorsi o formati tecnici; traduce autonomamente le risposte nella struttura operativa pertinente. Quando una decisione comporta una scrittura o un'installazione, spiega l'effetto in termini comprensibili prima di chiedere l'approvazione.

L'aha moment dell'onboarding arriva quando il responsabile vede una prima serie di regole utili già ricostruite dall'agente e riconosce che il sistema ha compreso come deve operare sul marketing dell'organizzazione. Il valore non coincide con il completamento di un questionario o con la spiegazione dell'architettura del framework.

Il percorso approvato è chat-first e ottimizzato per arrivare rapidamente a quel momento:

1. leggere il business context canonico;
2. analizzare i materiali marketing forniti o indicati dall'utente;
3. presentare nel primo turno sostanziale una proposta compatta delle regole già ricavabili nelle cinque aree;
4. porre al massimo tre domande sulle sole decisioni essenziali ancora mancanti;
5. mostrare il profilo completo soltanto al momento dell'approvazione.

Non deve esserci un questionario preliminare né un tutorial separato. L'agente non chiede di riscrivere informazioni già disponibili, non espone all'utente i nomi interni dei core e non usa turni di solo avanzamento. Se l'utente fornisce già un playbook o regole sufficientemente complete, il flusso passa direttamente alla revisione. Se esiste un profilo approvato, la skill ne riepiloga stato e rischi di aggiornamento e interviene soltanto sulle regole interessate, senza ripetere l'onboarding.

Nel primo ciclo la qualità dell'esperienza viene osservata attraverso tempo e turni fino alla prima proposta utile, domande superflue, correzioni necessarie e completamento dell'approvazione. Non si fissa ancora una durata numerica senza una baseline reale.

#### User story primaria e riuso

> Come direttore marketing, uso `setup-marketing-system` per creare e approvare il profilo marketing stabile della mia organizzazione, così l'agente può applicarlo ogni volta che gli chiedo di svolgere un'attività di marketing aziendale.

Il setup crea un artefatto canonico persistente: il riuso non dipende dalla memoria della conversazione in cui è stato costruito. Prima di ogni attività di marketing specifica dell'organizzazione, l'agente deve leggere il business context e il profilo marketing approvato, insieme all'eventuale overlay del brand pertinente, e applicarne regole e vincoli.

Il profilo è un prerequisito per il lavoro di marketing aziendale, non per domande generiche sul marketing. Se manca, non è approvato, non è leggibile o presenta un rischio concreto di obsolescenza, l'agente non deve fingere di conoscere le regole dell'organizzazione: segnala il problema e propone di creare o aggiornare il profilo prima di procedere. L'avvio del setup o dell'aggiornamento resta esplicito; il controllo preliminare da parte delle skill a valle è automatico.

#### Trasparenza del riuso — decisione approvata

Ogni risposta che svolge o fa avanzare in modo sostanziale un'attività di marketing specifica dell'organizzazione deve mostrare un FYI breve con il contesto effettivamente applicato. La formula resta informativa e non interrompe il lavoro, per esempio:

> Nota operativa: contesto applicato, Identità Acme v2 + Fondamenti di marketing v1 + integrazione Brand X v1.

Il FYI indica almeno entità e versioni della business identity, delle Marketing Foundations e dell'eventuale overlay pertinente. Non elenca normalmente percorsi, fonti o dettagli tecnici, che restano disponibili su richiesta. Deve riflettere soltanto file realmente letti e verificati nella sessione: la configurazione di un instruction file non basta per dichiarare che il contesto sia stato applicato.

Se un artefatto richiesto manca, è illeggibile, non approvato, incoerente o materialmente obsoleto, l'agente sostituisce il FYI con un avviso esplicito e azionabile; non afferma di aver applicato un profilo valido. Le domande generiche sul marketing e i messaggi di puro coordinamento non richiedono il FYI.

#### Percorso continuo delle Foundations e dipendenza dal business context — decisione approvata

Nel percorso dedicato alle Marketing Foundations, `setup-marketing-system` mantiene la continuità anche quando il business context non è ancora stato creato. All'avvio verifica l'identità canonica pertinente:

- se è approvata e utilizzabile, procede con le Marketing Foundations;
- se manca o deve essere aggiornata e `setup-business-context` è disponibile, orchestra nello stesso dialogo la creazione o l'aggiornamento del contesto minimo necessario, riutilizzando materiali e risposte già acquisiti;
- dopo l'approvazione e la scrittura dell'identità, riprende il setup marketing senza chiedere all'utente di conoscere o riavviare manualmente un'altra skill.

Il routing interno non deve nascondere ciò che viene approvato. Business identity e Marketing Foundations restano artefatti distinti, con scope, percorsi, versioni e approvazioni canoniche esplicite. La skill non duplica dentro le Marketing Foundations i contenuti o la logica di `setup-business-context`. L'eventuale installazione nelle istruzioni dell'agente può essere rinviata alla fine del percorso e proposta con un diff unico che elenchi chiaramente entrambi i riferimenti, senza accorpare le approvazioni dei contenuti.

##### Fallback quando la dipendenza non è disponibile — decisione approvata

Se `setup-business-context` non è disponibile nell'ambiente, `setup-marketing-system` può suggerirne l'acquisizione spiegando in linguaggio non tecnico perché è necessaria. Deve indicare una fonte verificabile, la versione proposta e la destinazione prima di chiedere il consenso; non inventa un URL e non scarica automaticamente. Il download e l'installazione sono azioni distinte: prima di ciascuna richiede un'approvazione esplicita e, tra le due, verifica struttura e integrità del pacchetto. Se l'utente rifiuta o rinvia, la skill può continuare soltanto con una bozza provvisoria e non dichiara approvate, canoniche o automaticamente disponibili le Marketing Foundations.

La distribuzione preferita include o dichiara `setup-business-context` come dipendenza, così il recupero esterno resta un fallback e non un passaggio ordinario dell'onboarding.

#### Artefatto canonico — decisione approvata

L'identificatore tecnico dell'artefatto resta `marketing-foundations`, ma il titolo, le etichette e gli stati sono espressi nella lingua di lavoro del responsabile. In italiano l'artefatto è presentato come “Fondamenti di marketing”; l'etichetta “profilo marketing operativo” non è adottata perché rischia di far pensare che le fondazioni strategiche stabili siano escluse e che serva automaticamente un secondo profilo strategico.

La prima versione produce un unico artefatto canonico chiamato **Marketing Foundations**, che riunisce le regole stabili necessarie agli agenti: relazione tra offerte e pubblici, messaggi e prove, ruolo generale dei canali, standard di qualità e approvazioni. Le strategie riferite a obiettivi, priorità, mercati, budget o periodi specifici restano invece artefatti distinti dei workflow Strategy e Campaign, perché cambiano con una frequenza e per una ragione diverse.

La struttura approvata dei **Fondamenti di marketing** ha tre livelli:

1. **Riferimenti di contesto**: entità, business identity collegata, versione, proprietario e data di revisione;
2. **Regole di marketing stabili**: le cinque aree approvate del setup;
3. **Governance**: fonti e provenienza, conflitti, regole mancanti, trigger di aggiornamento e changelog.

Il primo livello referenzia la business identity canonica senza ricopiarne i contenuti. Il secondo contiene soltanto regole persistenti e approvate. Il terzo rende visibili base, limiti e manutenzione dell'artefatto.

#### Formato dell'artefatto — decisione approvata

Il file canonico è Markdown nella lingua di lavoro del responsabile, leggibile sia dal responsabile sia dall'agente. Il frontmatter tecnico resta minimo e rende verificabili almeno versione, stato, entità, scope, proprietario, data dell'ultima revisione e percorso/versione del business context collegato. Il corpo usa titoli e regole esplicite; non è un dump YAML o JSON né richiede all'utente di comprendere una struttura dati per revisionarlo. In italiano, stati, etichette e spiegazioni restano in italiano; l'inglese è riservato a termini di marketing consolidati quando naturali.

Durante l'onboarding la skill presenta il contenuto in linguaggio manageriale e in una forma compatta, pur rendendo integralmente revisionabili le informazioni che entreranno nell'artefatto al gate di approvazione. Non espone serializzazioni tecniche come meccanismo di stato o continuità della conversazione. La struttura tecnica viene spiegata soltanto quando serve a comprendere una modifica, un riferimento o una conseguenza dell'approvazione.

Lo schema dettagliato sarà mantenuto in una reference dedicata della skill; `SKILL.md` conterrà soltanto lo scopo, il workflow, i vincoli essenziali e il criterio che indica quando leggere quella reference. In questo modo lo schema resta stabile e verificabile senza appesantire ogni invocazione.

#### Modello rule-first — decisione approvata

Le Marketing Foundations sono costruite attorno a regole applicabili, non a descrizioni generiche dell'organizzazione. Ogni regola deve permettere all'agente di comprendere:

- quale comportamento è richiesto, consentito o vietato;
- in quale condizione e scope si applica;
- su quale fonte, decisione approvata o altra base si fonda;
- quale eccezione, approvazione o comportamento prudente vale quando è rilevante.

Questi elementi sono requisiti di chiarezza, non quattro campi obbligatori da compilare per ogni regola. La forma può restare naturale e compatta. Le informazioni descrittive servono soltanto quando chiariscono l'applicazione; non devono costringere l'agente a dedurre una regola operativa da un paragrafo narrativo.

Quando una decisione manca, la skill non inventa una direttiva: registra il vuoto con stato, impatto e comportamento prudente. Conflitti, assunzioni e regole proposte restano distinguibili dalle regole approvate fino alla loro risoluzione.

##### 1. Coerenza tra offerta, pubblico e situazione: decisione approvata

Questa area non ricopia il catalogo delle offerte né le descrizioni dei pubblici presenti nel business context. Referenzia le entità canoniche e registra le regole stabili necessarie per collegarle correttamente nel lavoro di marketing:

- quali offerte sono pertinenti per quali pubblici;
- in quali situazioni, bisogni o risultati desiderati la relazione è valida;
- quali condizioni indicano buon fit, cattivo fit o esclusione;
- quale comportamento prudente adottare quando il fit non è chiaro.

Non contiene priorità trimestrali, segmentazioni di una campagna o personas create per una singola iniziativa. Il business context stabilisce chi è l'organizzazione, cosa offre e quali pubblici conosce; le Marketing Foundations stabiliscono come usare stabilmente queste relazioni nelle attività di marketing.

##### 2. Messaggi, claim ed evidenze: decisione approvata

Questa area stabilisce:

- quali messaggi o temi di valore sono approvati per offerte, pubblici e situazioni;
- quali claim sono consentiti, condizionati o vietati;
- quali riscontri sono necessari per sostenere i diversi tipi di claim;
- quali qualificazioni, limitazioni o approvazioni devono accompagnarne l'uso;
- quale comportamento prudente adottare quando un riscontro manca, è scaduto o non sostiene pienamente il claim.

Per **evidence** si intendono riscontri verificabili già esistenti, come specifiche, policy, dati, ricerche, certificazioni, case study, testimonianze autorizzate o pagine aziendali approvate. L'onboarding non chiede al responsabile di produrre nuovi studi, case study o evidence pack: cerca prima nei materiali e nel business context, quindi domanda soltanto dove reperire un riscontro necessario per un claim importante.

La sezione non duplica il registro delle prove del business context; lo referenzia e definisce come i riscontri possono essere usati nel marketing. Se la base è insufficiente, l'agente non usa il claim come fatto: può proporre una formulazione più prudente da approvare oppure richiedere verifica. Non contiene copy di campagna e non trasforma automaticamente un'ipotesi di posizionamento in un messaggio approvato.

##### 3. Ruolo di canali e formati: decisione approvata

Questa area descrive soltanto decisioni stabili:

- a cosa serve normalmente ciascun canale;
- per quali pubblici, situazioni o offerte è adatto;
- quali formati hanno un ruolo riconosciuto;
- quali limiti, usi impropri e condizioni devono essere rispettati;
- quale comportamento prudente adottare quando il ruolo di un canale o formato non è definito.

La skill ricava queste regole dal lavoro e dai materiali reali dell'organizzazione; non impone al responsabile di compilare in anticipo una matrice di tutte le piattaforme. Un canale non trovato nelle fonti resta `non stabilito dalle fonti fornite` finché l'utente non ne classifica lo stato: non viene dichiarato automaticamente inattivo o non utilizzato.

La sezione non contiene calendario editoriale, frequenze temporanee, budget, media plan, mix di una campagna o configurazione degli account. Queste sono decisioni riferite a un periodo o a un'iniziativa e appartengono ai workflow a valle.

##### 4. Standard editoriali, visivi e di qualità: decisione approvata

Questa area contiene le regole minime che ogni output marketing deve rispettare:

- applicazione di voce, lingua e terminologia canoniche;
- standard editoriali e visivi trasversali;
- riferimenti obbligatori a brand guideline, template e asset approvati;
- requisiti di accuratezza, accessibilità e qualità;
- errori o pratiche vietate;
- controlli minimi prima che un output possa essere considerato pronto.

Le Marketing Foundations contengono le istruzioni applicabili dagli agenti e referenziano i documenti autorevoli già esistenti. Non creano né duplicano logo, visual identity, template, asset, manuali editoriali o brand guideline. Se un documento esterno è necessario per applicare una regola, il profilo ne registra percorso o riferimento, versione quando disponibile e scope.

Nella prima versione questa area non genera automaticamente un secondo profilo editoriale o visuale. Un artefatto separato richiederà una necessità osservabile di portabilità, manutenzione, proprietà o permessi differenti; le differenze di un brand appartenente a un'azienda possono invece vivere nel relativo overlay marketing.

##### 5. Controlli, autorità e approvazioni: decisione approvata

Questa area stabilisce:

- quali attività l'agente può svolgere autonomamente, può soltanto proporre o non deve svolgere;
- quali azioni richiedono approvazione prima di modificare, inviare, pubblicare o spendere;
- quali ruoli aziendali sono autorizzati ad approvare i diversi tipi di output;
- quando sono necessari controlli legali, privacy, compliance o brand;
- quale comportamento prudente adottare quando responsabilità o autorizzazione non sono chiare.

L'approvazione del contenuto resta distinta dall'autorizzazione all'esecuzione: approvare un testo, un piano o un asset non autorizza automaticamente a pubblicarlo, inviarlo, configurarlo o attivare una spesa. La sezione registra soltanto autorità e controlli confermati; non inventa una catena approvativa e non configura strumenti o workflow.

Se manca una regola essenziale, il default è lavorare in modalità bozza o raccomandazione e fermarsi prima di qualsiasi azione esterna. Le autorizzazioni registrate nel profilo non ampliano comunque i permessi effettivi concessi all'agente nella singola attività.

##### Governance del profilo — decisione approvata

Le Marketing Foundations riutilizzano la grammatica di provenienza del business context:

- `[C]` — confermato dal responsabile o da uno stakeholder autorizzato;
- `[S1]`, `[S2]`, ... — documentato in una fonte registrata;
- `[I]` — inferito dall'agente e non ancora confermato;
- `[?]` — vuoto o conflitto irrisolto.

I marcatori si applicano alle regole e alle decisioni conseguenti, non a ogni frase amministrativa. In un profilo approvato nessun elemento `[I]` può funzionare come regola operativa: prima della scrittura deve essere confermato, spostato tra i vuoti con il relativo fallback oppure rimosso.

La governance include un registro delle fonti, conflitti distinti in bloccanti e non bloccanti, incognite con stato, impatto e comportamento prudente, trigger di revisione basati su cambiamenti reali e un changelog. Un nuovo profilo approvato parte da `v1`; una modifica sostanziale incrementa la versione intera e aggiorna la data di revisione, mentre una correzione puramente tipografica preserva versione e changelog.

I percorsi canonici approvati sono:

- `.agents/marketing/foundations.md` per le **Marketing Foundations** dell'azienda o del brand autonomo;
- `.agents/marketing/brands/<brand-slug>.md` per l'overlay di un brand appartenente a un'azienda.

Il file base referenzia l'identità canonica pertinente: `.agents/company-identity.md` per un'azienda oppure `.agents/brand-identity.md` per un brand autonomo. Per un brand appartenente a un'azienda, l'agente legge in ordine l'identità aziendale, l'identità del brand, le Marketing Foundations aziendali e infine l'overlay marketing del brand. Ogni riferimento registra percorso e versione dell'artefatto verificato.

L'overlay contiene soltanto differenze e specializzazioni valide nello scope esplicito del brand; non ricopia le regole aziendali. Identifica inoltre il file base e la versione rispetto alla quale è stato verificato. L'ordine di lettura non autorizza a risolvere silenziosamente un conflitto materiale: la skill deve renderlo visibile e richiederne la risoluzione prima di approvare o aggiornare l'overlay.

#### Approvazione e installazione — decisione approvata

La creazione o l'aggiornamento delle **Marketing Foundations** usa due gate distinti, che non possono essere accorpati in un consenso generico:

1. **Approvazione del contenuto e scrittura canonica.** La skill mostra il profilo completo proposto, distinguendo fonti, inferenze, regole formulate con l'utente, conflitti e vuoti. Indica il percorso che verrà creato o aggiornato e, in caso di revisione, rende comprensibili le modifiche. Scrive il file canonico soltanto dopo un'approvazione esplicita del responsabile autorizzato.
2. **Installazione nelle istruzioni dell'agente.** Dopo la scrittura, la skill spiega quale instruction file locale propone di modificare, quale regola di caricamento aggiungerà e quali artefatti verranno letti. Richiede una seconda approvazione esplicita prima di modificare `AGENTS.md`, `CLAUDE.md` o un file equivalente.

Il secondo gate non è implicito nel primo. Se l'installazione viene rifiutata o rinviata, le Marketing Foundations restano un artefatto canonico valido, ma la skill non deve dichiarare che il caricamento automatico sia configurato. Lo stesso principio vale per gli aggiornamenti: approvare una nuova versione del profilo non autorizza modifiche ulteriori alle istruzioni dell'agente.

#### Criterio di utilizzabilità — decisione approvata

Le **Marketing Foundations** non devono essere complete in ogni dettaglio per diventare utilizzabili. Possono essere approvate quando:

- il business context referenziato è approvato, leggibile e coerente con l'entità del profilo;
- tutte e cinque le aree delle regole stabili sono state valutate;
- ogni area contiene regole approvate oppure una classificazione precisa dei vuoti residui;
- non restano conflitti bloccanti irrisolti;
- controlli, responsabilità e approvazioni essenziali sono sufficientemente definiti;
- per ogni vuoto non bloccante è indicato il comportamento prudente che l'agente deve adottare finché la regola non viene definita.

La mancanza di informazioni non equivale a inesistenza. Un vuoto può restare nel profilo solo se il suo stato e il suo impatto sono visibili; se impedisce all'agente di operare senza inventare una decisione o superare un'autorità, blocca l'approvazione. La skill privilegia quindi un profilo minimo ma onesto rispetto a un onboarding lungo o a una completezza solo apparente.

La prima versione non separa un profilo “strategic” da uno “operational”. Un eventuale secondo artefatto persistente richiederà in futuro una motivazione osservabile, come proprietari, frequenze di aggiornamento, permessi o utilizzatori realmente differenti. La sola eleganza della tassonomia non giustifica un secondo file né un onboarding più lungo.

Anche se in futuro la stessa skill producesse più artefatti, non dovrebbe iniziare chiedendo all'utente quale file vuole creare. Il responsabile descrive il bisogno e i materiali disponibili; la skill riconosce il percorso pertinente e spiega l'artefatto proposto in termini manageriali prima di richiederne l'approvazione.

Se una regola operativa essenziale non è ancora stata definita, la skill può aiutare il responsabile a formularla attraverso una proposta motivata, alternative comprensibili o una domanda ad alta leva. La regola entra nel profilo solo dopo approvazione esplicita e con una base distinguibile dalle informazioni già esistenti.

Questa skill orchestra il setup, ma non deve simulare di aver completato una strategia o una campagna. Non sceglie autonomamente obiettivi, segmenti, posizionamento, budget, canali di una specifica iniziativa o piani di esecuzione. La discovery ha definito schema, percorsi, approvazioni e criteri di utilizzabilità; la loro traduzione nei file della skill resta un gate di authoring separato.

#### Blueprint di authoring — decisione approvata

La prima versione dovrebbe usare la struttura minima seguente:

```text
skills/setup-marketing-system/
├── SKILL.md
├── INSTALL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── marketing-foundations-template.md
    ├── question-routing.md
    └── installation.md
```

Responsabilità dei file:

- `SKILL.md` — frontmatter con nome, descrizione discriminante e versione; trigger di creazione, aggiornamento e installazione; controllo del business context; workflow chat-first; cinque aree; provenienza; gate; confini e routing alle reference;
- `INSTALL.md` — installazione da ZIP o sorgente GitHub, verifica della versione, checksum e avvertenze sul caricamento della skill in una nuova sessione;
- `agents/openai.yaml` — metadati UI nella lingua di lavoro del repository, coerenti con la skill e con l'invocazione automatica disponibile;
- `references/marketing-foundations-template.md` — frontmatter dell'artefatto, schema completo, composizione base/overlay, regole di versione e un esempio minimo di regola;
- `references/question-routing.md` — criteri per estrarre una prima proposta utile e scegliere al massimo tre vuoti decisivi senza eseguire un questionario;
- `references/installation.md` — adattatori per instruction file, blocchi gestiti, diff da approvare, composizione identity/foundations/overlay e FYI obbligatorio.

La prima versione non richiede `scripts/`, `assets/`, esempi generici o un README interno alla skill: non esiste ancora una trasformazione deterministica ripetuta che giustifichi codice, e i dettagli condizionali sono coperti dalle tre reference. La logica di `setup-business-context` viene richiamata come dipendenza, non copiata.

Il piano di test proposto resta separato dal pacchetto pubblicabile della skill:

```text
evals/setup-marketing-system/
├── eval-catalog.md
├── fixtures/
│   ├── synthetic-standalone/
│   └── synthetic-multibrand/
└── runs/

experiments/setup-marketing-system/
└── [soltanto protocolli o note sanificate approvate]
```

Le fixture pubblicabili saranno interamente sintetiche ma coerenti e multi-documento. Dovranno includere almeno business identity approvata, materiali marketing realisti, un claim con base insufficiente o conflittuale, regole di canale, standard qualitativi e una policy di approvazione. La fixture multi-brand aggiungerà identità figlia, base aziendale e differenze sufficienti a verificare l'overlay senza duplicazione.

Il catalogo iniziale coprirà almeno: prerequisito presente, contesto mancante ma skill dipendente disponibile, dipendenza assente, prima proposta e massimo tre domande, cinque aree e vuoti, claim/evidence, separazione tra regole stabili e decisioni temporanee, due gate, composizione multi-brand, FYI runtime, aggiornamento mirato, fonti non affidabili e confini rispetto a strategia, campagne, strumenti e asset. Il forward test userà una richiesta nuova e un valutatore indipendente che riceve skill, profilo approvato e materiali minimi, ma non la risposta attesa o le conclusioni della discovery.

Durante gli eval non si scrive nei percorsi canonici e non si modificano instruction file. Le prove di gate restano simulazioni osservabili o operano soltanto in un workspace isolato esplicitamente non canonico. Materiali reali di clienti, note interne, contatti, prezzi o altre informazioni sensibili restano fuori dal repository e dagli archivi pubblicabili; un eventuale risultato del pilota entra in `experiments/` solo dopo sanificazione e approvazione specifica.

##### Stato dell'authoring locale — 2026-08-25

Il blueprint è stato tradotto nella skill approvata `v0.2.1` sotto `skills/setup-marketing-system/`, con `SKILL.md`, metadati UI, tre reference e istruzioni di installazione. Non sono stati aggiunti script o asset: non esiste ancora una trasformazione deterministica ripetuta che ne giustifichi l'uso.

Gli eval locali includono un catalogo comportamentale, una fixture standalone sintetica, una fixture multi-brand sintetica e tre run indipendenti in sola lettura: dry onboarding Relaybird, forward test Relaybird e forward test Fieldnote/Copperline. Nei run osservati non sono emersi hard fail: il processo ha limitato i claim non supportati, escluso regole temporanee, mantenuto separata l'autorizzazione alla pubblicazione, composto correttamente parent e overlay e mostrato il FYI.

Il validatore strutturale di `skill-creator` ha dato esito positivo tramite un adattatore YAML temporaneo isolato, necessario perché i runtime Python disponibili non includono PyYAML. Anche `agents/openai.yaml`, i frontmatter delle fixture e `git diff --check` risultano validi. Nessun percorso canonico `.agents/`, instruction file, installazione, commit o pubblicazione è stato creato o modificato.

Le fixture sintetiche, i tre eval indipendenti registrati e i controlli di release rendono `setup-marketing-system` una skill approvata. La release v0.2.1 non amplia i suoi confini: non definisce strategie temporanee, non esegue campagne e non autorizza azioni esterne.

### 3. Strategy Core

- `define-marketing-challenge`: trasforma un obiettivo, problema, opportunità, segnale o proposta tattica in una sfida di marketing confermata, distinguendo fatti, segnali, inferenze e assunzioni senza scegliere una soluzione;
- `choose-marketing-direction`: confronta direzioni plausibili rispetto a una sfida confermata, rende visibile l'assunzione più fragile e il primo test utile; il responsabile approva e registra la scelta;
- `define-marketing-mix`: traduce la direzione approvata in scelte coerenti su Product, Price, Place e Promotion, distinguendo vincoli, proposte, ipotesi, decisioni esterne e autorità prima dell'attivazione;
- `build-evidence-pack`, eventualmente futuro: prepara un dossier autonomo soltanto quando quantità, conflitti o riuso delle fonti lo rendono utile. Non appartiene al percorso essenziale e non blocca le tre skill dello Strategy Core.

#### `define-marketing-challenge`: user story e perimetro

> Come marketing manager o decisore aziendale, quando devo affrontare un obiettivo, un problema, un'opportunità o una proposta tattica che potrebbe richiedere il marketing, uso `define-marketing-challenge` per capire quale cambiamento bisogna realmente ottenere, per chi e entro quali confini. Ottengo un **Brief della sfida di marketing** confermato, che distingue fatti e assunzioni ed è pronto per valutare possibili direzioni senza anticipare la campagna.

La skill serve al proprietario della decisione: un responsabile aziendale, un professionista che lavora sul proprio marketing oppure un consulente o un'agenzia che facilita il lavoro insieme a un referente del cliente autorizzato a confermare la sfida. Non serve invece a interpretare unilateralmente il brief ricevuto da un cliente. Quel lavoro richiede un workflow separato, provvisoriamente chiamato `review-client-marketing-brief`, che mantenga distinti mandato del cliente, interpretazioni dell'agenzia, perimetro contrattuale e domande da sottoporre al cliente.

La skill interviene soltanto quando esiste un'ambiguità strategica reale. Non è un passaggio obbligatorio se obiettivo, pubblico, cambiamento cercato e direzione sono già sufficientemente chiari. Può concludere che serve prima una decisione aziendale, che il problema non è principalmente di marketing oppure che non ci sono elementi sufficienti per confermare il brief.

#### Esperienza conversazionale

La chat è l'interfaccia autorevole. Il workflow segue cinque momenti, non cinque schermate o domande fisse:

1. **Attivazione selettiva.** Identifica l'entità, legge Business Identity e Marketing Foundations pertinenti, verifica eventuali brief esistenti e mostra il FYI con i contesti e le versioni realmente applicati. Se il contesto manca o presenta un conflitto materiale, sostituisce il FYI con un avviso concreto e mantiene il risultato come bozza prudente.
2. **Prima formulazione utile.** Il primo turno sostanziale presenta che cosa sembra essere in gioco, una sfida provvisoria, ciò che è supportato e ciò che è ancora assunto, più non oltre tre domande capaci di cambiare il brief. Non apre con un questionario, una spiegazione dell'architettura o un messaggio di solo avanzamento.
3. **Chiarimento mirato.** Mantiene privatamente un registro delle lacune e chiede soltanto ciò che serve a capire se il problema è di marketing, quale risultato e cambiamento sono cercati, quale pubblico è coinvolto o ancora da scegliere, quali vincoli sono reali e chi può confermare il brief. Uno stato esplicito di non conoscenza è una risposta valida.
4. **Revisione e conferma.** Mostra la formulazione completa, base conoscitiva, assunzioni, conflitti, aspetti aperti, decisione preparata e artefatto proposto. Se restano punti non bloccanti, permette sia di confermare mantenendoli aperti sia di approfondirli. Scrive soltanto dopo una conferma esplicita che comprenda l'autorizzazione al salvataggio.
5. **Chiusura e handoff.** Riporta cosa è stato confermato e salvato, chiarisce che nessuna direzione è stata ancora scelta e può proporre `choose-marketing-direction` senza avviarla automaticamente.

La prima risposta utile usa normalmente quattro gruppi manageriali compatti: cosa sembra essere in gioco, sfida provvisoria, cosa sappiamo e cosa stiamo supponendo, cosa serve per confermarla. Il limite iniziale da validare negli eval è 450 parole, comprese domande e chiave delle fonti. Il limite è un tetto, non un obiettivo, e non giustifica l'eliminazione di vincoli critici.

#### Brief della sfida di marketing

Il brief è pronto quando un secondo agente può confrontare direzioni plausibili senza reinterpretare il problema, inventare pubblico, risultato o vincoli, trattare una tattica proposta come decisione oppure confondere fatti e assunzioni. Contiene soltanto ciò che serve per preparare la scelta:

1. sintesi della sfida, rilevanza attuale, decisione da preparare e responsabile;
2. situazione di partenza, risultato aziendale interessato, segnali ed eventuale tattica già proposta;
3. pubblico coinvolto o scelta di pubblico ancora aperta, situazione, comportamento o condizione attuale e cambiamento cercato;
4. perimetro, esclusioni, risorse, vincoli e limiti di autorità;
5. fatti, segnali, inferenze e assunzioni con base e conseguenza;
6. conflitti e aspetti aperti che possono cambiare formulazione, alternative, autorità o fattibilità;
7. stato di preparazione e decisione da passare a `choose-marketing-direction`.

Il budget entra soltanto come vincolo o questione aperta capace di cambiare il perimetro o la fattibilità: limite già approvato, ordine di grandezza, assenza di nuova spesa, autorità necessaria, tempo del team o altre capacità disponibili. La skill non crea un budget, non alloca risorse tra canali e non chiede dettagli finanziari sensibili non necessari. L'assenza di una cifra non blocca il brief se le direzioni possono comunque essere confrontate; diventa bloccante solo quando senza almeno un limite o un ordine di grandezza il confronto sarebbe puramente teorico o non autorizzato.

Il brief non contiene direzione scelta, piano di test, messaggi, canali, asset, media plan o piano di misurazione. Un target numerico è conservato solo quando esiste una base o una decisione autorizzata; non viene inventato per simulare precisione.

#### Artefatto e stato

Ogni decisione usa un fascicolo dedicato:

```text
.agents/marketing/decisions/<decision-slug>/
├── challenge.md
├── direction.md        # creato successivamente
└── marketing-mix.md    # creato dopo l'approvazione della direzione
```

`challenge.md` referenzia percorso e versione di Business Identity, Marketing Foundations ed eventuale contesto del brand senza duplicarli. Usa i marcatori `[C]`, `[S#]`, `[I]` e `[?]`; il tipo dell'elemento resta distinto dalla sua provenienza, quindi un'assunzione può essere confermata come assunzione senza diventare un fatto.

Gli stati del Brief della sfida sono `bozza`, `confermato` e `superato`. Una modifica sostanziale della stessa sfida incrementa la versione intera; una sfida diversa crea un nuovo fascicolo; una formulazione sostituita indica il riferimento successivo. La creazione di `direction.md` o `marketing-mix.md` non rende superati gli artefatti a monte che li sostengono.

Il Brief della sfida può essere confermato quando i contesti richiesti sono utilizzabili, risultato e cambiamento cercato sono comprensibili, il pubblico è identificato o la sua scelta è dichiaratamente parte della decisione, tattiche e vincoli sono classificati correttamente, fatti e assunzioni restano distinguibili, il responsabile è noto, non esistono conflitti bloccanti ed è chiaro quale scelta dovrà affrontare il workflow successivo.

Il fascicolo non viene installato in `AGENTS.md`, `CLAUDE.md` o istruzioni equivalenti: è un artefatto riferito a una decisione, da caricare quando si lavora su quella decisione, non un contesto globale da applicare a ogni attività.

##### Stato della release: 2026-08-26

Il blueprint è stato pubblicato come release stabile `v0.1.1` sotto `skills/define-marketing-challenge/`, con `SKILL.md`, metadati UI, template del Brief della sfida, routing delle domande e istruzioni di installazione. Non sono stati aggiunti script o asset perché la prima versione non richiede trasformazioni deterministiche né una superficie visuale. Il primo forward test indipendente non ha rilevato hard fail; la patch chiarisce provenienza, dati aggregati, fallback per brief cliente e conferma senza salvataggio.

Il catalogo iniziale comprende 18 eval comportamentali, una fixture Relaybird a due turni, un forward test nuovo e una regressione per i brief cliente ricevuti dalle agenzie. Il self-check locale dell'autore ha prodotto una prima risposta di 322 parole, quattro gruppi e tre domande, superando il controllo meccanico di compattezza senza scritture canoniche. Questo controllo non è indipendente perché l'autore conosceva le aspettative della fixture.

La validazione strutturale di `skill-creator`, `git diff --check` e il retest indipendente della `v0.1.1` hanno esito positivo. La release contiene lo ZIP della sola skill e il relativo checksum SHA-256.

#### `choose-marketing-direction`: approvata v0.2.0

> Come proprietario di una decisione marketing, parto da una sfida confermata, formulo una diagnosi provvisoria e confronto alternative realmente strategiche per scegliere come produrre il cambiamento cercato. Ottengo una direzione approvabile sottoposta a stress test, con trade-off, non-scelte, assunzione più fragile e primo test utile, senza trasformarla prematuramente in marketing mix o campagna.

La skill ricostruisce prima una diagnosi strategica proporzionata: tensione centrale, ipotesi causale, evidenze e incognite sui pubblici, alternative o sostituti, capacità dell'organizzazione e incertezza decisiva. La diagnosi resta provvisoria, può mantenere aperte letture concorrenti e può concludere che il problema non sia principalmente di marketing. La skill non avvia automaticamente ricerca di mercato o competitive intelligence.

Deriva quindi i criteri dal brief e presenta presto da due a quattro alternative reali, o un numero inferiore quando non esistono altre strade responsabili. Una direzione deve differire per pubblico o situazione, ostacolo, leva, meccanismo, posizione oppure sequenza di apprendimento. Webinar, newsletter, advertising, eventi e formati non diventano automaticamente direzioni diverse.

Il confronto resta qualitativo e motivato. La skill agisce anche come challenger: seleziona il miglior argomento contrario, verifica condizioni necessarie, capacità, risposte plausibili degli attori e conseguenze indesiderate, e rende esplicito che cosa la scelta implica non fare. Punteggi, pesi, ROI e stime entrano soltanto quando esiste un modello autorizzato e una base adeguata. L'esito può essere una raccomandazione, una raccomandazione condizionata, una richiesta di apprendere prima oppure la conclusione che nessuna opzione sia pronta.

La direzione rende visibili conseguenze e dipendenze su Product, Price, Place e Promotion, ma non definisce il mix. Non fissa roadmap, caratteristiche tecniche, prezzi, distribuzione, media mix, messaggi, asset o budget. Il primo test riduce l'incertezza strategica più importante e include una regola per confermare, correggere, fermare oppure riaprire la diagnosi; la skill non lo esegue né modifica automaticamente gli artefatti approvati.

L'artefatto proposto è:

```text
.agents/marketing/decisions/<decision-slug>/direction.md
```

Usa gli stati `bozza`, `approvata` e `superata`, referenzia la versione esatta di `challenge.md` e richiede sia approvazione della scelta sia autorizzazione al salvataggio. Il [forward test indipendente](evals/choose-marketing-direction/runs/2026-08-26-independent-forward-v0.2.0.md) della v0.2.0 è passato senza hard fail. La [release stabile v0.2.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/choose-marketing-direction-v0.2.0) contiene lo ZIP della sola skill e il relativo checksum. Il passaggio successivo normale è `define-marketing-mix`.

#### `define-marketing-mix`: approvata v0.1.1

> Come responsabile marketing, traduco una direzione approvata in decisioni coerenti su Product, Price, Place e Promotion, rendendo visibili vincoli, ipotesi, dipendenze e proprietari prima di progettare la campagna o altre attivazioni.

La skill impedisce che il percorso salti dalla strategia direttamente alla Promotion. Per ogni P usa uno stato operativo: `vincolo approvato`, `scelta da definire`, `proposta`, `ipotesi da verificare`, `decisione esterna` oppure `non applicabile`. Tutte le P devono avere uno stato, ma non devono ricevere lo stesso livello di dettaglio né cambiare in ogni decisione.

- **Product** riguarda configurazione dell'offerta, packaging, esperienza e servizio pertinenti al marketing; roadmap tecnica, sviluppo, fattibilità e requisiti regolamentati restano delle funzioni competenti.
- **Price** riguarda logica di valore, architettura e condizioni; nessun prezzo viene fissato senza economics, evidenze e autorità adeguate.
- **Place** riguarda accesso, vendita, distribuzione ed erogazione; non coincide con i canali di comunicazione.
- **Promotion** riguarda ruolo strategico della comunicazione, territorio di valore e sequenza generale; messaggi, calendario, media plan e asset restano nel Campaign Core.

Il mix controlla la coerenza tra le P e registra come decisioni esterne le dipendenze che superano l'autorità marketing. Non modifica prodotto, listini, accordi, account o campagne.

L'artefatto proposto è:

```text
.agents/marketing/decisions/<decision-slug>/marketing-mix.md
```

Usa gli stati `bozza`, `approvato` e `superato`, referenzia versioni esatte di sfida e direzione e richiede approvazione del contenuto più autorizzazione al salvataggio. Il [forward test indipendente](evals/define-marketing-mix/runs/2026-08-26-independent-forward-v0.1.1.md) della v0.1.1 è passato senza hard fail. La [release stabile v0.1.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/define-marketing-mix-v0.1.1) contiene lo ZIP della sola skill e il relativo checksum. La componente Promotion può essere passata a `to-campaign-spec` soltanto quando dipendenze e autorità non rendono l'attivazione prematura.

Le due release includono `SKILL.md`, metadati UI, istruzioni di installazione, reference, cataloghi comportamentali e pacchetti verificabili. La validazione strutturale e i forward test non equivalgono a una prova con marketer reali né autorizzano l'esecuzione delle attività descritte dalle skill.

### 4. Campaign Core

- `to-campaign-spec`: traduce la componente Promotion e le attivazioni pertinenti di un marketing mix approvato in messaggi, ruolo dei canali, asset, dipendenze, responsabilità, approvazioni e piano di misurazione;
- `campaign-review`: verifica separatamente coerenza strategica, solidità delle affermazioni e qualità degli asset;
- `learn-from-results`: confronta previsioni e risultati, separa segnale e rumore e aggiorna il playbook.

### 5. Content Core

- `content-director`: valuta se il materiale merita un contenuto, quale obiettivo può servire e quale formato lo valorizza;
- builder specializzati: producono l'asset e mantengono selezione, fedeltà, struttura, resa e QA specifici;
- `editorial-review`, eventualmente futura: serve per contenuti creati altrove o audit multi-asset, non come passaggio obbligatorio dopo ogni builder.

### Ordine di costruzione

1. `setup-business-context` — fondazione riusabile consolidata;
2. progettare e testare `setup-marketing-system` come onboarding delle Marketing Foundations;
3. validare lo Strategy Core con `define-marketing-challenge` + `choose-marketing-direction` + `define-marketing-mix`;
4. verificare `Augmented Marketing Assistant` in sessioni pulite, distinguendo selezione diretta della skill, handoff riuscito e fallback quando l'handoff non è disponibile;
5. svolgere un micro-pilot con persone poco tecniche prima di aggiungere un altro agente generalista;
6. collegare il primo percorso Content ai builder già esistenti;
7. introdurre il Campaign Core quando esistono marketing mix approvati da tradurre in attivazioni;
8. aggiungere apprendimento continuo e monitoring solo nei processi che mostrano un uso ripetuto.

## Content Director: responsabilità e confini

**Content Director** è il nome preferibile rispetto a Content Router: comunica giudizio editoriale, non semplice instradamento tecnico.

Riceve URL, articolo, documento, appunti, trascrizione, ricerca o idea incompleta. Legge il business context e il profilo operativo o overlay di brand pertinente, quando disponibili, e valuta:

1. valore editoriale;
2. struttura dell’idea;
3. solidità delle prove;
4. obiettivo;
5. formato più adatto.

Deve raccomandare un formato principale e, solo quando esiste una vera alternativa, una seconda opzione. Deve poter concludere che il materiale non è ancora sufficiente per produrre un contenuto.

Produce un brief, non le slide né la card:

```markdown
Formato: carosello
Obiettivo: spiegare un meccanismo controintuitivo
Pubblico: ...
Idea centrale: ...
Fonte primaria: ...
Affermazioni da verificare: ...
Sequenza: ...
CTA: ...
```

Non decide numero preciso delle slide, formulazione finale, a capo, composizione, leggibilità o applicazione grafica.

## Confine con Carousel Builder e Quote Card Builder

Il giudizio editoriale specifico non va spostato in una terza review obbligatoria. I builder possiedono il contesto necessario e intervengono nel punto giusto.

| Componente | Responsabilità |
|---|---|
| Setup Business Context | Identità generale e verificabile dell'azienda o del brand, fonti, limiti e contesto persistente |
| Setup Marketing System | Profilo operativo aziendale e overlay di brand riusabili da strategia, campagne e contenuti |
| Content Director | Se l’idea merita un contenuto e quale formato la valorizza |
| Carousel Builder | Selezione, fedeltà, struttura, slide, grafica, leggibilità e QA del carosello |
| Quote Card Builder | Selezione della frase, attribuzione, adattamento, gerarchia e QA della card |
| Editorial Review futura | Audit di contenuti creati altrove o di campagne multi-asset |

Una skill Editorial Review autonoma, se introdotta, dovrebbe servire soprattutto a revisionare contenuti esterni, confrontare più asset o fare audit; non deve diventare un passaggio standard dopo ogni builder.

I criteri comuni — fedeltà alle fonti, distinzione tra citazione e parafrasi, forza delle affermazioni, coerenza con pubblico e obiettivo, attribuzioni e CTA — possono vivere in un documento o modulo condiviso (`editorial-standards.md`). Ogni builder aggiunge poi i propri controlli.

Per aumentare l’indipendenza del controllo, il builder può eseguire internamente un revisore isolato che riceve fonte, contesto applicabile, testi approvati e output, e restituisce solo i problemi. Per l’utente resta un unico flusso.

## Posizionamento e differenziazione

Da evitare:

- catalogo organizzato per canale;
- molti generatori di copy, post, email e landing page;
- nome o promessa troppo simili a raccolte già note;
- “il tuo CMO artificiale”.

La differenziazione è il giudizio: decidere cosa non fare, quali prove mancano, quale assunzione è fragile e quale passaggio richiede approvazione.

Le skill già esistenti diventano moduli esecutivi del framework, non vengono sostituite.

## Primo test consigliato

Prima di costruire il repository completo, eseguire un pilota italiano su attività reali con una piccola coorte di ex corsisti, clienti o manager. Il primo percorso da osservare è:

- `setup-business-context`;
- `setup-marketing-system`;
- `define-marketing-challenge`;
- `choose-marketing-direction`;
- `define-marketing-mix`.

I segnali utili non sono il numero di output prodotti, ma comportamenti osservabili:

- il setup viene completato senza che un facilitatore debba spiegare l'architettura interna;
- il contesto viene riusato correttamente in un secondo lavoro;
- il processo cambia, restringe o interrompe almeno una decisione reale;
- emergono assunzioni, conflitti o prove mancanti che l'uso abituale del chatbot non aveva reso visibili;
- l'utente distingue chiaramente fatti aziendali, direzione strategica, marketing mix e decisioni di campagna.

Per `setup-marketing-system`, il criterio di successo combina eval realistici e un forward test indipendente:

- dai materiali forniti, il primo turno sostanziale produce una proposta utile oppure un blocker concreto e pone non più di tre domande decisive;
- tutte le cinque aree vengono coperte da regole supportate oppure da una classificazione corretta dei vuoti;
- durante gli eval non vengono scritti artefatti canonici né modificati instruction file; eventuali output osservabili restano in un ambiente isolato;
- in un secondo task indipendente, l'agente legge il profilo senza chiedere di ripeterlo, mostra il FYI e applica concretamente almeno una regola alla decisione o all'output;
- quando profilo, riscontri o autorizzazioni non sono sufficienti, il processo restringe, sospende o mantiene in bozza il lavoro invece di inventare il dato mancante;
- nello scenario multi-brand vengono caricati soltanto identità, base e overlay pertinenti, rispettando versioni e conflitti;
- il risultato non dichiara di aver definito una strategia, completato una campagna, configurato strumenti o prodotto asset.

Sono hard fail almeno: una scrittura canonica durante il test, una falsa dichiarazione di caricamento nel FYI, l'uso di un overlay non pertinente, un'inferenza trattata come regola approvata, il superamento silenzioso di un conflitto bloccante o un'azione esterna senza l'approvazione richiesta.

Non fissare soglie numeriche prima di avere una baseline. Dopo il pilota, definire criteri quantitativi in base agli abbandoni, ai riusi e agli errori realmente osservati; solo allora valutare adattamenti ad altre lingue, distribuzione pubblica e cataloghi esterni.

## Decisioni da non perdere

- Il perimetro minimo comprende agenti che possono installare e caricare skill; i chatbot privi di skill non sono un target. Filesystem, connector, subagenti, viste visuali e automazioni sono capability da osservare, non da presumere.
- Le skill mantengono il risultato essenziale anche senza scrittura nel workspace: restituiscono l'artefatto completo e il percorso previsto senza dichiarare che il file esista. Nessun connector è obbligatorio per Fondazione e Strategy Core.
- Comandi, hook, manifest e marketplace sono adattatori di ambiente e non devono cambiare artefatti, provenienza, gate o confini di autorità.
- **Augmented Marketing Assistant** è l'ingresso conversazionale per richieste ambigue o utenti che non sanno da dove iniziare: orienta e attiva le skill quando l'ambiente lo consente, altrimenti indica quale invocare e si ferma senza duplicarne il metodo.
- **Setup Business Context** è la base persistente per azienda o brand e registra l'identità esistente senza crearne la strategia.
- Il supporto visuale delle skill di setup è un miglioramento opzionale e capability-gated: può offrire una vista singola di revisione, ma chat, stato confermato, approvazioni e scritture canoniche restano autorevoli. Se la capability manca o fallisce, il percorso continua senza perdita di informazioni; un wizard persistente e deterministico richiederebbe un'app o uno strumento dedicato.
- Un dato assente dalle fonti non è automaticamente inesistente; i vuoti vengono classificati e quelli non bloccanti restano espliciti nell'identità.
- Le domande non formano un questionario fisso: un router seleziona fino a tre lacune ad alto impatto, usando lenti da marketer e business strategist ma senza creare nuove scelte strategiche.
- L'installazione negli instruction file degli agenti è separata dall'approvazione del contenuto e richiede un consenso esplicito dopo la spiegazione della modifica.
- **Setup Marketing System** è l'ingresso specifico alla costruzione delle Marketing Foundations e parte dal lavoro reale dell'organizzazione, non dalla scelta di un file interno.
- Quando una regola operativa di marketing essenziale manca, **Setup Marketing System** può aiutare il responsabile a formularla; la proposta non diventa una regola aziendale finché non viene approvata esplicitamente.
- La prima versione di **Setup Marketing System** raccoglie soltanto regole stabili. Priorità di periodo, campagne, budget e KPI temporanei restano fuori dall'onboarding per mantenerlo breve.
- Il nucleo minimo comprende cinque aree: relazione tra offerte, pubblici e situazioni d'uso; messaggi, claim e prove; ruolo di canali e formati; standard editoriali, visivi e qualitativi; controlli e approvazioni. Sono risultati da ottenere, non sezioni di un questionario obbligatorio.
- L'aha moment dell'onboarding è la prima proposta utile di regole ricavata dal contesto e dai materiali, non il completamento del setup. Il percorso è chat-first, non ripete informazioni disponibili, pone al massimo tre domande essenziali e offre una revisione diretta a chi possiede già un playbook.
- L'utente di riferimento è un responsabile interno competente sul business e sul marketing, ma non necessariamente su skill e agenti AI. L'esperienza usa linguaggio manageriale e nasconde l'architettura tecnica finché una scelta operativa non richiede di spiegarla.
- La user story primaria è: il direttore marketing crea e approva una volta il profilo marketing stabile, poi l'agente lo legge e lo applica a ogni attività di marketing specifica dell'organizzazione. Il profilo persistente è un prerequisito verificabile, non memoria implicita della chat.
- Ogni risposta che svolge o fa avanzare un'attività marketing aziendale mostra un FYI compatto con entità e versioni del contesto realmente applicato. Se il profilo non è utilizzabile, il FYI viene sostituito da un avviso azionabile e non da una falsa dichiarazione di caricamento.
- Nel percorso di costruzione delle Marketing Foundations, `setup-marketing-system` resta l'unico ingresso percepito: se il business context manca, orchestra `setup-business-context` nello stesso dialogo e riusa materiali e risposte, senza duplicarne la logica né approvare Marketing Foundations prive di identità canonica.
- Se `setup-business-context` non è disponibile, la skill può suggerirne l'acquisizione soltanto da una fonte e versione verificabili. Download e installazione richiedono consensi distinti e una verifica intermedia del pacchetto; senza la dipendenza il risultato marketing resta una bozza non canonica.
- La prima versione produce un unico artefatto canonico nella lingua di lavoro del responsabile, chiamato **Fondamenti di marketing** in italiano. Non separa profilo strategico e operativo; le strategie temporanee restano artefatti dei workflow a valle.
- **Marketing Foundations** è organizzato in tre livelli: riferimenti al contesto, regole stabili e governance. Referenzia la business identity senza duplicarla e mantiene visibili provenienza, conflitti e aggiornamenti.
- L'artefatto è Markdown nella lingua di lavoro del responsabile, con frontmatter minimo e corpo leggibile. L'onboarding lo presenta in linguaggio manageriale senza usare YAML o JSON come stato visibile; lo schema completo vive in una reference dedicata, non nel corpo principale della skill.
- Le Marketing Foundations adottano un modello rule-first: ogni regola rende chiari comportamento, scope e base, aggiungendo eccezioni, approvazioni o fallback solo quando servono. Non impongono una scheda rigida e non trasformano descrizioni narrative in direttive implicite.
- **Coerenza tra offerta, pubblico e situazione** collega per regola offerte e pubblici già canonici alle situazioni in cui il marketing può considerarli pertinenti, includendo fit, esclusioni e comportamento prudente senza introdurre segmentazioni o priorità di campagna.
- **Messaggi, claim ed evidenze** definisce messaggi consentiti e uso dei riscontri esistenti senza chiedere di produrne di nuovi durante l'onboarding. Un claim non adeguatamente sostenuto viene limitato, riformulato per approvazione o bloccato.
- **Ruolo di canali e formati** registra il ruolo stabile, l'idoneità e i limiti di canali e formati ricavati dal lavoro reale, senza introdurre calendario, budget, media plan o configurazione degli account.
- **Standard editoriali, visivi e di qualità** contiene le regole minime applicabili dagli agenti e referenzia linee guida, template e asset autorevoli senza duplicarli o generarli. La prima versione non crea automaticamente un secondo profilo editoriale o visuale.
- **Controlli, autorità e approvazioni** distingue attività autonome, proposte e vietate, identifica i controlli necessari e separa l'approvazione del contenuto dall'autorizzazione a eseguire. In assenza di una regola essenziale, l'agente resta in modalità bozza o raccomandazione.
- La governance riusa i marcatori `[C]`, `[S#]`, `[I]` e `[?]` del business context. Nessuna inferenza può agire come regola in un profilo approvato; fonti, conflitti, incognite, trigger di revisione, versione intera e changelog restano espliciti.
- Il successo di `setup-marketing-system` richiede eval realistici senza scritture canoniche e un forward test indipendente che dimostri riuso, FYI, applicazione concreta delle regole, corretta composizione multi-brand e hard fail sui confini essenziali.
- I percorsi canonici sono `.agents/marketing/foundations.md` per la base e `.agents/marketing/brands/<brand-slug>.md` per gli overlay. Un overlay contiene soltanto differenze esplicite, registra la versione della base verificata e non prevale silenziosamente in caso di conflitto.
- Approvazione e installazione sono due gate distinti: prima si approva il contenuto e si autorizza la scrittura canonica; solo dopo un secondo consenso può modificare le istruzioni dell'agente per caricare automaticamente identità, foundations e overlay pertinente.
- Le Marketing Foundations sono utilizzabili senza essere esaustive: tutte le cinque aree devono essere valutate, i vuoti non bloccanti devono avere stato e comportamento prudente espliciti, mentre conflitti bloccanti o controlli essenziali mancanti impediscono l'approvazione.
- L'onboarding non chiede all'utente di scegliere quale file creare: parte dal bisogno e propone l'artefatto pertinente. Un secondo file è giustificato solo da proprietari, frequenze di aggiornamento, permessi o utilizzatori differenti.
- Gli standard editoriali e visivi minimi vivono nelle Marketing Foundations; manuali, template e asset dettagliati restano riferimenti esterni. Non viene reintrodotto `content-profile-builder` come skill approvata.
- Strategy, Campaign e Content sono tre core distinti per decisione e artefatto, non tre agenti generalisti che duplicano il lavoro.
- `define-marketing-challenge` serve al proprietario della decisione e produce un Brief della sfida confermato prima di qualsiasi scelta di direzione. Un'agenzia che interpreta unilateralmente un brief ricevuto richiede un workflow separato.
- La prima risposta di `define-marketing-challenge` formula già una sfida provvisoria, distingue supporto e assunzioni e pone non più di tre domande ad alta conseguenza; non apre un workshop o un questionario generico.
- Budget, tempo e capacità entrano nel Brief della sfida solo come vincoli o questioni aperte necessari a rendere realistico il confronto. Allocazione e piano di spesa restano a valle.
- `challenge.md`, `direction.md` e `marketing-mix.md` vivono nello stesso fascicolo decisionale sotto `.agents/marketing/decisions/<decision-slug>/`; non vengono installati nelle istruzioni globali dell'agente.
- `choose-marketing-direction` distingue alternative strategiche da tattiche, rende falsificabile la raccomandazione e passa le implicazioni sulle quattro P senza definirle.
- `define-marketing-mix` impedisce che il sistema riduca il marketing alla Promotion: classifica e collega Product, Price, Place e Promotion rispettando autorità e dipendenze cross-funzionali.
- `build-evidence-pack` è una capacità opzionale futura, non un passaggio del percorso essenziale `define-marketing-challenge` + `choose-marketing-direction` + `define-marketing-mix`.
- **Content Director** è opzionale quando il formato è già deciso.
- Carousel Builder e Quote Card Builder mantengono il giudizio editoriale e il QA specifici del proprio output.
- Editorial Review non è un passaggio obbligatorio del sistema iniziale.
- `monitoring-setup` è un modulo di ascolto a monte, non un sostituto degli strumenti di monitoring e non un passaggio obbligatorio.
- Il framework deve ottimizzare decisioni e apprendimento, non il numero di asset prodotti.
