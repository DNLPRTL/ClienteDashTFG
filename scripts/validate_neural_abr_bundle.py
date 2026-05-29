#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Mapping

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.artifacts import ensure_outside_repo
from core.neural_abr.bundle import BundleError, read_json_file, validate_bundle_dir, write_json_file
from core.neural_abr.export import (
    render_closure_report_markdown,
    render_handoff_markdown,
    render_open_limitations_markdown,
)
from core.neural_abr.inference import (
    InferenceError,
    load_neural_abr_bundle,
    load_validation_samples,
    render_inference_smoke_markdown,
    render_latency_markdown,
    run_sample_inference,
)
from core.neural_abr.normalization import NormalizationStats


DECISION_READY = "PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G"
DECISION_PASS_NOT_READY = "PHASE4F_EXPORT_PASS_NOT_READY_FOR_PHASE4G"
DECISION_BLOCKED = "PHASE4F_BLOCKED_NEEDS_FIX"

FORBIDDEN_ARTIFACT_SUFFIXES = (
    ".pt",
    ".pth",
    ".onnx",
    ".npy",
    ".npz",
    ".pkl",
    ".joblib",
    ".zip",
    ".pdf",
    ".log",
)
IGNORED_REPO_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}
PROTECTED_CHANGE_PREFIXES = (
    "controllers/",
    "player/",
    "runtime/",
    "media/",
    "main.py",
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a local-only Phase 4F NeuralABR-Lite bundle.")
    parser.add_argument("--bundle-dir", required=True)
    parser.add_argument("--dataset-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--phase", required=True, choices=("phase4f",))
    parser.add_argument(
        "--docs-dir",
        help="Optional docs directory override for tests. Defaults to docs/science/04_neural_abr.",
    )
    args = parser.parse_args(argv)

    docs_dir = Path(args.docs_dir).resolve() if args.docs_dir else REPO_ROOT / "docs" / "science" / "04_neural_abr"
    report = validate_phase4f_bundle(
        bundle_dir=args.bundle_dir,
        dataset_dir=args.dataset_dir,
        output_dir=args.output_dir,
        docs_dir=docs_dir,
    )

    print("NeuralABR-Lite Phase 4F bundle validation summary")
    print("decision: {0}".format(report["decision"]))
    print("hard_failures: {0}".format(json.dumps(report["hard_failures"], sort_keys=True)))
    print("warnings: {0}".format(json.dumps(report["warnings"], sort_keys=True)))
    print("sample_valid_action_rate: {0}".format(_gate_detail(report, "sample_inference_valid_action_rate")))
    print("p95_latency_ms: {0}".format(_gate_detail(report, "p95_latency_ms")))
    print("diagnostic_only: true")
    return 1 if report["decision"] == DECISION_BLOCKED else 0


def validate_phase4f_bundle(
    bundle_dir: object,
    dataset_dir: object,
    output_dir: object,
    docs_dir: object,
) -> Mapping[str, object]:
    output_path = ensure_outside_repo(output_dir, purpose="Phase 4F bundle validation output")
    output_path.mkdir(parents=True, exist_ok=True)
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)

    gates: dict[str, Mapping[str, object]] = {}
    warnings: list[str] = []
    sample_report: Mapping[str, object] = {}
    latency_report: Mapping[str, object] = {}
    bundle_validation = None

    try:
        bundle_validation = validate_bundle_dir(bundle_dir)
        gates["required_files_present"] = _gate(True, "all required bundle files are present")
        gates["sha256_hashes_match"] = _gate(True, "all payload hashes match bundle_manifest.json")
    except BundleError as exc:
        gates["required_files_present"] = _gate(False, str(exc))
        gates["sha256_hashes_match"] = _gate(False, str(exc))

    if bundle_validation is not None:
        bundle_path = bundle_validation.bundle_dir
        gates["model_card_present"] = _json_gate(bundle_path / "model_card.json")
        gates["feature_schema_present"] = _json_gate(bundle_path / "feature_schema.json")
        gates["normalization_stats_present"] = _normalization_gate(bundle_path / "normalization_stats.json")
        gates["ladder_schema_present"] = _json_gate(bundle_path / "ladder_schema.json")
        gates["inference_contract_present"] = _json_gate(bundle_path / "inference_contract.json")
        gates["fallback_policy_present"] = _json_gate(bundle_path / "fallback_policy.json")
        try:
            engine = load_neural_abr_bundle(bundle_path)
            gates["model_loads_on_cpu"] = _gate(True, "model_state.pt loads with map_location=cpu and eval mode")
            samples = load_validation_samples(dataset_dir, max_samples=512)
            sample_report = run_sample_inference(engine, samples)
            latency_report = {
                "schema_version": "neural_abr_lite_phase4f_latency_report_v1",
                "phase": "phase4f",
                "latency_summary": sample_report.get("latency_summary"),
                "target_p95_ms": 10.0,
                "diagnostic_only": True,
                "not_benchmark": True,
                "production_latency_claim": False,
            }
            gates["sample_inference_valid_action_rate"] = _gate(
                sample_report.get("valid_action_rate") == 1.0,
                sample_report.get("valid_action_rate"),
            )
            gates["no_nan_inf_scores"] = _gate(
                sample_report.get("no_nan_inf_scores") is True,
                sample_report.get("no_nan_inf_scores"),
            )
            gates["deterministic_inference"] = _gate(
                sample_report.get("deterministic_rate") == 1.0,
                sample_report.get("deterministic_rate"),
            )
            p95_latency = _p95_latency(sample_report)
            latency_pass = p95_latency is not None and p95_latency <= 10.0
            gates["p95_latency_ms"] = _gate(latency_pass, p95_latency)
            if not latency_pass:
                warnings.append("p95 latency exceeds 10 ms; no production latency claim is made")
        except (BundleError, InferenceError) as exc:
            gates["model_loads_on_cpu"] = _gate(False, str(exc))
            gates["sample_inference_valid_action_rate"] = _gate(False, str(exc))
            gates["no_nan_inf_scores"] = _gate(False, str(exc))
            gates["deterministic_inference"] = _gate(False, str(exc))
            gates["p95_latency_ms"] = _gate(False, str(exc))
    else:
        for name in (
            "model_card_present",
            "feature_schema_present",
            "normalization_stats_present",
            "ladder_schema_present",
            "inference_contract_present",
            "fallback_policy_present",
            "model_loads_on_cpu",
            "sample_inference_valid_action_rate",
            "no_nan_inf_scores",
            "deterministic_inference",
            "p95_latency_ms",
        ):
            gates.setdefault(name, _gate(False, "bundle validation did not complete"))

    forbidden_artifacts = _forbidden_repo_artifacts(REPO_ROOT)
    protected_changes = _protected_git_changes(REPO_ROOT)
    gates["no_repo_artifacts"] = _gate(not forbidden_artifacts, forbidden_artifacts)
    gates["no_controller_player_runtime_media_main_changes"] = _gate(not protected_changes, protected_changes)

    hard_gate_names = [
        "required_files_present",
        "sha256_hashes_match",
        "model_card_present",
        "feature_schema_present",
        "normalization_stats_present",
        "ladder_schema_present",
        "inference_contract_present",
        "fallback_policy_present",
        "model_loads_on_cpu",
        "sample_inference_valid_action_rate",
        "no_nan_inf_scores",
        "deterministic_inference",
        "no_repo_artifacts",
        "no_controller_player_runtime_media_main_changes",
    ]
    hard_failures = [name for name in hard_gate_names if gates.get(name, {}).get("status") != "PASS"]
    if hard_failures:
        decision = DECISION_BLOCKED
    elif gates.get("p95_latency_ms", {}).get("status") != "PASS":
        decision = DECISION_PASS_NOT_READY
    else:
        decision = DECISION_READY

    report = {
        "schema_version": "neural_abr_lite_phase4f_bundle_validation_report_v1",
        "phase": "phase4f",
        "decision": decision,
        "bundle_dir": str(Path(bundle_dir).resolve()),
        "dataset_dir": str(Path(dataset_dir).resolve()),
        "output_dir": str(output_path),
        "gates": gates,
        "hard_failures": hard_failures,
        "warnings": warnings,
        "sample_inference_report": sample_report,
        "latency_report": latency_report,
        "diagnostic_only": True,
        "not_benchmark": True,
        "no_ranking": True,
        "no_sota_claim": True,
        "no_real_world_claim": True,
        "client_integration": False,
        "controller_registered": False,
    }
    write_json_file(output_path / "bundle_validation_report.json", report)
    if sample_report:
        write_json_file(output_path / "sample_inference_report.json", sample_report)
    if latency_report:
        write_json_file(output_path / "inference_latency_report.json", latency_report)
    _write_docs(report, docs_path)
    return report


