
# Augmented Marketing Suite

> Un insieme di skill per aiutarti a prendere decisioni di marketing più chiare, verificabili e approvabili con un agente IA.

Se usi Claude, ChatGPT, Codex o un altro ambiente compatibile, puoi chiedere all'agente di aiutarti a capire un problema di marketing, confrontare alcune strade e preparare il passo successivo.

Non devi conoscere il metodo o i nomi tecnici per iniziare. Puoi descrivere il bisogno con parole tue.

<img width="1800" height="1200" alt="AMS-framework-1" src="https://github.com/user-attachments/assets/2469268c-85b4-42d4-9eb1-fe8d8481b34a" />

## Che cos'è una skill?

Una skill è un insieme di istruzioni specializzate che l'agente può usare quando serve. In questo progetto ogni skill ha un compito preciso e produce un documento che puoi leggere, correggere e approvare.

Qui per agente IA intendiamo l'assistente con cui lavori, per esempio Claude, ChatGPT o Codex, quando l'ambiente consente di installare queste istruzioni.

La Suite non è un direttore marketing automatico e non decide al posto tuo. Ti aiuta a rendere più ordinato e ricostruibile il percorso che porta a una decisione.

Chi contribuisce nuove skill trova i criteri comuni nello [standard di progettazione](STANDARD-PROGETTAZIONE-SKILL.md): risposte proporzionate, dialogo per differenza, fonti separate dai materiali metodologici, gate compatti e test senza scritture canoniche.

## Versione stabile 1.0.0 pubblicata

Augmented Marketing Suite 1.0.0 distribuisce gli stessi dodici elementi nei plugin Claude e OpenAI/Codex: **Augmented Marketing Assistant v0.3.0** e undici skill specialistiche. L'Assistant è una normale skill di orientamento, condivisa tra i due plugin: aiuta chi descrive un bisogno senza sapere da quale passaggio iniziare e, quando il meccanismo dell'ambiente lo consente, richiama la skill pertinente nella stessa conversazione. Non introduce agenti o subagenti. Se nomini già una skill, questa viene usata direttamente.

La versione stabile 1.0.0 è pubblicata su GitHub con 15 asset: 13 ZIP, un manifest e `SHA256SUMS`. Gli archivi locali, il manifest e i checksum sono in [`dist/1.0.0`](dist/1.0.0/README.md); il rapporto delle verifiche è [`evals/suite-1.0.0/README.md`](evals/suite-1.0.0/README.md). Il rapporto registra anche il limite noto: due test conversazionali Claude non sono verificati perché mancava l'autenticazione. Questa uscita non introduce nuove prove comportamentali né un pilot con marketer reali.

Pagina release: [Augmented Marketing Suite v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0).

## Da dove cominciare

### Le dodici skill della Suite 1.0.0

