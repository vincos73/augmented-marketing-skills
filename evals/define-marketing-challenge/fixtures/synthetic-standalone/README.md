# Fixture sintetica: Relaybird, calo delle demo

Questa fixture verifica il primo percorso di `define-marketing-challenge` usando i contesti Relaybird già approvati e interamente sintetici.

## Contesti richiesti

- Business Identity: `../../../setup-marketing-system/fixtures/synthetic-standalone/brand-identity.md`
- Marketing Foundations: `../../../setup-marketing-system/fixtures/synthetic-standalone/approved-marketing-foundations.md`

I percorsi sopra sono relativi a questa cartella della fixture. I due artefatti devono essere letti in sola lettura e referenziati tramite entità e versione, non copiati nella sfida.

## Materiali specifici della decisione

- `manager-request.md`: richiesta iniziale della direttrice marketing, con tattica proposta da Sales e vincoli di capacità;
- `performance-snapshot.md`: dati aggregati che mostrano un sintomo ma non ne dimostrano la causa;
- `stakeholder-notes.md`: interpretazioni in conflitto e limiti di prodotto, autorità e budget;
- `user-answers.md`: conferme del responsabile per simulare il secondo turno senza autorizzare scritture;
- `expected-run.md`: comportamenti osservabili attesi nel dry run;
- `forward-test.md`: richiesta indipendente per verificare il riuso della skill dopo l'authoring.

Tutti i nomi, numeri e materiali sono inventati. La fixture non contiene clienti, contatti, prezzi reali o informazioni riservate.

## Isolamento

Il dry run non autorizza scritture in `.agents/marketing/decisions/`, modifiche agli instruction file, configurazioni, spesa o attività esterne. Se serve rendere osservabile un artefatto, restituirlo soltanto nella risposta o in un workspace temporaneo esplicitamente non canonico.
