# Phase 6 Statistical Comparison Plan

Status: final Phase 6A2 protocol decision. No statistical test is executed here.

## Statistical Unit

The statistical unit is the session/trace, not segment rows.

Segment rows are repeated observations within a session and must not be treated as independent samples for controller-level significance claims.

## Descriptive Reporting

For each controller and evaluation group, report:

- mean;
- median;
- standard deviation;
- IQR;
- p5;
- p25;
- p50;
- p75;
- p95;
- sample count;
- eligible/excluded counts.

## Confidence Intervals

Report bootstrap 95% confidence intervals over sessions/traces for `qoe_linear_mean` and important secondary metrics when sample size permits.

The bootstrap procedure and seed must be recorded in the future evidence package.

## Pairwise Comparisons

Use paired comparisons by `trace_id` when comparing controllers on the same trace/session.

Preferred tests:

- Wilcoxon signed-rank test if assumptions and sample size are acceptable.
- Paired permutation test as an alternative non-parametric paired comparison.

Apply Holm correction for multiple comparisons where relevant.

## Effect Size

Report effect size alongside p-values and confidence intervals. Acceptable effect-size forms include paired mean difference, paired median difference, rank-biserial correlation or another documented paired effect-size measure.

## Claim Discipline

- Do not declare a winner from small, noisy or underpowered samples.
- Do not overclaim if OOD coverage is limited.
- Do not claim `neural_abr_lite` improves QoE unless the frozen protocol, trace eligibility, statistical plan and evidence package support it.
- Report negative, mixed or inconclusive outcomes plainly.
