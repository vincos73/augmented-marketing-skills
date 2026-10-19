# Monitoraggio — stato della distribuzione autonoma

19 ottobre 2026. Progetto approvato dall’utente: **setup-monitoring prepara il piano; activate-monitoring lo esegue con un esecutore unico e file Markdown nella cartella dell’utente**. SQLite e il vincolo di tre agenti sono rimossi da questa nuova distribuzione. Un aiuto specialistico è facoltativo; i limiti complessivi restano quelli del piano.

## Sorgenti autorevoli

- [setup-monitoring 0.1.2](releases/activate-monitoring/0.1.0/source/setup-monitoring/SKILL.md)
- [activate-monitoring 0.1.0](releases/activate-monitoring/0.1.0/source/activate-monitoring/SKILL.md)
- [Distribuzione, download e requisiti](releases/activate-monitoring/0.1.0/README.md)

Queste due skill sono distribuite separatamente dai pacchetti Suite OpenAI 1.0.2 e Claude/italiano 1.0.0. La loro sorgente sta nella cartella della distribuzione autonoma, non viene aggiunta implicitamente all’inventario dei vecchi bundle. Nessuna nuova versione dei plugin della Suite o candidatura al catalogo ChatGPT è compresa in questo incarico.

## Comportamento

L’esecutore riusa piano, versione, criteri, fonti e autorizzazioni applicabili senza rifare il setup. Usa ricerca aperta e fonti previste, verifica le prove, confronta lo storico e salva riepilogo/report/registro. Titolo e data originali possono sostenere una scheda limitata; snippet e riassunti del motore restano piste. Le informazioni importanti già lette non devono sparire senza esito.

La cartella viene scelta dall’utente e risolta nell’ambiente reale. `monitoring-plan.md` conserva le decisioni, `registro.md` la continuità e `report/` i risultati. Stato del controllo e stato di consegna sono separati; rettifiche e lacune restano visibili. Un database delle preview precedenti non viene importato o modificato automaticamente.

Accesso persistente ai file e riavvio programmato dipendono dalle capacità osservate dell’ambiente. In loro assenza non si dichiara uno storico automatico o un monitoraggio attivo. La ricorrenza richiede autorizzazione applicabile e un meccanismo effettivo; la sola configurazione non prova un avvio. Email facoltativa soltanto con plugin disponibile, destinatari/contenuto definiti e invio autorizzato.

## Verifiche e confini

Per richiesta dell’utente non vengono ripetuti confronti di ricerca o test comportamentali. La verifica di distribuzione riguarda struttura, riferimenti, sorgenti, ZIP e checksum. Non certifica qualità del web, caricamento in una nuova sessione, funzionamento desktop o ricorrenza. Nessun monitoraggio reale, invio email o archivio operativo viene creato durante la pubblicazione.

Le vecchie preview e le prove locali rimangono materiale storico distinto e non vengono incluse negli ZIP. La preview.10 non aveva dimostrato un vantaggio stabile sul generalista; questa uscita non rivendica quel vantaggio. Il valore proposto è il percorso completo da piano a continuità dei risultati, con minore coordinamento.

Lo stato effettivo della pubblicazione è verificabile nella [release GitHub activate-monitoring-v0.1.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/activate-monitoring-v0.1.0). Una release GitHub non implica disponibilità nel catalogo ChatGPT o installazione locale.
