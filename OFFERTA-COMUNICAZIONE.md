---
artifact: offer-communication
version: 5
status: bozza
last_reviewed: 2026-08-27
scope: "Fonte di lavoro per posizionamento, README pubblico e materiali di comunicazione di Augmented Marketing Suite"
---

# Offerta e comunicazione di Augmented Marketing Suite

## Scopo del documento

Questo documento stabilisce come presentare Augmented Marketing Suite: quale problema affronta, quale valore offre, a chi serve, che cosa lo distingue e quali promesse sono sostenibili allo stato attuale.

È la fonte di lavoro per:

- il README pubblico del repository;
- pagine di presentazione e schede del progetto;
- post, newsletter, slide e materiali di lancio;
- descrizioni brevi delle singole skill;
- messaggi rivolti a possibili utilizzatori, collaboratori e valutatori.

Non sostituisce [MARKETING-AGENT-SYSTEM.md](MARKETING-AGENT-SYSTEM.md), che resta autorevole per architettura e decisioni di prodotto, né [README.md](README.md), che deve descrivere lo stato tecnico verificato al momento della pubblicazione. Questo documento governa l'offerta e il linguaggio con cui viene comunicata.

Le versioni, lo stato delle skill e le prove disponibili devono essere ricontrollati nelle fonti tecniche prima di riusare un messaggio pubblico.

## Il problema affrontato

Molti strumenti per il marketing assistito dall'IA partono dall'esecuzione: generano post, email, campagne, immagini o piani. Questo rende più veloce produrre materiali, ma non garantisce che il problema sia stato formulato correttamente, che la direzione scelta sia plausibile o che le attività siano coerenti tra loro.

Nell'uso ordinario degli agenti emergono quattro difficoltà:

1. il contesto dell'organizzazione resta disperso tra chat e prompt;
2. fatti, inferenze e convinzioni vengono facilmente confusi;
3. una tattica iniziale può essere scambiata per una strategia;
4. una buona esecuzione può nascondere una decisione debole.

Augmented Marketing Suite nasce per intervenire prima e durante la produzione, rendendo persistente il contesto e guidando le decisioni che collegano identità, strategia, marketing mix, campagne e contenuti.

## Categoria e tesi di prodotto

**Categoria di lavoro:** framework pubblico di skill installabili per il marketing con agenti IA.

**Tesi di prodotto:** un agente diventa più utile nel marketing quando non riceve soltanto istruzioni su che cosa produrre, ma dispone di contesto approvato, regole operative, un processo decisionale e artefatti che conservano le scelte nel tempo.

Il progetto non è un agente generalista che promette di fare il lavoro di un CMO. Non è neppure un catalogo di generatori organizzati per canale. Ogni skill possiede una decisione, un artefatto e un confine riconoscibili.

**Augmented Marketing Assistant** è l'ingresso conversazionale per chi non sa da quale passaggio iniziare: comprende il bisogno espresso nel linguaggio dell'utente, spiega il passaggio utile e attiva la skill pertinente quando l'ambiente lo consente. Se il passaggio non è disponibile, indica quale skill invocare e si ferma. Non aggiunge una competenza di marketing e non prende decisioni al posto delle skill o del responsabile.

## Offerta in una frase

> Augmented Marketing Suite è un framework di skill che aiuta manager e agenti IA a prendere decisioni di marketing usando contesto condiviso, regole approvate, alternative esplicite e artefatti verificabili.

## Descrizione breve

Augmented Marketing Suite porta metodo nel lavoro di marketing con gli agenti IA. Le skill aiutano a costruire un contesto riusabile, distinguere fatti e assunzioni, formulare la sfida, confrontare direzioni strategiche, coordinare le quattro P e trasformare le decisioni approvate in attività verificabili.

## Descrizione estesa

Augmented Marketing Suite rende installabile una parte del processo con cui un marketer esperto prepara, prende e documenta le decisioni. Il sistema parte dall'identità dell'organizzazione e dalle regole di marketing approvate, non da un prompt isolato. Prima di produrre una campagna o un contenuto, può chiarire la sfida, confrontare alternative, esplicitare trade-off, individuare l'assunzione più fragile e verificare la coerenza tra Product, Price, Place e Promotion. Le decisioni restano in documenti versionati e l'approvazione del contenuto non autorizza automaticamente pubblicazione, spesa o altre azioni esterne.

## Pubblico prioritario di lavoro

Il pubblico principale è composto da:

