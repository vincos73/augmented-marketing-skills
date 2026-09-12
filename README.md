
# Augmented Marketing Suite

> Un insieme di skill per aiutarti a prendere decisioni di marketing più chiare, verificabili e approvabili con un agente IA.

Se usi ChatGPT, Codex o un altro ambiente compatibile, puoi chiedere all'agente di aiutarti a capire un problema di marketing, confrontare alcune strade e preparare il passo successivo.

Non devi conoscere il metodo o i nomi tecnici per iniziare. Puoi descrivere il bisogno con parole tue.

<img width="1800" height="1200" alt="AMS-framework-1" src="https://github.com/user-attachments/assets/2469268c-85b4-42d4-9eb1-fe8d8481b34a" />

## Che cos'è una skill?

Una skill è un insieme di istruzioni specializzate che l'agente può usare quando serve. In questo progetto ogni skill ha un compito preciso e produce un documento che puoi leggere, correggere e approvare.

Qui per agente IA intendiamo l'assistente con cui lavori, per esempio ChatGPT o Codex, quando l'ambiente consente di installare queste istruzioni.

La Suite non è un direttore marketing automatico e non decide al posto tuo. Ti aiuta a rendere più ordinato e ricostruibile il percorso che porta a una decisione.

Chi contribuisce nuove skill trova i criteri comuni nello [standard di progettazione](STANDARD-PROGETTAZIONE-SKILL.md): risposte proporzionate, dialogo per differenza, fonti separate dai materiali metodologici, gate compatti e test senza scritture canoniche.

## Versione pubblicata: beta.11

La [beta.11](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.11) aggiunge **`setup-brand-voice`** per definire o rivedere una voce riutilizzabile e **`write-marketing-copy`** per scrivere, riscrivere o adattare un testo marketing. La Suite comprende ora undici skill specialistiche, più l’Assistant nel plugin OpenAI/Codex.

Tutte le dodici skill sono state riviste secondo le linee guida Astra fornite: descrizioni mirate, istruzioni essenziali, riferimenti consultati quando pertinenti e riuso delle autorizzazioni già date. [Rapporto, versioni e limiti della verifica](SUITE-REVIEW-BETA11.md).

Gli archivi, i checksum e il manifest sono allegati alla release. La pubblicazione non dimostra installazione locale, caricamento in una sessione o validazione con marketer reali.

## Da dove cominciare

### Skill pubblicate nella Suite beta.11

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni |
| --- | --- | --- |
| Non sai da quale passaggio iniziare. | [`Augmented Marketing Assistant`](agents/augmented-marketing-assistant.md) | Un orientamento in linguaggio comune verso il passaggio più utile. |
| Vuoi spiegare all'agente chi è la tua organizzazione. | [`setup-business-context`](skills/setup-business-context/) | Un contesto riutilizzabile con identità, fatti approvati, vincoli e aspetti ancora da chiarire. |
| Vuoi definire le regole con cui fare marketing. | [`setup-marketing-system`](skills/setup-marketing-system/) | Fondamenti di marketing condivisi, con fonti, regole, limiti e responsabilità da chiarire. |
| Vuoi definire o rivedere una voce riutilizzabile. | [`setup-brand-voice`](skills/setup-brand-voice/) | Una guida alla voce del brand o una revisione circoscritta. |
| Hai un'idea, una richiesta o un problema, ma non sai se è davvero una sfida di marketing. | [`define-marketing-challenge`](skills/define-marketing-challenge/) | Un documento di sintesi che chiarisce problema, pubblico, cambiamento desiderato, evidenze e criteri di successo. |
| Devi scegliere tra più strade possibili. | [`choose-marketing-direction`](skills/choose-marketing-direction/) | Un confronto tra alternative, con vantaggi, svantaggi, rischi e assunzioni espliciti. |
| Hai scelto una direzione e devi renderla concreta. | [`define-marketing-mix`](skills/define-marketing-mix/) | Scelte coerenti su offerta, prezzo, distribuzione e comunicazione. |
| Hai un testo marketing da scrivere, riscrivere o adattare. | [`write-marketing-copy`](skills/write-marketing-copy/) | Copy pronto per la revisione, basato su voce e fatti disponibili. |

