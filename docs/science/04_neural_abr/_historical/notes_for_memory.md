# Phase 4 notes for memory

## Chapter 2 — State of the art

Use the source cards to structure the literature:

1. Classical ABR and DASH/HAS context.
2. RL neural ABR: Pensieve and descendants.
3. Imitation learning: Comyco, SABR, AIRL as evidence for expert trajectories.
4. Real-world caution: Fugu/Puffer, ABRL/Facebook, Into the Wild.
5. Generalization/OOD: Oboe, MetaABR, A2BR, MERINA, EAStream, ANT, BETA, NMoEABR.
6. Strong non-IA ABR: SODA.
7. Recent frontier: Fortuna, EAStream, NMoEABR, BETA, SABR.

## Chapter 4 — Design

The design rationale should state:

```text
NeuralABR-Lite is intentionally small, CPU-first and transparent.
It uses candidate scoring and action masking to stay compatible with MPD ladders.
It uses behavior cloning to avoid unstable PPO-first training.
It uses trace-regime balancing to reduce skew.
It uses fallback to keep integration safe.
```

## Chapter 6 — Evaluation

Use careful wording:

- "trace-driven validation";
- "offline validation";
- "OOD diagnostic";
- "no formal benchmark in Phase 4";
- "no real-world claim";
- "no SOTA claim".

## Defense points

- If IA loses to BBA/MPC, that is a valid result.
- If stable networks make IA irrelevant, say so.
- If PPO is not selected, justify via CPU-first, reproducibility and literature.
- If reward learning is not selected, justify via Phase 3.5 reward closure.
