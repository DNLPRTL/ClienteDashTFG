# Incendio: Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance
**Archivo PDF:** `3592473.3592564.pdf`  **Identificador:** `14_incendio_sabr_marl_expert_guidance`  **Páginas:** 7  **SHA256 PDF:** `f0892af80b424cfa0cce1a60c3c5136287aef62856899b26c4bac95cfe6fd6b4`  **Foco para Fase 4-5 v1:** Short-video ABR; MARL with expert guidance; imitation initialization and fine-tuning; bitrate + video-ID decisions.
> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.
## 1. Cómo usar este `.md`
- Leer primero secciones 2-5 para ubicar método, señales, datos, evaluación y limitaciones.
- Usar la extracción por categorías como material de diseño/contrato/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No convertir resultados del paper en promesas directas para DashClientModular4; deben transformarse en hipótesis, guardrails y tests Phase 6.
## 2. Metadatos extraídos
- **format:** PDF 1.7
- **title:** Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance
- **author:** Yueheng Li; Qianyuan Zheng; Zicheng Zhang; Hao Chen; Zhan Ma
- **subject:** -  Information systems  ->  Multimedia streaming.
- **keywords:** Short video streaming, Adaptive bitrate, Reinforcement Learning
- **creator:** LaTeX with acmart 2022/04/09 v1.84 Typesetting articles for the Association for Computing Machinery and hyperref 2022-06-13 v7.00r Hypertext links for LaTeX
- **producer:** pdfTeX, Version 3.141592653-2.6-1.40.24 (TeX Live 2022) kpathsea version 6.3.4; modified using iText® 7.1.16 ©2000-2021 iText Group NV (AGPL-version)
- **creationDate:** D:20230412080753Z
- **modDate:** D:20230524094036-04'00'

## 3. Índice de secciones detectadas
- p.1: ABSTRACT
- p.1: experiments indicate that Incendio outperforms the current state-
- p.1: CCS CONCEPTS
- p.1: KEYWORDS
- p.1: INTRODUCTION
- p.1: methods were developed. For example, PDAS [21], a typical rules-
- p.2: BACKGROUNDS AND RELATED WORKS
- p.2: SYSTEM OVERVIEW
- p.3: method of Incendio in the following section.
- p.3: INCENDIO DESIGN
- p.4: evaluation, we still use Equation (1) to evaluate the performance.
- p.5: method, which represents the difference in the expected reward
- p.5: EVALUATION
- p.5: Methodology
- p.6: experiments are conducted on a desktop equipped with an Intel(R)
- p.6: CONCLUSION
- p.6: ACKNOWLEDGMENTS
- p.7: REFERENCES

## 4. Índice de páginas con palabras clave
- p.1: state, action, reward, QoE, buffer, bandwidth, download, chunk, training, MPC, PPO, expert, generalization, inference, quality, network condition
- p.2: state, action, reward, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, training, MPC, imitation, expert, risk, quality
- p.3: state, action, reward, rebuffer, buffer, throughput, bandwidth, download, chunk, training, imitation, expert, inference, network condition
- p.4: state, action, reward, QoE, throughput, bandwidth, download, chunk, trace, training, MPC, PPO, imitation, expert, quality
- p.5: state, action, reward, rebuffer, buffer, throughput, bandwidth, chunk, dataset, trace, training, baseline, MPC, expert, network condition
- p.6: state, action, reward, QoE, rebuffer, buffer, bandwidth, chunk, dataset, trace, training, MPC, PPO, imitation, expert, generalization, inference, quality, visual, network condition
- p.7: action, bandwidth, Pensieve, PPO, imitation, expert, quality, visual, network condition

## 5. Extracción técnica cruda por categorías

### 5.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE

**[Modelo / arquitectura / algoritmo | extracto 2 | p.1]**

pular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Ch

**[Modelo / arquitectura / algoritmo | extracto 3 | p.1]**

njing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng,

**[Modelo / arquitectura / algoritmo | extracto 4 | p.1]**

Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen,

**[Modelo / arquitectura / algoritmo | extracto 5 | p.1]**

ing author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0184-9/23/06...$15.00 https://doi.org/10.1145/3592473.3592564 the Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’23), June 7–10, 2023, Vancouver, BC, Canada. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3592473.3592564 1 INTRODUCTION In recent years, there has been a significant surge in using short video streaming applications such as Kwai [7] and TikTok [14] for entertainment, social connection, etc, resulting in exponential traffic growth. Such a short video service largely differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) durin

**[Modelo / arquitectura / algoritmo | extracto 6 | p.1]**

mpetitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuristic search for decision-making, its decision inference time grows exponentially as the length of the optimization horizon increases. Thus, RL-based approaches are introduced to overcome these issues through the use of neural networks to make a direct con- nection with environmental observation and action. For instance, DAM [9], an RL-based SABR method [3, 13], makes decisions for buffer management and bitrate adaptation simultaneously based 58

**[Modelo / arquitectura / algoritmo | extracto 7 | p.1]**

g University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma.

**[Modelo / arquitectura / algoritmo | extracto 8 | p.1]**

anjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Imp

**[Modelo / arquitectura / algoritmo | extracto 9 | p.1]**

ina Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving

**[Modelo / arquitectura / algoritmo | extracto 10 | p.2]**

r joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the us

**[Modelo / arquitectura / algoritmo | extracto 11 | p.2]**

winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rat

**[Modelo / arquitectura / algoritmo | extracto 12 | p.2]**

switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system architecture of Incendio is illustrated in Figure 1. Each short video is sliced into chunks with a length of 1s. Each chunk 1User retention rate indicates the percentage of the users that choose to continue the watching of current video by statistics, which can be provided by content providers at the granularity of chunk. 59

**[Modelo / arquitectura / algoritmo | extracto 13 | p.2]**

State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the p

**[Modelo / arquitectura / algoritmo | extracto 14 | p.2]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Y. Li et al. … Video queue Incendio’s SABR policy CDN Node client BM agent video ID, bitrate played playing downloaded to be downloaded State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate level

**[Modelo / arquitectura / algoritmo | extracto 15 | p.2]**

past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across a

**[Modelo / arquitectura / algoritmo | extracto 16 | p.2]**

e training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional

### 5.x Estado / inputs / features

**[Estado / inputs / features | extracto 1 | p.1]**

te level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bea

**[Estado / inputs / features | extracto 2 | p.1]**

Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert G

