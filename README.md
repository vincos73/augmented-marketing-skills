
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

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni |
| --- | --- | --- |
| Non sai da quale passaggio iniziare. | [`Augmented Marketing Assistant`](agents/augmented-marketing-assistant.md) | Un orientamento in linguaggio comune verso il passaggio più utile. |
| Vuoi spiegare all'agente chi è la tua organizzazione. | [`setup-business-context`](skills/setup-business-context/) | Un contesto riutilizzabile con identità, fatti approvati, vincoli e aspetti ancora da chiarire. |
| Vuoi definire le regole con cui fare marketing. | [`setup-marketing-system`](skills/setup-marketing-system/) | Fondamenti di marketing condivisi, con fonti, regole, limiti e responsabilità da chiarire. |
| Hai un'idea, una richiesta o un problema, ma non sai se è davvero una sfida di marketing. | [`define-marketing-challenge`](skills/define-marketing-challenge/) | Un documento di sintesi che chiarisce problema, pubblico, cambiamento desiderato, evidenze e criteri di successo. |
| Devi scegliere tra più strade possibili. | [`choose-marketing-direction`](skills/choose-marketing-direction/) | Un confronto tra alternative, con vantaggi, svantaggi, rischi e assunzioni espliciti. |
| Hai scelto una direzione e devi renderla concreta. | [`define-marketing-mix`](skills/define-marketing-mix/) | Scelte coerenti su offerta, prezzo, distribuzione e comunicazione. |

I nomi tra parentesi sono quelli da usare per richiamare direttamente le skill. Se l'ambiente supporta l'Assistant, puoi invece descrivere semplicemente ciò che vuoi fare.

### Sorgente candidata in sviluppo

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni | Stato |
| --- | --- | --- | --- |
| Vuoi progettare una campagna partendo da un'esigenza, un brief o un marketing mix. | [`design-campaign`](skills/design-campaign/) | Una Campaign Spec con funnel, messaggi, canali, asset, responsabilità e misurazione. | v0.1.4 candidata; non inclusa nella Suite pubblicata |
| Hai fonti o un'idea, ma non sai quale singolo contenuto sarebbe più utile. | [`content-director`](skills/content-director/) | Una raccomandazione editoriale agnostica e, dopo approvazione, un Content Brief. | [v0.1.1 stabile](https://github.com/vincos73/augmented-marketing-skills/releases/tag/content-director-v0.1.1); retest e sei regressioni: PASS, zero hard fail |

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

Solo dopo puoi passare a pagine, campagne e contenuti. `design-campaign` è presente come sorgente candidata non ancora pubblicata; `content-director` è disponibile come release singola stabile e non è incluso nella Suite beta.8. Le altre competenze per campagne, contenuti e apprendimento restano previste per uno sviluppo futuro.

## Versioni della Suite e release singole

Le versioni correnti delle cinque skill sono incluse nella [release della Suite beta.8](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.8), con gli archivi e i checksum nel repository. Le release singole precedenti restano indicate nella tabella di installazione quando sono il riferimento verificato per quella skill.

| Skill | Versione inclusa nella Suite beta.8 | Risultato principale |
| --- | --- | --- |
| [`setup-business-context`](skills/setup-business-context/) | v0.6.4 | Contesto identitario riutilizzabile. |
| [`setup-marketing-system`](skills/setup-marketing-system/) | v0.3.1 | Fondamenti e regole di marketing condivisi. |
| [`define-marketing-challenge`](skills/define-marketing-challenge/) | v0.1.3 | Documento sintetico e verificabile della sfida. |
| [`choose-marketing-direction`](skills/choose-marketing-direction/) | v0.2.2 | Confronto e scelta della direzione. |
| [`define-marketing-mix`](skills/define-marketing-mix/) | v0.1.3 | Marketing mix su offerta, prezzo, distribuzione e comunicazione. |

## Cosa non devi aspettarti

- L'agente non inventa fatti per riempire i vuoti: segnala ciò che manca o che deve essere verificato.
- Una proposta non diventa automaticamente una decisione approvata.
- L'approvazione di un documento non autorizza pubblicazioni, acquisti media o altre azioni esterne.
- La Suite non sostituisce la responsabilità di chi conosce l'organizzazione e deve approvare le scelte.

