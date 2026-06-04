# Phase 4F Defense Talking Points

- Phase 4F deliberately separates model export/inference from client integration.
- The bundle contains the model state, feature schema, train-only normalization, ladder schema, inference contract, fallback policy, model card, and manifest hashes.
- Action masking is enforced at inference so invalid MPD representation indices cannot be selected.
- CPU-only loading keeps the candidate compatible with the validated hardware boundary.
- The fallback policy is documented for future Phase 5 integration, but Phase 4F does not execute a client fallback path.
- The latency report is a safety feasibility check only, not a benchmark against ABR controllers.
- No benchmark/ranking, SOTA, or real-world validation claim is made.
- Phase 4G remains the gate that decides whether Phase 5 integration is allowed.
- Phase 4F-R1 fixed a cross-platform validation issue: Ubuntu failed because `no_repo_artifacts` was treated as a hard correctness failure in a temporary unit fixture.
- The repaired validator keeps correctness gates strict and moves repository hygiene to an explicit environmental gate. Use `--check-repo-hygiene` when that check must block.
- Real repo artifact hygiene remains enforced by explicit validation/commit checks; pure temporary fixtures report it as `NOT_CHECKED`.
- Phase 4G is allowed only after Windows and Ubuntu both pass the repaired validation commands.

Bundle dir: `C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_091652`