I nomi tra parentesi sono quelli da usare per richiamare direttamente le skill. Se l'ambiente supporta l'Assistant, puoi invece descrivere semplicemente ciò che vuoi fare.

### Campaign Core: incluso nella beta.11

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni | Stato |
| --- | --- | --- | --- |
| Vuoi progettare una campagna partendo da un'esigenza, un brief o un marketing mix. | [`design-campaign`](skills/design-campaign/) | Una Campaign Spec con percorso, messaggi, canali, asset, responsabilità e misurazione. | v0.1.7 inclusa nella beta.11 |
| Vuoi verificare una campagna prima della pubblicazione o dell'invio. | [`campaign-review`](skills/campaign-review/) | Una review separata di coerenza strategica, affermazioni, prontezza operativa e baseline decisionale per il debrief. | v0.1.4 inclusa nella beta.11 |
| Devi leggere i risultati e decidere che cosa fare dopo. | [`campaign-debrief`](skills/campaign-debrief/) | Una lettura dei risultati con limiti, decisione consigliata e prossima verifica. | v0.1.7 inclusa nella beta.11 |

Le tre skill completano la sequenza del Campaign Core. La beta.11 mantiene la verifica end-to-end controllata sulla fixture sintetica Fabriloom come evidenza storica e aggiunge una revisione delle istruzioni per Astra. La pubblicazione non dimostra validazione con marketer reali o funzionamento identico in ogni runtime.

### Content Core: incluso nella beta.11

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni | Stato |
| --- | --- | --- | --- |
| Hai fonti o un'idea, ma non sai quale singolo contenuto sarebbe più utile. | [`content-director`](skills/content-director/) | Una raccomandazione editoriale agnostica e, dopo approvazione, un Content Brief. | v0.1.2 inclusa nella beta.11 |

## Il percorso, in parole semplici

```text
Prima capisci il contesto
          ↓
Poi chiarisci la sfida
          ↓
Confronti le alternative
          ↓
Scegli una direzione
          ↓
Definisci offerta, prezzo, distribuzione e comunicazione
          ↓
Progetti e verifichi la campagna
          ↓
Dopo i risultati decidi il passo successivo
```

Puoi usare tutto il percorso oppure solo il passaggio che ti serve. Le skill non pubblicano contenuti, non fanno pubblicità a pagamento e non cambiano strumenti o account esterni senza un'autorizzazione distinta.

## Perché può essere utile

Un agente IA può produrre rapidamente analisi, idee e testi. La velocità, però, non basta per prendere una buona decisione. Prima bisogna capire se il problema è quello giusto, quali informazioni sono affidabili e quali scelte sono ancora aperte.

La Suite aiuta a:

- separare fonti, fatti, inferenze, ipotesi e informazioni mancanti;
- non trasformare automaticamente una richiesta tattica in una soluzione;
- confrontare alternative prima di sceglierne una;
- mantenere visibili vincoli, rischi, responsabilità e approvazioni;
- lasciare documenti riutilizzabili invece di affidare tutto alla memoria della chat.

## Un esempio

Immagina di voler proporre un nuovo servizio di formazione.

1. Spieghi all'agente che cosa fa l'organizzazione, per chi lavora e quali informazioni sono già confermate.
2. Chiarisci quale cambiamento vuoi ottenere e quale problema vuoi risolvere.
3. Confronti, per esempio, un percorso breve, un laboratorio periodico e un servizio più strutturato.
4. Scegli una direzione, rendendo esplicite le ipotesi ancora da verificare.
5. Definisci in modo coerente l'offerta, il prezzo, il modo di accesso e la comunicazione.

