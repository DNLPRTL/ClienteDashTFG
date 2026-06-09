# SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning
**Archivo PDF:** `2509.10486v1.pdf`  
**Identificador:** `03_sabr_2025_bc_rl_finetuning`  
**Páginas:** 6  
**Foco para Fase 4-5 v1:** BC pretraining + RL fine-tuning; ABRBench-3G/4G+; OOD generalization.

> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.

## 1. Cómo usar este `.md`
- Leer primero las secciones 2-4 para ubicar método, datos y evaluación.
- Usar los extractos crudos por categoría como material base para diseño/contratos/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No tratar los resultados del paper como promesa directa para DashClientModular4; convertirlos en hipótesis/guardrails y verificar en Phase 6.

## 2. Índice de secciones detectadas
- p.1: I. INTRODUCTION
- p.2: II. RELATED WORKS
- p.2: III. PROPOSED SABR FRAMEWORK
- p.2: A. BC pretraining with DPO
- p.3: B. RL fine-tuning with PPO
- p.4: IV. PROPOSED BENCHMARKS
- p.4: V. IMPLEMENTATION DETAILS
- p.4: VI. EVALUATION
- p.4: A. Experimental setup
- p.5: B. Proposed SABR vs. existing baselines
- p.5: C. Evaluation on the OOD datasets
- p.5: VII. CONCLUSION
- p.6: C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Training language
- p.6: C. Finn, “Direct preference optimization: Your language model is
- p.6: W. Chen et al., “Lora: Low-rank adaptation of large language models.”
- p.6: D. Rybkin, Z. Yang, Z. M. Mao et al., “A variegated look at 5g in the
- p.6: 2021 ACM SIGCOMM 2021 Conference, 2021, pp. 610–625.
- p.6: T. Killeen, Z. Lin, N. Gimelshein, L. Antiga et al., “Pytorch: An

## 3. Índice de páginas con palabras clave
- p.1: action, QoE, dataset, trace, training, PPO, imitation, behavior cloning, latency, OOD, generalization
- p.2: state, action, reward, QoE, buffer, throughput, trace, training, baseline, PPO, imitation, behavior cloning, OOD, generalization
- p.3: state, action, reward, buffer, training, PPO, generalization
- p.4: state, action, reward, QoE, trace, training, baseline, PPO, OOD, generalization
- p.5: reward, QoE, rebuffer, buffer, dataset, trace, training, baseline, imitation, OOD, generalization
- p.6: action, reward, QoE, throughput, trace, training, baseline, PPO, imitation, generalization

## 4. Extracción técnica cruda por categorías

### 4.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Modelo / arquitectura / algoritmo | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Modelo / arquitectura / algoritmo | extracto 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t ̸= aw t 8: Append sample: B ←B ∪{(st, aw t , al t)} 9: Execute at in the ABR simulator to obtain next state st+1 10: end for 11: for 1, 2, . . . , Epretrain do 12: Sample mini-batch ˆB of size mpretrain from B 13: Update πθ using the DPO loss on ˆB (Eq. 2) 14: end for 15: end for 16: Output: Base model πθ B. RL fine-tuning with PPO Only BC training is constrained to the distribution of expert pol

