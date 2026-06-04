# Phase 4E open limitations

## Tier 0 Scope

This run is Tier 0 synthetic smoke only. It proves that the machinery runs, not that the learned policy is useful on external traces.

## Data Limitations

- No external traces were used.
- No public-trace provenance was documented for this run.
- No real DASH media or segment files were used.
- Legacy dry-runs remain forbidden and were not used.

## Model Limitations

- The model showed fixed representation-3 predictions on train, validation and OOD diagnostic splits.
- No CPU inference latency budget was measured in this phase.
- No export artifact was produced.
- No fallback runtime path was integrated.

## Validation Limitations

- Validation was offline sanity validation only.
- OOD was synthetic diagnostic OOD, not real network OOD.
- No formal benchmark or ranking was run.
- No superiority over classical controllers is claimed.

## Integration Limitations

- No player, runtime, downloader, media engine, parser, or controller registry code was touched.
- Client integration remains blocked.
- `PHASE4E_OFFLINE_CANDIDATE_READY_FOR_PHASE4F` was not granted.

## Required Next Work

- Prepare documented external traces outside the repository.
- Build trace-level train/validation/OOD manifests.
- Repeat dataset build, validation, train-only normalization, training and offline validation.
- Require non-pathological prediction behavior before considering Phase 4F export work.