Solo dopo puoi passare a pagine, campagne e contenuti. La beta.11 include il Campaign Core completo, `content-director`, `setup-brand-voice` e `write-marketing-copy`. Research & Evidence e monitoring restano sviluppi successivi da validare.

## Stato della roadmap

| Area | Stato attuale | Prossimo passaggio |
| --- | --- | --- |
| Fondazione e Strategy Core | Pubblicati nella Suite beta.11 con istruzioni aggiornate | Osservare utilizzo e riuso con marketer reali |
| Campaign Core | Tre skill incluse nella Suite beta.11; run integrato precedente su nove skill PASS su Codex Desktop | Svolgere un pilot con un responsabile reale e rinnovare le prove sugli altri runtime |
| Brand voice e copy | `setup-brand-voice` e `write-marketing-copy` incluse nella beta.11 | Verificare l'utilità su materiali di brand reali |
| Content Core | `content-director` v0.1.2 inclusa nella Suite beta.11 | Collegare il Content Brief ai builder specializzati e provarlo con manager reali |
| Research & Evidence | Roadmap opzionale | Aggiungere capacità autonome solo quando emerge un uso ripetuto |
| Monitoring | Roadmap opzionale | Validare il bisogno prima di introdurre setup e automazioni dedicate |

## Versioni incluse nella beta.11

La [release beta.11](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.11) contiene le versioni sotto. La beta.10 e le release singole precedenti restano riferimenti storici verificati.

| Skill | Versione inclusa nella Suite beta.11 | Risultato principale |
| --- | --- | --- | --- |
| [`Augmented Marketing Assistant`](skills/augmented-marketing-assistant/) | v0.2.1, solo OpenAI/Codex | Orientamento verso il passaggio pertinente. |
| [`setup-business-context`](skills/setup-business-context/) | v0.6.7 | Contesto identitario riutilizzabile. |
| [`setup-marketing-system`](skills/setup-marketing-system/) | v0.3.4 | Fondamenti e regole di marketing condivisi. |
| [`setup-brand-voice`](skills/setup-brand-voice/) | v0.1.2 | Guida alla voce del brand o revisione circoscritta. |
| [`define-marketing-challenge`](skills/define-marketing-challenge/) | v0.1.8 | Documento sintetico e verificabile della sfida. |
| [`choose-marketing-direction`](skills/choose-marketing-direction/) | v0.2.8 | Confronto e scelta della direzione. |
| [`define-marketing-mix`](skills/define-marketing-mix/) | v0.1.9 | Marketing mix su offerta, prezzo, distribuzione e comunicazione. |
| [`design-campaign`](skills/design-campaign/) | v0.1.7 | Campaign Spec approvabile. |
| [`campaign-review`](skills/campaign-review/) | v0.1.4 | Review pre-lancio separata con baseline decisionale per il debrief. |
| [`campaign-debrief`](skills/campaign-debrief/) | v0.1.7 | Lettura dei risultati e decisione successiva. |
| [`content-director`](skills/content-director/) | v0.1.2 | Raccomandazione editoriale e Content Brief. |
| [`write-marketing-copy`](skills/write-marketing-copy/) | v0.1.5 | Copy marketing pronto per revisione. |

## Cosa non devi aspettarti

- L'agente non inventa fatti per riempire i vuoti: segnala ciò che manca o che deve essere verificato.
- Una proposta non diventa automaticamente una decisione approvata.
- L'approvazione di un documento non autorizza pubblicazioni, acquisti media o altre azioni esterne.
- La Suite non sostituisce la responsabilità di chi conosce l'organizzazione e deve approvare le scelte.

## Installazione

La regola è semplice: **per una skill singola usa uno ZIP portabile; per tutte le skill usa il plugin dedicato alla piattaforma**. Non caricare mai il bundle OpenAI/Codex in Claude, né il bundle Claude in ChatGPT/Codex.

