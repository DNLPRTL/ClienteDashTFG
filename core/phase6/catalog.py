from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Iterable, List, Mapping, Optional

from core.controller.registry import CONTROLLER_REGISTRY


DEFAULT_CONTROLLER_EXCLUDE = frozenset(
    {
        "min_rate",
        "fixed_rate",
        "max_rate",
        "fixed_quality",
        "scripted_quality",
        "max_quality",
    }
)

DEFAULT_CONTROLLER_ALIASES = {
    "rate_based": "base_rate_based",
    "bba": "base_bba",
    "bola": "base_bola",
    "mpc": "base_mpc",
    "robust_mpc": "base_robust_mpc",
    "neural_abr_lite_robust_mpc": "propio_rmp",
    "neural_abr_lite_teacher_hibrido": "propio_th",
    "spbc_abr_v2_dpo_anchor_safe_rank": "propio_spbc_v2_anchor",
    "phase45_v3_neural_throughput_calibrated_mpc_v1": "propio_neural_mpc_v1",
}

DEFAULT_CONTROLLER_HUMAN_NAMES = {
    "rate_based": "Rate Based",
    "bba": "BBA",
    "bola": "BOLA",
    "mpc": "MPC",
    "robust_mpc": "Robust MPC",
    "neural_abr_lite_robust_mpc": "Propio RMP",
    "neural_abr_lite_teacher_hibrido": "Propio TH",
    "spbc_abr_v2_dpo_anchor_safe_rank": "Propio SPBC v2 Anchor",
    "phase45_v3_neural_throughput_calibrated_mpc_v1": "Propio Neural-MPC v1",
}

MEDIA_PROFILES = {
    "preflight_paseo_1min_30fps_4s": {
        "media_profile_id": "preflight_paseo_1min_30fps_4s",
        "display_name": "Preflight Paseo 1 min 30 fps",
        "mpd_url": (
            "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/"
            "Paseo_Almunecar_1min_30fps_simple_4s.mpd"
        ),
        "segment_duration_s": 4.0,
        "duration_class": "1min",
        "diagnostic_only": True,
    },
    "paseo_10min_30fps_4s": {
        "media_profile_id": "paseo_10min_30fps_4s",
        "display_name": "Paseo Almunecar 10 min 30 fps",
        "mpd_url": (
            "http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/"
            "Paseo_Almunecar_10min_30fps_simple_4s.mpd"
        ),
        "segment_duration_s": 4.0,
        "duration_class": "10min",
        "diagnostic_only": False,
    },
    "blender_10min_30fps_4s": {
        "media_profile_id": "blender_10min_30fps_4s",
        "display_name": "Blender Sunflower 10 min 30 fps",
        "mpd_url": (
            "http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/"
            "Blender_Sunflower_10min_30fps_simple_4s.mpd"
        ),
        "segment_duration_s": 4.0,
        "duration_class": "10min",
        "diagnostic_only": False,
    },
    "paseo_10min_60fps_4s": {
        "media_profile_id": "paseo_10min_60fps_4s",
        "display_name": "Paseo Almunecar 10 min 60 fps",
        "mpd_url": (
            "http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/"
            "Paseo_Almunecar_10min_60fps_simple_4s.mpd"
        ),
        "segment_duration_s": 4.0,
        "duration_class": "10min",
        "diagnostic_only": False,
    },
    "blender_10min_60fps_4s": {
        "media_profile_id": "blender_10min_60fps_4s",
        "display_name": "Blender Sunflower 10 min 60 fps",
        "mpd_url": (
            "http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/"
            "Blender_Sunflower_10min_60fps_simple_4s.mpd"
        ),
        "segment_duration_s": 4.0,
        "duration_class": "10min",
        "diagnostic_only": False,
    },
}

