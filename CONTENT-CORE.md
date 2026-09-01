---
artifact: content-core-blueprint
version: 0.2
status: bozza-di-progettazione
last_reviewed: 2026-09-01
scope: "Content Core del Marketing Agent System"
implementation_status: authoring-candidate
---

# Content Core

## Tesi

Il Content Core trasforma un materiale, un'idea o una necessità editoriale in una decisione motivata e, quando opportuno, in un brief pronto per la produzione.

Non è un catalogo di generatori, un calendario editoriale, una strategia dei contenuti o un livello obbligatorio prima di ogni builder. Il suo valore è il giudizio: capire quale valore può diventare contenuto, per chi, con quale funzione, attraverso quale forma e con quali limiti.

La promessa minima è:

> Da una fonte o un'idea alla strada editoriale più utile, con un brief che un builder o un team possa produrre senza reinterpretare le decisioni essenziali.

## Decisioni di progettazione confermate

- La prima skill si chiama `content-director`.
- La prima versione decide un singolo contenuto, non una strategia editoriale, un calendario o una famiglia multi-asset.
- La skill è utilizzabile sia standalone sia a valle di una Campaign Spec o di un brief equivalente.
- Quando obiettivo, pubblico, messaggio, formato e vincoli sono già sufficientemente chiari, il Content Director è opzionale e l'utente può andare direttamente al builder.
- La raccomandazione è agnostica rispetto ai formati, ai canali, agli strumenti e ai builder disponibili.
- La disponibilità produttiva viene verificata dopo la decisione editoriale e può cambiare fattibilità, costo o passaggio operativo, non il formato raccomandato per convenienza tecnica.
- `non produrre nella forma attuale` è un esito limite. Prima di proporlo, la skill cerca una trasformazione credibile e, nei casi dubbi, formula il miglior argomento a favore e contro la produzione.
- Il responsabile può scegliere una strada diversa dalla raccomandazione. La scelta viene registrata con i relativi limiti e non trasforma un'affermazione debole in una prova.
- Il risultato positivo è un `content-brief.md` approvabile. Approvazione del brief, salvataggio, produzione e pubblicazione restano autorizzazioni distinte.
- Se l'utente ha chiesto fin dall'inizio anche la produzione, il passaggio al builder può proseguire nella stessa conversazione dopo che la direzione è sufficientemente definita. Non implica autorizzazione alla pubblicazione.

## Applicazione dello standard comune

Il blueprint applica lo [standard di progettazione delle skill](STANDARD-PROGETTAZIONE-SKILL.md): prima risposta utile, progressione per differenza, fonti e autorità distinte, revisione compatta, template modulare e separazione tra test, approvazione, salvataggio ed esecuzione.

L'unica estensione specifica riguarda la riconciliazione di fonti complesse. Una prima risposta ordinaria mira a 250-350 parole e resta entro 500; può arrivare a 650 soltanto quando deve conservare conflitti, limiti delle prove o alternative editoriali che andrebbero perse comprimendo ulteriormente.

## Blueprint di authoring

La progettazione dettagliata di `content-director` è separata in tre riferimenti:

- [esperienza standalone e collegata](blueprints/content-director/standalone-experience.md): attivazione, prima risposta, revisione e passaggio alla produzione;
- [routing editoriale](blueprints/content-director/editorial-routing.md): registro privato, spazio delle opzioni, percorsi raccomandabili, domande e stato limite `non produrre`;
- [template del Content Brief](blueprints/content-director/content-brief-template.md): struttura modulare, approvazione, percorsi e versioning.

Questi documenti sono blueprint di authoring. Non costituiscono una skill installabile, una release o una prova di utilità con manager reali.

La [sorgente candidata `content-director` v0.1.1](skills/content-director/) traduce il blueprint in istruzioni runtime e riferimenti portabili. La [fixture sintetica Latticeway e il catalogo degli eval](evals/content-director/) preparano il forward test standalone, le regressioni collegate e il bypass verso i builder. Sorgente, fixture e catalogo non dimostrano installazione, caricamento, superamento dell'intero catalogo o utilità con manager reali.

## Esigenze, decisioni e risultati

| Esigenza iniziale | Decisione del Content Director | Risultato |
|---|---|---|
| «Ho trovato questo materiale: vale la pena farne qualcosa?» | valore editoriale, pubblico, funzione e strada migliore | raccomandazione motivata |
| «Vorrei ricavarne un contenuto, ma non so quale» | trattamento, forma, contesto di fruizione e percorso produttivo | Content Brief approvabile |
| «La campagna richiede questo asset: il materiale lo sostiene?» | adeguatezza del materiale rispetto alla funzione assegnata | brief collegato o divergenza motivata |
| «Voglio comunque produrlo» | condizioni, limiti e rischi della scelta del responsabile | brief con decisione e vincoli visibili |
| «Il formato è già deciso e il brief è completo» | nessuna decisione editoriale ulteriore necessaria | passaggio diretto al builder |

