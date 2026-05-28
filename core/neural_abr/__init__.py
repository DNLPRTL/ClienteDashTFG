"""Offline NeuralABR-Lite training pipeline package.

This package is intentionally not a DashClientModular4 controller registry
entry. Phase 4D code is limited to offline dataset, training-smoke and sanity
validation artifacts.
"""

from __future__ import annotations

from core.neural_abr.constants import DATASET_SCHEMA_VERSION, K_CONTEXT

__all__ = ["DATASET_SCHEMA_VERSION", "K_CONTEXT"]
