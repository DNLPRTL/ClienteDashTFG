# Source note: ppo_abr_search_note

## Status

- No dedicated PPO-ABR PDF was uploaded in Package 3.
- PPO appears in several uploaded sources, especially SABR, NMoEABR and AIRL, but only as a component inside broader systems.
- This note must not be treated as a source card for a standalone PPO-ABR method.

## Decision

- PPO remains blocked as a default/base choice.
- PPO fine-tuning may be considered only after:
  - behavior cloning baseline is working;
  - training data contract is closed;
  - reward hacking tests exist;
  - CPU runtime remains feasible;
  - no validation/test leakage occurs.

## Use in memory

- Defense point: the TFG explicitly reviewed PPO-related evidence but did not choose PPO by inertia.
