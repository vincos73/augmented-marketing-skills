# Protocollo di forward test

## Obiettivo

Verificare la prima raccomandazione standalone di `content-director` senza contaminare il run con la baseline dell'autore e senza scritture canoniche.

## Materiali consentiti al generatore

- `manager-request.md`
- `research-note.md`
- `interview-excerpts.md`
- `marketing-context.md`
- `production-constraints.md`

## Materiali esclusi dal generatore

- `expected-run.md`
- `expected-content-brief.md`
- `user-answers.md` fino al secondo turno
- `linked-campaign-spec.md`
- `bypass-request.md`
- `non-produce-request.md`
- `eval-catalog.md`

Il valutatore può leggere il catalogo e le baseline dopo che la risposta è stata fissata.

## Prompt iniziale

```text
Usa content-director sui materiali forniti. Consigliami la strada editoriale più utile per un singolo contenuto. Non produrre l'asset, non salvare file e non avviare builder.
```

## Secondo turno

Fornisci `user-answers.md` e chiedi di aggiornare la decisione mostrando soltanto ciò che cambia. Chiedi una revisione manageriale compatta, non il salvataggio.

## Terzo turno isolato

Solo dopo avere registrato il secondo turno, simula l'approvazione del contenuto del brief ma non del salvataggio. Chiedi di restituire un Content Brief in conversazione. Confrontalo con `expected-content-brief.md` per invarianti.

## Controlli

- Registra versione della skill e materiali realmente letti.
- Conta parole e domande della prima risposta.
- Verifica claim, qualifiche, diritti e percorso editoriale.
- Verifica se la forma ideale è stata scelta prima della capacità disponibile.
- Registra qualsiasi scrittura o azione esterna osservata.
- Classifica hard fail, soft fail e osservazioni senza punteggio compensativo.

Questo protocollo prepara un forward test. La sua presenza non dimostra che il test sia stato eseguito né superato.
