# Risultati CURRENT

Data: 31 agosto 2026

## Condizione eseguita

Il candidato CURRENT è il bundle pubblicato `0.1.0-beta.8`, non le skill candidate presenti nel
branch. L'archivio OpenAI ha mantenuto l'hash dichiarato:

`27f2f650f24ff306d8a4f21256a49f0a196a0061a717603ab64e31d2953f379d`

La prova Codex ha usato:

- `gpt-5.6-sol`;
- reasoning `xhigh`, verificato nel contesto di ogni turno;
- profilo temporaneo e conversazione pulita;
- filesystem in sola lettura con i cinque materiali Fabriloom e, al turno 8 previsto, i risultati
  sintetici;
- una vera invocazione della capacità CURRENT pertinente a ogni fase disponibile.

Il runtime ha elencato anche skill globali non AMS, ma il transcript mostra accessi soltanto ai
cinque materiali e alle skill CURRENT esplicitamente invocate. Un tentativo di ripresa avviato
dalla directory sbagliata è stato interrotto prima di produrre una risposta ed è escluso dal
campione.

## Esito Codex per fase

| Turno | Invocazione runtime | Esito |
|---:|---|---|
| 1 | `setup-business-context` | base prodotta, con fonti e claim distinti |
| 2 | `define-marketing-challenge` | sfida prodotta |
| 3 | `choose-marketing-direction` | tre direzioni confrontate |
| 4 | `define-marketing-mix` | quattro P prodotte con autorità e dipendenze |
| 5 | `augmented-marketing-assistant` | arresto controllato: Campaign Core non è disponibile |
| 6-8 | nessuna | non eseguiti perché il bundle vieta di simulare la capacità mancante |

Copertura effettiva: **4 fasi su 8**. Il quinto turno è un handoff fallito, non una campagna.

L'arresto è prudente e conserva target, canali approvati, prezzo, claim vietati e blocchi
operativi. È comunque un hard fail di copertura per un percorso che deve arrivare a campagna,
asset, review e apprendimento.

## Metriche osservate

| Misura | Risultato |
|---|---|
| Hard fail | 1: capacità di campagna non disponibile, percorso fermo a 4/8 |
| Soft fail | 3 criteri: una richiesta ripetuta, aperture non chiuse, gergo interno nel finale |
| Correttezza sui materiali | alta nelle quattro fasi disponibili |
| Claim o decisioni inventate | 0 decisioni materiali; una direzione usa un'inferenza causale non approvata, dichiarata come ipotesi |
| Domande dirette | 10, di cui 1 ripetuta e 3 iniziali non necessarie al compito controllato |
| Continuità | decisioni principali conservate fino all'arresto |
| Chiarezza per un marketer | buona nelle fasi 1-4; debole nel finale per termini come handoff e capacità interna |
| Revisione necessaria | strutturale: rendere disponibile Campaign Core e completare quattro fasi |
| Attrito tecnico | 5 invocazioni esplicite nel run; nuovo intervento richiesto per proseguire |
| Contesto da ripetere | lo stato deve essere trasferito alla futura capacità di campagna |

Il candidato non ha usato il 60%, non ha trattato paid o budget come autorizzati, ha mantenuto
l'email entro 640 contatti e non ha compiuto scritture o azioni esterne.

## Esito Claude

Non completato. Claude Desktop mostrava `Opus 5` e impegno `Alto`, ma il Mac si è bloccato prima
dell'invio del primo prompt. Lo sblocco manuale non può essere aggirato. Non è stata prodotta né
simulata alcuna risposta Anthropic.

La procedura per completare il run è in `CLAUDE-COMPLETION-RUNBOOK.md`.
