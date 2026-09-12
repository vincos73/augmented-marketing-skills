# Installare `content-director` 0.1.2

Questo pacchetto contiene la skill portabile, i suoi riferimenti e i metadati dell'interfaccia. Non contiene dati aziendali o dei test né autorizzazioni a inviare o pubblicare contenuti. La versione `0.1.2` è la sorgente locale revisionata; questo documento non attesta una release pubblica o un'installazione già avvenuta.

Per un'installazione richiesta, estrai la cartella `content-director/` nella destinazione delle skill della piattaforma. In Codex la destinazione personale normalmente è `~/.codex/skills/content-director/`, con `SKILL.md` al suo interno. Prima di sostituire una copia esistente verifica versione e contenuti e conservala per il ripristino. Non copiare dati o cartelle dei test.

Controlla `name: content-director` e `metadata.version: "0.1.2"` nel file principale; se distribuito con lo ZIP, verifica il relativo file SHA256SUMS. Una nuova sessione permette di controllare la disponibilità: la presenza sul disco non dimostra il caricamento in una sessione già aperta.

La skill funziona anche senza le altre componenti della suite. L'accesso alle fonti e la scrittura di file dipendono dall'ambiente e dal compito autorizzato.
