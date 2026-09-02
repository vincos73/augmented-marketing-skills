---
artifact: ams-probe-codex-runtime-results
status: partial-pass
probe_version: "0.0.1"
tested_on: "2026-08-30"
---

# Risultati runtime Codex

## Perimetro osservato

- Caricamento: skill repo-scoped copiate in una fixture sotto `/private/tmp`; nessuna installazione del plugin.
- Esecuzione: sessioni nuove, effimere, non interattive e con sandbox `read-only`.
- Verificato: selezione naturale del router, esclusione degli specialisti dal roster automatico, invocazione esplicita di uno specialista.
- Non verificato: installazione dello ZIP OpenAI, continuità multi-turno, compattazione, aggiornamento e rimozione.

## Prova 1 — richiesta naturale

Prompt integrale:

> Ho l’obiettivo di far conoscere un nuovo servizio alle PMI, ma non so quale problema di marketing dovremmo affrontare per primo. Rispondi alla richiesta senza modificare file.

Esito: **PASS**. Codex ha selezionato `ams-router`, letto soltanto il playbook `challenge` e non ha prodotto marker specialistici.

Risposta integrale:

```text
PROBE_PLAYBOOK: challenge

“Far conoscere il servizio” descrive il risultato desiderato, ma non chiarisce ancora l’ostacolo. Il primo problema potrebbe essere, per esempio, scarsa notorietà, bisogno poco riconosciuto, proposta poco comprensibile o mancanza di fiducia: richiedono risposte diverse.

Per formulare la sfida giusta servono tre informazioni:

1. Quali PMI volete raggiungere: settore, dimensione e ruolo del decisore?
2. Che cosa dovrebbero fare concretamente dopo aver conosciuto il servizio?
3. Avete già evidenze su dove si blocca il percorso: non vi conoscono, non percepiscono il problema, non capiscono la proposta o non si fidano?

Bozza provvisoria:

> Dobbiamo capire quale ostacolo impedisce alle PMI prioritarie di passare dalla situazione attuale all’interesse concreto per il nuovo servizio, così da decidere quale problema di marketing affrontare per primo.

Questa formulazione non è ancora confermata: le risposte permetteranno di distinguere fatti, ipotesi e incognite, quindi scegliere una priorità verificabile.

STATO_PROBE
- fase: challenge
- confermato: obiettivo di far conoscere un nuovo servizio alle PMI
- ancora_da_decidere: segmento prioritario, comportamento desiderato e principale ostacolo di marketing
```

## Prova 2 — roster automatico

Prompt integrale:

> Senza leggere il filesystem, elenca soltanto le skill AMS Probe che risultano disponibili alla tua invocazione automatica in questa sessione.

Esito: **PASS**. Risposta integrale:

```text
- `ams-router`
```

I due specialisti con `allow_implicit_invocation: false` non sono comparsi.

## Prova 3 — invocazione manuale

Un primo tentativo con il nome generico `$define-marketing-challenge` ha caricato la skill reale omonima già installata, non quella del probe. Questo ha dimostrato una collisione nel namespace globale Codex.

Correzione limitata all’adattatore di test: i due specialisti OpenAI hanno ricevuto il prefisso `ams-probe-`. La sorgente neutrale e il bundle Claude non sono cambiati.

Prompt di retest integrale:

> $ams-probe-define-marketing-challenge Ho l’obiettivo di far conoscere un nuovo servizio alle PMI. Rispondi senza modificare file.

Esito: **PASS**. Codex ha letto il playbook dalla fixture del probe.

Risposta integrale:

```text
PROBE_SPECIALIST: define-marketing-challenge
PROBE_PLAYBOOK: challenge

Per formulare una sfida di marketing servono tre chiarimenti:

1. Qual è il servizio e quale problema concreto risolve?
2. Quali PMI volete raggiungere: settore, dimensione, territorio e interlocutore decisionale?
3. Quale risultato aziendale dovrebbe produrre la notorietà — richieste di contatto, prove, vendite o altro — ed entro quando?

Al momento, “far conoscere” indica un cambiamento di notorietà, ma non chiarisce il comportamento atteso né il suo contributo al business. Con queste risposte preparerò una prima formulazione revisionabile, non ancora confermata.
```

## Limiti e segnali collaterali

- Codex ha avvisato che il roster complessivo di skill installate eccede il budget delle descrizioni e che alcune vengono abbreviate. Il router è stato comunque selezionato correttamente in questa prova.
- Il runtime ha segnalato metadata non validi in alcune skill globali estranee al probe; non hanno impedito il test, ma rendono l’ambiente meno isolato del solo filesystem temporaneo.
- Il risultato dimostra il comportamento delle skill repo-scoped nel Codex corrente, non l’installazione del plugin distribuito in ChatGPT o Codex.

## Verdetto parziale Codex

**PASS per i tre comportamenti fondamentali osservati; collaudo plugin e continuità ancora pendenti.**

