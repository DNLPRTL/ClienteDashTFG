# Phase 4D next steps

## Step 1 — Generate implementation prompt

Generate a Codex prompt for offline pipeline only.

## Step 2 — Implement minimal schemas and tests

Start with trace schema, feature schema and action mask tests before replay or training.

## Step 3 — Implement deterministic replay smoke

Use tiny synthetic traces to verify transitions.

## Step 4 — Implement teacher label smoke

Generate teacher labels on synthetic traces only.

## Step 5 — Implement dataset builder smoke

Produce a tiny local-only dataset manifest outside the repo.

## Step 6 — Implement minimal model/training smoke

Only after dataset and leakage audit pass.

## Step 7 — Do not integrate client

Phase 4D must end with offline pipeline validation, not a neural controller in DashClientModular4.
