# Source Card: Into The Wild / ABR-Arena

## Identity

- Source ID: `2025_hoffman_into_the_wild_abr_arena`
- Title: Into the Wild: Real-World Testing for ML-Based ABR
- Authors: Benjamin Hoffman, Alexander Dietmuller, Ayush Mishra, Laurent Vanbever
- Year/venue: 2025, PACMI
- Intake origin: `wave1_mandatory_methodology/2025_hoffman_into_the_wild_abr_arena.md`
- Phase 6A0 triage: `ACCEPTED_MANDATORY_METHODOLOGY`

## Why It Matters

This source draws the line between reproducible trace-driven validation and real-world global deployment evidence. It is especially relevant for ML-based ABR, where simulation or one deployment context may not generalize.

## Phase 6 Protocol Transfers

- Add an explicit sim-to-real threat.
- Separate test/OOD evidence from real-world user deployment.
- Do not claim global generalization for `neural_abr_lite`.
- Keep VM/content/demo use separate from benchmark networking.

## What Does Not Transfer

- No ABR-Arena implementation.
- No cloud or MTurk requirement.
- No abandonment of the Python trace-driven path.

## Current Decision

Use as claims-discipline and real-world-gap evidence.
