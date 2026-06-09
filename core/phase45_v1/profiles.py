from __future__ import annotations

from dataclasses import dataclass


class Phase45ProfileError(ValueError):
    """Raised when a Phase 4-5 v1 dataset profile is invalid."""


@dataclass(frozen=True)
class DatasetProfile:
    name: str
    train_window_count: int
    validation_window_count: int
    oracle_horizon_segments: int
    oracle_beam_width: int
    future_horizon_segments: int
    max_windows_per_trace: int
    synthetic_max_fraction: float
    dataset_max_fraction: float
    semantics_max_fraction: float
    seed: str

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "train_window_count": self.train_window_count,
            "validation_window_count": self.validation_window_count,
            "oracle_horizon_segments": self.oracle_horizon_segments,
            "oracle_beam_width": self.oracle_beam_width,
            "future_horizon_segments": self.future_horizon_segments,
            "max_windows_per_trace": self.max_windows_per_trace,
            "synthetic_max_fraction": self.synthetic_max_fraction,
            "dataset_max_fraction": self.dataset_max_fraction,
            "semantics_max_fraction": self.semantics_max_fraction,
            "seed": self.seed,
        }


PROFILES: dict[str, DatasetProfile] = {
    "smoke": DatasetProfile(
        name="smoke",
        train_window_count=24,
        validation_window_count=8,
        oracle_horizon_segments=3,
        oracle_beam_width=4,
        future_horizon_segments=3,
        max_windows_per_trace=1,
        synthetic_max_fraction=0.15,
        dataset_max_fraction=0.50,
        semantics_max_fraction=0.70,
        seed="phase45_v1_smoke_dataset_seed",
    ),
    "pilot": DatasetProfile(
        name="pilot",
        train_window_count=512,
        validation_window_count=128,
        oracle_horizon_segments=4,
        oracle_beam_width=5,
        future_horizon_segments=4,
        max_windows_per_trace=3,
        synthetic_max_fraction=0.15,
        dataset_max_fraction=0.40,
        semantics_max_fraction=0.55,
        seed="phase45_v1_pilot_dataset_seed",
    ),
    "full_v1": DatasetProfile(
        name="full_v1",
        train_window_count=8192,
        validation_window_count=2048,
        oracle_horizon_segments=5,
        oracle_beam_width=6,
        future_horizon_segments=5,
        max_windows_per_trace=4,
        synthetic_max_fraction=0.15,
        dataset_max_fraction=0.35,
        semantics_max_fraction=0.50,
        seed="phase45_v1_full_dataset_seed",
    ),
}


def profile_by_name(name: str) -> DatasetProfile:
    key = str(name).strip()
    if key not in PROFILES:
        raise Phase45ProfileError("unknown Phase 4-5 v1 dataset profile: {0}".format(name))
    return PROFILES[key]
