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
| Fare in modo che l'agente conosca l'azienda o il brand prima di lavorarci | [`setup-business-context`](skills/setup-business-context/SKILL.md) | **Business Identity** verificabile e versionata: identità aziendale, identità di un brand autonomo oppure identità di un brand collegata all'azienda | **Approvata**, v0.5.0 |
| Definire le regole di marketing stabili che l'agente deve applicare in ogni attività aziendale | [`setup-marketing-system`](skills/setup-marketing-system/SKILL.md) | **Marketing Foundations** aziendali ed eventuali overlay di brand: regole su offerte e pubblici, messaggi e prove, ruolo dei canali, qualità e approvazioni | **Candidata**, v0.1.0 |
| Chiarire il problema da affrontare e scegliere quale opportunità o ipotesi testare | Strategy Core: `challenge-brief`, `build-evidence-pack`, `choose-marketing-bet` | Brief del problema, evidenze distinte dalle assunzioni e decisione di marketing approvata con il relativo test | **Roadmap** |
| Trasformare una decisione approvata in una campagna coordinata | Campaign Core: `to-campaign-spec`, `campaign-review`, `learn-from-results` | Campaign Spec con messaggi, canali, asset, responsabilità, approvazioni e misure; review e apprendimento finale | **Roadmap** |
| Capire se un materiale merita di diventare un contenuto e quale formato usare | Content Core: `content-director` | Content Brief con obiettivo, pubblico, idea centrale, fonti, punti da verificare, formato e sequenza consigliata | **Roadmap** |
| Produrre il contenuto nel formato scelto | Builder specializzati, per esempio Carousel Builder e Quote Card Builder | Asset finale con i controlli editoriali, strutturali, visivi e tecnici specifici del formato | **Moduli esterni già esistenti**, non inclusi in questo repository |
| Costruire un sistema di ascolto su competitor, reputazione, normative o altri temi | `monitoring-setup` | Mappa delle fonti, query, frequenze, alert, configurazione, digest e runbook di manutenzione | **Ipotesi opzionale di roadmap** |

I nomi delle skill in roadmap descrivono il lavoro ancora da progettare. Non indicano componenti già approvati, installati o disponibili in questo repository.

## Che cosa esiste oggi

### `setup-business-context` v0.5.0

È l'unica skill sorgente approvata. Costruisce una carta d'identità persistente partendo dalle fonti fornite dall'utente. Mantiene visibili provenienza, conflitti e informazioni mancanti; non inventa un posizionamento e non definisce la strategia.

Gli output canonici previsti sono:

- `.agents/company-identity.md` per un'azienda;
- `.agents/brand-identity.md` per un brand autonomo;
- `.agents/brands/<brand>.md` per un brand appartenente a un'azienda.

La [release stabile v0.5.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/v0.5.0) contiene lo ZIP della sola skill e il relativo checksum. Le istruzioni per l'installazione manuale sono in [`skills/setup-business-context/INSTALL.md`](skills/setup-business-context/INSTALL.md).

### `setup-marketing-system` v0.1.0

È il prossimo incremento del framework ed è ancora una candidata in valutazione. Aiuta un responsabile marketing a ricostruire dai materiali reali le regole stabili che un agente deve seguire. Presenta presto una prima proposta utile e chiede soltanto le decisioni mancanti che hanno un impatto reale.

Produce un unico artefatto in inglese chiamato **Marketing Foundations**:

- `.agents/marketing/foundations.md` per la base aziendale o per un brand autonomo;
- `.agents/marketing/brands/<brand-slug>.md` per le sole differenze di un brand appartenente all'azienda.

La skill verifica prima che esista una Business Identity utilizzabile e la referenzia senza copiarla. Non definisce obiettivi trimestrali, budget, campagne o piani di canale temporanei. Non configura strumenti, non pubblica e non produce asset.

La [pre-release v0.1.0-rc.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/setup-marketing-system-v0.1.0-rc.1) serve per revisione ed eval. Non equivale all'approvazione della skill e non la installa automaticamente.

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
| `setup-business-context` | approvata e disponibile come release stabile v0.5.0 |
| `setup-marketing-system` | sorgente candidata v0.1.0, con fixture sintetiche, eval e pre-release rc.1 |
| Strategy Core | architettura e confini definiti; skill non ancora progettate o approvate |
| Campaign Core | roadmap; nessuna skill inclusa |
| Content Core | roadmap; collegamento con builder esterni ancora da validare |
| `monitoring-setup` | ipotesi opzionale; non inclusa |

La presenza di una cartella sotto `skills/` prova soltanto che esiste una sorgente di authoring. Non dimostra che la skill sia approvata, installata o attiva nell'ambiente dell'utente.

Il documento autorevole con architettura, decisioni, confini ed eval è [`MARKETING-AGENT-SYSTEM.md`](MARKETING-AGENT-SYSTEM.md).

## Struttura del repository

```text
skills/                         sorgenti delle skill
  setup-business-context/       skill approvata
  setup-marketing-system/       candidata in valutazione
evals/                          cataloghi, fixture sintetiche e risultati osservati
experiments/                    prove non incluse nelle skill attive
MARKETING-AGENT-SYSTEM.md       framework e decisioni autorevoli
```

Il repository è privato. Le fixture versionate sono sintetiche e pubblicabili; materiali reali di clienti, contatti, prezzi, note interne e risultati sensibili devono restare fuori dal repository finché non vengono sanificati e approvati separatamente.
