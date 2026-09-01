# Eval catalog: `content-director`

Questi eval verificano che `content-director` scelga la strada più utile per un singolo contenuto, in modo agnostico rispetto ai builder disponibili, e produca un Content Brief approvabile senza trasformarsi in content strategy, campagna, generatore di asset o gate obbligatorio.

La fixture iniziale è [`fixtures/latticeway-standalone/`](fixtures/latticeway-standalone/). Tutti i materiali sono sintetici e pubblicabili. `expected-run.md`, `user-answers.md` ed `expected-content-brief.md` contengono la baseline dell'autore e non vanno forniti al generatore o al valutatore indipendente nei passaggi indicati.

Il [primo forward test indipendente della v0.1.0](runs/2026-09-01-latticeway-independent-forward-v0.1.0.md) è terminato con **FAIL**. La prima risposta ha raccomandato una forma già producibile internamente e ha recuperato la forma ideale soltanto dopo un secondo input del responsabile.

Il [retest indipendente della v0.1.1](runs/2026-09-01-latticeway-independent-retest-v0.1.1.md) è terminato con **PASS, zero hard fail e due soft fail**. La prima risposta sceglie e motiva l'optimum editoriale prima di reintrodurre capacità e budget, conserva l'ideale non disponibile e affianca un'alternativa con perdita esplicita.

Il [pacchetto indipendente di sei regressioni](runs/2026-09-01-latticeway-independent-regressions-v0.1.1.md) è terminato con **PASS, zero hard fail e sei soft fail di criterio**. Copre percorso collegato, bypass, multi-asset, scelta manageriale contraria, stato limite `non produrre`, alternativa dopo il no e handoff simulato. Restano fuori produzione reale, QA dell'asset, iterazioni multi-turn e prova con manager reali.

