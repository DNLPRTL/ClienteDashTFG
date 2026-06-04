# Phase 4D open limitations

Phase 4D is intentionally limited to offline pipeline correctness.

## Data limitations

- The implemented smoke dataset is synthetic and diagnostic-only.
- No public or externally documented trace corpus is selected in this phase.
- No real DASH media segments or large video artifacts are included.
- Legacy dry-runs remain forbidden as training data.

## Teacher limitations

- The robust MPC teacher is a compact offline labeler based on the existing project logic and Phase 4 contract, not a claim of optimality.
- The bounded oracle is not used for training.
- Teacher agreement is reported only as sanity information.

## Model limitations

- The model is a small behavior-cloning candidate scorer.
- It has not been exported for runtime inference.
- It has not been integrated into the controller registry.
- It has not been validated as a final ABR policy.

## Validation limitations

- The smoke reports action validity, teacher agreement, and OOD diagnostic behavior.
- It does not rank NeuralABR-Lite against BBA, MPC, robustMPC, or any other controller.
- It does not make real-world, SOTA, QoE superiority, or production readiness claims.

## Next blocked work

Later phases still need larger trace selection, stronger offline validation, export/inference checks, fallback integration design, and explicit acceptance before any Phase 5 client integration can be considered.
