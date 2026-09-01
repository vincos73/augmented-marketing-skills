# Validazione indipendente raw-to-snapshot

Questa prova verifica che uno snapshot normalizzato sia sostenuto dagli input e output grezzi del run. Il checker legge raw e snapshot separatamente; gli oracle restano soltanto specifiche di regressione.

Il checker mantiene due profili distinti. `integrated-postexecution-v1` applica tutte le asserzioni statiche specifiche di Fabriloom. `nine-skill-minimum-v1` valuta una capture raw v4 reale senza imporre ID o dettagli Fabriloom non presenti nell'output host.

Il profilo minimo richiede esattamente nove skill nell'ordine candidato, continuità del target 20, autorizzazione del committente distinta e logicamente precedente all'esecuzione, asset/versione/canale coerenti tra review, autorizzazione ed esecuzione, Paid escluso, tracking verificato soltanto dopo evidenza operativa, risultato 7 su 20 e assenza di attribuzione causale o ROI. L'autorizzazione può apparire nell'input dello stesso turno dell'esecuzione, perché l'input precede l'output, ma non può essere prodotta o promossa dall'output del modello. Un fatto mancante non può essere ricostruito dallo snapshot.

Ogni oggetto semantico dello snapshot dichiara un JSON Pointer `source_ref`. Per raw v4 il riferimento deve risolversi sotto `normalized_input` o `normalized_output`, già verificati contro i rispettivi payload host dal checker di provenienza. Le decisioni di autorizzazione devono risolversi esclusivamente sotto `normalized_input`; le osservazioni di esecuzione possono risolversi sotto `normalized_output`. Per la fixture Fabriloom v2 il checker conserva i controlli locali completi. I casi negativi coprono omissioni, contraddizioni, puntatori tra stream diversi, promozioni da review, output del modello, proof metadata, expected o oracle, perdita del target, autorizzazione confusa con l'esecuzione, divergenza di asset o Paid, tracking anticipato e attribuzione causale.

    python3 evals/raw-to-snapshot/scripts/check_raw_to_snapshot.py --oracle evals/raw-to-snapshot/oracles/cases.json

Per un run catturato:

    python3 evals/raw-to-snapshot/scripts/check_raw_to_snapshot.py --capture-manifest /path/capture-manifest.json --raw /path/raw.json --snapshot /path/snapshot.json --require-behavior

`integrated-profile-contract.json` contiene le aspettative Fabriloom complete. `minimum-behavior-contract.json` contiene soltanto gli invarianti trasferibili del run a nove skill. `expected-run.md`, gli oracle e le fixture positive non fanno parte del pacchetto di input del run comportamentale. I dettagli delle receipt reali sono in `evals/behavioral-provenance/README.md`.
