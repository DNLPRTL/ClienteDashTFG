from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable, Mapping

from core.phase45_v1.constants import NORMALIZATION_SCHEMA_ID, TRAINING_ROLE


@dataclass(frozen=True)
class NumericStats:
    count: int
    mean: float
    std: float
    minimum: float
    maximum: float

    def to_json(self) -> dict[str, object]:
        return {
            "count": self.count,
            "mean": round(self.mean, 9),
            "std": round(self.std, 9),
            "min": round(self.minimum, 9),
            "max": round(self.maximum, 9),
        }


def build_train_only_normalization(samples: Iterable[Mapping[str, object]]) -> Mapping[str, object]:
    values: dict[str, list[float]] = defaultdict(list)
    for sample in samples:
        role = str(sample.get("data_role", ""))
        if role != TRAINING_ROLE:
            continue
        model_inputs = sample.get("model_inputs")
        if not isinstance(model_inputs, Mapping):
            continue
        _collect_model_input_values(model_inputs, values)
    stats = {name: _numeric_stats(items).to_json() for name, items in sorted(values.items()) if items}
    return {
        "schema_id": NORMALIZATION_SCHEMA_ID,
        "fitted_on_data_role": TRAINING_ROLE,
        "metadata_fields_used": False,
        "target_fields_used": False,
        "stat_count": len(stats),
        "stats": stats,
    }


def _collect_model_input_values(model_inputs: Mapping[str, object], values: dict[str, list[float]]) -> None:
    context = model_inputs.get("context")
    if isinstance(context, Mapping):
        _collect_mapping_values("context", context, values)
    candidates = model_inputs.get("candidates")
    if isinstance(candidates, list):
        for candidate in candidates:
            if isinstance(candidate, Mapping):
                _collect_mapping_values("candidate", candidate, values)
    action_mask = model_inputs.get("action_mask")
    if isinstance(action_mask, list):
        for index, item in enumerate(action_mask):
            _add_numeric(values, "action_mask_{0}".format(index), item)


def _collect_mapping_values(prefix: str, mapping: Mapping[str, object], values: dict[str, list[float]]) -> None:
    for key, raw_value in mapping.items():
        name = "{0}.{1}".format(prefix, key)
        if isinstance(raw_value, (list, tuple)):
            for index, item in enumerate(raw_value):
                _add_numeric(values, "{0}_{1}".format(name, index), item)
        else:
            _add_numeric(values, name, raw_value)


def _add_numeric(values: dict[str, list[float]], name: str, raw_value: object) -> None:
    if isinstance(raw_value, bool):
        values[name].append(1.0 if raw_value else 0.0)
        return
    try:
        value = float(raw_value)
    except (TypeError, ValueError):
        return
    if math.isfinite(value):
        values[name].append(value)


def _numeric_stats(values: list[float]) -> NumericStats:
    count = len(values)
    mean = sum(values) / float(count)
    variance = sum((value - mean) ** 2 for value in values) / float(count)
    return NumericStats(
        count=count,
        mean=float(mean),
        std=math.sqrt(max(variance, 0.0)),
        minimum=min(values),
        maximum=max(values),
    )
