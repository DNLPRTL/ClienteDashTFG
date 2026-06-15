#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.controller.registry import create_controller
from core.phase45_v3.neural_mpc_controller import NEURAL_MPC_CONTROLLER_KEY


DEFAULT_BUNDLE_DIR = Path.home() / "TFG" / "modelos" / "phase45_v3" / "neural_mpc_experimental_candidate_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Smoke no-benchmark del controller runtime Neural-MPC Phase45 v3."
    )
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--max-inference-latency-ms", type=float, default=1000.0)
    args = parser.parse_args(argv)

    controller = create_controller(
        NEURAL_MPC_CONTROLLER_KEY,
        {
            "bundle_dir": str(args.bundle_dir),
            "fallback_controller": "robust_mpc",
            "verify_hashes": True,
            "max_inference_latency_ms": float(args.max_inference_latency_ms),
            "diagnostic_only": True,
        },
    )
    feedback = _smoke_feedback()
    controller.setPlayerFeedback(feedback)
    selected_rate = float(controller.calcControlAction())
    selected_level = int(controller.quantizeRate(selected_rate))
    diagnostics = controller.get_neural_diagnostics()
    status = (
        "PASS"
        if diagnostics.get("neural_bundle_loaded") == 1
        and diagnostics.get("neural_bundle_hash_ok") == 1
        and diagnostics.get("neural_valid_action") == 1
        and diagnostics.get("neural_fallback_used") == 0
        and diagnostics.get("neural_fallback_reason") == "success_neural"
        else "REVIEW"
    )
    report = {
        "schema_id": "phase45_v3_neural_mpc_runtime_controller_smoke_v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": status,
        "decision": "RUNTIME_CONTROLLER_LOADS_AND_SELECTS" if status == "PASS" else "CHECK_RUNTIME_DIAGNOSTICS",
        "controller_key": NEURAL_MPC_CONTROLLER_KEY,
        "bundle_dir": str(args.bundle_dir),
        "selected_rate_Bps": selected_rate,
        "selected_level": selected_level,
        "diagnostics": diagnostics,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "phase6_formal_evaluation_performed": False,
        "qoe_claims_authorized": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


def _smoke_feedback() -> dict[str, object]:
    rates = [37500.0, 93750.0, 150000.0, 231250.0, 356250.0, 537500.0]
    return {
        "queued_bytes": 0,
        "queued_time": 12.0,
        "cur_bitrate": rates[2],
        "bwe": 750000.0,
        "level": 2,
        "max_level": len(rates) - 1,
        "cur_rate": rates[2],
        "max_rate": max(rates),
        "min_rate": min(rates),
        "max_bitrate": max(rates),
        "min_bitrate": min(rates),
        "last_fragment_size": 450000,
        "last_download_time": 0.75,
        "downloaded_bytes": 450000,
        "fragment_duration": 4.0,
        "rates": rates,
        "segment_index": 4,
        "total_segments": 30,
        "start_segment_request": 1.0,
        "stop_segment_request": 1.75,
    }


if __name__ == "__main__":
    raise SystemExit(main())