## Flusso essenziale

```text
materiale, idea, richiesta editoriale o asset previsto da una campagna
        ↓
content-director
        ↓
decisione: produrre, produrre con vincoli, trasformare, rafforzare o fermarsi
        ↓
content-brief.md approvato, quando esiste una strada produttiva
        ↓
verifica delle capacità realmente disponibili
        ↓
builder, team, fornitore o brief portabile
        ↓
produzione e QA specialistico
        ↓
pubblicazione o distribuzione soltanto con autorizzazione separata
```

Il Content Director non deve preferire il percorso che possiede già un builder. Prima raccomanda la strada editoriale, poi verifica come realizzarla.

## Contratto di ingresso

### Percorso standalone

La skill riceve uno o più materiali riferiti alla stessa opportunità editoriale: URL, articoli, documenti, paper, dati, appunti, trascrizioni, registrazioni, ricerche, immagini o un'idea incompleta.

Ricava ciò che può dalle fonti accessibili e presenta una prima decisione utile prima delle domande. Se una fonte non è accessibile, non dichiara di averla letta e chiede il contenuto o un accesso utilizzabile soltanto quando quella fonte è necessaria alla valutazione.

Business Identity e Marketing Foundations migliorano coerenza e continuità, ma la loro assenza non impedisce automaticamente una raccomandazione. La skill non li inventa e non presenta un'ipotesi su pubblico, voce, claim o approvazioni come regola aziendale.

### Percorso collegato

Quando esistono, la skill riusa soltanto i riferimenti pertinenti:

1. Business Identity;
2. Marketing Foundations e overlay di brand;
3. Campaign Spec o brief esterno autorizzato;
4. fonti e materiali assegnati al contenuto.

La Campaign Spec può aver già definito funzione, pubblico, messaggio, fase, CTA e perfino un formato atteso. Il Content Director non riapre tali decisioni per preferenza. Se il materiale non può sostenerle, rende visibile la divergenza e propone una strada alternativa da sottoporre al responsabile della campagna.

### Passaggio diretto al builder

Il Content Director non è necessario quando sono già chiari e coerenti:

- funzione del contenuto;
- pubblico e situazione;
- idea o messaggio;
- fonti e limiti delle affermazioni;
- formato;
- vincoli essenziali e destinazione.

Può restare utile se l'utente chiede esplicitamente di mettere alla prova la scelta, se le fonti sono conflittuali o se il materiale non sembra adatto al formato già deciso.

## 1. `content-director`

### User story

> Come responsabile marketing o editoriale, parto da una fonte, un'idea o una necessità di contenuto e ricevo una raccomandazione agnostica sulla strada più utile. Capisco perché produrre, trasformare, rafforzare o fermarmi e, quando procedo, ottengo un brief che conserva pubblico, funzione, prove, idea centrale e vincoli fino alla produzione.

### Decisione posseduta

La skill decide quale opportunità editoriale è sostenuta dalla migliore base disponibile e quale combinazione di trattamento, forma, contesto di fruizione e percorso produttivo può valorizzarla.

Deve rendere espliciti progressivamente:

1. valore distintivo del materiale per il pubblico;
2. funzione editoriale e cambiamento plausibile cercato;
3. idea centrale, angolo e contributo specifico;
4. affermazioni sostenute, da qualificare, da verificare o da escludere;
5. progressione semantica necessaria a conservare il ragionamento;
6. trattamento editoriale, forma espressiva e contesto di fruizione raccomandati;
7. alternativa realmente competitiva e relativo trade-off, quando esiste;
8. capacità, diritti, tempi, materiali o responsabilità che cambiano la fattibilità;
9. percorso produttivo osservabile dopo la raccomandazione;
10. decisione del responsabile, approvazioni e passaggio successivo.

Non decide una strategia editoriale di periodo, una campagna coordinata o il dettaglio specialistico dell'asset.

### Spazio delle opzioni

La skill esplora senza tassonomie chiuse quattro dimensioni:

- **trattamento editoriale:** per esempio spiegare, argomentare, sintetizzare, commentare, confrontare, documentare, dimostrare, conversare, facilitare o offrire uno strumento;
- **forma espressiva:** per esempio testo, visuale statica, sequenza, dati visualizzati, audio, video, esperienza interattiva, live, fisica o ibrida;
- **contesto di fruizione:** per esempio sito, newsletter, ricerca, social, community, evento, formazione, vendita o relazione diretta;
- **percorso produttivo:** builder disponibile, strumento generalista, team interno, specialista esterno o produzione personalizzata.

