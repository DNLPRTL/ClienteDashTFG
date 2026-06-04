from __future__ import annotations

import argparse
import importlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


SCHEMA_VERSION = "phase6_evaluation_readiness_v1"
REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = (
    "docs/science/06_validation/evaluation_protocol.md",
    "docs/science/06_validation/metrics_schema.md",
    "docs/science/06_validation/statistical_comparison.md",
    "docs/science/06_validation/results_tables_plan.md",
    "docs/science/06_validation/reproducibility_checklist.md",
    "docs/science/06_validation/threats_to_validity.md",
    "docs/science/06_validation/controller_matrix.md",
    "docs/science/06_validation/trace_selection_policy.md",
    "docs/science/06_validation/media_profile_decision.md",
    "docs/science/06_validation/ubuntu_evidence_package_spec.md",
)

REQUIRED_SCRIPTS = (
    "scripts/run_trace_dry_run.py",
    "scripts/compute_qoe_from_dry_run.py",
    "scripts/audit_phase6_trace_eligibility.py",
    "scripts/validate_phase6_trace_manifest.py",
    "scripts/phase6c_source_registry.py",
    "scripts/download_phase6_trace_sources.py",
    "scripts/extract_phase6_trace_archives.py",
    "scripts/normalize_phase6_trace_sources.py",
    "scripts/build_phase6_reference_manifest.py",
    "scripts/build_phase6_candidate_manifest.py",
    "scripts/freeze_phase6_trace_manifest.py",
    "scripts/run_phase6c_trace_materialization.py",
)

REQUIRED_CONTROLLERS = (
    "min_rate",
    "fixed_rate",
    "max_rate",
    "rate_based",
    "bba",
    "bola",
    "mpc",
    "robust_mpc",
    "neural_abr_lite",
)

REQUIRED_IMPORTS = (
    "core.evaluation.qoe",
    "core.evaluation.artifacts",
    "scripts.compute_qoe_from_dry_run",
)

