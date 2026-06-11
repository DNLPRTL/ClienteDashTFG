#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.controller.registry import create_controller
from core.phase45_v1.spbc_v2_dpo_bundle import (
    SPBC_V2_DPO_CONTROLLER_KEY,
    validate_spbc_v2_dpo_bundle_dir,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_BUNDLE_DIR = (
    TFG_ROOT
    / "modelos"
    / "phase45_v1"
    / "spbc_abr_v2_dpo"
    / "full_v2_anchor_safe_rank_v1_bundle"
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida el bundle SPBC ABR v2 DPO y ejecuta una inferencia smoke sin benchmark."
    )
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--no-verify-hashes", action="store_true")
    parser.add_argument("--max-inference-latency-ms", type=float, default=1000.0)
    args = parser.parse_args(argv)

    verify_hashes = not bool(args.no_verify_hashes)
    validation = validate_spbc_v2_dpo_bundle_dir(args.bundle_dir, verify_hashes=verify_hashes)
    controller = create_controller(
        SPBC_V2_DPO_CONTROLLER_KEY,
        {
            "bundle_dir": str(args.bundle_dir),
            "verify_hashes": verify_hashes,
            "max_inference_latency_ms": float(args.max_inference_latency_ms),
            "diagnostic_only": False,
            "fallback_controller": "robust_mpc",
        },
    )
    feedback = controller.augment_feedback(_smoke_feedback())
    controller.setPlayerFeedback(feedback)
    selected_rate = float(controller.calcControlAction())
    diagnostics = controller.get_neural_diagnostics()
    status = "PASS" if diagnostics.get("neural_fallback_reason") == "success_neural" else "REVIEW"
    report = {
        "schema_id": "phase45_v2_spbc_dpo_bundle_validation_v1",
        "status": status,
        "decision": "BUNDLE_READY_FOR_PHASE6" if status == "PASS" else "CHECK_DIAGNOSTICS_BEFORE_PHASE6",
        "bundle_dir": str(args.bundle_dir),
        "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
        "selected_rate_Bps": selected_rate,
        "selected_level": int(controller.quantizeRate(selected_rate)),
        "diagnostics": diagnostics,
        "manifest_status": validation["status"],
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


def _smoke_feedback() -> dict[str, object]:
    rates = [37500.0, 93750.0, 150000.0, 231250.0, 356250.0, 537500.0]
    return {
        "queued_bytes": 0,
        "queued_time": 8.0,
        "cur_bitrate": rates[0],
        "bwe": 120000.0,
        "level": 0,
        "max_level": len(rates) - 1,
        "cur_rate": rates[0],
        "max_rate": max(rates),
        "min_rate": min(rates),
        "max_bitrate": max(rates),
        "min_bitrate": min(rates),
        "last_fragment_size": 150000,
        "last_download_time": 1.0,
        "downloaded_bytes": 150000,
        "fragment_duration": 4.0,
        "rates": rates,
        "segment_index": 2,
        "total_segments": 30,
        "start_segment_request": 1.0,
        "stop_segment_request": 2.0,
    }


if __name__ == "__main__":
    raise SystemExit(main())
