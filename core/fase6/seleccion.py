from __future__ import annotations

import hashlib
import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Deque, Dict, Iterable, List, Mapping, Sequence

from core.fase6.catalogo import especificacion_preset


DATASET_ID_SINTETICO = "synthetic_controlled_network"
SEMANTICA_SINTETICA = "synthetic_available_bandwidth"


def cargar_manifest_trazas(path: str | Path) -> Dict[str, Any]:
    manifest_path = Path(path)
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("La raiz del manifest de trazas debe ser un mapping")
    traces = data.get("traces")
    if not isinstance(traces, list):
        raise ValueError("El manifest de trazas debe contener una lista traces")
    return data


def seleccionar_ventanas_trazas(manifest: Mapping[str, Any], preset: str, config: Mapping[str, Any]) -> List[Dict[str, Any]]:
    spec = especificacion_preset(preset)
    network_cfg = _mapping(config.get("network_replay"))
    experiment_cfg = _mapping(config.get("experiment"))
    window_duration_s = float(network_cfg.get("window_duration_s", 120.0))
    decision_interval_s = float(network_cfg.get("decision_interval_s", 4.0))
    min_mean_throughput_kbps = float(network_cfg.get("min_mean_throughput_kbps_for_formal", 0.0) or 0.0)
    min_max_throughput_kbps = float(network_cfg.get("min_max_throughput_kbps_for_formal", 0.0) or 0.0)
    seed = int(experiment_cfg.get("seed", 606))
    include_synthetic = bool(experiment_cfg.get("include_synthetic_diagnostic", True))

    traces = [item for item in manifest.get("traces", []) if isinstance(item, Mapping)]
    eval_candidates = [
        item
        for item in traces
        if item.get("split") == "eval"
        and item.get("usable_for_eval", True) is not False
        and float(item.get("duration_s", 0.0) or 0.0) >= window_duration_s
    ]

    real_candidates = [
        item
        for item in eval_candidates
        if not es_traza_sintetica(item)
        and _pasa_suelo_throughput_formal(
            item,
            min_mean_throughput_kbps=min_mean_throughput_kbps,
            min_max_throughput_kbps=min_max_throughput_kbps,
        )
    ]
    synthetic_candidates = [item for item in eval_candidates if es_traza_sintetica(item)]

    real_windows = _seleccion_balanceada(
        real_candidates,
        target_count=int(spec["real_windows"]),
        seed=seed,
        window_duration_s=window_duration_s,
        decision_interval_s=decision_interval_s,
        synthetic=False,
        path_rewrites=_reescrituras_rutas(config),
    )
    synthetic_windows: List[Dict[str, Any]] = []
    if include_synthetic:
        synthetic_windows = _seleccion_balanceada(
            synthetic_candidates,
            target_count=int(spec["synthetic_windows"]),
            seed=seed + 17,
            window_duration_s=window_duration_s,
            decision_interval_s=decision_interval_s,
            synthetic=True,
            path_rewrites=_reescrituras_rutas(config),
        )
    return real_windows + synthetic_windows


def es_traza_sintetica(trace: Mapping[str, Any]) -> bool:
    return (
        bool(trace.get("synthetic"))
        or trace.get("dataset_id") == DATASET_ID_SINTETICO
        or trace.get("semantics") == SEMANTICA_SINTETICA
    )


def _pasa_suelo_throughput_formal(
    trace: Mapping[str, Any],
    *,
    min_mean_throughput_kbps: float,
    min_max_throughput_kbps: float,
) -> bool:
    mean_kbps = float(trace.get("throughput_mean_kbps", 0.0) or 0.0)
    max_kbps = float(trace.get("throughput_max_kbps", 0.0) or 0.0)
    return mean_kbps >= min_mean_throughput_kbps and max_kbps >= min_max_throughput_kbps


