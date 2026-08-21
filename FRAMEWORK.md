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
setup-business-context
        ↓
Content Profile Builder ───────────────┐
        ↓                              │
challenge-brief → evidence-pack       │
        ↓                              │
choose-marketing-bet                  │
        ↓                              │
to-campaign-spec                      │
        ↓                              │
Carousel Builder / Quote Card Builder / altri builder
        ↓
campaign-review → learn-from-results → playbook aggiornato
```

Un modulo opzionale di ascolto può alimentare il sistema prima del setup o in modo continuativo:

```text
monitoring-setup / web-radar-setup
        ↓
fonti, query, segnali e digest
        ↓
evidence-pack → Content Director → builder
```

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

### Primo incremento e roadmap

Al momento il repository contiene quattro skill sorgente:

- `setup-business-context`: identità aziendale o di brand persistente e verificabile;
- `content-profile-builder`: profili editoriali e visivi riutilizzabili e versionati;
- `build-evidence-pack`: fonti, inferenze, assunzioni e verifiche aperte;
- `content-director`: giudizio editoriale e brief verso i builder.

Le altre competenze mostrate nell'architettura — `challenge-brief`, `choose-marketing-bet`, `to-campaign-spec`, `campaign-review` e `learn-from-results` — sono roadmap, non contenuti già inclusi nel repository. Questa distinzione evita di promettere funzionalità non ancora disponibili.

Il set resta intenzionalmente incompleto: non produce campagne complete e non automatizza la pubblicazione. I moduli successivi saranno aggiunti dopo un primo uso reale e una revisione del nucleo iniziale.

Le cartelle sotto `skills/` sono sorgenti di authoring, non prova di installazione attiva. Per la scoperta locale in un repository Codex, una skill approvata dovrà essere collocata in `.agents/skills/`; per distribuirla in ChatGPT sul web, desktop e mobile dovrà essere confezionata come plugin. Authoring, installazione locale e distribuzione restano tre gate distinti.

### 1. `setup-business-context`

Costruisce e installa la carta d'identità persistente che gli agenti devono conoscere prima di lavorare per o su un'azienda o un brand. Parte soltanto dalle fonti fornite, allegate o citate dall'utente; prepara prima una bozza e pone poche domande sui vuoti realmente decisivi.

La skill distingue le informazioni confermate dal responsabile, documentate da una fonte, inferite dall'agente o ancora ignote. Mantiene visibili le contraddizioni e non trasforma un'inferenza in un fatto attraverso la riscrittura.

L'onboarding conserva quattro macro-fasi — entità e fonti, revisione della bozza, risoluzione dei vuoti decisivi, approvazioni — ma il numero di domande varia in base ai materiali. Una card interattiva può ridurre l'attrito quando l'ambiente la supporta; resta un miglioramento progressivo. Il flusso completo deve funzionare anche in chat testuale, con le stesse scelte, regole e approvazioni, senza perdere informazioni o ricominciare.

Quando la card può essere stilizzata direttamente, usa una firma cromatica Vincos leggera: tipografia nativa dell'ambiente, navy `#072743` per azioni e avanzamento, panna `#FEFDFB` come base chiara, grigio `#323232` per il testo e azzurro `#E3F4FF` soltanto come superficie di selezione accompagnata da testo o contorno navy. Non aggiunge logo, Barlow o motivi decorativi e non trasferisce questa veste nei file identità, che restano neutrali rispetto all'azienda o al brand descritto.

Un elemento non trovato nelle fonti non viene dichiarato inesistente. La skill distingue tra informazione disponibile, esistente ma non disponibile, non definita dall'organizzazione, ignota all'utente e non applicabile. I vuoti essenziali richiedono uno stato esplicito; quelli importanti ma non bloccanti, come una missione non documentata, restano visibili nell'identità senza essere inventati.

La selezione delle domande applica due lenti complementari — marketing e modello di business — senza trasformarsi in un workshop strategico. Dopo aver estratto ciò che le fonti già sostengono, l'agente privilegia al massimo tre vuoti per volta: perimetro e offerta corrente, sistema cliente/utente/pagatore/decisore, situazione che genera la domanda, alternative reali, capacità distintiva, valore, prova, fraintendimenti e vincoli. Obiettivi di crescita, nuovi segmenti, pricing, canali e posizionamento futuro restano fuori dal setup.

L'output canonico è separato dalla skill:

- `.agents/company-identity.md` per un'azienda;
- `.agents/brand-identity.md` per un brand autonomo;
- `.agents/brands/<brand>.md` per un brand appartenente a un'azienda.

Il flusso ha due approvazioni distinte: la prima autorizza il salvataggio dell'identità; la seconda autorizza l'eventuale modifica spiegata e circoscritta di `AGENTS.md`, `CLAUDE.md` o di entrambi. La skill documenta l'identità esistente: non definisce la strategia, non produce campagne, non configura strumenti e non inventa un posizionamento o una brand identity mancanti.

### 2. Roadmap — `content-profile-builder`

Costruisce, aggiorna, seleziona, importa ed esporta profili editoriali e visivi riutilizzabili.

Il profilo è un documento separato dalla skill: la skill è il metodo, il profilo è il contesto dell’utente. Non va incorporato stabilmente nel codice della skill.

Un profilo può contenere:

- pubblico e obiettivi;
- posizionamento e temi principali;
- voce, tono e formule da evitare;
- criteri editoriali e regole sulle fonti;
- palette, font, logo e indicazioni visive;
- CTA, vincoli e requisiti di accessibilità.

