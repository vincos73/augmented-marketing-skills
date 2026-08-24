# Marketing Decision Skills

Documento fondativo del framework emerso dalla conversazione **“Analisi framework marketer”** (20 agosto 2026).

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
setup-business-context  (fondazione autonoma: fatti durevoli su azienda e brand)
        ↓ riferimento, non duplicazione
setup-marketing-system  (punto d'ingresso e profilo operativo)
        ├── Strategy Core  → challenge-brief → build-evidence-pack → choose-marketing-bet
        ├── Campaign Core  → to-campaign-spec → campaign-review → learn-from-results
        └── Content Core   → Content Director → builder specializzati
```

I tre core non sono cartelle decorative e non devono diventare tre agenti generalisti. Sono famiglie di decisioni con artefatti e confini diversi:

- **Strategy Core:** decide quale problema, pubblico, comportamento o opportunità meritano una scommessa e quale assunzione testare;
- **Campaign Core:** traduce una scommessa approvata in un sistema coordinato di messaggi, canali, asset, responsabilità, misure e apprendimento;
- **Content Core:** valuta e produce singoli contenuti o famiglie di contenuti, mantenendo il giudizio specifico nei builder.

`setup-marketing-system` è l'onboarding del framework, non un quarto core. Deve partire dal lavoro reale dell'organizzazione, verificare se esiste un business context utilizzabile e costruire un profilo operativo riusabile dai tre core. Per aziende multi-brand può mantenere un livello aziendale e overlay di brand, sempre referenziando le identità canoniche create da `setup-business-context` invece di copiarle.

Il **profilo editoriale e visivo** resta un artefatto utile, ma per il primo sistema non richiede una skill autonoma `content-profile-builder`: può essere una sezione o un overlay gestito da `setup-marketing-system`. Una skill separata sarà giustificata solo se l'uso reale dimostrerà che importazione, portabilità o manutenzione del profilo costituiscono un lavoro autonomo.

Un modulo opzionale di ascolto può alimentare il sistema prima di una decisione o in modo continuativo:

```text
monitoring-setup  (autonomo e opzionale)
        ↓
fonti, query, segnali e digest
        ↓
build-evidence-pack → Strategy Core / Campaign Core / Content Director
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

`monitoring-setup` non decide ancora quale contenuto produrre. Fornisce segnali e materiali a `build-evidence-pack`, a `Content Director` o direttamente a un sistema di briefing. Il Content Director continua a valutare rilevanza, solidità, obiettivo e formato; i builder producono l’asset.

Per questo è una skill **abilitante e opzionale**, non un passaggio obbligatorio di ogni campagna.

### Distribuzione

È adatta come asset gratuito per clienti, lead magnet e strumento di reputazione. Si può articolare in tre livelli:

1. **Starter:** Google Alerts, RSS e digest manuale;
2. **Pro:** changedetection.io, filtri, notifiche e fonti personalizzate;
3. **Advanced:** RSSHub, Huginn/n8n, sintesi AI e archivio storico.

La promessa concreta può essere:

> Costruisci il tuo radar informativo personalizzato e smetti di controllare manualmente decine di siti.

## Nucleo iniziale delle skill

### Fondazione consolidata e roadmap

Al momento il repository contiene una sola skill sorgente approvata:

- `setup-business-context`: identità aziendale o di brand persistente, verificabile e riusabile.

`setup-marketing-system`, i tre core e le relative competenze restano roadmap o ipotesi da validare, non contenuti già inclusi nel repository. Il set resta intenzionalmente incompleto: non produce campagne complete e non automatizza la pubblicazione.

Le cartelle sotto `skills/` sono sorgenti di authoring, non prova di installazione attiva. Per la scoperta locale in un repository Codex, una skill approvata dovrà essere collocata in `.agents/skills/`; per distribuirla in ChatGPT sul web, desktop e mobile dovrà essere confezionata come plugin. Authoring, installazione locale e distribuzione restano tre gate distinti.

### 1. Fondazione — `setup-business-context`

Costruisce e installa la carta d'identità persistente che gli agenti devono conoscere prima di lavorare per o su un'azienda o un brand. Parte soltanto dalle fonti fornite, allegate o citate dall'utente; prepara prima una bozza e pone poche domande sui vuoti realmente decisivi.

La skill distingue le informazioni confermate dal responsabile, documentate da una fonte, inferite dall'agente o ancora ignote. Mantiene visibili le contraddizioni e non trasforma un'inferenza in un fatto attraverso la riscrittura.

L'onboarding conserva quattro macro-fasi — entità e fonti, revisione della bozza, risoluzione dei vuoti decisivi, approvazioni — ma il numero di domande varia in base ai materiali. Nel primo ciclo la chat testuale è l'interfaccia primaria: dopo l'invio delle fonti, il turno successivo deve produrre direttamente una comprensione provvisoria utile o un blocker concreto, senza renderizzazioni o trasferimenti di stato intermedi.

La card interattiva resta un esperimento fuori dal pacchetto attivo. Non viene invocata automaticamente e potrà rientrare nel prodotto solo quando un componente persistente saprà mantenere lo stato senza essere ricostruito a ogni fase. Un'eventuale visualizzazione richiesta esplicitamente serve come vista singola di revisione; input essenziali e approvazioni restano in chat.

Un elemento non trovato nelle fonti non viene dichiarato inesistente. La skill distingue tra informazione disponibile, esistente ma non disponibile, non definita dall'organizzazione, ignota all'utente e non applicabile. I vuoti essenziali richiedono uno stato esplicito; quelli importanti ma non bloccanti, come una missione non documentata, restano visibili nell'identità senza essere inventati.

La selezione delle domande applica due lenti complementari — marketing e modello di business — senza trasformarsi in un workshop strategico. Dopo aver estratto ciò che le fonti già sostengono, l'agente privilegia al massimo tre vuoti per volta: perimetro e offerta corrente, sistema cliente/utente/pagatore/decisore, situazione che genera la domanda, alternative reali, capacità distintiva, valore, prova, fraintendimenti e vincoli. Obiettivi di crescita, nuovi segmenti, pricing, canali e posizionamento futuro restano fuori dal setup.

L'output canonico è separato dalla skill:

- `.agents/company-identity.md` per un'azienda;
- `.agents/brand-identity.md` per un brand autonomo;
- `.agents/brands/<brand>.md` per un brand appartenente a un'azienda.

Un contesto di brand figlio viene usato insieme all'identità dell'azienda, non al suo posto. I workflow a valle referenziano entità, percorso, versione e data di revisione invece di duplicare i fatti in nuovi profili. La freschezza viene verificata attraverso cambiamenti concreti — offerte, perimetro, relazioni di brand, prove o vincoli — non con una scadenza generica.

Il flusso ha due approvazioni distinte: la prima autorizza il salvataggio dell'identità; la seconda autorizza l'eventuale modifica spiegata e circoscritta di `AGENTS.md`, `CLAUDE.md` o di entrambi. La skill documenta l'identità esistente: non definisce la strategia, non produce campagne, non configura strumenti e non inventa un posizionamento o una brand identity mancanti.

### 2. Punto d'ingresso — `setup-marketing-system`

Aiuta un'organizzazione a predisporre il proprio modo di lavorare con gli agenti. Parte dai lavori di marketing reali, non da una scelta fra nomi interni di skill. Verifica il business context, individua le decisioni ricorrenti e crea un profilo operativo riusabile dai tre core.

Il profilo può includere scelte approvate su priorità, pubblici, messaggi, prove, canali, capacità, misurazione, ruoli, approvazioni e convenzioni editoriali o visive. Se esistono più brand, mantiene una base aziendale e overlay espliciti; non fonde automaticamente contesti diversi.

Questa skill orchestra il setup, ma non deve simulare di aver completato una strategia o una campagna. Il suo schema, i percorsi canonici e le approvazioni saranno definiti nel secondo incremento.

### 3. Strategy Core

- `challenge-brief`: chiarisce obiettivo, pubblico, comportamento atteso, vincoli, prove, rischi e decisore senza produrre una campagna;
- `build-evidence-pack`: separa dati, testimonianze, inferenze e assunzioni, rendendo visibili contraddizioni e lacune;
- `choose-marketing-bet`: confronta alternative, esplicita l'assunzione più fragile e propone il test meno costoso; l'utente approva e registra la scelta.

### 4. Campaign Core

- `to-campaign-spec`: traduce una scommessa approvata in messaggi, ruolo dei canali, asset, dipendenze, responsabilità, approvazioni e piano di misurazione;
- `campaign-review`: verifica separatamente coerenza strategica, solidità delle affermazioni e qualità degli asset;
- `learn-from-results`: confronta previsioni e risultati, separa segnale e rumore e aggiorna il playbook.

### 5. Content Core

- `content-director`: valuta se il materiale merita un contenuto, quale obiettivo può servire e quale formato lo valorizza;
- builder specializzati: producono l'asset e mantengono selezione, fedeltà, struttura, resa e QA specifici;
- `editorial-review`, eventualmente futura: serve per contenuti creati altrove o audit multi-asset, non come passaggio obbligatorio dopo ogni builder.

### Ordine di costruzione

1. `setup-business-context` — fondazione riusabile consolidata;
2. progettare e testare `setup-marketing-system` come punto d'ingresso;
3. validare lo Strategy Core iniziando dal percorso minimo `challenge-brief` + `choose-marketing-bet`;
4. collegare il primo percorso Content ai builder già esistenti;
5. introdurre il Campaign Core quando esistono decisioni strategiche reali da tradurre;
6. aggiungere apprendimento continuo e monitoring solo nei processi che mostrano un uso ripetuto.

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
- `challenge-brief`;
- `choose-marketing-bet`.

I segnali utili non sono il numero di output prodotti, ma comportamenti osservabili:

- il setup viene completato senza che un facilitatore debba spiegare l'architettura interna;
- il contesto viene riusato correttamente in un secondo lavoro;
- il processo cambia, restringe o interrompe almeno una decisione reale;
- emergono assunzioni, conflitti o prove mancanti che l'uso abituale del chatbot non aveva reso visibili;
- l'utente distingue chiaramente fatti aziendali, scelte di marketing e decisioni di campagna.

Non fissare soglie numeriche prima di avere una baseline. Dopo il pilota, definire criteri quantitativi in base agli abbandoni, ai riusi e agli errori realmente osservati; solo allora valutare versione inglese, distribuzione pubblica e cataloghi esterni.

## Decisioni da non perdere

- **Setup Business Context** è la base persistente per azienda o brand e registra l'identità esistente senza crearne la strategia.
- La card interattiva è un miglioramento opzionale: l'onboarding deve restare completabile integralmente in chat testuale con lo stesso risultato.
- Un dato assente dalle fonti non è automaticamente inesistente; i vuoti vengono classificati e quelli non bloccanti restano espliciti nell'identità.
- Le domande non formano un questionario fisso: un router seleziona fino a tre lacune ad alto impatto, usando lenti da marketer e business strategist ma senza creare nuove scelte strategiche.
- L'installazione negli instruction file degli agenti è separata dall'approvazione del contenuto e richiede un consenso esplicito dopo la spiegazione della modifica.
- **Setup Marketing System** è il punto d'ingresso del framework e parte dal lavoro reale dell'organizzazione, non dalla scelta di una skill interna.
- Il profilo editoriale e visivo resta separato e versionato, ma nel primo sistema è un artefatto o overlay gestito dal setup, non una skill core autonoma.
- Strategy, Campaign e Content sono tre core distinti per decisione e artefatto, non tre agenti generalisti che duplicano il lavoro.
- **Content Director** è opzionale quando il formato è già deciso.
- Carousel Builder e Quote Card Builder mantengono il giudizio editoriale e il QA specifici del proprio output.
- Editorial Review non è un passaggio obbligatorio del sistema iniziale.
- `monitoring-setup` è un modulo di ascolto a monte, non un sostituto degli strumenti di monitoring e non un passaggio obbligatorio.
- Il framework deve ottimizzare decisioni e apprendimento, non il numero di asset prodotti.
