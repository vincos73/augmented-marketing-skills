# Specifica runtime e readiness

Questa matrice separa cinque tipi di prova che non si compensano tra loro:

1. `static_only`: struttura e regressioni statiche della sorgente;
2. `observed_unverified`: comportamento osservato senza provenance host completa;
3. `provenance_verified`: run comportamentale collegato a capture e receipt host esterne verificate;
4. `runtime_loaded_verified`: pacchetto candidato installato e caricato su una superficie runtime identificata;
5. `pilot_verified`: uso completato da almeno un marketer reale con evidenza esterna.

`not_run` indica assenza di prova. Gli assi comportamento, runtime e pilot restano separati: un run osservato non prova il caricamento, un caricamento non prova il comportamento end-to-end e nessuno dei due prova un pilot.

## Evidenze

- Le evidenze `repository` possono avere soltanto tipo `static_structure` o `static_regression`, devono risolversi dentro il repository e non possono sostenere stati runtime, comportamentali o pilot.
- Le evidenze `external` usano riferimenti neutrali `external://...`. Per `observed_unverified` il riferimento resta esplicitamente non verificato.
- Gli stati `provenance_verified`, `runtime_loaded_verified` e `pilot_verified` richiedono evidenze `external_verified` risolte da un indice esterno fornito al checker. Path privati, thread id e receipt positive non appartengono al report pubblicabile.
- Un run a nove skill con provenance richiede un envelope esterno digestato che collega candidata, manifest, superficie, capture manifest, raw e snapshot. Il checker riesegue i controlli di provenance e grounding sui file indicati; due soli flag `pass` non costituiscono prova.
- `packaged_candidate` è distinto da `source_candidate`. Richiede package root esterna, manifest con le nove skill esatte, parità dei digest, archivio e checksum ricomputabili. Se `package_state` è `not_built`, package parity, candidate readiness, runtime verificati e pilot non possono essere promossi.
- Package root e ZIP devono avere l'albero esatto derivato dal manifest candidato: nessuna skill, directory o file extra o mancante; nessun duplicato, path traversal o symlink; byte identici tra sorgente, root e archivio.
- Il registro issue usa priorità esatte `P0`, `P1`, `P2`, `P3`. Valori come `critical`, `P0 `, `null` o campo mancante invalidano il record. Un P0/P1 è chiuso soltanto con stato `closed` o `resolved`; qualsiasi altro stato mantiene il gate non soddisfatto. `source_system` è un identificatore canonico, non vuoto e già trimmato. La allowlist corrente ammette soltanto `external-issue-tracker-export`; valori auto-dichiarati come `self_asserted`, varianti di maiuscole, spazi finali, solo whitespace o sistemi sconosciuti invalidano la prova e mantengono falsi i flag di readiness dipendenti.
- `runtime_loaded_verified` richiede due prove esterne distinte: receipt di installazione e capture di caricamento, entrambe legate allo stesso package candidato, alla stessa superficie e allo stesso checksum. ID non vuoti e globalmente univoci; timestamp RFC 3339 timezone-aware; `install_at <= load_at`.
- `pilot_verified` richiede un `installed_package`, un runtime caricato coerente e un record esterno strutturato di almeno una sessione completata da un marketer reale. Vale `runtime_loaded_at <= started_at <= finished_at <= completed_at` sulla stessa candidata, package e superficie. `completed_at` deve inoltre seguire strettamente tutti i prerequisiti verificati.
- Gli ID canonici sono stringhe non vuote, già trimmate e univoche nel proprio perimetro. Questo vale anche per record, prerequisiti, gate, riferimenti a record, eventi e sessioni. Gate duplicati falliscono anche se le due voci sono identiche.
- `candidate_id`, source base commit, versione di `campaign-review` e suite base devono coincidere con allowlist e manifesti plugin sorgente. Questa verifica identifica la base, ma non promuove né modifica il plugin.

## Prerequisiti

- `provenance_verified` sull'asse comportamento accetta soltanto `behavioral_capture`, richiede una precedente osservazione dello stesso candidato e una regressione statica PASS.
- `runtime_loaded_verified` accetta soltanto `install_receipt` e `runtime_load_capture`, richiede osservazione precedente dello stesso package sulla stessa superficie, identità del pacchetto installato collegata alla candidata e prova esterna di installazione e caricamento.
- `pilot_verified` richiede il run candidato a nove skill con provenance, assenza verificata di P0/P1 e package parity/checksum.

Il checker può validare la matrice corrente senza indice esterno perché nessuno stato verificato è dichiarato. Un futuro stato verificato deve essere controllato con:

```text
python3 evals/robustness/runtime-readiness/scripts/check_readiness.py \
  --external-evidence-index /percorso/esterno/evidence-index.json
```

L'indice esterno non viene conservato nel repository. Ogni voce collega un riferimento neutrale a un file esterno, al suo SHA-256 e al tipo di prova. Il checker verifica esistenza, collocazione esterna, digest e contenuto minimo del report di prova.

Nel runner unificato lo stesso indice viene passato con `--readiness-evidence-index`. È distinto da `--capture-manifest`, `--raw` e `--snapshot`: il primo risolve tutte le prove della matrice, gli altri tre alimentano il run comportamentale corrente.

JSON minimi con soli flag `pass`, contatori P0/P1 o booleani di parità vengono respinti. JSON secondari malformati o con UTF-8 invalido, incluso l'indice esterno, producono errori strutturati e non traceback. Il checker ricomputa la capture a nove skill, l'intero albero del package root e dello ZIP, il checksum dell'archivio, le cronologie e i legami package-superficie-pilot. L'autenticità dell'exporter host o del sistema esterno resta un trust boundary: in produzione l'indice deve provenire dal processo di cattura autorizzato, non da un file redatto dal candidato.

## Readiness

La prossima beta candidata richiede tutti questi gate:

- suite statica PASS;
- forward test Review→Debrief compattato PASS;
- run delle nove skill candidate con provenance verificata su almeno un runtime;
- nessun P0 o P1 aperto;
- package parity e checksum verificati.

Cross-runtime refresh e pilot reale sono gate successivi espliciti. La validità strutturale della matrice non rende soddisfatto nessuno di questi gate.
