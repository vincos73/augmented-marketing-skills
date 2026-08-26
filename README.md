# Augmented Marketing Skills

Un framework di skill per aiutare manager e agenti AI a svolgere attività di marketing usando un contesto condiviso, regole approvate e decisioni verificabili.

Il progetto non vuole costruire un «CMO artificiale» né un catalogo di generatori per canale. L'obiettivo è rendere riutilizzabile il processo di lavoro di un marketer esperto: capire il contesto, distinguere fatti e ipotesi, decidere che cosa vale la pena fare, tradurre la decisione in un brief e controllare il risultato.

Il principio di base è semplice: ogni passaggio importante produce un documento persistente. Le informazioni non restano affidate alla memoria della chat e le skill successive possono leggere gli artefatti già approvati senza chiedere ogni volta le stesse cose.

## Come funziona il framework

```text
Business Identity
        ↓
Marketing Foundations
        ↓
Decisione strategica
        ↓
Marketing Mix: Product · Price · Place · Promotion
        ↓
Campaign Spec oppure Content Brief
        ↓
Asset prodotti dai builder specializzati
        ↓
Risultati e apprendimento
```

Il percorso non è obbligatoriamente lineare. Se obiettivo e formato sono già chiari, l'utente può usare direttamente un builder. Se invece manca il contesto necessario, l'agente deve segnalarlo prima di procedere.

## Esigenza, skill e output

| Esigenza dell'utente | Skill che la risolve | Output della skill | Stato |
| --- | --- | --- | --- |
| Fare in modo che l'agente conosca l'azienda o il brand prima di lavorarci | [`setup-business-context`](skills/setup-business-context/SKILL.md) | **Business Identity** verificabile e versionata: identità aziendale, identità di un brand autonomo oppure identità di un brand collegata all'azienda | **Approvata**, v0.6.2 |
| Definire le regole di marketing stabili che l'agente deve applicare in ogni attività aziendale | [`setup-marketing-system`](skills/setup-marketing-system/SKILL.md) | **Fondamenti di marketing** aziendali ed eventuali integrazioni di brand: regole su offerte e pubblici, messaggi e prove, ruolo dei canali, qualità e approvazioni | **Approvata**, v0.2.1 |
| Mettere a fuoco una sfida di marketing e scegliere come affrontarla | Strategy Core: `define-marketing-challenge`, `choose-marketing-direction` | Brief della sfida confermato e direzione approvata con diagnosi, stress test, trade-off, assunzione fragile e primo test utile | `define-marketing-challenge` approvata; `choose-marketing-direction` candidata v0.2.0 |
| Tradurre la direzione in scelte coerenti sulle quattro P | Strategy Core: `define-marketing-mix` | Marketing Mix approvato con Product, Price, Place e Promotion, dipendenze e autorità | **Candidata**, v0.1.0 |
| Trasformare la componente Promotion e le altre attivazioni pertinenti in una campagna coordinata | Campaign Core: `to-campaign-spec`, `campaign-review`, `learn-from-results` | Campaign Spec con messaggi, canali, asset, responsabilità, approvazioni e misure; review e apprendimento finale | **Roadmap** |
| Capire se un materiale merita di diventare un contenuto e quale formato usare | Content Core: `content-director` | Content Brief con obiettivo, pubblico, idea centrale, fonti, punti da verificare, formato e sequenza consigliata | **Roadmap** |
| Produrre il contenuto nel formato scelto | Builder specializzati, per esempio Carousel Builder e Quote Card Builder | Asset finale con i controlli editoriali, strutturali, visivi e tecnici specifici del formato | **Moduli esterni già esistenti**, non inclusi in questo repository |
| Costruire un sistema di ascolto su competitor, reputazione, normative o altri temi | `monitoring-setup` | Mappa delle fonti, query, frequenze, alert, configurazione, digest e runbook di manutenzione | **Ipotesi opzionale di roadmap** |

I nomi delle skill in roadmap descrivono il lavoro ancora da progettare. Non indicano componenti già approvati, installati o disponibili in questo repository.

## Che cosa esiste oggi

### `setup-business-context` v0.6.2

È una skill sorgente approvata. Costruisce una carta d'identità persistente partendo dalle fonti fornite dall'utente. Mantiene visibili provenienza, conflitti e aspetti ancora aperti; il template è modulare e al gate 1 permette di approvare lasciando aperti i punti non bloccanti oppure di approfondirli prima. Non inventa un posizionamento e non definisce la strategia.

Gli output canonici previsti sono:

- `.agents/company-identity.md` per un'azienda;
- `.agents/brand-identity.md` per un brand autonomo;
- `.agents/brands/<brand>.md` per un brand appartenente a un'azienda.

La sorgente e la copia locale attualmente installata sono alla versione v0.6.2. La [release pubblica stabile v0.6.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/v0.6.0) contiene lo ZIP della precedente versione pubblicata e il relativo checksum. Le istruzioni per l'installazione manuale sono in [`skills/setup-business-context/INSTALL.md`](skills/setup-business-context/INSTALL.md).

### `setup-marketing-system` v0.2.1

È una skill approvata del framework. Aiuta un responsabile marketing a ricostruire dai materiali reali le regole stabili che un agente deve seguire. Presenta presto una prima proposta utile, chiede soltanto decisioni mancanti con impatto reale e invita esplicitamente a caricare le fonti utili, come linee guida verbali o visuali, quando possono cambiare una regola stabile.

Produce un unico artefatto canonico, presentato nella lingua di lavoro del responsabile. In italiano il titolo è **Fondamenti di marketing**:

- `.agents/marketing/foundations.md` per la base aziendale o per un brand autonomo;
- `.agents/marketing/brands/<brand-slug>.md` per le sole differenze di un brand appartenente all'azienda.

