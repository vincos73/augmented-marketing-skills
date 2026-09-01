# Provenance comportamentale Codex

Questo gate accetta un run comportamentale soltanto quando nove invocazioni reali delle skill beta.9 sono accompagnate da file raw esterni, receipt verificabili e una catena SHA-256 integra. Il campo `evidence_mode: behavioral_run` non costituisce una prova.

## Boundary

- Nessuna receipt positiva è conservata nel repository.
- Capture manifest, nove receipt, nove input raw, nove output raw, raw manifest normalizzato e snapshot devono essere file esterni al repository.
- Ogni file è distinto. Lo stesso output non può provare più skill.
- `provider/runtime` deve essere presente in `runtime-allowlist.json`.
- `source_base_commit` deve essere `561dc936a011ac7b8b3842a1897572fe5abd1ad1` e i digest delle nove directory `skills/` devono coincidere con l'allowlist.
- Una risposta raw è immutabile ai fini del gate perché il suo byte stream è indirizzato da SHA-256 nella receipt, nel raw manifest e nella capture. Qualsiasi modifica successiva invalida il run.

## Cattura di un turno reale Codex

Per ciascuna skill, l'orchestratore di cattura deve:

1. Leggere `invocation_id`, `thread_id`, `turn_id`, `message_id`, modello, provider, runtime e timestamp dall'export o dall'API host Codex. Questi identificatori non devono essere chiesti al modello e non devono essere inventati dal runner.
2. Salvare l'input host in un file JSON esterno con `capture_kind: codex_invocation_input`, i metadati host in `receipt_metadata` e il payload realmente inviato.
3. Salvare la risposta host integrale in un file JSON esterno distinto con `capture_kind: codex_invocation_output`, gli stessi metadati e il payload realmente ricevuto.
4. Calcolare i digest dei due file e creare la receipt nel formato di `receipt.schema.json`. `previous_event_sha256` è `null` per la prima skill e coincide con `event_sha256` della receipt precedente per le altre otto.
5. Calcolare `event_sha256` sul JSON canonico della receipt senza il campo `event_sha256`: chiavi ordinate, UTF-8, separatori compatti.
6. Nel raw manifest, collegare ogni oggetto normalizzato all'input o all'output esterno tramite JSON Pointer oppure tramite intervallo testuale ed excerpt. Il checker ricomputa sia il digest dell'oggetto normalizzato sia quello dell'excerpt.

Formato minimo della receipt, con valori host reali:

```json
{
  "schema_version": "1.0.0",
  "invocation_id": "<host invocation id>",
  "provider": "openai",
  "runtime": "codex-desktop",
  "thread_id": "<host thread id>",
  "turn_id": "<host turn id>",
  "message_id": "<host message id>",
  "model": "<model osservato>",
  "skill_id": "<skill allowlisted>",
  "skill_version": "<versione allowlisted>",
  "skill_sha256": "<digest package allowlisted>",
  "input_path": "/percorso/esterno/input.json",
  "input_sha256": "<sha256 byte stream>",
  "output_path": "/percorso/esterno/output.json",
  "output_sha256": "<sha256 byte stream>",
  "captured_at": "<timestamp host RFC 3339>",
  "previous_event_sha256": null,
  "event_sha256": "<sha256 receipt canonica>"
}
```

Il formato esatto della capture è definito da `capture-manifest.schema.json`. La verifica finale è:

```text
python3 evals/robustness/run_robustness.py \
  --capture-manifest /percorso/esterno/capture-manifest.json \
  --raw /percorso/esterno/raw-manifest.json \
  --snapshot /percorso/esterno/snapshot.json
```

Il risultato è comportamentale soltanto se passano `RUN_CAPTURED`, `PROVENANCE_VERIFIED`, `ADAPTER_GROUNDED` e tutti i gate statici. Solo allora `BEHAVIOR_PASS` può essere `pass`.

## Formato esatto della cattura reale a nove skill

I due envelope esterni di ciascuna invocazione hanno esattamente questi campi. `receipt_metadata` ripete i metadati host della receipt; `payload` contiene l'input o l'output integrale realmente esportato:

```json
{
  "schema_version": "1.0.0",
  "capture_kind": "codex_invocation_output",
  "receipt_metadata": {
    "invocation_id": "<host invocation id>",
    "provider": "openai",
    "runtime": "codex-desktop",
    "thread_id": "<host thread id>",
    "turn_id": "<host turn id>",
    "message_id": "<host message id>",
    "model": "<model osservato>",
    "skill_id": "<skill allowlisted>",
    "skill_version": "<versione allowlisted>",
    "skill_sha256": "<digest package allowlisted>",
    "captured_at": "<timestamp host RFC 3339>"
  },
  "payload": "<output host integrale, JSON o testo>"
}
```

Il raw manifest comportamentale usa `schema_version: 4.0.0`. `proof_metadata` contiene soltanto `artifact_digests` e `harness_ids`: sono metadati di prova, mai fatti prodotti dal modello. Profilo, ID degli invarianti condivisi e scenario del runner vivono sotto `proof_metadata.harness_ids`; non compaiono in `normalized_output`. Ogni evento usa esattamente:

