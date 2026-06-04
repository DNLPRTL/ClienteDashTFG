# Phase 6A0 Open Gaps For Phase 6B/C

Status: Phase 6B hardening items are closed by readiness/audit code. Phase 6C dataset materialization items remain open.

## Hardening Gaps

| Gap | Why it matters | Future action |
| --- | --- | --- |
| `canonical_content_fingerprint` audit support | Phase 6 must block overlap by `trace_id`, `leakage_group`, `checksum_sha256` and canonical content identity | Closed in Phase 6B by hardening `scripts/audit_phase6_trace_eligibility.py` |
| Current audit script scope | The previous script checked `checksum_sha256`, `trace_id` and `leakage_group`, but did not explicitly parse `canonical_content_fingerprint` | Closed in Phase 6B; checksum and fingerprint are now parsed, reported and blocked separately |
| Ghent duplicate materialization | `logs_all` plus per-mobility folders can duplicate traces | Before split, use one source path or deduplicate by checksum/fingerprint |
| Dataset access/license/format | Candidate datasets cannot be evaluated until local-only inspection is complete | Create conversion specs and manifest checks outside Git |
| Lancaster missing source note/card | Lancaster is intended for Phase 6C discussion, but no source card was included in the current wave pack | Do not authorize Lancaster until a source note/card exists |
| ABRBench source/dataset boundary | SABR mentions ABRBench, but ABRBench itself is not materialized or licensed in this block | Treat as deferred until dataset card/access/license/format checks |
| VMAF/P.1203/MOS artifacts | Perceptual claims need media/perceptual artifacts and a metric decision | Keep deferred until artifact-dependent protocol exists |
| Statistical comparison plan | No final ranking/winner can exist without a planned comparison method | Draft Phase 6A2 statistical comparison before benchmark authorization |
| Evidence ZIP procedure | Future run artifacts need a strict external package contract | Use `ubuntu_evidence_package_spec.md` before any execution |

## Protocol Gaps Closed By Phase 6A2

- Controller matrix is frozen in `controller_matrix.md`.
- Trace group policy is frozen in `trace_selection_policy.md`.
- Media profile policy is frozen in `media_profile_decision.md`.
- Metrics and gate semantics are frozen in `metrics_schema.md`.
- Statistical comparison policy is frozen in `statistical_comparison.md`.
- Results table and figure plan is frozen in `results_tables_plan.md`.

## Remaining Readiness Gaps

- Final trace IDs remain open until `phase6_trace_manifest_final.json` exists after Phase 6C materialization and eligibility audit.
- HSDPA/Ghent materialization still requires local-only access/license/format checks.
- OOD materialization still requires Raca 4G, Raca 5G and Lumos5G access/license/format checks.
- Lancaster remains unauthorized for primary final evaluation until a source card/source note exists and eligibility audit proves no overlap.
- Evidence package wiring remains future technical readiness work.

## Phase 6B Closure Notes

- `scripts/validate_phase6_trace_manifest.py` validates `phase6_trace_manifest_v1` manifests without running benchmark code.
- `scripts/check_phase6_evaluation_readiness.py` reports structural readiness for Phase 6C and always keeps `ready_for_benchmark=false` and `benchmark_authorized=false`.
- `scripts/audit_phase6_trace_eligibility.py` now blocks Phase 6 evaluation overlap with Phase 4 by `canonical_content_fingerprint` in addition to checksum, trace ID and leakage group.
- Ghent duplicate grouping now prefers canonical content fingerprint when present and falls back to checksum.

## Non-Action In This Block

This block intentionally does not:

- implement benchmark code;
- run benchmark commands;
- generate plots;
- create rankings;
- declare a winner;
- claim QoE improvement.
