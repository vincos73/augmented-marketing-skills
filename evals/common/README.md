# Primitive comuni di stato

Questa directory definisce il vocabolario minimo condiviso dagli eval di robustezza. Non sostituisce i contratti specialistici di E2E, lineage, cross-Core safety o authorization-ledger.

Il contratto comune separa:

- identità conversazionale separata dagli artefatti;
- identificatore, versione, stato e digest nullable di un artefatto;
- invarianti di business e relativa base;
- decisione autorizzativa e osservazione dell'azione;
- archi di lineage tra artefatti o passaggi;
- profilo della prova e modalità dell'evidenza.
- otto `shared_invariant_ids` identici nei contratti specialistici.

I profili restano distinti: `chat-v1` ammette `artifacts: []` e richiede digest null per artefatti non creati; `preexecution-static-v1` conserva tracking non verificato; `integrated-postexecution-v1` richiede una prova Operations oltre il boundary; `authorization-ledger-v1` verifica quattro transizioni autorizzative. Il digest è obbligatorio soltanto per stati persistenti, forniti o osservati. La route `provided_by_external_evidence` richiede un file identificato da digest.

Il file [state-contract.schema.json](state-contract.schema.json) è il contratto machine-readable. Il checker è [check_state_contract.py](scripts/check_state_contract.py). Il confine statico Fabriloom elenca le nove skill reali in [fabriloom-nine-step](../robustness/fabriloom-nine-step/), ma non viene presentato come run comportamentale.