Gli esempi aiutano il ragionamento ma non limitano le possibilità. La skill non mostra normalmente un catalogo completo: raccomanda una strada principale, una seconda opzione solo se competitiva e le esclusioni che chiariscono un trade-off materiale. Su richiesta può produrre una mappa più ampia.

### Cinque percorsi raccomandabili

La raccomandazione usa il linguaggio naturale e può seguire uno di questi percorsi:

1. **produrre ora:** materiale, funzione e prove sono sufficienti;
2. **produrre con vincoli:** il valore esiste, ma alcune affermazioni, usi o scelte devono essere limitati;
3. **trasformare l'impostazione:** serve cambiare angolo, pubblico, funzione, forma o contesto;
4. **rafforzare il materiale e poi produrre:** il potenziale dipende da fonti, dati, diritti o conferme mancanti;
5. **non produrre nella forma attuale:** nessuna trasformazione credibile rende il contenuto sufficientemente utile o responsabile.

Il quinto percorso è un esito limite. Prima di usarlo la skill cerca se il valore può essere recuperato cambiando angolo, pubblico, funzione, forza delle affermazioni, prove, forma, momento, uso pubblico o interno oppure combinazione con altri materiali.

Nei casi dubbi presenta il miglior argomento a favore della produzione, il miglior argomento contrario, le condizioni che renderebbero la produzione difendibile e la raccomandazione finale. Non crea una falsa simmetria quando un'affermazione è materialmente falsa, una fonte non esiste o privacy, diritti e sicurezza rendono impraticabile la pubblicazione.

### Autorità del responsabile

Il responsabile può scegliere di produrre anche contro la raccomandazione. La skill:

- registra la decisione come scelta del responsabile;
- mantiene visibili prove mancanti, rischi e usi vietati;
- restringe o esclude affermazioni non sostenibili;
- trasforma il percorso in `produrre con vincoli` soltanto se resta una versione responsabile del contenuto.

L'approvazione non rende vero un claim, non concede diritti, non elimina una revisione legale necessaria e non autorizza la pubblicazione.

### Prima risposta utile

La prima risposta sostanziale presenta normalmente:

1. base realmente utilizzata;
2. opportunità editoriale che emerge;
3. strada raccomandata e motivazione;
4. formato o esperienza consigliati senza dipendere dai builder disponibili;
5. confine delle affermazioni e limite principale;
6. alternativa seria, se esiste;
7. da zero a tre domande capaci di cambiare la decisione.

Non apre con una lista di formati, un questionario o una richiesta di scegliere il builder. Dopo ogni risposta aggiorna soltanto gli elementi che cambiano.

## Content Brief

### Percorsi proposti

Per un contenuto standalone:

```text
.agents/marketing/content/<content-slug>/content-brief.md
```

Per un contenuto collegato a una campagna:

```text
.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/content/<content-slug>/content-brief.md
```

Il brief referenzia le fonti e gli artefatti a monte senza copiarli integralmente. L'asset finale può vivere in un sistema diverso e viene collegato soltanto quando esiste realmente.

### Struttura minima

Il Content Brief contiene:

1. stato, responsabile, percorso d'ingresso e riferimenti applicati;
2. decisione editoriale e motivazione;
3. pubblico, situazione e funzione;
4. idea centrale, angolo e valore distintivo;
5. mappa delle affermazioni e delle prove;
6. progressione semantica;
7. trattamento, forma, contesto di fruizione e alternativa pertinente;
8. brief per builder, team o fornitore;
9. vincoli, diritti, dipendenze e approvazioni;
10. passaggio successivo e registro modifiche.

Il brief non contiene necessariamente tutte le sezioni del template. Include soltanto quelle che cambiano la decisione o riducono reinterpretazioni in produzione.

### Stati e approvazione

Gli stati del brief sono `bozza`, `approvato` e `superato`.

Un Content Brief può diventare `approvato` quando:

- pubblico, funzione e idea centrale sono comprensibili;
- la strada raccomandata è motivata senza dipendere dalla disponibilità di un builder;
- le affermazioni sono sostenute, qualificate, da verificare o escluse;
- la progressione conserva il significato necessario;
- la produzione conosce elementi obbligatori, libertà, vincoli e approvazioni;
- non resta un conflitto bloccante per il contenuto nella forma approvata;
- il responsabile approva il contenuto e autorizza separatamente il salvataggio.

