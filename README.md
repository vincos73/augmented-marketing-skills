# Augmented Marketing Suite

> Un insieme di skill per aiutarti a prendere decisioni di marketing più chiare, verificabili e approvabili con un agente IA.

Se usi ChatGPT, Codex o un altro ambiente compatibile, puoi chiedere all'agente di aiutarti a capire un problema di marketing, confrontare alcune strade e preparare il passo successivo.

Non devi conoscere il metodo o i nomi tecnici per iniziare. Puoi descrivere il bisogno con parole tue.

## Che cos'è una skill?

Una skill è un insieme di istruzioni specializzate che l'agente può usare quando serve. In questo progetto ogni skill ha un compito preciso e produce un documento che puoi leggere, correggere e approvare.

Qui per agente IA intendiamo l'assistente con cui lavori, per esempio ChatGPT o Codex, quando l'ambiente consente di installare queste istruzioni.

La Suite non è un direttore marketing automatico e non decide al posto tuo. Ti aiuta a rendere più ordinato e ricostruibile il percorso che porta a una decisione.

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

Solo dopo puoi passare a pagine, campagne e contenuti. Le competenze per campagne, contenuti e apprendimento sono previste per uno sviluppo futuro e non fanno parte delle skill disponibili in questo progetto.

## Skill disponibili oggi

Queste sono le versioni stabili installabili dalla Suite beta.

| Skill | Versione stabile | Risultato principale |
| --- | --- | --- |
| [`setup-business-context`](skills/setup-business-context/) | [v0.6.3](https://github.com/vincos73/augmented-marketing-skills/releases/tag/setup-business-context-v0.6.3) | Contesto identitario riutilizzabile. |
| [`setup-marketing-system`](skills/setup-marketing-system/) | [v0.3.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/setup-marketing-system-v0.3.0) | Fondamenti e regole di marketing condivisi. |
| [`define-marketing-challenge`](skills/define-marketing-challenge/) | [v0.1.2](https://github.com/vincos73/augmented-marketing-skills/releases/tag/define-marketing-challenge-v0.1.2) | Documento sintetico e verificabile della sfida. |
| [`choose-marketing-direction`](skills/choose-marketing-direction/) | [v0.2.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/choose-marketing-direction-v0.2.1) | Confronto e scelta della direzione. |
| [`define-marketing-mix`](skills/define-marketing-mix/) | [v0.1.2](https://github.com/vincos73/augmented-marketing-skills/releases/tag/define-marketing-mix-v0.1.2) | Marketing mix su offerta, prezzo, distribuzione e comunicazione. |

## Cosa non devi aspettarti

- L'agente non inventa fatti per riempire i vuoti: segnala ciò che manca o che deve essere verificato.
- Una proposta non diventa automaticamente una decisione approvata.
- L'approvazione di un documento non autorizza pubblicazioni, acquisti media o altre azioni esterne.
- La Suite non sostituisce la responsabilità di chi conosce l'organizzazione e deve approvare le scelte.

## Installazione

### Il modo più semplice: Suite completa

La [versione beta.6 di Augmented Marketing Suite pubblicata su GitHub](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.6) contiene le cinque skill e l'Assistant, comprese le versioni più recenti delle due skill di setup. Segui le istruzioni di [`INSTALLAZIONE.md`](INSTALLAZIONE.md).

La beta.6 è pensata per ChatGPT e Codex in ambienti che supportano l'installazione di skill. Dopo l'installazione, apri una nuova chat e descrivi il bisogno. La presenza dei file sul disco non dimostra che una chat già aperta abbia caricato la versione aggiornata.

> Allegare uno ZIP a una chat normale non registra automaticamente un plugin. Se il tuo ambiente non mostra un catalogo o un meccanismo di installazione, chiedi all'amministratore dell'ambiente quale procedura supporta.

### Installare una sola skill

Questa è un'opzione per chi gestisce direttamente l'installazione. Scarica la versione pubblicata della skill desiderata, estraila e segui il file `INSTALL.md` incluso nella cartella. Mantieni l'intera cartella, compresi istruzioni, riferimenti ed eventuali controlli.

| Skill | Versione pubblicata da installare |
| --- | --- |
| `setup-business-context` | `setup-business-context-v0.6.3` |
| `setup-marketing-system` | `setup-marketing-system-v0.3.0` |
| `define-marketing-challenge` | `define-marketing-challenge-v0.1.2` |
| `choose-marketing-direction` | `choose-marketing-direction-v0.2.1` |
| `define-marketing-mix` | `define-marketing-mix-v0.1.2` |

Scegliere una versione pubblicata precisa evita di installare involontariamente una versione ancora in sviluppo. In Codex, la destinazione abituale è `~/.codex/skills/`, ma il percorso può cambiare in base all'ambiente.

## Per chi vuole approfondire

- [Installazione dettagliata](INSTALLAZIONE.md)
- [Contratto di portabilità](PORTABILITA.md)
- [Architettura e confini del sistema](MARKETING-AGENT-SYSTEM.md)

## Contribuire

Il repository accoglie contributi su istruzioni, template, controlli ed esempi sintetici. Non includere dati di clienti, casi reali riservati o informazioni personali.
