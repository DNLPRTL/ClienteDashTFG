# Phase 5 remaining roadmap

## Phase 5C: implementation prompt/spec finalization

Status after Phase 5C: documentation/specification finalized. The Phase 5D prompt, file plan, runtime feature spec, bundle loading spec, telemetry hook decision and test plan are ready for review.

## Phase 5D: controller implementation

Status after Phase 5D: guarded scorer controller implemented and registered as `neural_abr_lite`, with CPU-only local bundle loading, action mask, safety guard, fallback chain, diagnostic telemetry, and fake-engine structural tests. This remains diagnostic-only and not benchmark evidence.

## Phase 5E: structural smoke

Status after Phase 5E documentation: structural smoke gates, fake-engine real-bundle runbook, artifact inspection checklist and optional Ubuntu/GStreamer runbook are prepared. Synthetic temporary-bundle smoke remains covered by tests. Real local Phase 4F bundle and Ubuntu/GStreamer smoke require user-provided bundle/MPD paths and remain structural-only, not benchmark evidence.

## Phase 5F: fallback/error/telemetry hardening

After Phase 5E smoke acceptance, exercise missing bundle, invalid manifest, schema mismatch, non-finite output, masked action, safety rejection, timeout and runtime exception paths.

## Phase 5G: closure and handoff to Phase 6

Close Phase 5 only after structural integration is stable and no benchmark claims have been made.

## Phase 6: formal comparative validation

Define evaluation traces, baselines, metrics, statistical handling and reporting rules before any ranking, winner or improvement claim.
