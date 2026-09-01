# Contratto del riepilogo di passaggio

Il riepilogo è l'unico input trasmesso alla skill successiva. Non riporta l'output completo, non finge che esista un file canonico e non autorizza alcuna azione.

```markdown
## Riepilogo di passaggio

- Passaggio concluso: <nome skill e versione letta>
- Entità: Fabriloom, azienda sintetica B2B
- Stato del contenuto: `confermato in chat`
- Versione conversazionale: `chat-v1`
- Salvataggio canonico: `negato`; nessun percorso `.agents/` esiste o è stato letto
- Installazione nelle istruzioni: `non applicabile dopo salvataggio negato` oppure `negata`
- Autorizzazione all'esecuzione: `negata`
- Decisioni confermate: <solo decisioni necessarie, con base [S#] o [C]>
- Prove e limiti: <fonti, claim vietati, conflitti, dati non comparabili>
- Vincoli e capacità: <limiti quantitativi e loro stato>
- Ruoli e autorità: <Legal, Finance, Sales, Growth Operations, Operations, Marketing Director>
- Aspetti aperti: <incertezze che non sono state risolte>
- Conseguenza per il passaggio successivo: <cosa può essere esplorato, non approvato o non eseguito>
```

## Regole di interpretazione

1. `confermato in chat` non equivale a `approvato` come stato canonico e non permette di chiamare l'output `v1`.
2. La skill ricevente può riusare soltanto decisioni, prove, vincoli, ruoli e aspetti aperti espressamente elencati. Se manca una base indispensabile, produce una bozza prudente o un blocker, senza inventare il documento a monte.
3. Un rifiuto di salvataggio non autorizza l'installazione. Per Business Identity e Fondamenti, l'installazione va comunque nominata e separata quando applicabile; nel caso simulato è impossibile perché non esiste un artefatto da referenziare.
4. L'approvazione del contenuto non autorizza test esterni, spesa, paid media, modifiche operative, configurazioni, contatti, produzione o pubblicazione.
5. Il passaggio non trasferisce i dati personali o gli eventuali dettagli sensibili delle fonti. Qui non sono presenti dati reali.
