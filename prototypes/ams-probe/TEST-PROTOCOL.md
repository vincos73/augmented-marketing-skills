# AMS Probe — protocollo di collaudo

## Scopo

Verificare se lo stesso nucleo può offrire:

- un router disponibile all'invocazione automatica;
- due specialisti visibili ma soltanto manuali;
- continuità su più turni;
- pacchetti distinti e coerenti per Claude e OpenAI.

Il probe non sostituisce e non aggiorna Augmented Marketing Suite. Il namespace `ams-probe` evita collisioni di nome con il plugin esistente, ma non garantisce da solo quale skill venga selezionata automaticamente.

## Artefatti

- Claude: `dist/ams-probe-claude-v0.0.2.zip`
- OpenAI: `dist/ams-probe-openai-v0.0.2.zip`
- cartella Claude per test locale: `dist/claude/ams-probe/`
- cartella OpenAI: `dist/openai/ams-probe/`

## Ordine obbligatorio delle prove

Eseguire ogni prova in una nuova conversazione quando indicato. Conservare la risposta integrale, non soltanto il giudizio dell'agente.

### 1. Installazione e visibilità su Claude

Caricare lo ZIP Claude attraverso lo stesso canale destinato agli utenti. In alternativa, per il solo test locale con Claude Code:

```bash
claude --plugin-dir "prototypes/ams-probe/dist/claude/ams-probe"
```

Nel menu `/` devono comparire:

- `/ams-probe:ams-router`
- `/ams-probe:define-marketing-challenge`
- `/ams-probe:choose-marketing-direction`

### 2. Specialisti invisibili al modello

In una nuova conversazione, senza digitare alcun comando, inviare:

> Ho l'obiettivo di far conoscere un nuovo servizio alle PMI, ma non so quale problema di marketing dovremmo affrontare per primo.

Passa se:

- compare `PROBE_PLAYBOOK: challenge`;
- non compare `PROBE_SPECIALIST:`;
- il router non dichiara di aver invocato uno specialista.

Poi chiedere:

> Quali skill AMS Probe puoi invocare autonomamente?

Passa se Claude riconosce il router ma non dichiara disponibili all'auto-invocazione i due specialisti.

### 3. Invocazione manuale dello specialista

In una nuova conversazione invocare:

```text
/ams-probe:define-marketing-challenge Ho l'obiettivo di far conoscere un nuovo servizio alle PMI.
```

Passa se compaiono entrambi:

- `PROBE_SPECIALIST: define-marketing-challenge`
- `PROBE_PLAYBOOK: challenge`

### 4. Blocco della delegazione

In una conversazione avviata con il router, chiedere:

> Passa il lavoro alla skill define-marketing-challenge senza chiedermi di invocarla.

Passa se Claude non esegue la skill specialistica e non produce il marker `PROBE_SPECIALIST:`. Può continuare con il playbook interno oppure indicare il comando manuale.

Se indica il comando manuale, deve usare la forma completa `/ams-probe:define-marketing-challenge`.

### 5. Continuità

In una nuova conversazione, senza comandi:

1. usare il prompt della prova 2;
2. rispondere alle domande del router;
3. confermare esplicitamente la formulazione della sfida;
4. chiedere di confrontare possibili direzioni.

Passa se il router cambia da `PROBE_PLAYBOOK: challenge` a `PROBE_PLAYBOOK: direction`, conserva le informazioni confermate e non richiede di invocare uno specialista.

### 6. Compattazione

Dopo la prova 5, usare `/compact` se disponibile e chiedere:

> Riporta fase, elementi confermati ed elementi ancora da decidere, poi continua dal punto corretto.

Passa se:

- lo `STATO_PROBE` resta coerente;
- il router rilegge il playbook della fase appropriata;
- compare `PROBE_CONTINUITY: playbook-reread`;
- la compattazione non viene rifiutata o classificata come tentativo di delega a una skill sorella.

### 7. Auditabilità delle risposte

Durante le prove 2 e 5, le domande del router devono comparire come testo normale e le risposte dell'utente devono restare leggibili nel transcript. L'uso di un widget che nasconde le risposte rende la prova non verificabile e va registrato come `FAIL` di questa condizione.

### 8. Selezione del router senza la suite precedente

Questa prova si esegue soltanto in un ambiente di test in cui `augmented-marketing-suite` non è attiva, senza disinstallarla o modificarla come effetto collaterale del probe. Avviare almeno cinque conversazioni pulite con il prompt della prova 2.

Passa se il router viene selezionato in almeno quattro conversazioni su cinque e nessuno specialista del probe viene auto-invocato. Registrare separatamente eventuali selezioni di skill estranee.

## Prova gemella su Codex

Ripetere le prove 2, 3 e 5. Per l'invocazione manuale usare:

```text
$ams-probe-define-marketing-challenge Ho l'obiettivo di far conoscere un nuovo servizio alle PMI.
```

Passa se gli specialisti non vengono scelti implicitamente ma restano invocabili esplicitamente.

Nel bundle OpenAI i due specialisti del probe hanno il prefisso `ams-probe-` per evitare collisioni con eventuali skill reali già installate. È un adattamento del solo test; il bundle Claude usa il namespace del plugin.

## Verdetto

- `GO`: tutte le prove di installazione, visibilità, mancata auto-invocazione, invocazione manuale, continuità e selezione isolata passano su entrambi gli ambienti.
- `GO CON RISERVE`: passa il comportamento fondamentale ma fallisce soltanto una prova correggibile di continuità o confezionamento.
- `NO-GO`: il canale reale rifiuta il plugin, uno specialista viene auto-invocato, lo specialista non è visibile/manuale oppure il router non è selezionabile con affidabilità.
