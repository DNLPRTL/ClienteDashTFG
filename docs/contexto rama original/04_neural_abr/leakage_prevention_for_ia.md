# Leakage prevention for IA

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Purpose

This document defines blocking rules against invalid ML claims.

## Leakage classes

### L1 — future-information leakage

Using information unavailable at the current ABR decision.

Examples:

```text
future throughput
future download time
future rebuffer
future reward
future chosen action
future segment outcomes
```

Gate:

```text
BLOCK training and validation until removed.
```

### L2 — split leakage

The same trace, transformed trace or derived samples appear in multiple splits.

Gate:

```text
BLOCK training and validation until trace-level disjoint split is restored.
```

### L3 — normalization leakage

Normalization statistics include validation/OOD/test traces.

Gate:

```text
BLOCK training and validation until train-only normalization is restored.
```

### L4 — teacher leakage

A teacher uses future information and the future-derived values leak into model inputs rather than labels only.

Gate:

```text
BLOCK training. Oracle-derived inputs are forbidden.
```

### L5 — legacy artifact leakage

Training uses DashClientModular4 dry-runs, smokes, benchmark artifacts or controller outputs as if they were neutral network traces.

Gate:

```text
BLOCK training dataset creation.
```

## Teacher future rule

A teacher may be allowed to use future information only if it is explicitly marked as oracle/diagnostic and if the future information appears only in the label or diagnostic upper bound, never in the student input.

## Required future reports

A future implementation must create:

```text
leakage_audit_report.json
feature_availability_report.json
split_disjointness_report.json
normalization_scope_report.json
```

These reports are generated artifacts and stay outside the repo unless summarized in Markdown.

## Phase 4B decision

Leakage gates are blocking gates. Passing training smokes is irrelevant if leakage gates fail.