FORBIDDEN_GENERATED_DIRS = (
    "docs/science/06_validation/results",
    "docs/science/06_validation/plots",
    "docs/science/06_validation/generated",
)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Check Phase 6 evaluation readiness without running benchmarks.")
    parser.add_argument("--phase4-dataset-manifest", type=Path)
    parser.add_argument("--phase6-candidate-manifest", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--require-manifests", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = build_report(
            phase4_manifest=args.phase4_dataset_manifest,
            phase6_manifest=args.phase6_candidate_manifest,
            strict=args.strict,
            require_manifests=args.require_manifests,
        )
        payload = json.dumps(report, indent=2, sort_keys=True)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(payload, encoding="utf-8")
            print("phase6_evaluation_readiness: {0}".format("PASS" if report["ready_for_phase6c"] else "BLOCK"))
            print("output: {0}".format(args.output))
        else:
            print(payload)
    except (OSError, json.JSONDecodeError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        print("unexpected readiness failure: {0}".format(exc), file=sys.stderr)
        return 1

    return 0 if report["ready_for_phase6c"] else 2


def build_report(
    *,
    phase4_manifest: Optional[Path],
    phase6_manifest: Optional[Path],
    strict: bool = False,
    require_manifests: bool = False,
) -> Dict[str, Any]:
    ensure_repo_on_path()
    checks: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []
    notes: List[str] = [
        "Phase 6B/6C readiness and materialization automation do not authorize benchmark execution.",
        "ready_for_phase6c is not ready_for_benchmark.",
    ]

    check_required_paths(REQUIRED_DOCS, "required_doc", checks, errors)
    check_required_paths(REQUIRED_SCRIPTS, "required_script", checks, errors)
    check_required_controllers(checks, errors)
    check_required_imports(checks, errors)
    check_forbidden_generated_artifacts(checks, errors)

    manifest_audit: Dict[str, Any] = {"ran": False}
    manifests_provided = bool(phase4_manifest) and bool(phase6_manifest)
    partial_manifests = bool(phase4_manifest) != bool(phase6_manifest)

    if partial_manifests:
        errors.append("phase4 and phase6 manifests must be provided together.")
        checks.append(
            {
                "name": "manifest_pair",
                "status": "fail",
                "detail": "phase4 and phase6 manifests must be provided together",
            }
        )
    elif not manifests_provided:
        warnings.append("manifest_audit_not_run")
        checks.append(
            {
                "name": "manifest_audit",
                "status": "warn",
                "detail": "manifest_audit_not_run",
            }
        )
        if require_manifests:
            errors.append("manifest_audit_not_run: --require-manifests was set.")
    else:
        manifest_audit = run_manifest_checks(phase4_manifest, phase6_manifest, checks, errors, warnings)

    ready_for_phase6c = not errors
    return {
        "schema_version": SCHEMA_VERSION,
        "strict": bool(strict),
        "ready_for_phase6c": ready_for_phase6c,
        "ready_for_benchmark": False,
        "benchmark_authorized": False,
        "checks": checks,
        "errors": errors,
        "warnings": warnings,
        "notes": notes,
        "manifest_audit": manifest_audit,
    }


def check_required_paths(paths: Sequence[str], check_name: str, checks: List[Dict[str, Any]], errors: List[str]) -> None:
    for relative_path in paths:
        path = REPO_ROOT / relative_path
        if path.is_file():
            checks.append({"name": check_name, "status": "ok", "detail": relative_path})
        else:
            checks.append({"name": check_name, "status": "fail", "detail": relative_path})
            errors.append("{0} missing: {1}".format(check_name, relative_path))


def check_required_controllers(checks: List[Dict[str, Any]], errors: List[str]) -> None:
    try:
        registry = importlib.import_module("core.controller.registry")
        available = set(getattr(registry, "CONTROLLER_REGISTRY", {}).keys())
    except Exception as exc:
        checks.append({"name": "controller_registry_import", "status": "fail", "detail": format_exc(exc)})
        errors.append("controller registry import failed: {0}".format(format_exc(exc)))
        return

    missing = [controller for controller in REQUIRED_CONTROLLERS if controller not in available]
    if missing:
        checks.append({"name": "controller_registry", "status": "fail", "detail": ", ".join(missing)})
        errors.append("required controllers missing from registry: {0}".format(", ".join(missing)))
    else:
        checks.append(
            {
                "name": "controller_registry",
                "status": "ok",
                "detail": ", ".join(REQUIRED_CONTROLLERS),
            }
        )


def check_required_imports(checks: List[Dict[str, Any]], errors: List[str]) -> None:
    for module_name in REQUIRED_IMPORTS:
        try:
            importlib.import_module(module_name)
            checks.append({"name": "import", "status": "ok", "detail": module_name})
        except Exception as exc:
            checks.append({"name": "import", "status": "fail", "detail": "{0}: {1}".format(module_name, format_exc(exc))})
            errors.append("import failed: {0}: {1}".format(module_name, format_exc(exc)))


def check_forbidden_generated_artifacts(checks: List[Dict[str, Any]], errors: List[str]) -> None:
    for relative_dir in FORBIDDEN_GENERATED_DIRS:
        path = REPO_ROOT / relative_dir
        if not path.exists():
            checks.append({"name": "forbidden_generated_artifacts", "status": "ok", "detail": "{0} absent".format(relative_dir)})
            continue
        files = [item for item in path.rglob("*") if item.is_file()]
        if files:
            details = [str(item.relative_to(REPO_ROOT)) for item in files]
            checks.append({"name": "forbidden_generated_artifacts", "status": "fail", "detail": details})
            errors.append("forbidden generated artifacts found under {0}".format(relative_dir))
        else:
            checks.append({"name": "forbidden_generated_artifacts", "status": "ok", "detail": "{0} empty".format(relative_dir)})


def run_manifest_checks(
    phase4_manifest: Path,
    phase6_manifest: Path,
    checks: List[Dict[str, Any]],
    errors: List[str],
    warnings: List[str],
) -> Dict[str, Any]:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        validation_output = temp_root / "phase6_manifest_validation.json"
        audit_output = temp_root / "phase6_trace_eligibility_audit.json"

        validation_result = subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "validate_phase6_trace_manifest.py"),
                "--manifest",
                str(phase6_manifest),
                "--output",
                str(validation_output),
                "--strict-final",
                "--fail-on-error",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        validation_report = json.loads(validation_output.read_text(encoding="utf-8")) if validation_output.exists() else {}
        if validation_result.returncode == 0 and validation_report.get("valid"):
            checks.append({"name": "manifest_validation", "status": "ok", "detail": str(phase6_manifest)})
        else:
            checks.append(
                {
                    "name": "manifest_validation",
                    "status": "fail",
                    "detail": validation_report.get("errors", validation_result.stderr),
                }
            )
            errors.append("phase6 candidate manifest failed strict-final validation.")

        warnings.extend(validation_report.get("warnings", []))

        audit_result = subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "audit_phase6_trace_eligibility.py"),
                "--phase4-dataset-manifest",
                str(phase4_manifest),
                "--phase6-candidate-manifest",
                str(phase6_manifest),
                "--output",
                str(audit_output),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        audit_report = json.loads(audit_output.read_text(encoding="utf-8")) if audit_output.exists() else {}
        audit_passed = audit_result.returncode == 0 and bool(audit_report.get("use_for_phase6_eval"))
        if audit_passed:
            checks.append({"name": "trace_eligibility_audit", "status": "ok", "detail": str(phase6_manifest)})
        else:
            checks.append(
                {
                    "name": "trace_eligibility_audit",
                    "status": "fail",
                    "detail": audit_report.get("reasons", audit_result.stderr),
                }
            )
            errors.append("phase6 candidate manifest failed Phase 4 overlap audit.")

    return {
        "ran": True,
        "validation_valid": bool(validation_report.get("valid")),
        "validation_error_count": len(validation_report.get("errors", [])),
        "audit_use_for_phase6_eval": bool(audit_report.get("use_for_phase6_eval")),
        "audit_reasons": audit_report.get("reasons", []),
        "audit_counts": audit_report.get("counts", {}),
    }


def ensure_repo_on_path() -> None:
    root = str(REPO_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)


def format_exc(exc: BaseException) -> str:
    message = str(exc)
    if message:
        return "{0}: {1}".format(exc.__class__.__name__, message)
    return exc.__class__.__name__


if __name__ == "__main__":
    raise SystemExit(main())
