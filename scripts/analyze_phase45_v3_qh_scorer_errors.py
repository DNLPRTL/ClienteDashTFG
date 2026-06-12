#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from dataclasses import fields
from pathlib import Path
from typing import Mapping, Sequence

import torch


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.artifacts import read_jsonl, write_json
from core.phase45_v3.constants import VALIDATION_DATA_FILENAME, VALIDATION_ROLE
from core.phase45_v3.qh_scorer_training import (
    QH_SCORER_MODEL_FILENAME,
    QhScorerNormalization,
    QhScorerTrainingProfile,
    _build_qh_scorer_model,
    examples_to_tensors,
    load_qh_scorer_examples,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3" / "qh_closed_loop_pilot"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v3" / "qh_scorer"
DEFAULT_REPORT_FILENAME = "analisis_errores_phase45_v3_qh_scorer.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analiza errores de un scorer Phase45 v3 Q_H.")
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--model-path", type=Path, default=None)
    parser.add_argument("--dataset-dir", type=Path, default=DEFAULT_DATASET_ROOT)
    parser.add_argument("--output-json", type=Path, default=None)
    parser.add_argument("--top-n", type=int, default=100)
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args(argv)

    model_path = _resolve_model_path(args.run_name, args.model_path)
    output_json = args.output_json or model_path.parent / DEFAULT_REPORT_FILENAME
    report = analyze_qh_scorer_errors(
        model_path=model_path,
        dataset_dir=args.dataset_dir,
        output_json=output_json,
        top_n=args.top_n,
        device=args.device,
    )
    _print_compact(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def analyze_qh_scorer_errors(
    *,
    model_path: Path,
    dataset_dir: Path,
    output_json: Path,
    top_n: int,
    device: str,
) -> Mapping[str, object]:
    checkpoint = torch.load(model_path.expanduser(), map_location="cpu", weights_only=False)
    profile = _profile_from_checkpoint(checkpoint["profile"])
    normalization = _normalization_from_checkpoint(checkpoint["normalization"])
    examples = load_qh_scorer_examples(dataset_dir.expanduser() / VALIDATION_DATA_FILENAME, VALIDATION_ROLE, None)
    raw_rows = read_jsonl(dataset_dir.expanduser() / VALIDATION_DATA_FILENAME)
    tensors = examples_to_tensors(examples, normalization)
    model = _build_qh_scorer_model(profile)
    model.load_state_dict(checkpoint["model_state_dict"])
    active_device = torch.device(device)
    model.to(active_device)
    model.eval()

    context, candidates, masks, q_values_norm, selected, high_capacity = tuple(tensor.to(active_device) for tensor in tensors)
    with torch.no_grad():
        scores = model(context, candidates, masks)
        predicted = torch.argmax(scores, dim=1)
    q_values = q_values_norm * float(normalization.q_value_std) + float(normalization.q_value_mean)
    selected_q = torch.gather(q_values, 1, selected.unsqueeze(1)).squeeze(1)
    predicted_q = torch.gather(q_values, 1, predicted.unsqueeze(1)).squeeze(1)
    regret = torch.clamp(selected_q - predicted_q, min=0.0)

    rows = []
    for index, raw in enumerate(raw_rows):
        metadata = raw.get("metadata", {})
        model_inputs = raw.get("model_inputs", {})
        context_mapping = model_inputs.get("context", {}) if isinstance(model_inputs, Mapping) else {}
        row = {
            "sample_index": index,
            "sample_id": raw.get("sample_id"),
            "regret_q_h": float(regret[index].detach().cpu()),
            "target_action": int(selected[index].detach().cpu()),
            "predicted_action": int(predicted[index].detach().cpu()),
            "target_q_h": float(selected_q[index].detach().cpu()),
            "predicted_q_h": float(predicted_q[index].detach().cpu()),
            "high_capacity_state": bool(float(high_capacity[index].detach().cpu()) > 0.5),
            "buffer_s": _float_or_none(context_mapping.get("buffer_s") if isinstance(context_mapping, Mapping) else None),
            "last_bitrate_bps": _float_or_none(context_mapping.get("last_bitrate_bps") if isinstance(context_mapping, Mapping) else None),
            "recent_rebuffer_s": _float_or_none(context_mapping.get("recent_rebuffer_s") if isinstance(context_mapping, Mapping) else None),
            "throughput_bucket": _metadata_value(metadata, "throughput_bucket"),
            "variability_bucket": _metadata_value(metadata, "variability_bucket"),
            "rollout_policy": _metadata_value(metadata, "rollout_policy"),
            "dataset_id": _metadata_value(metadata, "dataset_id"),
            "semantics": _metadata_value(metadata, "semantics"),
            "synthetic": _metadata_value(metadata, "synthetic"),
            "segment_index": _metadata_value(metadata, "segment_index"),
        }
        row["buffer_bucket"] = _bucket_buffer(row["buffer_s"])
        row["last_bitrate_bucket"] = _bucket_bitrate(row["last_bitrate_bps"])
        row["regret_bucket"] = _bucket_regret(row["regret_q_h"])
        rows.append(row)

    sorted_rows = sorted(rows, key=lambda item: float(item["regret_q_h"]), reverse=True)
    report = {
        "schema_id": "phase45_v3_qh_scorer_error_analysis_v1",
        "status": "PASS",
        "model_path": str(model_path.expanduser()),
        "model_sha256": checkpoint.get("model_sha256"),
        "dataset_dir": str(dataset_dir.expanduser()),
        "output_json": str(output_json.expanduser()),
        "profile": profile.to_json(),
        "sample_count": len(rows),
        "overall": _summary(rows),
        "by_target_action": _summaries_by(rows, "target_action"),
        "by_predicted_action": _summaries_by(rows, "predicted_action"),
        "by_rollout_policy": _summaries_by(rows, "rollout_policy"),
        "by_throughput_bucket": _summaries_by(rows, "throughput_bucket"),
        "by_variability_bucket": _summaries_by(rows, "variability_bucket"),
        "by_buffer_bucket": _summaries_by(rows, "buffer_bucket"),
        "by_last_bitrate_bucket": _summaries_by(rows, "last_bitrate_bucket"),
        "by_high_capacity_state": _summaries_by(rows, "high_capacity_state"),
        "by_regret_bucket": _count_by(rows, "regret_bucket"),
        "confusion_target_predicted": _confusion(rows),
        "top_errors": sorted_rows[: max(int(top_n), 0)],
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
    }
    write_json(output_json.expanduser(), report)
    return report


def _resolve_model_path(run_name: str | None, model_path: Path | None) -> Path:
    if model_path is not None:
        return model_path
    if run_name is None:
        raise SystemExit("pass --run-name or --model-path")
    return DEFAULT_MODEL_ROOT / run_name / QH_SCORER_MODEL_FILENAME


def _profile_from_checkpoint(payload: Mapping[str, object]) -> QhScorerTrainingProfile:
    defaults = QhScorerTrainingProfile(
        name=str(payload.get("name", "checkpoint")),
        epochs=int(payload.get("epochs", 1)),
        batch_size=int(payload.get("batch_size", 512)),
        learning_rate=float(payload.get("learning_rate", 1.0e-4)),
        hidden_sizes=tuple(int(value) for value in payload.get("hidden_sizes", (256, 128, 64))),  # type: ignore[arg-type]
        max_training_samples=payload.get("max_training_samples"),  # type: ignore[arg-type]
        max_validation_samples=payload.get("max_validation_samples"),  # type: ignore[arg-type]
    )
    accepted = {field.name for field in fields(QhScorerTrainingProfile)}
    overrides = {}
    for key, value in payload.items():
        if key in accepted:
            overrides[key] = tuple(value) if key == "hidden_sizes" else value
    return QhScorerTrainingProfile(**{**defaults.to_json(), **overrides})  # type: ignore[arg-type]


def _normalization_from_checkpoint(payload: Mapping[str, object]) -> QhScorerNormalization:
    return QhScorerNormalization(
        schema_id=str(payload.get("schema_id", "phase45_v3_qh_scorer_normalization_v1")),
        context_mean=tuple(float(value) for value in payload["context_mean"]),  # type: ignore[index]
        context_std=tuple(float(value) for value in payload["context_std"]),  # type: ignore[index]
        candidate_mean=tuple(float(value) for value in payload["candidate_mean"]),  # type: ignore[index]
        candidate_std=tuple(float(value) for value in payload["candidate_std"]),  # type: ignore[index]
        q_value_mean=float(payload["q_value_mean"]),
        q_value_std=float(payload["q_value_std"]),
        fitted_on_data_role=str(payload.get("fitted_on_data_role", "training")),
    )


def _summary(rows: Sequence[Mapping[str, object]]) -> Mapping[str, object]:
    regrets = [float(row["regret_q_h"]) for row in rows]
    return {
        "count": len(regrets),
        "mean_regret_q_h": round(_mean(regrets), 6),
        "p50_regret_q_h": round(_quantile(regrets, 0.50), 6),
        "p95_regret_q_h": round(_quantile(regrets, 0.95), 6),
        "max_regret_q_h": round(max(regrets) if regrets else 0.0, 6),
        "regret_gt_0_5_rate": round(_ratio(sum(1 for value in regrets if value > 0.5), len(regrets)), 6),
        "regret_gt_1_0_rate": round(_ratio(sum(1 for value in regrets if value > 1.0), len(regrets)), 6),
        "regret_gt_2_0_rate": round(_ratio(sum(1 for value in regrets if value > 2.0), len(regrets)), 6),
    }


def _summaries_by(rows: Sequence[Mapping[str, object]], key: str) -> Mapping[str, object]:
    grouped: dict[str, list[Mapping[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key))].append(row)
    return {name: _summary(group) for name, group in sorted(grouped.items())}


def _count_by(rows: Sequence[Mapping[str, object]], key: str) -> Mapping[str, int]:
    return dict(sorted(Counter(str(row.get(key)) for row in rows).items()))


def _confusion(rows: Sequence[Mapping[str, object]]) -> Mapping[str, Mapping[str, int]]:
    matrix: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        matrix[str(row["target_action"])][str(row["predicted_action"])] += 1
    return {target: dict(sorted(values.items())) for target, values in sorted(matrix.items())}


def _metadata_value(metadata: object, key: str) -> object:
    if isinstance(metadata, Mapping):
        return metadata.get(key)
    return None


def _float_or_none(value: object) -> float | None:
    try:
        return None if value is None else float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def _bucket_buffer(value: object) -> str:
    if value is None:
        return "unknown"
    number = float(value)
    if number < 4.0:
        return "00_04s"
    if number < 8.0:
        return "04_08s"
    if number < 16.0:
        return "08_16s"
    if number < 32.0:
        return "16_32s"
    return "32s_plus"


def _bucket_bitrate(value: object) -> str:
    if value is None:
        return "unknown"
    kbps = float(value) / 1000.0
    if kbps <= 0.0:
        return "startup"
    if kbps <= 750.0:
        return "low"
    if kbps <= 1850.0:
        return "mid"
    if kbps <= 2850.0:
        return "high"
    return "top"


def _bucket_regret(value: object) -> str:
    number = float(value)
    if number <= 0.0:
        return "0"
    if number <= 0.5:
        return "0_0.5"
    if number <= 1.0:
        return "0.5_1.0"
    if number <= 2.0:
        return "1.0_2.0"
    return "2.0_plus"


def _mean(values: Sequence[float]) -> float:
    return sum(values) / float(len(values)) if values else 0.0


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _quantile(values: Sequence[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(max(int(round(float(q) * (len(ordered) - 1))), 0), len(ordered) - 1)
    return ordered[index]


def _print_compact(report: Mapping[str, object]) -> None:
    overall = report["overall"]  # type: ignore[index]
    print(
        "phase45_v3_qh_scorer_error_analysis status={status} samples={sample_count} "
        "mean_regret={mean_regret_q_h} p95={p95_regret_q_h} "
        "gt0_5={regret_gt_0_5_rate} gt1_0={regret_gt_1_0_rate} gt2_0={regret_gt_2_0_rate} "
        "output={output}".format(
            status=report["status"],
            sample_count=report["sample_count"],
            mean_regret_q_h=overall["mean_regret_q_h"],
            p95_regret_q_h=overall["p95_regret_q_h"],
            regret_gt_0_5_rate=overall["regret_gt_0_5_rate"],
            regret_gt_1_0_rate=overall["regret_gt_1_0_rate"],
            regret_gt_2_0_rate=overall["regret_gt_2_0_rate"],
            output=report.get("output_json", report.get("model_path")),
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
