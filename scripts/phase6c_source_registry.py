from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY_PATH = REPO_ROOT / "configs" / "phase6" / "phase6c_public_sources.json"
REGISTRY_SCHEMA_VERSION = "phase6c_public_source_registry_v1"
EXTERNAL_SUBDIRS = (
    "raw",
    "archives",
    "extracted",
    "normalized",
    "manifests",
    "reports",
    "audit",
    "receipts",
    "logs",
    "_local_inventory",
)
PRIMARY_SOURCE_IDS = ("raca_4g_lte", "raca_5g")
DIAGNOSTIC_SOURCE_IDS = ("ghent_4g_lte", "hsdpa_norway")
OPTIONAL_SOURCE_IDS = ("lumos5g",)
EXCLUDED_SOURCE_IDS = ("lancaster_abr_throughput_traces",)


class Phase6CError(RuntimeError):
    pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect the Phase 6C public trace source registry.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--list", action="store_true", help="Print source IDs and roles.")
    args = parser.parse_args(argv)

    registry = load_source_registry(args.registry)
    if args.list:
        for source in registry["sources"]:
            print("{0}\t{1}\t{2}\t{3}".format(
                source["source_id"],
                source.get("dataset_family", ""),
                source.get("role", ""),
                source.get("eval_gate", ""),
            ))
        return 0

    print(json.dumps(registry, indent=2, sort_keys=True))
    return 0


def load_source_registry(path: Optional[Path] = None) -> Dict[str, Any]:
    registry_path = Path(path or DEFAULT_REGISTRY_PATH)
    data = json.loads(registry_path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise Phase6CError("source registry must be a JSON object")
    if data.get("schema_version") != REGISTRY_SCHEMA_VERSION:
        raise Phase6CError(
            "unexpected source registry schema_version: {0}".format(data.get("schema_version"))
        )
    sources = data.get("sources")
    if not isinstance(sources, list):
        raise Phase6CError("source registry missing sources list")
    seen = set()
    for source in sources:
        if not isinstance(source, Mapping):
            raise Phase6CError("source registry contains a non-object source")
        source_id = str(source.get("source_id", "")).strip()
        if not source_id:
            raise Phase6CError("source registry contains source without source_id")
        if source_id in seen:
            raise Phase6CError("duplicate source_id in registry: {0}".format(source_id))
        seen.add(source_id)
    return dict(data)


def sources_by_id(registry: Mapping[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {str(source["source_id"]): dict(source) for source in registry.get("sources", [])}


def selected_sources(
    registry: Mapping[str, Any],
    source_spec: str = "primary",
    *,
    include_lumos: bool = False,
    include_diagnostic: bool = False,
) -> List[Dict[str, Any]]:
    by_id = sources_by_id(registry)
    requested = resolve_source_ids(
        registry,
        source_spec=source_spec,
        include_lumos=include_lumos,
        include_diagnostic=include_diagnostic,
    )
    missing = [source_id for source_id in requested if source_id not in by_id]
    if missing:
        raise Phase6CError("unknown Phase 6C source id(s): {0}".format(", ".join(missing)))

    selected = [by_id[source_id] for source_id in requested]
    forbidden = [source["source_id"] for source in selected if source.get("role", "").startswith("excluded")]
    if forbidden:
        raise Phase6CError("excluded sources cannot be selected for download: {0}".format(", ".join(forbidden)))
    return selected


def resolve_source_ids(
    registry: Mapping[str, Any],
    *,
    source_spec: str = "primary",
    include_lumos: bool = False,
    include_diagnostic: bool = False,
) -> List[str]:
    by_id = sources_by_id(registry)
    normalized = (source_spec or "primary").strip().lower()
    if normalized == "primary":
        requested = list(PRIMARY_SOURCE_IDS)
    elif normalized == "all":
        requested = [
            source_id
            for source_id, source in by_id.items()
            if source.get("enabled_by_default", False)
            and source.get("download_by_default", False)
            and source_id not in EXCLUDED_SOURCE_IDS
        ]
    else:
        requested = [item.strip() for item in source_spec.split(",") if item.strip()]

    if include_lumos:
        requested.extend(source_id for source_id in OPTIONAL_SOURCE_IDS if source_id not in requested)
    if include_diagnostic:
        requested.extend(source_id for source_id in DIAGNOSTIC_SOURCE_IDS if source_id not in requested)

    missing = [source_id for source_id in requested if source_id not in by_id]
    if missing:
        raise Phase6CError("unknown Phase 6C source id(s): {0}".format(", ".join(missing)))
    forbidden = [source_id for source_id in requested if source_id in EXCLUDED_SOURCE_IDS]
    if forbidden:
        raise Phase6CError("excluded sources cannot be selected: {0}".format(", ".join(forbidden)))
    return list(dict.fromkeys(requested))


def source_arg_from_ids(source_ids: Sequence[str]) -> str:
    return ",".join(source_ids)


def source_id_for_dataset_family(registry: Mapping[str, Any], dataset_family: str) -> str:
    for source in registry.get("sources", []):
        if source.get("dataset_family") == dataset_family:
            return str(source.get("source_id", dataset_family))
    return dataset_family


def create_external_layout(external_root: Path, *, allow_repo_output: bool = False) -> Dict[str, Path]:
    root = resolve_path(external_root)
    if not allow_repo_output:
        refuse_repo_path(root)
    root.mkdir(parents=True, exist_ok=True)
    paths = {"root": root}
    for subdir in EXTERNAL_SUBDIRS:
        path = root / subdir
        path.mkdir(parents=True, exist_ok=True)
        paths[subdir] = path
    (paths["manifests"] / "per_trace").mkdir(parents=True, exist_ok=True)
    return paths


def refuse_repo_path(path: Path) -> None:
    resolved = resolve_path(path)
    repo = resolve_path(REPO_ROOT)
    if resolved == repo or repo in resolved.parents:
        raise Phase6CError(
            "refusing to write Phase 6C materialization outputs inside the repository: {0}".format(resolved)
        )


def resolve_path(path: Path) -> Path:
    return Path(path).expanduser().resolve()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def md5_file(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_markdown_report(path: Path, title: str, lines: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = ["# {0}".format(title), ""]
    body.extend(lines)
    body.append("")
    path.write_text("\n".join(body), encoding="utf-8")


def relative_to_root(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def status_is_success(status: str) -> bool:
    return status in {
        "downloaded",
        "copied_from_local_file",
        "already_present",
        "skipped_existing",
        "extracted",
        "skipped_existing_extraction",
        "copied_plain_report",
        "normalized",
    }


def failure_status(status: str) -> bool:
    return status in {
        "failed",
        "checksum_mismatch",
        "blocked_by_provider_or_manual_confirmation_required",
        "offline_skipped",
        "invalid_archive",
        "path_traversal_blocked",
        "normalization_failed",
    }


if __name__ == "__main__":
    sys.exit(main())