PRESET_SPECS = {
    "diagnostico": {
        "preset": "diagnostico",
        "real_windows": 2,
        "synthetic_windows": 1,
        "media_profile_ids": ["paseo_10min_30fps_4s"],
        "benchmark_capable": False,
        "ranking_capable": False,
        "max_media_segments": 6,
        "network_window_duration_s": 90.0,
        "timeout_seconds": 240.0,
        "estimated_session_duration_s": 30.0,
    },
    "rapido": {
        "preset": "rapido",
        "real_windows": 8,
        "synthetic_windows": 2,
        "media_profile_ids": ["paseo_10min_30fps_4s"],
        "benchmark_capable": False,
        "ranking_capable": False,
        "max_media_segments": 30,
        "network_window_duration_s": 300.0,
        "timeout_seconds": 900.0,
        "estimated_session_duration_s": 125.0,
    },
    "equilibrado": {
        "preset": "equilibrado",
        "real_windows": 24,
        "synthetic_windows": 4,
        "media_profile_ids": ["paseo_10min_30fps_4s", "blender_10min_30fps_4s"],
        "benchmark_capable": True,
        "ranking_capable": True,
        "max_media_segments": 30,
        "network_window_duration_s": 300.0,
        "timeout_seconds": 900.0,
        "estimated_session_duration_s": 125.0,
    },
    "extendido": {
        "preset": "extendido",
        "real_windows": 48,
        "synthetic_windows": 8,
        "media_profile_ids": [
            "paseo_10min_30fps_4s",
            "blender_10min_30fps_4s",
            "paseo_10min_60fps_4s",
            "blender_10min_60fps_4s",
        ],
        "benchmark_capable": True,
        "ranking_capable": True,
        "max_media_segments": 30,
        "network_window_duration_s": 300.0,
        "timeout_seconds": 900.0,
        "estimated_session_duration_s": 125.0,
    },
}

PRESET_NAMES = tuple(PRESET_SPECS.keys())


def preset_spec(preset: str) -> Dict[str, Any]:
    try:
        return deepcopy(PRESET_SPECS[str(preset)])
    except KeyError as exc:
        raise ValueError("Unknown Phase 6 preset: {0}".format(preset)) from exc


def media_profiles_for_preset(preset: str, config: Optional[Mapping[str, Any]] = None) -> List[Dict[str, Any]]:
    config = config or {}
    media_overrides = _mapping(config.get("media_profiles"))
    spec = preset_spec(preset)
    configured_ids = _list_or_none((_mapping(config.get("experiment"))).get("media_profile_ids"))
    profile_ids = configured_ids or list(spec["media_profile_ids"])
    profiles = []
    for profile_id in profile_ids:
        if profile_id in media_overrides:
            raw_profile = dict(media_overrides[profile_id])
            raw_profile.setdefault("media_profile_id", profile_id)
        else:
            raw_profile = deepcopy(MEDIA_PROFILES[profile_id])
        profiles.append(raw_profile)
    return profiles


def discover_comparable_controllers(config: Optional[Mapping[str, Any]] = None) -> List[Dict[str, Any]]:
    config = config or {}
    experiment = _mapping(config.get("experiment"))
    aliases = dict(DEFAULT_CONTROLLER_ALIASES)
    aliases.update(_mapping(config.get("controller_aliases")))
    human_names = dict(DEFAULT_CONTROLLER_HUMAN_NAMES)
    human_names.update(_mapping(config.get("controller_display_names")))

    excluded = set(DEFAULT_CONTROLLER_EXCLUDE)
    excluded.update(str(item) for item in _list_or_empty(config.get("excluded_controllers")))
    configured = _list_or_none(experiment.get("controllers"))
    keys: Iterable[str] = configured or CONTROLLER_REGISTRY.keys()

    selected = []
    for key in keys:
        controller_key = str(key)
        if controller_key in excluded:
            continue
        if controller_key not in CONTROLLER_REGISTRY:
            raise ValueError("Unknown controller in Phase 6 config: {0}".format(controller_key))
        selected.append(
            {
                "controller_key": controller_key,
                "alias": str(aliases.get(controller_key, _safe_alias(controller_key))),
                "display_name": str(human_names.get(controller_key, controller_key.replace("_", " ").title())),
            }
        )
    return selected


def controller_params(config: Mapping[str, Any], controller_key: str) -> Dict[str, Any]:
    raw_params = _mapping(config.get("controller_params"))
    return dict(_mapping(raw_params.get(controller_key)))


def _safe_alias(key: str) -> str:
    allowed = []
    for char in str(key).lower():
        allowed.append(char if char.isalnum() else "_")
    alias = "".join(allowed).strip("_")
    return alias or "controller"


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _list_or_empty(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, (str, bytes)):
        return [value]
    try:
        return list(value)
    except TypeError:
        return [value]


def _list_or_none(value: Any) -> Optional[List[Any]]:
    items = _list_or_empty(value)
    return items or None