def render_bundle_validation_markdown(report: Mapping[str, object]) -> str:
    gates = _mapping(report.get("gates"))
    lines = [
        "# Phase 4F Bundle Validation Report",
        "",
        "Decision: `{0}`".format(report.get("decision")),
        "",
        "Phase 4F validates a local-only export/inference bundle. It does not integrate NeuralABR-Lite into DashClientModular4 and does not register a neural controller.",
        "",
        "- Bundle dir: `{0}`".format(report.get("bundle_dir")),
        "- Hard failures: `{0}`".format(report.get("hard_failures")),
        "- Warnings: `{0}`".format(report.get("warnings")),
        "",
        "## Gates",
        "",
    ]
    for name in sorted(gates):
        gate = _mapping(gates[name])
        lines.append("- `{0}`: `{1}` ({2})".format(name, gate.get("status"), gate.get("details")))
    lines.extend(
        [
            "",
            "No benchmark/ranking, SOTA, or real-world validation claim is made. Bundle artifacts are local-only and outside the repository. Phase 4G will decide whether Phase 5 integration is allowed.",
            "",
        ]
    )
    return "\n".join(lines)


def _write_docs(report: Mapping[str, object], docs_path: Path) -> None:
    sample_report = _mapping(report.get("sample_inference_report"))
    latency_report = _mapping(report.get("latency_report"))
    decision = str(report.get("decision"))
    phase4g_allowed = decision == DECISION_READY
    reason = (
        "All Phase 4F export/inference gates passed."
        if phase4g_allowed
        else "Phase 4F did not pass every readiness gate."
    )
    documents = {
        "phase4f_bundle_validation_report.md": render_bundle_validation_markdown(report),
        "phase4f_open_limitations.md": render_open_limitations_markdown(),
        "phase4f_closure_report.md": render_closure_report_markdown(
            decision=decision,
            reason=reason,
            bundle_dir=str(report.get("bundle_dir")),
        ),
        "phase4f_to_phase4g_handoff.md": render_handoff_markdown(
            decision=decision,
            phase4g_allowed=phase4g_allowed,
        ),
    }
    if sample_report:
        documents["phase4f_inference_smoke_report.md"] = render_inference_smoke_markdown(sample_report)
    if latency_report:
        documents["phase4f_inference_latency_report.md"] = render_latency_markdown(latency_report)
    for filename, text in documents.items():
        (docs_path / filename).write_text(text, encoding="utf-8")


