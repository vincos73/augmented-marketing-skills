# Contratto comune minimo

Il contratto comune v2 descrive uno snapshot normalizzato, non è una prova di runtime e non crea artefatti canonici. L'identità conversazionale è separata dalla raccolta degli artefatti. `chat-v1` può quindi avere `artifacts: []`; per elementi conversazionali o non creati il digest è null. Ogni riferimento persistente, fornito o osservato usa la forma `ID@versione` e conserva un digest SHA-256. Lo stato `provided_by_external_evidence` richiede anche `evidence_ref`; lo stato `persistent` è accettabile dal checker integrato solo con save autorizzato e osservato.

Decisione e osservazione sono campi distinti. Una decisione negata può essere osservata, ma l'azione collegata deve restare `not_observed` o `not_applicable`. Un'azione marcata `observed` richiede una decisione autorizzativa compatibile. La provenienza simulata resta distinta dall'osservazione live.

Ogni identità, scenario, artefatto, invariante, decisione, osservazione e arco dichiara un `source_ref` in forma JSON Pointer. Il checker raw-to-snapshot risolve il pointer e confronta localmente l'intero oggetto semantico; un campo aggiunto senza grounding fallisce. `shared_invariant_ids` conserva gli stessi otto identificatori tra common state, ledger, cross-Core e lineage. Il profilo e la modalità dell'evidenza mantengono distinti fixture sintetica, run comportamentale, runtime e pilot reale.

Questo contratto è volutamente più piccolo dei contratti specialistici. I checker specialistici restano normativi per il proprio eval; il checker comune verifica solo forma, identità, digest, separazione decisione/osservazione e risoluzione degli archi.