**[Modelo / arquitectura / algoritmo | extracto 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Modelo / arquitectura / algoritmo | extracto 5 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Estado / inputs / features observables

**[Estado / inputs / features observables | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Estado / inputs / features observables | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Estado / inputs / features observables | extracto 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t ̸= aw t 8: Append sample: B ←B ∪{(st, aw t , al t)} 9: Execute at in the ABR simulator to obtain next state st+1 10: end for 11: for 1, 2, . . . , Epretrain do 12: Sample mini-batch ˆB of size mpretrain from B 13: Update πθ using the DPO loss on ˆB (Eq. 2) 14: end for 15: end for 16: Output: Base model πθ B. RL fine-tuning with PPO Only BC training is constrained to the distribution of expert pol

**[Estado / inputs / features observables | extracto 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Estado / inputs / features observables | extracto 5 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Acción / decisión ABR | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Acción / decisión ABR | extracto 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t ̸= aw t 8: Append sample: B ←B ∪{(st, aw t , al t)} 9: Execute at in the ABR simulator to obtain next state st+1 10: end for 11: for 1, 2, . . . , Epretrain do 12: Sample mini-batch ˆB of size mpretrain from B 13: Update πθ using the DPO loss on ˆB (Eq. 2) 14: end for 15: end for 16: Output: Base model πθ B. RL fine-tuning with PPO Only BC training is constrained to the distribution of expert pol

**[Acción / decisión ABR | extracto 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Acción / decisión ABR | extracto 5 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Reward / QoE / función objetivo

**[Reward / QoE / función objetivo | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Reward / QoE / función objetivo | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Reward / QoE / función objetivo | extracto 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t ̸= aw t 8: Append sample: B ←B ∪{(st, aw t , al t)} 9: Execute at in the ABR simulator to obtain next state st+1 10: end for 11: for 1, 2, . . . , Epretrain do 12: Sample mini-batch ˆB of size mpretrain from B 13: Update πθ using the DPO loss on ˆB (Eq. 2) 14: end for 15: end for 16: Output: Base model πθ B. RL fine-tuning with PPO Only BC training is constrained to the distribution of expert pol

**[Reward / QoE / función objetivo | extracto 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Reward / QoE / función objetivo | extracto 5 | p.5]**

We evaluate performance using the QoE metrics: QoE = N X n=1 q(Rn) −δ N−1 X n=1

**[Reward / QoE / función objetivo | extracto 6 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Entrenamiento / learning procedure

**[Entrenamiento / learning procedure | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Entrenamiento / learning procedure | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Entrenamiento / learning procedure | extracto 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t ̸= aw t 8: Append sample: B ←B ∪{(st, aw t , al t)} 9: Execute at in the ABR simulator to obtain next state st+1 10: end for 11: for 1, 2, . . . , Epretrain do 12: Sample mini-batch ˆB of size mpretrain from B 13: Update πθ using the DPO loss on ˆB (Eq. 2) 14: end for 15: end for 16: Output: Base model πθ B. RL fine-tuning with PPO Only BC training is constrained to the distribution of expert pol

**[Entrenamiento / learning procedure | extracto 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Entrenamiento / learning procedure | extracto 5 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Datos / trazas / datasets / contenidos

**[Datos / trazas / datasets / contenidos | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Datos / trazas / datasets / contenidos | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Datos / trazas / datasets / contenidos | extracto 3 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Datos / trazas / datasets / contenidos | extracto 4 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Evaluación / baselines / experimentos | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Evaluación / baselines / experimentos | extracto 3 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Evaluación / baselines / experimentos | extracto 4 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

### 4.x Limitaciones / riesgos / aplicabilidad

**[Limitaciones / riesgos / aplicabilidad | extracto 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning (RL) fine-tuning. We also introduce benchmarks, ABRBench-3G and ABRBench-4G+, which provide wide-coverage training traces and dedicated OOD test sets for assessing robustness to unseen network conditions. Experimental results demonstrate that SABR achieves the best average rank compared with Pensieve, Comyco, and NetLLM across the proposed benchmarks. These results indicate that SABR enables more 

**[Limitaciones / riesgos / aplicabilidad | extracto 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective evaluation of ABR models’ generalization to unseen network conditions. • We empirically validate that SABR achieves the best average rank compared with Pensieve, Comyco, NetLLM, and the other baselines. II. RELATED WORKS Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and RL to overcome the limitations of traditional rule-based bitrate co

**[Limitaciones / riesgos / aplicabilidad | extracto 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t ̸= aw t 8: Append sample: B ←B ∪{(st, aw t , al t)} 9: Execute at in the ABR simulator to obtain next state st+1 10: end for 11: for 1, 2, . . . , Epretrain do 12: Sample mini-batch ˆB of size mpretrain from B 13: Update πθ using the DPO loss on ˆB (Eq. 2) 14: end for 15: end for 16: Output: Base model πθ B. RL fine-tuning with PPO Only BC training is constrained to the distribution of expert pol

**[Limitaciones / riesgos / aplicabilidad | extracto 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mask the performance under other bandwidth conditions. Tables I and II present the trace set information of ABRBench-3G and ABRBench-4G+. TABLE I ABRBENCH-3G TRACE STATISTICS Group Trace Set Count Range (Mbps) Training Same with test 1828 0.00 ∼45.38 Test FCC-16 [6], [21], [22] 69 0.00 ∼8.95 FCC-18 [23], [24] 100 0.00 ∼41.76 Oboe [25], [26] 100 0.16 ∼9.01 Puffer-21 [26], [27] 100 0.00 ∼25.14 Puffer-2

**[Limitaciones / riesgos / aplicabilidad | extracto 5 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm is executed ten times, and the average performance is reported. For the learning-based methods (SABR, Pensieve, Comyco, and NetLLM), each result is obtained by training ten separate models, and the reported performance is the average across all models on the test runs. Furthermore, we compute the average rank of each algorithm across the multiple trace sets in each benchmark. Formally, let ri,j de

## 5. Figuras, tablas, algoritmos y ecuaciones detectadas por texto

**[elemento detectado 1 | p.1]**

SABR: A Stable Adaptive Bitrate Framework Using Behavior Cloning Pretraining and Reinforcement Learning Fine-Tuning Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†, Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE ∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China †School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn ‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore Email: {ebhsoong, chau.yuen}@ntu.edu.sg Abstract—With the advent of 5G, the internet has entered a new video-centric era. From short-video platforms like TikTok to long-video platforms like Bilibili, online video services are reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality of Experience (QoE). Recent learning-based ABR methods have attracted increasing attention. However, most of them rely on limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions, resulting in poor generalization in out-of-distribution (OOD) scenarios. To address this limitation, we propose SABR, a training framework that combines behavior cloning (BC) pretraining with reinforcement learning 

**[elemento detectado 2 | p.2]**

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF leverages the exploration capability of RL to align the model’s behavior with human preferences. This combination enables Generative Pre-trained Transformer (GPT) models to faithfully assist and serve humans in real-world daily applications. Inspired by this, we propose a two-stage training framework for ABR, termed SABR: Behavior Cloning (BC) pretraining + RL fine-tuning. In the pretraining stage, we adopt the Direct Preference Optimization (DPO) [4] algorithm to perform BC on expert data, obtaining a base model. In the fine-tuning stage, we optimize the base model using the Proximal Policy Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution (OOD) set. Our main contributions are as follows: • We propose a stable framework, SABR, which combines BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range of network trace data. • We design SABR with DPO-based BC for fast and stable pretraining, and PPO-based RL for deeper exploration, enabling robust adaptation to challenging network dynamics. • We release two benchmarks, which provide an effective 

**[elemento detectado 3 | p.3]**

β > 0 controls the update strength, and σ(·) denotes the sigmoid function. D is the set of preference trajectory pairs. In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise formulation as follows: LDPO-step(θ) = −E(s,aw,al)∼D h log σ  β · h log πθ(aw | s) πref(aw | s) −log πθ(al | s) πref(al | s) ii . (2) Here, (s, aw, al) ∼D are sampled state-action pairs, where aw is an expert (preferred) action and al is a less preferred (e.g., randomly sampled) alternative. The loss encourages the model to increase the preference margin for expert actions over less preferred ones at each step. The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through interaction with the ABR simulator, the model collects samples that are subsequently used for training. The beam search strategy follows the implementation from Comyco [8], [15]. Algorithm 1 BC pretraining with DPO 1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR simulator, iteration Npretrain, rollout step Tpretrain, epoch Epretrain, mini-batch size mpretrain 2: Initialize πref, buffer B ←∅, obtain initial state s1 from ABR simulator 3: for 1, 2, . . . , Npretrain do 4: for 1, 2, . . . , Tpretrain do 5: Select action at ∼πθ(· | st) 6: Expert action aw t ←BEAM SEARCH POLICY(st) 7: Randomly select an alternative action al t

**[elemento detectado 4 | p.4]**

encouraging exploration; and c1 and c2 are their respective weighting coefficients. The overall RL fine-tuning procedure with PPO is shown in Algorithm 2. IV. PROPOSED BENCHMARKS We release two benchmarks: ABRBench-3G and ABRBench-4G+. Each benchmark consists of both video content and network traces. The traces are reorganized and curated from publicly available trace sets on the internet, such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22]. Each benchmark contains multiple trace sets to ensure broad coverage of network conditions. In each benchmark, traces are divided into training, testing, and OOD sets. The training and testing sets are created by splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the remaining 30% are used for testing. The OOD set is also used to evaluate model performance, but unlike the test set, it specifically focuses on assessing generalization to unseen distributions. Therefore, trace sets included in the OOD set are not split or reused in other sets. For training, models are trained on the entire training set with all traces randomly shuffled. Evaluation is performed separately for each trace set within the test and OOD sets. During evaluation, we preserve the trace set granularity, since certain trace sets (e.g., those with high bandwidth) can skew the overall average QoE and mas

**[elemento detectado 5 | p.5]**

−µ N X n=1 Tn, (6) where N represents the total number of video chunks, Rn is the bitrate of the n-th chunk, and Tn denotes the rebuffering time at that step. The function q(Rn) maps the bitrate Rn to a corresponding quality score. δ is the smoothness penalty coefficient, and µ is the rebuffering penalty coefficient. Consistent with prior work [6], [8], [34], we adopt q(Rn) = Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines: • Buffer-Based (BB): A simple heuristic that adapts bitrates based on buffer occupancy to reduce rebuffering. • BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations. • RobustMPC [34]: An extension of the MPC method. It maximizes a given QoE metric over a horizon of 5 future chunks. • QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate decisions based on expected buffer occupancy. • Pensieve [6]: An RL-based ABR method that trains a policy network with A3C to maximize a QoE reward. • Comyco [8]: A learning-based ABR method that employs imitation learning to train a policy from MPC-generated expert trajectories. • NetLLM [12]: Adapts LLMs to ABR by combining parameter-efficient fine-tuning (LoRA) with offline RL. For the comparative evaluation, each algorithm 

## 6. Texto crudo extraído del cuerpo principal por página

> Esta sección conserva el texto extraído página a página hasta referencias/bibliografía cuando se detecta. Se incluye para no perder detalles de método, entrenamiento, datos o evaluación. Puede tener problemas de orden de columnas o fórmulas por naturaleza del PDF.

### Página 1

SABR: A Stable Adaptive Bitrate Framework
Using Behavior Cloning Pretraining and
Reinforcement Learning Fine-Tuning
Pengcheng Luo∗†, Yunyang Zhao∗†, Bowen Zhang∗†, Genke Yang∗†,
Boon-Hee Soong‡, Senior Member, IEEE, Chau Yuen‡, Fellow, IEEE
∗Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong University, Ningbo, China
†School of Automation and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai, China
Email: {luopeng69131, zyyfighting, bwz96sco, gkyang}@sjtu.edu.cn
‡School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore
Email: {ebhsoong, chau.yuen}@ntu.edu.sg
Abstract—With the advent of 5G, the internet has entered a
new video-centric era. From short-video platforms like TikTok
to long-video platforms like Bilibili, online video services are
reshaping user consumption habits. Adaptive Bitrate (ABR) control is widely recognized as a critical factor influencing Quality
of Experience (QoE). Recent learning-based ABR methods have
attracted increasing attention. However, most of them rely on
limited network trace sets during training and overlook the widedistribution characteristics of real-world network conditions,
resulting in poor generalization in out-of-distribution (OOD)
scenarios. To address this limitation, we propose SABR, a training
framework that combines behavior cloning (BC) pretraining
with reinforcement learning (RL) fine-tuning. We also introduce
benchmarks, ABRBench-3G and ABRBench-4G+, which provide
wide-coverage training traces and dedicated OOD test sets for
assessing robustness to unseen network conditions. Experimental
results demonstrate that SABR achieves the best average rank
compared with Pensieve, Comyco, and NetLLM across the
proposed benchmarks. These results indicate that SABR enables
more stable learning across wide distributions and improves
generalization to unseen network conditions.
Index Terms—Adaptive Bitrate, pretraining, fine-tuning, behavior cloning, reinforcement learning
I. INTRODUCTION
The emergence of 5G networks marks a new stage of
internet development, in which video constitutes the dominant share of digital content. Short-form services such as
TikTok and long-form streaming platforms such as Bilibili
are reshaping content consumption habits, making video the
primary medium for information, entertainment, and social
interaction worldwide. In this context, the smoothness and
clarity of video playback are decisive for user experience, with
Adaptive Bitrate (ABR) algorithms serving as a fundamental
mechanism to ensure high Quality of Experience (QoE). ABR
algorithms dynamically adjust video bitrate in response to realtime fluctuations in network bandwidth, thereby minimizing
stalling and latency, as illustrated in Figure 1.
Code: https://github.com/luopeng69131/SABR
Dataset: https://github.com/luopeng69131/ABRBench
Fig. 1. An overview of ABR.
As the user base continues to expand, video streaming
service providers accumulate massive volumes of network data
on a daily basis. This wealth of data presents unprecedented
opportunities for analyzing user behavior and optimizing
streaming strategies, while also providing a solid foundation
for applying artificial intelligence (AI) techniques to ABR research. AI approaches such as deep learning and reinforcement
learning (RL) are increasingly driving ABR algorithms toward
higher performance and stronger adaptability. Nevertheless,
current research still faces the following two major challenges:
• Limited generalization to unseen distributions: Most studies train ABR models on a specific network trace set,
without fully leveraging the vast amount of network
trace data. Therefore, models exhibit limited performance
when facing unseen network conditions.
• Degradation under wide-distribution training: When the
training dataset encompasses a broad spectrum of network conditions, the efficiency and stability of the ABR
model training can be significantly undermined.
Similar issues have been studied in the field of large
language models (LLMs), where the two-stage training framework of pretraining + fine-tuning has proven to be an effective
solution [1], [2]. The pretraining stage enables the model
to acquire initial representations and understanding of widedistribution training data, while the fine-tuning stage enables
more effective generalization to the target environment. In
LLM alignment techniques, Supervised Fine-Tuning (SFT) +
Reinforcement Learning from Human Feedback (RLHF) can
be regarded as an extension of this framework [3]. SFT uses
arXiv:2509.10486v1  [cs.NI]  30 Aug 2025

### Página 2

large-scale supervised data to help the model initially understand human instructions and task structures, while RLHF
leverages the exploration capability of RL to align the model’s
behavior with human preferences. This combination enables
Generative Pre-trained Transformer (GPT) models to faithfully
assist and serve humans in real-world daily applications.
Inspired by this, we propose a two-stage training framework
for ABR, termed SABR: Behavior Cloning (BC) pretraining
+ RL fine-tuning. In the pretraining stage, we adopt the Direct
Preference Optimization (DPO) [4] algorithm to perform BC
on expert data, obtaining a base model. In the fine-tuning
stage, we optimize the base model using the Proximal Policy
Optimization (PPO) [5] algorithm. We also integrate mainstream network trace sets and videos to construct benchmarks:
ABRBench-3G and ABRBench-4G+. Each benchmark contains a training set, a test set, and an Out-of-Distribution
(OOD) set. Our main contributions are as follows:
• We propose a stable framework, SABR, which combines
BC pretraining and RL fine-tuning. The framework improves ABR generalization by leveraging a wide range
of network trace data.
• We design SABR with DPO-based BC for fast and stable
pretraining, and PPO-based RL for deeper exploration,
enabling robust adaptation to challenging network dynamics.
• We release two benchmarks, which provide an effective
evaluation of ABR models’ generalization to unseen
network conditions.
• We empirically validate that SABR achieves the best
average rank compared with Pensieve, Comyco, NetLLM,
and the other baselines.
II. RELATED WORKS
Learning-based ABR research has been extensively explored, with the core idea of leveraging neural networks and
RL to overcome the limitations of traditional rule-based bitrate
control. Pensieve [6] was the first to apply the RL model to
ABR, using network states (e.g., throughput and buffer length)
as inputs to train an A3C [7] policy on 3G network traces,
thereby demonstrating the feasibility and advantages of RL
in ABR control. Comyco [8] further introduced quality-aware
QoE metrics and employed imitation learning from Model
Predictive Control (MPC)-generated expert data, significantly
improving training efficiency and model performance. To
address user differences in video quality preferences, Jade [9]
incorporated ranking-based QoE feedback into RLHF, aligning
the optimization objective and achieving QoE improvements
across heterogeneous network conditions.
Genet [10] introduced an automatic curriculum learning
approach [11], which starts from network environments with
large performance gaps compared to the rule baselines, and
gradually expands the training distribution, thereby enabling
the model to improve progressively. However, curriculum
learning may suffer from distributional shift and forgetting issues when the training distribution becomes broad.
NetLLM [12] adapted LLMs to multiple networking tasks,
including ABR. Through multi-modal encoding and LowRank adaptation (LoRA) [13], it reduced training costs and
showcased the potential of LLMs in ABR tasks.
While these works have advanced learning-based ABR, two
limitations persist: limited generalization to unseen network
conditions and degraded stability under wide-distribution training. These issues underscore the necessity of more robust and
efficient training paradigms, with comprehensive benchmarks
for evaluation.
III. PROPOSED SABR FRAMEWORK
The SABR framework consists of two stages: BC pretraining and RL fine-tuning. In the BC pretraining stage, we train
the model on expert data using the DPO algorithm to obtain
a base model. In the RL fine-tuning stage, we refine the base
model via PPO training. An overview of the framework is
shown in Figure 2.
Fig. 2. Proposed SABR framework: BC pretraining + RL fine-tuning.
A. BC pretraining with DPO
Originally proposed for preference alignment in LLMs,
DPO directly maximizes the likelihood ratio of humanpreferred responses, thereby avoiding the need for reward
models and complex RL optimization commonly used in
traditional RLHF pipelines. Motivated by its ability to directly
capture preferences from data, we adopt DPO to learn from
expert demonstrations for ABR. In the BC pretraining stage,
we use DPO to efficiently learn from expert samples, treating
them as preferred actions. This initializes a base model with
stable performance and a stronger control policy for ABR.
In the original DPO algorithm, given a pair of candidate
trajectories τw (the “winner”) and τl (the “loser”), it directly
maximizes the log-ratio of their probabilities to favor the
preferred trajectory. The objective is defined as:
LDPO(θ) = −E(τw,τl)∼D
h
log σ

β ·
h
log πθ(τw)
πref(τw)
−log πθ(τl)
πref(τl)
ii
. (1)
Here, πθ(τ) denotes the likelihood of trajectory τ under the
current model, while πref(τ) represents the likelihood under a
reference model, typically the initialization model. The scalar

### Página 3

β > 0 controls the update strength, and σ(·) denotes the
sigmoid function. D is the set of preference trajectory pairs.
In BC training, since we focus on learning from each stateaction pair, we adapt the original DPO loss into a step-wise
formulation as follows:
LDPO-step(θ) = −E(s,aw,al)∼D
h
log σ

β ·
h
log πθ(aw | s)
πref(aw | s)
−log πθ(al | s)
πref(al | s)
ii
.
(2)
Here, (s, aw, al) ∼D are sampled state-action pairs, where aw
is an expert (preferred) action and al is a less preferred (e.g.,
randomly sampled) alternative. The loss encourages the model
to increase the preference margin for expert actions over less
preferred ones at each step.
The BC training procedure is designed following the DAGGER algorithm [14], as detailed in Algorithm 1. Through
interaction with the ABR simulator, the model collects samples
that are subsequently used for training. The beam search
strategy follows the implementation from Comyco [8], [15].
Algorithm 1 BC pretraining with DPO
1: Input: Initial model πθ, BEAM SEARCH POLICY, ABR
simulator, iteration Npretrain, rollout step Tpretrain, epoch
Epretrain, mini-batch size mpretrain
2: Initialize πref, buffer B ←∅, obtain initial state s1 from
ABR simulator
3: for 1, 2, . . . , Npretrain do
4:
for 1, 2, . . . , Tpretrain do
5:
Select action at ∼πθ(· | st)
6:
Expert action aw
t ←BEAM SEARCH POLICY(st)
7:
Randomly select an alternative action al
t ̸= aw
t
8:
Append sample: B ←B ∪{(st, aw
t , al
t)}
9:
Execute at in the ABR simulator to obtain next state
st+1
10:
end for
11:
for 1, 2, . . . , Epretrain do
12:
Sample mini-batch ˆB of size mpretrain from B
13:
Update πθ using the DPO loss on ˆB (Eq. 2)
14:
end for
15: end for
16: Output: Base model πθ
B. RL fine-tuning with PPO
Only BC training is constrained to the distribution of expert
policies and lacks the capacity to explore a broader policy
space. To improve generalization in network environments,
we perform RL fine-tuning of the base model using PPO.
PPO is a policy-gradient–based RL method that restricts the
extent of policy updates between iterations to prevent training
instability and performance collapse. PPO has demonstrated
strong stability and sample efficiency in both continuous [16]
and discrete tasks [17].
PPO consists of both an actor network πθ and a critic
network Vϕ. The objective of the actor network is formalized
through the actor loss, given by:
LActor(θ) = Et
h
min
 rt(θ)At, clip(rt(θ), 1 −ϵ, 1 + ϵ)At
i
,
(3)
where
rt(θ) = πθ(at | st)
πθold(at | st),
(4)
denotes the probability ratio between the current actor network
πθ(a | s) and the previous actor network πθold(a | s). At is the
advantage estimate at time step t, and ϵ is the clipping threshold. The advantage function At is typically computed using
Generalized Advantage Estimation (GAE) [18], which reflects
the reward information that guides policy improvement.
Algorithm 2 RL fine-tuning with PPO
1: Input: Actor network πθ (initialized from base model),
critic network Vϕ, ABR simulator, iteration Nfinetune, rollout steps Tfinetune, PPO epochs Efinetune, mini-batch size
mfinetune, clipping parameter ϵ, discount factor γ, GAE
parameter λ
2: Empty buffer B ←∅, obtain initial state s1 from ABR
simulator
3: for 1, 2, . . . , Nfinetune do
4:
for 1, 2, . . . , Tfinetune do
5:
Select action at ∼πθ(· | st)
6:
Execute at in the ABR simulator to obtain reward rt
and next state st+1
7:
Append transition: B ←B ∪{(st, at, rt, st+1)}
8:
end for
9:
For all transitions in B, compute ˆVt = Vϕ(st) and
ˆVt+1 = Vϕ(st+1)
10:
Compute TD errors δt
= rt + γ ˆVt+1 −ˆVt, then
advantages ˆAt via GAE with (γ, λ)
11:
Set target value V target
t
= ˆVt + ˆAt for critic updates
12:
Augment
each
transition
in
B
to
{(st, at, rt, st+1, ˆAt, V target
t
)}
13:
for 1, 2, . . . , Efinetune do
14:
Sample mini-batch ˆB of size mfinetune from B
15:
Update parameters θ and ϕ using the full PPO
objective (Eq. 5) on ˆB
16:
end for
17:
Clear B ←∅
18:
πθold ←πθ
19: end for
20: Output: fine-tuned model πθ
The full PPO objective combines the actor loss, critic loss,
and an entropy regularization term, and is given by:
LPPO(θ) = Et
h
LActor(θ)−c1
 Vϕ(st)−V target
t
2+c2S[πθ](st)
i
,
(5)
where Vϕ(st) is the state value predicted by the critic network,
with
 Vϕ(st) −V target
t
2 as the critic loss where V target
t
is
the target value; S[πθ](st) is an entropy regularization term

### Página 4

encouraging exploration; and c1 and c2 are their respective
weighting coefficients. The overall RL fine-tuning procedure
with PPO is shown in Algorithm 2.
IV. PROPOSED BENCHMARKS
We
release
two
benchmarks:
ABRBench-3G
and
ABRBench-4G+. Each benchmark consists of both video
content and network traces. The traces are reorganized and
curated from publicly available trace sets on the internet,
such as Lumos 4G/5G [19], [20] and FCC [6], [21], [22].
Each benchmark contains multiple trace sets to ensure broad
coverage of network conditions.
In each benchmark, traces are divided into training, testing,
and OOD sets. The training and testing sets are created by
splitting each trace set proportionally. For example, in FCC18, 75% of traces are allocated to the training set, while the
remaining 30% are used for testing. The OOD set is also
used to evaluate model performance, but unlike the test set,
it specifically focuses on assessing generalization to unseen
distributions. Therefore, trace sets included in the OOD set
are not split or reused in other sets.
For training, models are trained on the entire training set
with all traces randomly shuffled. Evaluation is performed
separately for each trace set within the test and OOD sets.
During evaluation, we preserve the trace set granularity, since
certain trace sets (e.g., those with high bandwidth) can skew
the overall average QoE and mask the performance under other
bandwidth conditions. Tables I and II present the trace set
information of ABRBench-3G and ABRBench-4G+.
TABLE I
ABRBENCH-3G TRACE STATISTICS
Group
Trace Set
Count
Range (Mbps)
Training
Same with test
1828
0.00 ∼45.38
Test
FCC-16 [6], [21], [22]
69
0.00 ∼8.95
FCC-18 [23], [24]
100
0.00 ∼41.76
Oboe [25], [26]
100
0.16 ∼9.01
Puffer-21 [26], [27]
100
0.00 ∼25.14
Puffer-22 [26], [27]
100
0.00 ∼9.29
OOD
HSR [24]
34
0.00 ∼44.68
TABLE II
ABRBENCH-4G+ TRACE STATISTICS
Group
Trace Set
Count
Range (Mbps)
Training
Same with test
262
0.00 ∼1890.00
Test
Lumos 4G [19], [20]
53
0.00 ∼270.00
Lumos 5G [19], [20]
37
0.00 ∼1920.00
Solis Wi-Fi [28]
24
0.00 ∼124.00
OOD
Ghent [24]
40
0.00 ∼110.97
Lab [24]
61
0.16 ∼175.91
We denote the set of available bitrates as R. Specifically, ABRBench-3G uses the Envivio-Dash3 [29] video
TABLE III
HYPERPARAMETERS FOR THE SABR FRAMEWORK
Symbol
Description
Value
DPO parameters
Npretrain
Iteration (DPO)
15
Epretrain
Epochs per pretraining iteration
5
Tpretrain
Rollout steps per iteration
2000
mpretrain
Mini-batch size (pretraining)
128
αpretrain
DPO learning rate
3e-4
β
DPO update scale
0.1
PPO parameters
Nfinetune
Iteration (PPO)
244
Efinetune
PPO epochs per update
10
Tfinetune
Rollout steps per environment
512
mfinetune
Mini-batch size (fine-tuning)
64
αfinetune
PPO learning rate
3e-4
ϵ
Clipping threshold
0.2
γ
Discount factor
0.99
λ
GAE parameter
0.95
c1
Coefficient of critic loss
0.5
c2
Coefficient of entropy
0.0
Other parameters
Lbeam
Beam search future horizon
5
Kmax
Beam search maximum beam
5000
with
R3G
=
{300, 750, 1200, 1850, 2850, 4300},
while
ABRBench-4G+ uses the Big Buck Bunny [30] video with
R4G+ = {1000, 2500, 5000, 8000, 16000, 40000}.
V. IMPLEMENTATION DETAILS
The state, action, reward function, and state transition in
our Markov Decision Process are consistent with those in Pensieve [6]. Our ABR simulator follows the design of Pensieve’s
Python environment [6], while using the C++ implementation
from [8], [15] to improve efficiency. Apart from the C++
simulator, all other components are implemented in Python.
The BC pretraining is implemented in PyTorch [31], while
RL fine-tuning is based on the PPO algorithm from StableBaselines3 (SB3) [32]. During training, we utilize the Vector
Environment module of SB3 to enable parallel sample collection, thereby improving training efficiency. The number of
parallel environments is set to 4.
In the implementations of Pensieve [6] and Comyco [8],
the input features are represented as a 6-by-8 matrix. In our
implementation, we flatten this matrix into a 48-dimensional
vector. The actor network πθ (base model) adopts a fully
connected network of [48, tanh, 64, tanh, 64, 6], while the
critic network is designed as [48, tanh, 64, tanh, 64, 1]. The
two networks do not share parameters. For both DPO and
PPO training, the Adam optimizer [33] is employed. The
hyperparameter settings of the SABR are shown in Table III.
VI. EVALUATION
A. Experimental setup
We build a trace-driven ABR simulator [6], where both
network traces and video content are drawn from ABRBench3G and ABRBench-4G+. Each experiment is conducted on
videos consisting of 49 chunks, with each chunk lasting 4
seconds, emulated over the collected network traces.

### Página 5

We evaluate performance using the QoE metrics:
QoE =
N
X
n=1
q(Rn) −δ
N−1
X
n=1
q(Rn+1) −q(Rn)
 −µ
N
X
n=1
Tn,
(6)
where N represents the total number of video chunks, Rn is
the bitrate of the n-th chunk, and Tn denotes the rebuffering
time at that step. The function q(Rn) maps the bitrate Rn
to a corresponding quality score. δ is the smoothness penalty
coefficient, and µ is the rebuffering penalty coefficient.
Consistent with prior work [6], [8], [34], we adopt q(Rn) =
Rn, where Rn ∈R3G or R4G+. We set N = 49, δ = 1, and
use µ = 4.3 for ABRBench-3G and µ = 40 for ABRBench4G+. We compare SABR against baselines:
• Buffer-Based (BB): A simple heuristic that adapts bitrates
based on buffer occupancy to reduce rebuffering.
• BOLA [35]: Uses Lyapunov optimization to select bitrates solely considering buffer occupancy observations.
• RobustMPC [34]: An extension of the MPC method. It
maximizes a given QoE metric over a horizon of 5 future
chunks.
• QUETRA [36]: A queueing-theoretic algorithm that models the ABR task as an M/D/1/K system, enabling bitrate
decisions based on expected buffer occupancy.
• Pensieve [6]: An RL-based ABR method that trains a
policy network with A3C to maximize a QoE reward.
• Comyco [8]: A learning-based ABR method that employs
imitation learning to train a policy from MPC-generated
expert trajectories.
• NetLLM [12]: Adapts LLMs to ABR by combining
parameter-efficient fine-tuning (LoRA) with offline RL.
For the comparative evaluation, each algorithm is executed
ten times, and the average performance is reported. For
the learning-based methods (SABR, Pensieve, Comyco, and
NetLLM), each result is obtained by training ten separate
models, and the reported performance is the average across all
models on the test runs. Furthermore, we compute the average
rank of each algorithm across the multiple trace sets in each
benchmark. Formally, let ri,j denote the rank of algorithm i
on trace set j, and let M be the total number of trace sets in
the benchmark. The average rank of algorithm i is defined as
Ave Rank(i) = 1
M
M
X
j=1
ri,j.
(7)
A lower average rank indicates better overall performance.
B. Proposed SABR vs. existing baselines
To evaluate the generalization capability of the models, we
conducted comparisons across different methods on the test
sets of ABRBench-3G and ABRBench-4G+. The learningbased models were trained on the corresponding benchmark
training sets before testing. Tables IV and V show the QoE
performance of the different methods.
For ABRBench-3G, SABR achieved the best QoE performance on FCC-16, FCC-18, Oboe, and Puffer-22. For
TABLE IV
QOE PERFORMANCE COMPARISON ON THE ABRBENCH-3G TEST SETS
Algorithm
FCC-16
FCC-18
Oboe
Puffer-21
Puffer-22
Ave Rank
BB
25.37
131.54
82.74
-6.05
13.28
7.2
BOLA
32.51
123.42
81.02
38.35
30.99
6.0
QUETRA
33.91
122.25
82.84
42.48
36.89
4.4
RobustMPC
36.56
143.30
96.14
34.13
36.90
3.4
Pensieve
34.50
134.39
90.92
38.94
35.23
3.8
Comyco
32.10
143.89
96.23
-4.09
31.34
4.8
NetLLM
21.92
141.91
97.39
37.55
33.73
4.6
SABR
36.68
145.18
99.68
36.05
40.05
1.8
TABLE V
QOE PERFORMANCE COMPARISON ON THE ABRBENCH-4G+ TEST SETS
Algorithm
Lumos 4G
Lumos 5G
Solis Wi-Fi
Ave Rank
BB
1255.91
1726.66
429.34
5.0
BOLA
1200.05
1614.40
477.08
5.0
QUETRA
754.43
992.74
421.58
7.7
RobustMPC
1283.05
1696.77
589.64
3.0
Pensieve
1160.76
1828.24
447.84
5.0
Comyco
1285.43
1835.42
552.55
2.0
NetLLM
672.35
1510.35
474.15
6.7
SABR
1309.65
1832.14
576.33
1.7
ABRBench-4G+, SABR achieved the highest QoE on Lumos
4G, while performing slightly worse than the best methods
on the other two trace sets. Across both benchmarks, SABR
attains the lowest average rank among all methods, demonstrating its overall superior performance and robustness across
diverse network conditions.
C. Evaluation on the OOD datasets
To evaluate the generalization performance of the models
under unseen distributions, we conducted comparisons on the
OOD datasets of ABRBench-3G (HSR) and ABRBench-4G+
(Ghent and Lab). The learning-based models were trained on
the corresponding benchmark training sets before testing. Table VI presents the QoE performance of the different methods.
SABR obtained the lowest average rank (2.0), outperforming
Comyco (3.7), RobustMPC (4.0), and other baselines. This
indicates that SABR maintains strong performance on unseen
distributions.
TABLE VI
QOE PERFORMANCE COMPARISON ON THE OOD SETS
Algorithm
HSR
Ghent
Lab
Ave Rank
BB
138.86
834.30
1429.22
4.3
BOLA
137.02
912.39
1342.63
5.0
QUETRA
132.56
566.61
965.94
7.0
RobustMPC
122.37
1075.17
1527.84
4.0
Pensieve
137.82
652.45
1508.43
4.7
Comyco
130.22
963.94
1595.09
3.7
NetLLM
129.25
1035.09
1307.49
5.3
SABR
142.20
1023.56
1561.18
2.0
VII. CONCLUSION
In this paper, we propose SABR, a two-stage framework
consisting of BC pretraining and RL fine-tuning. The frame-

## 7. Referencias/bibliografía
Referencias detectadas desde la página 6. No se expanden completas aquí para no contaminar la lectura de método; consultar PDF original o raw text si hace falta.
