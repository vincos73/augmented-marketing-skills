# Proposte di miglioramento per Augmented Marketing Suite

Data: 2 settembre 2026
Stato: proposta da discutere, non ancora approvata

## Scopo

Questo documento raccoglie e ordina le proposte emerse da:

- valutazione delle skill per ingegneri di [mattpocock/skills](https://github.com/mattpocock/skills);
- verifiche architetturali e comportamentali di Augmented Marketing Suite;
- feedback di un marketer che ha usato le cinque skill di Setup e Strategy per un riposizionamento;
- test end-to-end e consolidamento della beta.10;
- review critica della beta.10 contenuta in [SUITE-REVIEW-BETA10.md](SUITE-REVIEW-BETA10.md).

Le proposte non costituiscono una nuova release e non autorizzano modifiche alle skill, packaging, pubblicazione o installazione.

## Evidenze da preservare

### Feedback dal riposizionamento

Il feedback del marketer promuove soprattutto il sistema di artefatti e gate:

> Il sistema è la parte più riuscita. Ogni passaggio produce un documento su disco con versioni, stato e provenienza di ogni affermazione; i gate espliciti separano l'approvazione del contenuto dall'autorizzazione a salvare e dall'esecuzione. Questa architettura ha retto anche ai due stress test involontari e volontari del mio percorso: quando la chat ha perso memoria per l'auto-compattazione, il lavoro è ripartito dai file senza che dovessi rispiegare nulla; e quando ho provato a forzare la suite fuori ordine, chiedere il mix con una direzione non più valida, si è fermata da sola, con il motivo giusto e il percorso per sbloccare. La catena sfida → direzione → mix regge anche quando la si maltratta.

Questa è evidenza qualitativa, non un benchmark statistico. Rafforza però tre requisiti di prodotto:

- gli artefatti persistenti sono più importanti della memoria implicita della chat;
- stato, provenienza e autorizzazioni devono restare separati e verificabili;
- interruzione, ripresa e uso fuori ordine sono casi di prova essenziali.

### Gap principale osservato dal marketer

Le skill sono prudenti nel non inventare, ma non sempre sono abbastanza attive nel recuperare informazioni aziendali ad alta conseguenza. Nel test sono mancate domande su:

1. cambiamenti di settore capaci di invalidare la sfida, inclusa una norma già registrata nei contesti;
2. periodo di riferimento dei dati;
3. obiettivo di fatturato, clienti necessari e budget.

Il principio da formalizzare resta:

> "Non inventare" e "non chiedere" sono regole diverse.

Le domande strutturate con scelta multipla, `Altro` e `non ancora definito` sono il pattern preferito quando aiutano il responsabile a rendere esplicito ciò che sa senza trasformare il percorso in un questionario.

## Principi importati dalle skill per ingegneri

### Frontiera delle decisioni

Una domanda entra nel dialogo soltanto quando i suoi prerequisiti sono risolti. L'agente ricerca e riconcilia i fatti disponibili; il responsabile prende le decisioni che gli competono.

Applicazioni principali:

- non discutere canali o budget se pubblico e obiettivo sono ancora aperti;
- non definire il follow-up prima di sapere quale risposta deve generare la campagna;
- non chiedere un target numerico prima di avere evento osservabile, definizione e base di confronto;
- non ripetere informazioni già confermate;
- rinviare le decisioni a valle rendendone visibile il prerequisito.

### Review su assi non compensabili

Ogni review dovrebbe distinguere:

1. **Contratto e governo:** fonti, provenienza, autorità, approvazioni, stato dell'artefatto, modalità test ed effetti esterni.
2. **Qualità della decisione:** fedeltà al brief, coerenza strategica, utilità, proporzione e rework necessario.

Un hard fail sul primo asse non viene compensato da un buon risultato sul secondo.

### Mappa dei percorsi

Il percorso dovrebbe essere rappresentabile in questa forma:

```text
situazione osservata
→ risultato già disponibile
→ decisione ancora necessaria
→ capacità pertinente
→ output prodotto
→ passo successivo consentito
→ condizioni per saltare, rinviare o fermarsi
```

### Sviluppo per vertical slice

Ogni capacità importante dovrebbe attraversare la catena completa:

```text
sorgente
→ fixture
→ dialogo completo
→ review indipendente
→ packaging
→ caricamento runtime
→ prova con utente
```

## Proposte prioritarie consolidate

| ID | Priorità | Proposta | Stato dopo beta.10 | Prova di accettazione |
|---|---|---|---|---|
| P1 | P0 | Completare e verificare un percorso end-to-end | Beta.10 include nove skill e la catena candidata; runtime e pilot completo restano separati | Il percorso attraversa Strategy, Campaign, Content, review e debrief nel runtime dichiarato |
| P2 | P0 | Introdurre la frontiera delle decisioni | Ancora prioritario | Le domande rispettano prerequisiti, autorità e informazioni già disponibili |
| P3 | P0 | Separare contratto e qualità della decisione | Rafforzato da `campaign-review`, da estendere agli eval | I due esiti restano distinti e un hard fail non viene mediato |
| P4 | P0 | Garantire continuità dopo compattazione e ripresa | Rafforzato da artefatti, lineage e stato | Il percorso riparte dai file senza ricostruzioni o decisioni perse |
| P5 | P1 | Mantenere build e pacchetti riproducibili | Molto rafforzato in beta.10 | Sorgente, manifesti, ZIP e checksum restano confrontabili |
| P6 | P0 | Rafforzare disciplina su claim, numeri e causalità | Ancora prioritario | Claim e risultati distinguono documentato, osservato, correlato, causale e ipotesi |
| P7 | P1 | Rendere esplicita la mappa dei percorsi | Assistant ampliato, verifica runtime ancora necessaria | Ingressi, bypass, output, stop e passo successivo sono leggibili |
| P8 | P1 | Confinare le differenze di piattaforma agli adattatori | Bundle distinti presenti | Nucleo, adattatore e comportamento runtime sono verificati separatamente |
| P9 | P1 | Ridurre gergo, ripetizioni e attrito | Migliorato, non provato con campione sufficiente | Dialoghi proporzionati, niente domande ripetute, linguaggio da marketer |
| P10 | P1 | Rendere il passaggio di stato più forte dell'handoff | Rafforzato da contratti e artefatti | Il percorso continua anche senza attivazione automatica della skill successiva |
| P11 | P1 | Separare stable, beta, candidate, package, installazione e runtime | Parzialmente soddisfatto | Documentazione e report mostrano stati coerenti e datati |
| P12 | P1 | Consolidare Content Core indipendentemente dai builder | `content-director` è presente e testato sinteticamente | Uso con manager reali e passaggio ai builder osservati |
| P13 | P1 | Usare confronti matched prima di claim di superiorità | Evidenza ancora limitata | Confronto su attività complete, materiali equivalenti e criteri congelati |
| P14 | P1 | Estendere i pilot con marketer reali | Una prima evidenza qualitativa sul Core iniziale | Pilot osservato sull'intero percorso con rework, comprensione e decisioni cambiate |
| P15 | P2 | Distinguere artefatti canonici, eval e file rigenerabili | Parzialmente soddisfatto | Struttura e manifest rendono evidente che cosa versionare o rigenerare |
| P16 | P0 | Trasformare le domande ad alta conseguenza in requisiti attivi | Principale gap del feedback reale | Prima dell'approvazione emergono mercato, periodo, obiettivi, clienti e risorse mancanti |
| P17 | P1 | Usare domande strutturate con `Altro` e `non ancora definito` | Pattern già utile dove applicato | Le opzioni non orientano la risposta e distinguono gap, fatto ignoto e decisione aperta |
| P18 | P1 | Chiudere il contratto operativo dei pacchetti | `INSTALL.md` aggiunti; coerenza da verificare per formato | Ogni pacchetto dichiara installazione, capacità incluse, escluse e passi successivi reali |

## Priorità recepite dalla review Claude sulla beta.10

### P19, allineare readiness, provenance e release

**Priorità: P0.** Accorpa i rilievi R1, R2 e la parte valida di R3.

Il README della provenance è rimasto alla beta.9 mentre l'allowlist usa la sorgente beta.10. Inoltre il report di readiness è una fotografia pre-package conservata nel tag pubblicato. Il commit sorgente `2bed5fb` è diverso dal commit del tag `5c5a39f` per una ragione legittima, ma la distinzione non è spiegata abbastanza bene a chi deve produrre una capture.

Prova di accettazione:

- le istruzioni citano versione e commit sorgente correnti;
- una capture costruita seguendo soltanto il README supera il controllo previsto;
- commit sorgente, commit di packaging e commit del tag sono distinti e spiegati;
- il report pre-package è datato e accompagnato da uno stato post-release oppure marcato chiaramente come storico;
- i digest delle skill restano la prova di identità del contenuto distribuito.

### P20, verificare installazione, attivazione e routing su Claude

**Priorità: P1.** Recepimento di R4.

La beta.10 distribuisce un pacchetto Claude, ma la matrice corrente registra `not_run` per Claude Code, Desktop e Cloud. Poiché il bundle Claude non include l'Assistant, il routing dipende dalle description e dal comportamento della piattaforma.

Prova di accettazione:

- installazione osservata del pacchetto esatto;
- richiesta naturale in italiano, senza nome tecnico della skill;
- attivazione corretta di almeno Setup, Strategy, Campaign e Content;
- percorso multi-turn con stato trasferito tra fasi;
- ripresa da file dopo nuova sessione o compattazione;
- distinzione tra skill presente, caricata e realmente attivata.

### P21, confrontare il sistema su un'attività completa

**Priorità: P1.** Rafforza P13 e P14 e recepisce R5.

Il confronto tra una risposta con skill e un prompt disciplinato è utile, ma non misura il vantaggio distintivo osservato della Suite. Il confronto principale deve coprire un'attività completa con interruzioni, revisioni e passaggi di stato.

Misure minime:

- informazioni perse o ricostruite;
- domande ripetute o mancate;
- correzioni richieste dal marketer;
- rispetto dei gate e delle autorizzazioni;
- tempo e turni fino a una decisione approvabile;
- qualità e riusabilità degli artefatti;
- capacità di riprendere dopo compattazione;
- utilità percepita e decisioni effettivamente cambiate.

La baseline deve essere un buon agente generalista con lo stesso materiale e non una risposta deliberatamente debole.

### P22, chiudere la regressione multi-turn di `design-campaign`

**Priorità: P2.** Recepimento circoscritto di R6.

La v0.1.3 ha già superato un test multi-turn su avanzamento per differenza e assenza di scritture canoniche. La v0.1.4 è stata riverificata soprattutto sulla prima risposta e sul linguaggio. Serve un solo dialogo completo sulla versione distribuita, non una riapertura dell'intera progettazione.

Prova di accettazione:

- nessuna riscrittura integrale del piano a ogni turno;
- revisione finale compatta;
- nessuna scrittura canonica in modalità test;
- linguaggio da marketer;
- approvazione del contenuto distinta dal salvataggio e dall'esecuzione.

### P23, chiudere i residui di manutenzione

**Priorità: P2.** Recepimento di R9.

Azioni proposte:

- chiudere la PR #3 ormai obsoleta rispetto a `setup-marketing-system` v0.3.2;
- aggiornare o archiviare [CAMPAIGN-CORE-STATUS.md](CAMPAIGN-CORE-STATUS.md);
- separare progressivamente in [MARKETING-AGENT-SYSTEM.md](MARKETING-AGENT-SYSTEM.md) architettura stabile, decision log e stato corrente;
- evitare che documenti storici vengano letti come istruzioni operative correnti.

### P24, misurare prima di comprimere le istruzioni

**Priorità: P2 sperimentale.** Recepimento prudente di R8.

La differenza di lunghezza tra le skill è reale, ma non dimostra un difetto. Non viene adottato un tetto universale di 1.200 parole. Si propone invece un test A/B sulla skill più lunga:

1. versione beta.10 corrente;
2. versione compressa del 20-30%;
3. stesse fixture nuove e stesso modello;
4. confronto su hard fail, domande, provenienza, gate, rework e lunghezza del dialogo.

La versione compressa sostituisce quella corrente soltanto se non perde comportamento utile.

## Rilievi Claude non trasformati in priorità

Non vengono adottati:

- un file `references/common.md` come nuova dipendenza runtime condivisa;
- un tetto universale di 1.200 parole per tutte le skill;
- la fusione automatica delle due skill di fondazione;
- l'obiettivo che le righe aggiunte alle skill superino quelle aggiunte ai checker.

La ripetizione di alcune invarianti nelle skill resta un trade-off intenzionale di portabilità. Il rischio da monitorare è la deriva delle regole, non la duplicazione in sé. Un meccanismo di generazione o controllo comune sarà valutato soltanto dopo un disallineamento reale e ripetuto.

## Roadmap aggiornata

### Fase 0, correggere i contratti pubblicati

- Eseguire P19.
- Chiudere gli elementi immediati di P23.
- Mantenere distinti sorgente, package, release, installazione e runtime.

### Fase 1, migliorare il dialogo decisionale

- Implementare P2, P16 e P17 sulle skill Setup e Strategy.
- Chiudere P22 con un dialogo completo di `design-campaign` v0.1.4.
- Conservare la progressione per differenza e la prima risposta utile.

### Fase 2, verificare la portabilità reale

- Eseguire P20 sulle superfici Claude pertinenti.
- Verificare che i passi successivi indicati esistano nel pacchetto caricato.
- Ripetere il percorso dopo nuova sessione o compattazione.

### Fase 3, validare l'utilità

- Eseguire P21 con almeno un marketer esterno.
- Usare una baseline generalista matched.
- Conservare separati esito tecnico, utilità percepita e risultato di business.
- Eseguire P24 soltanto come esperimento controllato.

## Criterio di successo complessivo

Una versione successiva dovrebbe essere promossa soltanto se dimostra contemporaneamente:

- percorso completo sul perimetro dichiarato e nel runtime corretto;
- nessuna decisione materiale inventata;
- domande attive sulle informazioni ad alta conseguenza;
- meno ripetizioni e meno rework rispetto alla baseline;
- continuità dopo ripresa o compattazione;
- comportamento comprensibile per un marketer;
- provenienza, readiness e istruzioni di release coerenti;
- portabilità osservata, non soltanto dedotta dai file;
- utilità verificata con persone reali, separata dai test sintetici.

La formulazione prudente resta: **beta.10 pubblicata e tecnicamente consolidata, con evidenze sintetiche e una prima esperienza qualitativa sul Core iniziale; comportamento cross-runtime e utilità end-to-end richiedono ancora validazione separata.**
