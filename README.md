
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

## Da dove cominciare

### Skill pubblicate nella Suite beta.10

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni |
| --- | --- | --- |
| Non sai da quale passaggio iniziare. | [`Augmented Marketing Assistant`](agents/augmented-marketing-assistant.md) | Un orientamento in linguaggio comune verso il passaggio più utile. |
| Vuoi spiegare all'agente chi è la tua organizzazione. | [`setup-business-context`](skills/setup-business-context/) | Un contesto riutilizzabile con identità, fatti approvati, vincoli e aspetti ancora da chiarire. |
| Vuoi definire le regole con cui fare marketing. | [`setup-marketing-system`](skills/setup-marketing-system/) | Fondamenti di marketing condivisi, con fonti, regole, limiti e responsabilità da chiarire. |
| Hai un'idea, una richiesta o un problema, ma non sai se è davvero una sfida di marketing. | [`define-marketing-challenge`](skills/define-marketing-challenge/) | Un documento di sintesi che chiarisce problema, pubblico, cambiamento desiderato, evidenze e criteri di successo. |
| Devi scegliere tra più strade possibili. | [`choose-marketing-direction`](skills/choose-marketing-direction/) | Un confronto tra alternative, con vantaggi, svantaggi, rischi e assunzioni espliciti. |
| Hai scelto una direzione e devi renderla concreta. | [`define-marketing-mix`](skills/define-marketing-mix/) | Scelte coerenti su offerta, prezzo, distribuzione e comunicazione. |

I nomi tra parentesi sono quelli da usare per richiamare direttamente le skill. Se l'ambiente supporta l'Assistant, puoi invece descrivere semplicemente ciò che vuoi fare.

### Campaign Core: incluso nella beta.10

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni | Stato |
| --- | --- | --- | --- |
| Vuoi progettare una campagna partendo da un'esigenza, un brief o un marketing mix. | [`design-campaign`](skills/design-campaign/) | Una Campaign Spec con percorso, messaggi, canali, asset, responsabilità e misurazione. | v0.1.4 inclusa nella beta.10 |
| Vuoi verificare una campagna prima della pubblicazione o dell'invio. | [`campaign-review`](skills/campaign-review/) | Una review separata di coerenza strategica, affermazioni, prontezza operativa e baseline decisionale per il debrief. | v0.1.3 inclusa nella beta.10 |
| Devi leggere i risultati e decidere che cosa fare dopo. | [`campaign-debrief`](skills/campaign-debrief/) | Una lettura dei risultati con limiti, decisione consigliata e prossima verifica. | v0.1.6 inclusa nella beta.10 |

Le tre skill completano la sequenza del Campaign Core. La beta.10 aggiunge `campaign-review` v0.1.3 e una suite di robustezza pubblicabile; la verifica end-to-end controllata sulla fixture sintetica Fabriloom è PASS. La pubblicazione non dimostra validazione con marketer reali o funzionamento identico in ogni runtime.

### Content Core: incluso nella beta.10

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni | Stato |
| --- | --- | --- | --- |
| Hai fonti o un'idea, ma non sai quale singolo contenuto sarebbe più utile. | [`content-director`](skills/content-director/) | Una raccomandazione editoriale agnostica e, dopo approvazione, un Content Brief. | v0.1.1 inclusa nella beta.10 e disponibile come [release singola stabile](https://github.com/vincos73/augmented-marketing-skills/releases/tag/content-director-v0.1.1) |

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

Solo dopo puoi passare a pagine, campagne e contenuti. La beta.10 include il Campaign Core completo con `design-campaign`, `campaign-review` e `campaign-debrief`, oltre a `content-director` per scegliere la strada editoriale di un singolo contenuto. Research & Evidence e monitoring restano sviluppi successivi da validare.

## Stato della roadmap

| Area | Stato attuale | Prossimo passaggio |
| --- | --- | --- |
| Fondazione e Strategy Core | Pubblicati nella Suite beta.10 con le revisioni sorgente più recenti | Osservare utilizzo e riuso con marketer reali |
| Campaign Core | Tre skill incluse nella Suite beta.10; run integrato controllato a nove skill PASS su Codex Desktop | Svolgere un pilot con un responsabile reale e rinnovare le prove sugli altri runtime |
| Content Core | `content-director` v0.1.1 inclusa nella Suite beta.10 e pubblicata singolarmente | Collegare il Content Brief ai builder specializzati e provarlo con manager reali |
| Research & Evidence | Roadmap opzionale | Aggiungere capacità autonome solo quando emerge un uso ripetuto |
| Monitoring | Roadmap opzionale | Validare il bisogno prima di introdurre setup e automazioni dedicate |

## Versioni della Suite e release singole

La [release della Suite beta.10](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.10) porta nei pacchetti le versioni sorgente correnti su `main`. Le release singole precedenti restano disponibili come riferimenti storici verificati.

