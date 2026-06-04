# Defendibility and acceptance gates

## What “defensible” means here

A defensible Phase 4 result is not the same as a SOTA claim and not the same as proven real-world superiority.

For this TFG, defensible means:

```text
scientifically motivated by the literature;
method chosen by evidence, not fashion;
state/action/reward contracts closed;
training data not contaminated;
no future leakage;
CPU-first and reproducible;
offline validation honest;
limitations explicit;
integration gated by safety/fallback.
```

## Gate C — Environment defensibility

Phase 4C passes if:

```text
replay environment is specified;
trace format is specified;
teacher label generation is specified;
leakage audit is specified;
artifacts layout is outside repo;
no code/client changes are made.
```

This proves the design is implementable cleanly, not that the model works yet.

## Gate D — Pipeline defensibility

Phase 4D passes if future code can:

```text
load/convert traces;
construct action masks;
generate teacher labels;
produce samples;
validate manifests;
fit normalization on train only;
pass unit/smoke tests;
keep artifacts outside repo.
```

This proves the pipeline works, not that the model is good yet.

## Gate E — Model defensibility

Phase 4E is the first point where we know whether we have a defensible trained candidate.

Required for `OFFLINE_CANDIDATE`:

```text
1. Reproducible run from manifest.
2. 100% valid actions.
3. 0 NaN/Inf outputs.
4. No leakage audit failures.
5. No trivial collapse to min/max/fixed.
6. Validation sanity reward above random/pathological baselines.
7. CPU inference latency within budget.
8. OOD diagnostic reported, even if poor.
9. Model card documents failures honestly.
```

If these fail, the result may still be an academically valid negative result, but the model is not accepted for integration.

## Gate F — Integration readiness

Phase 4F passes if the model bundle is exportable and inferable with:

```text
feature schema;
normalization stats;
action mask;
fallback policy;
model card;
export manifest;
latency check;
compatibility note for DashClientModular4.
```

## Gate G — Unequivocal go/no-go

Only Phase 4G can mark:

```text
ACCEPTED_FOR_PHASE5_INTEGRATION
```

This requires passing Gates C, D, E and F.

If Phase 4G marks:

```text
DIAGNOSTIC_ONLY_NOT_FOR_INTEGRATION
```

then the model can be discussed in the thesis but must not be integrated as an active client controller.

## Negative but still strong outcome

If NeuralABR-Lite loses to BBA/MPC or fails OOD, the TFG can still be strong if it proves:

```text
why it failed;
which assumptions broke;
how leakage was avoided;
why simple ABR remains competitive;
what would be needed for improvement.
```
