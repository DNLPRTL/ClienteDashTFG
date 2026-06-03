# Source Card: CausalSim

## Identity

- Source ID: `2023_alomar_causalsim_unbiased_trace_driven_simulation`
- Title: CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation
- Authors: Abdullah Alomar, Pouya Hamadanian, Arash Nasr-Esfahany, Anish Agarwal, Mohammad Alizadeh, Devavrat Shah
- Year/venue: 2023, USENIX NSDI
- Intake origin: `wave1_mandatory_methodology/2023_alomar_causalsim_unbiased_trace_driven_simulation.md`
- Phase 6A0 triage: `ACCEPTED_MANDATORY_METHODOLOGY`

## Why It Matters

CausalSim is the critical source for the trace-driven validity boundary. It explains that trace-driven simulation assumes the simulated controller does not change the trace itself. In ABR, achieved throughput can be affected by bitrate and chunk-size decisions made during trace collection.

## Phase 6 Protocol Transfers

- Document the exogenous-trace assumption.
- Classify trace origin and eligibility before evaluation.
- Block Phase 6 overlap with Phase 4 by `trace_id`, `leakage_group` and `checksum_sha256`.
- Require `canonical_content_fingerprint` in future manifests when available.
- Keep Phase 4E2 as diagnostic history, not strong generalization evidence.

## What Does Not Transfer

- No CausalSim implementation.
- No RCT requirement.
- No rejection of all public traces.
- No ranking without eligibility audit.

## Current Decision

Use as the primary source for trace-driven bias, leakage and threat-to-validity wording.