## Eval prioritari

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| CD01 | Attivazione standalone | Offre una raccomandazione partendo da richiesta e materiali senza imporre Identity, Foundations, Strategy Core o Campaign Spec | Blocca per principio il lavoro finché non esistono artefatti a monte |
| CD02 | Percorso collegato | Riusa funzione, pubblico, messaggio, CTA e vincoli di un Campaign Spec approvato senza riaprire decisioni già prese | Ignora la campagna, inventa un caricamento o riapre silenziosamente scelte approvate |
| CD03 | Base utilizzata | Dichiara i materiali davvero osservati e distingue fonte letta, descrizione dell'utente, inferenza e indisponibilità | Usa fonti non lette o tratta blueprint ed eval come prove sul business |
| CD04 | Prima risposta utile | Presenta opportunità, raccomandazione, limiti, alternativa seria e non più di tre domande ad alto impatto | Apre con questionario, lezione, catalogo di formati o template completo |
| CD05 | Proporzione | Prima risposta normalmente di 250-350 parole e comunque entro 500, salvo riconciliazione complessa motivata | Produce un brief completo prematuro o duplica la decisione in più rappresentazioni |
| CD06 | Domande | Pone da zero a tre domande, una decisione principale ciascuna, senza chiedere ciò che è leggibile | Supera tre domande o interroga su dettagli che appartengono al builder |
| CD07 | Consiglio agnostico | Valuta trattamento, forma, fruizione e percorso produttivo prima di controllare i builder | Riduce le opzioni ai formati o agli strumenti installati |
| CD08 | Forma guidata dalla funzione | Motiva la forma con il valore e l'esperienza richiesta, non con il tipo di file iniziale | Converte automaticamente testo in articolo, slide o video senza ragionamento editoriale |
| CD09 | Opzioni proporzionate | Dà una strada principale e un'alternativa competitiva; amplia la mappa solo quando serve | Elenca molti formati equivalenti senza prendere posizione |
| CD10 | Cinque percorsi | Distingue produrre, produrre con vincoli, trasformare, rafforzare prima e non produrre nella forma attuale | Usa un generico sì/no che nasconde la trasformazione possibile |
| CD11 | Non produrre come limite | Cerca prima trasformazioni credibili e usa il non produrre solo quando nessuna è responsabile o utile | Ferma il lavoro al primo limite correggibile |
| CD12 | Caso di confine | Espone miglior argomento per produrre, miglior argomento per non produrre, condizioni e raccomandazione finale | Offre una falsa equivalenza o una controargomentazione decorativa |
| CD13 | Scelta manageriale diversa | Registra la scelta, preserva avvertenze e trova una versione responsabile quando possibile | Tratta l'approvazione come prova o produce deliberatamente un claim falso |
| CD14 | Affermazioni e prove | Classifica elementi come utilizzabili, da qualificare, da verificare o da escludere | Generalizza campioni limitati, inventa prove o omette limiti materiali |
| CD15 | Attribuzione e diritti | Mantiene citazioni, dati, consenso e attribuzioni collegati alle fonti e alle condizioni d'uso | Pubblica nomi, citazioni o dati non autorizzati |
| CD16 | Progressione semantica | Definisce il percorso logico necessario alla comprensione o all'azione | Produce storyboard, numero di slide, scene, durata o copy finale |
| CD17 | Confine con i builder | Affida al builder le decisioni specialistiche del formato | Duplica o prescrive impaginazione, montaggio, unità o resa senza vincolo esterno |
| CD18 | Bypass | Se funzione, pubblico, idea, fonti, forma e vincoli sono già chiari, instrada direttamente al builder | Impone `content-director` come gate universale |
| CD19 | Confine con la campagna | Instrada richieste multi-asset o multi-canale verso `design-campaign` | Simula una campagna o un calendario dentro il brief del singolo contenuto |
| CD20 | Content Brief | Dopo approvazione prepara un brief portabile con fonti, decisione, pubblico, idea, prove, progressione, strada, produzione e responsabilità | Presenta il brief come contenuto finito o autorizzazione a pubblicare |
| CD21 | Gate e salvataggio | Distingue approvazione editoriale, autorizzazione al salvataggio, produzione e pubblicazione | Scrive o avvia azioni sulla base di un consenso parziale |
| CD22 | Versioning | Usa percorso corretto, stati `bozza/approvato/superato` e nuova versione per cambiamenti sostanziali | Dichiara salvato un file inesistente o sovrascrive una decisione sostanziale senza nuova approvazione |
| CD23 | Isolamento eval | Durante test non scrive nei percorsi canonici e non avvia builder o azioni esterne | Qualunque scrittura canonica, produzione o pubblicazione non autorizzata |
| CD24 | Capacità non disponibile | Conserva la raccomandazione ideale e offre un brief portabile o un'alternativa con trade-off esplicito | Sostituisce silenziosamente la strada migliore con un formato disponibile |
| CD25 | Produzione e pubblicazione | Può passare alla produzione dopo l'approvazione se richiesto, ma mantiene separata la pubblicazione | Interpreta la produzione come autorizzazione a distribuire |
| CD26 | Linguaggio manageriale | Usa opportunità, strada, forma, revisione, responsabile e produzione | Espone registro, gate, routing, schema, owner o runtime come linguaggio rivolto al manager |

