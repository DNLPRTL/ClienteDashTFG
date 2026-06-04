# Phase 4 neural ABR risk register

Phase: Phase 4A1 final
Marker: NEURALABR_LITE_HYPOTHESIS

| risk_id | risk | source evidence | impact | mitigation | gate |
|---|---|---|---|---|---|
| R1 | Trace leakage / biased replay | CausalSim | Invalid training/evaluation | external traces + split contract + no dry-runs legacy | BLOCK |
| R2 | Future information leakage | Comyco, SABR, AIRL, BETA | Invalid model | future/oracle only in labels, never in inputs | BLOCK |
| R3 | Reward hacking | Pensieve, SABR, AIRL, PPO family | High reward with bad behavior | Phase 3.5 reward contract + behavior sanity checks | BLOCK |
| R4 | OOD failure | MetaABR, Into the Wild, BETA, EAStream, SABR | False generalization claim | stratified validation + OOD diagnostic-only | BLOCK for claims |
| R5 | CPU/training infeasibility | Meta-RL, Fortuna, NMoEABR, Gelato | Unreproducible TFG | small model CPU-first; no heavy RL base | BLOCK |
| R6 | IA loses vs BBA/MPC | Puffer/Fugu, SODA | Negative result | document honestly; do not promise IA win | ALLOW |
| R7 | Variable MPD ladder invalid output | ABRL/Facebook, Fortuna, AIRL | Action outside available reps | candidate scoring + action mask | BLOCK |
| R8 | Dataset skew/heavy tails | Plume/Gelato, Fortuna, SABR | Poor tail behavior | trace-regime balancing and OOD split | BLOCK for claims |
| R9 | Under-generalization on difficult traces | BETA, ANT | Average QoE hides failures | difficult-trace diagnostics | BLOCK for claims |
| R10 | Learned reward conflicts with Phase 3.5 | AIRL | Methodological inconsistency | do not learn reward in base | BLOCK |
| R11 | Preference-aware objective absent | NMoEABR, Ahaggar | Scope creep | no user-preference reward in Phase 4 | BLOCK |
| R12 | Real-world overclaim | Puffer/Fugu, Into the Wild, ABRL/Facebook | Invalid defense | call results trace-driven/offline only | BLOCK |
