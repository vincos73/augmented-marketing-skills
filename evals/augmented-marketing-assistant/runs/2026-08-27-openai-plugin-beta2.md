# Verifica strutturale del plugin OpenAI beta.2

**Data:** 2026-08-27

**Versione:** 0.1.0-beta.2

**Ambiente verificato:** repository locale e pacchetto estratto

## Difetto osservato nella beta.1

Il caricamento dello ZIP neutro in una chat ChatGPT non ha registrato Augmented Marketing Assistant. La sessione ha inoltre riportato `setup-marketing-system` come non disponibile, pur riconoscendo altre quattro skill.

L'ispezione del pacchetto ha confermato che `setup-marketing-system` era presente, completo e strutturalmente valido. La beta.1 non conteneva però il manifesto `.codex-plugin/plugin.json`; il file `agents/augmented-marketing-assistant.md` non costituiva un componente registrabile dal formato plugin OpenAI.

La causa specifica della scoperta parziale delle cinque skill non è stata dimostrata. La loro presenza nel messaggio della sessione non viene considerata prova di installazione dal pacchetto.

## Correzione

La beta.2 introduce:

- `.codex-plugin/plugin.json` con riferimento a `./skills/`;
- una skill tecnica `augmented-marketing-assistant` che adatta il comportamento dell'agente al formato OpenAI;
- istruzioni che distinguono allegato leggibile, plugin registrato, skill disponibile e caricamento in una nuova chat;
- nessun MCP, connector, hook o componente non necessario.

L'adattatore non possiede metodo o artefatti di marketing. Instrada verso le cinque skill specialistiche e mantiene separati orientamento, decisione e approvazione.

## Controlli superati

- validazione di `skills/augmented-marketing-assistant` con `quick_validate.py`;
- validazione dell'intera radice plugin con `validate_plugin.py`;
- validazione delle altre cinque skill;
- controllo `git diff --check`;
- estrazione dello ZIP e nuova validazione della radice e delle sei skill;
- parità tra cartelle sorgenti e contenuto estratto.

## Limite

La validazione strutturale non dimostra che il plugin sia stato registrato nell'account ChatGPT dell'utente. Occorre installarlo attraverso il catalogo Plugin personale o pubblico e verificarlo in una nuova chat. Un normale allegato ZIP non costituisce questo test.