- responsabili marketing e comunicazione che stanno introducendo agenti IA nel proprio lavoro;
- professionisti del marketing che vogliono un metodo più solido dei prompt occasionali;
- consulenti e agenzie che lavorano insieme a un referente autorizzato del cliente;
- team che devono condividere contesto, regole e decisioni tra persone e agenti diversi;
- progettisti di workflow agentici interessati a governance, artefatti persistenti e approvazioni.

Questo pubblico è una scelta di prodotto ancora da validare con l'uso reale. Non va presentato come segmento dimostrato né come elenco esaustivo.

## Situazioni d'uso

Il framework è pertinente quando una persona o un team vuole:

- fare in modo che l'agente conosca l'organizzazione prima di lavorarci;
- rendere riusabili regole di marketing oggi affidate alla memoria delle persone;
- capire se un problema richieda davvero un intervento di marketing;
- evitare che una proposta tattica diventi automaticamente la soluzione;
- confrontare direzioni strategiche e rendere visibili le rinunce;
- coordinare Product, Price, Place e Promotion;
- passare da una decisione approvata a una campagna o a un contenuto;
- conservare fonti, assunzioni, approvazioni e apprendimento tra attività diverse.

Il percorso non deve essere imposto quando obiettivo, formato e vincoli sono già sufficientemente chiari. Le skill esecutive possono essere usate direttamente quando i passaggi a monte non aggiungono valore.

## Architettura dell'offerta

```text
Augmented Marketing Assistant
        ↓ orientamento e handoff
Business Identity
        ↓
Marketing Foundations
        ↓
Brief della sfida
        ↓
Direzione di marketing
        ↓
Marketing Mix: Product · Price · Place · Promotion
        ↓
Campagne, contenuti e altre attivazioni
        ↓
Risultati e apprendimento
```

| Livello | Ruolo |
|---|---|
| Ingresso conversazionale | `Augmented Marketing Assistant` orienta verso il passaggio pertinente senza duplicare il metodo delle skill |
| Fondazione | `setup-business-context` crea l'identità persistente; `setup-marketing-system` definisce le regole stabili che gli agenti devono applicare |
| Strategy Core | `define-marketing-challenge` chiarisce il cambiamento cercato; `choose-marketing-direction` confronta alternative; `define-marketing-mix` coordina le quattro P |
| Campaign Core | `design-campaign` progetta la campagna, `campaign-review` la verifica prima del lancio e `campaign-debrief` interpreta i risultati |
| Content Core | `content-director` valuta fonti o idee, raccomanda la strada editoriale e passa un Content Brief ai builder |

Nel nucleo minimo non esiste un agente Strategist separato. Il lavoro strategico è distribuito tra le tre skill dello Strategy Core; l'Assistant orienta senza duplicarne il metodo. Un eventuale ruolo trasversale richiederà una user story e un artefatto distinti, validati dall'uso reale.

## Stato dell'offerta

La comunicazione deve distinguere sempre ciò che è disponibile da ciò che è candidato o in roadmap.

| Area | Stato comunicabile |
|---|---|
| Augmented Marketing Suite | Beta 0.1.0-beta.10 con plugin OpenAI/Codex, plugin Claude, nove skill specialistiche e Assistant; caricamento multipiattaforma e pilot esterno restano verifiche separate |
| Augmented Marketing Assistant | v0.2.0 beta; orienta anche verso Campaign Core e Content Director; gli smoke test runtime precedenti riguardano la v0.1.0 |
| Business Identity | `setup-business-context` v0.6.5 nella Suite beta.10 |
| Marketing Foundations | `setup-marketing-system` v0.3.2 nella Suite beta.10 |
| Brief della sfida | `define-marketing-challenge` v0.1.4 nella Suite beta.10 |
| Direzione di marketing | `choose-marketing-direction` v0.2.3 nella Suite beta.10 |
| Marketing Mix | `define-marketing-mix` v0.1.4 nella Suite beta.10 |
| Campaign Core | Tre skill pubblicate nella Suite beta.10; run integrato controllato a nove skill PASS su Codex Desktop, pilot con responsabile reale ancora mancante |
| Content Core | `content-director` v0.1.1 pubblicata singolarmente e nella Suite beta.10; builder esterni non inclusi |
| Monitoring | Ipotesi opzionale di roadmap |

Una cartella presente nel repository dimostra che esiste una sorgente di authoring. Non dimostra approvazione, installazione, pubblicazione o affidabilità in produzione.

## Promessa e grado di maturità

### Promessa sostenibile ora

