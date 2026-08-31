# Runbook Claude - AMS Vertical Slice v0.1.2

Questo runbook si usa soltanto dopo l'autorizzazione esplicita a trasmettere la fixture sintetica
al servizio Anthropic.

## Preparazione osservabile

1. Aprire Claude Desktop, `Impostazioni > Personalizza > Plugin`.
2. Annotare versione e stato di Augmented Marketing Suite.
3. Disabilitare temporaneamente la suite corrente per evitare competizione di selezione; non
   rimuoverla.
4. Caricare `dist/ams-vertical-slice-claude-v0.1.2.zip` tramite il canale plugin dell'app.
5. Verificare che compaiano `/ams-vertical-router` e gli otto specialisti.
6. Aprire una nuova chat e annotare modello, skill usata e file letti.

## Run VERTICAL

- Allegare i cinque file di `fixture/materials/` e inviare `runtime/prompts/vertical-turn-01.txt`.
- Inviare in ordine i prompt 02-07, uno per turno.
- Dopo `direction`, usare `/compact` quando disponibile; chiedere di riportare fase, conferme e
  punti aperti e verificare `SLICE_CONTINUITY: playbook-reread`.
- Rendere disponibile `fixture/simulated-results.md` e inviare il prompt 08.
- Salvare le risposte integrali, i marker, lo stato e gli indicatori dell'interfaccia.

## Specialista manuale

In una chat nuova invocare `/ams-vertical-slice:review-campaign` con il contenuto di
`runtime/prompts/manual-review.txt` senza la prima frase Codex. Verificare:

- `SLICE_SPECIALIST: review-campaign` presente;
- `SLICE_PLAYBOOK: review` presente;
- `STATO_VERTICAL_SLICE` assente;
- nessun altro specialista usato.

## Ripristino

1. Disabilitare AMS Vertical Slice.
2. Riabilitare Augmented Marketing Suite nella versione annotata.
3. Riavviare Claude Desktop e verificare che la suite corrente sia attiva.
4. Non rimuovere plugin o chat senza conferma dell'utente.