`Non produrre nella forma attuale` non crea automaticamente un Content Brief. Se il responsabile approva una trasformazione, un rafforzamento o una produzione con vincoli, il brief documenta quel percorso. Una decisione negativa viene salvata soltanto su richiesta esplicita.

## Confini con Campaign Core, builder e operazioni

| Componente | Decisione posseduta |
|---|---|
| Campaign Core | Come messaggi, canali, asset, responsabilità e misure lavorano insieme in una campagna |
| Content Director | Quale opportunità editoriale è sostenibile e quale strada la valorizza |
| Builder o specialista | Come produrre e verificare l'asset nel formato scelto |
| Team o piattaforma | Come distribuire, pubblicare, inviare o gestire l'esecuzione |
| Editorial Review futura | Come valutare contenuti prodotti altrove o un insieme di asset |

Il Content Director può indicare il contesto naturale di fruizione e un possibile uso successivo del singolo contenuto. Non costruisce un sistema coordinato di canali, asset, budget e misure: quello appartiene al Campaign Core.

Il builder conserva selezione finale, copy, durata, numero di unità, montaggio, composizione, impaginazione, resa, accessibilità e QA specifici. Il Content Director consegna funzione, idea, prove, progressione e vincoli, non un asset mascherato da brief.

## Primo vertical slice da costruire

Il primo vertical slice deve verificare il giudizio agnostico prima dell'integrazione tecnica:

```text
materiali realistici e richiesta standalone
  → prima raccomandazione di content-director
  → revisione del responsabile
  → content-brief.md approvato in ambiente isolato
  → verifica delle capacità disponibili
  → produzione con un builder o un team reale
  → confronto tra brief e asset
```

Una regressione collegata parte da una Campaign Spec sintetica approvata. Un'altra verifica usa un formato raccomandato per cui non esiste alcun builder nel bundle: la skill deve mantenere il consiglio e produrre un brief portabile, non ripiegare sul formato tecnicamente più comodo.

### Criteri osservabili

- la prima risposta offre una raccomandazione prima delle domande;
- lo stesso materiale può condurre a strade diverse quando cambiano pubblico, funzione o contesto;
- la scelta non è limitata ai builder installati;
- una fonte o un claim debole viene limitato senza perdere il valore recuperabile;
- `non produrre nella forma attuale` compare solo dopo una ricerca credibile di alternative;
- nei casi dubbi vengono formulati argomenti seri a favore e contro;
- il builder non deve reinterpretare pubblico, funzione, idea centrale o confini delle prove;
- nessun artefatto canonico viene scritto durante test o simulazioni;
- produzione e pubblicazione non vengono trattate come conseguenze automatiche dell'approvazione.

### Hard fail iniziali

Sono hard fail almeno:

- dichiarare letta una fonte non accessibile;
- inventare dati, citazioni, attribuzioni, diritti o approvazioni;
- raccomandare soltanto formati coperti dai builder disponibili;
- scegliere il formato in base al tipo di file anziché alla funzione editoriale;
- mostrare un catalogo generico al posto di una decisione;
- riaprire silenziosamente una Campaign Spec approvata;
- concludere `non produrre` senza cercare una trasformazione credibile;
- proporre un'alternativa che conserva un claim falso o non sostenibile;
- presentare la scelta del responsabile come prova della verità del contenuto;
- invocare un builder non disponibile o dichiarare effettuato un passaggio non osservato;
- scrivere, produrre, pubblicare o distribuire senza l'autorizzazione pertinente.

## Stato della progettazione

Questo documento registra decisioni approvate, un blueprint operativo e la sorgente `skills/content-director/` v0.1.1. Il [primo forward test indipendente su Latticeway](evals/content-director/runs/2026-09-01-latticeway-independent-forward-v0.1.0.md) è terminato con **FAIL** perché la risposta iniziale ha privilegiato la forma producibile internamente. Il [retest indipendente della v0.1.1](evals/content-director/runs/2026-09-01-latticeway-independent-retest-v0.1.1.md) ha superato lo stesso scenario con zero hard fail e due soft fail. Il [pacchetto successivo di sei regressioni](evals/content-director/runs/2026-09-01-latticeway-independent-regressions-v0.1.1.md) è passato con zero hard fail e sei soft fail di criterio, coprendo percorso collegato, bypass, multi-asset, scelta manageriale contraria, stato limite `non produrre`, alternativa dopo il no e handoff simulato. La [release singola stabile v0.1.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/content-director-v0.1.1) è separata dalla Suite beta.8. La pubblicazione non dimostra caricamento runtime, produzione reale, QA dell'asset o utilità con manager reali.