**[Estado / inputs / features | extracto 3 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inf

**[Estado / inputs / features | extracto 4 | p.1]**

ly differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system beha

**[Estado / inputs / features | extracto 5 | p.1]**

nterested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuris

**[Estado / inputs / features | extracto 6 | p.1]**

s the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [

**[Estado / inputs / features | extracto 7 | p.2]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Y. Li et al. … Video queue Incendio’s SABR policy CDN Node client BM agent video ID, bitrate played playing downloaded to be downloaded State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR frame

**[Estado / inputs / features | extracto 8 | p.2]**

nagement (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference

**[Estado / inputs / features | extracto 9 | p.2]**

s two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15],

**[Estado / inputs / features | extracto 10 | p.2]**

5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which

**[Estado / inputs / features | extracto 11 | p.2]**

asibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has atta

**[Estado / inputs / features | extracto 12 | p.2]**

of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorp

**[Estado / inputs / features | extracto 13 | p.3]**

to the queue. The RL agent of Incendio consists of two hierarchical agents re- sponsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. For each decision iteration, the BM-agent chooses to sleep for a fixed duration or selects a video that needs the most buffering based on observations of past throughput mea- surements and the status for each video in the queue including user retention rate, remaining buffer size, average chunk size, rebuffer- ing time, and bitrate as well as its fluctuation of last downloaded chunk. If BM-agent makes a sleep decision, the client’s preloading process will be suspended for a predefined time duration. Otherwise, BM-agent decides which video to prefetch with a video ID. Subse- quently, BA-agent determines the bitrate of the next chunk for this video to download based on video states and network conditions. Afterward, the client submits the request with a video ID and its bitrate to the CDN node and promotes a new round of interaction. The number of videos in the queue and the bitrate levels for each of them is determined by the underlying streaming platform. Here we adopt the same settings used in MMGC2022, which comprises five videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive ineffici

**[Estado / inputs / features | extracto 14 | p.3]**

n the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update for Incendio but also avoids it from converging to sub-optimal policies. conv2D 4x5x64 4x5x16 4x5x4 1x80 1x144 1x5 1x64 GRU 1x64 1x6 bm ta conv2D conv2D Flatten Fc 4x5x1  tb  ju  jl jg Fc Figure 3: The NN architecture of Incendio’s BM-agent. This section first introduces the input states, actions, and neural networks of Incendio’s agents, which remain consistent across the pre-train and fine-tune training stages. Then the training algorithms for pre-training and fine-tuning are elaborated. 4.1 Multi-agent Design Incendio’s multi-agent takes an action 𝑎𝑡based on the observations collected by clients as input state𝑠𝑡, according to its policy 𝜋𝜃(𝑠𝑡,𝑎𝑡) which is represented by neural networks. This subsection expounds on the specification of Incendio’s state, action, and neural network design. State. The state gathered by Incendio at step 𝑡is defined as 𝑠𝑡= ( ®𝑏𝑡, ®𝑙𝑗, ®𝑔𝑗, ®𝑢𝑗, ®ℎ𝑗, ®𝑞𝑗, ®𝑓𝑗). The first component is a vector of throughput measurements observed in past 𝐾chunks (e.g., ®𝑏𝑡= {𝑏𝑡−𝐾+1, . . . ,𝑏𝑡}), each of which can be calculated by dividing the chunk size by the download duration. The remaining state comp

**[Estado / inputs / features | extracto 15 | p.3]**

recommended video, 𝑚= 1) until the chunk 𝑛, which can be calculated as follows: 𝑙𝑗= 𝑝𝑛 𝑗 𝑝𝑚 𝑗 , (2) where 𝑝𝑚 𝑗denotes the user retention rate of video 𝑗in chunk 𝑚by statistical averaging; 𝑔𝑗represents the current buffer size for video 𝑗; 𝑢𝑗denotes the mean size of next chunks at different bitrates for video 𝑗; ℎ𝑗is the rebuffering time caused by downloading the last chunk for video 𝑗and is equal to 0 if no rebuffering occurred; and 𝑞𝑗and 𝑓𝑗respectively denote the bitrate and its fluctuation at which the last chunk was downloaded for video 𝑗. The bitrate fluctuation can be obtained by 𝑓𝑗= 𝑞𝑗−𝑞𝑗−1 . (3) The state for BM-agent is defined as 𝑠𝑏𝑚 𝑡 = ( ®𝑏𝑡, ®𝑙𝑗, ®𝑔𝑗, ®𝑢𝑗). And the state for BA-agent to make the decision on video 𝑗is defined as 𝑠𝑏𝑎 𝑡 = ( ®𝑏𝑡,𝑙𝑗,𝑔𝑗,𝑢𝑗,ℎ𝑗,𝑞𝑗, 𝑓𝑗). In this work, we set 𝐾= 5 empirically to capture the temporal features from past observations. Action. The output action 𝑎𝑏𝑚 𝑡 of BM-agent is a 0-1 vector with a length of 6. The first five values in this vector represent the corresponding video ID, while the last value signifies sleep for a fixed duration of 𝜏= 200𝑚𝑠. This setting is motivated by the need to balance the trade-off between utilizing computing resources optimally and not missing the ideal decision-making time. Simi- larly, the BA-agent takes an action 𝑎𝑏𝑎 𝑡 from the bitrate ladders of {750, 1200, 1850} kbps (same as MMGC2022), which correspond to different video qualities. 60

**[Estado / inputs / features | extracto 16 | p.3]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Environment imitation learning hand-crafted model expert model reinforcement learning optimal Incendio ta ˆta IL L ts ts ta ts ta GAE tA ta RL L Figure 2: Two-stage training of Incendio: it is first initiated by imitating the hand-crafted model and then fine-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue starts to play, and the downloaded but unplayed chunks for the previous video are cleared, resulting in a waste of bandwidth. In the meantime, a new video suggested by the video recommendation mechanism will be appended to the queue. The RL agent of Incendio consists of two hierarchical agents re- sponsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. For each decision iteration, the BM-agent chooses to sleep for a fixed duration or selects a video that needs the most buffering based on observations of past throughput mea- surements and the status for each video in the queue i

### 5.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuristic search for decision-making, its decision inference time grows exponentially as the length of the optimization horizon increases. Thus, RL-based approaches are introduced to overcome these issues through the use of neural networks to make a direct con- nection with environmental observation and action. For instance, DAM [9], an RL-based SABR method [3, 13], makes decisions for buffer management and bitrate adaptation simultaneously based 58

**[Acción / decisión ABR | extracto 2 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound

**[Acción / decisión ABR | extracto 3 | p.1]**

g, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Usin

**[Acción / decisión ABR | extracto 4 | p.1]**

jing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗B

**[Acción / decisión ABR | extracto 5 | p.1]**

ght held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0184-9/23/06...$15.00 https://doi.org/10.1145/3592473.3592564 the Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’23), June 7–10, 2023, Vancouver, BC, Canada. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3592473.3592564 1 INTRODUCTION In recent years, there has been a significant surge in using short video streaming applications such as Kwai [7] and TikTok [14] for entertainment, social connection, etc, resulting in exponential traffic growth. Such a short video service largely differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a

**[Acción / decisión ABR | extracto 6 | p.1]**

Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Age

**[Acción / decisión ABR | extracto 7 | p.2]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Y. Li et al. … Video queue Incendio’s SABR policy CDN Node client BM agent video ID, bitrate played playing downloaded to be downloaded State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accele

**[Acción / decisión ABR | extracto 8 | p.2]**

s SABR policy CDN Node client BM agent video ID, bitrate played playing downloaded to be downloaded State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces

**[Acción / decisión ABR | extracto 9 | p.2]**

sponsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network a

**[Acción / decisión ABR | extracto 10 | p.2]**

ntrol policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system architecture of Incendio is illustrated in Figure 1. Each short video is sliced into chunks with a length of 1s. Each chunk 1User retention rate indicates the percentage of the users that choose to continue the watching of current video by statistics, which can be provided by content providers at the granularity of chunk. 59

**[Acción / decisión ABR | extracto 11 | p.2]**

L made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system architecture of Incendio is illustrated in Figure 1. Each short video is sliced into chunks with a leng

**[Acción / decisión ABR | extracto 12 | p.2]**

retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system architecture of Incendio is illustrated in Figure 1. Each short video is sliced into chunks with a length of 1s. Each chunk 1User retention rate indicates the percentage of the users that choose to continue the watching of current

**[Acción / decisión ABR | extracto 13 | p.2]**

ity in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system architecture of Incendio is illustrated in Figure 1. Each short video is sliced into chunks with a length of 1s. Each chunk 1User retention rate indicates the percentage of the users that choose to continue the watching of current video by statistics, which can be provided by content providers at the granularity of chunk. 59

**[Acción / decisión ABR | extracto 14 | p.3]**

respectively. For each decision iteration, the BM-agent chooses to sleep for a fixed duration or selects a video that needs the most buffering based on observations of past throughput mea- surements and the status for each video in the queue including user retention rate, remaining buffer size, average chunk size, rebuffer- ing time, and bitrate as well as its fluctuation of last downloaded chunk. If BM-agent makes a sleep decision, the client’s preloading process will be suspended for a predefined time duration. Otherwise, BM-agent decides which video to prefetch with a video ID. Subse- quently, BA-agent determines the bitrate of the next chunk for this video to download based on video states and network conditions. Afterward, the client submits the request with a video ID and its bitrate to the CDN node and promotes a new round of interaction. The number of videos in the queue and the bitrate levels for each of them is determined by the underlying streaming platform. Here we adopt the same settings used in MMGC2022, which comprises five videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until conve

**[Acción / decisión ABR | extracto 15 | p.3]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Environment imitation learning hand-crafted model expert model reinforcement learning optimal Incendio ta ˆta IL L ts ts ta ts ta GAE tA ta RL L Figure 2: Two-stage training of Incendio: it is first initiated by imitating the hand-crafted model and then fine-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue starts to play, and the downloaded but unplayed chunks for the previous video are cleared, resulting in a waste of bandwidth. In the meantime, a new video suggested by the video recommendation mechanism will be appended to the queue. The RL agent of Incendio consists of two hierarchical agents re- sponsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. For each decision iteration, the BM-agent chooses to sleep for a fixed durat

**[Acción / decisión ABR | extracto 16 | p.3]**

-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue starts to play, and the downloaded but unplayed chunks for the previous video are cleared, resulting in a waste of bandwidth. In the meantime, a new video suggested by the video recommendation mechanism will be appended to the queue. The RL agent of Incendio consists of two hierarchical agents re- sponsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. For each decision iteration, the BM-agent chooses to sleep for a fixed duration or selects a video that needs the most buffering based on observations of past throughput mea- surements and the status for each video in the queue including user retention rate, remaining buffer size, average chunk size, rebuffer- ing time, and bitrate as well as its fluctuation of last downloaded chunk. If BM-agent makes a sleep decision, the client’s preloading process will be suspended for a predefined time duration. Otherwise, BM-agent decides which video to prefetch with a video ID. Subse- quently, BA-agent determines the bitrate of the next chunk for this video to download based on video states and network conditions. Afterward, the client submits the request with a video ID and its bitrate to the CDN node and promotes a new round of interaction. The number of videos in

### 5.x Reward / QoE / objetivo

**[Reward / QoE / objetivo | extracto 1 | p.1]**

challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuristic search for decision-making, its decision inference time grows exponentially as the length of the optimization horizon increases. Thus, RL-based approaches are introduced to overcome these issues through the use of neural networks to make a direct con- nection with environmental observation and action. For instance, DAM [9], an RL-based SABR method [3, 13], makes decisions for buffer management and bitrate adaptation simultaneously based 58

**[Reward / QoE / objetivo | extracto 2 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintain

**[Reward / QoE / objetivo | extracto 3 | p.1]**

3.3592564 the Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’23), June 7–10, 2023, Vancouver, BC, Canada. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3592473.3592564 1 INTRODUCTION In recent years, there has been a significant surge in using short video streaming applications such as Kwai [7] and TikTok [14] for entertainment, social connection, etc, resulting in exponential traffic growth. Such a short video service largely differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Bo

**[Reward / QoE / objetivo | extracto 4 | p.1]**

qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for compon

**[Reward / QoE / objetivo | extracto 5 | p.1]**

est permissions from permissions@acm.org. NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0184-9/23/06...$15.00 https://doi.org/10.1145/3592473.3592564 the Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’23), June 7–10, 2023, Vancouver, BC, Canada. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3592473.3592564 1 INTRODUCTION In recent years, there has been a significant surge in using short video streaming applications such as Kwai [7] and TikTok [14] for entertainment, social connection, etc, resulting in exponential traffic growth. Such a short video service largely differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client bu

**[Reward / QoE / objetivo | extracto 6 | p.1]**

r classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn

**[Reward / QoE / objetivo | extracto 7 | p.2]**

ion iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the

**[Reward / QoE / objetivo | extracto 8 | p.2]**

ndio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [

**[Reward / QoE / objetivo | extracto 9 | p.2]**

the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty t

**[Reward / QoE / objetivo | extracto 10 | p.2]**

ary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively repres

**[Reward / QoE / objetivo | extracto 11 | p.2]**

n well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly gen

**[Reward / QoE / objetivo | extracto 12 | p.2]**

th wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload or

**[Reward / QoE / objetivo | extracto 13 | p.2]**

ptimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system archit

**[Reward / QoE / objetivo | extracto 14 | p.2]**

ailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness

**[Reward / QoE / objetivo | extracto 15 | p.3]**

videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update for Incendio but also avoids it from converging to sub-optimal policies. conv2D 4x5x64 4x5x16 4x5x4 1x80 1x144 1x5 1x64 GRU 1x64 1x6 bm ta conv2D conv2D Flatten Fc 4x5x1  tb  ju  jl jg Fc Figure 3: The NN architecture of Incendio’s BM-agent. This section first introduces the input states, actions, and neural networks of Incendio’s agents, which remain consistent across the pre-train and fine-tune training stages. Then the training algorithms for pre-training and fine-tuning are elaborated. 4.1 Multi-agent Design Incendio’s multi-agent takes an action 𝑎𝑡based on the observations collected by clients as input state𝑠𝑡, according to its policy 𝜋𝜃(𝑠𝑡,𝑎𝑡) which is represented by neural networks. This subsection expounds on the specification of Incendio’s sta

**[Reward / QoE / objetivo | extracto 16 | p.3]**

in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update for Incendio but also avoids it from converging to sub-optimal policies. conv2D 4x5x64 4x5x16 4x5x4 1x80 1x144 1x5 1x64 GRU 1x64 1x6 bm ta conv2D conv2D Flatten Fc 4x5x1  tb  ju  jl jg Fc Figure 3: The NN architecture of Incendio’s BM-agent. This section first introduces the input states, actions, and neural networks of Incendio’s agents, which remain consistent across the pre-train and fine-tune training stages. Then the training algorithms for pre-training and fine-tuning are elaborated. 4.1 Multi-agent Design Incendio’s multi-agent takes an action 𝑎𝑡based on the observations collected by clients as input state𝑠𝑡, according to its policy 𝜋𝜃(𝑠𝑡,𝑎𝑡) which is represented by neural networks. This subsection expounds on the specification of Incendio’s state, action

### 5.x Entrenamiento / optimización

**[Entrenamiento / optimización | extracto 1 | p.1]**

eo applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to ma

**[Entrenamiento / optimización | extracto 2 | p.1]**

elding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others tha

**[Entrenamiento / optimización | extracto 3 | p.1]**

rates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted w

**[Entrenamiento / optimización | extracto 4 | p.1]**

n. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuristic search for decision-making, its decision inference time grows exponentially as the length of the optimization horizon increases. Thus, RL-based approaches are introduced to overcome these issues through the use of neural networks to make a direct con- nection with environmental observation and action. For instance, DAM [9], an RL-based SABR method [3, 13], makes decisions for buffer management and bitrate adaptation simultaneously based 58

**[Entrenamiento / optimización | extracto 5 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in thi

**[Entrenamiento / optimización | extracto 6 | p.1]**

load or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuristic search for decision-making, its decision inference time grows exponentially as the length of the optimization horizon increases. Thus, RL-based approaches are introduced to overcome these issues through the use of neural networks to make a direct con- nection with environmental observation and action. For instance, DAM [9], an RL-based SABR method [3, 13], makes decisions for buffer management and bitrate adaptation simultaneously based 58

**[Entrenamiento / optimización | extracto 7 | p.1]**

.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada © 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0184-9/23/06...$15.00 https://doi.org/10.1145/3592473.3592564 the Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’23), June 7–10, 2023, Vancouver, BC, Canada. ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3592473.3592564 1 INTRODUCTION In recent years, there has been a significant surge in using short video streaming applications such as Kwai [7] and TikTok [14] for entertainment, social connection, etc, resulting in exponential traffic growth. Such a short video service largely differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often lea

**[Entrenamiento / optimización | extracto 8 | p.2]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Y. Li et al. … Video queue Incendio’s SABR policy CDN Node client BM agent video ID, bitrate played playing downloaded to be downloaded State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network

**[Entrenamiento / optimización | extracto 9 | p.2]**

ng of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training

**[Entrenamiento / optimización | extracto 10 | p.2]**

e Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including

**[Entrenamiento / optimización | extracto 11 | p.2]**

related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function wel

**[Entrenamiento / optimización | extracto 12 | p.2]**

s attributed to the search in large discrete action space that is closely related to the number of videos in the queue and the total bitrate levels for each video. This paper, therefore, proposes the Incendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This sect

**[Entrenamiento / optimización | extracto 13 | p.3]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Environment imitation learning hand-crafted model expert model reinforcement learning optimal Incendio ta ˆta IL L ts ts ta ts ta GAE tA ta RL L Figure 2: Two-stage training of Incendio: it is first initiated by imitating the hand-crafted model and then fine-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue starts to play, and the downloaded but unplayed chunks for the previous video are cleared, resulting in a waste of bandwidth. In the meantime, a new video suggested by the video recommendation mechanism will be appended to the queue. The RL agent of Incendio consists of two hierarchical agents re- sponsible

**[Entrenamiento / optimización | extracto 14 | p.3]**

ffer size, average chunk size, rebuffer- ing time, and bitrate as well as its fluctuation of last downloaded chunk. If BM-agent makes a sleep decision, the client’s preloading process will be suspended for a predefined time duration. Otherwise, BM-agent decides which video to prefetch with a video ID. Subse- quently, BA-agent determines the bitrate of the next chunk for this video to download based on video states and network conditions. Afterward, the client submits the request with a video ID and its bitrate to the CDN node and promotes a new round of interaction. The number of videos in the queue and the bitrate levels for each of them is determined by the underlying streaming platform. Here we adopt the same settings used in MMGC2022, which comprises five videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update

**[Entrenamiento / optimización | extracto 15 | p.3]**

nd its bitrate to the CDN node and promotes a new round of interaction. The number of videos in the queue and the bitrate levels for each of them is determined by the underlying streaming platform. Here we adopt the same settings used in MMGC2022, which comprises five videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update for Incendio but also avoids it from converging to sub-optimal policies. conv2D 4x5x64 4x5x16 4x5x4 1x80 1x144 1x5 1x64 GRU 1x64 1x6 bm ta conv2D conv2D Flatten Fc 4x5x1  tb  ju  jl jg Fc Figure 3: The NN architecture of Incendio’s BM-agent. This section first introduces the input states, actions, and neural networks of Incendio’s agents, which remain consistent across the pre-train and fine-tune training stages. Then the training algorithms for pre-training and fine-tuning are elaborated. 4.

**[Entrenamiento / optimización | extracto 16 | p.3]**

next chunk for this video to download based on video states and network conditions. Afterward, the client submits the request with a video ID and its bitrate to the CDN node and promotes a new round of interaction. The number of videos in the queue and the bitrate levels for each of them is determined by the underlying streaming platform. Here we adopt the same settings used in MMGC2022, which comprises five videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update for Incendio but also avoids it from converging to sub-optimal policies. conv2D 4x5x64 4x5x16 4x5x4 1x80 1x144 1x5 1x64 GRU 1x64 1x6 bm ta conv2D conv2D Flatten Fc 4x5x1  tb  ju  jl jg Fc Figure 3: The NN architecture of Incendio’s BM-agent. This section first introduces the input states, actions, and neural networks of Incendio’s agents, which rema

### 5.x Datos / trazas / datasets

**[Datos / trazas / datasets | extracto 1 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tang

**[Datos / trazas / datasets | extracto 2 | p.2]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Y. Li et al. … Video queue Incendio’s SABR policy CDN Node client BM agent video ID, bitrate played playing downloaded to be downloaded State State State BA agent State video ID sleep time if video bitrate … sleep time Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user retention rate, video chunk size, and buffer status at each decision iteration. on the probability of every combination of the atomic actions. Dur- ing the training of DAM, it suffers from a slow convergence rate (and thus an extremely-long time duration) to the global optimality which is attributed to the search in large discrete action space that is closely related to the number of videos in the queu

**[Datos / trazas / datasets | extracto 3 | p.3]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Environment imitation learning hand-crafted model expert model reinforcement learning optimal Incendio ta ˆta IL L ts ts ta ts ta GAE tA ta RL L Figure 2: Two-stage training of Incendio: it is first initiated by imitating the hand-crafted model and then fine-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue starts to play, an

**[Datos / trazas / datasets | extracto 4 | p.4]**

ward function which could be formulated as follows: 𝑟𝑡= 𝑤𝑛· 𝑙𝑛· (𝑅𝑛−𝑆𝑛) −𝜇· 𝑇𝑛−𝜈· 𝑏𝑤𝑛, (6) where 𝑙𝑛is the conditional probability as defined in Equation (2). The idea behind this is that if the user retention rate of the next to-be-downloaded chunk is much lower than that of the current playing one, which means there is a high probability that the user will swipe away before playing the next chunk, and the agent will receive a lower reward. To get a higher reward, the agent will try to pause the download until the conditional probability increase, leading to less bandwidth wastage. 𝑤𝑛indicates whether the last downloaded chunk 𝑛will be watched by the user and is defined as follows: 𝑤𝑛= ( 0, if user will scroll to next video before chunk 𝑛 1, if user will watch chunk 𝑛. (7) In the training, 𝑤𝑛is sampled randomly in the user retention rate trace whenever a video is added to the video queue. During the evaluation, we still use Equation (1) to evaluate the performance. Training methodology. We use the clipped surrogate loss func- tion to train Incendio’s RL agents and additionally introduce the entropy of policy to avoid converging to sub-optimal policies at the 61

**[Datos / trazas / datasets | extracto 5 | p.4]**

rt policy directly determines the height that an agent can achieve via imitation learning. Inspired by a recent research on combining the learning-based method with a rules-based method to further improve the performance [19], we use the state-of-the-art hand-crafted method PDAS [21] to guide Incendio. As detailed in §2, PDAS integrates user retention rate to enhance the accuracy of QoE estimation, and employs MPC techniques to enable an optimal decision-making process by ex- haustively analyzing all potential future decision combinations, thus attaining good performance. In this work, we estimate the QoE of each possible action combination using the model designed by PDAS based on the real throughput over a horizon of future chunks and pick the largest one as the expert policy. Then we sepa- rate this expert policy into two subsets: the video ID trajectory and the bitrate trajectory, which are individually used to train Incen- dio’s two agents respectively. Please refer to PDAS for more details. Note that PDAS is mainly used to improve the efficiency of the exploration at the early stage of the training, and can be replaced by any other outstanding rule-based method. Loss function. Similar to traditional supervised learning where samples consist of feature-label pairs, imitation learning is charac- terized by the demonstration of state-action pairs. Therefore, the cross-entropy function, which is widely used in classification prob- lems, also applies here. The loss function of imitation learning for Incendio is described as follows: 𝐿𝐼𝐿= − ∑︁ 𝑡 ˆ𝐴𝑡log 𝜋𝜃(𝑠𝑡,𝑎𝑡), (4) where 𝜋𝜃(𝑠,𝑎) is the policy of the agent with parameter 𝜃. ˆ𝐴is the action probability list generated by expert

**[Datos / trazas / datasets | extracto 6 | p.5]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada 0 20 40 60 Score Video bitrate Rebuffering Smoothness Bandwidth wastage Average Value MPC+fixed-preload DAM PDAS Incendio (a) Average results (b) CDF results Figure 4: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under MMGC2022 video dataset and bandwidth trace dataset. The scores are normalized for the CDF results. 0 20 40 60 Score Video bitrate Rebuffering Smoothness Bandwidth wastage Average Value MPC+fixed-preload DAM PDAS Incendio (a) Average results (b) CDF results Figure 5: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under DUASVS video data set and Oboe/FCC bandwidth trace datasets. The utility scores are normalized for the CDF results. early stage of training. The loss function is formulated as follows: 𝐿𝑅𝐿= − ∑︁ 𝑡 ∑︁ 𝑘 min  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, clip  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, 1 −𝜖, 1 + 𝜖  𝐴𝐺𝐴𝐸 𝑡 + 𝛽 ∑︁ 𝑡 ∑︁ 𝑘 𝐻  𝜋𝜃  𝑠𝑘 𝑡  . (8) Here 𝐴𝐺𝐴𝐸 𝑡 is the advantage function computed using the GAE [10] method, which represents the difference in the expected reward when the agent deterministically picks action 𝑎𝑡in state 𝑠𝑡, com- par

**[Datos / trazas / datasets | extracto 7 | p.5]**

ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada 0 20 40 60 Score Video bitrate Rebuffering Smoothness Bandwidth wastage Average Value MPC+fixed-preload DAM PDAS Incendio (a) Average results (b) CDF results Figure 4: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under MMGC2022 video dataset and bandwidth trace dataset. The scores are normalized for the CDF results. 0 20 40 60 Score Video bitrate Rebuffering Smoothness Bandwidth wastage Average Value MPC+fixed-preload DAM PDAS Incendio (a) Average results (b) CDF results Figure 5: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under DUASVS video data set and Oboe/FCC bandwidth trace datasets. The utility scores are normalized for the CDF results. early stage of training. The loss function is formulated as follows: 𝐿𝑅𝐿= − ∑︁ 𝑡 ∑︁ 𝑘 min  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, clip  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, 1 −𝜖, 1 + 𝜖  𝐴𝐺𝐴𝐸 𝑡 + 𝛽 ∑︁ 𝑡 ∑︁ 𝑘 𝐻  𝜋𝜃  𝑠𝑘 𝑡  . (8) Here 𝐴𝐺𝐴𝐸 𝑡 is the advantage function computed using the GAE [10] method, which represents the difference in the expected reward when the agent deterministically picks action 𝑎𝑡in state 𝑠𝑡, com- pared with the expected reward for actions following the policy 𝜋𝜃with the policy parameters 𝜃. 𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡and 𝐻(·) represent the surrogate objective and policy entropy respectively. k indexes the agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term and we decay it when the reward does not increase for 100 epochs. The gradient update formula is similar to Equation (5) and more technical details with

**[Datos / trazas / datasets | extracto 8 | p.5]**

ge function computed using the GAE [10] method, which represents the difference in the expected reward when the agent deterministically picks action 𝑎𝑡in state 𝑠𝑡, com- pared with the expected reward for actions following the policy 𝜋𝜃with the policy parameters 𝜃. 𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡and 𝐻(·) represent the surrogate objective and policy entropy respectively. k indexes the agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term and we decay it when the reward does not increase for 100 epochs. The gradient update formula is similar to Equation (5) and more technical details with respect to the training algorithm can be found in [16]. 5 EVALUATION 5.1 Methodology To evaluate the performance of Incendio, we utilize the multi-video simulator provided in MMGC2022 to simulate various short video streaming sessions by randomly combining different video traces and network traces. As for video traces, each chunk size at different bitrates is recorded in a video size trace track, and corresponding user retention rates per chunk are contained in a user retention rate trace track. To train Incendio, we create a corpus of network traces by com- bining some public datasets including Oboe [1] and FCC [2]. As for video traces, we use the DUASVS [17] which contains millions of records including the video chunk statistics and users’ retention rates. Unless otherwise noted, we used a random sample of 80% of our corpus as a training set for Incendio and the remaining 20% as a testing set for all SABR algorithms. The same training set is also used to train DAM for a fair comparison. Since both network and video traces in MMGC2022 are relatively small, we only use this MMGC2022 dataset for evaluation. Note

**[Datos / trazas / datasets | extracto 9 | p.5]**

tively. k indexes the agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term and we decay it when the reward does not increase for 100 epochs. The gradient update formula is similar to Equation (5) and more technical details with respect to the training algorithm can be found in [16]. 5 EVALUATION 5.1 Methodology To evaluate the performance of Incendio, we utilize the multi-video simulator provided in MMGC2022 to simulate various short video streaming sessions by randomly combining different video traces and network traces. As for video traces, each chunk size at different bitrates is recorded in a video size trace track, and corresponding user retention rates per chunk are contained in a user retention rate trace track. To train Incendio, we create a corpus of network traces by com- bining some public datasets including Oboe [1] and FCC [2]. As for video traces, we use the DUASVS [17] which contains millions of records including the video chunk statistics and users’ retention rates. Unless otherwise noted, we used a random sample of 80% of our corpus as a training set for Incendio and the remaining 20% as a testing set for all SABR algorithms. The same training set is also used to train DAM for a fair comparison. Since both network and video traces in MMGC2022 are relatively small, we only use this MMGC2022 dataset for evaluation. Note that the network traces provided by MMGC2022 record bandwidth samples over time under high, medium, and low network conditions, respectively. We compare Incendio to the following schemes, which collec- tively represent the state-of-the-art methods: • MPC+fix-preload, combines a prevalent model-based ABR ap- proach (i.e., RobustMPC [15]),

**[Datos / trazas / datasets | extracto 10 | p.5]**

︁ 𝑘 min  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, clip  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, 1 −𝜖, 1 + 𝜖  𝐴𝐺𝐴𝐸 𝑡 + 𝛽 ∑︁ 𝑡 ∑︁ 𝑘 𝐻  𝜋𝜃  𝑠𝑘 𝑡  . (8) Here 𝐴𝐺𝐴𝐸 𝑡 is the advantage function computed using the GAE [10] method, which represents the difference in the expected reward when the agent deterministically picks action 𝑎𝑡in state 𝑠𝑡, com- pared with the expected reward for actions following the policy 𝜋𝜃with the policy parameters 𝜃. 𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡and 𝐻(·) represent the surrogate objective and policy entropy respectively. k indexes the agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term and we decay it when the reward does not increase for 100 epochs. The gradient update formula is similar to Equation (5) and more technical details with respect to the training algorithm can be found in [16]. 5 EVALUATION 5.1 Methodology To evaluate the performance of Incendio, we utilize the multi-video simulator provided in MMGC2022 to simulate various short video streaming sessions by randomly combining different video traces and network traces. As for video traces, each chunk size at different bitrates is recorded in a video size trace track, and corresponding user retention rates per chunk are contained in a user retention rate trace track. To train Incendio, we create a corpus of network traces by com- bining some public datasets including Oboe [1] and FCC [2]. As for video traces, we use the DUASVS [17] which contains millions of records including the video chunk statistics and users’ retention rates. Unless otherwise noted, we used a random sample of 80% of our corpus as a training set for Incendio and the remaining 20% as a testing set for all SABR algorithms. The same training set is also used to train DAM for a fair comparison

**[Datos / trazas / datasets | extracto 11 | p.6]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Y. Li et al. PDAS Figure 6: The training log of Incendio and DAM. DUASVS) and bandwidth datasets (MMGC2022 and Oboe/FCC). As clearly reported in Figure 4(a) and Figure 5(a), Incendio gains a clear leading position on the metric of both average score and some indi- vidual components (i.e., rebuffering, smoothness, and bandwidth wastage). Specifically, Incendio outperforms the state-of-the-art PDAS by 53.2% on the average utility score. Furthermore, Incendio achieves reduction of 39.1% - 61.8% on rebuffering and 34.9% - 59.2% on bandwidth wastage, which are remarkable improvements com- pared to other schemes. The results in the form of full CDF, shown in Figure 4(b) and Figure 5(b), further demonstrate the consistent performance of Incendio. As illustrated in Figure 4(a), PDAS outperforms MPC+fixed- preload for nearly all the metrics, indicating that it is a more ad- vanced variant of MPC. However, PDAS shows inferior performance to

**[Datos / trazas / datasets | extracto 12 | p.6]**

ng, smoothness, and bandwidth wastage). Specifically, Incendio outperforms the state-of-the-art PDAS by 53.2% on the average utility score. Furthermore, Incendio achieves reduction of 39.1% - 61.8% on rebuffering and 34.9% - 59.2% on bandwidth wastage, which are remarkable improvements com- pared to other schemes. The results in the form of full CDF, shown in Figure 4(b) and Figure 5(b), further demonstrate the consistent performance of Incendio. As illustrated in Figure 4(a), PDAS outperforms MPC+fixed- preload for nearly all the metrics, indicating that it is a more ad- vanced variant of MPC. However, PDAS shows inferior performance to DAM in bandwidth saving and managing bitrate fluctuation, sug- gesting that the max buffer model of PDAS is not well-designed. On the other hand, PDAS reports the worst performance using the DUASVS video data set under the Oboe/FCC network conditions, which reveals the poor generalization of PDAS. We believe that this is because the hyperparameters in PDAS fine-tuned using the MMGC2022 dataset are not able to characterize the network dy- namics of Oboe/FCC traces and the variation of user preference in the DUASVS video set. Interestingly, we find that DAM demonstrates unstable perfor- mance at different QoE ranges as visualized in Figure 4(b) and Fig- ure 5(b), reporting relatively higher performance within the high QoE range (> 0.8 approximately) but the noticeable lower perfor- mance in the low and intermediate QoE ranges (< 0.8) compared to other competitors. The reason is that DAM tends to discard certain actions to facilitate the exploration process due to the vast multi- dimensional exploratory space. Furthermore, we find evidence of the ab

**[Datos / trazas / datasets | extracto 13 | p.6]**

h are remarkable improvements com- pared to other schemes. The results in the form of full CDF, shown in Figure 4(b) and Figure 5(b), further demonstrate the consistent performance of Incendio. As illustrated in Figure 4(a), PDAS outperforms MPC+fixed- preload for nearly all the metrics, indicating that it is a more ad- vanced variant of MPC. However, PDAS shows inferior performance to DAM in bandwidth saving and managing bitrate fluctuation, sug- gesting that the max buffer model of PDAS is not well-designed. On the other hand, PDAS reports the worst performance using the DUASVS video data set under the Oboe/FCC network conditions, which reveals the poor generalization of PDAS. We believe that this is because the hyperparameters in PDAS fine-tuned using the MMGC2022 dataset are not able to characterize the network dy- namics of Oboe/FCC traces and the variation of user preference in the DUASVS video set. Interestingly, we find that DAM demonstrates unstable perfor- mance at different QoE ranges as visualized in Figure 4(b) and Fig- ure 5(b), reporting relatively higher performance within the high QoE range (> 0.8 approximately) but the noticeable lower perfor- mance in the low and intermediate QoE ranges (< 0.8) compared to other competitors. The reason is that DAM tends to discard certain actions to facilitate the exploration process due to the vast multi- dimensional exploratory space. Furthermore, we find evidence of the above analysis from the training log of DAM: it always chooses the middle-level bitrate for recommended video and never selects the lowest bitrate for the current playing video. The metric perfor- mance of DAM is also consistent with our findings, whereby

**[Datos / trazas / datasets | extracto 14 | p.6]**

width wastage). Specifically, Incendio outperforms the state-of-the-art PDAS by 53.2% on the average utility score. Furthermore, Incendio achieves reduction of 39.1% - 61.8% on rebuffering and 34.9% - 59.2% on bandwidth wastage, which are remarkable improvements com- pared to other schemes. The results in the form of full CDF, shown in Figure 4(b) and Figure 5(b), further demonstrate the consistent performance of Incendio. As illustrated in Figure 4(a), PDAS outperforms MPC+fixed- preload for nearly all the metrics, indicating that it is a more ad- vanced variant of MPC. However, PDAS shows inferior performance to DAM in bandwidth saving and managing bitrate fluctuation, sug- gesting that the max buffer model of PDAS is not well-designed. On the other hand, PDAS reports the worst performance using the DUASVS video data set under the Oboe/FCC network conditions, which reveals the poor generalization of PDAS. We believe that this is because the hyperparameters in PDAS fine-tuned using the MMGC2022 dataset are not able to characterize the network dy- namics of Oboe/FCC traces and the variation of user preference in the DUASVS video set. Interestingly, we find that DAM demonstrates unstable perfor- mance at different QoE ranges as visualized in Figure 4(b) and Fig- ure 5(b), reporting relatively higher performance within the high QoE range (> 0.8 approximately) but the noticeable lower perfor- mance in the low and intermediate QoE ranges (< 0.8) compared to other competitors. The reason is that DAM tends to discard certain actions to facilitate the exploration process due to the vast multi- dimensional exploratory space. Furthermore, we find evidence of the above analysis from t

**[Datos / trazas / datasets | extracto 15 | p.6]**

uffering, smoothness, and bandwidth wastage). Specifically, Incendio outperforms the state-of-the-art PDAS by 53.2% on the average utility score. Furthermore, Incendio achieves reduction of 39.1% - 61.8% on rebuffering and 34.9% - 59.2% on bandwidth wastage, which are remarkable improvements com- pared to other schemes. The results in the form of full CDF, shown in Figure 4(b) and Figure 5(b), further demonstrate the consistent performance of Incendio. As illustrated in Figure 4(a), PDAS outperforms MPC+fixed- preload for nearly all the metrics, indicating that it is a more ad- vanced variant of MPC. However, PDAS shows inferior performance to DAM in bandwidth saving and managing bitrate fluctuation, sug- gesting that the max buffer model of PDAS is not well-designed. On the other hand, PDAS reports the worst performance using the DUASVS video data set under the Oboe/FCC network conditions, which reveals the poor generalization of PDAS. We believe that this is because the hyperparameters in PDAS fine-tuned using the MMGC2022 dataset are not able to characterize the network dy- namics of Oboe/FCC traces and the variation of user preference in the DUASVS video set. Interestingly, we find that DAM demonstrates unstable perfor- mance at different QoE ranges as visualized in Figure 4(b) and Fig- ure 5(b), reporting relatively higher performance within the high QoE range (> 0.8 approximately) but the noticeable lower perfor- mance in the low and intermediate QoE ranges (< 0.8) compared to other competitors. The reason is that DAM tends to discard certain actions to facilitate the exploration process due to the vast multi- dimensional exploratory space. Furthermore, we find evidence

**[Datos / trazas / datasets | extracto 16 | p.7]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada REFERENCES [1] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe: Auto- Tuning Video ABR Algorithms to Network Conditions. In Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication (Budapest, Hungary) (SIGCOMM ’18). Association for Computing Machinery, New York, NY, USA, 44–58. https://doi.org/10.1145/3230543.3230558 [2] Federal Communications Commission. 2016. Raw Data - Measuring Broadband America 2016. Retrieved March 1, 2022 from https://www.fcc.gov/reports- research/reports/measuring-broadband-america/raw-data-measuring- broadband-america-2016 [3] Ting-Han Fan and Yubo Wang. 2022. Soft actor-critic with integer actions. In 2022 American Control Conference (ACC). IEEE, 2611–2616. [4] Jianchao He, Miao Hu, Yipeng Zhou, and Di Wu. 2020. LiveClip: Towards Intel- ligent Mobile Short-Form Video Streaming with Deep Reinforcement Learn- ing. In Proceedings of the 30th ACM Workshop on Network and Operating Systems Support for Digital Audio and Video (Istanbul, Turkey) (NOSSDAV ’20). Association for Computing Machinery, New York, NY, USA, 54–59. https: //doi.org/10.1145/3386290.3396937 [5] Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Xin Yao, and Lifeng Sun. 2019. Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learn- ing. In Proceedings of the 27th ACM Internation

### 5.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

ithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed

**[Evaluación / baselines / experimentos | extracto 2 | p.1]**

bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies a

**[Evaluación / baselines / experimentos | extracto 3 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are ine

**[Evaluación / baselines / experimentos | extracto 4 | p.1]**

itions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward function and a handcrafted buffer management model. However, rules-based ap- proaches are often criticized for their poor generalization to differ- ent environments since fixed control rules could not thoroughly characterize system behaviors for all scenarios in practice [1, 8]. Additionally, as PDAS is a variant of model predictive control (MPC [15]) that uses a greedy heuristic search for decision-making, its decision inference time grows exponentially as the length of the optimization horizon increases. Thus, RL-based approaches are introduced to overcome these issues through the use of neural networks to make a direct con- nection with environmental observation and action. For instance, DAM [9], an RL-based SABR method [3, 13], makes decisions for buffer management and bitrate adaptation simultaneously based 58

**[Evaluación / baselines / experimentos | extracto 5 | p.2]**

- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in

**[Evaluación / baselines / experimentos | extracto 6 | p.2]**

sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly

**[Evaluación / baselines / experimentos | extracto 7 | p.2]**

k, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming a

**[Evaluación / baselines / experimentos | extracto 8 | p.2]**

the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested in [22] which are consistent with the other methods for a fair comparison. Rule-based SABR approaches. APL [18] presented an adaptive preloading mechanism through the use of Lyapunov optimization to jointly maximize playback smoothness and minimize bandwidth waste. However, APL made a fixed bitrate assumption for short videos, which is impractical for real-world applications. PDAS [21] incorporates user retention rate1 for more accurate QoE prediction and utilizes MPC rules to facilitate decision-making by comparing all possible combinations of future actions, which has attained state- of-the-art performance (ranked first in MMGC2022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to deve

**[Evaluación / baselines / experimentos | extracto 9 | p.2]**

bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video stre

**[Evaluación / baselines / experimentos | extracto 10 | p.3]**

NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Environment imitation learning hand-crafted model expert model reinforcement learning optimal Incendio ta ˆta IL L ts ts ta ts ta GAE tA ta RL L Figure 2: Two-stage training of Incendio: it is first initiated by imitating the hand-crafted model and then fine-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue starts to play, and the downloaded but unplayed chunks for the previous video are cleared, resulting in a waste of bandwidth. In the meantime, a new video suggested by the video recommendation mechanism will be appended to the queue. The RL agent of Incendio consists of two hierarchical agents re- sponsible for buffer management (BM-agent) and bitrate adaption (BA-agent) respectively. For each decision iteration, the BM-agent chooses to sleep for a fixed duration or selects a video that needs the most buffering based on observations of past throughput mea- surements and the status for each video in the queue including user retention rate, remaining buffer size, average chunk size, rebuffer- ing time, and bitrate as well as its fluctuation of last downloaded chunk. If BM-agent makes a sleep decision, the client’s preloading process will be suspended for a predefined time duration. Otherwise, BM-agent decides which video to prefetch wi

**[Evaluación / baselines / experimentos | extracto 11 | p.3]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada Environment imitation learning hand-crafted model expert model reinforcement learning optimal Incendio ta ˆta IL L ts ts ta ts ta GAE tA ta RL L Figure 2: Two-stage training of Incendio: it is first initiated by imitating the hand-crafted model and then fine-tuned with reinforcement learning. is encoded into several bitrate versions and stored in a content delivery network (CDN) node. The client downloads video chunks from the CDN node purposely and maintains a local buffer for each short video in the video queue, including the current playing video and several recommended videos. Different videos are marked with different IDs. Every time when the user scrolls the screen, the second video in the queue st

**[Evaluación / baselines / experimentos | extracto 12 | p.4]**

(𝑅𝑛−𝑆𝑛) −𝜇· 𝑇𝑛−𝜈· 𝑏𝑤𝑛, (6) where 𝑙𝑛is the conditional probability as defined in Equation (2). The idea behind this is that if the user retention rate of the next to-be-downloaded chunk is much lower than that of the current playing one, which means there is a high probability that the user will swipe away before playing the next chunk, and the agent will receive a lower reward. To get a higher reward, the agent will try to pause the download until the conditional probability increase, leading to less bandwidth wastage. 𝑤𝑛indicates whether the last downloaded chunk 𝑛will be watched by the user and is defined as follows: 𝑤𝑛= ( 0, if user will scroll to next video before chunk 𝑛 1, if user will watch chunk 𝑛. (7) In the training, 𝑤𝑛is sampled randomly in the user retention rate trace whenever a video is added to the video queue. During the evaluation, we still use Equation (1) to evaluate the performance. Training methodology. We use the clipped surrogate loss func- tion to train Incendio’s RL agents and additionally introduce the entropy of policy to avoid converging to sub-optimal policies at the 61

**[Evaluación / baselines / experimentos | extracto 13 | p.4]**

output is then concatenated and passed through a fully connected layer with 64 units. Each layer of the network uses leaky-ReLU as the activation function. At the output layer, we use the Soft- Max activation function in a fully connected network to obtain a 6-dimension vector that represents the probabilities of choos- ing each action. For BA-agent’s actor network, we substitute the convolution layers with a fully connected layer, while keeping the remaining parts identical to the BM-agent. BM-agent and BA-agent share one critic network, which concatenates the last hidden layer of BM-agent’s actor network and that of BA-agent’s to output a tensor as value without activation function. This well-designed neural network enables Incendio to efficiently extract temporal and spatial features from observations and eventually achieve excellent performances. 4.2 Pre-train with IL Imitation learning is a type of machine learning where an agent learns to perform a task by observing trajectories produced by an expert and has proved to be effective in various fields, e.g., robotic, autonomous vehicles, and network streaming [5, 6, 20]. The reason we use imitation learning to pre-train Incendio is that it can reduce the amount of trial and error needed for an agent to learn a task, leading to faster convergence and more efficient learning. Expert policy. The quality of expert policy directly determines the height that an agent can achieve via imitation learning. Inspired by a recent research on combining the learning-based method with a rules-based method to further improve the performance [19], we use the state-of-the-art hand-crafted method PDAS [21] to guide Incendio. As detailed in §2, PDAS

**[Evaluación / baselines / experimentos | extracto 14 | p.4]**

t learns to perform a task by observing trajectories produced by an expert and has proved to be effective in various fields, e.g., robotic, autonomous vehicles, and network streaming [5, 6, 20]. The reason we use imitation learning to pre-train Incendio is that it can reduce the amount of trial and error needed for an agent to learn a task, leading to faster convergence and more efficient learning. Expert policy. The quality of expert policy directly determines the height that an agent can achieve via imitation learning. Inspired by a recent research on combining the learning-based method with a rules-based method to further improve the performance [19], we use the state-of-the-art hand-crafted method PDAS [21] to guide Incendio. As detailed in §2, PDAS integrates user retention rate to enhance the accuracy of QoE estimation, and employs MPC techniques to enable an optimal decision-making process by ex- haustively analyzing all potential future decision combinations, thus attaining good performance. In this work, we estimate the QoE of each possible action combination using the model designed by PDAS based on the real throughput over a horizon of future chunks and pick the largest one as the expert policy. Then we sepa- rate this expert policy into two subsets: the video ID trajectory and the bitrate trajectory, which are individually used to train Incen- dio’s two agents respectively. Please refer to PDAS for more details. Note that PDAS is mainly used to improve the efficiency of the exploration at the early stage of the training, and can be replaced by any other outstanding rule-based method. Loss function. Similar to traditional supervised learning where samples consist

**[Evaluación / baselines / experimentos | extracto 15 | p.5]**

sults. early stage of training. The loss function is formulated as follows: 𝐿𝑅𝐿= − ∑︁ 𝑡 ∑︁ 𝑘 min  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, clip  𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡, 1 −𝜖, 1 + 𝜖  𝐴𝐺𝐴𝐸 𝑡 + 𝛽 ∑︁ 𝑡 ∑︁ 𝑘 𝐻  𝜋𝜃  𝑠𝑘 𝑡  . (8) Here 𝐴𝐺𝐴𝐸 𝑡 is the advantage function computed using the GAE [10] method, which represents the difference in the expected reward when the agent deterministically picks action 𝑎𝑡in state 𝑠𝑡, com- pared with the expected reward for actions following the policy 𝜋𝜃with the policy parameters 𝜃. 𝑟𝑎𝑡𝑖𝑜𝑘 𝜃,𝑡and 𝐻(·) represent the surrogate objective and policy entropy respectively. k indexes the agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term and we decay it when the reward does not increase for 100 epochs. The gradient update formula is similar to Equation (5) and more technical details with respect to the training algorithm can be found in [16]. 5 EVALUATION 5.1 Methodology To evaluate the performance of Incendio, we utilize the multi-video simulator provided in MMGC2022 to simulate various short video streaming sessions by randomly combining different video traces and network traces. As for video traces, each chunk size at different bitrates is recorded in a video size trace track, and corresponding user retention rates per chunk are contained in a user retention rate trace track. To train Incendio, we create a corpus of network traces by com- bining some public datasets including Oboe [1] and FCC [2]. As for video traces, we use the DUASVS [17] which contains millions of records including the video chunk statistics and users’ retention rates. Unless otherwise noted, we used a random sample of 80% of our corpus as a training set for Incendio and the remaining 20% as a testing set for all SA

**[Evaluación / baselines / experimentos | extracto 16 | p.5]**

llions of records including the video chunk statistics and users’ retention rates. Unless otherwise noted, we used a random sample of 80% of our corpus as a training set for Incendio and the remaining 20% as a testing set for all SABR algorithms. The same training set is also used to train DAM for a fair comparison. Since both network and video traces in MMGC2022 are relatively small, we only use this MMGC2022 dataset for evaluation. Note that the network traces provided by MMGC2022 record bandwidth samples over time under high, medium, and low network conditions, respectively. We compare Incendio to the following schemes, which collec- tively represent the state-of-the-art methods: • MPC+fix-preload, combines a prevalent model-based ABR ap- proach (i.e., RobustMPC [15]), with the sleeping mechanism used in fix-preload [22], which is the baseline provided by MMGC2022. RobustMPC maximizes the accumulated utility score defined by Equation (1) over a horizon of 5 future chunks based on the buffer occupancy observations and throughput predictions. • DAM [9], a deep reinforcement learning-based approach, which trains a control policy to make the decision of video ID, bi- trate level, and pause/sleep time jointly using an action masking mechanism. It ranks first among all learning-based techniques in MMGC2022. We faithfully implement DAM following its paper. • PDAS [21], the state-of-the-art approach in MMGC2022 which optimizes the utility score by jointly utilizing user retention rate and a handcrafted buffer management model. PDAS employs RobustMPC to enable optimal decision-making. We faithfully implement PDAS following its paper. 5.2 Overall Results Figure 4 and Figure 5 demonstrat

### 5.x Limitaciones / riesgos / implementación

**[Limitaciones / riesgos / implementación | extracto 1 | p.1]**

ticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the au

**[Limitaciones / riesgos / implementación | extracto 2 | p.1]**

dth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinforcement Learning ACM Reference Format: Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma. 2023. Improving ABR Performance for Short Video Streaming Using Multi- Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of ∗Both authors contributed equally to this research. †Hao Chen is the corresponding author, chenhao1210@nju.edu.cn. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be h

**[Limitaciones / riesgos / implementación | extracto 3 | p.1]**

rcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by imitating the hand-crafted expert rules and then fine-tuned through the use of MARL. Results from extensive experiments indicate that Incendio outperforms the current state- of-the-art SABR algorithm with a 53.2% improvement measured by the utility score while maintaining low training complexity and inference time. CCS CONCEPTS • Information systems →Multimedia streaming. KEYWORDS Short video streaming, Adaptive bitrate, Reinfo

**[Limitaciones / riesgos / implementación | extracto 4 | p.1]**

Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance Yueheng Li∗ Nanjing University Nanjing, China Qianyuan Zheng∗ Nanjing University Nanjing, China Zicheng Zhang Nanjing University Nanjing, China Hao Chen† Nanjing University Nanjing, China Zhan Ma Nanjing University Nanjing, China ABSTRACT In the realm of short video streaming, popular adaptive bitrate (ABR) algorithms developed for classical long video applications suffer from catastrophic failures because they are tuned to solely adapt bitrates. Instead, short video adaptive bitrate (SABR) algo- rithms have to properly determine which video at which bitrate level together for content prefetching, without sacrificing the users’ qual- ity of experience (QoE) and yielding noticeable bandwidth wastage jointly. Unfortunately, existing SABR methods are inevitably en- tangled with slow convergence and poor generalization. Thus, in this paper, we propose Incendio, a novel SABR framework that applies Multi-Agent Reinforcement Learning (MARL) with Expert Guidance to separate the decision of video ID and video bitrate in respective buffer management and bitrate adaptation agents to maximize the system-level utilized score modeled as a compound function of QoE and bandwidth wastage metrics. To train Incendio, it is first initialized by im

**[Limitaciones / riesgos / implementación | extracto 5 | p.1]**

ears, there has been a significant surge in using short video streaming applications such as Kwai [7] and TikTok [14] for entertainment, social connection, etc, resulting in exponential traffic growth. Such a short video service largely differs from traditional long video streaming scenarios like video-on-demand (VoD), in which it allows the user to promptly switch to his/her interested content by just scrolling the touch screen. To this end, we often need to prefetch personalized content into the local buffer properly. Prefetching as many short videos as possible into the local buffer ensures the quality of experience (QoE) during consumption but often leads to significant bandwidth wastage. On the other hand, inadequate buffering may cause noticeable start-up delays when scrolling to the next one that is not yet cached. To tackle these challenges, content providers mainly resort to short video adaptive bitrate algorithms (SABR) for optimizing the user’s QoE and reducing bandwidth wastage simultaneously, for which the SABR algorithm needs to determine which video to download or remain idle and then identify which bitrate of this specific video to preload. To this end, network conditions, client buffer status, chunk sizes, as well as the users’ viewing prefer- ences can be jointly leveraged to make a proper decision. A short video streaming grand challenge was held in ACM Multimedia 2022 (MMGC2022 [22]) that attracted numerous competitive solutions. Both rules-based and reinforcement learning (RL) based SABR methods were developed. For example, PDAS [21], a typical rules- based approach, offers the leading performance in MMGC2022, in which it applies a probability-based reward fun

**[Limitaciones / riesgos / implementación | extracto 6 | p.2]**

mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimization objective. Unlike long video streaming applica- tions (e.g., VoD) that mainly focus on enhancing the user’s QoE, short video streaming has to consider QoE improvement and band- width efficiency (e.g., bandwidth wastage reduction) jointly. 𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖 = ∑︁ 𝑚 (𝑅𝑚−𝑆𝑚) − ∑︁ 𝑛 𝜇· 𝑇𝑛− ∑︁ 𝑛 𝜈· 𝑏𝑤𝑛. (1) As illustrated in Equation (1), the optimization objective of SABR involves not only the QoE model [1, 8, 15] but also a bandwidth usage penalty term, which is defined as the overall utility score [22]. 𝑚and 𝑛represent the index of played and downloaded chunks of video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively represent the rebuffering time and bandwidth usage caused by downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as suggested i

**[Limitaciones / riesgos / implementación | extracto 7 | p.2]**

022). Nevertheless, PDAS’s hyperparameters are highly context-dependent, making the model hardly generalizable to various conditions with different user preferences and networks (refer to §5.2 for further elaboration). Learning-based approaches have demonstrated their superi- ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em- ploys reinforcement learning to anticipate video switch events and dynamically modify preload orders, while overlooking the issues of bitrate adaptation and bandwidth conservation. DUASVS [17] utilizes integrated learning to develop a control policy for both decisions of prefetch threshold and video bitrate. DAM [9] achieves superior performance (ranked first among all learning-based tech- niques in MMGC2022) by incorporating the user retention rate into the reward function and minimizing training complexity through the utilization of action masks. However, the aforemen- tioned learning-based approaches suffer from slow convergence in training, given a large discrete action space in SABR tasks which is derived by multidimensional decisions of whether to sleep or not, the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for further elaboration). 3 SYSTEM OVERVIEW The system architecture of Incendio is illustrated in Figure 1. Each short video is sliced into chunks with a length of 1s. Each chunk 1User retention rate indicates the percentage of the users that choose to continue the watching of current video by statistics, which can be provided by content providers at the granularity of chunk. 59

**[Limitaciones / riesgos / implementación | extracto 8 | p.2]**

ncendio, yet another novel SABR framework, to address the aforementioned issues in existing approaches for joint optimization of QoE and bandwidth efficiency. We separate the decision of respective buffer management and bitrate adaption in a sequential manner, i.e., sub-task decomposi- tion, to which the hierarchical multi-agent reinforcement learning (MARL) is devised to simultaneously train them to optimize a com- pound reward. This greatly reduces the action space for optimality search, accelerating neural network training with a much faster con- vergence rate. On the other hand, instead of executing the MARL from the scratch, we propose imitation learning to pre-train In- cendio from a rudimentary state to an expert state by leveraging human experience, which further reduces the number of invalid trials in MARL and also mitigates the risk of sub-optimality. We evaluate the performance of Incendio by comparing it against state-of-the-art algorithms including PDAS [21], MPC [15], and DAM [9], under various network and users’ preference conditions (as detailed in §5.1). Our results indicate that Incendio consistently outperforms the existing algorithms across all scenarios. On aver- age, Incendio exhibits a 53.2% improvement to the award-winning PDAS under the measurement of overall utility score (as reported in §5.2), while maintaining exceptional training efficiency (as reported in §5.3) and feasibility of deployment (as reported in §5.4). 2 BACKGROUNDS AND RELATED WORKS This section commences by first briefing the optimization objective function well-accepted in the context of the SABR problem. Then, we review existing SABR algorithms and discuss their limitations. Optimi

**[Limitaciones / riesgos / implementación | extracto 9 | p.3]**

well as its fluctuation of last downloaded chunk. If BM-agent makes a sleep decision, the client’s preloading process will be suspended for a predefined time duration. Otherwise, BM-agent decides which video to prefetch with a video ID. Subse- quently, BA-agent determines the bitrate of the next chunk for this video to download based on video states and network conditions. Afterward, the client submits the request with a video ID and its bitrate to the CDN node and promotes a new round of interaction. The number of videos in the queue and the bitrate levels for each of them is determined by the underlying streaming platform. Here we adopt the same settings used in MMGC2022, which comprises five videos in the queue and three bitrate levels for each of them. Once the offline training is completed, the Incendio policy remains fixed for task inference. We detail the agent design and training method of Incendio in the following section. 4 INCENDIO DESIGN As depicted in Figure 2, Incendio’s training process comprises of two stages. In the first stage, we pre-train the Incendio’s two agents individually by imitating a hand-crafted expert policy, which pre- vents them from massive inefficient explorations in the early train- ing. Subsequently, Incendio’s policy is further fine-tuned using multi-agent reinforcement learning (MARL) until converging to a global optimum. Notably, Incendio utilizes a centralized training and decentralized execution (CTDE) approach to train Incendio’s two agents, in which they collaborate to attain a shared reward objective. This training strategy not only facilitates the efficient policy update for Incendio but also avoids it from converging to sub-optimal pol

**[Limitaciones / riesgos / implementación | extracto 10 | p.5]**

Oboe [1] and FCC [2]. As for video traces, we use the DUASVS [17] which contains millions of records including the video chunk statistics and users’ retention rates. Unless otherwise noted, we used a random sample of 80% of our corpus as a training set for Incendio and the remaining 20% as a testing set for all SABR algorithms. The same training set is also used to train DAM for a fair comparison. Since both network and video traces in MMGC2022 are relatively small, we only use this MMGC2022 dataset for evaluation. Note that the network traces provided by MMGC2022 record bandwidth samples over time under high, medium, and low network conditions, respectively. We compare Incendio to the following schemes, which collec- tively represent the state-of-the-art methods: • MPC+fix-preload, combines a prevalent model-based ABR ap- proach (i.e., RobustMPC [15]), with the sleeping mechanism used in fix-preload [22], which is the baseline provided by MMGC2022. RobustMPC maximizes the accumulated utility score defined by Equation (1) over a horizon of 5 future chunks based on the buffer occupancy observations and throughput predictions. • DAM [9], a deep reinforcement learning-based approach, which trains a control policy to make the decision of video ID, bi- trate level, and pause/sleep time jointly using an action masking mechanism. It ranks first among all learning-based techniques in MMGC2022. We faithfully implement DAM following its paper. • PDAS [21], the state-of-the-art approach in MMGC2022 which optimizes the utility score by jointly utilizing user retention rate and a handcrafted buffer management model. PDAS employs RobustMPC to enable optimal decision-making. We faithfully im

**[Limitaciones / riesgos / implementación | extracto 11 | p.6]**

ing and takes a long convergence time duration to the final policy. That’s because DAM encounters a significant challenge due to the substantial exploration Table 1: The inference time for Incendio and existing SABR algorithms in two different environments. Time is measured by milliseconds. MPC+fixed-preload DAM PDAS Incendio E1 0.6 0.4 7.1 1.0 E2 11.8 0.4 318.1 1.1 space generated by all possible combinations of atomic actions. In contrast, Incendio demonstrates the ability to learn an expert-level policy within a significantly shorter duration of 4k epochs via imitation learning. Furthermore, our proposed two-stage training framework enables Incendio to make substantial progress during the reinforcement learning phase. These results demonstrate the efficiency and significance of our training approach. 5.4 Inference Time To evaluate the complexity of Incendio, we record its runtime in the inference phase and compare it with that using MPC+fix-preload, DAM, and PDAS. We set two different environments for evalua- tion. In the environment 𝐸1, we keep the same setting as in the MMGC2022 competition, while the numbers of videos and bitrate levels are slightly increased to 7 and 6 respectively in the 𝐸2. The experiments are conducted on a desktop equipped with an Intel(R) Core(TM) i5-12500@3.00GHz CPU and repeated thousands of times. Table 1 lists the average inference times for MPC+fix-preload, DAM, PDAS, and Incendio. As shown, the computation complexity of MPC+fix-preload and PDAS grows exponentially as the numbers of videos in the queue and bitrate levels increase, which is unaccept- able for mobile devices. This is because these two MPC-based SABR algorithms make decisions by co

**[Limitaciones / riesgos / implementación | extracto 12 | p.6]**

two-stage training framework enables Incendio to make substantial progress during the reinforcement learning phase. These results demonstrate the efficiency and significance of our training approach. 5.4 Inference Time To evaluate the complexity of Incendio, we record its runtime in the inference phase and compare it with that using MPC+fix-preload, DAM, and PDAS. We set two different environments for evalua- tion. In the environment 𝐸1, we keep the same setting as in the MMGC2022 competition, while the numbers of videos and bitrate levels are slightly increased to 7 and 6 respectively in the 𝐸2. The experiments are conducted on a desktop equipped with an Intel(R) Core(TM) i5-12500@3.00GHz CPU and repeated thousands of times. Table 1 lists the average inference times for MPC+fix-preload, DAM, PDAS, and Incendio. As shown, the computation complexity of MPC+fix-preload and PDAS grows exponentially as the numbers of videos in the queue and bitrate levels increase, which is unaccept- able for mobile devices. This is because these two MPC-based SABR algorithms make decisions by comparing the expected rewards of all possible combinations of future actions, which limits its applica- tion in scenarios with large action space. On the contrary, Incendio maintains a lightweight computational complexity in these envi- ronments, which rivals DAM at the same order of magnitude but provides superior SABR performance (§5.2) and higher training efficiency (§5.3). 6 CONCLUSION We proposed and evaluated Incendio, a novel ABR framework for short video streaming using multi-agent reinforcement learning with expert guidance, with which we separate the decision of buffer management (e.g., video prefetchi

**[Limitaciones / riesgos / implementación | extracto 13 | p.6]**

tes the ability to learn an expert-level policy within a significantly shorter duration of 4k epochs via imitation learning. Furthermore, our proposed two-stage training framework enables Incendio to make substantial progress during the reinforcement learning phase. These results demonstrate the efficiency and significance of our training approach. 5.4 Inference Time To evaluate the complexity of Incendio, we record its runtime in the inference phase and compare it with that using MPC+fix-preload, DAM, and PDAS. We set two different environments for evalua- tion. In the environment 𝐸1, we keep the same setting as in the MMGC2022 competition, while the numbers of videos and bitrate levels are slightly increased to 7 and 6 respectively in the 𝐸2. The experiments are conducted on a desktop equipped with an Intel(R) Core(TM) i5-12500@3.00GHz CPU and repeated thousands of times. Table 1 lists the average inference times for MPC+fix-preload, DAM, PDAS, and Incendio. As shown, the computation complexity of MPC+fix-preload and PDAS grows exponentially as the numbers of videos in the queue and bitrate levels increase, which is unaccept- able for mobile devices. This is because these two MPC-based SABR algorithms make decisions by comparing the expected rewards of all possible combinations of future actions, which limits its applica- tion in scenarios with large action space. On the contrary, Incendio maintains a lightweight computational complexity in these envi- ronments, which rivals DAM at the same order of magnitude but provides superior SABR performance (§5.2) and higher training efficiency (§5.3). 6 CONCLUSION We proposed and evaluated Incendio, a novel ABR framework for short

**[Limitaciones / riesgos / implementación | extracto 14 | p.6]**

pace. Furthermore, we find evidence of the above analysis from the training log of DAM: it always chooses the middle-level bitrate for recommended video and never selects the lowest bitrate for the current playing video. The metric perfor- mance of DAM is also consistent with our findings, whereby being partially owed to choosing high-quality (high bitrate) chunks leads to higher probabilities of rebuffering. 5.3 Training Efficiency We plot the training log of Incendio and DAM in Figure 6 to compare the training efficiency of our two-stage training approach and the centralized RL method of DAM. As shown, DAM falls into a sub- optimal policy at the early stage of the training and takes a long convergence time duration to the final policy. That’s because DAM encounters a significant challenge due to the substantial exploration Table 1: The inference time for Incendio and existing SABR algorithms in two different environments. Time is measured by milliseconds. MPC+fixed-preload DAM PDAS Incendio E1 0.6 0.4 7.1 1.0 E2 11.8 0.4 318.1 1.1 space generated by all possible combinations of atomic actions. In contrast, Incendio demonstrates the ability to learn an expert-level policy within a significantly shorter duration of 4k epochs via imitation learning. Furthermore, our proposed two-stage training framework enables Incendio to make substantial progress during the reinforcement learning phase. These results demonstrate the efficiency and significance of our training approach. 5.4 Inference Time To evaluate the complexity of Incendio, we record its runtime in the inference phase and compare it with that using MPC+fix-preload, DAM, and PDAS. We set two different environments for evalua- t

**[Limitaciones / riesgos / implementación | extracto 15 | p.6]**

rms the state-of-the-art PDAS by 53.2% on the average utility score. Furthermore, Incendio achieves reduction of 39.1% - 61.8% on rebuffering and 34.9% - 59.2% on bandwidth wastage, which are remarkable improvements com- pared to other schemes. The results in the form of full CDF, shown in Figure 4(b) and Figure 5(b), further demonstrate the consistent performance of Incendio. As illustrated in Figure 4(a), PDAS outperforms MPC+fixed- preload for nearly all the metrics, indicating that it is a more ad- vanced variant of MPC. However, PDAS shows inferior performance to DAM in bandwidth saving and managing bitrate fluctuation, sug- gesting that the max buffer model of PDAS is not well-designed. On the other hand, PDAS reports the worst performance using the DUASVS video data set under the Oboe/FCC network conditions, which reveals the poor generalization of PDAS. We believe that this is because the hyperparameters in PDAS fine-tuned using the MMGC2022 dataset are not able to characterize the network dy- namics of Oboe/FCC traces and the variation of user preference in the DUASVS video set. Interestingly, we find that DAM demonstrates unstable perfor- mance at different QoE ranges as visualized in Figure 4(b) and Fig- ure 5(b), reporting relatively higher performance within the high QoE range (> 0.8 approximately) but the noticeable lower perfor- mance in the low and intermediate QoE ranges (< 0.8) compared to other competitors. The reason is that DAM tends to discard certain actions to facilitate the exploration process due to the vast multi- dimensional exploratory space. Furthermore, we find evidence of the above analysis from the training log of DAM: it always chooses the middle-level

**[Limitaciones / riesgos / implementación | extracto 16 | p.6]**

n process due to the vast multi- dimensional exploratory space. Furthermore, we find evidence of the above analysis from the training log of DAM: it always chooses the middle-level bitrate for recommended video and never selects the lowest bitrate for the current playing video. The metric perfor- mance of DAM is also consistent with our findings, whereby being partially owed to choosing high-quality (high bitrate) chunks leads to higher probabilities of rebuffering. 5.3 Training Efficiency We plot the training log of Incendio and DAM in Figure 6 to compare the training efficiency of our two-stage training approach and the centralized RL method of DAM. As shown, DAM falls into a sub- optimal policy at the early stage of the training and takes a long convergence time duration to the final policy. That’s because DAM encounters a significant challenge due to the substantial exploration Table 1: The inference time for Incendio and existing SABR algorithms in two different environments. Time is measured by milliseconds. MPC+fixed-preload DAM PDAS Incendio E1 0.6 0.4 7.1 1.0 E2 11.8 0.4 318.1 1.1 space generated by all possible combinations of atomic actions. In contrast, Incendio demonstrates the ability to learn an expert-level policy within a significantly shorter duration of 4k epochs via imitation learning. Furthermore, our proposed two-stage training framework enables Incendio to make substantial progress during the reinforcement learning phase. These results demonstrate the efficiency and significance of our training approach. 5.4 Inference Time To evaluate the complexity of Incendio, we record its runtime in the inference phase and compare it with that using MPC+fix-preload, DAM,

## 6. Figuras / tablas / algoritmos / ecuaciones detectados por texto
- p.2: Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption
- p.2: Figure 1. Each
- p.3: Figure 2: Two-stage training of Incendio: it is first initiated by
- p.3: Figure 2, Incendio’s training process comprises of
- p.3: Figure 3: The NN architecture of Incendio’s BM-agent.
- p.4: Figure 3. To capture temporal features from
- p.5: Figure 4: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under
- p.5: Figure 5: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under
- p.5: Figure 4 and Figure 5 demonstrate the results of performance com-
- p.6: Figure 6: The training log of Incendio and DAM.
- p.6: Figure 4(a) and Figure 5(a), Incendio gains a clear
- p.6: Figure 4(b) and Figure 5(b), further demonstrate the consistent
- p.6: Figure 4(a), PDAS outperforms MPC+fixed-
- p.6: Figure 4(b) and Fig-
- p.6: Figure 6 to compare
- p.6: Table 1: The inference time for Incendio and existing SABR
- p.6: Table 1 lists the average inference times for MPC+fix-preload, DAM,

## 7. Líneas con posible contenido matemático/formal
- p.1: `video streaming applications such as Kwai [7] and TikTok [14] for`
- p.1: `(MMGC2022 [22]) that attracted numerous competitive solutions.`
- p.1: `methods were developed. For example, PDAS [21], a typical rules-`
- p.1: `characterize system behaviors for all scenarios in practice [1, 8].`
- p.1: `(MPC [15]) that uses a greedy heuristic search for decision-making,`
- p.1: `DAM [9], an RL-based SABR method [3, 13], makes decisions for`
- p.2: `state-of-the-art algorithms including PDAS [21], MPC [15], and`
- p.2: `DAM [9], under various network and users’ preference conditions`
- p.2: `involves not only the QoE model [1, 8, 15] but also a bandwidth`
- p.2: `usage penalty term, which is defined as the overall utility score [22].`
- p.2: `downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as`
- p.2: `suggested in [22] which are consistent with the other methods for`
- p.2: `Rule-based SABR approaches. APL [18] presented an adaptive`
- p.2: `videos, which is impractical for real-world applications. PDAS [21]`
- p.2: `ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em-`
- p.2: `of bitrate adaptation and bandwidth conservation. DUASVS [17]`
- p.2: `decisions of prefetch threshold and video bitrate. DAM [9] achieves`
- p.3: `{𝑏𝑡−𝐾+1, . . . ,𝑏𝑡}), each of which can be calculated by dividing the`
- p.3: `nents represent different types of factors for each video 𝑗∈[1, 5]`
- p.3: `= ( ®𝑏𝑡,𝑙𝑗,𝑔𝑗,𝑢𝑗,ℎ𝑗,𝑞𝑗, 𝑓𝑗). In this work, we set 𝐾= 5 empirically`
- p.3: `{750, 1200, 1850} kbps (same as MMGC2022), which correspond to`
- p.4: `autonomous vehicles, and network streaming [5, 6, 20]. The reason`
- p.4: `a rules-based method to further improve the performance [19], we`
- p.4: `use the state-of-the-art hand-crafted method PDAS [21] to guide`
- p.4: `policy gradient method [12] as the training strategy for both IL`
- p.4: `(MAPPO [16]) algorithm which is an effective improved version of`
- p.4: `PPO [11] designed for multi-agent tasks. At each interaction step,`
- p.5: `is the advantage function computed using the GAE [10]`
- p.5: `agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term`
- p.5: `in [16].`
- p.5: `bining some public datasets including Oboe [1] and FCC [2]. As for`
- p.5: `video traces, we use the DUASVS [17] which contains millions of`
- p.5: `proach (i.e., RobustMPC [15]), with the sleeping mechanism used`
- p.5: `in fix-preload [22], which is the baseline provided by MMGC2022.`
- p.5: `• DAM [9], a deep reinforcement learning-based approach, which`
- p.5: `• PDAS [21], the state-of-the-art approach in MMGC2022 which`
- p.7: `[1] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen,`
- p.7: `[2] Federal Communications Commission. 2016. Raw Data - Measuring Broadband`
- p.7: `[3] Ting-Han Fan and Yubo Wang. 2022. Soft actor-critic with integer actions. In`
- p.7: `[4] Jianchao He, Miao Hu, Yipeng Zhou, and Di Wu. 2020. LiveClip: Towards Intel-`
- p.7: `[5] Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Xin Yao, and Lifeng`
- p.7: `[6] Ahmed Hussein, Mohamed Medhat Gaber, Eyad Elyan, and Chrisina Jayne. 2017.`
- p.7: `[7] Kwai. 2022. Kwai. Retrieved June 16, 2022 from https://www.kwai.com`
- p.7: `[8] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural Adap-`
- p.7: `[9] Si-Ze Qian, Yuhong Xie, Zipeng Pan, Yuan Zhang, and Tao Lin. 2022. DAM: Deep`
- p.7: `[10] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel.`
- p.7: `[11] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.`
- p.7: `[12] Richard S Sutton, David McAllester, Satinder Singh, and Yishay Mansour. 1999.`
- p.7: `[13] Yunhao Tang and Shipra Agrawal. 2020. Discretizing continuous action space`
- p.7: `[14] TikTok. 2022. TikTok. Retrieved June 16, 2022 from https://www.tiktok.com`
- p.7: `[15] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A Control-`
- p.7: `[16] Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao, Yu Wang, Alexandre Bayen,`
- p.7: `[17] Guanghui Zhang, Jie Zhang, Ke Liu, Jing Guo, Jack Lee, Haibo Hu, and Vaneet`
- p.7: `[18] Haodan Zhang, Yixuan Ban, Xinggong Zhang, Zongming Guo, Zhimin Xu, Sheng-`
- p.7: `[19] Huanhuan Zhang, Anfu Zhou, Yuhan Hu, Chaoyue Li, Guangping Wang, Xinyu`
- p.7: `[20] Jiakai Zhang and Kyunghyun Cho. 2016. Query-Efficient Imitation Learning for`
- p.7: `[21] Chao Zhou, Yixuan Ban, Yangchao Zhao, Liang Guo, and Bing Yu. 2022. PDAS:`
- p.7: `[22] Xutong Zuo, Yishu Li, Mohan Xu, Wei Tsang Ooi, Jiangchuan Liu, Junchen`

## 8. Texto crudo completo por página

> Mantener este bloque para Codex si necesita comprobar contexto literal. Puede contener errores de orden por columnas del PDF. Para fórmulas exactas o tablas complejas, usar PDF original.


### Página 1

```text
Improving ABR Performance for Short Video Streaming Using
Multi-Agent Reinforcement Learning with Expert Guidance
Yueheng Li∗
Nanjing University
Nanjing, China
Qianyuan Zheng∗
Nanjing University
Nanjing, China
Zicheng Zhang
Nanjing University
Nanjing, China
Hao Chen†
Nanjing University
Nanjing, China
Zhan Ma
Nanjing University
Nanjing, China
ABSTRACT
In the realm of short video streaming, popular adaptive bitrate
(ABR) algorithms developed for classical long video applications
suffer from catastrophic failures because they are tuned to solely
adapt bitrates. Instead, short video adaptive bitrate (SABR) algo-
rithms have to properly determine which video at which bitrate level
together for content prefetching, without sacrificing the users’ qual-
ity of experience (QoE) and yielding noticeable bandwidth wastage
jointly. Unfortunately, existing SABR methods are inevitably en-
tangled with slow convergence and poor generalization. Thus, in
this paper, we propose Incendio, a novel SABR framework that
applies Multi-Agent Reinforcement Learning (MARL) with Expert
Guidance to separate the decision of video ID and video bitrate
in respective buffer management and bitrate adaptation agents to
maximize the system-level utilized score modeled as a compound
function of QoE and bandwidth wastage metrics. To train Incendio,
it is first initialized by imitating the hand-crafted expert rules and
then fine-tuned through the use of MARL. Results from extensive
experiments indicate that Incendio outperforms the current state-
of-the-art SABR algorithm with a 53.2% improvement measured
by the utility score while maintaining low training complexity and
inference time.
CCS CONCEPTS
• Information systems →Multimedia streaming.
KEYWORDS
Short video streaming, Adaptive bitrate, Reinforcement Learning
ACM Reference Format:
Yueheng Li, Qianyuan Zheng, Zicheng Zhang, Hao Chen, and Zhan Ma.
2023. Improving ABR Performance for Short Video Streaming Using Multi-
Agent Reinforcement Learning with Expert Guidance. In The 33rd edition of
∗Both authors contributed equally to this research.
†Hao Chen is the corresponding author, chenhao1210@nju.edu.cn.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0184-9/23/06...$15.00
https://doi.org/10.1145/3592473.3592564
the Workshop on Network and Operating System Support for Digital Audio
and Video (NOSSDAV ’23), June 7–10, 2023, Vancouver, BC, Canada. ACM,
New York, NY, USA, 7 pages. https://doi.org/10.1145/3592473.3592564
1
INTRODUCTION
In recent years, there has been a significant surge in using short
video streaming applications such as Kwai [7] and TikTok [14] for
entertainment, social connection, etc, resulting in exponential traffic
growth. Such a short video service largely differs from traditional
long video streaming scenarios like video-on-demand (VoD), in
which it allows the user to promptly switch to his/her interested
content by just scrolling the touch screen. To this end, we often
need to prefetch personalized content into the local buffer properly.
Prefetching as many short videos as possible into the local buffer
ensures the quality of experience (QoE) during consumption but
often leads to significant bandwidth wastage. On the other hand,
inadequate buffering may cause noticeable start-up delays when
scrolling to the next one that is not yet cached.
To tackle these challenges, content providers mainly resort to
short video adaptive bitrate algorithms (SABR) for optimizing the
user’s QoE and reducing bandwidth wastage simultaneously, for
which the SABR algorithm needs to determine which video to
download or remain idle and then identify which bitrate of this
specific video to preload. To this end, network conditions, client
buffer status, chunk sizes, as well as the users’ viewing prefer-
ences can be jointly leveraged to make a proper decision. A short
video streaming grand challenge was held in ACM Multimedia 2022
(MMGC2022 [22]) that attracted numerous competitive solutions.
Both rules-based and reinforcement learning (RL) based SABR
methods were developed. For example, PDAS [21], a typical rules-
based approach, offers the leading performance in MMGC2022,
in which it applies a probability-based reward function and a
handcrafted buffer management model. However, rules-based ap-
proaches are often criticized for their poor generalization to differ-
ent environments since fixed control rules could not thoroughly
characterize system behaviors for all scenarios in practice [1, 8].
Additionally, as PDAS is a variant of model predictive control
(MPC [15]) that uses a greedy heuristic search for decision-making,
its decision inference time grows exponentially as the length of the
optimization horizon increases.
Thus, RL-based approaches are introduced to overcome these
issues through the use of neural networks to make a direct con-
nection with environmental observation and action. For instance,
DAM [9], an RL-based SABR method [3, 13], makes decisions for
buffer management and bitrate adaptation simultaneously based
58
```

### Página 2

```text
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
Y. Li et al.
…
Video queue
Incendio’s SABR policy
CDN Node
client
BM agent
video ID, bitrate
played
playing
downloaded
to be downloaded
State
State
State
BA agent
State
video ID
sleep
time
if
video
bitrate
…
sleep time
Figure 1: Incendio uses two hierarchical agents which are responsible for buffer management (BM-agent) and bitrate adaption
(BA-agent) respectively. They make their decisions based on the observations including past throughput measurements, user
retention rate, video chunk size, and buffer status at each decision iteration.
on the probability of every combination of the atomic actions. Dur-
ing the training of DAM, it suffers from a slow convergence rate
(and thus an extremely-long time duration) to the global optimality
which is attributed to the search in large discrete action space that
is closely related to the number of videos in the queue and the total
bitrate levels for each video.
This paper, therefore, proposes the Incendio, yet another novel
SABR framework, to address the aforementioned issues in existing
approaches for joint optimization of QoE and bandwidth efficiency.
We separate the decision of respective buffer management and
bitrate adaption in a sequential manner, i.e., sub-task decomposi-
tion, to which the hierarchical multi-agent reinforcement learning
(MARL) is devised to simultaneously train them to optimize a com-
pound reward. This greatly reduces the action space for optimality
search, accelerating neural network training with a much faster con-
vergence rate. On the other hand, instead of executing the MARL
from the scratch, we propose imitation learning to pre-train In-
cendio from a rudimentary state to an expert state by leveraging
human experience, which further reduces the number of invalid
trials in MARL and also mitigates the risk of sub-optimality.
We evaluate the performance of Incendio by comparing it against
state-of-the-art algorithms including PDAS [21], MPC [15], and
DAM [9], under various network and users’ preference conditions
(as detailed in §5.1). Our results indicate that Incendio consistently
outperforms the existing algorithms across all scenarios. On aver-
age, Incendio exhibits a 53.2% improvement to the award-winning
PDAS under the measurement of overall utility score (as reported in
§5.2), while maintaining exceptional training efficiency (as reported
in §5.3) and feasibility of deployment (as reported in §5.4).
2
BACKGROUNDS AND RELATED WORKS
This section commences by first briefing the optimization objective
function well-accepted in the context of the SABR problem. Then,
we review existing SABR algorithms and discuss their limitations.
Optimization objective. Unlike long video streaming applica-
tions (e.g., VoD) that mainly focus on enhancing the user’s QoE,
short video streaming has to consider QoE improvement and band-
width efficiency (e.g., bandwidth wastage reduction) jointly.
𝑈𝑖= 𝑄𝑜𝐸𝑖−𝐵𝑎𝑛𝑑𝑤𝑖𝑑𝑡ℎ𝑖
=
∑︁
𝑚
(𝑅𝑚−𝑆𝑚) −
∑︁
𝑛
𝜇· 𝑇𝑛−
∑︁
𝑛
𝜈· 𝑏𝑤𝑛.
(1)
As illustrated in Equation (1), the optimization objective of SABR
involves not only the QoE model [1, 8, 15] but also a bandwidth
usage penalty term, which is defined as the overall utility score [22].
𝑚and 𝑛represent the index of played and downloaded chunks of
video 𝑖. 𝑅𝑚and 𝑆𝑚respectively denote the quality (bitrate) and its
fluctuation for each played chunk 𝑚. And 𝑇𝑛and 𝑏𝑤𝑛respectively
represent the rebuffering time and bandwidth usage caused by
downloading chunk 𝑛. We set the coefficients 𝜇= 1.85,𝜈= 0.5 as
suggested in [22] which are consistent with the other methods for
a fair comparison.
Rule-based SABR approaches. APL [18] presented an adaptive
preloading mechanism through the use of Lyapunov optimization
to jointly maximize playback smoothness and minimize bandwidth
waste. However, APL made a fixed bitrate assumption for short
videos, which is impractical for real-world applications. PDAS [21]
incorporates user retention rate1 for more accurate QoE prediction
and utilizes MPC rules to facilitate decision-making by comparing
all possible combinations of future actions, which has attained state-
of-the-art performance (ranked first in MMGC2022). Nevertheless,
PDAS’s hyperparameters are highly context-dependent, making the
model hardly generalizable to various conditions with different user
preferences and networks (refer to §5.2 for further elaboration).
Learning-based approaches have demonstrated their superi-
ority in traditional ABR tasks [5, 8, 15]. For SABR, LiveClip [4] em-
ploys reinforcement learning to anticipate video switch events and
dynamically modify preload orders, while overlooking the issues
of bitrate adaptation and bandwidth conservation. DUASVS [17]
utilizes integrated learning to develop a control policy for both
decisions of prefetch threshold and video bitrate. DAM [9] achieves
superior performance (ranked first among all learning-based tech-
niques in MMGC2022) by incorporating the user retention rate
into the reward function and minimizing training complexity
through the utilization of action masks. However, the aforemen-
tioned learning-based approaches suffer from slow convergence in
training, given a large discrete action space in SABR tasks which is
derived by multidimensional decisions of whether to sleep or not,
the video ID (to-be-prefetched), and bitrate level (refer to §5.3 for
further elaboration).
3
SYSTEM OVERVIEW
The system architecture of Incendio is illustrated in Figure 1. Each
short video is sliced into chunks with a length of 1s. Each chunk
1User retention rate indicates the percentage of the users that choose to continue the
watching of current video by statistics, which can be provided by content providers at
the granularity of chunk.
59
```

### Página 3

```text
Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
Environment
imitation learning
hand-crafted
model
expert
model
reinforcement learning
optimal
Incendio
ta
ˆta
IL
L
ts
ts
ta
ts
ta
GAE
tA
ta
RL
L
Figure 2: Two-stage training of Incendio: it is first initiated by
imitating the hand-crafted model and then fine-tuned with
reinforcement learning.
is encoded into several bitrate versions and stored in a content
delivery network (CDN) node. The client downloads video chunks
from the CDN node purposely and maintains a local buffer for
each short video in the video queue, including the current playing
video and several recommended videos. Different videos are marked
with different IDs. Every time when the user scrolls the screen, the
second video in the queue starts to play, and the downloaded but
unplayed chunks for the previous video are cleared, resulting in a
waste of bandwidth. In the meantime, a new video suggested by the
video recommendation mechanism will be appended to the queue.
The RL agent of Incendio consists of two hierarchical agents re-
sponsible for buffer management (BM-agent) and bitrate adaption
(BA-agent) respectively. For each decision iteration, the BM-agent
chooses to sleep for a fixed duration or selects a video that needs
the most buffering based on observations of past throughput mea-
surements and the status for each video in the queue including user
retention rate, remaining buffer size, average chunk size, rebuffer-
ing time, and bitrate as well as its fluctuation of last downloaded
chunk. If BM-agent makes a sleep decision, the client’s preloading
process will be suspended for a predefined time duration. Otherwise,
BM-agent decides which video to prefetch with a video ID. Subse-
quently, BA-agent determines the bitrate of the next chunk for this
video to download based on video states and network conditions.
Afterward, the client submits the request with a video ID and its
bitrate to the CDN node and promotes a new round of interaction.
The number of videos in the queue and the bitrate levels for each
of them is determined by the underlying streaming platform. Here
we adopt the same settings used in MMGC2022, which comprises
five videos in the queue and three bitrate levels for each of them.
Once the offline training is completed, the Incendio policy remains
fixed for task inference. We detail the agent design and training
method of Incendio in the following section.
4
INCENDIO DESIGN
As depicted in Figure 2, Incendio’s training process comprises of
two stages. In the first stage, we pre-train the Incendio’s two agents
individually by imitating a hand-crafted expert policy, which pre-
vents them from massive inefficient explorations in the early train-
ing. Subsequently, Incendio’s policy is further fine-tuned using
multi-agent reinforcement learning (MARL) until converging to a
global optimum. Notably, Incendio utilizes a centralized training
and decentralized execution (CTDE) approach to train Incendio’s
two agents, in which they collaborate to attain a shared reward
objective. This training strategy not only facilitates the efficient
policy update for Incendio but also avoids it from converging to
sub-optimal policies.
conv2D
4x5x64
4x5x16
4x5x4
1x80
1x144
1x5
1x64
GRU
1x64
1x6
bm
ta
conv2D
conv2D
Flatten
Fc
4x5x1

tb

ju

jl
jg
Fc
Figure 3: The NN architecture of Incendio’s BM-agent.
This section first introduces the input states, actions, and neural
networks of Incendio’s agents, which remain consistent across the
pre-train and fine-tune training stages. Then the training algorithms
for pre-training and fine-tuning are elaborated.
4.1
Multi-agent Design
Incendio’s multi-agent takes an action 𝑎𝑡based on the observations
collected by clients as input state𝑠𝑡, according to its policy 𝜋𝜃(𝑠𝑡,𝑎𝑡)
which is represented by neural networks. This subsection expounds
on the specification of Incendio’s state, action, and neural network
design.
State. The state gathered by Incendio at step 𝑡is defined as
𝑠𝑡= ( ®𝑏𝑡, ®𝑙𝑗, ®𝑔𝑗, ®𝑢𝑗, ®ℎ𝑗, ®𝑞𝑗, ®𝑓𝑗). The first component is a vector of
throughput measurements observed in past 𝐾chunks (e.g., ®𝑏𝑡=
{𝑏𝑡−𝐾+1, . . . ,𝑏𝑡}), each of which can be calculated by dividing the
chunk size by the download duration. The remaining state compo-
nents represent different types of factors for each video 𝑗∈[1, 5]
in the queue. Specifically, 𝑙𝑗is the conditional probability that a
user will continue to watch the video 𝑗from the current playing
chunk 𝑚(for recommended video, 𝑚= 1) until the chunk 𝑛, which
can be calculated as follows:
𝑙𝑗=
𝑝𝑛
𝑗
𝑝𝑚
𝑗
,
(2)
where 𝑝𝑚
𝑗denotes the user retention rate of video 𝑗in chunk 𝑚by
statistical averaging; 𝑔𝑗represents the current buffer size for video
𝑗; 𝑢𝑗denotes the mean size of next chunks at different bitrates for
video 𝑗; ℎ𝑗is the rebuffering time caused by downloading the last
chunk for video 𝑗and is equal to 0 if no rebuffering occurred; and
𝑞𝑗and 𝑓𝑗respectively denote the bitrate and its fluctuation at which
the last chunk was downloaded for video 𝑗. The bitrate fluctuation
can be obtained by
𝑓𝑗=


𝑞𝑗−𝑞𝑗−1


.
(3)
The state for BM-agent is defined as 𝑠𝑏𝑚
𝑡
= ( ®𝑏𝑡, ®𝑙𝑗, ®𝑔𝑗, ®𝑢𝑗). And
the state for BA-agent to make the decision on video 𝑗is defined as
𝑠𝑏𝑎
𝑡
= ( ®𝑏𝑡,𝑙𝑗,𝑔𝑗,𝑢𝑗,ℎ𝑗,𝑞𝑗, 𝑓𝑗). In this work, we set 𝐾= 5 empirically
to capture the temporal features from past observations.
Action. The output action 𝑎𝑏𝑚
𝑡
of BM-agent is a 0-1 vector with
a length of 6. The first five values in this vector represent the
corresponding video ID, while the last value signifies sleep for a
fixed duration of 𝜏= 200𝑚𝑠. This setting is motivated by the need
to balance the trade-off between utilizing computing resources
optimally and not missing the ideal decision-making time. Simi-
larly, the BA-agent takes an action 𝑎𝑏𝑎
𝑡
from the bitrate ladders of
{750, 1200, 1850} kbps (same as MMGC2022), which correspond to
different video qualities.
60
```

### Página 4

```text
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
Y. Li et al.
Neural networks. Incendio employs the actor-critic framework
to represent its control policy. The actor network structure for the
BM-agent is depicted in Figure 3. To capture temporal features from
the past bandwidth, we adopt a gated recurrent unit (GRU) layer
with 64 units. Moreover, to extract spatial features between input
vectors, we use three 2-D convolutional network layers with kernel
sizes of 5x5 and output channels of 64, 16, and 4, respectively. The
output is then concatenated and passed through a fully connected
layer with 64 units. Each layer of the network uses leaky-ReLU
as the activation function. At the output layer, we use the Soft-
Max activation function in a fully connected network to obtain
a 6-dimension vector that represents the probabilities of choos-
ing each action. For BA-agent’s actor network, we substitute the
convolution layers with a fully connected layer, while keeping the
remaining parts identical to the BM-agent. BM-agent and BA-agent
share one critic network, which concatenates the last hidden layer
of BM-agent’s actor network and that of BA-agent’s to output a
tensor as value without activation function. This well-designed
neural network enables Incendio to efficiently extract temporal and
spatial features from observations and eventually achieve excellent
performances.
4.2
Pre-train with IL
Imitation learning is a type of machine learning where an agent
learns to perform a task by observing trajectories produced by an
expert and has proved to be effective in various fields, e.g., robotic,
autonomous vehicles, and network streaming [5, 6, 20]. The reason
we use imitation learning to pre-train Incendio is that it can reduce
the amount of trial and error needed for an agent to learn a task,
leading to faster convergence and more efficient learning.
Expert policy. The quality of expert policy directly determines
the height that an agent can achieve via imitation learning. Inspired
by a recent research on combining the learning-based method with
a rules-based method to further improve the performance [19], we
use the state-of-the-art hand-crafted method PDAS [21] to guide
Incendio. As detailed in §2, PDAS integrates user retention rate
to enhance the accuracy of QoE estimation, and employs MPC
techniques to enable an optimal decision-making process by ex-
haustively analyzing all potential future decision combinations,
thus attaining good performance. In this work, we estimate the
QoE of each possible action combination using the model designed
by PDAS based on the real throughput over a horizon of future
chunks and pick the largest one as the expert policy. Then we sepa-
rate this expert policy into two subsets: the video ID trajectory and
the bitrate trajectory, which are individually used to train Incen-
dio’s two agents respectively. Please refer to PDAS for more details.
Note that PDAS is mainly used to improve the efficiency of the
exploration at the early stage of the training, and can be replaced
by any other outstanding rule-based method.
Loss function. Similar to traditional supervised learning where
samples consist of feature-label pairs, imitation learning is charac-
terized by the demonstration of state-action pairs. Therefore, the
cross-entropy function, which is widely used in classification prob-
lems, also applies here. The loss function of imitation learning for
Incendio is described as follows:
𝐿𝐼𝐿= −
∑︁
𝑡
ˆ𝐴𝑡log 𝜋𝜃(𝑠𝑡,𝑎𝑡),
(4)
where 𝜋𝜃(𝑠,𝑎) is the policy of the agent with parameter 𝜃. ˆ𝐴is the
action probability list generated by expert policy, where the value
of expert action ˆ𝑎is equal to 1 and the others are 0. We use the
policy gradient method [12] as the training strategy for both IL
and RL. Its main idea is to estimate the gradients of the expected
total reward with respect to the policy parameter 𝜃, and update
the network parameters according to the gradients, which can be
written as follows:
𝑑𝜃←𝑑𝜃−𝛼
∑︁
𝑡
∇𝜃ˆ𝐴𝑡log 𝜋𝜃(𝑠𝑡,𝑎𝑡).
(5)
We set the learning rate 𝛼= 0.0001. The BM-agent and BA-agent
of Incendio are trained with the same loss function. We also intro-
duce a novel experience replay mechanism to improve the sample
utilization efficiency.
4.3
Fine-tune with RL
Incendio fine-tunes its SABR policy using a state-of-the-art
MARL framework, i.e., multi-agent proximal policy optimization
(MAPPO [16]) algorithm which is an effective improved version of
PPO [11] designed for multi-agent tasks. At each interaction step,
Incendio takes an action 𝑎𝑡including 𝑎𝑏𝑚
𝑡
and 𝑎𝑏𝑎
𝑡
according to its
policy 𝜋𝜃and the observations 𝑠𝑡. Then the environment transits
to a new state 𝑠𝑡+1 and returns a reward 𝑟𝑡which will be used to
update the NN parameters of both agents for Incendio. From the
perspective of one agent, changes brought about by another agent
will be regarded as environmental changes.
Reward. In a typical RL task, the agent learns the optimal policy
by maximizing the expected cumulative (discounted) reward that it
receives from the environment. Thus, we set the reward to reflect
the MMGC2022 utility score that is defined in Equation (1). Aiming
to maximize the expected cumulative discounted reward, Incendio’s
RL agents learn to get higher utility scores. To motivate Incendio
to learn a more bandwidth-efficient policy, we add a coefficient 𝑤𝑛
to the first term of the reward function which could be formulated
as follows:
𝑟𝑡= 𝑤𝑛· 𝑙𝑛· (𝑅𝑛−𝑆𝑛) −𝜇· 𝑇𝑛−𝜈· 𝑏𝑤𝑛,
(6)
where 𝑙𝑛is the conditional probability as defined in Equation (2).
The idea behind this is that if the user retention rate of the next
to-be-downloaded chunk is much lower than that of the current
playing one, which means there is a high probability that the user
will swipe away before playing the next chunk, and the agent will
receive a lower reward. To get a higher reward, the agent will try
to pause the download until the conditional probability increase,
leading to less bandwidth wastage. 𝑤𝑛indicates whether the last
downloaded chunk 𝑛will be watched by the user and is defined as
follows:
𝑤𝑛=
(
0,
if user will scroll to next video before chunk 𝑛
1,
if user will watch chunk 𝑛.
(7)
In the training, 𝑤𝑛is sampled randomly in the user retention rate
trace whenever a video is added to the video queue. During the
evaluation, we still use Equation (1) to evaluate the performance.
Training methodology. We use the clipped surrogate loss func-
tion to train Incendio’s RL agents and additionally introduce the
entropy of policy to avoid converging to sub-optimal policies at the
61
```

### Página 5

```text
Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
0
20
40
60
Score
Video bitrate
Rebuffering
Smoothness
Bandwidth wastage
Average Value
MPC+fixed-preload
DAM
PDAS
Incendio
(a) Average results
(b) CDF results
Figure 4: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under
MMGC2022 video dataset and bandwidth trace dataset. The scores are normalized for the CDF results.
0
20
40
60
Score
Video bitrate
Rebuffering
Smoothness
Bandwidth wastage
Average Value
MPC+fixed-preload
DAM
PDAS
Incendio
(a) Average results
(b) CDF results
Figure 5: Comparing Incendio with the other schemes in terms of the average performance and full CDF performance under
DUASVS video data set and Oboe/FCC bandwidth trace datasets. The utility scores are normalized for the CDF results.
early stage of training. The loss function is formulated as follows:
𝐿𝑅𝐿= −
∑︁
𝑡
∑︁
𝑘
min

𝑟𝑎𝑡𝑖𝑜𝑘
𝜃,𝑡, clip

𝑟𝑎𝑡𝑖𝑜𝑘
𝜃,𝑡, 1 −𝜖, 1 + 𝜖

𝐴𝐺𝐴𝐸
𝑡
+ 𝛽
∑︁
𝑡
∑︁
𝑘
𝐻

𝜋𝜃

𝑠𝑘
𝑡

.
(8)
Here 𝐴𝐺𝐴𝐸
𝑡
is the advantage function computed using the GAE [10]
method, which represents the difference in the expected reward
when the agent deterministically picks action 𝑎𝑡in state 𝑠𝑡, com-
pared with the expected reward for actions following the policy
𝜋𝜃with the policy parameters 𝜃. 𝑟𝑎𝑡𝑖𝑜𝑘
𝜃,𝑡and 𝐻(·) represent the
surrogate objective and policy entropy respectively. k indexes the
agents where 𝑘∈{𝑏𝑚,𝑏𝑎}. 𝛽is the weight of the entropy term
and we decay it when the reward does not increase for 100 epochs.
The gradient update formula is similar to Equation (5) and more
technical details with respect to the training algorithm can be found
in [16].
5
EVALUATION
5.1
Methodology
To evaluate the performance of Incendio, we utilize the multi-video
simulator provided in MMGC2022 to simulate various short video
streaming sessions by randomly combining different video traces
and network traces. As for video traces, each chunk size at different
bitrates is recorded in a video size trace track, and corresponding
user retention rates per chunk are contained in a user retention
rate trace track.
To train Incendio, we create a corpus of network traces by com-
bining some public datasets including Oboe [1] and FCC [2]. As for
video traces, we use the DUASVS [17] which contains millions of
records including the video chunk statistics and users’ retention
rates. Unless otherwise noted, we used a random sample of 80% of
our corpus as a training set for Incendio and the remaining 20% as
a testing set for all SABR algorithms. The same training set is also
used to train DAM for a fair comparison. Since both network and
video traces in MMGC2022 are relatively small, we only use this
MMGC2022 dataset for evaluation. Note that the network traces
provided by MMGC2022 record bandwidth samples over time under
high, medium, and low network conditions, respectively.
We compare Incendio to the following schemes, which collec-
tively represent the state-of-the-art methods:
• MPC+fix-preload, combines a prevalent model-based ABR ap-
proach (i.e., RobustMPC [15]), with the sleeping mechanism used
in fix-preload [22], which is the baseline provided by MMGC2022.
RobustMPC maximizes the accumulated utility score defined by
Equation (1) over a horizon of 5 future chunks based on the buffer
occupancy observations and throughput predictions.
• DAM [9], a deep reinforcement learning-based approach, which
trains a control policy to make the decision of video ID, bi-
trate level, and pause/sleep time jointly using an action masking
mechanism. It ranks first among all learning-based techniques in
MMGC2022. We faithfully implement DAM following its paper.
• PDAS [21], the state-of-the-art approach in MMGC2022 which
optimizes the utility score by jointly utilizing user retention rate
and a handcrafted buffer management model. PDAS employs
RobustMPC to enable optimal decision-making. We faithfully
implement PDAS following its paper.
5.2
Overall Results
Figure 4 and Figure 5 demonstrate the results of performance com-
parison between Incendio and other schemes in terms of average
utility score metrics and related full cumulative distribution func-
tion (CDF) under different short video datasets (MMGC2022 and
62
```

### Página 6

```text
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
Y. Li et al.
PDAS
Figure 6: The training log of Incendio and DAM.
DUASVS) and bandwidth datasets (MMGC2022 and Oboe/FCC). As
clearly reported in Figure 4(a) and Figure 5(a), Incendio gains a clear
leading position on the metric of both average score and some indi-
vidual components (i.e., rebuffering, smoothness, and bandwidth
wastage). Specifically, Incendio outperforms the state-of-the-art
PDAS by 53.2% on the average utility score. Furthermore, Incendio
achieves reduction of 39.1% - 61.8% on rebuffering and 34.9% - 59.2%
on bandwidth wastage, which are remarkable improvements com-
pared to other schemes. The results in the form of full CDF, shown
in Figure 4(b) and Figure 5(b), further demonstrate the consistent
performance of Incendio.
As illustrated in Figure 4(a), PDAS outperforms MPC+fixed-
preload for nearly all the metrics, indicating that it is a more ad-
vanced variant of MPC. However, PDAS shows inferior performance
to DAM in bandwidth saving and managing bitrate fluctuation, sug-
gesting that the max buffer model of PDAS is not well-designed.
On the other hand, PDAS reports the worst performance using the
DUASVS video data set under the Oboe/FCC network conditions,
which reveals the poor generalization of PDAS. We believe that
this is because the hyperparameters in PDAS fine-tuned using the
MMGC2022 dataset are not able to characterize the network dy-
namics of Oboe/FCC traces and the variation of user preference in
the DUASVS video set.
Interestingly, we find that DAM demonstrates unstable perfor-
mance at different QoE ranges as visualized in Figure 4(b) and Fig-
ure 5(b), reporting relatively higher performance within the high
QoE range (> 0.8 approximately) but the noticeable lower perfor-
mance in the low and intermediate QoE ranges (< 0.8) compared to
other competitors. The reason is that DAM tends to discard certain
actions to facilitate the exploration process due to the vast multi-
dimensional exploratory space. Furthermore, we find evidence of
the above analysis from the training log of DAM: it always chooses
the middle-level bitrate for recommended video and never selects
the lowest bitrate for the current playing video. The metric perfor-
mance of DAM is also consistent with our findings, whereby being
partially owed to choosing high-quality (high bitrate) chunks leads
to higher probabilities of rebuffering.
5.3
Training Efficiency
We plot the training log of Incendio and DAM in Figure 6 to compare
the training efficiency of our two-stage training approach and the
centralized RL method of DAM. As shown, DAM falls into a sub-
optimal policy at the early stage of the training and takes a long
convergence time duration to the final policy. That’s because DAM
encounters a significant challenge due to the substantial exploration
Table 1: The inference time for Incendio and existing SABR
algorithms in two different environments. Time is measured
by milliseconds.
MPC+fixed-preload
DAM
PDAS
Incendio
E1
0.6
0.4
7.1
1.0
E2
11.8
0.4
318.1
1.1
space generated by all possible combinations of atomic actions. In
contrast, Incendio demonstrates the ability to learn an expert-level
policy within a significantly shorter duration of 4k epochs via
imitation learning. Furthermore, our proposed two-stage training
framework enables Incendio to make substantial progress during
the reinforcement learning phase. These results demonstrate the
efficiency and significance of our training approach.
5.4
Inference Time
To evaluate the complexity of Incendio, we record its runtime in the
inference phase and compare it with that using MPC+fix-preload,
DAM, and PDAS. We set two different environments for evalua-
tion. In the environment 𝐸1, we keep the same setting as in the
MMGC2022 competition, while the numbers of videos and bitrate
levels are slightly increased to 7 and 6 respectively in the 𝐸2. The
experiments are conducted on a desktop equipped with an Intel(R)
Core(TM) i5-12500@3.00GHz CPU and repeated thousands of times.
Table 1 lists the average inference times for MPC+fix-preload, DAM,
PDAS, and Incendio. As shown, the computation complexity of
MPC+fix-preload and PDAS grows exponentially as the numbers of
videos in the queue and bitrate levels increase, which is unaccept-
able for mobile devices. This is because these two MPC-based SABR
algorithms make decisions by comparing the expected rewards of
all possible combinations of future actions, which limits its applica-
tion in scenarios with large action space. On the contrary, Incendio
maintains a lightweight computational complexity in these envi-
ronments, which rivals DAM at the same order of magnitude but
provides superior SABR performance (§5.2) and higher training
efficiency (§5.3).
6
CONCLUSION
We proposed and evaluated Incendio, a novel ABR framework for
short video streaming using multi-agent reinforcement learning
with expert guidance, with which we separate the decision of buffer
management (e.g., video prefetching) and bitrate adaptation in a
sequential manner to optimize the system-level utility score. As a
result, the training of Incendio is initiated with human expert policy
using imitation learning and then uses a much smaller action space
for policy fine-tuning, providing a much faster convergence rate
and exhibiting exceptional generalization abilities. Over a broad set
of testing conditions, we find the proposed Incendio provides more
than 2x performance improvement to the state-of-the-art scheme
when using the utility score measurement.
ACKNOWLEDGMENTS
This work is partially supported by National Natural Science Foun-
dation of China (62101241), Jiangsu Provincial Double-Innovation
Doctor Program (JSSCBS20210001), and ZTE Collaborative Re-
search fund.
63
```

### Página 7

```text
Improving ABR Performance for Short Video Streaming Using Multi-Agent Reinforcement Learning with Expert Guidance
NOSSDAV ’23, June 7–10, 2023, Vancouver, Canada
REFERENCES
[1] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen,
Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe: Auto-
Tuning Video ABR Algorithms to Network Conditions. In Proceedings of the
2018 Conference of the ACM Special Interest Group on Data Communication
(Budapest, Hungary) (SIGCOMM ’18). Association for Computing Machinery,
New York, NY, USA, 44–58. https://doi.org/10.1145/3230543.3230558
[2] Federal Communications Commission. 2016. Raw Data - Measuring Broadband
America 2016.
Retrieved March 1, 2022 from https://www.fcc.gov/reports-
research/reports/measuring-broadband-america/raw-data-measuring-
broadband-america-2016
[3] Ting-Han Fan and Yubo Wang. 2022. Soft actor-critic with integer actions. In
2022 American Control Conference (ACC). IEEE, 2611–2616.
[4] Jianchao He, Miao Hu, Yipeng Zhou, and Di Wu. 2020. LiveClip: Towards Intel-
ligent Mobile Short-Form Video Streaming with Deep Reinforcement Learn-
ing. In Proceedings of the 30th ACM Workshop on Network and Operating
Systems Support for Digital Audio and Video (Istanbul, Turkey) (NOSSDAV ’20).
Association for Computing Machinery, New York, NY, USA, 54–59.
https:
//doi.org/10.1145/3386290.3396937
[5] Tianchi Huang, Chao Zhou, Rui-Xiao Zhang, Chenglei Wu, Xin Yao, and Lifeng
Sun. 2019. Comyco: Quality-Aware Adaptive Video Streaming via Imitation Learn-
ing. In Proceedings of the 27th ACM International Conference on Multimedia
(Nice, France) (MM ’19). Association for Computing Machinery, New York, NY,
USA, 429–437. https://doi.org/10.1145/3343031.3351014
[6] Ahmed Hussein, Mohamed Medhat Gaber, Eyad Elyan, and Chrisina Jayne. 2017.
Imitation Learning: A Survey of Learning Methods. ACM Comput. Surv. 50, 2,
Article 21 (apr 2017), 35 pages. https://doi.org/10.1145/3054912
[7] Kwai. 2022. Kwai. Retrieved June 16, 2022 from https://www.kwai.com
[8] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural Adap-
tive Video Streaming with Pensieve. In Proceedings of the Conference of the
ACM Special Interest Group on Data Communication (Los Angeles, CA, USA)
(SIGCOMM ’17). Association for Computing Machinery, New York, NY, USA,
197–210. https://doi.org/10.1145/3098822.3098843
[9] Si-Ze Qian, Yuhong Xie, Zipeng Pan, Yuan Zhang, and Tao Lin. 2022. DAM: Deep
Reinforcement Learning Based Preload Algorithm with Action Masking for Short
Video Streaming. In Proceedings of the 30th ACM International Conference on
Multimedia (Lisboa, Portugal) (MM ’22). Association for Computing Machinery,
New York, NY, USA, 7030–7034. https://doi.org/10.1145/3503161.3551573
[10] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel.
2015. High-Dimensional Continuous Control Using Generalized Advantage
Estimation. https://doi.org/10.48550/ARXIV.1506.02438
[11] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal Policy Optimization Algorithms. https://doi.org/10.48550/ARXIV.
1707.06347
[12] Richard S Sutton, David McAllester, Satinder Singh, and Yishay Mansour. 1999.
Policy Gradient Methods for Reinforcement Learning with Function Approxima-
tion. In Advances in Neural Information Processing Systems, S. Solla, T. Leen,
and K. Müller (Eds.), Vol. 12. MIT Press. https://proceedings.neurips.cc/paper/
1999/file/464d828b85b0bed98e80ade0a5c43b0f-Paper.pdf
[13] Yunhao Tang and Shipra Agrawal. 2020. Discretizing continuous action space
for on-policy optimization. In Proceedings of the aaai conference on artificial
intelligence, Vol. 34. 5981–5988.
[14] TikTok. 2022. TikTok. Retrieved June 16, 2022 from https://www.tiktok.com
[15] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A Control-
Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP.
SIGCOMM Comput. Commun. Rev. 45, 4 (aug 2015), 325–338. https://doi.org/
10.1145/2829988.2787486
[16] Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao, Yu Wang, Alexandre Bayen,
and Yi Wu. 2021. The Surprising Effectiveness of PPO in Cooperative, Multi-Agent
Games. https://doi.org/10.48550/ARXIV.2103.01955
[17] Guanghui Zhang, Jie Zhang, Ke Liu, Jing Guo, Jack Lee, Haibo Hu, and Vaneet
Aggarwal. 2022. DUASVS: A Mobile Data Saving Strategy in Short-form Video
Streaming. IEEE Transactions on Services Computing (2022), 1–1. https://doi.
org/10.1109/TSC.2022.3150012
[18] Haodan Zhang, Yixuan Ban, Xinggong Zhang, Zongming Guo, Zhimin Xu, Sheng-
bin Meng, Junlin Li, and Yue Wang. 2020. Apl: Adaptive preloading of short video
with lyapunov optimization. In 2020 IEEE International Conference on Visual
Communications and Image Processing (VCIP). IEEE, 13–16.
[19] Huanhuan Zhang, Anfu Zhou, Yuhan Hu, Chaoyue Li, Guangping Wang, Xinyu
Zhang, Huadong Ma, Leilei Wu, Aiyun Chen, and Changhui Wu. 2021. Loki:
Improving Long Tail Performance of Learning-Based Real-Time Video Adaptation
by Fusing Rule-Based Models. In Proceedings of the 27th Annual International
Conference on Mobile Computing and Networking (New Orleans, Louisiana)
(MobiCom ’21). Association for Computing Machinery, New York, NY, USA,
775–788. https://doi.org/10.1145/3447993.3483259
[20] Jiakai Zhang and Kyunghyun Cho. 2016. Query-Efficient Imitation Learning for
End-to-End Autonomous Driving. https://doi.org/10.48550/ARXIV.1605.06450
[21] Chao Zhou, Yixuan Ban, Yangchao Zhao, Liang Guo, and Bing Yu. 2022. PDAS:
Probability-Driven Adaptive Streaming for Short Video. In Proceedings of the
30th ACM International Conference on Multimedia (Lisboa, Portugal) (MM ’22).
Association for Computing Machinery, New York, NY, USA, 7021–7025. https:
//doi.org/10.1145/3503161.3551571
[22] Xutong Zuo, Yishu Li, Mohan Xu, Wei Tsang Ooi, Jiangchuan Liu, Junchen
Jiang, Xinggong Zhang, Kai Zheng, and Yong Cui. 2022. Bandwidth-Efficient
Multi-Video Prefetching for Short Video Streaming. In Proceedings of the 30th
ACM International Conference on Multimedia (Lisboa, Portugal) (MM ’22). As-
sociation for Computing Machinery, New York, NY, USA, 7084–7088.
https:
//doi.org/10.1145/3503161.3551584
64
```
