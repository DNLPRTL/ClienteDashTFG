"""Local-only NeuralABR-Lite export bundle helpers for Phase 4F."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, MutableMapping, Sequence

from core.neural_abr.artifacts import ensure_existing_dir, ensure_outside_repo


BUNDLE_SCHEMA_VERSION = "neural_abr_lite_bundle_manifest_v1"
BUNDLE_PHASE = "phase4f"
BUNDLE_SOURCE_PHASE = "phase4e2"
BUNDLE_MODEL_FAMILY = "NeuralABR-Lite Candidate Scorer"
BUNDLE_TRAINING_METHOD = "behavior_cloning"
BUNDLE_TEACHER = "robust_mpc"
BUNDLE_ACTION_SPACE = "representation_index"
BUNDLE_REWARD_CONTEXT = "qoe_linear_v1 / reward_n"

REQUIRED_BUNDLE_FILES = (
    "bundle_manifest.json",
    "model_card.json",
    "feature_schema.json",
    "normalization_stats.json",
    "ladder_schema.json",
    "inference_contract.json",
    "fallback_policy.json",
    "model_state.pt",
)

HASHED_BUNDLE_FILES = tuple(filename for filename in REQUIRED_BUNDLE_FILES if filename != "bundle_manifest.json")

REQUIRED_MANIFEST_FIELDS = (
    "schema_version",
    "phase",
    "source_phase",
    "model_family",
    "training_method",
    "teacher",
    "action_space",
    "reward_context",
    "model_file",
    "feature_schema_file",
    "normalization_stats_file",
    "fallback_policy_file",
    "created_at_utc",
    "source_run_dir",
    "source_dataset_dir",
    "source_validation_dir",
    "files",
)


class BundleError(ValueError):
    """Raised when a Phase 4F bundle violates the export contract."""


class MissingBundleFileError(BundleError, FileNotFoundError):
    """Raised when a required bundle file is absent."""


class InvalidBundleError(BundleError):
    """Raised when bundle metadata or hashes are invalid."""


@dataclass(frozen=True)
class BundleFileRecord:
    filename: str
    sha256: str
    size_bytes: int

    def to_json(self) -> Mapping[str, object]:
        return {
            "filename": self.filename,
            "sha256": self.sha256,
            "size_bytes": self.size_bytes,
        }


@dataclass(frozen=True)
class BundleValidationResult:
    bundle_dir: Path
    manifest: Mapping[str, object]
    file_records: Mapping[str, BundleFileRecord]

    def to_json(self) -> Mapping[str, object]:
        return {
            "bundle_dir": str(self.bundle_dir),
            "required_files": list(REQUIRED_BUNDLE_FILES),
            "hashes_valid": True,
            "files": {
                filename: record.to_json()
                for filename, record in sorted(self.file_records.items())
            },
            "manifest": dict(self.manifest),
        }


def read_json_file(path: object) -> Mapping[str, object]:
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError as exc:
        raise MissingBundleFileError("missing JSON file: {0}".format(Path(path))) from exc
    except json.JSONDecodeError as exc:
        raise InvalidBundleError("invalid JSON file: {0}".format(Path(path))) from exc
    if not isinstance(payload, Mapping):
        raise InvalidBundleError("JSON file must contain an object: {0}".format(Path(path)))
    return payload


def write_json_file(path: object, payload: Mapping[str, object]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def sha256_file(path: object) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_record(path: object, filename: str | None = None) -> BundleFileRecord:
    resolved = Path(path)
    if not resolved.is_file():
        raise MissingBundleFileError("missing bundle file: {0}".format(resolved))
    return BundleFileRecord(
        filename=filename or resolved.name,
        sha256=sha256_file(resolved),
        size_bytes=resolved.stat().st_size,
    )


def prepare_bundle_output_dir(path: object, overwrite: bool = False) -> Path:
    from core.neural_abr.artifacts import prepare_output_dir

    return prepare_output_dir(path, overwrite=overwrite, purpose="Phase 4F bundle")


def resolve_bundle_dir(path: object) -> Path:
    return ensure_existing_dir(path, purpose="Phase 4F bundle")


def bundle_path(bundle_dir: object, filename: str) -> Path:
    return Path(bundle_dir).resolve() / filename


def build_bundle_manifest(metadata: Mapping[str, object], bundle_dir: object) -> Mapping[str, object]:
    bundle_path_value = ensure_outside_repo(bundle_dir, purpose="Phase 4F bundle")
    records = {
        filename: file_record(bundle_path_value / filename, filename).to_json()
        for filename in HASHED_BUNDLE_FILES
    }
    payload: MutableMapping[str, object] = dict(metadata)
    payload.setdefault("schema_version", BUNDLE_SCHEMA_VERSION)
    payload.setdefault("phase", BUNDLE_PHASE)
    payload.setdefault("source_phase", BUNDLE_SOURCE_PHASE)
    payload.setdefault("model_family", BUNDLE_MODEL_FAMILY)
    payload.setdefault("training_method", BUNDLE_TRAINING_METHOD)
    payload.setdefault("teacher", BUNDLE_TEACHER)
    payload.setdefault("action_space", BUNDLE_ACTION_SPACE)
    payload.setdefault("reward_context", BUNDLE_REWARD_CONTEXT)
    payload.setdefault("model_file", "model_state.pt")
    payload.setdefault("feature_schema_file", "feature_schema.json")
    payload.setdefault("normalization_stats_file", "normalization_stats.json")
    payload.setdefault("fallback_policy_file", "fallback_policy.json")
    payload["files"] = records
    payload["required_files"] = list(REQUIRED_BUNDLE_FILES)
    payload["hash_policy"] = "sha256 over all required payload files; manifest self-hash is excluded"
    return dict(payload)


def write_bundle_manifest(bundle_dir: object, metadata: Mapping[str, object]) -> Mapping[str, object]:
    resolved = ensure_outside_repo(bundle_dir, purpose="Phase 4F bundle")
    manifest = build_bundle_manifest(metadata, resolved)
    write_json_file(resolved / "bundle_manifest.json", manifest)
    return manifest


def load_bundle_manifest(bundle_dir: object) -> Mapping[str, object]:
    resolved = resolve_bundle_dir(bundle_dir)
    return read_json_file(resolved / "bundle_manifest.json")


def validate_bundle_dir(bundle_dir: object, verify_hashes: bool = True) -> BundleValidationResult:
    resolved = resolve_bundle_dir(bundle_dir)
    missing = [
        filename
        for filename in REQUIRED_BUNDLE_FILES
        if not (resolved / filename).is_file()
    ]
    if missing:
        raise MissingBundleFileError("missing bundle file(s): {0}".format(", ".join(missing)))

    manifest = read_json_file(resolved / "bundle_manifest.json")
    _validate_manifest_fields(manifest)
    file_records = _manifest_file_records(manifest, HASHED_BUNDLE_FILES)

    if verify_hashes:
        mismatches = []
        for filename, expected_record in file_records.items():
            actual = file_record(resolved / filename, filename)
            if actual.sha256 != expected_record.sha256:
                mismatches.append("{0}: expected {1}, got {2}".format(filename, expected_record.sha256, actual.sha256))
        if mismatches:
            raise InvalidBundleError("bundle SHA256 mismatch: {0}".format("; ".join(mismatches)))

    return BundleValidationResult(bundle_dir=resolved, manifest=manifest, file_records=file_records)


def _validate_manifest_fields(manifest: Mapping[str, object]) -> None:
    missing = [field for field in REQUIRED_MANIFEST_FIELDS if field not in manifest]
    if missing:
        raise InvalidBundleError("bundle manifest missing field(s): {0}".format(", ".join(missing)))
    if manifest.get("schema_version") != BUNDLE_SCHEMA_VERSION:
        raise InvalidBundleError("bundle manifest schema_version is invalid")
    if manifest.get("phase") != BUNDLE_PHASE:
        raise InvalidBundleError("bundle manifest phase must be phase4f")
    if manifest.get("source_phase") != BUNDLE_SOURCE_PHASE:
        raise InvalidBundleError("bundle manifest source_phase must be phase4e2")


def _manifest_file_records(manifest: Mapping[str, object], filenames: Sequence[str]) -> Mapping[str, BundleFileRecord]:
    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise InvalidBundleError("bundle manifest files must be a mapping")
    records = {}
    for filename in filenames:
        raw_record = files.get(filename)
        if not isinstance(raw_record, Mapping):
            raise InvalidBundleError("bundle manifest missing file record for {0}".format(filename))
        raw_hash = raw_record.get("sha256")
        if not isinstance(raw_hash, str) or len(raw_hash) != 64:
            raise InvalidBundleError("bundle manifest has invalid sha256 for {0}".format(filename))
        try:
            size_bytes = int(raw_record.get("size_bytes", 0))
        except (TypeError, ValueError) as exc:
            raise InvalidBundleError("bundle manifest has invalid size for {0}".format(filename)) from exc
        if size_bytes <= 0:
            raise InvalidBundleError("bundle manifest has invalid size for {0}".format(filename))
        records[filename] = BundleFileRecord(filename=filename, sha256=raw_hash, size_bytes=size_bytes)
    return records
