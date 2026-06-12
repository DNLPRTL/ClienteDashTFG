from __future__ import annotations

from dataclasses import dataclass


class Phase45V3ProfileError(ValueError):
    """Raised when a Phase 4-5 v3 dataset profile is invalid."""


@dataclass(frozen=True)
class Phase45V3DatasetProfile:
    name: str
    train_window_count: int
    validation_window_count: int
    qh_horizon_segments: int
    qh_beam_width: int
    max_windows_per_trace: int
    synthetic_max_fraction: float
    dataset_max_fraction: float
    semantics_max_fraction: float
    seed: str
    rollouts_per_window: int = 2

    @property
    def oracle_horizon_segments(self) -> int:
        return self.qh_horizon_segments

    @property
    def oracle_beam_width(self) -> int:
        return self.qh_beam_width

    @property
    def future_horizon_segments(self) -> int:
        return self.qh_horizon_segments

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "train_window_count": self.train_window_count,
            "validation_window_count": self.validation_window_count,
            "qh_horizon_segments": self.qh_horizon_segments,
            "qh_beam_width": self.qh_beam_width,
            "max_windows_per_trace": self.max_windows_per_trace,
            "synthetic_max_fraction": self.synthetic_max_fraction,
            "dataset_max_fraction": self.dataset_max_fraction,
            "semantics_max_fraction": self.semantics_max_fraction,
            "seed": self.seed,
            "rollouts_per_window": self.rollouts_per_window,
        }


PROFILES: dict[str, Phase45V3DatasetProfile] = {
    "smoke": Phase45V3DatasetProfile(
        name="smoke",
        train_window_count=12,
        validation_window_count=4,
        qh_horizon_segments=3,
        qh_beam_width=10,
        max_windows_per_trace=1,
        synthetic_max_fraction=0.15,
        dataset_max_fraction=0.50,
        semantics_max_fraction=0.70,
        seed="phase45_v3_smoke_qh_dataset_seed",
        rollouts_per_window=2,
    ),
    "pilot": Phase45V3DatasetProfile(
        name="pilot",
        train_window_count=256,
        validation_window_count=64,
        qh_horizon_segments=4,
        qh_beam_width=18,
        max_windows_per_trace=3,
        synthetic_max_fraction=0.15,
        dataset_max_fraction=0.40,
        semantics_max_fraction=0.55,
        seed="phase45_v3_pilot_qh_dataset_seed",
        rollouts_per_window=4,
    ),
    "full_v1": Phase45V3DatasetProfile(
        name="full_v1",
        train_window_count=4096,
        validation_window_count=1024,
        qh_horizon_segments=5,
        qh_beam_width=24,
        max_windows_per_trace=4,
        synthetic_max_fraction=0.15,
        dataset_max_fraction=0.35,
        semantics_max_fraction=0.50,
        seed="phase45_v3_full_qh_dataset_seed",
        rollouts_per_window=4,
    ),
}


def profile_by_name(name: str) -> Phase45V3DatasetProfile:
    key = str(name).strip()
    if key not in PROFILES:
        raise Phase45V3ProfileError("unknown Phase 4-5 v3 dataset profile: {0}".format(name))
    return PROFILES[key]
