# Istruzioni per Claude — collaudo runtime AMS Probe

Esegui un collaudo del plugin sperimentale `ams-probe`. Non modificare il repository, il plugin `augmented-marketing-suite` o i file generati. Non correggere il probe durante il test.

Leggi prima:

```text
prototypes/ams-probe/TEST-PROTOCOL.md
```

Usa esclusivamente questo bundle:

```text
prototypes/ams-probe/dist/ams-probe-claude-v0.0.2.zip
```

oppure, per `--plugin-dir`:

```text
prototypes/ams-probe/dist/claude/ams-probe
```

Questa è una regressione mirata della versione `0.0.2`. Esegui nell'ordine almeno le prove 1–7 del protocollo. Non eseguire la prova 8 finché l'utente non autorizza esplicitamente un ambiente senza la suite precedente. Ogni prova che richiede una nuova conversazione deve partire senza contenuto del test precedente. Registra:

- versione e canale Claude realmente usati;
- metodo di installazione;
- risposta integrale di ogni prova;
- marker osservati;
- PASS o FAIL con motivazione;
- differenza tra comportamento documentato e osservato;
- eventuali limiti che hanno impedito una prova.

Non dichiarare superata una prova sulla sola base del frontmatter o della documentazione. Il verdetto deve dipendere dal comportamento osservato.

Concludi con `GO`, `GO CON RISERVE` o `NO-GO` secondo le condizioni del protocollo.