| Ambiente | Una skill | Tutte le skill |
| --- | --- | --- |
| Claude | Uno ZIP in `dist/beta.11/agent-skills/` | `dist/beta.11/claude/augmented-marketing-suite-claude-v0.1.0-beta.11.zip` in **Personalizza → Plugin** |
| ChatGPT | Uno ZIP in `dist/beta.11/agent-skills/` nel flusso Skills | `dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip` nel flusso Plugin |
| Codex | Uno ZIP in `dist/beta.11/agent-skills/` quando il flusso locale lo consente | `dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip` nel marketplace o catalogo Plugin |

### Per Claude o ChatGPT: una skill alla volta

La beta.11 offre un archivio ZIP per ciascuna delle undici skill specialistiche in [`dist/beta.11/agent-skills/`](dist/beta.11/agent-skills/). Ogni archivio contiene una sola cartella radice con `SKILL.md` e i riferimenti necessari: è il formato più semplice per il caricamento diretto di una skill compatibile con Agent Skills.

Scegli la skill che ti serve, caricala con il meccanismo di skill del tuo ambiente e avvia una nuova chat. Claude non usa l'Assistant incluso nella Suite OpenAI, quindi gli archivi portabili contengono soltanto le undici skill specialistiche.

### Per Claude: Suite completa con un solo upload

Carica [`dist/beta.11/claude/augmented-marketing-suite-claude-v0.1.0-beta.11.zip`](dist/beta.11/claude/augmented-marketing-suite-claude-v0.1.0-beta.11.zip) nella sezione **Personalizza → Plugin** di Claude. È un plugin Claude dedicato: ha `.claude-plugin/plugin.json` e include le undici skill specialistiche, senza Augmented Marketing Assistant.

### Per ChatGPT e Codex: Suite completa con un solo upload

La beta.11 offre anche [`dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip`](dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip), con il manifesto `.codex-plugin`, undici skill specialistiche e Augmented Marketing Assistant. Segui le istruzioni di [`INSTALLAZIONE.md`](INSTALLAZIONE.md).

> Allegare uno ZIP a una chat normale consente di leggerlo, ma non registra automaticamente un plugin o una skill. Usa soltanto il flusso di installazione disponibile nel tuo account o workspace.

### Installare una versione pubblicata

Per una release già pubblicata, scarica la skill desiderata, estraila e segui il file `INSTALL.md` incluso nella cartella. Mantieni l'intera cartella, compresi istruzioni, riferimenti ed eventuali controlli.

| Skill | Versione pubblicata da installare |
| --- | --- |
| `setup-business-context` | Suite beta.11: `v0.6.7` |
| `setup-marketing-system` | Suite beta.11: `v0.3.4` |
| `setup-brand-voice` | Suite beta.11: `v0.1.2` |
| `define-marketing-challenge` | Suite beta.11: `v0.1.8` |
| `choose-marketing-direction` | Suite beta.11: `v0.2.8` |
| `define-marketing-mix` | Suite beta.11: `v0.1.9` |
| `design-campaign` | Suite beta.11: `v0.1.7` |
| `campaign-review` | Suite beta.11: `v0.1.4` |
| `campaign-debrief` | Suite beta.11: `v0.1.7` |
| `content-director` | Suite beta.11: `v0.1.2` |
| `write-marketing-copy` | Suite beta.11: `v0.1.5` |

Scegliere una versione pubblicata precisa evita di installare involontariamente una versione ancora in sviluppo. In Codex, la destinazione abituale è `~/.codex/skills/`, ma il percorso può cambiare in base all'ambiente.

## Per chi vuole approfondire

- [Installazione dettagliata](INSTALLAZIONE.md)
- [Contratto di portabilità](PORTABILITA.md)
- [Architettura e confini del sistema](MARKETING-AGENT-SYSTEM.md)

## Contribuire

Il repository accoglie contributi su istruzioni, template, controlli ed esempi sintetici. Non includere dati di clienti, casi reali riservati o informazioni personali.
