# Neural methods crosswalk

Phase: Phase 4A1 final  
Marker: NEURALABR_LITE_HYPOTHESIS

| candidate_method | supporting_sources | main advantage | main risk | CPU-first feasibility | data feasibility | DashClientModular4 fit | A1 decision |
|---|---|---|---|---|---|---|---|
| Candidate-scoring imitation learning | Comyco, SABR, ABRL/Facebook, AIRL, Fortuna action masking | Efficient, small, explainable, valid for variable MPD ladders | Teacher bias and future-label leakage | High | Medium | High | Preferred hypothesis |
| Fugu-lite predictor + policy | Fugu/Puffer | Interpretable predictor; conservative control | Needs predictor uncertainty and chunk-size contract | High | Medium | Medium/High | Alternative candidate |
| Guidance + classical safety layer | Ahaggar, ABRL/Facebook, SODA | Safer than opaque RL; easier fallback | Hybrid design complexity | High | Medium | High | Strong design pattern |
| BC + tiny PPO fine-tune | SABR | Modern and potentially stronger than pure BC | Reward hacking, variance, extra dependencies | Medium | Medium | Medium | Optional extension only |
| Direct PPO/A2C/A3C | Pensieve, NMoEABR, AIRL, SABR | End-to-end policy optimization | Cost, instability, reward hacking | Low/Medium | Medium | Medium | Not base |
| Full meta-RL | A2BR, MERINA, MetaABR, EAStream, NMoEABR | Generalization/adaptation | Too complex for TFG CPU-first | Low | High | Medium | Not base |
| Offline RL full | Fortuna | Uses offline data, reduces online interaction | Needs logged policy/offline dataset; OOD risk | Low | Low/Medium | Medium | Not base |
| Multi-model condition-wise DRL | ANT, BETA | Specializes by regime/difficult traces | Multiple models and detector errors | Low/Medium | Medium/High | Medium | Inspiration only |
| MoE / preference-aware ABR | NMoEABR | Frontier generalization and preferences | Too complex, preference data absent | Low | Low | Low/Medium | Future work |
| AIRL / learned reward | AIRL | Learns from demonstrations and reward structure | Conflicts with Phase 3.5 fixed reward | Low | Medium | Medium | Not base |
| SODA-like non-IA | SODA | Strong deployability and smoothness | Not IA controller | High | High | Medium | Comparator/defense |
