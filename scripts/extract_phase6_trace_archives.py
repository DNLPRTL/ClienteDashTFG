from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        relative_to_root,
        resolve_source_ids,
        sha256_file,
        utc_now,
        write_json,
        write_markdown_report,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        relative_to_root,
        resolve_source_ids,
        sha256_file,
        utc_now,
        write_json,
        write_markdown_report,
    )


RECEIPT_SCHEMA_VERSION = "phase6c_extract_receipts_v1"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Safely extract Phase 6C trace archives into an external root.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--sources", default="primary")
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--include-lumos", action="store_true")
    parser.add_argument("--include-diagnostic", action="store_true")
    parser.add_argument("--force-extract", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        report = extract_phase6_archives(
            external_root=args.external_root,
            sources=args.sources,
            registry_path=args.source_registry,
            include_lumos=args.include_lumos,
            include_diagnostic=args.include_diagnostic,
            force_extract=args.force_extract,
            strict=args.strict,
            allow_repo_output=args.allow_repo_output,
        )
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6c_extract: {0}".format("PASS" if report["valid"] else "WARN_OR_FAIL"))
    print("receipts: {0}".format(report["receipts_path"]))
    return 0 if report["valid"] else 2


def extract_phase6_archives(
    *,
    external_root: Path,
    sources: str = "primary",
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    include_lumos: bool = False,
    include_diagnostic: bool = False,
    force_extract: bool = False,
    strict: bool = False,
    allow_repo_output: bool = False,
) -> Dict[str, Any]:
    paths = create_external_layout(external_root, allow_repo_output=allow_repo_output)
    registry = load_source_registry(registry_path)
    selected_ids = resolve_source_ids(
        registry,
        source_spec=sources,
        include_lumos=include_lumos,
        include_diagnostic=include_diagnostic,
    )
    receipts: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []

    archives_root = paths["archives"]
    for source_id in selected_ids:
        source_dir = archives_root / source_id
        if not source_dir.is_dir():
            warnings.append("{0}: archive directory missing".format(source_id))
            continue
        for path in sorted(item for item in source_dir.rglob("*") if item.is_file()):
            if path.suffix.lower() == ".zip":
                print("phase6c_extract: {0}".format(relative_to_root(path, paths["root"])))
                receipt = extract_zip(path, paths["extracted"] / source_id, paths["root"], force_extract=force_extract)
            elif source_id == "hsdpa_norway" and path.name.startswith("report."):
                print("phase6c_extract: {0}".format(relative_to_root(path, paths["root"])))
                receipt = copy_plain_hsdpa_report(path, paths["extracted"] / source_id, paths["root"], source_dir, force_extract=force_extract)
            else:
                receipt = {
                    "source_id": source_id,
                    "archive_path": relative_to_root(path, paths["root"]),
                    "status": "skipped_non_archive",
                    "generated_at": utc_now(),
                }
            receipts.append(receipt)

    for receipt in receipts:
        if receipt["status"] in ("extracted", "copied_plain_report", "skipped_existing_extraction", "skipped_non_archive"):
            if receipt["status"] == "skipped_non_archive":
                warnings.append("{0}: skipped_non_archive".format(receipt.get("archive_path", "")))
            continue
        message = "{0}: {1}".format(receipt.get("archive_path", ""), receipt["status"])
        if strict:
            errors.append(message)
        else:
            warnings.append(message)

    receipt_doc = {
        "schema_version": RECEIPT_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "external_root": str(paths["root"]),
        "strict": strict,
        "sources": selected_ids,
        "force_extract": force_extract,
        "receipts": receipts,
        "errors": errors,
        "warnings": warnings,
    }
    receipts_path = paths["receipts"] / "phase6c_extract_receipts.json"
    report_path = paths["reports"] / "phase6c_extract_report.md"
    write_json(receipts_path, receipt_doc)
    write_extract_report(report_path, receipts, errors, warnings)
    return {
        "valid": not errors,
        "receipts": receipts,
        "errors": errors,
        "warnings": warnings,
        "receipts_path": str(receipts_path),
        "report_path": str(report_path),
    }


def extract_zip(zip_path: Path, target_dir: Path, root: Path, *, force_extract: bool = False) -> Dict[str, Any]:
    try:
        archive_sha256 = sha256_file(zip_path)
        marker = target_dir / ".phase6c_extract_marker.json"
        if marker.exists() and not force_extract:
            try:
                marker_data = json.loads(marker.read_text(encoding="utf-8"))
            except Exception:
                marker_data = {}
            if marker_data.get("archive_sha256") == archive_sha256:
                return {
                    "source_id": zip_path.parent.name,
                    "archive_path": relative_to_root(zip_path, root),
                    "target_dir": relative_to_root(target_dir, root),
                    "status": "skipped_existing_extraction",
                    "sha256": archive_sha256,
                    "generated_at": utc_now(),
                }
        target_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path) as archive:
            for member in archive.infolist():
                destination = safe_zip_destination(target_dir, member.filename)
                if member.is_dir():
                    destination.mkdir(parents=True, exist_ok=True)
                    continue
                destination.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as source, destination.open("wb") as target:
                    shutil.copyfileobj(source, target)
        receipt = {
            "source_id": zip_path.parent.name,
            "archive_path": relative_to_root(zip_path, root),
            "target_dir": relative_to_root(target_dir, root),
            "status": "extracted",
            "sha256": archive_sha256,
            "generated_at": utc_now(),
        }
        marker.write_text(
            json.dumps(
                {
                    "archive_path": relative_to_root(zip_path, root),
                    "archive_sha256": archive_sha256,
                    "extracted_at": utc_now(),
                },
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )
        return receipt
    except Phase6CError as exc:
        return {
            "source_id": zip_path.parent.name,
            "archive_path": relative_to_root(zip_path, root),
            "target_dir": relative_to_root(target_dir, root),
            "status": "path_traversal_blocked",
            "error": str(exc),
            "generated_at": utc_now(),
        }
    except zipfile.BadZipFile as exc:
        return {
            "source_id": zip_path.parent.name,
            "archive_path": relative_to_root(zip_path, root),
            "target_dir": relative_to_root(target_dir, root),
            "status": "invalid_archive",
            "error": str(exc),
            "generated_at": utc_now(),
        }


def safe_zip_destination(target_dir: Path, member_name: str) -> Path:
    destination = (target_dir / member_name).resolve()
    root = target_dir.resolve()
    if destination != root and root not in destination.parents:
        raise Phase6CError("zip member escapes target directory: {0}".format(member_name))
    return destination


def copy_plain_hsdpa_report(
    path: Path,
    target_root: Path,
    root: Path,
    source_root: Path,
    *,
    force_extract: bool = False,
) -> Dict[str, Any]:
    try:
        relative = path.relative_to(source_root)
    except ValueError:
        relative = Path(path.name)
    target = target_root / relative
    source_sha256 = sha256_file(path)
    if target.exists() and not force_extract and sha256_file(target) == source_sha256:
        return {
            "source_id": "hsdpa_norway",
            "archive_path": relative_to_root(path, root),
            "target_path": relative_to_root(target, root),
            "status": "skipped_existing_extraction",
            "sha256": source_sha256,
            "generated_at": utc_now(),
        }
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    return {
        "source_id": "hsdpa_norway",
        "archive_path": relative_to_root(path, root),
        "target_path": relative_to_root(target, root),
        "status": "copied_plain_report",
        "sha256": source_sha256,
        "generated_at": utc_now(),
    }


def write_extract_report(path: Path, receipts: Sequence[Mapping[str, Any]], errors: Sequence[str], warnings: Sequence[str]) -> None:
    lines = [
        "Phase 6C extraction report. Extracted files remain outside Git and are not benchmark evidence.",
        "",
        "- errors: {0}".format(len(errors)),
        "- warnings: {0}".format(len(warnings)),
        "- extracted_or_copied: {0}".format(
            sum(1 for receipt in receipts if receipt.get("status") in ("extracted", "copied_plain_report"))
        ),
        "",
        "## Receipts",
        "",
    ]
    for receipt in receipts:
        lines.append("- `{0}`: `{1}`".format(receipt.get("archive_path", ""), receipt.get("status", "")))
    write_markdown_report(path, "Phase 6C Extract Report", lines)


if __name__ == "__main__":
    sys.exit(main())