Ogni modifica sostanziale crea una versione. Un asset può registrare nome, versione e digest del profilo usato.

I profili possono essere locali al progetto o portatili (`content-profile.md`, JSON o ZIP con asset). Non devono mai essere fusi automaticamente tra loro. Quando sono disponibili più profili, il sistema chiede quale applicare.

Regola progettuale:

> Il profilo viene incorporato nel flusso delle skill, non nel codice delle skill.

### 3. Roadmap — `challenge-brief`

Interroga obiettivo, pubblico, comportamento atteso, budget, prove, rischi e decisore. Non produce ancora la campagna.

### 4. Roadmap — `build-evidence-pack`

Distingue dati, testimonianze, inferenze e assunzioni; segnala contraddizioni e informazioni mancanti.

### 5. Roadmap — `choose-marketing-bet`

Confronta le alternative, esplicita l’assunzione più fragile e propone il test meno costoso. La scelta finale viene approvata e registrata dall’utente.

### 6. Roadmap — `to-campaign-spec`

Traduce la decisione in messaggi, ruolo dei canali, asset, dipendenze, responsabilità, approvazioni e piano di misurazione.

### 7. Roadmap — `campaign-review`

Esegue revisioni separate su:

- coerenza con la decisione;
- solidità delle affermazioni;
- qualità e correttezza degli asset.

### 8. Roadmap — `learn-from-results`

Confronta previsioni e risultati, separa segnale e rumore e aggiorna il playbook. È la componente che trasforma una raccolta di skill in un sistema che apprende.

## Content Director: responsabilità e confini

**Content Director** è il nome preferibile rispetto a Content Router: comunica giudizio editoriale, non semplice instradamento tecnico.

Riceve URL, articolo, documento, appunti, trascrizione, ricerca o idea incompleta. Legge il profilo disponibile e valuta:

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
| Content Profile Builder | Regole editoriali e visive riutilizzabili per la produzione di contenuti |
| Content Director | Se l’idea merita un contenuto e quale formato la valorizza |
| Carousel Builder | Selezione, fedeltà, struttura, slide, grafica, leggibilità e QA del carosello |
| Quote Card Builder | Selezione della frase, attribuzione, adattamento, gerarchia e QA della card |
| Editorial Review futura | Audit di contenuti creati altrove o di campagne multi-asset |

Una skill Editorial Review autonoma, se introdotta, dovrebbe servire soprattutto a revisionare contenuti esterni, confrontare più asset o fare audit; non deve diventare un passaggio standard dopo ogni builder.

I criteri comuni — fedeltà alle fonti, distinzione tra citazione e parafrasi, forza delle affermazioni, coerenza con pubblico e obiettivo, attribuzioni e CTA — possono vivere in un documento o modulo condiviso (`editorial-standards.md`). Ogni builder aggiunge poi i propri controlli.

Per aumentare l’indipendenza del controllo, il builder può eseguire internamente un revisore isolato che riceve fonte, profilo, testi approvati e output, e restituisce solo i problemi. Per l’utente resta un unico flusso.

## Posizionamento e differenziazione

Da evitare:

- catalogo organizzato per canale;
- molti generatori di copy, post, email e landing page;
- nome o promessa troppo simili a raccolte già note;
- “il tuo CMO artificiale”.

La differenziazione è il giudizio: decidere cosa non fare, quali prove mancano, quale assunzione è fragile e quale passaggio richiede approvazione.

Le skill già esistenti diventano moduli esecutivi del framework, non vengono sostituite.

## Primo test consigliato

Prima di costruire il repository completo, eseguire un pilota italiano con 8–10 ex corsisti su attività reali, usando:

- `setup-business-context`;
- `challenge-brief`;
- `choose-marketing-bet`;
- `campaign-review`.

Segnali di validazione:

- almeno 6 partecipanti completano il setup;
- almeno 4 riutilizzano spontaneamente una skill su un secondo lavoro;
- almeno 3 dichiarano che il processo ha modificato una decisione concreta;
- emergono errori o assunzioni che l’uso abituale di ChatGPT non aveva rilevato.

Solo dopo il pilota valutare versione inglese, distribuzione pubblica e cataloghi esterni.

## Decisioni da non perdere

- **Setup Business Context** è la base persistente per azienda o brand e registra l'identità esistente senza crearne la strategia.
- La card interattiva è un miglioramento opzionale: l'onboarding deve restare completabile integralmente in chat testuale con lo stesso risultato.
- Un dato assente dalle fonti non è automaticamente inesistente; i vuoti vengono classificati e quelli non bloccanti restano espliciti nell'identità.
- Le domande non formano un questionario fisso: un router seleziona fino a tre lacune ad alto impatto, usando lenti da marketer e business strategist ma senza creare nuove scelte strategiche.
- L'installazione negli instruction file degli agenti è separata dall'approvazione del contenuto e richiede un consenso esplicito dopo la spiegazione della modifica.
- Il nome funzionale della skill di profilo è **Content Profile Builder**.
- Il profilo resta separato e versionato; non viene scritto dentro la skill.
- **Content Director** è opzionale quando il formato è già deciso.
- Carousel Builder e Quote Card Builder mantengono il giudizio editoriale e il QA specifici del proprio output.
- Editorial Review non è un passaggio obbligatorio del sistema iniziale.
- `monitoring-setup` è un modulo di ascolto a monte, non un sostituto degli strumenti di monitoring e non un passaggio obbligatorio.
- Il framework deve ottimizzare decisioni e apprendimento, non il numero di asset prodotti.
