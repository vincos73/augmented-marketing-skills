# Monitoraggio — stato della distribuzione autonoma

20 ottobre 2026. Versioni aggiornate: **setup-monitoring 0.1.4** prepara il piano; **activate-monitoring 0.1.2** lo esegue con un esecutore unico e file Markdown nella cartella dell’utente.

## Sorgenti e distribuzione

- [setup-monitoring 0.1.4](releases/activate-monitoring/0.1.2/source/setup-monitoring/SKILL.md)
- [activate-monitoring 0.1.2](releases/activate-monitoring/0.1.2/source/activate-monitoring/SKILL.md)
- [Distribuzione e ZIP](releases/activate-monitoring/0.1.2/README.md)
- [Verifiche di struttura e pacchetti](releases/activate-monitoring/0.1.2/verification.json)
- [Release GitHub activate-monitoring-v0.1.2](https://github.com/vincos73/augmented-marketing-skills/releases/tag/activate-monitoring-v0.1.2)

Le distribuzioni precedenti 0.1.0 e 0.1.1 restano archiviate senza riscrivere sorgenti o asset. Queste skill autonome non modificano i plugin della Suite o il catalogo ChatGPT.

## Comportamento approvato

Una sola programmazione avvia l'intero lavoro. Nella stessa esecuzione l'agente cerca, verifica gli originali, confronta lo storico, salva report e registro e consegna il riepilogo appena termina. Comunica «avvio alle …, consegna al termine»; non introduce una seconda routine per la preparazione o l'invio.

Il passaggio da setup ad activate è esplicito e riusa piano, cartella, limiti e autorizzazioni. Ogni prompt programmato richiama `$activate-monitoring` e legge piano e registro, senza ricreare la programmazione. Un'ora precisa di ricezione ancora richiesta va chiarita prima di adottare la modalità con consegna al termine.

La conferma distingue programmazione attiva, primo controllo eseguito e prima consegna osservata. Una routine salvata non prova che il controllo o la consegna siano già avvenuti.

La cartella dell'utente contiene `monitoring-plan.md`, `registro.md` e `report/`. Rimangono ricerca aperta, verifica degli originali, rettifiche, lacune e continuità. Nessun database, eseguibile aggiuntivo, plugin di ricerca o gruppo obbligatorio di agenti.

Per file locali occorrono computer e app disponibili: [documentazione ufficiale](https://learn.chatgpt.com/docs/automations). Un monitoraggio su richiesta non sostituisce silenziosamente una ricorrenza richiesta. Email soltanto con strumenti e autorizzazioni applicabili.

## Verifiche e confini

La verifica della distribuzione riguarda istruzioni, struttura, riferimenti, parità fra sorgenti e ZIP, checksum e compatibilità del packaging storico. Nessun nuovo confronto di ricerca o test comportamentale; la pubblicazione e l'installazione non provano una futura esecuzione programmata. I dati operativi dell'utente non vengono pubblicati nel repository della skill.

Le preview e gli esperimenti storici restano separati. La preview.10 non aveva dimostrato un vantaggio stabile sul generalista; questa distribuzione non rivendica quel vantaggio. Il valore proposto è il percorso da piano a continuità dei risultati, con minore coordinamento.

Manutenzione: `python3 scripts/build_monitoring_release.py --release-version 0.1.2 --check`. Le opzioni `0.1.0` e `0.1.1` verificano i pacchetti precedenti senza modificarli.
