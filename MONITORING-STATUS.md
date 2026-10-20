# Monitoraggio — stato della distribuzione autonoma

20 ottobre 2026. Distribuzione aggiornata: **setup-monitoring 0.1.3** prepara il piano; **activate-monitoring 0.1.1** lo esegue con un esecutore unico e file Markdown nella cartella dell’utente. Nessun database, eseguibile aggiuntivo o gruppo obbligatorio di agenti.

## Sorgenti autorevoli

- [setup-monitoring 0.1.3](releases/activate-monitoring/0.1.1/source/setup-monitoring/SKILL.md)
- [activate-monitoring 0.1.1](releases/activate-monitoring/0.1.1/source/activate-monitoring/SKILL.md)
- [Distribuzione e download](releases/activate-monitoring/0.1.1/README.md)
- [Verifica di struttura e pacchetti](releases/activate-monitoring/0.1.1/verification.json)

**Pubblicazione GitHub verificata il 20 ottobre 2026:** [release `activate-monitoring-v0.1.1`](https://github.com/vincos73/augmented-marketing-skills/releases/tag/activate-monitoring-v0.1.1), sorgente al commit `7cbdba033318e2d57d032dacba41e8d91eab8435`, quattro asset pubblici: due ZIP, manifest e checksum. Download anonimi, CRC, checksum e corrispondenza degli otto file sorgente al tag verificati; [riscontro della pubblicazione](releases/activate-monitoring/0.1.1/publication.json). Installazione sul Mac dell’autore eseguita e confrontata con gli stessi pacchetti pubblici; non certifica una futura esecuzione programmata. I vecchi sorgenti e asset della [0.1.0](releases/activate-monitoring/0.1.0/README.md) restano invariati. Le due skill sono distribuite separatamente dai plugin Suite OpenAI 1.0.2 e Claude/italiano 1.0.0; nessuna nuova versione della Suite o pubblicazione nel catalogo ChatGPT è compresa in questo aggiornamento.

## Correzioni dal test reale

Il passaggio da setup ad activate è esplicito e riusa approvazione, piano, cartella e limiti. Ogni prompt programmato richiama `$activate-monitoring`, legge piano e registro e identifica la fase da svolgere senza ricreare la programmazione.

La conferma distingue programmazione attiva, primo controllo eseguito e prima consegna osservata. Una routine salvata non prova che il monitoraggio sia già riuscito o che il riepilogo sia arrivato puntualmente.

Un riepilogo richiesto alle 05:00 resta una consegna alle 05:00. Acquisizione e verifica iniziano prima, con un termine e un margine scelti nel piano. Quando servono due fasi, la preparazione salva report e sintesi; la consegna legge quel risultato per data, ciclo e versione senza avviare un’altra ricerca. Un report mancante o parziale viene dichiarato, non sostituito da un risultato precedente o da «nessuna novità».

La puntualità dipende dalle capacità dell’ambiente; per file locali occorrono computer e app disponibili. [Documentazione ufficiale sulle attività programmate](https://learn.chatgpt.com/docs/automations).

## Continuità e confini

La cartella dell’utente contiene `monitoring-plan.md`, `registro.md` e `report/`. Rimangono ricerca aperta, verifica degli originali, confronto con lo storico, rettifiche e lacune. Email soltanto con strumenti e autorizzazioni applicabili. I dati operativi dell’utente non vengono pubblicati nel repository della skill.

Le verifiche di questa uscita riguardano istruzioni, struttura, riferimenti, parità sorgenti/ZIP, checksum e compatibilità del packaging con la precedente release. Non sono stati ripetuti confronti di ricerca o test comportamentali. L’aggiornamento di routine e installazioni locali è distinto dalla prova di una futura esecuzione programmata.

Le preview e gli esperimenti storici rimangono separati. La preview.10 non aveva dimostrato un vantaggio stabile sul generalista; questa distribuzione non rivendica quel vantaggio. Il valore proposto è il percorso da piano a continuità dei risultati, con minore coordinamento.

Per la manutenzione: `python3 scripts/build_monitoring_release.py --release-version 0.1.1 --check`; la stessa opzione con `0.1.0` verifica i pacchetti storici senza modificarli.
