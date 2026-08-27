# Augmented Marketing Skills

> Skill installabili per portare contesto, metodo e decisioni verificabili nel marketing con agenti IA.

Augmented Marketing Skills aiuta manager, marketer e consulenti a lavorare con agenti IA, tra cui ChatGPT, Claude e Codex, quando il loro ambiente supporta l'installazione di skill.

Prima dell'esecuzione, le skill aiutano a mettere a fuoco la sfida, confrontare direzioni alternative, rendere visibili le assunzioni e coordinare prodotto, prezzo, distribuzione e comunicazione.

Non sostituiscono un marketer o un CMO. Rendono più esplicito e ricostruibile il processo con cui si arriva a una decisione.

## Perché esiste

Un agente IA può generare velocemente analisi, idee e contenuti. Un testo ben scritto, però, non garantisce che il problema iniziale sia quello giusto, che la scelta sia coerente con il contesto o che una tattica non stia prendendo il posto della strategia.

Queste skill aiutano a:

- evitare di ricostruire il contesto dell'organizzazione a ogni conversazione;
- distinguere fonti, fatti, inferenze, assunzioni e aspetti ancora aperti;
- verificare una richiesta tattica prima di trasformarla in una soluzione;
- confrontare alternative e trade-off prima di scegliere;
- coordinare le quattro P del marketing mix;
- lasciare una traccia che possa essere rivista e approvata.

## Come funziona

```text
Identità e contesto dell'organizzazione
                 ↓
Fondamenti di marketing condivisi
                 ↓
Definizione della sfida
                 ↓
Confronto e scelta della direzione
                 ↓
Marketing mix: prodotto, prezzo, distribuzione, comunicazione
                 ↓
Campagne, contenuti e attivazioni
                 ↓
Risultati e apprendimento
```

Ogni skill produce un artefatto che può essere rivisto, corretto, approvato e usato come input nel passaggio seguente.

## Le skill disponibili

| Skill | A cosa serve | Risultato | Stato |
| --- | --- | --- | --- |
| [`setup-business-context`](skills/setup-business-context/) | Raccogliere identità, fatti approvati, vincoli e aspetti aperti di un'organizzazione. | Un contesto riutilizzabile per gli agenti. | Sorgente v0.6.2; [release pubblica v0.6.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/v0.6.0). |
| [`setup-marketing-system`](skills/setup-marketing-system/) | Tradurre il contesto in fondamenti, regole e limiti di marketing condivisi. | Un sistema di riferimento per le decisioni successive. | [Release stabile v0.2.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/setup-marketing-system-v0.2.1). |
| [`define-marketing-challenge`](skills/define-marketing-challenge/) | Capire se una richiesta è davvero una sfida di marketing e formularla in modo verificabile. | Un brief della sfida, con evidenze, ipotesi e criteri di successo. | [Release stabile v0.1.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/define-marketing-challenge-v0.1.1). |
| [`choose-marketing-direction`](skills/choose-marketing-direction/) | Confrontare direzioni possibili e scegliere quella più coerente con obiettivi, vincoli e rischi. | Una direzione, con trade-off e assunzioni espliciti. | [Release stabile v0.2.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/choose-marketing-direction-v0.2.0). |
| [`define-marketing-mix`](skills/define-marketing-mix/) | Tradurre una direzione approvata in decisioni coerenti su Product, Price, Place e Promotion. | Un marketing mix verificabile prima dell'esecuzione. | [Release stabile v0.1.1](https://github.com/vincos73/augmented-marketing-skills/releases/tag/define-marketing-mix-v0.1.1). |

Le skill per campagne, contenuti e apprendimento sono in roadmap e non vanno considerate disponibili. I builder specializzati, come Carousel Builder, sono moduli esterni e non fanno parte di questo repository.

## Un esempio pratico

Immagina di voler lanciare un percorso di formazione continua per professionisti del marketing e della comunicazione.

Invece di chiedere subito all'agente di creare una landing page o un piano editoriale, puoi:

1. fornirgli il contesto reale dell'organizzazione e le regole già approvate;
2. trasformare l'idea iniziale in una sfida: quale cambiamento pratico vuoi ottenere, per chi e con quali vincoli?
3. confrontare più direzioni, ad esempio una community leggera, un laboratorio mensile o un percorso più strutturato;
4. scegliere una direzione, dichiarando ciò che resta da verificare;
5. definire offerta, prezzo, canale di accesso e comunicazione;
6. passare a campagne, pagine e contenuti solo dopo questa decisione.

L'agente non decide al posto tuo. Ti aiuta a rendere la decisione più leggibile, discutibile e condivisibile.

## Non devi usare tutto il percorso

