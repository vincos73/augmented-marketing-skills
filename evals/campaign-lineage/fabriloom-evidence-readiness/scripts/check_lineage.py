#!/usr/bin/env python3
"""Validate the isolated Fabriloom Evidence Readiness lineage fixture."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "lineage-manifest.json"
NEGATIVE_DIR = ROOT / "negative-cases"
REF_PATTERN = re.compile(r"^[A-Z][A-Z0-9-]*@[0-9]+$")
READY_VERDICTS = {"pronta", "pronta con condizioni"}


class LineageError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise LineageError(f"Front matter mancante: {path.relative_to(ROOT)}")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError as error:
        raise LineageError(f"Front matter non chiuso: {path.relative_to(ROOT)}") from error
    parsed: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise LineageError(f"Riga front matter non valida in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        parsed[key.strip()] = value.strip()
    return parsed


def require_ref(value: Any, label: str) -> str:
    if not isinstance(value, str) or "@" not in value:
        raise LineageError(f"{label} non include una versione: {value!r}")
    if not REF_PATTERN.fullmatch(value):
        raise LineageError(f"{label} non ha formato ID@versione valido: {value!r}")
    return value


def collect_artifacts(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    artifacts = manifest["artifacts"]
    ordered = [artifacts["campaign_spec"], artifacts["operations"]]
    ordered.extend(artifacts["assets"])
    ordered.extend(artifacts["reviews"])
    ordered.extend(
        [artifacts["authorization"], artifacts["execution"], artifacts["results"], artifacts["debrief"]]
    )

    by_ref: dict[str, dict[str, Any]] = {}
    for artifact in ordered:
        ref = require_ref(artifact.get("ref"), "Riferimento artefatto")
        if ref in by_ref:
            raise LineageError(f"Riferimento duplicato: {ref}")
        by_ref[ref] = artifact
    return by_ref


def validate_files(by_ref: dict[str, dict[str, Any]]) -> None:
    for ref, artifact in by_ref.items():
        relative = artifact.get("path")
        if not isinstance(relative, str):
            raise LineageError(f"Percorso mancante per {ref}")
        path = ROOT / relative
        if not path.is_file():
            raise LineageError(f"File mancante per {ref}: {relative}")
        expected = artifact.get("sha256")
        actual = digest(path)
        if expected != actual:
            raise LineageError(f"Digest non corrispondente per {ref}: atteso {expected}, osservato {actual}")
        expected_version = ref.rsplit("@", 1)[1]
        metadata = front_matter(path)
        if metadata.get("version") != expected_version:
            raise LineageError(f"versione del file non corrisponde al riferimento per {ref}")
        expected_identity = ref.rsplit("@", 1)[0]
        if metadata.get("artifact_id") != expected_identity:
            raise LineageError(f"artifact_id del file non corrisponde al riferimento per {ref}")

        mappings: dict[str, str] = {
            "status": "status",
            "campaign_spec_ref": "campaign_spec_ref",
            "expected_ref": "expected_ref",
            "executed_ref": "executed_ref",
            "observed_ref": "observed_ref",
            "execution_ref": "execution_ref",
            "tracking_ref": "tracking_ref",
            "sales_capacity_ref": "sales_capacity_ref",
            "authorization_ref": "authorization_ref",
            "scope": "scope",
            "provenance": "provenance",
            "supersedes": "supersedes",
            "superseded_by": "superseded_by",
        }
        if ref.startswith("REVIEW-"):
            mappings["asset_ref"] = "reviewed_asset_ref"
        elif ref.startswith("AUTH-"):
            mappings["asset_ref"] = "authorized_asset_ref"
            mappings["review_ref"] = "approved_review_ref"
            mappings["authority"] = "owner"
        elif ref.startswith("EXEC-"):
            mappings["asset_ref"] = "executed_asset_ref"
            mappings["review_ref"] = "approved_review_ref"
        elif ref.startswith("DEBRIEF-"):
            mappings["asset_ref"] = "asset_ref"
            mappings["review_ref"] = "review_ref"
        for manifest_key, front_key in mappings.items():
            if manifest_key in artifact and str(artifact[manifest_key]) != metadata.get(front_key):
                raise LineageError(
                    f"front matter {front_key} non corrisponde al manifest per {ref}"
                )


def resolve(by_ref: dict[str, dict[str, Any]], value: Any, label: str) -> dict[str, Any]:
    ref = require_ref(value, label)
    if ref not in by_ref:
        raise LineageError(f"{label} non risolve un artefatto della fixture: {ref}")
    return by_ref[ref]


def validate_constraints(manifest: dict[str, Any]) -> None:
    artifacts = manifest["artifacts"]
    asset_v0 = ROOT / artifacts["assets"][0]["path"]
    asset_v1 = ROOT / artifacts["assets"][1]["path"]
    spec = (ROOT / artifacts["campaign_spec"]["path"]).read_text(encoding="utf-8")
    v0_text = asset_v0.read_text(encoding="utf-8")
    v1_text = asset_v1.read_text(encoding="utf-8")

    if "60% più velocemente" not in v0_text:
        raise LineageError("Il candidato v0 non contiene il difetto intenzionale del 60%")
    if "60%" in v1_text:
        raise LineageError("Il candidato v1 conserva il claim vietato del 60%")
    if "Testimonianza anonima autorizzata" not in v1_text:
        raise LineageError("Il candidato v1 non rende osservabile la testimonianza anonima")
    if artifacts["assets"][1].get("provided_by_fixture") is not True:
        raise LineageError("Il candidato v1 non risulta fornito dalla fixture")
    if any(asset.get("testimonial_anonymous") is not True for asset in artifacts["assets"]):
        raise LineageError("La testimonianza non resta anonima in tutte le versioni asset")
    if "Paid media" not in spec or "autorizzazione Finance separate" not in spec:
        raise LineageError("La Campaign Spec non mantiene paid come decisione separata")
    if "TRK-FAB-ERS-OWNED@1" not in spec or "sei call qualificate" not in spec:
        raise LineageError("Tracking o capacità non sono espliciti nella Campaign Spec")
    formula_42 = "Nei tre progetti pilota osservati, il tempo dichiarato per preparare un questionario si è ridotto in mediana del 42%. Il campione è limitato e i risultati non sono garantiti."
    if formula_42 not in spec or "approvazione Legal" not in spec:
        raise LineageError("Il claim condizionale del 42% non conserva formula completa e gate Legal")
    if "follow-up entro due giorni lavorativi" not in spec:
        raise LineageError("Il vincolo Sales non conserva il follow-up entro due giorni lavorativi")
    operations = (ROOT / artifacts["operations"]["path"]).read_text(encoding="utf-8")
    if "TRK-FAB-ERS-OWNED@1" not in operations or "E2E-FAB-ERS-04" not in operations:
        raise LineageError("Il tracking non risolve un'evidenza di test osservabile")


def validate_lineage(manifest: dict[str, Any], check_files: bool = True) -> None:
    if manifest.get("schema_version") != 1:
        raise LineageError("schema_version non supportata")
    shared_ids = [
        "speed-60", "speed-42-conditional", "pilot-quote-01",
        "operations-total-sprints", "operations-weekly-starts",
        "sales-weekly-qualified-calls", "TRK-FAB-ERS-OWNED@1", "paid-media",
    ]
    if manifest.get("scenario_id") != "FABRILOOM-ERS-INTEGRATED-POSTEXEC-V1" or manifest.get("profile") != "integrated-postexecution-v1":
        raise LineageError("scenario o profilo integrato post-execution non valido")
    if manifest.get("shared_invariant_ids") != shared_ids:
        raise LineageError("shared_invariant_ids divergenti")

    artifacts = manifest["artifacts"]
    by_ref = collect_artifacts(manifest)
    if check_files:
        validate_files(by_ref)
        validate_constraints(manifest)

    spec = artifacts["campaign_spec"]
    if spec.get("status") != "approvata":
        raise LineageError("La Campaign Spec di riferimento non è approvata")
    if spec.get("provisioning") != "provided_by_external_evidence":
        raise LineageError("La Campaign Spec non è fornita da evidenza esterna")

    reviews = artifacts["reviews"]
    for review in reviews:
        resolve(by_ref, review.get("campaign_spec_ref"), "Campaign Spec della review")
        asset = resolve(by_ref, review.get("asset_ref"), "Asset della review")
        if asset.get("campaign_spec_ref") != review.get("campaign_spec_ref"):
            raise LineageError(f"La review {review['ref']} e il suo asset riferiscono Campaign Spec diverse")
        if review.get("asset_sha256") != asset.get("sha256"):
            raise LineageError(f"La review {review['ref']} non conserva il digest dell'asset osservato")

    final_review = reviews[-1]
    if final_review.get("status") != "approvata" or final_review.get("verdict") not in READY_VERDICTS:
        raise LineageError("La review finale non è approvata e procedibile")

    for finding in final_review.get("findings", []):
        if finding.get("severity") == "bloccante" and finding.get("status") != "chiuso":
            raise LineageError(f"rilievo bloccante non chiuso nella review finale: {finding.get('id')}")

    prior_review = resolve(by_ref, final_review.get("supersedes"), "Review sostituita")
    if prior_review.get("superseded_by") != final_review.get("ref"):
        raise LineageError("Le relazioni supersedes e superseded_by tra le review non coincidono")
    blocking_ids = {
        finding["id"]
        for finding in prior_review.get("findings", [])
        if finding.get("severity") == "bloccante" and finding.get("status") != "chiuso"
    }
    resolutions = {item.get("finding_id"): item for item in final_review.get("resolutions", [])}
    for finding_id in blocking_ids:
        resolution = resolutions.get(finding_id)
        if not resolution or resolution.get("status") != "chiuso":
            raise LineageError(f"rilievo bloccante non chiuso dalla nuova review: {finding_id}")
        resolution_review = resolve(by_ref, resolution.get("review_ref"), "Review della risoluzione")
        if resolution_review.get("ref") != prior_review.get("ref"):
            raise LineageError(f"resolution review_ref non corrisponde alla review sostituita: {finding_id}")
        if resolution.get("observed_in_review") is not True:
            raise LineageError(f"La chiusura di {finding_id} è dedotta dall'esistenza dell'asset, non osservata nella review")
        if resolution.get("observed_asset_ref") != final_review.get("asset_ref"):
            raise LineageError(f"La chiusura di {finding_id} osserva una versione asset diversa")
        if resolution.get("observed_asset_sha256") != final_review.get("asset_sha256"):
            raise LineageError(f"La chiusura di {finding_id} non conserva il digest dell'asset osservato")

    execution = artifacts["execution"]
    executed_asset = resolve(by_ref, execution.get("asset_ref"), "Asset dell'execution log")
    executed_review = resolve(by_ref, execution.get("review_ref"), "Review dell'execution log")
    if executed_review.get("superseded_by"):
        raise LineageError(f"execution log cita una review superata: {execution.get('review_ref')}")
    if executed_review.get("status") != "approvata" or executed_review.get("verdict") not in READY_VERDICTS:
        raise LineageError("L'execution log cita una review non procedibile")
    for finding in executed_review.get("findings", []):
        if finding.get("severity") == "bloccante" and finding.get("status") != "chiuso":
            raise LineageError(f"rilievo bloccante non chiuso nell'execution log: {finding.get('id')}")
    if execution.get("asset_ref") != executed_review.get("asset_ref"):
        raise LineageError("execution log usa un asset diverso da quello revisionato")
    if execution.get("asset_sha256") != executed_asset.get("sha256"):
        raise LineageError("execution log non conserva il digest dell'asset eseguito")
    if execution.get("review_sha256") != executed_review.get("sha256"):
        raise LineageError("execution log non conserva il digest della review approvata")
    if execution.get("campaign_spec_ref") != executed_review.get("campaign_spec_ref"):
        raise LineageError("execution log e review non riferiscono la stessa Campaign Spec")

    authorization = resolve(by_ref, execution.get("authorization_ref"), "Autorizzazione dell'execution log")
    if authorization.get("status") != "approvata":
        raise LineageError("L'autorizzazione specifica non è approvata")
    if authorization.get("asset_ref") != execution.get("asset_ref"):
        raise LineageError("L'autorizzazione riguarda un asset diverso da quello eseguito")
    if authorization.get("review_ref") != execution.get("review_ref"):
        raise LineageError("L'autorizzazione riguarda una review diversa da quella eseguita")
    if authorization.get("authority") != "Marketing Director" or authorization.get("provenance") != "simulated":
        raise LineageError("Autorità o provenienza simulata dell'autorizzazione non conservata")
    scope = str(authorization.get("scope", "")).casefold()
    if "paid" in scope or "sponsorizzat" in scope:
        raise LineageError("paid scope non autorizzato dalla fixture organica")
    if execution.get("paid_activated") is not False:
        raise LineageError("Paid media risulta attivato senza decisione separata")
    require_ref(execution.get("tracking_ref"), "Tracking dell'execution log")
    if execution.get("sales_capacity_ref") != "sales-weekly-qualified-calls":
        raise LineageError("L'execution log non riferisce l'invariante Sales condiviso")
    if execution.get("capacity_per_week") != 6:
        raise LineageError("La capacità dell'execution log non corrisponde a sei call settimanali")

    results = artifacts["results"]
    if results.get("execution_ref") != execution.get("ref"):
        raise LineageError("I risultati non riferiscono l'esecuzione osservata")
    if results.get("tracking_ref") != execution.get("tracking_ref"):
        raise LineageError("I risultati non usano il tracking dell'esecuzione")
    if results.get("source_coverage") != "9/9":
        raise LineageError("La copertura della sorgente non è esplicita come 9/9")

    debrief = artifacts["debrief"]
    if str(debrief.get("path", "")).startswith("oracles/"):
        raise LineageError("Il debrief osservato non può essere l'oracolo expected")
    expected_digest = digest(ROOT / "oracles" / "expected-debrief.md")
    if debrief.get("sha256") == expected_digest:
        raise LineageError("Il digest del debrief osservato coincide con l'oracolo expected")
    if debrief.get("expected_ref") != spec.get("ref"):
        raise LineageError("Il debrief non riferisce l'atteso della Campaign Spec")
    if debrief.get("executed_ref") != execution.get("ref"):
        raise LineageError("Il debrief non riferisce l'esecuzione effettiva")
    if debrief.get("observed_ref") != results.get("ref"):
        raise LineageError("Il debrief non riferisce i risultati osservati")
    if debrief.get("asset_ref") != execution.get("asset_ref") or debrief.get("review_ref") != execution.get("review_ref"):
        raise LineageError("Il debrief non conserva la coppia asset-review dell'esecuzione")
    if debrief.get("causality") != "not_attributed":
        raise LineageError("Il debrief attribuisce causalità senza base adeguata")


def set_path(document: dict[str, Any], dotted_path: str, value: Any) -> None:
    parts = dotted_path.split(".")
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = value
    else:
        cursor[last] = value


def run_negative_cases(base: dict[str, Any]) -> list[str]:
    passed: list[str] = []
    for path in sorted(NEGATIVE_DIR.glob("*.json")):
        case = load_json(path)
        mutated = copy.deepcopy(base)
        for mutation in case["mutations"]:
            set_path(mutated, mutation["path"], mutation["value"])
        try:
            validate_lineage(mutated, check_files=case.get("check_files", False))
        except LineageError as error:
            expected = case["expected_error"]
            if expected not in str(error):
                raise LineageError(
                    f"{case['name']}: errore inatteso. Atteso '{expected}', osservato '{error}'"
                ) from error
            passed.append(case["name"])
        else:
            raise LineageError(f"{case['name']}: il caso negativo è stato accettato")
    return passed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--skip-negative", action="store_true")
    args = parser.parse_args()

    try:
        manifest = load_json(args.manifest.resolve())
        validate_lineage(manifest)
        print(f"PASS manifest positivo: {manifest['fixture_id']}")
        if not args.skip_negative:
            for name in run_negative_cases(manifest):
                print(f"PASS caso negativo respinto: {name}")
    except (KeyError, IndexError, TypeError, json.JSONDecodeError, LineageError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
