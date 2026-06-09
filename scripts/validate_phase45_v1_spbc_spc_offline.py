#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase45_v1.offline_validation import (
    OFFLINE_VALIDATION_PROFILES,
    profile_by_name,
    validate_spbc_spc_offline,
)
from core.phase45_v1.constants import SPBC_MODEL_FILENAME, SPC_MODEL_FILENAME


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_DIR = TFG_ROOT / "datasets_normalizados" / "phase45_v1" / "phase45v1B_spc_spbc_dataset_v1"
DEFAULT_SPBC_CHECKPOINT = TFG_ROOT / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / SPBC_MODEL_FILENAME
DEFAULT_SPC_CHECKPOINT = TFG_ROOT / "modelos" / "phase45_v1" / "spc_abr_v1" / "full_v1" / SPC_MODEL_FILENAME
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "modelos" / "phase45_v1" / "offline_validation" / "spbc_spc_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Valida offline spbc_abr_v1 + spc_abr_v1 sin ejecutar Phase 6.")
    parser.add_argument("--profile", choices=sorted(OFFLINE_VALIDATION_PROFILES), default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=DEFAULT_DATASET_DIR)
    parser.add_argument("--spbc-checkpoint", type=Path, default=DEFAULT_SPBC_CHECKPOINT)
    parser.add_argument("--spc-checkpoint", type=Path, default=DEFAULT_SPC_CHECKPOINT)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument("--risk-threshold", type=float, default=0.50)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--max-validation-samples", type=int, default=None)
    parser.add_argument(
        "--no-profile-sample-limits",
        action="store_true",
        help="Usa todo validation aunque el perfil smoke/pilot tenga limite por defecto.",
    )
    parser.add_argument("--skip-dataset-validation", action="store_true")
    parser.add_argument(
        "--quiet-progress",
        action="store_true",
        help="No muestra progreso incremental por stderr; el JSON final se sigue escribiendo por stdout.",
    )
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    profile = profile_by_name(args.profile)
    output_dir = args.output_dir or (DEFAULT_OUTPUT_ROOT / args.profile)
    max_validation_samples = None if args.no_profile_sample_limits else "profile"
    if args.max_validation_samples is not None:
        max_validation_samples = args.max_validation_samples

    progress_started = time.monotonic()
    progress_callback = None if args.quiet_progress else _make_progress_printer(progress_started)
    report = validate_spbc_spc_offline(
        args.dataset_dir,
        args.spbc_checkpoint,
        args.spc_checkpoint,
        output_dir,
        profile=profile,
        overwrite=args.overwrite,
        device=args.device,
        risk_threshold=args.risk_threshold,
        batch_size=args.batch_size,
        max_validation_samples=max_validation_samples,
        validate_dataset=not args.skip_dataset_validation,
        progress_callback=progress_callback,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def _make_progress_printer(started: float):
    def _print_progress(event: Mapping[str, object]) -> None:
        event_key = str(event.get("event", "progress"))
        elapsed = _format_seconds(time.monotonic() - started)
        if event_key == "validation_batch":
            batch = int(event.get("batch", 0))
            batches = int(event.get("batches", 1))
            percent = 100.0 * float(batch) / max(float(batches), 1.0)
            line = "[{elapsed}] validacion batch {batch}/{batches} ({percent:5.1f}%)".format(
                elapsed=elapsed,
                batch=batch,
                batches=batches,
                percent=percent,
            )
        elif event_key == "examples_loaded":
            line = "[{0}] muestras cargadas: validation={1}".format(elapsed, event.get("validation_samples"))
        elif event_key == "finished":
            line = "[{0}] terminado en {1}; gate={2}; salida={3}".format(
                elapsed,
                _format_seconds(float(event.get("validation_duration_s", 0.0))),
                event.get("offline_gate_status"),
                event.get("output_dir"),
            )
        else:
            line = "[{0}] {1}".format(elapsed, event.get("message", event_key))
        print(line, file=sys.stderr, flush=True)

    return _print_progress


def _format_seconds(value: float) -> str:
    seconds = max(int(round(float(value))), 0)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return "{0:d}h{1:02d}m{2:02d}s".format(hours, minutes, seconds)
    if minutes:
        return "{0:d}m{1:02d}s".format(minutes, seconds)
    return "{0:d}s".format(seconds)


if __name__ == "__main__":
    raise SystemExit(main())
