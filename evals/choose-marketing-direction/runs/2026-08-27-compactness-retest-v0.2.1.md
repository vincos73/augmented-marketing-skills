# Retest di compattezza di `choose-marketing-direction` v0.2.1

**Data:** 2026-08-27
**Fixture:** Northline Analytics, interamente sintetica
**Esito:** pass, nessun hard fail

## Correzioni verificate

La patch limita normalmente la prima risposta a 600 parole, elimina duplicazioni e formule tecniche ridondanti e preserva diagnosi, alternative, trade-off, falsificabilità e primo test. Le regressioni osservate durante l'authoring hanno aggiunto tre vincoli: non dedurre rapporti tra metriche scollegate, non restringere un pubblico ancora aperto e usare un nome neutrale per una direzione di apprendimento tra diagnosi concorrenti.

## Risultato osservato

- Prima risposta finale: 526 parole, contro 781 della v0.2.0 nella stessa fixture.
- Tre alternative realmente strategiche, con raccomandazione, trade-off e argomento contrario.
- Pubblico prioritario e due ipotesi causali restano aperti finché le evidenze non li discriminano.
- Gli esiti del test sono collegati alle direzioni conseguenti e a un eventuale problema di prodotto o servizio.
- Nessuna scrittura canonica o azione esterna.

Un marketer strategico senior con almeno quindici anni di esperienza ha confrontato alla cieca la candidata con l'output della v0.2.0, invertendo l'ordine A/B. Un ordine ha preferito la candidata e l'altro la versione precedente. Il punteggio aggregato è identico, 59/60 per entrambe: la candidata guadagna proporzione, mentre il confronto segnala una lieve variabilità nella disciplina probatoria. Non sono emersi errori critici.

## Limite della prova

Il risultato sostiene equivalenza qualitativa con una risposta più corta nella fixture testata. È un eval sintetico di authoring, non una validazione con marketer reali e non autorizza claim pubblici.
