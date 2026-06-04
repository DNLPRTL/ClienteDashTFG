# Phase 4G memory and defense summary

## Main thesis contribution from Phase 4

Phase 4 contributes a complete IA/ML ABR pipeline for DashClientModular4:

- scientific literature triage;
- method decision;
- state/action/reward contracts;
- external trace handling;
- teacher-based imitation learning;
- CPU-first training;
- offline validation;
- candidate readiness gates;
- model export;
- deterministic CPU inference smoke;
- explicit limitations.

## Why it is academically defensible

The work is defensible because it follows a traceable chain:

```text
paper evidence -> design decision -> contract -> implementation -> test -> limitation
```

The model is not presented as magic or SOTA. It is presented as a controlled, reproducible learned ABR candidate derived from evidence.

## Paper-to-design traceability

- Pensieve: neural ABR state/action/reward framing.
- Comyco: imitation learning from expert policies.
- SABR: behavior cloning / pretraining before RL fine-tuning.
- CausalSim: block contaminated dry-run logs as training data.
- Fugu/Puffer: keep claims humble; ML does not always beat simple ABR.
- Oboe: network regimes matter.
- Gelato/Plume: trace skew and rare conditions matter.
- ANT/BETA/MetaABR: OOD/generalization must be explicit.
- ABRL/Facebook/Ahaggar: learned scoring/guidance needs safety/fallback.
- SODA: non-IA ABR can be strong; smoothness and deployability matter.
- Surveys 2025/HAS review: taxonomy and state-of-the-art context.

## Defense points

A strong oral defense can say:

1. I did not choose PPO by fashion; I selected behavior cloning because it matched evidence, hardware and reproducibility.
2. I did not train on player dry-runs; I used external normalized traces to avoid causal contamination.
3. I separated offline training from runtime integration.
4. I validated action safety before attempting integration.
5. I exported a bundle with schemas, normalization, fallback and manifest.
6. I did not claim final superiority; comparative ranking is intentionally reserved for Phase 6.
7. The controller integration in Phase 5 will be hybrid and safe, not a raw neural black box.

## Figures and tables for the memory

Potential figures:

- Phase 4 pipeline diagram.
- NeuralABR-Lite candidate scorer architecture.
- Dataset/corpus split diagram.
- Bundle structure diagram.
- Safety/fallback future integration diagram.

Potential tables:

- Paper-to-decision matrix.
- Method feasibility matrix.
- Phase 4 acceptance gate table.
- Model/bundle artifact table.
- Limitations and mitigation table.