> Un sistema che guida e documenta le decisioni di marketing, rendendo visibili contesto, alternative, trade-off, assunzioni, approvazioni e coerenza del marketing mix.

Questa formulazione descrive il metodo senza attribuire al sistema un'efficacia non ancora dimostrata.

### Ambizione distintiva

> Rendere installabile il processo decisionale di un marketer senior.

È la direzione di prodotto e comunicazione. Esprime il tipo di comportamento che il framework vuole codificare: formulare il problema, produrre una diagnosi, confrontare alternative, contestare le assunzioni, scegliere che cosa non fare, coordinare le decisioni e apprendere dai risultati.

Non equivale ancora alla prova che il sistema produca decisioni pari a quelle di uno strategist esperto.

### Claim da non usare senza nuove evidenze

Non affermare che il framework:

- sostituisce un direttore marketing o uno strategist;
- equivale ad avere un esperto di strategia;
- migliora sicuramente risultati, vendite o ritorno sugli investimenti;
- riduce tempi o costi in una misura determinata;
- rende autonoma l'esecuzione del marketing;
- è una suite completa o pronta per ogni organizzazione;
- ha dimostrato efficacia con marketer reali, finché non esiste un pilot documentato.

## Quanto è strategico il sistema

Il valore strategico non deriva dall'uso della parola “strategia”, ma dai comportamenti imposti alle skill.

Il sistema è progettato per:

- separare il problema dalla soluzione già immaginata;
- distinguere fatti, segnali, inferenze e assunzioni;
- confrontare alternative basate su meccanismi differenti;
- esplicitare trade-off, rinunce e condizioni di stop;
- poter raccomandare di restringere, approfondire o non procedere;
- individuare l'assunzione più fragile;
- proporre il primo test utile prima di investire;
- verificare la coerenza delle quattro P;
- riconoscere le decisioni che richiedono Product, Finance, Sales, Operations o altre autorità.

`choose-marketing-direction` incorpora due rafforzamenti progettuali:

1. diagnosi provvisoria di situazione, clienti o pubblici, alternative e capacità dell'organizzazione;
2. stress test della raccomandazione con miglior argomento contrario, condizioni necessarie, risposte plausibili e conseguenze indesiderate.

Resta da completare la validazione realistica di questi comportamenti e un ciclo operativo che aggiorni diagnosi, direzione e marketing mix dopo il test. Fino ad allora, la definizione più corretta è **copilota decisionale strategico**.

## Differenze rispetto a una raccolta di prompt

- **Contesto persistente:** identità, regole e decisioni vivono in artefatti versionati. Non dipendono dalla memoria della chat in cui sono stati creati.
- **Una decisione per skill:** le skill non sono ruoli generici o agenti che fanno tutto. Ognuna trasforma un input riconoscibile in un artefatto utile al passaggio successivo.
- **Un ingresso comprensibile:** l'Assistant parte dal bisogno dell'utente e attiva il percorso pertinente senza trasformarsi in un decisore o in un router software.
- **Assunzioni riconoscibili:** fonti, inferenze, conflitti e incognite restano visibili. Un'opinione confermata dal management può restare un'assunzione.
- **Decisione prima della produzione:** una tattica o un asset non vengono usati per evitare una scelta strategica. Il sistema può anche concludere che non sia il momento di produrre.
- **Approvazione umana:** la skill formula e struttura, il responsabile approva. L'approvazione del contenuto resta distinta dall'autorizzazione a salvare, spendere, pubblicare o modificare sistemi esterni.
- **Quattro P:** il marketing mix collega Product, Price, Place e Promotion e rende visibili le decisioni che richiedono altre funzioni.

## Pilastri della comunicazione

| Pilastro | Significato |
|---|---|
| Context before execution | L'agente conosce identità e regole dell'organizzazione prima di svolgere attività specifiche |
| Decisions before production | Il framework aiuta a decidere che cosa valga la pena fare prima di generare campagne e contenuti |
| Evidence before confidence | Fatti, fonti e assunzioni restano separati; la sicurezza della formulazione non sostituisce la qualità dell'evidenza |
| Strategy means choice | Una direzione comporta alternative, rinunce, rischi e condizioni che potrebbero smentirla |
| Four Ps, not promotion alone | La comunicazione è una parte del marketing mix, non l'intero marketing |
| Human approval at consequential gates | Le decisioni e le azioni con conseguenze restano sotto l'autorità delle persone responsabili |

## Messaggi da usare