def _seleccion_balanceada(
    candidates: Sequence[Mapping[str, Any]],
    *,
    target_count: int,
    seed: int,
    window_duration_s: float,
    decision_interval_s: float,
    synthetic: bool,
    path_rewrites: Sequence[Mapping[str, str]],
) -> List[Dict[str, Any]]:
    if target_count <= 0:
        return []
    if len(candidates) < target_count:
        raise ValueError(
            "No hay suficientes trazas {0} de eval para el preset: se necesitan {1}, hay {2}".format(
                "synthetic" if synthetic else "real",
                target_count,
                len(candidates),
            )
        )

    grouped: Dict[tuple[str, str, str, str], List[Mapping[str, Any]]] = defaultdict(list)
    for item in candidates:
        grouped[_clave_balanceo(item)].append(item)

    group_queues: List[Deque[Mapping[str, Any]]] = []
    for key in sorted(grouped):
        items = sorted(grouped[key], key=lambda item: _token_estable(seed, str(item.get("trace_id", ""))))
        group_queues.append(deque(items))

    selected: List[Mapping[str, Any]] = []
    while group_queues and len(selected) < target_count:
        next_round: List[Deque[Mapping[str, Any]]] = []
        for queue in group_queues:
            if len(selected) >= target_count:
                next_round.append(queue)
                continue
            if queue:
                selected.append(queue.popleft())
            if queue:
                next_round.append(queue)
        group_queues = next_round

    windows = []
    for index, item in enumerate(selected, start=1):
        window_start_s = _inicio_ventana_para_traza(
            item,
            seed=seed,
            window_duration_s=window_duration_s,
            decision_interval_s=decision_interval_s,
        )
        trace_id = str(item.get("trace_id", "trace_{0:04d}".format(index)))
        window_id = "{0}_{1:03d}_{2}".format("synthetic" if synthetic else "real", index, _hash_corto(trace_id))
        windows.append(
            {
                "trace_window_id": window_id,
                "trace_id": trace_id,
                "dataset_id": str(item.get("dataset_id", "")),
                "semantics": str(item.get("semantics", "")),
                "network_condition": str(item.get("network_condition", "")),
                "difficulty_bucket": bucket_dificultad(item),
                "synthetic": bool(synthetic),
                "synthetic_scenario": str(item.get("synthetic_scenario", "")),
                "source_split": str(item.get("split", "")),
                "leakage_group": str(item.get("leakage_group", "")),
                "normalized_trace_path": _reescribir_ruta(str(item.get("normalized_trace_path", "")), path_rewrites),
                "window_start_s": float(window_start_s),
                "window_duration_s": float(window_duration_s),
                "throughput_mean_kbps": float(item.get("throughput_mean_kbps", 0.0) or 0.0),
                "throughput_min_kbps": float(item.get("throughput_min_kbps", 0.0) or 0.0),
                "throughput_max_kbps": float(item.get("throughput_max_kbps", 0.0) or 0.0),
            }
        )
    return windows


def bucket_dificultad(trace: Mapping[str, Any]) -> str:
    mean_kbps = float(trace.get("throughput_mean_kbps", 0.0) or 0.0)
    min_kbps = float(trace.get("throughput_min_kbps", 0.0) or 0.0)
    max_kbps = float(trace.get("throughput_max_kbps", 0.0) or 0.0)
    variability = (max_kbps - min_kbps) / mean_kbps if mean_kbps > 0 else 0.0
    if mean_kbps < 1500:
        return "baja_capacidad"
    if mean_kbps < 5000:
        return "media_capacidad_variable" if variability >= 1.5 else "media_capacidad"
    if mean_kbps < 20000:
        return "alta_capacidad_variable" if variability >= 1.5 else "alta_capacidad"
    return "muy_alta_capacidad"


def _clave_balanceo(trace: Mapping[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(trace.get("dataset_id", "")),
        str(trace.get("semantics", "")),
        str(trace.get("network_condition", "")),
        bucket_dificultad(trace),
    )


def _inicio_ventana_para_traza(
    trace: Mapping[str, Any],
    *,
    seed: int,
    window_duration_s: float,
    decision_interval_s: float,
) -> float:
    duration_s = float(trace.get("duration_s", 0.0) or 0.0)
    max_start_s = max(0.0, duration_s - window_duration_s)
    step_s = max(0.001, float(decision_interval_s or 4.0))
    possible = int(max_start_s // step_s) + 1
    if possible <= 1:
        return 0.0
    offset = _entero_estable(seed, str(trace.get("trace_id", ""))) % possible
    return float(offset * step_s)


def _reescrituras_rutas(config: Mapping[str, Any]) -> Sequence[Mapping[str, str]]:
    paths = _mapping(config.get("paths"))
    raw = paths.get("trace_path_rewrites") or []
    if isinstance(raw, Mapping):
        return [raw]
    try:
        return [item for item in raw if isinstance(item, Mapping)]
    except TypeError:
        return []


def _reescribir_ruta(path: str, rewrites: Sequence[Mapping[str, str]]) -> str:
    for rewrite in rewrites:
        source = str(rewrite.get("from", ""))
        target = str(rewrite.get("to", ""))
        if source and path.startswith(source):
            return target + path[len(source):]
    return path


def _token_estable(seed: int, text: str) -> str:
    return hashlib.sha256("{0}:{1}".format(seed, text).encode("utf-8")).hexdigest()


def _entero_estable(seed: int, text: str) -> int:
    return int(_token_estable(seed, text), 16)


def _hash_corto(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:10]


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}
