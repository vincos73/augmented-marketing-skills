# Verifica strutturale di Augmented Marketing Suite beta.3

**Data:** 2026-08-27

**Versione:** 0.1.0-beta.3

**Ambiente verificato:** repository locale e pacchetto estratto

## Decisione di naming

La beta.3 adotta **Augmented Marketing Suite** come nome del prodotto e del plugin (`augmented-marketing-suite`). **Augmented Marketing Assistant** resta l'ingresso conversazionale (`augmented-marketing-assistant`) incluso nella Suite.

La rinomina non modifica il metodo dell'Assistant, i nomi delle cinque skill specialistiche, i loro artefatti o i gate di approvazione.

## Controlli superati

- validazione del manifesto `.codex-plugin/plugin.json` con `validate_plugin.py`;
- validazione delle sei skill con `quick_validate.py`;
- controllo sintattico JSON del manifesto;
- controllo `git diff --check`;
- verifica dell'identificatore `augmented-marketing-suite` e del nome visualizzato `Augmented Marketing Suite`;
- estrazione dello ZIP e nuova validazione della radice e delle sei skill;
- parità tra i file distribuibili della sorgente e il contenuto estratto;
- assenza di MCP, connector, hook e automazioni nel pacchetto.

## Limite

La validazione strutturale non dimostra l'installazione nel catalogo Plugin di ChatGPT, il caricamento delle skill in una nuova chat o la comprensibilità presso marketer esterni. Questi aspetti richiedono test separati.

Poiché l'identificatore del plugin cambia rispetto alla beta.2, un'installazione precedente può convivere come plugin distinto. Le istruzioni richiedono quindi di rimuovere Augmented Marketing Assistant beta.2 prima di installare Augmented Marketing Suite beta.3.
