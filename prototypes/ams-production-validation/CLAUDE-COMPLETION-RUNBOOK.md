# Runbook per completare il confronto Claude

## Blocco osservato

Claude Desktop era raggiungibile in modalità Code e mostrava `Opus 5`, impegno `Alto` e modalità
veloce disattivata. Prima dell'invio del primo prompt, macOS si è bloccato. Lo sblocco richiede
un'azione manuale dell'utente.

Non esistono risposte Claude nuove da valutare. Non usare output Codex come sostituti.

## Preparazione

1. Sbloccare il Mac e aprire Claude Desktop.
2. Selezionare modalità Code e il checkout locale del progetto.
3. Verificare che il branch sia `codex/ams-production-validation` senza cambiare branch o file.
4. Impostare `Claude Opus 5`, impegno `Alto`, modalità veloce disattivata.
5. Verificare nel selettore dei comandi, senza inviare un prompt, che siano disponibili le cinque
   skill di `augmented-marketing-suite` beta.8.
6. Verificare che `ams-vertical-slice` e `ams-probe` siano inattivi.
7. Se il bundle CURRENT non è disponibile, fermarsi. Il caricamento o la sostituzione del plugin
   richiede una nuova autorizzazione e non appartiene a questo run.

## CURRENT

Creare una chat pulita. Fornire integralmente i cinque file in
`prototypes/ams-vertical-slice/fixture/materials/` e usare gli stessi otto prompt in
`prototypes/ams-vertical-slice/runtime/prompts/`.

Prefissare i primi quattro turni con questi comandi reali:

1. `/augmented-marketing-suite:setup-business-context`
2. `/augmented-marketing-suite:define-marketing-challenge`
3. `/augmented-marketing-suite:choose-marketing-direction`
4. `/augmented-marketing-suite:define-marketing-mix`

Al turno 5 inviare il prompt congelato e aggiungere:

> Usa soltanto capacità CURRENT realmente disponibili. Se manca la capacità di campagna,
> fermati senza simulare il metodo e conserva lo stato necessario all'handoff.

Non proseguire ai turni 6-8 se il candidato si arresta strutturalmente. Non correggere le risposte.

## GENERALIST

1. Disattivare temporaneamente tutte le skill AMS, inclusi CURRENT, Vertical Slice e Probe.
2. Creare una seconda chat pulita con lo stesso modello e lo stesso impegno.
3. Fornire gli stessi cinque materiali e il prompt iniziale comune.
4. Aggiungere soltanto l'istruzione neutrale congelata in `COMPARISON-PROTOCOL.md`.
5. Inviare i turni 2-8 senza adattamenti sostanziali.
6. Al turno 8 fornire il file reale `fixture/simulated-results.md`.

## Congelamento e controlli

Per ogni chat:

1. salvare la risposta dopo ogni turno prima di continuare;
2. esportare il transcript integrale nella cartella `private/`;
3. verificare nei metadati `model: claude-opus-5`, `effort: high` ed entrypoint Claude Desktop;
4. verificare che non risultino scritture, invii, pubblicazioni, spesa o configurazioni;
5. calcolare SHA-256 dei transcript e delle risposte congelate;
6. rimuovere identificativi prima di qualunque sintesi pubblicabile.

Infine ripristinare lo stato precedente: CURRENT attivo, Vertical Slice e Probe inattivi.

## Valutazione

Anonimizzare le tre risposte Claude, includendo la Vertical Slice v0.1.2 già congelata. Usare la
stessa rubrica e una sola valutazione iniziale. Aggiungere repliche soltanto se il risultato Claude
è ambiguo o sostanzialmente diverso tra risposte matched.