- “Dai all'agente un contesto che può riusare.”
- “Descrivi il lavoro da fare: l'Assistant ti accompagna al passaggio utile.”
- “Trasforma chat e prompt in decisioni verificabili.”
- “Metti a fuoco la sfida prima di scegliere la soluzione.”
- “Confronta direzioni, non semplici varianti tattiche.”
- “Rendi visibili assunzioni, rinunce e condizioni di stop.”
- “Coordina Product, Price, Place e Promotion prima della campagna.”
- “Mantieni separate approvazione del contenuto ed esecuzione.”
- “Usa direttamente un builder quando il lavoro strategico è già stato fatto.”

## Formulazioni da evitare

- “Il tuo CMO artificiale.”
- “Un team marketing autonomo.”
- “L'IA che prende le decisioni al posto tuo.”
- “Strategia completa in pochi minuti.”
- “Risultati migliori garantiti.”
- “La soluzione definitiva per ogni attività di marketing.”
- “È come avere uno strategist esperto”, prima della relativa validazione.
- “Suite completa”, finché Strategy, Campaign e Content Core non sono operativi e testati.

Evitare anche formule generiche come “rivoluziona il marketing”, “sblocca il potenziale”, “porta la strategia al livello successivo” e altre promesse prive di un meccanismo o di una prova.

## Mappa dei messaggi

| Domanda del pubblico | Risposta centrale | Elemento di supporto | Limite da dichiarare |
|---|---|---|---|
| Devo sapere quale skill usare? | No, l'Assistant può partire dal bisogno e proporre il passaggio pertinente | Mappa di instradamento, handoff esplicito e pacchetto beta | Non è ancora stato testato con marketer esterni e il caricamento dell'Assistant dipende dall'ambiente |
| Perché non basta un buon prompt? | Il prompt non conserva da solo contesto, regole e decisioni tra attività diverse | Artefatti persistenti e versionati | Richiede che l'organizzazione mantenga aggiornati i propri contesti |
| Decide davvero la strategia? | Guida la formulazione, il confronto e l'approvazione della decisione | Alternative, trade-off, assunzione fragile e test | La qualità dipende dalle fonti, dal modello e dal giudizio del responsabile |
| Sostituisce il marketer? | No, struttura il lavoro e rende più controllabile l'uso dell'agente | Gate di approvazione e limiti di autorità | Non assume responsabilità professionale o aziendale |
| Perché usare file invece della chat? | I file permettono riuso, verifica, versionamento e handoff | Business Identity, Foundations e fascicoli decisionali | Non ogni informazione deve diventare contesto globale |
| Devo usare tutte le skill? | No, il percorso è modulare e selettivo | Attivazione basata sul lavoro richiesto | Saltare un passaggio è corretto solo quando l'input necessario esiste già |
| È già pronto per un flusso completo? | Fondazioni e Strategy Core fino al marketing mix sono disponibili | Stato dichiarato nel README e nelle release | Campaign e Content Core sono ancora in roadmap |

## Struttura consigliata per il README

Il futuro README dovrebbe seguire questo ordine:

1. **Che cos'è:** descrizione in una frase e promessa sostenibile.
2. **Perché esiste:** limite dei generatori e dei prompt isolati.
3. **Come funziona:** percorso da Business Identity a risultati e apprendimento.
4. **Che cosa lo distingue:** decisioni, provenienza, artefatti e approvazioni.
5. **Ingresso conversazionale:** ruolo e stato verificato di Augmented Marketing Assistant.
6. **Skill disponibili:** tabella con input, output e stato verificato.
7. **Esempio di percorso:** una sfida che diventa direzione, mix e attivazione.
8. **Uso modulare:** quando saltare il percorso e usare direttamente un builder.
9. **Installazione:** solo procedure realmente disponibili e versioni verificate.
10. **Eval e limiti:** che cosa è stato testato e che cosa non è ancora dimostrato.
11. **Roadmap:** componenti candidate e future senza presentarli come disponibili.

La promessa ambiziosa può comparire come tesi del progetto, accompagnata dal suo grado di maturità. La prima schermata non deve far credere che tutti i core siano già operativi.

## Moduli per i materiali di comunicazione


**Presentazione di una riga**

> Skill installabili per portare contesto, metodo e decisioni verificabili nel marketing con agenti IA.

**Presentazione breve**

> Augmented Marketing Suite aiuta manager e agenti IA a lavorare con un contesto condiviso e un processo decisionale esplicito. Prima dell'esecuzione mette a fuoco la sfida, confronta direzioni, rende visibili le assunzioni e coordina le quattro P.

**Tesi editoriale**