Le skill sono modulari. Se obiettivo, formato e vincoli sono già chiari, puoi partire da una skill più operativa. Se la decisione è incerta o coinvolge più persone, il percorso completo aiuta a non saltare passaggi importanti.

## Installazione

Puoi installare una skill chiedendolo direttamente al tuo agente oppure scaricandola da GitHub.

> [!NOTE]
> ChatGPT, Claude e Codex possono usare procedure diverse. Se non sai quale sia quella prevista dal tuo ambiente, usa il primo metodo: l'agente deve confermare se può completare l'installazione e, se non può, indicarti il passaggio manuale minimo.

### 1. Chiedi al tuo agente di installarla

Apri una nuova conversazione con il tuo agente e copia il prompt qui sotto. GitHub mostra un pulsante per copiare il testo del blocco.

````text
Installa la skill `define-marketing-challenge` dal repository GitHub:
https://github.com/vincos73/augmented-marketing-skills

Usa la cartella:
skills/define-marketing-challenge

Installa esattamente la versione indicata dal tag:
define-marketing-challenge-v0.1.1

Prima verifica che il file SKILL.md dichiari la versione 0.1.1.
Installa l'intera cartella della skill nel percorso corretto per il tuo ambiente, senza modificare o sostituire altre skill.

Al termine, verifica che la skill sia disponibile in una nuova sessione e dimmi:
- dove l'hai installata;
- quale versione hai installato;
- come posso richiamarla.

Se non puoi accedere a GitHub o installare skill direttamente, spiegami il passaggio manuale minimo.
````

Per installare un'altra skill, sostituisci nome, cartella, tag e numero di versione con quelli nella tabella seguente.

| Skill | Cartella GitHub | Versione da fissare |
| --- | --- | --- |
| `setup-business-context` | `skills/setup-business-context` | release pubblica `v0.6.0` |
| `setup-marketing-system` | `skills/setup-marketing-system` | `setup-marketing-system-v0.2.1` |
| `define-marketing-challenge` | `skills/define-marketing-challenge` | `define-marketing-challenge-v0.1.1` |
| `choose-marketing-direction` | `skills/choose-marketing-direction` | `choose-marketing-direction-v0.2.0` |
| `define-marketing-mix` | `skills/define-marketing-mix` | `define-marketing-mix-v0.1.1` |

Fissare una release precisa evita di installare involontariamente una versione di sviluppo del ramo principale.

### 2. Installa manualmente dalla release

1. Apri la pagina delle [release](https://github.com/vincos73/augmented-marketing-skills/releases).
2. Scarica il file `.zip` della skill desiderata.
3. Estrai il contenuto dello ZIP.
4. Segui le istruzioni nel file `INSTALL.md` incluso nella cartella.

In Codex, di norma, la cartella completa della skill va copiata in:

```text
~/.codex/skills/
```

Su macOS, nel Finder puoi scegliere **Vai alla cartella** con `⌘⇧G` e inserire quel percorso.

Mantieni la struttura completa della cartella: istruzioni, esempi, template e script di verifica fanno parte della skill. Dopo l'installazione, apri una nuova sessione: la presenza dei file sul disco non dimostra che una chat già aperta li abbia caricati.

## Cosa rende diverso questo progetto

- Ogni skill ha un compito preciso, un artefatto atteso e un confine di approvazione.
- Il contesto dell'organizzazione è separato dalle decisioni specifiche.
- Fonti, fatti, inferenze, ipotesi e aspetti aperti non vengono trattati come equivalenti.
- Le alternative vengono confrontate con criteri e trade-off espliciti.
- La comunicazione è una delle quattro leve del marketing mix, non l'unica.
- L'approvazione di un documento non autorizza automaticamente azioni esterne, come pubblicazioni, acquisti media o modifiche a sistemi.

## Limiti e stato del progetto

Le skill includono esempi sintetici, controlli di struttura e valutazioni di coerenza. Queste verifiche dimostrano che il processo è stato progettato e testato in modo controllato, non che abbia già prodotto risultati misurabili con utenti reali.

La qualità delle decisioni dipende dalla qualità del contesto, delle fonti disponibili e dalla revisione di chi ne ha la responsabilità.

Il documento autorevole su architettura, decisioni, confini ed eval è [MARKETING-AGENT-SYSTEM.md](MARKETING-AGENT-SYSTEM.md).

## Roadmap

Le prossime aree previste includono:

- specifica e progettazione delle campagne;
- produzione e adattamento dei contenuti;
- osservazione dei risultati e apprendimento.

## Contribuire

Il repository accoglie contributi su istruzioni, template, controlli ed esempi sintetici. Non includere dati di clienti, casi reali riservati o informazioni personali.

Consulta [AGENTS.md](AGENTS.md) per le convenzioni del progetto.