```json
{
  "sequence": 1,
  "skill": "setup-business-context",
  "skill_version": "0.6.5",
  "receipt_path": "/percorso/esterno/01-receipt.json",
  "raw_input_path": "/percorso/esterno/01-input.json",
  "raw_input_sha256": "<sha256 input>",
  "raw_response_path": "/percorso/esterno/01-output.json",
  "raw_response_sha256": "<sha256 output>",
  "raw_input": "<copia esatta del payload host nell'envelope input>",
  "raw_output": "<copia esatta del payload host nell'envelope output>",
  "normalized_input": {"<oggetto semantico input>": "<valore derivato>"},
  "input_normalizations": [
    {
      "normalized_ref": "/events/0/normalized_input/<foglia>",
      "normalized_sha256": "<sha256 JSON canonico della foglia>",
      "transformation": {"id": "identity"},
      "source": "input",
      "location": {
        "kind": "json_pointer",
        "pointer": "/payload/<posizione reale>"
      }
    }
  ],
  "normalized_output": {"<oggetto semantico>": "<valore derivato>"},
  "normalizations": [
    {
      "normalized_ref": "/events/0/normalized_output/<foglia>",
      "normalized_sha256": "<sha256 JSON canonico della foglia>",
      "transformation": {"id": "identity"},
      "source": "output",
      "location": {
        "kind": "json_pointer",
        "pointer": "/payload/<posizione reale>"
      }
    }
  ]
}
```

I digest degli envelope preservano i byte stream host originali. `raw_input` e `raw_output` devono coincidere con i rispettivi `payload` senza aggiunte o campi promossi. Le due normalizzazioni sono separate e coprono ogni foglia di `normalized_input` e `normalized_output`. Ogni foglia deve essere derivabile con una trasformazione deterministica allowlisted da un JSON Pointer sotto `/payload` oppure, per testo, da un intervallo esatto. Il campo `source` deve essere rispettivamente `input` o `output`; un puntatore incrociato tra i due stream invalida il run.

Per input o output testuale, `location` usa esattamente `kind`, `pointer`, `unit`, `start`, `end`, `excerpt`, `excerpt_sha256`. `unit` è `char` o `byte`; gli offset devono ricostruire l'excerpt esatto senza spezzare UTF-8. I fatti dello snapshot possono usare `source_ref` sotto `/events/N/normalized_input` oppure `/events/N/normalized_output`. Le decisioni di autorizzazione costituiscono un'eccezione direzionale: sono valide soltanto quando provengono da `normalized_input`, formulate dal committente o dallo scenario host. L'output del modello può osservare un'esecuzione già autorizzata, ma non può creare, ripetere o promuovere un proprio testo ad atto di autorizzazione. Lo scenario del profilo minimo è metadato dell'harness e non dichiara `source_ref`. Autorizzazioni, tracking, asset, risultati o stati mancanti restano mancanti e fanno fallire il relativo gate. `proof_metadata`, fixture expected e oracle non possono fornire decisioni di autorizzazione.

La capture manifest elenca tutte e sole le nove skill nell'ordine beta.9:

```json
{
  "schema_version": "1.0.0",
  "capture_id": "<id capture esterno>",
  "evidence_mode": "behavioral_run",
  "source_base_commit": "561dc936a011ac7b8b3842a1897572fe5abd1ad1",
  "provider": "openai",
  "runtime": "codex-desktop",
  "thread_id": "<host thread id>",
  "model": "<model osservato>",
  "raw_manifest_path": "/percorso/esterno/raw-manifest.json",
  "raw_manifest_sha256": "<sha256 raw manifest>",
  "snapshot_path": "/percorso/esterno/snapshot.json",
  "snapshot_sha256": "<sha256 snapshot>",
  "events": [
    {"sequence": 1, "skill_id": "setup-business-context", "receipt_path": "/percorso/esterno/01-receipt.json", "receipt_sha256": "<sha256 receipt 01>"},
    {"sequence": 2, "skill_id": "setup-marketing-system", "receipt_path": "/percorso/esterno/02-receipt.json", "receipt_sha256": "<sha256 receipt 02>"},
    {"sequence": 3, "skill_id": "define-marketing-challenge", "receipt_path": "/percorso/esterno/03-receipt.json", "receipt_sha256": "<sha256 receipt 03>"},
    {"sequence": 4, "skill_id": "choose-marketing-direction", "receipt_path": "/percorso/esterno/04-receipt.json", "receipt_sha256": "<sha256 receipt 04>"},
    {"sequence": 5, "skill_id": "define-marketing-mix", "receipt_path": "/percorso/esterno/05-receipt.json", "receipt_sha256": "<sha256 receipt 05>"},
    {"sequence": 6, "skill_id": "design-campaign", "receipt_path": "/percorso/esterno/06-receipt.json", "receipt_sha256": "<sha256 receipt 06>"},
    {"sequence": 7, "skill_id": "content-director", "receipt_path": "/percorso/esterno/07-receipt.json", "receipt_sha256": "<sha256 receipt 07>"},
    {"sequence": 8, "skill_id": "campaign-review", "receipt_path": "/percorso/esterno/08-receipt.json", "receipt_sha256": "<sha256 receipt 08>"},
    {"sequence": 9, "skill_id": "campaign-debrief", "receipt_path": "/percorso/esterno/09-receipt.json", "receipt_sha256": "<sha256 receipt 09>"}
  ]
}
```
