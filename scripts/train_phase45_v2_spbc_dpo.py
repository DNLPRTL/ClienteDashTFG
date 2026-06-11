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
DEFAULT_INIT_SPBC_V1_CHECKPOINT = (
    TFG_ROOT / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Entrena offline spbc_abr_v2_dpo sobre el dataset v2 preference/on-policy."
    )
    parser.add_argument("--profile", choices=sorted(SPBC_V2_DPO_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=DEFAULT_DATASET_DIR)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument(
        "--init-checkpoint",
        type=Path,
        default=None,
        help="Checkpoint inicial congelado para warm-start y DPO reference; acepta spbc_abr_v1 o spbc_abr_v2_dpo.",
    )
    parser.add_argument(
        "--init-spbc-v1-checkpoint",
        type=Path,
        default=None,
        help="Alias legacy para --init-checkpoint con spbc_abr_v1/full_v1.",
    )
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
    parser.add_argument("--utility-loss-weight", type=float, default=None)
    parser.add_argument("--rebuffer-loss-weight", type=float, default=None)
    parser.add_argument("--dpo-beta", type=float, default=None)
    parser.add_argument("--ranking-margin-scale", type=float, default=None)
    parser.add_argument("--utility-temperature", type=float, default=None)
    parser.add_argument("--rebuffer-loss-cap-s", type=float, default=None)
    parser.add_argument("--aux-reward-loss-weight", type=float, default=None)
    parser.add_argument("--aux-rebuffer-loss-weight", type=float, default=None)
    parser.add_argument("--aux-risk-loss-weight", type=float, default=None)
    parser.add_argument("--reference-kl-loss-weight", type=float, default=None)
    parser.add_argument("--over-aggressive-probability-loss-weight", type=float, default=None)
    parser.add_argument("--over-aggressive-margin-loss-weight", type=float, default=None)
    parser.add_argument("--over-aggressive-reference-excess-loss-weight", type=float, default=None)
    parser.add_argument("--over-aggressive-margin", type=float, default=None)
    parser.add_argument("--safe-utility-rank-loss-weight", type=float, default=None)
    parser.add_argument("--safe-utility-margin", type=float, default=None)
    parser.add_argument("--safe-improvement-rank-loss-weight", type=float, default=None)
    parser.add_argument("--safe-improvement-reward-margin", type=float, default=None)
    parser.add_argument("--copy-baseline-loss-weight", type=float, default=None)
    parser.add_argument("--copy-baseline-reward-margin", type=float, default=None)
    parser.add_argument("--residual-logit-l2-loss-weight", type=float, default=None)
    parser.add_argument("--ppo-clip-loss-weight", type=float, default=None)
    parser.add_argument("--ppo-clip-epsilon", type=float, default=None)
    parser.add_argument("--ppo-advantage-clip", type=float, default=None)
    parser.add_argument("--ppo-over-aggressive-advantage-penalty", type=float, default=None)
    parser.add_argument("--ppo-rebuffer-advantage-penalty", type=float, default=None)
    parser.add_argument("--ppo-risk-advantage-penalty", type=float, default=None)
    parser.add_argument("--decision-reward-fusion-weight", type=float, default=None)
    parser.add_argument("--decision-rebuffer-fusion-weight", type=float, default=None)
    parser.add_argument("--decision-risk-fusion-weight", type=float, default=None)
    parser.add_argument("--focus-bucket-sample-weight", type=float, default=None)
    parser.add_argument("--severe-error-sample-weight", type=float, default=None)
    parser.add_argument("--safe-vs-rebuffer-pair-weight", type=float, default=None)
    parser.add_argument("--over-aggressive-rebuffer-action-weight", type=float, default=None)
    parser.add_argument("--selection-focus-weight", type=float, default=None)
    parser.add_argument("--selection-rebuffer-weight", type=float, default=None)
    parser.add_argument("--selection-over-aggressive-weight", type=float, default=None)
    parser.add_argument("--selection-invalid-weight", type=float, default=None)
    parser.add_argument(
        "--enable-safety-gate",
        action="store_true",
        help="Activa seleccion constrained: un epoch inseguro frente al checkpoint inicial no puede ser best_epoch.",
    )
    parser.add_argument("--safety-global-over-aggressive-tolerance", type=float, default=None)
    parser.add_argument("--safety-focus-over-aggressive-tolerance", type=float, default=None)
    parser.add_argument("--safety-spbc-v2-over-aggressive-tolerance", type=float, default=None)
    parser.add_argument("--safety-utility-regret-tolerance", type=float, default=None)
    parser.add_argument("--safety-rebuffer-regret-tolerance", type=float, default=None)
    parser.add_argument("--max-pair-weight", type=float, default=None)
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
    if args.init_checkpoint is not None and args.init_spbc_v1_checkpoint is not None:
        parser.error("usa solo uno de --init-checkpoint o --init-spbc-v1-checkpoint")

    profile = _profile_with_overrides(args)
    output_dir = args.output_dir or (DEFAULT_MODEL_ROOT / args.profile)
    init_checkpoint = args.init_checkpoint or args.init_spbc_v1_checkpoint or DEFAULT_INIT_SPBC_V1_CHECKPOINT
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
        init_checkpoint=init_checkpoint,
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
    if args.enable_safety_gate:
        replacements["safety_gate_enabled"] = True
    if args.seed is not None:
        replacements["seed"] = int(args.seed)
    for arg_name, field_name in (
        ("ce_loss_weight", "ce_loss_weight"),
        ("dpo_loss_weight", "dpo_loss_weight"),
        ("ranking_loss_weight", "ranking_loss_weight"),
        ("utility_loss_weight", "utility_loss_weight"),
        ("rebuffer_loss_weight", "rebuffer_loss_weight"),
        ("dpo_beta", "dpo_beta"),
        ("ranking_margin_scale", "ranking_margin_scale"),
        ("utility_temperature", "utility_temperature"),
        ("rebuffer_loss_cap_s", "rebuffer_loss_cap_s"),
        ("aux_reward_loss_weight", "aux_reward_loss_weight"),
        ("aux_rebuffer_loss_weight", "aux_rebuffer_loss_weight"),
        ("aux_risk_loss_weight", "aux_risk_loss_weight"),
        ("reference_kl_loss_weight", "reference_kl_loss_weight"),
        ("over_aggressive_probability_loss_weight", "over_aggressive_probability_loss_weight"),
        ("over_aggressive_margin_loss_weight", "over_aggressive_margin_loss_weight"),
        ("over_aggressive_reference_excess_loss_weight", "over_aggressive_reference_excess_loss_weight"),
        ("over_aggressive_margin", "over_aggressive_margin"),
        ("safe_utility_rank_loss_weight", "safe_utility_rank_loss_weight"),
        ("safe_utility_margin", "safe_utility_margin"),
        ("safe_improvement_rank_loss_weight", "safe_improvement_rank_loss_weight"),
        ("safe_improvement_reward_margin", "safe_improvement_reward_margin"),
        ("copy_baseline_loss_weight", "copy_baseline_loss_weight"),
        ("copy_baseline_reward_margin", "copy_baseline_reward_margin"),
        ("residual_logit_l2_loss_weight", "residual_logit_l2_loss_weight"),
        ("ppo_clip_loss_weight", "ppo_clip_loss_weight"),
        ("ppo_clip_epsilon", "ppo_clip_epsilon"),
        ("ppo_advantage_clip", "ppo_advantage_clip"),
        ("ppo_over_aggressive_advantage_penalty", "ppo_over_aggressive_advantage_penalty"),
        ("ppo_rebuffer_advantage_penalty", "ppo_rebuffer_advantage_penalty"),
        ("ppo_risk_advantage_penalty", "ppo_risk_advantage_penalty"),
        ("decision_reward_fusion_weight", "decision_reward_fusion_weight"),
        ("decision_rebuffer_fusion_weight", "decision_rebuffer_fusion_weight"),
        ("decision_risk_fusion_weight", "decision_risk_fusion_weight"),
        ("focus_bucket_sample_weight", "focus_bucket_sample_weight"),
        ("severe_error_sample_weight", "severe_error_sample_weight"),
        ("safe_vs_rebuffer_pair_weight", "safe_vs_rebuffer_pair_weight"),
        ("over_aggressive_rebuffer_action_weight", "over_aggressive_rebuffer_action_weight"),
        ("selection_focus_weight", "selection_focus_weight"),
        ("selection_rebuffer_weight", "selection_rebuffer_weight"),
        ("selection_over_aggressive_weight", "selection_over_aggressive_weight"),
        ("selection_invalid_weight", "selection_invalid_weight"),
        ("safety_global_over_aggressive_tolerance", "safety_global_over_aggressive_tolerance"),
        ("safety_focus_over_aggressive_tolerance", "safety_focus_over_aggressive_tolerance"),
        ("safety_spbc_v2_over_aggressive_tolerance", "safety_spbc_v2_over_aggressive_tolerance"),
        ("safety_utility_regret_tolerance", "safety_utility_regret_tolerance"),
        ("safety_rebuffer_regret_tolerance", "safety_rebuffer_regret_tolerance"),
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
                "top1={top1:.4f} pair_acc={pair_acc:.4f} qoe_gap={qoe_gap:.4f} "
                "u_regret={u_regret:.4f} rb_regret={rb_regret:.4f} "
                "over={over:.4f} focus_over={focus_over:.4f} safe={safe} "
                "selection={selection:.4f} best_epoch={best}{star}"
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
                u_regret=float(event.get("validation_utility_regret", 0.0)),
                rb_regret=float(event.get("validation_rebuffer_regret", 0.0)),
                over=float(event.get("validation_over_aggressive", 0.0)),
                focus_over=float(event.get("validation_focus_over_aggressive", 0.0)),
                safe="yes" if event.get("validation_safety_gate_passed") is True else "no",
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