La skill verifica prima che esista una Business Identity utilizzabile e la referenzia senza copiarla. Non definisce obiettivi trimestrali, budget, campagne o piani di canale temporanei. Non configura strumenti, non pubblica e non produce asset.

La [release stabile v0.2.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/setup-marketing-system-v0.2.1) contiene lo ZIP della sola skill e il relativo checksum. Le istruzioni per l'installazione manuale sono in [`skills/setup-marketing-system/INSTALL.md`](skills/setup-marketing-system/INSTALL.md).

### `define-marketing-challenge` v0.1.1

È una skill approvata dello Strategy Core. Aiuta il proprietario di una decisione a trasformare un obiettivo, problema, opportunità, segnale o proposta tattica in un **Brief della sfida di marketing** confermabile, senza scegliere ancora la direzione.

La skill legge Business Identity e Marketing Foundations pertinenti, produce una prima formulazione utile prima delle domande e mantiene distinti sintomo, causa presunta, tattica, vincolo e sfida. Budget, tempo e capacità entrano solo come limiti necessari a rendere realistico il confronto successivo; la skill non crea campagne, piani di spesa o asset.

La [release stabile v0.1.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/define-marketing-challenge-v0.1.1) contiene lo ZIP della sola skill e il relativo checksum. Il [catalogo degli eval](evals/define-marketing-challenge/eval-catalog.md) include una fixture sintetica a due turni, un forward test e una regressione per i brief cliente ricevuti dalle agenzie. Il primo forward test indipendente su `v0.1.0` non ha rilevato hard fail e ha prodotto due correzioni compatibili confluite in `v0.1.1`; il [retest indipendente](evals/define-marketing-challenge/runs/2026-08-26-independent-retest-v0.1.1.md) della versione corretta è passato senza errori sostanziali.

### Candidate dello Strategy Core

`choose-marketing-direction` v0.2.0 formula una diagnosi strategica provvisoria e confronta alternative realmente strategiche rispetto a una sfida confermata. Distingue osservazioni, interpretazioni e ipotesi causali; stressa condizioni, capacità, reazioni e conseguenze; raccomanda anche in forma condizionata o può concludere che nessuna opzione sia pronta. Produce la bozza di `direction.md`, con non-scelte, assunzione più fragile, primo test utile e condizioni di riapertura, ma non definisce ancora le quattro P e non autorizza l'esecuzione.

`define-marketing-mix` v0.1.0 traduce una direzione approvata in Product, Price, Place e Promotion. Ogni P viene classificata come vincolo, scelta, proposta, ipotesi, decisione esterna o non applicabile. La skill controlla la coerenza del sistema senza trasformare Product in roadmap tecnica, Price in una decisione finanziaria unilaterale, Place in un elenco di media o Promotion in un campaign plan.

Le due sorgenti, i template e i cataloghi di eval sono presenti per l'authoring, ma non sono ancora approvati, installati né pubblicati. Prima di una release richiedono fixture realistiche e forward test indipendenti.

## Regole comuni alle skill di setup

- Le fonti e la provenienza restano visibili.
- Fatti, inferenze, assunzioni, conflitti e incognite non vengono confusi.
- La prima risposta utile arriva prima di un eventuale approfondimento e contiene al massimo tre domande decisive.
- Una proposta dell'agente non diventa una regola aziendale senza approvazione esplicita.
- Approvazione del contenuto, scrittura canonica, installazione locale e pubblicazione sono gate distinti.
- L'onboarding deve poter essere completato interamente in chat. Una vista interattiva può aiutare la revisione, ma non conserva lo stato e non raccoglie approvazioni canoniche.
- Durante gli eval non vengono scritti artefatti canonici né modificati i file di istruzioni dell'agente.

## Stato del progetto

| Componente | Stato attuale |
| --- | --- |
| `setup-business-context` | approvata; sorgente e installazione locale v0.6.2; release pubblica stabile v0.6.0 |
| `setup-marketing-system` | approvata e disponibile come release stabile v0.2.1 |
| Strategy Core | `define-marketing-challenge` v0.1.1 approvata e disponibile come release stabile; `choose-marketing-direction` candidata v0.2.0 e `define-marketing-mix` candidata v0.1.0 con sorgenti ed eval catalog; evidence pack autonomo opzionale e rinviato |
| Campaign Core | roadmap; riceverà il marketing mix approvato e nessuna skill è ancora inclusa |
| Content Core | roadmap; collegamento con builder esterni ancora da validare |
| `monitoring-setup` | ipotesi opzionale; non inclusa |

La presenza di una cartella sotto `skills/` prova soltanto che esiste una sorgente di authoring. Non dimostra che la skill sia approvata, installata o attiva nell'ambiente dell'utente.

Il documento autorevole con architettura, decisioni, confini ed eval è [`MARKETING-AGENT-SYSTEM.md`](MARKETING-AGENT-SYSTEM.md).

## Struttura del repository

```text
skills/                         sorgenti delle skill
  setup-business-context/       skill approvata
  setup-marketing-system/       skill approvata
  define-marketing-challenge/   skill approvata
  choose-marketing-direction/   candidata Strategy Core
  define-marketing-mix/         candidata Strategy Core
evals/                          cataloghi, fixture sintetiche e risultati osservati
experiments/                    prove non incluse nelle skill attive
MARKETING-AGENT-SYSTEM.md       framework e decisioni autorevoli
```

Il repository è privato. Le fixture versionate sono sintetiche e pubblicabili; materiali reali di clienti, contatti, prezzi, note interne e risultati sensibili devono restare fuori dal repository finché non vengono sanificati e approvati separatamente.