| Skill | Versione sorgente su `main` | Versione inclusa nella Suite beta.10 | Risultato principale |
| --- | --- | --- | --- |
| [`Augmented Marketing Assistant`](skills/augmented-marketing-assistant/) | v0.2.0 | v0.2.0, solo OpenAI/Codex | Orientamento verso il passaggio pertinente. |
| [`setup-business-context`](skills/setup-business-context/) | v0.6.5 | v0.6.5 | Contesto identitario riutilizzabile. |
| [`setup-marketing-system`](skills/setup-marketing-system/) | v0.3.2 | v0.3.2 | Fondamenti e regole di marketing condivisi. |
| [`define-marketing-challenge`](skills/define-marketing-challenge/) | v0.1.4 | v0.1.4 | Documento sintetico e verificabile della sfida. |
| [`choose-marketing-direction`](skills/choose-marketing-direction/) | v0.2.3 | v0.2.3 | Confronto e scelta della direzione. |
| [`define-marketing-mix`](skills/define-marketing-mix/) | v0.1.4 | v0.1.4 | Marketing mix su offerta, prezzo, distribuzione e comunicazione. |
| [`design-campaign`](skills/design-campaign/) | v0.1.4 | v0.1.4 | Campaign Spec approvabile. |
| [`campaign-review`](skills/campaign-review/) | v0.1.3 | v0.1.3 | Review pre-lancio separata con baseline decisionale per il debrief. |
| [`campaign-debrief`](skills/campaign-debrief/) | v0.1.6 | v0.1.6 | Lettura dei risultati e decisione successiva. |
| [`content-director`](skills/content-director/) | v0.1.1 | v0.1.1 | Raccomandazione editoriale e Content Brief. |

## Cosa non devi aspettarti

- L'agente non inventa fatti per riempire i vuoti: segnala ciò che manca o che deve essere verificato.
- Una proposta non diventa automaticamente una decisione approvata.
- L'approvazione di un documento non autorizza pubblicazioni, acquisti media o altre azioni esterne.
- La Suite non sostituisce la responsabilità di chi conosce l'organizzazione e deve approvare le scelte.

## Installazione

La regola è semplice: **per una skill singola usa uno ZIP portabile; per tutte le skill usa il plugin dedicato alla piattaforma**. Non caricare mai il bundle OpenAI/Codex in Claude, né il bundle Claude in ChatGPT/Codex.

| Ambiente | Una skill | Tutte le skill |
| --- | --- | --- |
| Claude | Uno ZIP in `dist/agent-skills/` | `dist/claude/augmented-marketing-suite-claude-v0.1.0-beta.10.zip` in **Personalizza → Plugin** |
| ChatGPT | Uno ZIP in `dist/agent-skills/` nel flusso Skills | `dist/openai/augmented-marketing-suite-0.1.0-beta.10.zip` nel flusso Plugin |
| Codex | Uno ZIP in `dist/agent-skills/` quando il flusso locale lo consente | `dist/openai/augmented-marketing-suite-0.1.0-beta.10.zip` nel marketplace o catalogo Plugin |

### Per Claude o ChatGPT: una skill alla volta

La beta.10 pubblicata offre un archivio ZIP per ciascuna delle nove skill specialistiche in [`dist/agent-skills/`](dist/agent-skills/). Ogni archivio contiene una sola cartella radice con `SKILL.md` e i riferimenti necessari: è il formato più semplice per il caricamento diretto di una skill compatibile con Agent Skills.

Scegli la skill che ti serve, caricala con il meccanismo di skill del tuo ambiente e avvia una nuova chat. Claude non usa l'Assistant incluso nella Suite OpenAI, quindi gli archivi portabili contengono soltanto le nove skill specialistiche.

### Per Claude: Suite completa con un solo upload

Carica [`dist/claude/augmented-marketing-suite-claude-v0.1.0-beta.10.zip`](dist/claude/augmented-marketing-suite-claude-v0.1.0-beta.10.zip) nella sezione **Personalizza → Plugin** di Claude. È un plugin Claude dedicato: ha `.claude-plugin/plugin.json` e include le nove skill specialistiche, senza Augmented Marketing Assistant.

### Per ChatGPT e Codex: Suite completa con un solo upload

La beta.10 pubblicata offre anche [`dist/openai/augmented-marketing-suite-0.1.0-beta.10.zip`](dist/openai/augmented-marketing-suite-0.1.0-beta.10.zip), con il manifesto `.codex-plugin`, nove skill specialistiche e Augmented Marketing Assistant. Segui le istruzioni di [`INSTALLAZIONE.md`](INSTALLAZIONE.md).

> Allegare uno ZIP a una chat normale consente di leggerlo, ma non registra automaticamente un plugin o una skill. Usa soltanto il flusso di installazione disponibile nel tuo account o workspace.

### Installare una versione pubblicata

Per una release già pubblicata, scarica la skill desiderata, estraila e segui il file `INSTALL.md` incluso nella cartella. Mantieni l'intera cartella, compresi istruzioni, riferimenti ed eventuali controlli.

| Skill | Versione pubblicata da installare |
| --- | --- |
| `setup-business-context` | Suite beta.10: `v0.6.5` |
| `setup-marketing-system` | Suite beta.10: `v0.3.2` |
| `define-marketing-challenge` | Suite beta.10: `v0.1.4` |
| `choose-marketing-direction` | Suite beta.10: `v0.2.3` |
| `define-marketing-mix` | Suite beta.10: `v0.1.4` |
| `design-campaign` | Suite beta.10: `v0.1.4` |
| `campaign-review` | Suite beta.10: `v0.1.3` |
| `campaign-debrief` | Suite beta.10: `v0.1.6` |
| `content-director` | Suite beta.10: `v0.1.1` |

Scegliere una versione pubblicata precisa evita di installare involontariamente una versione ancora in sviluppo. In Codex, la destinazione abituale è `~/.codex/skills/`, ma il percorso può cambiare in base all'ambiente.

## Per chi vuole approfondire

- [Installazione dettagliata](INSTALLAZIONE.md)
- [Contratto di portabilità](PORTABILITA.md)
- [Architettura e confini del sistema](MARKETING-AGENT-SYSTEM.md)

## Contribuire

Il repository accoglie contributi su istruzioni, template, controlli ed esempi sintetici. Non includere dati di clienti, casi reali riservati o informazioni personali.
