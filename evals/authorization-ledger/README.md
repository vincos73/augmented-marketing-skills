# Ledger di approvazione e autorizzazione

Questo eval conserva quattro transizioni distinte: approvazione del contenuto, salvataggio, installazione ed esecuzione. Un consenso sul contenuto non concede le azioni successive.

Il contratto v2 aggiunge una matrice ruolo-azione esplicita:

- `Marketing Director` per `approve_content`;
- `Repository Maintainer` per `write_file`;
- `Runtime Administrator` per `install`;
- `Campaign Operator` per `execute`.

Un ruolo non previsto, incluso `Intern`, fallisce. Decisione e osservazione restano separate. Un'azione negata, non richiesta o non applicabile non può essere marcata osservata; la provenienza simulata non può essere promossa.

## Profili

`fixtures/fabriloom-valid/ledger.json` rappresenta `chat-v1`: l'identità conversazionale è separata, gli artefatti non sono creati, `path` e `digest` sono null in tutti i record.

`fixtures/fabriloom-valid/persistent-ledger.json` esercita il profilo persistente. Per ogni record persistente il checker risolve il file e ricalcola SHA-256. La catena saving-installation-execution deve conservare la stessa identità, versione, path e digest, oltre alle dipendenze esplicite.

Gli identificatori condivisi di claim, testimonianza, capacità, tracking e paid media sono dichiarati in `shared_invariant_ids` con gli stessi valori usati da common state, cross-Core e lineage.

## Regole principali

| Regola | Controllo |
|---|---|
| L001 | struttura, vocabolari e identificatori condivisi |
| L002 | quattro transizioni nell'ordine previsto |
| L003 | separazione tra decisione e azione osservata |
| L004 | una sola azione nello scope del passaggio |
| L006 | divieto di ereditare autorità |
| L007 | provenienza simulata conservata |
| L008 | path risolvibile e digest ricalcolato |
| L009 | catena identity-version-path-digest |
| L010 | soggetto, tempo ed evidenza dell'osservazione |
| L011 | id e dipendenze risolti |
| L012 | evidenze file, receipt e log risolvibili |
| L013 | matrice ruolo-azione |
| L014 | semantica `chat-v1` e digest null |

## Esecuzione

    python3 evals/authorization-ledger/scripts/check_ledger.py --oracle evals/authorization-ledger/oracles/cases.json

L'oracolo comprende i due casi positivi e le regressioni obbligatorie `intern-role-rejected` e `fake-digest-rejected`. Il checker usa soltanto la libreria standard e non installa né esegue artefatti.
