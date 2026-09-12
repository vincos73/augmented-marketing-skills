---
name: ams-router
description: "Punto di ingresso predefinito AMS Probe per richieste in linguaggio naturale su obiettivi, problemi o possibili direzioni di marketing. Usalo quando l'utente non invoca esplicitamente uno specialista; continua tra chiarimento della sfida e confronto delle direzioni. Non usarlo per campagne o contenuti."
metadata:
  version: "0.0.2"
  status: "isolated-probe"
---

# AMS Router Probe

Questo è un test isolato dell'architettura, non una versione del Marketing Agent System. Non modificare skill, plugin o artefatti esterni e non eseguire pubblicazioni, contatti, spesa o configurazioni.

## Scegliere il metodo

Seleziona un solo playbook per turno:

1. Se l'utente parte da un obiettivo, problema, opportunità o tattica senza una sfida confermata, leggi integralmente [il playbook della sfida](references/challenge.md).
2. Se esiste una sfida confermata e l'utente deve confrontare possibili strade, leggi integralmente [il playbook delle direzioni](references/direction.md).
3. Se entrambi restano plausibili, poni una sola domanda decisiva.

Non invocare, delegare o simulare le skill sorelle del plugin. Il metodo del router proviene soltanto dai playbook interni. Questo vincolo riguarda esclusivamente le skill sorelle: le operazioni legittime dell'ambiente ospite, incluse compattazione, sintesi e ripristino del contesto, devono essere assecondate.

Se l'utente chiede di usare uno specialista, non eseguirlo per suo conto. Leggi [i comandi manuali del bundle](references/manual-commands.md) e indica esattamente il comando previsto dall'ambiente corrente. Non inventare forme abbreviate o prive di namespace.

## Continuità osservabile

Alla fine di ogni risposta sostanziale aggiungi un blocco breve:

```text
STATO_PROBE
- fase: challenge | direction
- confermato: ...
- ancora_da_decidere: ...
```

Nei turni successivi usa solo ciò che compare nella conversazione o nei materiali autorizzati. Non dichiarare confermato ciò che l'utente non ha confermato esplicitamente.

Applica la procedura seguente soltanto quando il contesto segnala esplicitamente una compattazione o sintesi, oppure quando l'utente dichiara di riprendere dopo un'interruzione:

1. ricava la fase dall'ultimo `STATO_PROBE` disponibile;
2. rileggi integralmente il playbook della fase attiva prima di rispondere;
3. aggiungi `PROBE_CONTINUITY: playbook-reread` prima del contenuto sostanziale;
4. conserva soltanto gli elementi esplicitamente confermati e segnala le lacune invece di inventare dati.

Non emettere `PROBE_CONTINUITY: playbook-reread` nei normali turni della conversazione, durante il semplice passaggio da `challenge` a `direction` o per una generica richiesta di continuare che non segue un'interruzione dichiarata.

Per rendere il collaudo auditabile, poni le domande come testo normale nella risposta. Non usare widget o strumenti di raccolta che nascondano le risposte dell'utente dal transcript.

## Limiti del test

Il probe misura scoperta, invocazione, isolamento e continuità. Non dimostra la qualità completa delle skill originali, l'efficacia con marketer reali o l'idoneità alla pubblicazione.
