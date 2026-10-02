# Installare `write-marketing-copy` 0.1.6-l10n.1

La sorgente contiene la skill, i suoi riferimenti e i metadati dell'interfaccia OpenAI. Gli ZIP portabili escludono tali metadati; il plugin OpenAI li conserva. Non contiene dati aziendali o dei test né autorizzazioni a inviare o pubblicare contenuti. La versione `0.1.6-l10n.1` è la candidata locale della sorgente; non è una release pubblicata né un'installazione già avvenuta.

Per un'installazione richiesta, estrai la cartella `write-marketing-copy/` nella destinazione delle skill della piattaforma. In Codex la destinazione personale normalmente è `~/.codex/skills/write-marketing-copy/`, con `SKILL.md` al suo interno. Prima di sostituire una copia esistente verifica versione e contenuti e conservala per il ripristino. Non copiare dati o cartelle dei test.

Controlla `name: write-marketing-copy` e `metadata.version: "0.1.6-l10n.1"` nel file principale; per gli ZIP verifica il relativo file SHA256SUMS, anche quando si tratta di una candidata locale. Una nuova sessione permette di controllare la disponibilità: la presenza sul disco non dimostra il caricamento in una sessione già aperta.

La skill funziona anche senza le altre componenti della suite. L'accesso alle fonti e la scrittura di file dipendono dall'ambiente e dal compito autorizzato.
