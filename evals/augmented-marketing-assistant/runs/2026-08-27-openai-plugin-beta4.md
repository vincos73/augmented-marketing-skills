# Verifica di Augmented Marketing Suite beta.4

**Data:** 2026-08-27

**Versione:** 0.1.0-beta.4

**Ambiente verificato:** repository locale e pacchetto estratto

**Riscontro runtime aggiuntivo:** primo test manuale in Codex riferito dall'utente

## Correzione verificata

La beta.4 distingue tre stati che la beta.3 trattava come equivalenti:

1. skill presente nel pacchetto;
2. skill caricata nella conversazione;
3. handoff dalla skill attiva alla skill specialistica consentito dall'ambiente.

Augmented Marketing Assistant attiva la skill pertinente soltanto quando il terzo stato è osservabile. Se la skill risulta presente ma l'handoff non è disponibile, indica all'utente il nome tecnico esatto da invocare e si ferma senza formulare domande, bozze o raccomandazioni appartenenti alla skill specialistica.

## Naming dell'interfaccia

I titoli visibili delle cinque skill specialistiche coincidono con i rispettivi nomi tecnici:

- `setup-business-context`;
- `setup-marketing-system`;
- `define-marketing-challenge`;
- `choose-marketing-direction`;
- `define-marketing-mix`.

Le descrizioni e i prompt iniziali restano in italiano. Augmented Marketing Assistant conserva il proprio nome pubblico inglese.

## Regressione sintetica

**Richiesta:** “Voglio posizionare un nuovo servizio formativo.”

**Comportamento accettato:**

- l'ambiente seleziona direttamente `define-marketing-challenge`; oppure
- se Augmented Marketing Assistant è già attivo e non può effettuare l'handoff, indica `define-marketing-challenge`, chiede di invocarla direttamente e si ferma.

**Hard fail:** l'Assistant riconosce la skill corretta ma ne simula il metodo, formula la sfida o prosegue con le sue domande.

## Controlli strutturali superati

- validazione del manifesto `.codex-plugin/plugin.json`;
- validazione delle sei skill;
- controllo sintattico JSON e YAML;
- controllo `git diff --check`;
- estrazione dello ZIP e nuova validazione;
- parità tra sorgente e contenuto estratto;
- assenza di MCP, connector, hook e automazioni nel pacchetto.

## Riscontro manuale in Codex

Dopo l'installazione, l'utente ha riferito che l'Assistant “sembra funzionare” nel routing. Il riscontro è coerente con il comportamento atteso della beta.4 ed è un segnale positivo, ma non viene classificato come PASS riproducibile perché non sono stati conservati in questo run la richiesta completa, la risposta e l'evidenza tecnica dell'effettivo caricamento della skill specialistica.

La parità tra la sorgente dell'adattatore `skills/augmented-marketing-assistant` e la copia installata in Codex è stata verificata con `diff -qr` senza differenze.

Il successivo [smoke test runtime in Codex](2026-08-27-codex-runtime-smoke-beta4.md) ha coperto i tre casi definiti nel catalogo degli scenari. Ha dimostrato il caricamento diretto di `choose-marketing-direction` e il passaggio reale dall'Assistant a `define-marketing-challenge`. La richiesta completamente generica ha invece prodotto un soft fail perché la domanda non contemplava un'attività già definita.

## Limite

La verifica strutturale e lo smoke test Codex non dimostrano che ChatGPT o Codex selezionino sempre la skill attesa. Prima del micro-pilot resta da correggere e ritestare il soft fail della richiesta generica; il comportamento va poi verificato con persone poco tecniche.