## Installazione

La regola è semplice: **per una skill singola usa uno ZIP portabile; per tutte le skill usa il plugin dedicato alla piattaforma**. Non caricare mai il bundle OpenAI/Codex in Claude, né il bundle Claude in ChatGPT/Codex.

| Ambiente | Una skill | Tutte le skill |
| --- | --- | --- |
| Claude | Uno ZIP in `dist/agent-skills/` | `dist/claude/augmented-marketing-suite-claude-v0.1.0-beta.8.zip` in **Personalizza → Plugin** |
| ChatGPT | Uno ZIP in `dist/agent-skills/` nel flusso Skills | `dist/openai/augmented-marketing-suite-0.1.0-beta.8.zip` nel flusso Plugin |
| Codex | Uno ZIP in `dist/agent-skills/` quando il flusso locale lo consente | `dist/openai/augmented-marketing-suite-0.1.0-beta.8.zip` nel marketplace o catalogo Plugin |

### Per Claude o ChatGPT: una skill alla volta

La beta.8 pubblicata offre un archivio ZIP per ciascuna delle cinque skill specialistiche in [`dist/agent-skills/`](dist/agent-skills/). Ogni archivio contiene una sola cartella radice con `SKILL.md` e i riferimenti necessari: è il formato più semplice per il caricamento diretto di una skill compatibile con Agent Skills.

`content-director` v0.1.1 è pubblicata separatamente nella [release singola stabile](https://github.com/vincos73/augmented-marketing-skills/releases/tag/content-director-v0.1.1). Non fa parte degli archivi della Suite beta.8.

Scegli la skill che ti serve, caricala con il meccanismo di skill del tuo ambiente e avvia una nuova chat. Claude non usa l'Assistant incluso nella Suite OpenAI, quindi gli archivi portabili contengono soltanto le cinque skill specialistiche.

### Per Claude: Suite completa con un solo upload

Carica [`dist/claude/augmented-marketing-suite-claude-v0.1.0-beta.8.zip`](dist/claude/augmented-marketing-suite-claude-v0.1.0-beta.8.zip) nella sezione **Personalizza → Plugin** di Claude. È un plugin Claude dedicato: ha `.claude-plugin/plugin.json` e include le cinque skill specialistiche, senza Augmented Marketing Assistant.

### Per ChatGPT e Codex: Suite completa con un solo upload

La beta.8 pubblicata offre anche [`dist/openai/augmented-marketing-suite-0.1.0-beta.8.zip`](dist/openai/augmented-marketing-suite-0.1.0-beta.8.zip), con il manifesto `.codex-plugin` e tutte e sei le skill, incluso Augmented Marketing Assistant. Segui le istruzioni di [`INSTALLAZIONE.md`](INSTALLAZIONE.md).

> Allegare uno ZIP a una chat normale consente di leggerlo, ma non registra automaticamente un plugin o una skill. Usa soltanto il flusso di installazione disponibile nel tuo account o workspace.

### Installare una versione pubblicata

Per una release già pubblicata, scarica la skill desiderata, estraila e segui il file `INSTALL.md` incluso nella cartella. Mantieni l'intera cartella, compresi istruzioni, riferimenti ed eventuali controlli.

| Skill | Versione pubblicata da installare |
| --- | --- |
| `setup-business-context` | Suite beta.8: `v0.6.4` |
| `setup-marketing-system` | Suite beta.8: `v0.3.1` |
| `define-marketing-challenge` | Suite beta.8: `v0.1.3` |
| `choose-marketing-direction` | Suite beta.8: `v0.2.2` |
| `define-marketing-mix` | Suite beta.8: `v0.1.3` |

Scegliere una versione pubblicata precisa evita di installare involontariamente una versione ancora in sviluppo. In Codex, la destinazione abituale è `~/.codex/skills/`, ma il percorso può cambiare in base all'ambiente.

## Per chi vuole approfondire

- [Installazione dettagliata](INSTALLAZIONE.md)
- [Contratto di portabilità](PORTABILITA.md)
- [Architettura e confini del sistema](MARKETING-AGENT-SYSTEM.md)

## Contribuire

Il repository accoglie contributi su istruzioni, template, controlli ed esempi sintetici. Non includere dati di clienti, casi reali riservati o informazioni personali.
