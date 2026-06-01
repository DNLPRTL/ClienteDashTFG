# Phase 5B CPU inference contract

## Purpose

NeuralABR-Lite must remain CPU-first and deterministic for future controller integration.

## Required runtime behavior

- CPU-only inference.
- No GPU dependency.
- `model.eval()`.
- `torch.no_grad()`.
- Deterministic inference for identical inputs.
- Finite scores required.
- Action mask applied before selection.
- Latency measured per decision as diagnostic telemetry.
- Inference timeout triggers fallback.
- Non-finite output triggers fallback.

## Latency status

The future controller may record per-decision `neural_inference_ms`. A p95 target may be used as a diagnostic feasibility check, but it is not a production claim and not a controller benchmark.

## Failure behavior

Fallback is required for:

- PyTorch unavailable;
- model not loaded;
- schema mismatch;
- feature vector invalid;
- non-finite score;
- inference timeout;
- runtime exception.

## Boundary

CPU inference telemetry is diagnostic-only and not benchmark evidence.
