# Phase 4E.1 open limitations

## Data scope

- The run uses the 15-trace Phase 3 conversion-smoke subset, not a final external trace corpus.
- Source licenses/provenance remain inherited from the Phase 3 manifest and dataset-card work.
- The split is deterministic and suitable for smoke validation, not a final scientific split.

## Model scope

- The trained checkpoint is diagnostic-only.
- The highest representation remains dominant in predictions.
- CPU inference latency was not measured.
- No export/inference contract was exercised.
- No fallback runtime integration was implemented.

## Validation scope

- Validation is offline sanity validation only.
- OOD diagnostic is a smoke stress check, not a real-world generalization claim.
- No formal controller comparison or ranking was run.
- No superiority over BBA, BOLA, MPC or robustMPC is claimed.

## Integration scope

- Phase 4F remains blocked.
- No client integration is allowed from this result.
- No media/player/runtime/controller code was touched.

## Next work

- Expand external trace coverage beyond the 15-trace smoke subset.
- Review and potentially strengthen the split policy for a larger corpus.
- Add CPU inference latency measurement in a later gate.
- Decide separately whether a later candidate is ready for Phase 4F export.
