# Fixture sintetica standalone: Fabriloom

Fabriloom è un'impresa B2B interamente inventata per valutare `design-campaign`. Nomi, persone, dati, clienti, offerte e decisioni sono sintetici e pubblicabili.

La fixture simula una Marketing Director che vuole progettare una campagna partendo direttamente da materiali aziendali, senza Business Identity, Marketing Foundations, Brief della sfida, Direzione o Marketing Mix canonici.

## Obiettivo del test

Verificare che la skill:

- offra valore senza imporre il percorso Strategy Core;
- ricavi una prima architettura prima di porre domande;
- distingua obiettivo aziendale, obiettivo di campagna, output e outcome;
- limiti claim, target e budget alla base disponibile;
- colleghi canali, asset, CTA, conversione, capacità e misurazione;
- separi approvazione della Campaign Spec e prontezza all'esecuzione;
- non salvi, pubblichi, invii o modifichi sistemi durante il test.

## Materiali della simulazione

- `manager-request.md`: richiesta iniziale della Marketing Director, con target e claim da verificare;
- `offer-brief.md`: offerta corrente, pubblico possibile, prezzo, capacità ed esclusioni;
- `evidence-and-claims.md`: registro delle prove e limiti di utilizzo pubblico;
- `operations-and-channels.md`: capacità, canali, percorso di conversione, privacy e autorizzazioni;
- `prior-campaign-snapshot.md`: dati di una campagna precedente, utili ma non direttamente equivalenti;
- `user-answers.md`: risposte simulate ai chiarimenti e approvazione in chat; non va fornito nel forward test del primo turno;
- `expected-run.md`: baseline qualitativa dell'autore; non va fornita al generatore o al valutatore indipendente;
- `expected-campaign-spec.md`: esempio di contenuto atteso dopo le risposte, non artefatto canonico;
- `forward-test.md`: prompt e confini del forward test.

## Isolamento

Il test è in sola lettura. Non autorizza:

- scritture in `.agents/marketing/decisions/`;
- creazione o modifica di Identity, Foundations o artefatti Strategy;
- invio di email, pubblicazione social o apertura di iscrizioni;
- acquisto media, allocazione di budget o modifica di account;
- contatto con clienti, prospect o persone citate nei materiali.

Un output eventualmente approvato resta `contenuto approvato in chat; artefatto non creato` oppure viene scritto soltanto in un percorso temporaneo esplicitamente isolato da un test successivo.

## Classificazione

Tutti i file sono sintetici e pubblicabili. Non aggiungere dati reali, contatti, credenziali, risultati di clienti, listini riservati o appunti commerciali a questa directory.