def _json_gate(path: Path) -> Mapping[str, object]:
    try:
        read_json_file(path)
    except BundleError as exc:
        return _gate(False, str(exc))
    return _gate(True, str(path))


def _normalization_gate(path: Path) -> Mapping[str, object]:
    try:
        NormalizationStats.from_json(read_json_file(path))
    except Exception as exc:  # noqa: BLE001 - validation report should keep the cause.
        return _gate(False, str(exc))
    return _gate(True, str(path))


def _gate(passed: bool, details: object) -> Mapping[str, object]:
    return {
        "status": "PASS" if bool(passed) else "FAIL",
        "passed": bool(passed),
        "details": details,
    }


def _gate_detail(report: Mapping[str, object], name: str) -> object:
    return _mapping(_mapping(report.get("gates")).get(name)).get("details")


def _p95_latency(sample_report: Mapping[str, object]) -> float | None:
    latency = _mapping(sample_report.get("latency_summary"))
    value = latency.get("p95_ms")
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _forbidden_repo_artifacts(repo_root: Path) -> list[str]:
    offenders = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(repo_root).parts
        if any(part in IGNORED_REPO_DIRS for part in relative_parts):
            continue
        if path.suffix.lower() in FORBIDDEN_ARTIFACT_SUFFIXES:
            offenders.append(str(path.relative_to(repo_root)).replace("\\", "/"))
    return sorted(offenders)


def _protected_git_changes(repo_root: Path) -> list[str]:
    completed = subprocess.run(
        ["git", "status", "--short", "--untracked-files=all"],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        return ["git_status_failed:{0}".format(completed.stderr.strip() or completed.stdout.strip())]
    protected = []
    for line in completed.stdout.splitlines():
        if not line.strip():
            continue
        path_text = line[3:].strip().replace("\\", "/")
        candidates = [part.strip() for part in path_text.split(" -> ")] if " -> " in path_text else [path_text]
        if any(
            candidate == "main.py" or candidate.startswith(prefix)
            for candidate in candidates
            for prefix in PROTECTED_CHANGE_PREFIXES
        ):
            protected.append(line)
    return protected


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


if __name__ == "__main__":
    raise SystemExit(main())
