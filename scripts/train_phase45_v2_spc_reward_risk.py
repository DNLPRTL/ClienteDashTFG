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

from core.phase45_v1.spc_v2_reward_risk_training import (  # noqa: E402
    SPC_V2_REWARD_RISK_TRAINING_PROFILES,
    profile_by_name,
    train_spc_abr_v2_reward_risk,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_DIR = TFG_ROOT / "datasets_normalizados" / "phase45_v1" / "phase45v2_preference_onpolicy_dataset_v1"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v1" / "spc_abr_v2_reward_risk"
DEFAULT_REFERENCE_POLICY_CHECKPOINT = (
    TFG_ROOT
    / "modelos"
    / "phase45_v1"
    / "spbc_abr_v2_dpo"
    / "full_v1_utility_risk_v1"
    / "modelo_spbc_abr_v2_dpo.pt"
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Entrena offline spc_abr_v2_reward_risk sobre el dataset v2 preference/on-policy."
    )
    parser.add_argument("--profile", choices=sorted(SPC_V2_REWARD_RISK_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=DEFAULT_DATASET_DIR)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--reference-policy-checkpoint", type=Path, default=DEFAULT_REFERENCE_POLICY_CHECKPOINT)
    parser.add_argument(
        "--no-reference-policy-comparison",
        action="store_true",
        help="No compara el scorer contra una politica offline si existe.",
    )
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--best-immediate-ce-loss-weight", type=float, default=None)
    parser.add_argument("--pairwise-score-loss-weight", type=float, default=None)
    parser.add_argument("--reward-loss-weight", type=float, default=None)
    parser.add_argument("--rebuffer-loss-weight", type=float, default=None)
    parser.add_argument("--qoe-gap-loss-weight", type=float, default=None)
    parser.add_argument("--smoothness-loss-weight", type=float, default=None)
    parser.add_argument("--risk-loss-weight", type=float, default=None)
    parser.add_argument("--score-rebuffer-weight", type=float, default=None)
    parser.add_argument("--score-risk-weight", type=float, default=None)
    parser.add_argument("--score-smoothness-weight", type=float, default=None)
    parser.add_argument("--score-qoe-gap-weight", type=float, default=None)
    parser.add_argument("--pairwise-margin-scale", type=float, default=None)
    parser.add_argument("--risk-positive-weight", type=float, default=None)
    parser.add_argument("--focus-bucket-sample-weight", type=float, default=None)
    parser.add_argument("--severe-error-sample-weight", type=float, default=None)
    parser.add_argument("--safe-vs-rebuffer-pair-weight", type=float, default=None)
    parser.add_argument("--over-aggressive-rebuffer-action-weight", type=float, default=None)
    parser.add_argument("--max-pair-weight", type=float, default=None)
    parser.add_argument("--selection-focus-weight", type=float, default=None)
    parser.add_argument("--selection-rebuffer-weight", type=float, default=None)
    parser.add_argument("--selection-over-aggressive-weight", type=float, default=None)
    parser.add_argument("--selection-invalid-weight", type=float, default=None)
    parser.add_argument("--selection-prediction-loss-weight", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)
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

    reference_policy = None if args.no_reference_policy_comparison else args.reference_policy_checkpoint
    progress_started = time.monotonic()
    progress_callback = None if args.quiet_progress else _make_progress_printer(progress_started)
    report = train_spc_abr_v2_reward_risk(
        args.dataset_dir,
        output_dir,
        profile=profile,
        overwrite=args.overwrite,
        device=args.device,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        max_training_samples=max_training_samples,
        max_validation_samples=max_validation_samples,
        validate_dataset=not args.skip_dataset_validation,
        reference_policy_checkpoint=reference_policy,
        progress_callback=progress_callback,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def _profile_with_overrides(args: argparse.Namespace):
    profile = profile_by_name(args.profile)
    replacements: dict[str, object] = {}
    for arg_name, field_name in (
        ("best_immediate_ce_loss_weight", "best_immediate_ce_loss_weight"),
        ("pairwise_score_loss_weight", "pairwise_score_loss_weight"),
        ("reward_loss_weight", "reward_loss_weight"),
        ("rebuffer_loss_weight", "rebuffer_loss_weight"),
        ("qoe_gap_loss_weight", "qoe_gap_loss_weight"),
        ("smoothness_loss_weight", "smoothness_loss_weight"),
        ("risk_loss_weight", "risk_loss_weight"),
        ("score_rebuffer_weight", "score_rebuffer_weight"),
        ("score_risk_weight", "score_risk_weight"),
        ("score_smoothness_weight", "score_smoothness_weight"),
        ("score_qoe_gap_weight", "score_qoe_gap_weight"),
        ("pairwise_margin_scale", "pairwise_margin_scale"),
        ("risk_positive_weight", "risk_positive_weight"),
        ("focus_bucket_sample_weight", "focus_bucket_sample_weight"),
        ("severe_error_sample_weight", "severe_error_sample_weight"),
        ("safe_vs_rebuffer_pair_weight", "safe_vs_rebuffer_pair_weight"),
        ("over_aggressive_rebuffer_action_weight", "over_aggressive_rebuffer_action_weight"),
        ("max_pair_weight", "max_pair_weight"),
        ("selection_focus_weight", "selection_focus_weight"),
        ("selection_rebuffer_weight", "selection_rebuffer_weight"),
        ("selection_over_aggressive_weight", "selection_over_aggressive_weight"),
        ("selection_invalid_weight", "selection_invalid_weight"),
        ("selection_prediction_loss_weight", "selection_prediction_loss_weight"),
    ):
        value = getattr(args, arg_name)
        if value is not None:
            replacements[field_name] = float(value)
    if args.seed is not None:
        replacements["seed"] = int(args.seed)
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
                "reward_mae={reward_mae:.4f} rebuffer_mae={rebuffer_mae:.4f} "
                "risk_brier={risk_brier:.4f} u_regret={u_regret:.4f} "
                "rb_regret={rb_regret:.4f} selection={selection:.4f} "
                "best_epoch={best}{star}"
            ).format(
                elapsed=elapsed,
                epoch=event.get("epoch"),
                epochs=event.get("epochs"),
                duration=_format_seconds(float(event.get("epoch_duration_s", 0.0))),
                train_loss=float(event.get("training_loss", 0.0)),
                val_loss=float(event.get("validation_loss", 0.0)),
                reward_mae=float(event.get("validation_reward_mae", 0.0)),
                rebuffer_mae=float(event.get("validation_rebuffer_mae_s", 0.0)),
                risk_brier=float(event.get("validation_risk_brier", 0.0)),
                u_regret=float(event.get("validation_utility_regret", 0.0)),
                rb_regret=float(event.get("validation_rebuffer_regret", 0.0)),
                selection=float(event.get("validation_selection_score", 0.0)),
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