| Se ti trovi in questa situazione | Cosa usare | Che cosa ottieni |
| --- | --- | --- |
| Descrivi un bisogno di marketing, ma non sai da quale passaggio iniziare. | [`Augmented Marketing Assistant`](skills/augmented-marketing-assistant/) | Orientamento verso la skill utile; incluso in entrambi i plugin. |
| Vuoi spiegare all'agente chi è la tua organizzazione. | [`setup-business-context`](skills/setup-business-context/) | Un contesto riutilizzabile con identità, fatti approvati, vincoli e aspetti ancora da chiarire. |
| Vuoi definire le regole con cui fare marketing. | [`setup-marketing-system`](skills/setup-marketing-system/) | Fondamenti di marketing condivisi, con fonti, regole, limiti e responsabilità da chiarire. |
| Vuoi definire o rivedere una voce riutilizzabile. | [`setup-brand-voice`](skills/setup-brand-voice/) | Una guida alla voce del brand o una revisione circoscritta. |
| Hai un'idea, una richiesta o un problema, ma non sai se è davvero una sfida di marketing. | [`define-marketing-challenge`](skills/define-marketing-challenge/) | Un documento di sintesi che chiarisce problema, pubblico, cambiamento desiderato, evidenze e criteri di successo. |
| Devi scegliere tra più strade possibili. | [`choose-marketing-direction`](skills/choose-marketing-direction/) | Un confronto tra alternative, con vantaggi, svantaggi, rischi e assunzioni espliciti. |
| Hai scelto una direzione e devi renderla concreta. | [`define-marketing-mix`](skills/define-marketing-mix/) | Scelte coerenti su offerta, prezzo, distribuzione e comunicazione. |
| Vuoi progettare una campagna. | [`design-campaign`](skills/design-campaign/) | Una Campaign Spec con percorso, messaggi, canali, asset, responsabilità e misurazione. |
| Vuoi verificare una campagna prima della pubblicazione o dell'invio. | [`campaign-review`](skills/campaign-review/) | Una review separata di coerenza strategica, affermazioni, prontezza operativa e baseline decisionale per il debrief. |
| Devi leggere i risultati e decidere che cosa fare dopo. | [`campaign-debrief`](skills/campaign-debrief/) | Una lettura dei risultati con limiti, decisione consigliata e prossima verifica. |
| Hai fonti o un'idea, ma non sai quale singolo contenuto sarebbe più utile. | [`content-director`](skills/content-director/) | Una raccomandazione editoriale agnostica e, dopo approvazione, un Content Brief. |
| Hai un testo marketing da scrivere, riscrivere o adattare. | [`write-marketing-copy`](skills/write-marketing-copy/) | Copy pronto per la revisione, basato su voce e fatti disponibili. |

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

Solo dopo puoi passare a pagine, campagne e contenuti. Research & Evidence e monitoring restano sviluppi successivi da validare.

## Versioni incluse

Le versioni delle skill specialistiche restano quelle già definite e non vengono incrementate dalla release della Suite.

| Skill | Versione inclusa nella Suite 1.0.0 | Risultato principale |
| --- | --- | --- |
| [`Augmented Marketing Assistant`](skills/augmented-marketing-assistant/) | v0.3.0 | Orientamento verso il passaggio pertinente. |
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
| Claude | Uno ZIP in `dist/1.0.0/agent-skills/` | [`dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip`](dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip) in **Personalizza → Plugin** |
| ChatGPT | Uno ZIP in `dist/1.0.0/agent-skills/` nel flusso Skills | [`dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip`](dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip) nel flusso Plugin |
| Codex | Uno ZIP in `dist/1.0.0/agent-skills/` quando il flusso locale lo consente | [`dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip`](dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip) nel marketplace o catalogo Plugin |

Gli ZIP portabili contengono soltanto le undici skill specialistiche; l'Assistant è incluso nei due plugin completi. Per una release già pubblicata, scarica l'archivio dalla [pagina GitHub v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0), estrailo e segui [`INSTALLAZIONE.md`](INSTALLAZIONE.md).

Allega o carica gli ZIP soltanto nel flusso Skills o Plugin previsto dal tuo ambiente: allegare un archivio a una chat normale consente di leggerlo, ma non registra automaticamente una skill o un plugin. Dopo l'installazione apri una nuova chat e controlla che la skill sia visibile o invocabile.

## Per chi vuole approfondire

- [Installazione dettagliata](INSTALLAZIONE.md)
- [Contratto di portabilità](PORTABILITA.md)
- [Architettura e confini del sistema](MARKETING-AGENT-SYSTEM.md)
- [Offerta e comunicazione](OFFERTA-COMUNICAZIONE.md)
- [Note di release 1.0.0](RELEASE-NOTES-1.0.0.md)
- [Stato della release](RELEASE-STATUS.md)

## Storia recente

La beta.12 è stata la candidata locale che ha portato l'Assistant v0.3.0 anche nel plugin Claude. La beta.11 è la precedente release pubblicata con undici skill specialistiche e Assistant solo nel plugin OpenAI/Codex. Restano disponibili come riferimenti storici; la documentazione corrente e i percorsi di installazione fanno riferimento alla Suite 1.0.0.

## Contribuire

Il repository accoglie contributi su istruzioni, template, controlli ed esempi sintetici. Non includere dati di clienti, casi reali riservati o informazioni personali.
