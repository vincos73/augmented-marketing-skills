# setup-brand-voice — stato della prima versione

Aggiornato il 12 settembre 2026. Nome scelto dall'utente: **setup-brand-voice**. Versione inclusa nella Suite: **0.1.2**.

## Risultato

È stata progettata e creata una sola skill che proporziona il lavoro a sei condizioni: guida approvata, guida parziale, materiali senza guida, assenza di materiali, voce da ripensare e materiali contraddittori. Conserva le differenze tra gruppo, brand, persona, lingua e contesto. Il risultato può essere un riferimento recepito, una nuova guida o una revisione circoscritta.

I learning della suite sono incorporati: prima risposta utile, poche decisioni, avanzamento per differenza, fonti separate dalle proposte, approvazioni circoscritte, rispetto delle autorizzazioni già date e uso autonomo senza onboarding obbligatorio. La ricerca esterna ha informato la progettazione senza diventare una dipendenza operativa.

## File da cui riprendere

- [Progetto e decisioni](blueprints/setup-brand-voice/blueprint.md).
- [Skill sorgente](skills/setup-brand-voice/SKILL.md), con quattro riferimenti e metadati dell'interfaccia.
- [ZIP portabile 0.1.2](dist/beta.11/agent-skills/setup-brand-voice-0.1.2.zip), [manifest e checksum della Suite](dist/beta.11/manifest.json).
- [Rapporto delle prove](evals/setup-brand-voice/runs/2026-09-07/report.md), [protocollo](evals/setup-brand-voice/runs/2026-09-07/protocol.md) e [catalogo](evals/setup-brand-voice/eval-catalog.md).

## Verifica

Eseguite 10 prove indipendenti, 20 turni, quattro aziende sintetiche. I primi run hanno trovato una modifica tipografica a una clausola protetta, fatti impliciti non sostenuti in formule di cortesia e un'indicazione troppo ampia sulle battute. Le risposte iniziali sono conservate. Le istruzioni sono state corrette e i punti interessati riprovati con nuovi agenti.

Tre run su candidati precedenti risultano FAIL; sette risultano PASS, uno con soft fail poi recuperato. Nei tre run finali non sono stati rilevati errori nei punti verificati. Il rapporto mantiene distinti candidati, copertura, risultati testuali e verifiche fisiche. Non tutti i 16 scenari del catalogo sono stati eseguiti autonomamente.

Verificati un salvataggio realmente autorizzato in una cartella temporanea, metadati, riferimenti, integrità del pacchetto e parità con i sorgenti. Esito complessivo: **PASS CON RISERVA come prima versione locale**; efficacia e riconoscibilità su un brand reale restano da verificare.

## Distribuzione e lavoro successivo

La skill è inclusa nella Suite beta.11, nei suoi ZIP portabili e nel pacchetto OpenAI/Codex installato localmente. Il commit, push e release della Suite accompagnano questa pubblicazione. Il salvataggio di prova non è una guida aziendale reale.

Il prossimo uso utile è una prova guidata con materiali di un brand reale. Per un uso esteso restano le varianti di regressione indicate nel rapporto, l'aggiornamento di una guida su disco e il confronto con un generalista. Le revisioni future devono partire dai sorgenti e dal manifest finale, preservando i run già congelati.

Il digest del pacchetto è registrato nel [manifest beta.11](dist/beta.11/manifest.json); le fonti di ricerca storiche restano fuori dal repository di release.
