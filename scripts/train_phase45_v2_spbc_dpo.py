#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase45_v1.spbc_v2_dpo_training import (  # noqa: E402
    SPBC_V2_DPO_TRAINING_PROFILES,
    profile_by_name,
    train_spbc_abr_v2_dpo,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_DIR = TFG_ROOT / "datasets_normalizados" / "phase45_v1" / "phase45v2_preference_onpolicy_dataset_v1"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo"
DEFAULT_INIT_CHECKPOINT = (
    TFG_ROOT / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Entrena offline spbc_abr_v2_dpo sobre el dataset v2 preference/on-policy."
    )
    parser.add_argument("--profile", choices=sorted(SPBC_V2_DPO_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=DEFAULT_DATASET_DIR)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--init-spbc-v1-checkpoint", type=Path, default=DEFAULT_INIT_CHECKPOINT)
    parser.add_argument(
        "--allow-random-init-full",
        action="store_true",
        help="Permite full_v1 sin referencia spbc_abr_v1; solo para diagnostico explicito.",
    )
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--ce-loss-weight", type=float, default=None)
    parser.add_argument("--dpo-loss-weight", type=float, default=None)
    parser.add_argument("--ranking-loss-weight", type=float, default=None)
    parser.add_argument("--dpo-beta", type=float, default=None)
    parser.add_argument("--ranking-margin-scale", type=float, default=None)
    parser.add_argument("--max-pair-weight", type=float, default=None)
    parser.add_argument("--max-training-samples", type=int, default=None)
    parser.add_argument("--max-validation-samples", type=int, default=None)
    parser.add_argument(
        "--no-profile-sample-limits",
        action="store_true",
        help="Usa todo el dataset aunque el perfil smoke/pilot tenga limites por defecto.",
    )
    parser.add_argument("--skip-dataset-validation", action="store_true")
    parser.add_argument(
        "--quiet-progress",
        action="store_true",
        help="No muestra progreso incremental por stderr; el JSON final se sigue escribiendo por stdout.",
    )
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    profile = _profile_with_overrides(args)
    output_dir = args.output_dir or (DEFAULT_MODEL_ROOT / args.profile)
    max_training_samples: int | None | str = None if args.no_profile_sample_limits else "profile"
    max_validation_samples: int | None | str = None if args.no_profile_sample_limits else "profile"
    if args.max_training_samples is not None:
        max_training_samples = args.max_training_samples
    if args.max_validation_samples is not None:
        max_validation_samples = args.max_validation_samples

    progress_started = time.monotonic()
    progress_callback = None if args.quiet_progress else _make_progress_printer(progress_started)
    report = train_spbc_abr_v2_dpo(
        args.dataset_dir,
        output_dir,
        profile=profile,
        overwrite=args.overwrite,
        device=args.device,
        init_checkpoint=args.init_spbc_v1_checkpoint,
        allow_random_init_full=args.allow_random_init_full,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        max_training_samples=max_training_samples,
        max_validation_samples=max_validation_samples,
        validate_dataset=not args.skip_dataset_validation,
        progress_callback=progress_callback,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def _profile_with_overrides(args: argparse.Namespace):
    profile = profile_by_name(args.profile)
    replacements: dict[str, object] = {}
    for arg_name, field_name in (
        ("ce_loss_weight", "ce_loss_weight"),
        ("dpo_loss_weight", "dpo_loss_weight"),
        ("ranking_loss_weight", "ranking_loss_weight"),
        ("dpo_beta", "dpo_beta"),
        ("ranking_margin_scale", "ranking_margin_scale"),
        ("max_pair_weight", "max_pair_weight"),
    ):
        value = getattr(args, arg_name)
        if value is not None:
            replacements[field_name] = float(value)
    return replace(profile, **replacements) if replacements else profile


def _make_progress_printer(started: float):
    def _print_progress(event: Mapping[str, object]) -> None:
        event_key = str(event.get("event", "progress"))
        elapsed = _format_seconds(time.monotonic() - started)
        if event_key == "training_batch":
            epoch = event.get("epoch")
            epochs = event.get("epochs")
            batch = int(event.get("batch", 0))
            batches = int(event.get("batches", 1))
            percent = 100.0 * float(batch) / max(float(batches), 1.0)
            eta = _format_seconds(float(event.get("eta_s", 0.0)))
            loss = float(event.get("loss", 0.0))
            line = (
                "[{elapsed}] epoca {epoch}/{epochs} batch {batch}/{batches} "
                "({percent:5.1f}%) loss={loss:.4f} eta_epoca={eta}"
            ).format(
                elapsed=elapsed,
                epoch=epoch,
                epochs=epochs,
                batch=batch,
                batches=batches,
                percent=percent,
                loss=loss,
                eta=eta,
            )
        elif event_key == "epoch_finished":
            line = (
                "[{elapsed}] epoca {epoch}/{epochs} lista en {duration}; "
                "train_loss={train_loss:.4f} val_loss={val_loss:.4f} "
                "top1={top1:.4f} pair_acc={pair_acc:.4f} qoe_gap={qoe_gap:.4f} best_epoch={best}{star}"
            ).format(
                elapsed=elapsed,
                epoch=event.get("epoch"),
                epochs=event.get("epochs"),
                duration=_format_seconds(float(event.get("epoch_duration_s", 0.0))),
                train_loss=float(event.get("training_loss", 0.0)),
                val_loss=float(event.get("validation_loss", 0.0)),
                top1=float(event.get("validation_top1_accuracy", 0.0)),
                pair_acc=float(event.get("validation_pair_preference_accuracy", 0.0)),
                qoe_gap=float(event.get("validation_predicted_qoe_gap_mean", 0.0)),
                best=event.get("best_epoch"),
                star=" nuevo_mejor" if event.get("best_so_far") is True else "",
            )
        elif event_key == "examples_loaded":
            line = "[{0}] muestras cargadas: train={1} validation={2}".format(
                elapsed,
                event.get("training_samples"),
                event.get("validation_samples"),
            )
        elif event_key == "finished":
            line = "[{0}] terminado en {1}; best_epoch={2}; salida={3}".format(
                elapsed,
                _format_seconds(float(event.get("training_duration_s", 0.0))),
                event.get("best_epoch"),
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
