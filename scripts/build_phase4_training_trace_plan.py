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

from core.neural_abr.trace_sampling import (
    Phase4SamplingConfig,
    build_phase4_training_trace_artifacts,
    write_phase4_training_trace_artifacts,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "manifests_trazas" / "phase4" / "phase4A_plan_de_trazas_para_entrenamiento"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the Phase 4A balanced training trace plan from the curated Phase 3 manifest."
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--segment-duration-s", type=float, default=4.0)
    parser.add_argument("--window-duration-s", type=float, default=120.0)
    parser.add_argument("--train-window-count", type=int, default=4096)
    parser.add_argument("--validation-window-count", type=int, default=1024)
    parser.add_argument("--synthetic-max-fraction", type=float, default=0.15)
    parser.add_argument("--dataset-max-fraction", type=float, default=0.30)
    parser.add_argument("--semantics-max-fraction", type=float, default=0.35)
    parser.add_argument("--difficulty-max-fraction", type=float, default=0.45)
    parser.add_argument("--max-windows-per-trace", type=int, default=3)
    parser.add_argument("--seed", default="phase4a_training_trace_sampler_v1")
    args = parser.parse_args(argv)

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    config = Phase4SamplingConfig(
        segment_duration_s=args.segment_duration_s,
        window_duration_s=args.window_duration_s,
        train_window_count=args.train_window_count,
        validation_window_count=args.validation_window_count,
        synthetic_max_fraction=args.synthetic_max_fraction,
        dataset_max_fraction=args.dataset_max_fraction,
        semantics_max_fraction=args.semantics_max_fraction,
        difficulty_max_fraction=args.difficulty_max_fraction,
        max_windows_per_trace=args.max_windows_per_trace,
        seed=args.seed,
    )
    artifacts = build_phase4_training_trace_artifacts(
        manifest,
        config=config,
        source_manifest_path=args.manifest,
    )
    written = write_phase4_training_trace_artifacts(args.output_root, artifacts)
    training_plan = artifacts["phase4_plan_de_trazas_para_entrenamiento.json"]
    sampling_audit = artifacts["phase4_auditoria_de_seleccion_de_trazas.json"]
    print(
        json.dumps(
            {
                "status": "PASS",
                "phase": training_plan["phase"],
                "output_root": str(args.output_root),
                "written_files": written,
                "requested_training_window_count": training_plan["requested_training_window_count"],
                "requested_validation_window_count": training_plan["requested_validation_window_count"],
                "training_window_count": training_plan["training_window_count"],
                "validation_window_count": training_plan["validation_window_count"],
                "unfilled_requested_training_window_count": training_plan[
                    "unfilled_requested_training_window_count"
                ],
                "unfilled_requested_validation_window_count": training_plan[
                    "unfilled_requested_validation_window_count"
                ],
                "candidate_window_count": sampling_audit["candidate_window_summary"]["total_candidate_window_count"],
                "benchmark_performed": training_plan["benchmark_performed"],
                "ia_training_performed": training_plan["ia_training_performed"],
                "ranking_performed": training_plan["ranking_performed"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
