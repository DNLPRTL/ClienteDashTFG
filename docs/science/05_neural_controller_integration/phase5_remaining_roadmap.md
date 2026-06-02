# Phase 5 remaining roadmap

## Phase 5C: implementation prompt/spec finalization

Status after Phase 5C: documentation/specification finalized. The Phase 5D prompt, file plan, runtime feature spec, bundle loading spec, telemetry hook decision and test plan are ready for review.

## Phase 5D: controller implementation

Status after Phase 5D: guarded scorer controller implemented and registered as `neural_abr_lite`, with CPU-only local bundle loading, action mask, safety guard, fallback chain, diagnostic telemetry, and fake-engine structural tests. This remains diagnostic-only and not benchmark evidence.

## Phase 5E: structural smoke

Status after Phase 5E closure: `ACCEPTED_FOR_PHASE5F`.

User-reported Ubuntu fake-engine structural smokes were recorded for both no-bundle fallback and real-bundle execution, with run roots and artifacts kept outside the repository. Artifact inspection passed: canonical run files existed, legacy dataset outputs were absent, `segment_telemetry.csv` contained `feedback_neural_*` diagnostic fields, `evaluation_segments.csv` contained no neural diagnostic fields, `feedback_neural_diagnostic_only` was true/`1`, and no benchmark/ranking/improvement fields were reported.

Ubuntu/GStreamer remains optional pending unless a separate passed structural/demo run is provided. Fake/GStreamer smokes are diagnostic structural validation only, not benchmark evidence. No formal controller comparison was performed; Phase 6 remains the only phase for ranking/comparison.

## Phase 5F: fallback/error/telemetry hardening

Phase 5F may start after Phase 5E smoke acceptance. Exercise missing bundle, invalid manifest, schema mismatch, non-finite output, masked action, safety rejection, timeout and runtime exception paths.

## Phase 5G: closure and handoff to Phase 6

Close Phase 5 only after structural integration is stable and no benchmark claims have been made.

## Phase 6: formal comparative validation

Define evaluation traces, baselines, metrics, statistical handling and reporting rules before any ranking, winner or improvement claim.
