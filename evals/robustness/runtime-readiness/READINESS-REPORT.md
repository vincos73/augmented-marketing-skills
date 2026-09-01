# Snapshot pre-package della candidata beta.10

Data di riferimento: 1 settembre 2026.

Questo report è la vista portabile e prudente precedente al package. Non incorpora ricevute positive, export issue o prove di package temporanee; il workflow di release le verifica separatamente senza persisterle nel repository.

## Esito

La prossima beta candidata non è pronta. La matrice canonica portabile, verificabile senza ricevute private, conserva 2 gate soddisfatti su 5: suite statica e forward Review→Debrief compattato.

Una proiezione esterna separata e digestata ha verificato anche il run delle nove skill candidate su Codex Desktop: `RUN_CAPTURED`, `PROVENANCE_VERIFIED`, `ADAPTER_GROUNDED` e `BEHAVIOR_PASS` risultano PASS. Con quell'indice esterno la matrice è valida e raggiunge 3 gate soddisfatti su 5, ma `candidate_ready` resta `false`.

Restano da verificare assenza di P0/P1 aperti e package parity/checksum. `package_state` resta `not_built`; la prova della sorgente candidata non promuove installazione, caricamento runtime, package, pilot o release.

## Stato osservato

| Ambito | Stato | Lettura corretta |
|---|---|---|
| `campaign-review` v0.1.3 locale | `static_only`, PASS | Sorgente e regressioni statiche valide; nessuna prova runtime o pilot. |
| Forward indipendente Review→Debrief sotto compattazione | `observed_unverified`, PASS | Due ruoli separati; osservato 7 su target 20, scarto 13; nessuna causalità. Manca provenance host completa. |
| Candidata beta.10 a nove skill su Codex Desktop | `provenance_verified`, PASS esterno | Nove input e nove output host conservati, receipt concatenate, grounding input/output e `BEHAVIOR_PASS` verificati. Prova la sorgente candidata, non un package installato. |
| Beta.9 a nove skill su Codex Desktop | `observed_unverified`, issue observed | Il run manuale ha rilevato perdita dell'obiettivo. Non ha receipt normalizzate, non produce `BEHAVIOR_PASS` e non prova la candidata corrente. |
| Codex Desktop con package candidato installato | `not_run` | Installazione e caricamento della candidata non sono verificati. |
| Codex CLI sulla candidata | `not_run` | Nessuna prova corrente. |
| Claude Code/Desktop locale sulla candidata | `not_run` | Le prove storiche su altre versioni non vengono trasferite. |
| Claude Cloud sulla candidata | `not_run` | Le prove storiche su altri cataloghi non vengono trasferite. |
| Pilot con marketer reale | `not_run` | Nessuna evidenza esterna di pilot. |

## Prossimo passo minimo

Serve una nuova autorizzazione per costruire il package candidato. Solo su quel package esatto il quality owner potrà verificare l'export issue allowlisted e il release owner potrà controllare parità e checksum. Fino a quel momento i due gate restano pending e la candidata non è pronta.

Cross-runtime refresh sulle quattro superfici e pilot con marketer reale restano gate espliciti per la promozione successiva. Questo report non autorizza package, installazione, commit, pubblicazione o release.

Il checker respinge prove high-state dell'asse sbagliato, package autoasseriti o con entry extra, issue P0/P1 non chiuse, cronologie o ID runtime impossibili, pilot senza runtime installato, outcome non PASS e matrici invalide con flag ready. Per una promozione reale, l'autenticità dell'exporter esterno resta un trust boundary da governare fuori dal repository.
