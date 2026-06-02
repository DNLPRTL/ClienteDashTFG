# Phase 5 remaining roadmap

## Phase 5C: implementation prompt/spec finalization

Status after Phase 5C: documentation/specification finalized. The Phase 5D prompt, file plan, runtime feature spec, bundle loading spec, telemetry hook decision and test plan are ready for review.

## Phase 5D: controller implementation

Implement the guarded neural scorer controller and helper modules only after Phase 5C review and Ubuntu validation. Keep the implementation CPU-first, local-only, fail-closed and fallback-protected.

## Phase 5E: structural smoke

Run fake-engine structural smoke to verify bundle load/fail-closed behavior, feature building, action mask, safety guard, fallback and diagnostic telemetry. This is not a benchmark.

## Phase 5F: fallback/error/telemetry hardening

Exercise missing bundle, invalid manifest, schema mismatch, non-finite output, masked action, safety rejection, timeout and runtime exception paths.

## Phase 5G: closure and handoff to Phase 6

Close Phase 5 only after structural integration is stable and no benchmark claims have been made.

## Phase 6: formal comparative validation

Define evaluation traces, baselines, metrics, statistical handling and reporting rules before any ranking, winner or improvement claim.
