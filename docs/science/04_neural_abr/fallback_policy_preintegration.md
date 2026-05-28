# Fallback policy pre-integration contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This document defines the intended safety behavior before any integration code is written.

## Fallback principle

The neural model is advisory and bounded by ABR safety rules. It must never make the client unable to select a valid representation.

## Fallback triggers

A future integration must bypass the neural decision if:

```text
model file missing
model version incompatible
normalization manifest missing
input feature build fails
NaN or infinite score appears
all candidates are masked invalid
selected action is invalid
confidence/sanity gate fails, if implemented
runtime exception occurs
```

## Fallback priority

The preferred fallback chain is:

```text
1. robust_mpc, if its required state is available;
2. mpc or rate_based, if robust_mpc is unavailable;
3. bba or min_rate as conservative emergency fallback.
```

The exact implementation mapping is deferred to Phase 5 integration specs.

## No silent failure

Fallback activation must be visible in telemetry/reporting once integration exists.

Candidate future fields:

```text
neural_abr_used
neural_abr_fallback_reason
neural_abr_model_version
neural_abr_selected_representation
neural_abr_raw_score_gap
```

These fields are future integration ideas, not Phase 4B code changes.

## Phase 4B decision

A classical fallback is mandatory. NeuralABR-Lite is not allowed to be a single point of failure.