> Generare più velocemente non basta. Il vantaggio arriva quando l'agente sa quale problema sta affrontando, quali regole deve rispettare, quali alternative sono state scartate e quale decisione è stata approvata.

**Descrizione per una slide: dal prompt al sistema decisionale**

- contesto persistente;
- regole approvate;
- sfide formulate prima delle tattiche;
- alternative e trade-off espliciti;
- marketing mix coerente;
- approvazioni e apprendimento documentati.

## Prove necessarie per rafforzare la promessa strategica

Prima di affermare che il sistema offre una guida paragonabile a quella di uno strategist esperto, servono almeno:

1. fixture realistiche che richiedano diagnosi, scelta e rinuncia;
2. confronto tra agente senza skill e agente con lo Strategy Core;
3. valutazione cieca da parte di strategist o responsabili marketing;
4. casi in cui l'esito corretto sia fermarsi o richiedere una decisione non marketing;
5. pilot con utilizzatori reali e osservazione delle correzioni richieste;
6. evidenza che il processo cambia, restringe o interrompe almeno alcune decisioni;
7. ciclo di apprendimento che aggiorni diagnosi, direzione e marketing mix dopo il test.

Le metriche dovrebbero riguardare qualità della diagnosi, differenza reale tra alternative, chiarezza dei trade-off, coerenza delle quattro P, domande superflue, errori di autorità e utilità percepita dal decisore. Non usare punteggi promozionali privi di una baseline.

## Decisioni ancora aperte

- lingua principale della distribuzione e rapporto tra versione italiana e inglese;
- adattatori di distribuzione da mantenere per i diversi ambienti che supportano skill;
- licenza e condizioni di riuso;
- modalità con cui un test riapre e aggiorna gli artefatti strategici approvati;
- soglia di prove necessaria per usare il paragone con uno strategist esperto;
- forma e perimetro del primo pilot con utilizzatori reali.

Le decisioni aperte non devono essere presentate come fatti o funzionalità già disponibili.

## Regole di manutenzione

- Aggiornare questo documento quando cambia posizionamento, pubblico, promessa o architettura dell'offerta.
- Verificare lo stato tecnico nel README, nei file delle skill e nelle release prima di pubblicare numeri o versioni.
- Separare sempre capacità disponibili, candidate e roadmap.
- Non usare casi reali, percorsi locali, identità personali o risultati interni nei pacchetti pubblici.
- Usare per gli eval pubblici soltanto fixture sintetiche e pubblicabili.
- Conservare lo stesso grado di certezza nel passaggio da questo documento a README, post, pagine e slide.
- Trattare ogni claim più forte come un'ipotesi finché non esiste una prova adeguata.

## Fonti di progetto

- [MARKETING-AGENT-SYSTEM.md](MARKETING-AGENT-SYSTEM.md)
- [README.md](README.md)
- [PORTABILITA.md](PORTABILITA.md)
- [Augmented Marketing Assistant](agents/augmented-marketing-assistant.md)
- [setup-business-context](skills/setup-business-context/SKILL.md)
- [setup-marketing-system](skills/setup-marketing-system/SKILL.md)
- [define-marketing-challenge](skills/define-marketing-challenge/SKILL.md)
- [choose-marketing-direction](skills/choose-marketing-direction/SKILL.md)
- [define-marketing-mix](skills/define-marketing-mix/SKILL.md)

## Registro modifiche

- v7, 2026-08-27: promosso Augmented Marketing Assistant a v0.1.0 stabile dopo tre smoke test runtime Codex superati, mantenendo Augmented Marketing Suite in beta.
- v6, 2026-08-27: ristretto l'Assistant all'orientamento, aggiunto il fallback esplicito quando l'handoff non è disponibile e allineati i titoli visibili ai nomi tecnici inglesi.
- v5, 2026-08-27: adottato Augmented Marketing Suite come nome del prodotto e del plugin, mantenendo Augmented Marketing Assistant come ingresso conversazionale.
- v4, 2026-08-27: aggiunto il plugin OpenAI beta.2 e distinto il suo adattatore tecnico dal ruolo dell'Assistant.
- v3, 2026-08-27: introdotto Augmented Marketing Assistant come ingresso conversazionale e promosso alla beta, separandolo dalla logica delle skill.
- v2, 2026-08-27: allineato lo stato di Direzione di marketing e Marketing Mix alle release stabili e aggiunto il riferimento al contratto di portabilità.
- v1, 2026-08-26: prima formulazione dell'offerta, della promessa, dei confini dei claim e delle linee guida per README e comunicazione.
