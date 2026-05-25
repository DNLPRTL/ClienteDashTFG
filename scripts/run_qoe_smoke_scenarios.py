"""Run controlled Phase 3.5D QoE smoke scenarios outside the repository."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Mapping, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.evaluation.artifacts import (  # noqa: E402
    DRY_RUN_MANIFEST_FILENAME,
    DRY_RUN_SEGMENTS_FILENAME,
    DRY_RUN_SUMMARY_FILENAME,
    QOE_ARTIFACT_MANIFEST_FILENAME,
    QOE_RUN_SUMMARY_FILENAME,
    QOE_SEGMENT_REWARDS_FILENAME,
    QoEArtifactError,
    compute_qoe_artifacts_from_dry_run,
)


SMOKE_PHASE = "phase3_5d_controlled_qoe_smoke"
SMOKE_REPORT_FILENAME = "qoe_smoke_report.json"
SYNTHETIC_CONTROLLER_NAME = "synthetic_smoke_controller"


@dataclass(frozen=True)
class QOESmokeScenario:
    name: str
    bitrates_kbps: Sequence[float]
    rebuffer_s: Sequence[float]
    row_eval_gate: str
    expected_segment_count: int
    expected_session_eval_gate: str
    final_qoe_reward_defined: bool = True
    outputs_are_benchmark_results: bool = False
    expected_qoe_linear_sum: Optional[float] = None
    expected_qoe_linear_mean: Optional[float] = None
    expected_gate_reason: Optional[str] = None


@dataclass(frozen=True)
class QOESmokeScenarioResult:
    scenario_name: str
    trace_id: str
    controller_name: str
    qoe_linear_sum: float
    qoe_linear_mean: float
    session_eval_gate: str
    gate_reasons: Sequence[str]
    outputs_are_benchmark_results: bool
    no_final_ranking: bool
    qoe_output_dir: str
    checks_passed: bool


class QOESmokeError(ValueError):
    """Raised when controlled smoke scenarios cannot run safely."""


def run_qoe_smoke_scenarios(
    output_root: object,
    overwrite: bool = False,
    min_bitrate_kbps: float = 1000.0,
) -> Mapping[str, object]:
    """Create synthetic dry-run-like artifacts and compute QoE smoke outputs."""
    output_path = _prepare_output_root(output_root, overwrite=overwrite)
    scenarios = _scenario_definitions()
    scenario_results: List[QOESmokeScenarioResult] = []

    for scenario in scenarios:
        source_dir = output_path / scenario.name / "source_dry_run"
        qoe_dir = output_path / scenario.name / "qoe_outputs"
        _write_synthetic_dry_run_artifacts(source_dir, scenario)
        computation = compute_qoe_artifacts_from_dry_run(
            dry_run_dir=source_dir,
            output_dir=qoe_dir,
            expected_segment_count=scenario.expected_segment_count,
            min_bitrate_kbps=min_bitrate_kbps,
            overwrite=True,
        )
        summary = dict(computation.summary)
        scenario_results.append(
            _build_scenario_result(
                scenario=scenario,
                summary=summary,
                qoe_output_dir=qoe_dir,
            )
        )

    report = _build_smoke_report(output_path, scenario_results)
    _write_json(output_path / SMOKE_REPORT_FILENAME, report)
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Run controlled non-benchmark Phase 3.5D QoE smoke scenarios."
    )
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--min-bitrate-kbps", type=float, default=1000.0)
    args = parser.parse_args(argv)

    try:
        report = run_qoe_smoke_scenarios(
            output_root=args.output_root,
            overwrite=args.overwrite,
            min_bitrate_kbps=args.min_bitrate_kbps,
        )
    except (OSError, QoEArtifactError, QOESmokeError, ValueError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("output_root: {0}".format(Path(args.output_root)))
    print("scenario_count: {0}".format(report["scenario_count"]))
    print("all_checks_passed={0}".format(str(report["all_checks_passed"]).lower()))
    print("outputs_are_benchmark_results=false")
    print("no_final_ranking=true")
    print("ranking_performed=false")
    print("benchmark_performed=false")
    return 0 if report["all_checks_passed"] else 1


def _scenario_definitions() -> Sequence[QOESmokeScenario]:
    return (
        QOESmokeScenario(
            name="complete_use_for_eval",
            bitrates_kbps=(1000.0, 2000.0, 1000.0),
            rebuffer_s=(0.0, 0.0, 0.0),
            row_eval_gate="use_for_eval",
            expected_segment_count=3,
            expected_session_eval_gate="use_for_eval",
            expected_qoe_linear_sum=2.0,
            expected_qoe_linear_mean=2.0 / 3.0,
        ),
        QOESmokeScenario(
            name="legacy_do_not_use_for_eval",
            bitrates_kbps=(1000.0, 2000.0, 1000.0),
            rebuffer_s=(0.0, 0.0, 0.0),
            row_eval_gate="do_not_use_for_eval",
            expected_segment_count=3,
            expected_session_eval_gate="do_not_use_for_eval",
            final_qoe_reward_defined=False,
            expected_gate_reason="legacy_dry_run",
        ),
        QOESmokeScenario(
            name="incomplete_session",
            bitrates_kbps=(1000.0, 2000.0, 1000.0),
            rebuffer_s=(0.0, 0.0, 0.0),
            row_eval_gate="use_for_eval",
            expected_segment_count=4,
            expected_session_eval_gate="do_not_use_for_eval",
            expected_gate_reason="incomplete_session",
        ),
        QOESmokeScenario(
            name="source_claims_benchmark",
            bitrates_kbps=(1000.0, 2000.0, 1000.0),
            rebuffer_s=(0.0, 0.0, 0.0),
            row_eval_gate="use_for_eval",
            expected_segment_count=3,
            expected_session_eval_gate="do_not_use_for_eval",
            outputs_are_benchmark_results=True,
        ),
    )


def _prepare_output_root(output_root: object, overwrite: bool) -> Path:
    if output_root is None or not str(output_root).strip():
        raise QOESmokeError("output_root is required")
    output_path = Path(output_root).expanduser().resolve()
    repo_path = REPO_ROOT.resolve()
    if output_path == repo_path or repo_path in output_path.parents:
        raise QOESmokeError("output_root must be outside the repository: {0}".format(output_path))
    if output_path.parent == output_path:
        raise QOESmokeError("output_root cannot be a filesystem root: {0}".format(output_path))
    if output_path.exists() and not output_path.is_dir():
        raise QOESmokeError("output_root exists and is not a directory: {0}".format(output_path))
    if output_path.exists() and any(output_path.iterdir()):
        if not overwrite:
            raise QOESmokeError("output_root is not empty; pass --overwrite to replace smoke outputs")
        shutil.rmtree(str(output_path))
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def _write_synthetic_dry_run_artifacts(output_dir: Path, scenario: QOESmokeScenario) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    trace_id = _trace_id(scenario.name)
    rows = []
    for index, bitrate_kbps in enumerate(scenario.bitrates_kbps):
        rows.append(
            {
                "segment_index": str(index),
                "representation_bitrate_kbps": str(float(bitrate_kbps)),
                "rebuffer_s": str(float(scenario.rebuffer_s[index])),
                "controller_name": SYNTHETIC_CONTROLLER_NAME,
                "trace_id": trace_id,
                "row_eval_gate": scenario.row_eval_gate,
                "outputs_are_benchmark_results": _json_bool(scenario.outputs_are_benchmark_results),
                "final_qoe_reward_defined": _json_bool(scenario.final_qoe_reward_defined),
                "no_final_ranking": "true",
                "phase": "phase3_5d_synthetic_smoke_source",
                "phase_label": "3.5D synthetic smoke source",
                "schema_version": "synthetic_dry_run_like_v1",
                "segment_duration_s": "2.0",
                "buffer_before_s": "0.0",
                "buffer_after_s": "2.0",
                "download_duration_s": "0.1",
                "measured_throughput_kbps": str(float(bitrate_kbps) * 2.0),
            }
        )

    _write_segments_csv(output_dir / DRY_RUN_SEGMENTS_FILENAME, rows)
    common_payload = {
        "source": "synthetic_controlled_smoke",
        "smoke_phase": SMOKE_PHASE,
        "scenario_name": scenario.name,
        "trace_id": trace_id,
        "controller_name": SYNTHETIC_CONTROLLER_NAME,
        "segment_count": scenario.expected_segment_count,
        "outputs_are_benchmark_results": scenario.outputs_are_benchmark_results,
        "final_qoe_reward_defined": scenario.final_qoe_reward_defined,
        "no_final_ranking": True,
    }
    _write_json(
        output_dir / DRY_RUN_SUMMARY_FILENAME,
        dict(common_payload, artifact_type="trace_dry_run_summary"),
    )
    _write_json(
        output_dir / DRY_RUN_MANIFEST_FILENAME,
        dict(
            common_payload,
            artifact_type="trace_dry_run_manifest",
            artifacts={
                "trace_dry_run_segments": DRY_RUN_SEGMENTS_FILENAME,
                "trace_dry_run_summary": DRY_RUN_SUMMARY_FILENAME,
            },
        ),
    )


def _write_segments_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    fieldnames = [
        "segment_index",
        "representation_bitrate_kbps",
        "rebuffer_s",
        "controller_name",
        "trace_id",
        "row_eval_gate",
        "outputs_are_benchmark_results",
        "final_qoe_reward_defined",
        "no_final_ranking",
        "phase",
        "phase_label",
        "schema_version",
        "segment_duration_s",
        "buffer_before_s",
        "buffer_after_s",
        "download_duration_s",
        "measured_throughput_kbps",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _build_scenario_result(
    scenario: QOESmokeScenario,
    summary: Mapping[str, object],
    qoe_output_dir: Path,
) -> QOESmokeScenarioResult:
    gate_reasons = tuple(str(reason) for reason in summary.get("gate_reasons", ()))
    checks = [
        _is_close(summary["qoe_linear_sum"], scenario.expected_qoe_linear_sum)
        if scenario.expected_qoe_linear_sum is not None
        else True,
        _is_close(summary["qoe_linear_mean"], scenario.expected_qoe_linear_mean)
        if scenario.expected_qoe_linear_mean is not None
        else True,
        summary["session_eval_gate"] == scenario.expected_session_eval_gate,
        summary["outputs_are_benchmark_results"] is False,
        summary["no_final_ranking"] is True,
        _qoe_output_files_exist(qoe_output_dir),
    ]
    if scenario.expected_gate_reason:
        checks.append(scenario.expected_gate_reason in gate_reasons)
    if scenario.name == "source_claims_benchmark":
        checks.append(summary["outputs_are_benchmark_results"] is False)
    if scenario.name == "incomplete_session":
        checks.append(summary["session_completed"] is False)

    return QOESmokeScenarioResult(
        scenario_name=scenario.name,
        trace_id=str(summary["trace_id"]),
        controller_name=str(summary["controller_name"]),
        qoe_linear_sum=float(summary["qoe_linear_sum"]),
        qoe_linear_mean=float(summary["qoe_linear_mean"]),
        session_eval_gate=str(summary["session_eval_gate"]),
        gate_reasons=gate_reasons,
        outputs_are_benchmark_results=bool(summary["outputs_are_benchmark_results"]),
        no_final_ranking=bool(summary["no_final_ranking"]),
        qoe_output_dir=str(qoe_output_dir),
        checks_passed=all(checks),
    )


def _build_smoke_report(
    output_root: Path,
    scenario_results: Sequence[QOESmokeScenarioResult],
) -> Mapping[str, object]:
    scenarios = [
        {
            "scenario_name": result.scenario_name,
            "trace_id": result.trace_id,
            "controller_name": result.controller_name,
            "qoe_linear_sum": result.qoe_linear_sum,
            "qoe_linear_mean": result.qoe_linear_mean,
            "session_eval_gate": result.session_eval_gate,
            "gate_reasons": list(result.gate_reasons),
            "outputs_are_benchmark_results": result.outputs_are_benchmark_results,
            "no_final_ranking": result.no_final_ranking,
            "qoe_output_dir": result.qoe_output_dir,
            "checks_passed": result.checks_passed,
        }
        for result in scenario_results
    ]
    return {
        "artifact_type": "qoe_smoke_report",
        "smoke_phase": SMOKE_PHASE,
        "source": "synthetic_controlled_smoke",
        "outputs_are_benchmark_results": False,
        "no_final_ranking": True,
        "ranking_performed": False,
        "benchmark_performed": False,
        "ia_training_performed": False,
        "output_root": str(output_root),
        "scenario_count": len(scenario_results),
        "all_checks_passed": all(result.checks_passed for result in scenario_results),
        "scenarios": scenarios,
    }


def _qoe_output_files_exist(qoe_output_dir: Path) -> bool:
    return all(
        (qoe_output_dir / filename).is_file()
        for filename in (
            QOE_SEGMENT_REWARDS_FILENAME,
            QOE_RUN_SUMMARY_FILENAME,
            QOE_ARTIFACT_MANIFEST_FILENAME,
        )
    )


def _write_json(path: Path, payload: Mapping[str, object]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _trace_id(scenario_name: str) -> str:
    return "synthetic_smoke_{0}".format(scenario_name)


def _json_bool(value: bool) -> str:
    return str(bool(value)).lower()


def _is_close(value: object, expected: Optional[float], tolerance: float = 1e-9) -> bool:
    if expected is None:
        return True
    return abs(float(value) - expected) <= tolerance


if __name__ == "__main__":
    sys.exit(main())
