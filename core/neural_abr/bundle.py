from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, write_json
from core.neural_abr.constants import (
    BUNDLE_FALLBACK_POLICY_FILENAME,
    BUNDLE_INFERENCE_CONTRACT_FILENAME,
    BUNDLE_LADDER_SCHEMA_FILENAME,
    BUNDLE_MANIFEST_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_MODEL_FILENAME,
    CANDIDATE_MODEL_CONFIG_FILENAME,
    FEATURE_SCHEMA_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_INFERENCE_BUNDLE_SCHEMA_ID,
)


class BundleError(ValueError):
    """Raised when a Phase 4F inference bundle is invalid."""


REQUIRED_BUNDLE_FILES = (
    BUNDLE_MANIFEST_FILENAME,
    BUNDLE_MODEL_FILENAME,
    CANDIDATE_MODEL_CONFIG_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    FEATURE_SCHEMA_FILENAME,
    BUNDLE_LADDER_SCHEMA_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_INFERENCE_CONTRACT_FILENAME,
    BUNDLE_FALLBACK_POLICY_FILENAME,
)

HASHED_BUNDLE_FILES = tuple(filename for filename in REQUIRED_BUNDLE_FILES if filename != BUNDLE_MANIFEST_FILENAME)


def prepare_bundle_output_dir(path: object, overwrite: bool = False) -> Path:
    return prepare_output_dir(path, overwrite=overwrite, purpose="phase4 inference bundle")


def resolve_bundle_dir(path: object) -> Path:
    return ensure_existing_dir(path, purpose="phase4 inference bundle")


def sha256_file(path: object) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bundle_file_record(path: object, filename: str) -> Mapping[str, object]:
    resolved = Path(path)
    if not resolved.is_file():
        raise BundleError("missing bundle file: {0}".format(resolved))
    return {
        "filename": filename,
        "sha256": sha256_file(resolved),
        "size_bytes": resolved.stat().st_size,
    }


def write_phase4_bundle_manifest(bundle_dir: object, metadata: Mapping[str, object]) -> Mapping[str, object]:
    bundle_path = resolve_bundle_dir(bundle_dir)
    files = {
        filename: bundle_file_record(bundle_path / filename, filename)
        for filename in HASHED_BUNDLE_FILES
    }
    manifest = dict(metadata)
    manifest.update(
        {
            "schema_id": PHASE4_INFERENCE_BUNDLE_SCHEMA_ID,
            "human_readable_name": "Bundle local para inferencia offline de NeuralABR-Lite",
            "phase": "phase4f_export_bundle_inferencia",
            "required_files": list(REQUIRED_BUNDLE_FILES),
            "hash_policy": "sha256 de todos los archivos del bundle salvo el manifiesto",
            "files": files,
            "benchmark_performed": False,
            "outputs_are_benchmark_results": False,
            "ranking_performed": False,
            "no_final_ranking": True,
            "controller_integrated": False,
            "controller_registered": False,
        }
    )
    write_json(bundle_path / BUNDLE_MANIFEST_FILENAME, manifest)
    return manifest


def validate_phase4_bundle_dir(bundle_dir: object, verify_hashes: bool = True) -> Mapping[str, object]:
    bundle_path = resolve_bundle_dir(bundle_dir)
    missing = [filename for filename in REQUIRED_BUNDLE_FILES if not (bundle_path / filename).is_file()]
    if missing:
        raise BundleError("missing bundle file(s): {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / BUNDLE_MANIFEST_FILENAME)
    if manifest.get("schema_id") != PHASE4_INFERENCE_BUNDLE_SCHEMA_ID:
        raise BundleError("bundle manifest schema_id is invalid")
    if manifest.get("controller_integrated") is not False or manifest.get("controller_registered") is not False:
        raise BundleError("bundle must not register or integrate a controller in Phase 4F")
    for flag in ("benchmark_performed", "outputs_are_benchmark_results", "ranking_performed"):
        if manifest.get(flag) is not False:
            raise BundleError("{0} must be false".format(flag))
    if manifest.get("no_final_ranking") is not True:
        raise BundleError("no_final_ranking must be true")

    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise BundleError("bundle manifest files must be a mapping")
    hash_mismatches = []
    records = {}
    for filename in HASHED_BUNDLE_FILES:
        raw_record = files.get(filename)
        if not isinstance(raw_record, Mapping):
            raise BundleError("bundle manifest missing file record for {0}".format(filename))
        expected_hash = str(raw_record.get("sha256", ""))
        expected_size = int(raw_record.get("size_bytes", 0) or 0)
        actual_record = bundle_file_record(bundle_path / filename, filename)
        records[filename] = actual_record
        if expected_size != actual_record["size_bytes"]:
            hash_mismatches.append("{0}: size mismatch".format(filename))
        if verify_hashes and expected_hash != actual_record["sha256"]:
            hash_mismatches.append("{0}: sha256 mismatch".format(filename))
    if hash_mismatches:
        raise BundleError("; ".join(hash_mismatches))
    return {
        "status": "PASS",
        "bundle_dir": str(bundle_path),
        "manifest": dict(manifest),
        "required_files": list(REQUIRED_BUNDLE_FILES),
        "file_records": records,
        "hashes_valid": True,
    }


def require_bundle_files(file_names: Sequence[str]) -> None:
    missing_constants = [filename for filename in file_names if filename not in REQUIRED_BUNDLE_FILES]
    if missing_constants:
        raise BundleError("unknown bundle required file(s): {0}".format(", ".join(missing_constants)))
