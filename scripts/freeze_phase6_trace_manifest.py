from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

try:
    from scripts.phase6c_source_registry import Phase6CError, read_json, utc_now, write_json
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import Phase6CError, read_json, utc_now, write_json


OUTPUT_SCHEMA_VERSION = "phase6_trace_manifest_v1"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Freeze the final Phase 6 trace manifest after validation and audit.")
    parser.add_argument("--candidate-manifest", required=True, type=Path)
    parser.add_argument("--validation-report", required=True, type=Path)
    parser.add_argument("--eligibility-audit-report", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = freeze_phase6_manifest(
            candidate_manifest=args.candidate_manifest,
            validation_report=args.validation_report,
            eligibility_audit_report=args.eligibility_audit_report,
            output=args.output,
            strict=args.strict,
        )
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6_manifest_freeze: PASS")
    print("output: {0}".format(report["output"]))
    return 0


def freeze_phase6_manifest(
    *,
    candidate_manifest: Path,
    validation_report: Path,
    eligibility_audit_report: Path,
    output: Path,
    strict: bool = False,
) -> Dict[str, Any]:
    candidate = read_json(candidate_manifest)
    validation = read_json(validation_report)
    audit = read_json(eligibility_audit_report)

    errors: List[str] = []
    if not validation.get("valid"):
        errors.append("validation_report valid must be true")
    if not audit.get("use_for_phase6_eval"):
        errors.append("eligibility audit use_for_phase6_eval must be true")
    records = candidate.get("trace_records", [])
    if strict and not records:
        errors.append("strict mode requires candidate manifest trace_records")
    if errors:
        raise Phase6CError("; ".join(errors))

    frozen = dict(candidate)
    frozen["schema_version"] = OUTPUT_SCHEMA_VERSION
    frozen["manifest_role"] = "phase6_trace_manifest_final"
    frozen["freeze_metadata"] = {
        "frozen_at": utc_now(),
        "frozen_by_script": "scripts/freeze_phase6_trace_manifest.py",
        "source_candidate_manifest": str(candidate_manifest),
        "source_validation_report": str(validation_report),
        "source_eligibility_audit_report": str(eligibility_audit_report),
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6c_freeze_only": True,
    }
    frozen["benchmark_authorized"] = False
    frozen["ready_for_benchmark"] = False
    frozen["phase6c_freeze_only"] = True
    frozen["frozen_trace_ids"] = [record.get("trace_id", "") for record in records if record.get("trace_id")]
    write_json(output, frozen)
    return {"output": str(output), "records": len(records)}


if __name__ == "__main__":
    sys.exit(main())
