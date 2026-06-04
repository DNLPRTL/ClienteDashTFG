from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

try:
    from scripts.phase6c_source_registry import (
        Phase6CError,
        create_external_layout,
        relative_to_root,
        sha256_file,
        utc_now,
        write_json,
        write_markdown_report,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        Phase6CError,
        create_external_layout,
        relative_to_root,
        sha256_file,
        utc_now,
        write_json,
        write_markdown_report,
    )


RECEIPT_SCHEMA_VERSION = "phase6c_extract_receipts_v1"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Safely extract Phase 6C trace archives into an external root.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        report = extract_phase6_archives(
            external_root=args.external_root,
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
    strict: bool = False,
    allow_repo_output: bool = False,
) -> Dict[str, Any]:
    paths = create_external_layout(external_root, allow_repo_output=allow_repo_output)
    receipts: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []

    archives_root = paths["archives"]
    for source_dir in sorted(path for path in archives_root.iterdir() if path.is_dir()):
        source_id = source_dir.name
        for path in sorted(item for item in source_dir.rglob("*") if item.is_file()):
            if path.suffix.lower() == ".zip":
                receipt = extract_zip(path, paths["extracted"] / source_id, paths["root"])
            elif source_id == "hsdpa_norway" and path.name.startswith("report."):
                receipt = copy_plain_hsdpa_report(path, paths["extracted"] / source_id, paths["root"], source_dir)
            else:
                receipt = {
                    "source_id": source_id,
                    "archive_path": relative_to_root(path, paths["root"]),
                    "status": "skipped_non_archive",
                    "generated_at": utc_now(),
                }
            receipts.append(receipt)

    for receipt in receipts:
        if receipt["status"] in ("extracted", "copied_plain_report", "skipped_non_archive"):
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


def extract_zip(zip_path: Path, target_dir: Path, root: Path) -> Dict[str, Any]:
    try:
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
        return {
            "source_id": zip_path.parent.name,
            "archive_path": relative_to_root(zip_path, root),
            "target_dir": relative_to_root(target_dir, root),
            "status": "extracted",
            "sha256": sha256_file(zip_path),
            "generated_at": utc_now(),
        }
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


def copy_plain_hsdpa_report(path: Path, target_root: Path, root: Path, source_root: Path) -> Dict[str, Any]:
    try:
        relative = path.relative_to(source_root)
    except ValueError:
        relative = Path(path.name)
    target = target_root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    return {
        "source_id": "hsdpa_norway",
        "archive_path": relative_to_root(path, root),
        "target_path": relative_to_root(target, root),
        "status": "copied_plain_report",
        "sha256": sha256_file(target),
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
