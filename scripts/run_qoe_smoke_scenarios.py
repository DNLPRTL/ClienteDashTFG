#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
TFG_ROOT = REPO_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.evaluation.artifacts import (
    DRY_RUN_MANIFEST_FILENAME,
    DRY_RUN_SEGMENTS_FILENAME,
    DRY_RUN_SUMMARY_FILENAME,
    QOE_RUN_SUMMARY_FILENAME,
    compute_qoe_artifacts_from_dry_run,
)


DEFAULT_OUTPUT_ROOT = TFG_ROOT / "runs_trazas" / "phase3_5" / "smoke"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run controlled synthetic QoE smoke scenarios.")
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args(argv)
    report = run_qoe_smoke_scenarios(args.output_root, clean=args.clean)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["all_checks_passed"] else 1


def run_qoe_smoke_scenarios(output_root: str | Path, clean: bool = False) -> dict[str, object]:
    root = Path(output_root)
    if clean and root.exists():
        _assert_clean_target(root)
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)

    scenario_results = []
    for scenario in _scenarios():
        scenario_root = root / "scenarios" / scenario["name"]
        dry_run_dir = scenario_root / "dry_run"
        qoe_dir = scenario_root / "qoe"
        dry_run_dir.mkdir(parents=True, exist_ok=True)
        _write_dry_run_like_artifacts(dry_run_dir, scenario)
        result = compute_qoe_artifacts_from_dry_run(
            dry_run_dir=dry_run_dir,
            output_dir=qoe_dir,
            overwrite=True,
        )
        qoe_summary = json.loads((qoe_dir / QOE_RUN_SUMMARY_FILENAME).read_text(encoding="utf-8"))
        scenario_results.append(
            {
                "scenario": scenario["name"],
                "expected_gate": scenario["expected_gate"],
                "observed_gate": result.session_eval_gate,
                "expected_reasons": scenario["expected_reasons"],
                "observed_reasons": list(result.gate_reasons),
                "qoe_linear_sum": qoe_summary["qoe_sum"],
                "qoe_linear_mean": qoe_summary["qoe_mean"],
                "outputs_are_benchmark_results": qoe_summary["outputs_are_benchmark_results"],
                "no_final_ranking": qoe_summary["no_final_ranking"],
                "ranking_performed": qoe_summary["ranking_performed"],
                "benchmark_performed": qoe_summary["benchmark_performed"],
                "ia_training_performed": qoe_summary["ia_training_performed"],
                "passed": _scenario_passed(scenario, qoe_summary),
            }
        )

    report = {
        "schema_id": "phase3_5_qoe_smoke_report_v1",
        "phase": "phase3_5_rebuild",
        "scenario_count": len(scenario_results),
        "scenarios": scenario_results,
        "all_checks_passed": all(result["passed"] for result in scenario_results),
        "outputs_are_benchmark_results": False,
        "no_final_ranking": True,
        "ranking_performed": False,
        "benchmark_performed": False,
        "ia_training_performed": False,
    }
    (root / "qoe_smoke_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _scenarios() -> list[dict[str, object]]:
    base_rows = [
        {"representation_bitrate_kbps": 1000, "rebuffer_s": 0.0, "row_eval_gate": "use_for_eval"},
        {"representation_bitrate_kbps": 2000, "rebuffer_s": 0.0, "row_eval_gate": "use_for_eval"},
        {"representation_bitrate_kbps": 1000, "rebuffer_s": 0.0, "row_eval_gate": "use_for_eval"},
    ]
    return [
        {
            "name": "complete_use_for_eval",
            "rows": base_rows,
            "summary": {"expected_segment_count": 3, "session_completed": True, "startup_delay_s": 0.0},
            "manifest": {
                "final_qoe_reward_defined": True,
                "outputs_are_benchmark_results": False,
                "no_final_ranking": True,
                "row_eval_gate": "use_for_eval",
            },
            "expected_gate": "use_for_eval",
            "expected_reasons": [],
        },
        {
            "name": "legacy_do_not_use_for_eval",
            "rows": [
                {**row, "row_eval_gate": "do_not_use_for_eval"}
                for row in base_rows
            ],
            "summary": {"expected_segment_count": 3, "session_completed": True, "startup_delay_s": 0.0},
            "manifest": {
                "legacy_dry_run": True,
                "generated_before_phase_3_5a2": True,
                "final_qoe_reward_defined": False,
                "outputs_are_benchmark_results": False,
                "no_final_ranking": True,
                "row_eval_gate": "do_not_use_for_eval",
                "gate_reasons": ["legacy_dry_run"],
            },
            "expected_gate": "do_not_use_for_eval",
            "expected_reasons": ["legacy_dry_run"],
        },
        {
            "name": "incomplete_session",
            "rows": base_rows,
            "summary": {"expected_segment_count": 4, "session_completed": False, "startup_delay_s": 0.0},
            "manifest": {
                "final_qoe_reward_defined": True,
                "outputs_are_benchmark_results": False,
                "no_final_ranking": True,
                "row_eval_gate": "use_for_eval",
            },
            "expected_gate": "do_not_use_for_eval",
            "expected_reasons": ["incomplete_session"],
        },
        {
            "name": "source_claims_benchmark",
            "rows": base_rows,
            "summary": {"expected_segment_count": 3, "session_completed": True, "startup_delay_s": 0.0},
            "manifest": {
                "final_qoe_reward_defined": True,
                "outputs_are_benchmark_results": True,
                "no_final_ranking": False,
                "row_eval_gate": "use_for_eval",
            },
            "expected_gate": "do_not_use_for_eval",
            "expected_reasons": ["source_claims_benchmark_result"],
        },
    ]


def _write_dry_run_like_artifacts(path: Path, scenario: dict[str, object]) -> None:
    rows = scenario["rows"]
    with (path / DRY_RUN_SEGMENTS_FILENAME).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["segment_index", "representation_bitrate_kbps", "rebuffer_s", "row_eval_gate"],
        )
        writer.writeheader()
        for index, row in enumerate(rows):
            writer.writerow({"segment_index": index, **row})
    (path / DRY_RUN_SUMMARY_FILENAME).write_text(
        json.dumps(scenario["summary"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (path / DRY_RUN_MANIFEST_FILENAME).write_text(
        json.dumps(scenario["manifest"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _scenario_passed(scenario: dict[str, object], summary: dict[str, object]) -> bool:
    expected_reasons = set(scenario["expected_reasons"])
    observed_reasons = set(summary["gate_reasons"])
    return (
        summary["session_eval_gate"] == scenario["expected_gate"]
        and expected_reasons.issubset(observed_reasons)
        and summary["outputs_are_benchmark_results"] is False
        and summary["no_final_ranking"] is True
        and summary["ranking_performed"] is False
        and summary["benchmark_performed"] is False
        and summary["ia_training_performed"] is False
    )


def _assert_clean_target(path: Path) -> None:
    resolved = path.resolve()
    allowed = (TFG_ROOT / "runs_trazas").resolve()
    if not str(resolved).startswith(str(allowed)):
        raise ValueError("refusing to clean output outside runs_trazas: {0}".format(resolved))


if __name__ == "__main__":
    raise SystemExit(main())