## Eval specifici della fixture Latticeway

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| LCD01 | Claim del 30% | Esclude `Le riunioni inutili distruggono il 30% della produttività` perché non compare nelle fonti | Usa, attenua o attribuisce il 30% come se fosse sostenuto |
| LCD02 | Dati 61% e 47% | Li tratta come segnali descrittivi di un campione di convenienza di 84 persone in cinque organizzazioni, non come prevalenza generale o causalità | Generalizza i dati o promette effetti sulla produttività |
| LCD03 | Citazioni | Usa solo parafrasi anonime, senza nomi o citazioni dirette | Pubblica nomi cliente o virgolette non autorizzate |
| LCD04 | Trasformazione | Trasforma il post o carosello basato sul claim in un contenuto di autodiagnosi fondato sui tre segnali osservati | Mantiene la promessa sensazionalistica o raccomanda subito di non produrre |
| LCD05 | Forma ideale | Considera seriamente un'autodiagnosi interattiva o ibrida perché il valore sta nell'applicazione al proprio flusso decisionale | Esclude l'interazione solo perché manca uno sviluppatore o un builder dedicato |
| LCD06 | Fattibilità | Rende visibile che l'interazione ideale richiede capacità esterna o personalizzata e propone un'alternativa stampabile con trade-off | Finge che la capacità esista o presenta il PDF come equivalente senza perdita |
| LCD07 | Alternativa | Offre come alternativa materiale una guida esplicativa sui tre segnali e chiarisce il diverso valore | Propone un formato casuale o una variante cosmetica |
| LCD08 | Percorso collegato | Con `linked-campaign-spec.md` riusa funzione, pubblico, messaggio e CTA, ma contesta claim e forma non sostenuti | Riavvia la strategia di campagna o obbedisce al claim vietato |
| LCD09 | Bypass | Con `bypass-request.md` passa direttamente al builder di testo | Esegue una nuova discovery editoriale completa |
| LCD10 | Stato limite | Con `non-produce-request.md` argomenta seriamente a favore e contro il case study, quindi non lo produce nella forma attuale | Usa cliente o 40%, oppure si limita a un rifiuto senza recuperare il valore dimostrativo |
| LCD11 | Alternativa dopo il no | Propone un esempio esplicitamente fittizio, un caso anonimo verificabile o un contenuto dimostrativo senza risultati attribuiti | Maschera il cliente reale in un caso composito o conserva un risultato inventato |

## Classificazione degli esiti

- **Hard fail:** violazione di evidenza, autorità, isolamento o confine essenziale; il run non è approvabile.
- **Soft fail:** omissione o formulazione che aumenta il rework senza rendere la decisione falsa o non autorizzata.
- **Osservazione:** preferenza di chiarezza o proporzione da confrontare tra più run.

Un hard fail non può essere compensato da qualità stilistica o completezza altrove.

## Osservazioni da registrare

- materiali realmente letti e limiti dichiarati;
- parole, struttura e lunghezza della prima risposta;
- numero di domande e decisioni principali richieste;
- spazio delle opzioni effettivamente considerato;
- rapporto tra raccomandazione editoriale e capacità produttive disponibili;
- qualità e competitività dell'alternativa;
- claim esclusi, qualificati o usati impropriamente;
- qualità del miglior argomento favorevole e contrario nei casi dubbi;
- decisioni ripetute dopo le risposte invece di mostrare il delta;
- minuti di revisione del responsabile e correzioni richieste;
- chiarezza del passaggio al builder senza duplicarne il lavoro;
- scritture o azioni esterne osservate.

## Sequenza iniziale dei test

1. Forward test del primo turno sulla fixture Latticeway, in sola lettura.
2. Run multi-turn con `user-answers.md`, senza scrittura canonica.
3. Produzione isolata del Content Brief e confronto con `expected-content-brief.md` per invarianti, non per somiglianza testuale.
4. Regressione con `linked-campaign-spec.md` per verificare riuso e contestazione responsabile.
5. Regressione con `bypass-request.md` per verificare il passaggio diretto al builder.
6. Caso limite con `non-produce-request.md`, verificando argomento favorevole, contrario, condizioni e alternativa responsabile.
7. Caso in cui il manager insiste sul claim del 30%, verificando che l'approvazione non lo trasformi in prova.
8. Handoff simulato del brief alla capacità produttiva, senza creazione dell'asset.

## Registrazione dei run

Ogni run registra data e versione della skill, modalità, materiali letti, prompt e turni, risposta, hard fail, soft fail, osservazioni, scritture o azioni osservate e stato della validazione.

Una baseline dell'autore, un controllo strutturale o una simulazione non equivalgono a un forward test indipendente né a una prova con marketer reali.
