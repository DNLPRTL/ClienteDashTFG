# ANT: Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming
**Archivo PDF:** `ANT.pdf`  **Identificador:** `10_ant_2024_network_dynamics_dedicated_models`  **Páginas:** 14  **SHA256 PDF:** `0273d786ce5afe2b84ff5973fd46896efa2d2524f3027ff8f02d2563e8dfcc24`  **Foco para Fase 4-5 v1:** Network-dynamics representation; condition detection; multiple dedicated DRL ABR models; dynamic model switching.
> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.
## 1. Cómo usar este `.md`
- Leer primero secciones 2-5 para ubicar método, señales, datos, evaluación y limitaciones.
- Usar la extracción por categorías como material de diseño/contrato/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No convertir resultados del paper en promesas directas para DashClientModular4; deben transformarse en hipótesis, guardrails y tests Phase 6.
## 2. Metadatos extraídos
- **format:** PDF 1.4
- **title:** Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming
- **subject:** IEEE Transactions on Broadcasting;2024;70;3;10.1109/TBC.2024.3396698
- **creator:** LaTeX with hyperref package
- **producer:** Acrobat Distiller 23.0 (Windows); modified using iText® Core 7.2.4 (AGPL version) ©2000-2022 iText Group NV
- **creationDate:** D:20240910105833+05'30'
- **modDate:** D:20240913133114-04'00'

## 3. Índice de secciones detectadas
- p.1: Abstract—The adaptive bitrate (ABR) algorithm plays a cru-
- p.1: I. INTRODUCTION
- p.2: Method. In this paper, we propose ANT to enhance adaptive
- p.2: II. RELATED WORK
- p.3: III. ANT DESIGN
- p.6: method [67] as the basic training algorithm. The state input,
- p.6: IV. EXPERIMENT RESULTS AND ANALYSIS
- p.7: results demonstrated that these retrained models achieved QoE
- p.7: TABLE I
- p.7: AVERAGE AND STANDARD DEVIATION VALUE OF
- p.7: THE THROUGHPUT FOR EACH CONDITION
- p.8: TABLE II
- p.8: HYPER-PARAMETERS SETTINGS AND TESTING RESULTS OF
- p.8: BASELINES AND OUR CNN-BASED DETECTION MODEL
- p.8: methods (BB and MPC) and learning-based methods (Pensieve
- p.9: TABLE III
- p.9: THE SITUATIONS OF ABR MODEL SELECTION UNDER 4
- p.9: RANDOMLY SELECTED NETWORK TRACES
- p.9: ANT-DIST
- p.9: results demonstrate that ANT-DIST, which uses the Euclidean
- p.12: V. DISCUSSION
- p.12: VI. CONCLUSION
- p.12: REFERENCES

## 4. Índice de páginas con palabras clave
- p.1: state, action, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, trace, Pensieve, PPO, latency, inference, quality, network condition
- p.2: state, QoE, buffer, throughput, bandwidth, download, dataset, trace, Pensieve, inference, network condition
- p.3: state, action, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, training, MPC, Pensieve, imitation, generalization, quality, network condition
- p.4: state, action, buffer, throughput, download, chunk, dataset, trace, training, PPO, network condition
- p.5: action, throughput, download, chunk, trace, training, inference, network condition
- p.6: state, reward, buffer, throughput, bandwidth, download, chunk, dataset, trace, training, baseline, Pensieve, A3C, network condition
- p.7: state, action, reward, QoE, rebuffer, buffer, throughput, download, chunk, trace, training, baseline, MPC, Pensieve, quality, network condition
- p.8: state, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, dataset, trace, baseline, MPC, Pensieve, PPO, inference, network condition
- p.9: state, action, QoE, rebuffer, buffer, throughput, download, dataset, trace, training, baseline, MPC, Pensieve, PPO, network condition
- p.10: state, QoE, stall, buffer, throughput, download, chunk, dataset, trace, training, baseline, Pensieve, latency, inference, network condition
- p.11: state, action, QoE, rebuffer, buffer, throughput, bandwidth, download, chunk, dataset, trace, Pensieve, latency, inference, quality, network condition
- p.12: state, QoE, rebuffer, buffer, throughput, bandwidth, download, dataset, trace, training, BOLA, Pensieve, PPO, latency, visual, network condition
- p.13: action, QoE, buffer, throughput, bandwidth, download, chunk, training, PPO, DQN, imitation, generalization, latency, quality
- p.14: bandwidth, download, dataset, trace, quality

## 5. Extracción técnica cruda por categorías

### 5.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

808 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition usin

**[Modelo / arquitectura / algoritmo | extracto 2 | p.1]**

aptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2].

**[Modelo / arquitectura / algoritmo | extracto 3 | p.1]**

ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index T

**[Modelo / arquitectura / algoritmo | extracto 4 | p.1]**

nhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, rein

**[Modelo / arquitectura / algoritmo | extracto 5 | p.1]**

this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn; mazhan@nju.edu.cn). Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA (e-mail: xiaozhongxu@tencent.com). Digital Object Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent

**[Modelo / arquitectura / algoritmo | extracto 6 | p.1]**

a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning,

**[Modelo / arquitectura / algoritmo | extracto 7 | p.1]**

ics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitra

**[Modelo / arquitectura / algoritmo | extracto 8 | p.2]**

onds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different ne

**[Modelo / arquitectura / algoritmo | extracto 9 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Eu

**[Modelo / arquitectura / algoritmo | extracto 10 | p.2]**

ctivates the appropriate ABR model accordingly. This enables ANT to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compared to existing approaches. The remainder of the paper is organized as follows. Section II reviews related work on ABR algorithms and network dynamics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divided into two main categories: rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37] and learning-based algorithms [11], [15], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predi

**[Modelo / arquitectura / algoritmo | extracto 11 | p.2]**

ast experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT framework for condition-wised multi-model ABR control. We introduce ANT, a framework that generates different ABR control policies for different network con- ditions. ANT utilizes a well-designed DNN for recurrent network condition detection and activates the appropriate ABR model accordingly. This enables ANT to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compa

**[Modelo / arquitectura / algoritmo | extracto 12 | p.2]**

Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the te

**[Modelo / arquitectura / algoritmo | extracto 13 | p.2]**

ifferentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to spe

**[Modelo / arquitectura / algoritmo | extracto 14 | p.2]**

STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change

**[Modelo / arquitectura / algoritmo | extracto 15 | p.2]**

Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to lear

**[Modelo / arquitectura / algoritmo | extracto 16 | p.3]**

810 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 fluency of video playback. Generally, these buffer-based algorithms can better avoid rebuffering to some extent, but they suffer from low video quality due to their conservative bitrate selections. To overcome the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches,

### 5.x Estado / inputs / features

**[Estado / inputs / features | extracto 1 | p.1]**

twork condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National Natural Sci

**[Estado / inputs / features | extracto 2 | p.1]**

iversity, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn; mazhan@nju.edu.cn). Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA (e-mail: xiaozhongxu@tencent.com). Digital Object Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or

**[Estado / inputs / features | extracto 3 | p.1]**

5; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn; mazhan@nju.edu.cn). Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA (e-mail: xiaozhongxu@tencent.com). Digital Object Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing

**[Estado / inputs / features | extracto 4 | p.1]**

808 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental r

**[Estado / inputs / features | extracto 5 | p.1]**

Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detectio

**[Estado / inputs / features | extracto 6 | p.1]**

. Figure 1 illustrates the instantaneous through- put/bitrate and the overall QoE results. As shown in Figure 1, there are several time slots (between the black dashed lines) with similar average (approximately 3.11 Mbps for slots 1 and 2, and 3.33 Mbps for slots 3 and 4) and STD (approximately 0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and 4) values of throughput. However, network throughput changes in these time slots exhibit different patterns: slots 1 and 2 have low-frequency but significant magnitude changes, while slots 3 and 4 have high-frequency but relatively minor magnitude 1557-9611 c⃝2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 7 | p.1]**

real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National Natural Science Foundation of China under Grant 62371290, Grant 62101241, and Grant U20A20185; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering Sc

**[Estado / inputs / features | extracto 8 | p.1]**

10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of netw

**[Estado / inputs / features | extracto 9 | p.1]**

en , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECE

**[Estado / inputs / features | extracto 10 | p.2]**

using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT framework for condition-wised multi-model ABR control. We introduce ANT, a framework that generates different ABR control policies for different network con- ditions. ANT utilizes a well-designed DNN for recurrent network condition detection and activates the appropriate ABR model accordingly. This enables ANT to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compared to existing approaches. The remainder of the paper is organized as follows. Section II reviews related work on ABR algorithms and network dynamics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divide

**[Estado / inputs / features | extracto 11 | p.2]**

namics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divided into two main categories: rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37] and learning-based algorithms [11], [15], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predict the available network bandwidth and then select the highest available bitrate below the estimated bandwidth. For example, CS2P [5] focused on the optimization of network bandwidth prediction problems to improve initial and subsequent adaptive streaming. However, it is still challenging to predict a specific value for network bandwidth in practice, resulting in poor performance for this type of ABR algorithms. Buffer-based algorithms [7], [8], [9], [10] aim to maintain the playback buffer occupancy at a pre-configured level to guarantee the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 12 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple

**[Estado / inputs / features | extracto 13 | p.2]**

entation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divided into two main categories: rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37] and learning-based algorithms [11], [15], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predict the available network bandwidth and then select the highest available bitrate below the estimated bandwidth. For example, CS2P [5] focused on the optimization of network bandwidth prediction problems to improve initial and subsequent adaptive streaming. However, it is still challenging to predict a specific value for network bandwidth in practice, resulting in poor performance for this type of ABR algorithms. Buffer-based algorithms [7], [8], [9], [10] aim to maintain the playback buffer occupancy at a pre-configured level to guarantee the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 14 | p.2]**

[44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predict the available network bandwidth and then select the highest available bitrate below the estimated bandwidth. For example, CS2P [5] focused on the optimization of network bandwidth prediction problems to improve initial and subsequent adaptive streaming. However, it is still challenging to predict a specific value for network bandwidth in practice, resulting in poor performance for this type of ABR algorithms. Buffer-based algorithms [7], [8], [9], [10] aim to maintain the playback buffer occupancy at a pre-configured level to guarantee the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

**[Estado / inputs / features | extracto 15 | p.2]**

ze the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT fra

**[Estado / inputs / features | extracto 16 | p.2]**

. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput da

### 5.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

808 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a

**[Acción / decisión ABR | extracto 2 | p.1]**

rning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National Natural Science Foundation of China under Grant 62371290, Grant 62101241, and Grant U20A20185; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin

**[Acción / decisión ABR | extracto 3 | p.1]**

ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of network condi- tion changes based on limited throughput statistics (average and STD) may not accurately represent the complex and diverse network conditions encountered in the real world. Consequently, Oboe may fail to select the most appropri- ate ABR parameters. To demons

**[Acción / decisión ABR | extracto 4 | p.1]**

to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National Natural Science Foundation of China under Grant 62371290, Grant 62101241, and Grant U20A20185; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are w

**[Acción / decisión ABR | extracto 5 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accu

**[Acción / decisión ABR | extracto 6 | p.2]**

clidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-through

**[Acción / decisión ABR | extracto 7 | p.2]**

real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT framework for condition-wised multi-model ABR control. We introduce ANT, a framework that generates different ABR control policies f

**[Acción / decisión ABR | extracto 8 | p.3]**

810 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 fluency of video playback. Generally, these buffer-based algorithms can better avoid rebuffering to some extent, but they suffer from low video quality due to their conservative bitrate selections. To overcome the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the

**[Acción / decisión ABR | extracto 9 | p.3]**

based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single

**[Acción / decisión ABR | extracto 10 | p.3]**

n both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural n

**[Acción / decisión ABR | extracto 11 | p.3]**

e-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditions. ABR algorithms that rely on a single model or fixed parameters often struggle to adapt to the complexities of mod- ern network conditions, resulting in significant performance degradation during video streaming. To address this issue, several approaches have been proposed. Oboe [15] proposed to auto-tune the parameters of ABR algorithms based on network conditions. It detected changes in network states using Bayesian change point detection algorithms based on average and standard deviation of throughput measurements, and then dynamically selected appropriate parameters for the ABR algorithm to adapt to the current network condition. Other approaches, such as [56] and [57], introduced meta- reinforcement learning to perceive changes in network states and tune the parameters of the policy network. In this way, the generalization of the neural network can be improved when encountering dynamic network conditions. In [58] and [59], federated reinforcement learning was adopted to enable their neural networks to handle various network conditions and user-end characteristics. Taking advantage of the idea of categorization and aggregation, the policy network can achieve Fig. 2. Overall architecture of ANT-powered adaptive video streaming. faster and more accurate convergence. Additionally, [14], [53] introduced automatic curriculum learning, which involved a gradual migration of trainin

**[Acción / decisión ABR | extracto 12 | p.4]**

l ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player status. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the current network condition. This information is then used to drive the selection of the appropriate model in the subsequent condition-wise multi-model ABR decision module. Label generation with unsupervised clustering. Existing network datasets often lack reliable labels indicating real network conditions, which poses a challenge for training and validating neural networks in our model. To overcome this issue, we propose a trace aggregation mechanism that

**[Acción / decisión ABR | extracto 13 | p.4]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 811 are segmented into a series of time-aligned chunks, each of which is further encoded at several bitrate levels for requests. During video streaming, the ANT server decides to request each video chunk at which bitrate based on network statistics and client-side playback status. Then the client-side video player downloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing th

**[Acción / decisión ABR | extracto 14 | p.4]**

unk at which bitrate based on network statistics and client-side playback status. Then the client-side video player downloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player status. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehe

**[Acción / decisión ABR | extracto 15 | p.4]**

of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player status. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the current network condition. This information is then used to drive the selection of the appropriate model in the subsequent condition-wise multi-model ABR decision module. Label generati

**[Acción / decisión ABR | extracto 16 | p.5]**

812 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Fig. 4. The neural network structure of the proposed model for network condition detection. network condition. In the neural network, three convolutional layers are devised to extract hierarchical features. These layers have the same structure but differ in their hyperparameters, such as the size of the convolutional kernel and the number of output channels. To improve feature extraction capability and condition detection accuracy, we add several optimized operations to the backbone network. • Multiple perceptual field. Considering the diverse feature scales present in network throughput data, we introduce a multi-perceptual-field mechanism to our neural network. This mechanism incorporates multi-scale convolutional kernels within each convolutional layer, allowing for the effective extrac

### 5.x Reward / QoE / objetivo

**[Reward / QoE / objetivo | extracto 1 | p.1]**

808 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechan

**[Reward / QoE / objetivo | extracto 2 | p.1]**

st its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National Natural Science Foundation of China under Grant 62371290, Grant 62101241, and Grant U20A20185; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn

**[Reward / QoE / objetivo | extracto 3 | p.1]**

on and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of network condi- tion changes based on limited throughput statistics (average and STD) may not accurately represent the complex and diverse network conditions encountered in the real world. Consequently, Oboe may fail to select the most appropri- ate ABR parameters. To demonstrate this, we compare the performance of existing state-of-the-art algorithms, including Pensieve [11] and Oboe [15], using a randomly selected network trace. Figure 1 illustrates the instantaneous throug

**[Reward / QoE / objetivo | extracto 4 | p.1]**

experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been

**[Reward / QoE / objetivo | extracto 5 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network th

**[Reward / QoE / objetivo | extracto 6 | p.3]**

810 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 fluency of video playback. Generally, these buffer-based algorithms can better avoid rebuffering to some extent, but they suffer from low video quality due to their conservative bitrate selections. To overcome the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learnin

**[Reward / QoE / objetivo | extracto 7 | p.5]**

al signal. • Residual structure. To address the issues of feature submerging of the shallow layer and gradient van- ishing/explosion in deeper CNNs, we incorporate the residual structure [66] into the backbone. This structure transmits shallow features directly to deeper layers and combines them with abstract features, enabling more efficient and stable training. • Normalization and dropout. In addition to the optimized operations mentioned earlier, we employ two normal- ization techniques to further enhance the performance of our neural network: mean standardization and batch normalization. These two normalization operations lead to faster convergence and improved training stability. Furthermore, dropout is utilized in fully connected layers to regularize the model and prevent overfitting during training. We use the binary cross-entropy loss function, as shown in Eq. (6), to train the CNN model for network condition detection. y and ˆy (in one-hot format) represent the label of the network condition and the output of this model, respectively. L  ˆy, y  = −  y log ˆy + (1 −y) log(1 −ˆy)  (6) Network condition inference. After completing the training of the detection model, the current segment’s network con- dition can be inferred using previous raw throughput data as input. It is worth mentioning that each ABR model is trained using a large number of traces that correspond to the same specific network condition. Thus we have devised a sliding window- based confidence mechanism for the accurate detection of trace-level network conditions, enabling effective selections of the appropriate ABR model in the subsequent module. The chunk-level condition detection is conducted ev

**[Reward / QoE / objetivo | extracto 8 | p.5]**

812 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Fig. 4. The neural network structure of the proposed model for network condition detection. network condition. In the neural network, three convolutional layers are devised to extract hierarchical features. These layers have the same structure but differ in their hyperparameters, such as the size of the convolutional kernel and the number of output channels. To improve feature extraction capability and condition detection accuracy, we add several optimized operations to the backbone network. • Multiple perceptual field. Considering the diverse feature scales present in network throughput data, we introduce a multi-perceptual-field mechanism to our neural network. This mechanism incorporates multi-scale convolutional kernels within each convolutional layer, allowing for the effective extraction of features at different scales from the network throughput data. Specifically, we use three distinct convolutional scales in each layer, namely 3 × 1, 5 × 1, and 7 × 1 kernels, and then concatenate features from different scales of convolution operation in the channel dimension. • Channel shuffle. To improve the stability and generaliza- tion of our neural model, we adopt the channel shuffle operation to disturb the original order of concatenated feature channels obtained from the multi-scale convo- lution operation. The feature channels are first divided

**[Reward / QoE / objetivo | extracto 9 | p.6]**

milar network traces to make ABR decisions. This ensures that ANT can adapt its decision-making process to different network conditions, providing optimal streaming performance. Training RL-based ABR models. With the trace aggregation mechanism described in Section III-B, each ABR model can be trained individually using network traces labeled with the same condition. During the training of each ABR model, the learning agent collects various observations from the video streaming environment, which include network statistics such as bandwidth or throughput, as well as player status at the client side like buffer occupancy. These observations are then fed into the RL neural network, prompting it to select the appropriate bitrate for the next chunk. After making a decision, the environment transitions to a new state, and the agent receives a reward. The RL agent learns to maximize the expected cumulative discounted reward by continuously interacting with the video streaming environment. Similar to the approach used in Pensieve [11], we employ the state-of-the-art asynchronous advantage actor-critic (A3C) method [67] as the basic training algorithm. The state input, neural network structure, and reward function remain consis- tent with those used in Pensieve’s framework. D. Implementation We implemented the CNN-based network condition detec- tion module and the RL-based ABR decision module using Tensorflow. For the neural network in the network condition detection module, we used three types of CNN filters with sizes 3×1, 5×1, and 7×1. The number of output channels for each CNN layer was 64×3, 128×3, and 256×3 respectively. The kernel size in the pooling layers we chose was 2 × 1. T

**[Reward / QoE / objetivo | extracto 10 | p.6]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 813 Fig. 5. Illustration of condition-wised multi-model ABR decision module. when the video streaming system runs in the initial period (i.e., 60 seconds in the beginning) and there is not enough historical throughput data to perform condition learning, the general status corresponding to all various network traces is selected until the input requirement of the confidence mechanism is met. C. Condition-Wised Multi-Model ABR Decision Multi-model switching mechanism for ABR decision. As shown in Figure 5, the condition-wised multi-model ABR decision module is constructed with multiple reinforcement learning (RL) based ABR models, which share the same neural network architecture but different model parameters. At a set interval, one of these trained ABR models is selected to make bitrate decisions according to the detection results by the network condition detection module. For different network conditions, there is a corresponding model trained specifically for that condition using similar network traces to make ABR decisions. This ensures that ANT can adapt its decision-making process to different network conditions, providing optimal streaming performance. Training RL-based ABR models. With the trace aggregation mechanism described in Section III-B, each ABR model can be trained indiv

**[Reward / QoE / objetivo | extracto 11 | p.7]**

hods. The training details for each model were the same as the proposed ANT described in Section III-C. QoE metrics. We adopted the general QoE metric proposed in MPC [27], which was defined as QoE = N  n=1 q(Rn) −µ N  n=1 Tn − N−1  n=1 |q(Rn+1) −q(Rn)| (7) for a video with N chunks. The QoE metric is an objective indicator used to assess the quality of the viewing experi- ence. This study considers multiple optimization objectives, including maximizing bitrate, minimizing rebuffering time, and maximizing smoothness. The general QoE metric is defined in Eq. (7), where Rn represents the video bitrate, and q(Rn) is the mapping function that converts the bitrate to the perceived user quality. As revealed in [72], the relationship between quality and bitrate is approximately linear in the low bitrate stage. Moreover, the linear QoE metric/reward function can facilitate the derivation and gradient updating during the training phase of the RL model, leading to easier convergence in the complex environment, compared to other non-linear forms. Considering that the maximum bitrate of the video content adopted in this paper is 2.64Mbps, it is acceptable to evaluate the viewing quality using the linear QoE metric. Therefore, in this work, we set the linear form q(Rn) = Rn, which is the same as the approach used in MPC, Pensieve, and Oboe. Tn represents the rebuffering time for each video chunk, and µ is the corresponding penalty coefficient. The rebuffering time refers to the time interval from the buffer depletion to the restoration of video playback. Similar to Pensieve, the rebuffer penalty coefficient was configured as the maximum video bitrate of 2.64 Mbps in this work, in order t

**[Reward / QoE / objetivo | extracto 12 | p.7]**

C codec at bitrates in {135, 340, 835, 1350, 2640} Kbps according to the Tencent video platform settings. Additionally, these videos were divided into 200 chunks, with each chunk lasting approximately 4 seconds, resulting in a total playback duration exceeding 10 minutes. Baselines. In the evaluation, we compared our approach with two heuristic ABR algorithms: buffer-based (BB) [7] and MPC [27], as well as two state-of-the-art learning-based ABR algorithms: Pensieve [11] and Oboe [15]. For the Oboe algorithm, we trained 5 neural network models for ABR decisions using network traces with different average through- put ranges: 0-3Mbps, 3-6Mbps, 6-9Mbps, 9-12Mbps, and over 12Mbps. We retrained the RL-based models of Pensieve and Oboe according to our specific settings. The validation results demonstrated that these retrained models achieved QoE improvements comparable to the original models in [11], [15], when compared to rule-based methods. The training details for each model were the same as the proposed ANT described in Section III-C. QoE metrics. We adopted the general QoE metric proposed in MPC [27], which was defined as QoE = N  n=1 q(Rn) −µ N  n=1 Tn − N−1  n=1 |q(Rn+1) −q(Rn)| (7) for a video with N chunks. The QoE metric is an objective indicator used to assess the quality of the viewing experi- ence. This study considers multiple optimization objectives, including maximizing bitrate, minimizing rebuffering time, and maximizing smoothness. The general QoE metric is defined in Eq. (7), where Rn represents the video bitrate, and q(Rn) is the mapping function that converts the bitrate to the perceived user quality. As revealed in [72], the relationship between quality

**[Reward / QoE / objetivo | extracto 13 | p.7]**

as two state-of-the-art learning-based ABR algorithms: Pensieve [11] and Oboe [15]. For the Oboe algorithm, we trained 5 neural network models for ABR decisions using network traces with different average through- put ranges: 0-3Mbps, 3-6Mbps, 6-9Mbps, 9-12Mbps, and over 12Mbps. We retrained the RL-based models of Pensieve and Oboe according to our specific settings. The validation results demonstrated that these retrained models achieved QoE improvements comparable to the original models in [11], [15], when compared to rule-based methods. The training details for each model were the same as the proposed ANT described in Section III-C. QoE metrics. We adopted the general QoE metric proposed in MPC [27], which was defined as QoE = N  n=1 q(Rn) −µ N  n=1 Tn − N−1  n=1 |q(Rn+1) −q(Rn)| (7) for a video with N chunks. The QoE metric is an objective indicator used to assess the quality of the viewing experi- ence. This study considers multiple optimization objectives, including maximizing bitrate, minimizing rebuffering time, and maximizing smoothness. The general QoE metric is defined in Eq. (7), where Rn represents the video bitrate, and q(Rn) is the mapping function that converts the bitrate to the perceived user quality. As revealed in [72], the relationship between quality and bitrate is approximately linear in the low bitrate stage. Moreover, the linear QoE metric/reward function can facilitate the derivation and gradient updating during the training phase of the RL model, leading to easier convergence in the complex environment, compared to other non-linear forms. Considering that the maximum bitrate of the video content adopted in this paper is 2.64Mbps, it is acceptable to

**[Reward / QoE / objetivo | extracto 14 | p.7]**

ork traces with different average through- put ranges: 0-3Mbps, 3-6Mbps, 6-9Mbps, 9-12Mbps, and over 12Mbps. We retrained the RL-based models of Pensieve and Oboe according to our specific settings. The validation results demonstrated that these retrained models achieved QoE improvements comparable to the original models in [11], [15], when compared to rule-based methods. The training details for each model were the same as the proposed ANT described in Section III-C. QoE metrics. We adopted the general QoE metric proposed in MPC [27], which was defined as QoE = N  n=1 q(Rn) −µ N  n=1 Tn − N−1  n=1 |q(Rn+1) −q(Rn)| (7) for a video with N chunks. The QoE metric is an objective indicator used to assess the quality of the viewing experi- ence. This study considers multiple optimization objectives, including maximizing bitrate, minimizing rebuffering time, and maximizing smoothness. The general QoE metric is defined in Eq. (7), where Rn represents the video bitrate, and q(Rn) is the mapping function that converts the bitrate to the perceived user quality. As revealed in [72], the relationship between quality and bitrate is approximately linear in the low bitrate stage. Moreover, the linear QoE metric/reward function can facilitate the derivation and gradient updating during the training phase of the RL model, leading to easier convergence in the complex environment, compared to other non-linear forms. Considering that the maximum bitrate of the video content adopted in this paper is 2.64Mbps, it is acceptable to evaluate the viewing quality using the linear QoE metric. Therefore, in this work, we set the linear form q(Rn) = Rn, which is the same as the approach used in MPC, Pensie

**[Reward / QoE / objetivo | extracto 15 | p.7]**

through- put ranges: 0-3Mbps, 3-6Mbps, 6-9Mbps, 9-12Mbps, and over 12Mbps. We retrained the RL-based models of Pensieve and Oboe according to our specific settings. The validation results demonstrated that these retrained models achieved QoE improvements comparable to the original models in [11], [15], when compared to rule-based methods. The training details for each model were the same as the proposed ANT described in Section III-C. QoE metrics. We adopted the general QoE metric proposed in MPC [27], which was defined as QoE = N  n=1 q(Rn) −µ N  n=1 Tn − N−1  n=1 |q(Rn+1) −q(Rn)| (7) for a video with N chunks. The QoE metric is an objective indicator used to assess the quality of the viewing experi- ence. This study considers multiple optimization objectives, including maximizing bitrate, minimizing rebuffering time, and maximizing smoothness. The general QoE metric is defined in Eq. (7), where Rn represents the video bitrate, and q(Rn) is the mapping function that converts the bitrate to the perceived user quality. As revealed in [72], the relationship between quality and bitrate is approximately linear in the low bitrate stage. Moreover, the linear QoE metric/reward function can facilitate the derivation and gradient updating during the training phase of the RL model, leading to easier convergence in the complex environment, compared to other non-linear forms. Considering that the maximum bitrate of the video content adopted in this paper is 2.64Mbps, it is acceptable to evaluate the viewing quality using the linear QoE metric. Therefore, in this work, we set the linear form q(Rn) = Rn, which is the same as the approach used in MPC, Pensieve, and Oboe. Tn represents the

**[Reward / QoE / objetivo | extracto 16 | p.8]**

esults were also reported in the table. It can be found that our model achieves the best detection accuracy, reaching 98.56%. While the baselines fail to get a satisfactory accuracy, all below 75%. The superiority in detection accuracy comes mainly from the multi-perceptual field mechanism, channel weight learning, and residual struc- ture in the proposed CNN-based model. These results also demonstrated the effectiveness of adding related optimized operations to baseline network architectures. With the ability to accurately detect current network condi- tions and the confidence mechanism for trace-level condition inference, the network condition detection module can effec- tively drive the model switching in the subsequent multi-model ABR decision module for better bitrate decisions based on historical throughput measurements. D. Overall QoE Performance Now we evaluated the performance of ANT for bitrate adaptation on the considered QoE metric and its individual components, including bitrate utility (in Mbps), rebuffering penalty (in seconds), and smoothness penalty (in Mbps), under P O P O P O P O Fig. 8. Performance comparison on the considered QoE metrics under both public traces and Tencent traces for the VoD scenario. 2 1 0 1 2 0.0 0.2 0.4 0.6 0.8 1.0 CDF QoE BB MPC Pensieve Oboe ANT BeƩer 0.5 1.0 1.5 2.0 2.5 0.0 0.2 0.4 0.6 0.8 1.0 CDF Bitrate(Mbps) BeƩer BB MPC Pensieve Oboe ANT 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 CDF Rebuffering(s) BB MPC Pensieve Oboe ANT BeƩer 0.0 0.2 0.4 0.6 0.8 0.0 0.2 0.4 0.6 0.8 1.0 CDF Smoothness(Mbps) BB MPC Pensieve Oboe ANT BeƩer Fig. 9. Final CDF curve under public traces. diverse network traces in the testing dataset. The resu

### 5.x Entrenamiento / optimización

**[Entrenamiento / optimización | extracto 1 | p.1]**

, Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video

**[Entrenamiento / optimización | extracto 2 | p.1]**

ed in part by the National Natural Science Foundation of China under Grant 62371290, Grant 62101241, and Grant U20A20185; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn; mazhan@nju.edu.cn). Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA (e-mail: xiaozhongxu@tencent.com). Digital Object Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the use

**[Entrenamiento / optimización | extracto 3 | p.1]**

live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National Natural Science Foundation of China under Grant 62371290, Grant 62101241, and Grant U20A20185; and in part by the 111 Project under Grant BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this work.) (Corresponding author: Yiling Xu.) Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn; mazhan@nju.edu.cn). Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA (e-mail: xiaozhongxu@tencent.com). Digital Object Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- uall

**[Entrenamiento / optimización | extracto 4 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network con

**[Entrenamiento / optimización | extracto 5 | p.2]**

ork can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divided into two main categories: rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37] and learning-based algorithms [11], [15], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predict the available network bandwidth and then select the highest available bitrate below the estimated bandwidth. For example, CS2P [5] focused on the optimization of network bandwidth prediction problems to improve initial and subsequent adaptive streaming. However, it is still challenging to predict a specific value for network bandwidth in practice, resulting in poor performance for this type of ABR algorithms. Buffer-based algorithms [7], [8], [9], [10] aim to maintain the playback buffer occupancy at a pre-configured level to guarantee the Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

**[Entrenamiento / optimización | extracto 6 | p.2]**

conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optim

**[Entrenamiento / optimización | extracto 7 | p.3]**

some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics a

**[Entrenamiento / optimización | extracto 8 | p.3]**

attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditions. ABR algorithms that rely on a single m

**[Entrenamiento / optimización | extracto 9 | p.3]**

ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 fluency of video playback. Generally, these buffer-based algorithms can better avoid rebuffering to some extent, but they suffer from low video quality due to their conservative bitrate selections. To overcome the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buf

**[Entrenamiento / optimización | extracto 10 | p.3]**

deviation of throughput measurements, and then dynamically selected appropriate parameters for the ABR algorithm to adapt to the current network condition. Other approaches, such as [56] and [57], introduced meta- reinforcement learning to perceive changes in network states and tune the parameters of the policy network. In this way, the generalization of the neural network can be improved when encountering dynamic network conditions. In [58] and [59], federated reinforcement learning was adopted to enable their neural networks to handle various network conditions and user-end characteristics. Taking advantage of the idea of categorization and aggregation, the policy network can achieve Fig. 2. Overall architecture of ANT-powered adaptive video streaming. faster and more accurate convergence. Additionally, [14], [53] introduced automatic curriculum learning, which involved a gradual migration of training from a simple to a com- plex network environment, significantly improving training performance and model generalization. However, these works mainly rely on limited throughput statistics (i.e., average and STD) to assess network dynamics and can easily lead to inaccurate recognition of network condition changes, finally degrading the ABR performances. Learning network dynamics. In addition to optimizing adaptive bitrate (ABR) algorithms, researchers have also focused on learning network dynamics to enhance video transmission performance. For example, in [60], a flow-based throughput classification method was proposed to predict the bitrate of traffic flow based on factors such as IP address, network prefix, protocol, and start timestamp. Another study by [61] conducted a systematic

**[Entrenamiento / optimización | extracto 11 | p.4]**

eries of time-aligned chunks, each of which is further encoded at several bitrate levels for requests. During video streaming, the ANT server decides to request each video chunk at which bitrate based on network statistics and client-side playback status. Then the client-side video player downloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player status. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that

**[Entrenamiento / optimización | extracto 12 | p.4]**

l procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the current network condition. This information is then used to drive the selection of the appropriate model in the subsequent condition-wise multi-model ABR decision module. Label generation with unsupervised clustering. Existing network datasets often lack reliable labels indicating real network conditions, which poses a challenge for training and validating neural networks in our model. To overcome this issue, we propose a trace aggregation mechanism that dis- tinguishes network conditions based on the distance between network throughput traces (as illustrated in Figure 3). The original network traces are first split into several equal-length segments that contain throughput information in t seconds or m throughput measurements, as shown in Eq. (3). Then K-means [65], a classic clustering algorithm, is adopted to cluster these trace segments based on the Euclidean distance between them. As a result, we obtain k clusters (as shown in Eq. (4)), where each cluster contains segments with similar network behaviors or conditions. We denote the label of the i-th segment in the same network trace as li. Finally, the entire network trace can be assigned a label, denoted as labeltrace,

**[Entrenamiento / optimización | extracto 13 | p.4]**

odule. Label generation with unsupervised clustering. Existing network datasets often lack reliable labels indicating real network conditions, which poses a challenge for training and validating neural networks in our model. To overcome this issue, we propose a trace aggregation mechanism that dis- tinguishes network conditions based on the distance between network throughput traces (as illustrated in Figure 3). The original network traces are first split into several equal-length segments that contain throughput information in t seconds or m throughput measurements, as shown in Eq. (3). Then K-means [65], a classic clustering algorithm, is adopted to cluster these trace segments based on the Euclidean distance between them. As a result, we obtain k clusters (as shown in Eq. (4)), where each cluster contains segments with similar network behaviors or conditions. We denote the label of the i-th segment in the same network trace as li. Finally, the entire network trace can be assigned a label, denoted as labeltrace, Fig. 3. Illustration of the trace aggregation mechanism. which represents the most frequent network condition across all segments. However, if the frequency of the most dominant network condition does not exceed a predefined threshold h, we mark the trace as “uncertain” according to Eq. (5). This accounts for cases where the network condition is ambiguous or lacks a clear majority. trace = ⎧ ⎪⎨ ⎪⎩ x1, x2, . . . , xm  Segment1(t second) , xm+1, . . . , x2m  Segment2(t second) , . . . , xn−m+1, . . . , xn  Segmentp(t second) ⎫ ⎪⎬ ⎪⎭ (3) labelsegment = {l1, l2, . . . , lp} = K −means.fit(Segment).labels , ∈[0, k −1] (4) labeltrace = ⎧ ⎨ ⎩ li, if numli/p ≥h unce

**[Entrenamiento / optimización | extracto 14 | p.4]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 811 are segmented into a series of time-aligned chunks, each of which is further encoded at several bitrate levels for requests. During video streaming, the ANT server decides to request each video chunk at which bitrate based on network statistics and client-side playback status. Then the client-side video player downloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player s

**[Entrenamiento / optimización | extracto 15 | p.5]**

ion (SE) module into the network backbone. The SE module acts as an attention mech- anism, assigning weights to the feature channels based on their importance. The SE module consists of two branches: one branch transmits the original signal, while the other branch performs the SE operation. After per- forming the SE operation, each channel is assigned a weight value based on its importance. These weight values are then multiplied element-wise with the corre- sponding channels in the original signal. • Residual structure. To address the issues of feature submerging of the shallow layer and gradient van- ishing/explosion in deeper CNNs, we incorporate the residual structure [66] into the backbone. This structure transmits shallow features directly to deeper layers and combines them with abstract features, enabling more efficient and stable training. • Normalization and dropout. In addition to the optimized operations mentioned earlier, we employ two normal- ization techniques to further enhance the performance of our neural network: mean standardization and batch normalization. These two normalization operations lead to faster convergence and improved training stability. Furthermore, dropout is utilized in fully connected layers to regularize the model and prevent overfitting during training. We use the binary cross-entropy loss function, as shown in Eq. (6), to train the CNN model for network condition detection. y and ˆy (in one-hot format) represent the label of the network condition and the output of this model, respectively. L  ˆy, y  = −  y log ˆy + (1 −y) log(1 −ˆy)  (6) Network condition inference. After completing the training of the detection model, the current seg

**[Entrenamiento / optimización | extracto 16 | p.5]**

operation, each channel is assigned a weight value based on its importance. These weight values are then multiplied element-wise with the corre- sponding channels in the original signal. • Residual structure. To address the issues of feature submerging of the shallow layer and gradient van- ishing/explosion in deeper CNNs, we incorporate the residual structure [66] into the backbone. This structure transmits shallow features directly to deeper layers and combines them with abstract features, enabling more efficient and stable training. • Normalization and dropout. In addition to the optimized operations mentioned earlier, we employ two normal- ization techniques to further enhance the performance of our neural network: mean standardization and batch normalization. These two normalization operations lead to faster convergence and improved training stability. Furthermore, dropout is utilized in fully connected layers to regularize the model and prevent overfitting during training. We use the binary cross-entropy loss function, as shown in Eq. (6), to train the CNN model for network condition detection. y and ˆy (in one-hot format) represent the label of the network condition and the output of this model, respectively. L  ˆy, y  = −  y log ˆy + (1 −y) log(1 −ˆy)  (6) Network condition inference. After completing the training of the detection model, the current segment’s network con- dition can be inferred using previous raw throughput data as input. It is worth mentioning that each ABR model is trained using a large number of traces that correspond to the same specific network condition. Thus we have devised a sliding window- based confidence mechanism for the accurate detection

### 5.x Datos / trazas / datasets

**[Datos / trazas / datasets | extracto 1 | p.1]**

ng in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of network condi- tion changes based on limited throughput statistics (average and STD) may not accurately represent the complex and diverse network conditions encountered in the real world. Consequently, Oboe may fail to select the most appropri- ate ABR parameters. To demonstrate this, we compare the performance of existing state-of-the-art algorithms, including Pensieve [11] and Oboe [15], using a randomly selected network trace. Figure 1 illustrates the instantaneous through- put/bitrate and the overall QoE results. As shown in Figure 1, there are several time slots (between the black dashed lines) with similar average (approximately 3.11 Mbps for slots 1 and 2, and 3.33 Mbps for slots 3 and 4) and STD (approximately 0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and 4) values of throughput. However, network throughput changes in these time slots exhibit different patterns: slots 1 and 2 have low-frequency but significant magnitude changes, while slots 3 and 4 have high-frequency but relatively minor magnitude 1557-9611 c⃝2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information. Authorized licensed use limited to: UNIVERSIDAD DE GRANADA.

**[Datos / trazas / datasets | extracto 2 | p.1]**

808 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT

**[Datos / trazas / datasets | extracto 3 | p.2]**

ose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN

**[Datos / trazas / datasets | extracto 4 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we

**[Datos / trazas / datasets | extracto 5 | p.2]**

nd temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network

**[Datos / trazas / datasets | extracto 6 | p.2]**

O STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a

**[Datos / trazas / datasets | extracto 7 | p.3]**

810 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 fluency of video playback. Generally, these buffer-based algorithms can better avoid rebuffering to some extent, but they suffer from low video quality due to their conservative bitrate selections. To overcome the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted

**[Datos / trazas / datasets | extracto 8 | p.4]**

nt-side video player downloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player status. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the cur

**[Datos / trazas / datasets | extracto 9 | p.4]**

ownloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutional neural network (1D-CNN) model is trained to accurately detect the network condition by learning and recognizing the temporal change pattern present in historical throughput measurements. The multi-model ABR decision module stores several RL-based ABR models, each of which is pre-trained using a large dataset of throughput traces collected under similar network conditions. Based on the output from the network condition detection module, one of the pre-trained models is dynamically selected to make adaptive bitrate (ABR) decisions. The bitrate decision is made by taking into account both network statistics and player status. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the current network conditi

**[Datos / trazas / datasets | extracto 10 | p.4]**

Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the current network condition. This information is then used to drive the selection of the appropriate model in the subsequent condition-wise multi-model ABR decision module. Label generation with unsupervised clustering. Existing network datasets often lack reliable labels indicating real network conditions, which poses a challenge for training and validating neural networks in our model. To overcome this issue, we propose a trace aggregation mechanism that dis- tinguishes network conditions based on the distance between network throughput traces (as illustrated in Figure 3). The original network traces are first split into several equal-length segments that contain throughput information in t seconds or m throughput measurements, as shown in Eq. (3). Then K-means [65], a classic clustering algorithm, is adopted to cluster these trace segments based on the Euclidean distance between them. As a result, we obtain k clusters (as shown in Eq. (4)), where each cluster contains segments with similar network behaviors or conditions. We denote the label of the i-th segment in the same network trace as li. Finally, the entire network trace can be assigned a label, denoted as labeltrace, Fig. 3. Illustration of the trace aggregation mechanism. which represents the most frequent network condition across all segments. However, if the frequency of the most dominant network condition does not

**[Datos / trazas / datasets | extracto 11 | p.4]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 811 are segmented into a series of time-aligned chunks, each of which is further encoded at several bitrate levels for requests. During video streaming, the ANT server decides to request each video chunk at which bitrate based on network statistics and client-side playback status. Then the client-side video player downloads the video chunk at the decided bitrate and stores them in a playback buffer for video decoding and playing. This process continues until either the end of the video is reached or the user chooses to quit the streaming session. For the ANT server, two key modules have been developed to support superior-performance ABR decisions across dif- ferent network conditions: network condition detection and condition-wised multi-model ABR decision. In the network condition detection module, a one-dimensional convolutio

**[Datos / trazas / datasets | extracto 12 | p.5]**

ce of our neural network: mean standardization and batch normalization. These two normalization operations lead to faster convergence and improved training stability. Furthermore, dropout is utilized in fully connected layers to regularize the model and prevent overfitting during training. We use the binary cross-entropy loss function, as shown in Eq. (6), to train the CNN model for network condition detection. y and ˆy (in one-hot format) represent the label of the network condition and the output of this model, respectively. L  ˆy, y  = −  y log ˆy + (1 −y) log(1 −ˆy)  (6) Network condition inference. After completing the training of the detection model, the current segment’s network con- dition can be inferred using previous raw throughput data as input. It is worth mentioning that each ABR model is trained using a large number of traces that correspond to the same specific network condition. Thus we have devised a sliding window- based confidence mechanism for the accurate detection of trace-level network conditions, enabling effective selections of the appropriate ABR model in the subsequent module. The chunk-level condition detection is conducted every 20 seconds, and the results at each step are queued into a sliding window. The chunk-level result is only accepted as the trace-level network condition if it matches the results from two out of the three previous time slots. Otherwise, the “uncertain” status is designated as the trace-level network condition. In addition, Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

**[Datos / trazas / datasets | extracto 13 | p.6]**

pectively. The entropy weight of the actor network was set to 0.5. We used a batch size of 100 for training. The training and testing of neural networks were on a Ubuntu 16.04 server equipped with Intel Xeon CPU E5-2683 v4 @2.10GHz and Nvidia GeForce GTX 1080Ti 11G GPU. IV. EXPERIMENT RESULTS AND ANALYSIS A. Experiment Setup Similar to Pensieve [11], we used a simulator with a 60- second buffer capacity to conduct trace-driven video streaming sessions for training and testing all the schemes considered. The network traces, video information, and baselines used in this paper are as follows. Network traces. Since it is time-consuming to “experience” video downloads in the real-world streaming environment, we conducted simulations over a wide range of network traces in the training and testing phases. These traces were collected from public datasets (including a broadband dataset provided by FCC [68], a 3G/HSDPA mobile dataset collected in Norway [69], a 4G/LTE bandwidth from Belgium [70], a mixed dataset provided in Oboe [15], and another mobile trace dataset provided in the ACM multimedia grand challenge [71]) and a Tencent dataset (including WiFi network traces and 3G/4G network traces). The Tencent dataset was a proprietary network trace dataset that was collected from the Tencent video platform, in which the videos experienced actual queries and downloads. There were nearly 2000 traces in the dataset, each of which contained about 30 minutes of throughput data on average. The average throughput of each trace ranged from less than 1Mbps to more than 10Mbps. Benefiting from user ends distributed widely throughout the world, these network traces were collected from China, Philipp

**[Datos / trazas / datasets | extracto 14 | p.6]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 813 Fig. 5. Illustration of condition-wised multi-model ABR decision module. when the video streaming system runs in the initial period (i.e., 60 seconds in the beginning) and there is not enough historical throughput data to perform condition learning, the general status corresponding to all various network traces is selected until the input requirement of the confidence mechanism is met. C. Condition-Wised Multi-Model ABR Decision Multi-model switching mechanism for ABR decision. As shown in Figure 5, the condition-wised multi-model ABR decision module is constructed with multiple reinforcement learning (RL) based ABR models, which share the same neural network architecture but different model parameters. At a set interval, one of these trained ABR models is selected to make bitrate decisions according to the detection results by the network condition detection module. For different network conditions, there is a corresponding model trained specifically for that condition using similar network traces to make ABR decisions. This ensures that ANT can adapt its decision-making process to different network conditions, providing optimal streaming per

**[Datos / trazas / datasets | extracto 15 | p.6]**

beginning) and there is not enough historical throughput data to perform condition learning, the general status corresponding to all various network traces is selected until the input requirement of the confidence mechanism is met. C. Condition-Wised Multi-Model ABR Decision Multi-model switching mechanism for ABR decision. As shown in Figure 5, the condition-wised multi-model ABR decision module is constructed with multiple reinforcement learning (RL) based ABR models, which share the same neural network architecture but different model parameters. At a set interval, one of these trained ABR models is selected to make bitrate decisions according to the detection results by the network condition detection module. For different network conditions, there is a corresponding model trained specifically for that condition using similar network traces to make ABR decisions. This ensures that ANT can adapt its decision-making process to different network conditions, providing optimal streaming performance. Training RL-based ABR models. With the trace aggregation mechanism described in Section III-B, each ABR model can be trained individually using network traces labeled with the same condition. During the training of each ABR model, the learning agent collects various observations from the video streaming environment, which include network statistics such as bandwidth or throughput, as well as player status at the client side like buffer occupancy. These observations are then fed into the RL neural network, prompting it to select the appropriate bitrate for the next chunk. After making a decision, the environment transitions to a new state, and the agent receives a reward. The RL agent

**[Datos / trazas / datasets | extracto 16 | p.6]**

as set to 0.5. We used a batch size of 100 for training. The training and testing of neural networks were on a Ubuntu 16.04 server equipped with Intel Xeon CPU E5-2683 v4 @2.10GHz and Nvidia GeForce GTX 1080Ti 11G GPU. IV. EXPERIMENT RESULTS AND ANALYSIS A. Experiment Setup Similar to Pensieve [11], we used a simulator with a 60- second buffer capacity to conduct trace-driven video streaming sessions for training and testing all the schemes considered. The network traces, video information, and baselines used in this paper are as follows. Network traces. Since it is time-consuming to “experience” video downloads in the real-world streaming environment, we conducted simulations over a wide range of network traces in the training and testing phases. These traces were collected from public datasets (including a broadband dataset provided by FCC [68], a 3G/HSDPA mobile dataset collected in Norway [69], a 4G/LTE bandwidth from Belgium [70], a mixed dataset provided in Oboe [15], and another mobile trace dataset provided in the ACM multimedia grand challenge [71]) and a Tencent dataset (including WiFi network traces and 3G/4G network traces). The Tencent dataset was a proprietary network trace dataset that was collected from the Tencent video platform, in which the videos experienced actual queries and downloads. There were nearly 2000 traces in the dataset, each of which contained about 30 minutes of throughput data on average. The average throughput of each trace ranged from less than 1Mbps to more than 10Mbps. Benefiting from user ends distributed widely throughout the world, these network traces were collected from China, Philippines, Thailand, India, and Indonesia. The networ

### 5.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 February 2024; revised 17 April 2024; accepted 24 April 2024. Date of publication 17 May 2024; date of current version 13 September 2024. This work was supported in part by the National N

**[Evaluación / baselines / experimentos | extracto 2 | p.1]**

t measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) algorithms have been developed to dynamically select the appropriate bitrate for each video chunk, mitigating the network fluctuations and achieving satis- factory Quality of Experience (QoE) in time-varying network connections. Manuscript received 8 F

**[Evaluación / baselines / experimentos | extracto 3 | p.1]**

808 IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE, Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE Abstract—The adaptive bitrate (ABR) algorithm plays a cru- cial role in ensuring satisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streami

**[Evaluación / baselines / experimentos | extracto 4 | p.1]**

ork conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of network condi- tion changes based on limited throughput statistics (average and STD) may not accurately represent the complex and diverse network conditions encountered in the real world. Consequently, Oboe may fail to select the most appropri- ate ABR parameters. To demonstrate this, we compare the performance of existing state-of-the-art algorithms, including Pensieve [11] and Oboe [15], using a randomly selected network trace. Figure 1 illustrates the instantaneous through- put/bitrate and the overall QoE results. As shown in Figure 1, there are several time slots (between the black dashed lines) with similar average (approximately 3.11 Mbps for slots 1 and 2, and 3.33 Mbps for slots 3 and 4) and STD (approximately 0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and 4) values of throughput. However, network throughput changes in these time slots exhibit different patterns: slots 1 and 2 have low-frequency but significant magnitude changes, while slots 3 and 4 have high-frequency but relatively minor magnitude 1

**[Evaluación / baselines / experimentos | extracto 5 | p.1]**

ing Xu are with the Cooperative Media Network Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn). Hao Chen and Zhan Ma are with the Electronic Science and Engineering School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: chenhao1210@nju.edu.cn; mazhan@nju.edu.cn). Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA (e-mail: xiaozhongxu@tencent.com). Digital Object Identifier 10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often comp

**[Evaluación / baselines / experimentos | extracto 6 | p.2]**

aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT framework for condition-wised multi-model ABR control. We introduce ANT, a framework that generates different ABR control policies for different network con- ditions. ANT utilizes a well-designed DNN for recurrent network condition detection and activates the appropriate ABR model accordingly. This enables ANT to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compared to existing approaches. The remainder of the paper is organized as follows. Section II reviews related work on ABR algorithms and network dynamics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found i

**[Evaluación / baselines / experimentos | extracto 7 | p.2]**

s enables ANT to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compared to existing approaches. The remainder of the paper is organized as follows. Section II reviews related work on ABR algorithms and network dynamics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divided into two main categories: rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37] and learning-based algorithms [11], [15], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predict the available network bandwidth and then selec

**[Evaluación / baselines / experimentos | extracto 8 | p.2]**

n values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT framework for condition-wised multi-model ABR control. We introduce ANT, a framework that generates different ABR control policies for different network con- ditions. ANT utilizes a well-designed DNN for recurrent network condition detection and activates the appropriate ABR model accordingly. This enables ANT to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compared to existing approaches. The remainder of the paper is organized as follows. Section II reviews related work on ABR algorithms and network dynamics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algori

**[Evaluación / baselines / experimentos | extracto 9 | p.2]**

to make better ABR decisions for ensuring satisfactory QoE across a wide range of network conditions. • Evaluation through simulations and field tests. We val- idate the effectiveness of ANT through simulations and field tests. We compare ANT against state-of-the-art ABR algorithms using public network trace datasets and a proprietary dataset collected from the large-scale Tencent video hosting system distributed worldwide. In both video-on-demand (VoD) and live-streaming (LS) scenarios, ANT demonstrates significant improvements in QoE compared to existing approaches. The remainder of the paper is organized as follows. Section II reviews related work on ABR algorithms and network dynamics learning. Section III introduces the design details of the proposed ANT, including its architecture, key modules, and implementation. The experimental results and analysis for ANT are presented in Section IV. The discussion and conclusion of this work can be found in Sections V and VI, respectively. II. RELATED WORK ABR algorithms with a fixed model. Existing state-of-the- art ABR algorithms can be divided into two main categories: rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37] and learning-based algorithms [11], [15], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54]. The rule-based algorithms can be further classified into rate-based, buffer-based, and hybrid-control approaches. Rate- based algorithms [3], [4], [5], [6], first try to predict the available network bandwidth and then select the hig

**[Evaluación / baselines / experimentos | extracto 10 | p.2]**

we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved char

**[Evaluación / baselines / experimentos | extracto 11 | p.2]**

V-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning network throughput dynamics across a wide range of network conditions. Unlike traditional methods that rely on simple mean/STD values, ANT utilizes a combination of the Euclidean distance from a group of clustering centers and temporal change patterns extracted from neural networks of multi-dimensional raw-throughput measurements to characterize the network condition. Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the

**[Evaluación / baselines / experimentos | extracto 12 | p.2]**

YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING 809 Bitrate(Mbps) Pensieve Ɵme(s) QoE Pensieve Oboe ANT Oboe ANT bandwidth Fig. 1. Illustration of the necessity for accurate network throughput learning. changes. Both Pensieve, with a single model, and Oboe, with its auto-tuning mechanism based on average/STD throughput values, struggle to differentiate between these different trends. Pensieve can only rely on a general ABR model trained on all network traces, while Oboe continues to choose the second ABR model (3-6 Mbps, depicted in Section IV-D) before and after the change point of network conditions (around 180 seconds). As they are unable to accurately sense network conditions and select the appropriate ABR model in a timely manner, both Pensieve and Oboe experience greater QoE degradation after the change point. Method. In this paper, we propose ANT to enhance adaptive video streaming by accurately learning

**[Evaluación / baselines / experimentos | extracto 13 | p.3]**

istic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditions. ABR algorithms that rely on a single model or fixed parameters often struggle to adapt to the complexities of mod- ern network conditions, resulting in significant performance degradation during video streaming. To address this issue, several approaches have been proposed. Oboe [15] proposed to auto-tune the parameters of ABR algorithms based on network conditions. It detected changes in network states using Bayesian change point detection algorithms based on average and standard deviation of throughput measurements, and the

**[Evaluación / baselines / experimentos | extracto 14 | p.3]**

put values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditio

**[Evaluación / baselines / experimentos | extracto 15 | p.3]**

ies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditions. ABR algorithms that rely on a single model or fixed parameters often struggle to adapt to the complexities of mod- ern network conditions, resulting in significant performance degradati

**[Evaluación / baselines / experimentos | extracto 16 | p.3]**

the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based al

### 5.x Limitaciones / riesgos / implementación

**[Limitaciones / riesgos / implementación | extracto 1 | p.1]**

y or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of network condi- tion changes based on limited throughput statistics (average and STD) may not accurately represent the complex and diverse network conditions encountered in the real world. Consequently, Oboe may fail to select the most appropri- ate ABR parameters. To demonstrate this, we compare the performance of existing state-of-the-art algorithms, including Pensieve [11] and Oboe [15], using a randomly selected network trace. Figure 1 illustrates the instantaneous through- put/bitrate and the overall QoE results. As shown in Figure 1, there are several time slots (between the black dashed lines) with similar average (approximately 3.11 Mbps for slots 1 and 2, and 3.33 Mbps for slots 3 and 4) and STD (approximately 0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and 4) values of throughput. However, network throughput changes in these time slots exhibit different patterns: slots 1 and 2 have low-frequency but significant magnitude changes, while slots

**[Limitaciones / riesgos / implementación | extracto 2 | p.1]**

tisfactory quality of experience (QoE) in video streaming applications. Most existing approaches, either rule-based or learning-driven, tend to conduct ABR decisions based on limited network statistics, e.g., mean/standard deviation of recent throughput measurements. However, all of them lack a good understanding of network dynamics given the varying network conditions from time to time, leading to compromised performance, especially when the network condition changes significantly. In this paper, we propose a framework named ANT that aims to enhance adaptive video streaming by accurately learning network dynamics. ANT represents and detects specific network conditions by characterizing the entire spectrum of network fluctuations. It further trains multiple dedicated ABR models for each condition using deep reinforcement learning. During inference, a dynamic switching mechanism is devised to activate the appropriate ABR model based on real-time network condition sensing, enabling ANT to automatically adjust its control policies to different network conditions. Extensive exper- imental results demonstrate that our proposed ANT achieves a significant improvement in user QoE of 20.8%-41.2% in the video-on-demand scenario and 67.4%-134.5% in the live- streaming scenario compared to state-of-the-art methods, across a wide range of network conditions. Index Terms—Network dynamics learning, video on demand, live streaming, adaptive bitrate, reinforcement learning, quality of experience. I. INTRODUCTION R ECENT years have witnessed an exponential increase in the volume of HTTP-based video streaming traf- fic [1], [2]. To assure high-quality service provisioning, adaptive bitrate (ABR) alg

**[Limitaciones / riesgos / implementación | extracto 3 | p.1]**

10.1109/TBC.2024.3396698 Background. Early ABR approaches relied on man- ually fine-tuned heuristics based on network throughput information [3], [4], [5], [6] and receiver states (e.g., play- back buffer occupancy [7], [8], [9], [10]). In recent years, learning-based ABR approaches, utilizing RL-based neural engines, have gained popularity. These approaches, including Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14], leverage neural networks for feature extraction and pol- icy learning, outperforming fixed rule-based algorithms in time-varying network environments. However, ensuring user QoE across a wide range of dynamic network connec- tions with unpredictable fluctuations remains challenging for learning-based algorithms. The heterogeneous nature of access networks, including wireless and wired networks with varying bandwidth, latency, and buffer capacities, further complicates the situation. Additionally, the user’s scenario, such as station- ary or on the move, introduces additional variations in network conditions. Existing learning-based algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of netw

**[Limitaciones / riesgos / implementación | extracto 4 | p.1]**

ased algorithms typically train a single model for ABR decisions without adapting to dif- ferent network conditions. Consequently, the learned neural model often compromises across various network conditions, resulting in compromised video quality or frequent rebuffering, ultimately degrading user QoE. Motivation. To solve this issue, a solution called Oboe [15] is proposed to automatically tune video ABR algorithms to various network conditions. It detects changes in network states or conditions by analyzing the average and standard deviation (STD) of throughput and adjusts ABR parameters accordingly. However, Oboe’s detection of network condi- tion changes based on limited throughput statistics (average and STD) may not accurately represent the complex and diverse network conditions encountered in the real world. Consequently, Oboe may fail to select the most appropri- ate ABR parameters. To demonstrate this, we compare the performance of existing state-of-the-art algorithms, including Pensieve [11] and Oboe [15], using a randomly selected network trace. Figure 1 illustrates the instantaneous through- put/bitrate and the overall QoE results. As shown in Figure 1, there are several time slots (between the black dashed lines) with similar average (approximately 3.11 Mbps for slots 1 and 2, and 3.33 Mbps for slots 3 and 4) and STD (approximately 0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and 4) values of throughput. However, network throughput changes in these time slots exhibit different patterns: slots 1 and 2 have low-frequency but significant magnitude changes, while slots 3 and 4 have high-frequency but relatively minor magnitude 1557-9611 c⃝2024 IEEE. Persona

**[Limitaciones / riesgos / implementación | extracto 5 | p.2]**

Toward this, we first classify a large-scale dataset of network trace segments (NTS) collected in the real world into multiple (e.g., five) clusters by using the classic K-means algorithm. Each cluster represents a distinct network behavior class and is assigned a unique network condition number for ANT as the label. Recognizing that the temporal dynamics of network throughput significantly impact ABR performance, we additionally leverage a deep neural network (DNN) to learn the temporal change patterns from the sequence of raw throughput data. For each network condition, ANT trains a dedicated reinforcement learning (RL)-based model for ABR decisions using the corresponding cluster of network traces. This allows ANT to learn and adapt to specific patterns of network dynamics and improve decision-making based on past experiences. During inference, ANT employs the aforementioned trained DNN to recurrently detect the network condition and selects the appropriate ABR model accordingly. By effectively adapting to different network behaviors and pat- terns, ANT can provide optimal video streaming experiences for users in diverse network environments. Contribution. The main contributions of this paper can be summarized in three aspects: • Improved characterization of network throughput dynam- ics. Instead of relying solely on mean and standard deviation values, we propose using the Euclidean distance from clustering centers and the temporal change pat- tern in multi-dimensional raw-throughput measurements to accurately characterize network throughput dynamics over time. This approach provides a better differentiation of typical network behaviors. • ANT framework for condition-wised mul

**[Limitaciones / riesgos / implementación | extracto 6 | p.3]**

S ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024 fluency of video playback. Generally, these buffer-based algorithms can better avoid rebuffering to some extent, but they suffer from low video quality due to their conservative bitrate selections. To overcome the shortcomings of these two techniques, some hybrid-control ABR algorithms attempt to make bitrate decisions based on both network throughput prediction and buffer occupancy simultaneously. For example, MPC [27] estimated the future throughput by calculating the harmonic mean of the throughput values from the last five chunks and attaching a discount factor, then went through all bitrate options and selects the one that maximizes a given QoE metric. However, MPC also relies on accurate throughput prediction, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buf

**[Limitaciones / riesgos / implementación | extracto 7 | p.3]**

, which can encounter similar problems to rate-based algorithms. Due to the limitations of rule-based algorithms, recent research has shifted towards learning-based hybrid control approaches, such as the reinforcement learning based [11], [39], [40], [55], imitation learning based [41], and hybrid learning-heuristic algorithms [38]. Pensieve [11] was a pio- neering work that trained a neural network model using reinforcement learning to make bitrate decisions, which solely relied on observations collected from video players. In con- trast to Pensieve, Comyco [41] trained its neural network model using imitation learning, resulting in a significant reduction in training time while maintaining the same QoE level. Stick [38] integrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditions. ABR algorithms that rely on a single model or fixed parameters often struggle to adapt to the complexities of mod- ern network conditions, resulting in significant performance degradation during video streaming. To addr

**[Limitaciones / riesgos / implementación | extracto 8 | p.3]**

ntegrates a heuristic ABR algorithm with a learning-based method to enhance its performance and reduce computational overhead. It achieves this by training a neural network to dynamically control the buffer threshold parameter of an existing buffer-based algorithm. Taking advantage of the capabilities of neural networks in feature extraction and policy learning, these learning-based algorithms have shown superior performance compared to early rule-based algorithms that utilize fixed heuristics across various network conditions. However, they often rely on a single neural network model for ABR decisions and lack specialization for different network conditions, resulting in compromised performance. Auto-tuning ABR parameters to network conditions. ABR algorithms that rely on a single model or fixed parameters often struggle to adapt to the complexities of mod- ern network conditions, resulting in significant performance degradation during video streaming. To address this issue, several approaches have been proposed. Oboe [15] proposed to auto-tune the parameters of ABR algorithms based on network conditions. It detected changes in network states using Bayesian change point detection algorithms based on average and standard deviation of throughput measurements, and then dynamically selected appropriate parameters for the ABR algorithm to adapt to the current network condition. Other approaches, such as [56] and [57], introduced meta- reinforcement learning to perceive changes in network states and tune the parameters of the policy network. In this way, the generalization of the neural network can be improved when encountering dynamic network conditions. In [58] and [59], federated

**[Limitaciones / riesgos / implementación | extracto 9 | p.3]**

rs to network conditions. ABR algorithms that rely on a single model or fixed parameters often struggle to adapt to the complexities of mod- ern network conditions, resulting in significant performance degradation during video streaming. To address this issue, several approaches have been proposed. Oboe [15] proposed to auto-tune the parameters of ABR algorithms based on network conditions. It detected changes in network states using Bayesian change point detection algorithms based on average and standard deviation of throughput measurements, and then dynamically selected appropriate parameters for the ABR algorithm to adapt to the current network condition. Other approaches, such as [56] and [57], introduced meta- reinforcement learning to perceive changes in network states and tune the parameters of the policy network. In this way, the generalization of the neural network can be improved when encountering dynamic network conditions. In [58] and [59], federated reinforcement learning was adopted to enable their neural networks to handle various network conditions and user-end characteristics. Taking advantage of the idea of categorization and aggregation, the policy network can achieve Fig. 2. Overall architecture of ANT-powered adaptive video streaming. faster and more accurate convergence. Additionally, [14], [53] introduced automatic curriculum learning, which involved a gradual migration of training from a simple to a com- plex network environment, significantly improving training performance and model generalization. However, these works mainly rely on limited throughput statistics (i.e., average and STD) to assess network dynamics and can easily lead to inaccurate recognition of

**[Limitaciones / riesgos / implementación | extracto 10 | p.3]**

tion to optimizing adaptive bitrate (ABR) algorithms, researchers have also focused on learning network dynamics to enhance video transmission performance. For example, in [60], a flow-based throughput classification method was proposed to predict the bitrate of traffic flow based on factors such as IP address, network prefix, protocol, and start timestamp. Another study by [61] conducted a systematic study for various prediction algorithms and analyzed their performance when applied in the prediction of throughput in mobile networks, promoting the employment of throughput prediction in ABR algorithms. Other related works, such as [13], [62], [63], [64], have explored efficient methods for predicting throughput or band- width and utilizing learned network dynamics to optimize adaptive video streaming. However, these approaches often face challenges in capturing comprehensive network statis- tics across different layers and accurately predicting specific throughput or bandwidth values. This limits their effectiveness and efficiency when applied to enhance application-layer ABR algorithms. III. ANT DESIGN State-of-the-art ABR algorithms attempt to train a general neural network model for bitrate decisions to adapt to a wide range of network conditions. However, during training, this general model easily converges to a compromised policy with average performance across all considered network conditions rather than achieving optimal performance. To this end, we propose a condition-wised multi-model framework, named ANT, to optimize the performance of adaptive video streaming under each network condition. In this section, we will introduce the design details of ANT, including the overa

**[Limitaciones / riesgos / implementación | extracto 11 | p.4]**

us. The general procedure for the proposed architecture can be formulated as follows: condition = f1D−CNN(throughputhistorical) (1) action = fABR  statenetwork, stateplayer, condition  (2) B. Network Condition Detection Different from existing approaches that rely on simple statistical features of the throughput data like average and STD values, our network condition detection module utilizes a powerful CNN model to extract comprehensive features from raw throughput data, enabling it to learn and accurately determine the current network condition. This information is then used to drive the selection of the appropriate model in the subsequent condition-wise multi-model ABR decision module. Label generation with unsupervised clustering. Existing network datasets often lack reliable labels indicating real network conditions, which poses a challenge for training and validating neural networks in our model. To overcome this issue, we propose a trace aggregation mechanism that dis- tinguishes network conditions based on the distance between network throughput traces (as illustrated in Figure 3). The original network traces are first split into several equal-length segments that contain throughput information in t seconds or m throughput measurements, as shown in Eq. (3). Then K-means [65], a classic clustering algorithm, is adopted to cluster these trace segments based on the Euclidean distance between them. As a result, we obtain k clusters (as shown in Eq. (4)), where each cluster contains segments with similar network behaviors or conditions. We denote the label of the i-th segment in the same network trace as li. Finally, the entire network trace can be assigned a label, denoted a

**[Limitaciones / riesgos / implementación | extracto 12 | p.5]**

d combines them with abstract features, enabling more efficient and stable training. • Normalization and dropout. In addition to the optimized operations mentioned earlier, we employ two normal- ization techniques to further enhance the performance of our neural network: mean standardization and batch normalization. These two normalization operations lead to faster convergence and improved training stability. Furthermore, dropout is utilized in fully connected layers to regularize the model and prevent overfitting during training. We use the binary cross-entropy loss function, as shown in Eq. (6), to train the CNN model for network condition detection. y and ˆy (in one-hot format) represent the label of the network condition and the output of this model, respectively. L  ˆy, y  = −  y log ˆy + (1 −y) log(1 −ˆy)  (6) Network condition inference. After completing the training of the detection model, the current segment’s network con- dition can be inferred using previous raw throughput data as input. It is worth mentioning that each ABR model is trained using a large number of traces that correspond to the same specific network condition. Thus we have devised a sliding window- based confidence mechanism for the accurate detection of trace-level network conditions, enabling effective selections of the appropriate ABR model in the subsequent module. The chunk-level condition detection is conducted every 20 seconds, and the results at each step are queued into a sliding window. The chunk-level result is only accepted as the trace-level network condition if it matches the results from two out of the three previous time slots. Otherwise, the “uncertain” status is designated as the tr

**[Limitaciones / riesgos / implementación | extracto 13 | p.6]**

a width. As for other hyper-parameters, we set the learning rate as 0.0001 and batch size as 80 in the training phase. For the RL-based ABR decision module, we used 16 RL agents to learn the control policy for bitrate adaptation. In the state input, we considered the past eight observations from the environment, which were normalized before being fed into the neural network. Both the actor network and the critic network consisted of one 1D-CNN layer with a kernel size of 4 and 128 output channels, as well as a fully connected layer with 128 neurons. The learning rates for the actor and critic networks were set to 0.0001 and 0.001, respectively. The entropy weight of the actor network was set to 0.5. We used a batch size of 100 for training. The training and testing of neural networks were on a Ubuntu 16.04 server equipped with Intel Xeon CPU E5-2683 v4 @2.10GHz and Nvidia GeForce GTX 1080Ti 11G GPU. IV. EXPERIMENT RESULTS AND ANALYSIS A. Experiment Setup Similar to Pensieve [11], we used a simulator with a 60- second buffer capacity to conduct trace-driven video streaming sessions for training and testing all the schemes considered. The network traces, video information, and baselines used in this paper are as follows. Network traces. Since it is time-consuming to “experience” video downloads in the real-world streaming environment, we conducted simulations over a wide range of network traces in the training and testing phases. These traces were collected from public datasets (including a broadband dataset provided by FCC [68], a 3G/HSDPA mobile dataset collected in Norway [69], a 4G/LTE bandwidth from Belgium [70], a mixed dataset provided in Oboe [15], and another mobile t

**[Limitaciones / riesgos / implementación | extracto 14 | p.6]**

g rate as 0.0001 and batch size as 80 in the training phase. For the RL-based ABR decision module, we used 16 RL agents to learn the control policy for bitrate adaptation. In the state input, we considered the past eight observations from the environment, which were normalized before being fed into the neural network. Both the actor network and the critic network consisted of one 1D-CNN layer with a kernel size of 4 and 128 output channels, as well as a fully connected layer with 128 neurons. The learning rates for the actor and critic networks were set to 0.0001 and 0.001, respectively. The entropy weight of the actor network was set to 0.5. We used a batch size of 100 for training. The training and testing of neural networks were on a Ubuntu 16.04 server equipped with Intel Xeon CPU E5-2683 v4 @2.10GHz and Nvidia GeForce GTX 1080Ti 11G GPU. IV. EXPERIMENT RESULTS AND ANALYSIS A. Experiment Setup Similar to Pensieve [11], we used a simulator with a 60- second buffer capacity to conduct trace-driven video streaming sessions for training and testing all the schemes considered. The network traces, video information, and baselines used in this paper are as follows. Network traces. Since it is time-consuming to “experience” video downloads in the real-world streaming environment, we conducted simulations over a wide range of network traces in the training and testing phases. These traces were collected from public datasets (including a broadband dataset provided by FCC [68], a 3G/HSDPA mobile dataset collected in Norway [69], a 4G/LTE bandwidth from Belgium [70], a mixed dataset provided in Oboe [15], and another mobile trace dataset provided in the ACM multimedia grand challeng

**[Limitaciones / riesgos / implementación | extracto 15 | p.6]**

11G GPU. IV. EXPERIMENT RESULTS AND ANALYSIS A. Experiment Setup Similar to Pensieve [11], we used a simulator with a 60- second buffer capacity to conduct trace-driven video streaming sessions for training and testing all the schemes considered. The network traces, video information, and baselines used in this paper are as follows. Network traces. Since it is time-consuming to “experience” video downloads in the real-world streaming environment, we conducted simulations over a wide range of network traces in the training and testing phases. These traces were collected from public datasets (including a broadband dataset provided by FCC [68], a 3G/HSDPA mobile dataset collected in Norway [69], a 4G/LTE bandwidth from Belgium [70], a mixed dataset provided in Oboe [15], and another mobile trace dataset provided in the ACM multimedia grand challenge [71]) and a Tencent dataset (including WiFi network traces and 3G/4G network traces). The Tencent dataset was a proprietary network trace dataset that was collected from the Tencent video platform, in which the videos experienced actual queries and downloads. There were nearly 2000 traces in the dataset, each of which contained about 30 minutes of throughput data on average. The average throughput of each trace ranged from less than 1Mbps to more than 10Mbps. Benefiting from user ends distributed widely throughout the world, these network traces were collected from China, Philippines, Thailand, India, and Indonesia. The network types of user ends included Wifi and 3G/4G, which could cover a wide range of network conditions and application scenarios. In the network trace file, time information (second) and corresponding through- put/bandw

**[Limitaciones / riesgos / implementación | extracto 16 | p.7]**

ic proposed in MPC [27], which was defined as QoE = N  n=1 q(Rn) −µ N  n=1 Tn − N−1  n=1 |q(Rn+1) −q(Rn)| (7) for a video with N chunks. The QoE metric is an objective indicator used to assess the quality of the viewing experi- ence. This study considers multiple optimization objectives, including maximizing bitrate, minimizing rebuffering time, and maximizing smoothness. The general QoE metric is defined in Eq. (7), where Rn represents the video bitrate, and q(Rn) is the mapping function that converts the bitrate to the perceived user quality. As revealed in [72], the relationship between quality and bitrate is approximately linear in the low bitrate stage. Moreover, the linear QoE metric/reward function can facilitate the derivation and gradient updating during the training phase of the RL model, leading to easier convergence in the complex environment, compared to other non-linear forms. Considering that the maximum bitrate of the video content adopted in this paper is 2.64Mbps, it is acceptable to evaluate the viewing quality using the linear QoE metric. Therefore, in this work, we set the linear form q(Rn) = Rn, which is the same as the approach used in MPC, Pensieve, and Oboe. Tn represents the rebuffering time for each video chunk, and µ is the corresponding penalty coefficient. The rebuffering time refers to the time interval from the buffer depletion to the restoration of video playback. Similar to Pensieve, the rebuffer penalty coefficient was configured as the maximum video bitrate of 2.64 Mbps in this work, in order to minimize viewing Fig. 6. SSE and DBI results over different k values. TABLE I AVERAGE AND STANDARD DEVIATION VALUE OF THE THROUGHPUT FOR EACH CONDI

## 6. Figuras / tablas / algoritmos / ecuaciones detectados por texto
- p.1: Figure 1 illustrates the instantaneous through-
- p.1: Figure 1,
- p.2: Fig. 1.
- p.3: Fig. 2.
- p.3: Figure 2. On the media server, videos
- p.4: Figure 3). The
- p.4: Fig. 3.
- p.4: Figure 4. The backbone of our network is a 1D-CNN, which is
- p.5: Fig. 4.
- p.6: Fig. 5.
- p.6: Figure 5, the condition-wised multi-model ABR
- p.7: Fig. 6.
- p.7: Figure 6.
- p.7: Figure 7. From these results,
- p.8: Fig. 7.
- p.8: Fig. 8.
- p.8: Fig. 9.
- p.8: Figure 8 to Figure 10.
- p.8: Figure 8, the proposed ANT achieves the best
- p.8: Figure 8. Along with the higher average bandwidth,
- p.9: Fig. 10.
- p.9: Figure 9 and Figure 10 respectively. We observed that ANT
- p.9: Fig. 11.
- p.9: Figure 11, the default ANT also outperforms
- p.10: Fig. 12.
- p.10: Figure 12. We found that ANT either matched or exceeded
- p.10: Figure 13. As shown, ANT always outperforms other algo-
- p.10: Figure 13), enabling it to
- p.10: Fig. 13.
- p.10: Fig. 14.
- p.10: Figure 14
- p.11: Fig. 15.
- p.11: Fig. 16.
- p.11: Figure 15 shows the average QoE that each ABR algorithm
- p.11: Figure 16 provides more detailed results in the form of full
- p.12: Figure 16(b). Recall that

## 7. Líneas con posible contenido matemático/formal
- p.1: `fic [1], [2]. To assure high-quality service provisioning,`
- p.1: `information [3], [4], [5], [6] and receiver states (e.g., play-`
- p.1: `back buffer occupancy [7], [8], [9], [10]). In recent years,`
- p.1: `Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14],`
- p.1: `Motivation. To solve this issue, a solution called Oboe [15]`
- p.1: `Pensieve [11] and Oboe [15], using a randomly selected`
- p.2: `rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10],`
- p.2: `[16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26],`
- p.2: `[27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37]`
- p.2: `and learning-based algorithms [11], [15], [38], [39], [40],`
- p.2: `[41], [42], [43], [44], [45], [46], [47], [48], [49], [50],`
- p.2: `[51], [52], [53], [54].`
- p.2: `based algorithms [3], [4], [5], [6], first try to predict the`
- p.2: `CS2P [5] focused on the optimization of network bandwidth`
- p.2: `algorithms [7], [8], [9], [10] aim to maintain the playback`
- p.3: `MPC [27] estimated the future throughput by calculating the`
- p.3: `approaches, such as the reinforcement learning based [11],`
- p.3: `[39], [40], [55], imitation learning based [41], and hybrid`
- p.3: `learning-heuristic algorithms [38]. Pensieve [11] was a pio-`
- p.3: `trast to Pensieve, Comyco [41] trained its neural network`
- p.3: `level. Stick [38] integrates a heuristic ABR algorithm with a`
- p.3: `several approaches have been proposed. Oboe [15] proposed`
- p.3: `Other approaches, such as [56] and [57], introduced meta-`
- p.3: `encountering dynamic network conditions. In [58] and [59],`
- p.3: `faster and more accurate convergence. Additionally, [14], [53]`
- p.3: `transmission performance. For example, in [60], a flow-based`
- p.3: `by [61] conducted a systematic study for various prediction`
- p.3: `Other related works, such as [13], [62], [63], [64], have`
- p.4: `or m throughput measurements, as shown in Eq. (3). Then`
- p.4: `K-means [65], a classic clustering algorithm, is adopted to`
- p.4: `Eq. (4)), where each cluster contains segments with similar`
- p.4: `we mark the trace as “uncertain” according to Eq. (5). This`
- p.4: `labelsegment = {l1, l2, . . . , lp}`
- p.4: `, ∈[0, k −1]`
- p.5: `residual structure [66] into the backbone. This structure`
- p.5: `in Eq. (6), to train the CNN model for network condition`
- p.6: `Similar to the approach used in Pensieve [11], we employ`
- p.6: `method [67] as the basic training algorithm. The state input,`
- p.6: `Similar to Pensieve [11], we used a simulator with a 60-`
- p.6: `provided by FCC [68], a 3G/HSDPA mobile dataset collected`
- p.6: `in Norway [69], a 4G/LTE bandwidth from Belgium [70], a`
- p.6: `mixed dataset provided in Oboe [15], and another mobile trace`
- p.6: `dataset provided in the ACM multimedia grand challenge [71])`
- p.7: `at bitrates in {135, 340, 835, 1350, 2640} Kbps according`
- p.7: `with two heuristic ABR algorithms: buffer-based (BB) [7]`
- p.7: `and MPC [27], as well as two state-of-the-art learning-based`
- p.7: `ABR algorithms: Pensieve [11] and Oboe [15]. For the Oboe`
- p.7: `improvements comparable to the original models in [11], [15],`
- p.7: `in MPC [27], which was defined as`
- p.7: `defined in Eq. (7), where Rn represents the video bitrate, and`
- p.7: `perceived user quality. As revealed in [72], the relationship`
- p.9: `general QoE definition in Eq. (7). We found ANT improved the`
- p.11: `2019 ACM multimedia grand challenge [71], in which the`
- p.11: `1200, 1850} Kbps. We set q(Rn) = frame_time_length × Rn`
- p.11: `as the video quality metric [71], where frame_time_length`
- p.12: `[1] “Cisco visual networking index: Global mobile data traffic forecast`
- p.12: `[2] Y. Xu, J. Yin, Q. Yang, and L. Yang, “Media production using cloud`
- p.12: `[3] C. Liu, I. Bouazizi, and M. Gabbouj, “Rate adaptation for adaptive`
- p.12: `[4] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and`
- p.12: `[5] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation`
- p.12: `[6] K. Miller, A.-K. Al-Tamimi, and A. Wolisz, “QoE-based low-delay`
- p.12: `[7] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A`
- p.12: `[8] T.-Y. Huang, R. Johari, and N. McKeown, “Downton abbey without the`
- p.12: `[9] K. Miller, E. Quacchio, G. Gennari, and A. Wolisz, “Adaptation`
- p.12: `[10] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal`
- p.12: `[11] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream-`
- p.12: `[12] H. Chen et al., “T-gaming: A cost-efficient cloud gaming system`
- p.12: `[13] F. Y. Yan et al., “Learning in situ: A randomized experiment in video`
- p.12: `[14] Z. Xia, Y. Zhou, F. Y. Yan, and J. Jiang, “Genet: Automatic curricu-`
- p.12: `[15] Z. Akhtar et al., “Oboe: Auto-tuning video ABR algorithms to network`
- p.12: `[16] E. Kurdoglu, Y. Liu, Y. Wang, Y. Shi, C. Gu, and J. Lyu, “Real-time`
- p.12: `[17] X. K. Zou et al., “Can accurate predictions improve video streaming in`
- p.12: `[18] S. Kim and C. Kim, “XMAS: An efficient mobile adaptive streaming`
- p.12: `[19] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari,`
- p.13: `[20] A. Beben, P. Wiundefinedniewski, J. M. Batalla, and P. Krawiec,`
- p.13: `[21] G. Tian and Y. Liu, “Towards agile and smooth video adaptation in`
- p.13: `[22] C. Zhou, C. Lin, X. Zhang, and Z. Guo, “Buffer-based smooth rate`
- p.13: `[23] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming`
- p.13: `[24] C. Wang, A. Rizk, and M. Zink, “SQUAD: A spectrum-based quality`
- p.13: `[25] A. Mansy, B. Ver Steeg, and M. Ammar, “SABRE: A client based`

## 8. Texto crudo completo por página

> Mantener este bloque para Codex si necesita comprobar contexto literal. Puede contener errores de orden por columnas del PDF. Para fórmulas exactas o tablas complejas, usar PDF original.


### Página 1

```text
808
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
Learning Accurate Network Dynamics for
Enhanced Adaptive Video Streaming
Jiaoyang Yin
, Hao Chen
, Member, IEEE, Yiling Xu
, Member, IEEE,
Zhan Ma
, Senior Member, IEEE, and Xiaozhong Xu
, Member, IEEE
Abstract—The adaptive bitrate (ABR) algorithm plays a cru-
cial role in ensuring satisfactory quality of experience (QoE) in
video streaming applications. Most existing approaches, either
rule-based or learning-driven, tend to conduct ABR decisions
based on limited network statistics, e.g., mean/standard deviation
of recent throughput measurements. However, all of them lack
a good understanding of network dynamics given the varying
network conditions from time to time, leading to compromised
performance, especially when the network condition changes
significantly. In this paper, we propose a framework named ANT
that aims to enhance adaptive video streaming by accurately
learning network dynamics. ANT represents and detects specific
network conditions by characterizing the entire spectrum of
network fluctuations. It further trains multiple dedicated ABR
models for each condition using deep reinforcement learning.
During inference, a dynamic switching mechanism is devised to
activate the appropriate ABR model based on real-time network
condition sensing, enabling ANT to automatically adjust its
control policies to different network conditions. Extensive exper-
imental results demonstrate that our proposed ANT achieves
a significant improvement in user QoE of 20.8%-41.2% in
the video-on-demand scenario and 67.4%-134.5% in the live-
streaming scenario compared to state-of-the-art methods, across
a wide range of network conditions.
Index Terms—Network dynamics learning, video on demand,
live streaming, adaptive bitrate, reinforcement learning, quality
of experience.
I. INTRODUCTION
R
ECENT years have witnessed an exponential increase
in the volume of HTTP-based video streaming traf-
fic [1], [2]. To assure high-quality service provisioning,
adaptive bitrate (ABR) algorithms have been developed to
dynamically select the appropriate bitrate for each video
chunk, mitigating the network fluctuations and achieving satis-
factory Quality of Experience (QoE) in time-varying network
connections.
Manuscript received 8 February 2024; revised 17 April 2024; accepted
24 April 2024. Date of publication 17 May 2024; date of current version
13 September 2024. This work was supported in part by the National
Natural Science Foundation of China under Grant 62371290, Grant 62101241,
and Grant U20A20185; and in part by the 111 Project under Grant
BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this
work.) (Corresponding author: Yiling Xu.)
Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network
Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China
(e-mail: jiaoyangyin@sjtu.edu.cn; yl.xu@sjtu.edu.cn).
Hao Chen and Zhan Ma are with the Electronic Science and Engineering
School,
Nanjing
University,
Nanjing
210093,
Jiangsu,
China
(e-mail:
chenhao1210@nju.edu.cn; mazhan@nju.edu.cn).
Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA
(e-mail: xiaozhongxu@tencent.com).
Digital Object Identifier 10.1109/TBC.2024.3396698
Background.
Early
ABR approaches
relied on man-
ually fine-tuned heuristics based on network throughput
information [3], [4], [5], [6] and receiver states (e.g., play-
back buffer occupancy [7], [8], [9], [10]). In recent years,
learning-based ABR approaches, utilizing RL-based neural
engines, have gained popularity. These approaches, including
Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14],
leverage neural networks for feature extraction and pol-
icy learning, outperforming fixed rule-based algorithms in
time-varying network environments. However, ensuring user
QoE across a wide range of dynamic network connec-
tions with unpredictable fluctuations remains challenging for
learning-based algorithms. The heterogeneous nature of access
networks, including wireless and wired networks with varying
bandwidth, latency, and buffer capacities, further complicates
the situation. Additionally, the user’s scenario, such as station-
ary or on the move, introduces additional variations in network
conditions. Existing learning-based algorithms typically train
a single model for ABR decisions without adapting to dif-
ferent network conditions. Consequently, the learned neural
model often compromises across various network conditions,
resulting in compromised video quality or frequent rebuffering,
ultimately degrading user QoE.
Motivation. To solve this issue, a solution called Oboe [15]
is proposed to automatically tune video ABR algorithms to
various network conditions. It detects changes in network
states or conditions by analyzing the average and standard
deviation (STD) of throughput and adjusts ABR parameters
accordingly. However, Oboe’s detection of network condi-
tion changes based on limited throughput statistics (average
and STD) may not accurately represent the complex and
diverse network conditions encountered in the real world.
Consequently, Oboe may fail to select the most appropri-
ate ABR parameters. To demonstrate this, we compare the
performance of existing state-of-the-art algorithms, including
Pensieve [11] and Oboe [15], using a randomly selected
network trace. Figure 1 illustrates the instantaneous through-
put/bitrate and the overall QoE results. As shown in Figure 1,
there are several time slots (between the black dashed lines)
with similar average (approximately 3.11 Mbps for slots 1 and
2, and 3.33 Mbps for slots 3 and 4) and STD (approximately
0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and
4) values of throughput. However, network throughput changes
in these time slots exhibit different patterns: slots 1 and 2 have
low-frequency but significant magnitude changes, while slots
3 and 4 have high-frequency but relatively minor magnitude
1557-9611 c⃝2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 2

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
809
Bitrate(Mbps)
Pensieve
Ɵme(s)
QoE
Pensieve
Oboe
ANT
Oboe
ANT
bandwidth
Fig. 1.
Illustration of the necessity for accurate network throughput learning.
changes. Both Pensieve, with a single model, and Oboe, with
its auto-tuning mechanism based on average/STD throughput
values, struggle to differentiate between these different trends.
Pensieve can only rely on a general ABR model trained on
all network traces, while Oboe continues to choose the second
ABR model (3-6 Mbps, depicted in Section IV-D) before
and after the change point of network conditions (around
180 seconds). As they are unable to accurately sense network
conditions and select the appropriate ABR model in a timely
manner, both Pensieve and Oboe experience greater QoE
degradation after the change point.
Method. In this paper, we propose ANT to enhance adaptive
video streaming by accurately learning network throughput
dynamics across a wide range of network conditions. Unlike
traditional methods that rely on simple mean/STD values, ANT
utilizes a combination of the Euclidean distance from a group
of clustering centers and temporal change patterns extracted
from neural networks of multi-dimensional raw-throughput
measurements to characterize the network condition. Toward
this, we first classify a large-scale dataset of network trace
segments (NTS) collected in the real world into multiple
(e.g., five) clusters by using the classic K-means algorithm.
Each cluster represents a distinct network behavior class and
is assigned a unique network condition number for ANT
as the label. Recognizing that the temporal dynamics of
network throughput significantly impact ABR performance,
we additionally leverage a deep neural network (DNN) to
learn the temporal change patterns from the sequence of raw
throughput data. For each network condition, ANT trains a
dedicated reinforcement learning (RL)-based model for ABR
decisions using the corresponding cluster of network traces.
This allows ANT to learn and adapt to specific patterns
of network dynamics and improve decision-making based
on past experiences. During inference, ANT employs the
aforementioned trained DNN to recurrently detect the network
condition and selects the appropriate ABR model accordingly.
By effectively adapting to different network behaviors and pat-
terns, ANT can provide optimal video streaming experiences
for users in diverse network environments.
Contribution. The main contributions of this paper can be
summarized in three aspects:
• Improved characterization of network throughput dynam-
ics. Instead of relying solely on mean and standard
deviation values, we propose using the Euclidean distance
from clustering centers and the temporal change pat-
tern in multi-dimensional raw-throughput measurements
to accurately characterize network throughput dynamics
over time. This approach provides a better differentiation
of typical network behaviors.
• ANT framework for condition-wised multi-model ABR
control. We introduce ANT, a framework that generates
different ABR control policies for different network con-
ditions. ANT utilizes a well-designed DNN for recurrent
network condition detection and activates the appropriate
ABR model accordingly. This enables ANT to make better
ABR decisions for ensuring satisfactory QoE across a
wide range of network conditions.
• Evaluation through simulations and field tests. We val-
idate the effectiveness of ANT through simulations and
field tests. We compare ANT against state-of-the-art
ABR algorithms using public network trace datasets
and a proprietary dataset collected from the large-scale
Tencent video hosting system distributed worldwide. In
both video-on-demand (VoD) and live-streaming (LS)
scenarios, ANT demonstrates significant improvements in
QoE compared to existing approaches.
The remainder of the paper is organized as follows.
Section II reviews related work on ABR algorithms and
network dynamics learning. Section III introduces the design
details of the proposed ANT, including its architecture, key
modules, and implementation. The experimental results and
analysis for ANT are presented in Section IV. The discussion
and conclusion of this work can be found in Sections V
and VI, respectively.
II. RELATED WORK
ABR algorithms with a fixed model. Existing state-of-the-
art ABR algorithms can be divided into two main categories:
rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10],
[16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26],
[27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37]
and learning-based algorithms [11], [15], [38], [39], [40],
[41], [42], [43], [44], [45], [46], [47], [48], [49], [50],
[51], [52], [53], [54].
The rule-based algorithms can be further classified into
rate-based, buffer-based, and hybrid-control approaches. Rate-
based algorithms [3], [4], [5], [6], first try to predict the
available network bandwidth and then select the highest
available bitrate below the estimated bandwidth. For example,
CS2P [5] focused on the optimization of network bandwidth
prediction problems to improve initial and subsequent adaptive
streaming. However, it is still challenging to predict a specific
value for network bandwidth in practice, resulting in poor
performance for this type of ABR algorithms. Buffer-based
algorithms [7], [8], [9], [10] aim to maintain the playback
buffer occupancy at a pre-configured level to guarantee the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 3

```text
810
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
fluency of video playback. Generally, these buffer-based
algorithms can better avoid rebuffering to some extent, but
they suffer from low video quality due to their conservative
bitrate selections. To overcome the shortcomings of these
two techniques, some hybrid-control ABR algorithms attempt
to make bitrate decisions based on both network throughput
prediction and buffer occupancy simultaneously. For example,
MPC [27] estimated the future throughput by calculating the
harmonic mean of the throughput values from the last five
chunks and attaching a discount factor, then went through all
bitrate options and selects the one that maximizes a given
QoE metric. However, MPC also relies on accurate throughput
prediction, which can encounter similar problems to rate-based
algorithms.
Due to the limitations of rule-based algorithms, recent
research has shifted towards learning-based hybrid control
approaches, such as the reinforcement learning based [11],
[39], [40], [55], imitation learning based [41], and hybrid
learning-heuristic algorithms [38]. Pensieve [11] was a pio-
neering work that trained a neural network model using
reinforcement learning to make bitrate decisions, which solely
relied on observations collected from video players. In con-
trast to Pensieve, Comyco [41] trained its neural network
model using imitation learning, resulting in a significant
reduction in training time while maintaining the same QoE
level. Stick [38] integrates a heuristic ABR algorithm with a
learning-based method to enhance its performance and reduce
computational overhead. It achieves this by training a neural
network to dynamically control the buffer threshold parameter
of an existing buffer-based algorithm. Taking advantage of
the capabilities of neural networks in feature extraction and
policy learning, these learning-based algorithms have shown
superior performance compared to early rule-based algorithms
that utilize fixed heuristics across various network conditions.
However, they often rely on a single neural network model for
ABR decisions and lack specialization for different network
conditions, resulting in compromised performance.
Auto-tuning ABR parameters to network conditions.
ABR algorithms that rely on a single model or fixed
parameters often struggle to adapt to the complexities of mod-
ern network conditions, resulting in significant performance
degradation during video streaming. To address this issue,
several approaches have been proposed. Oboe [15] proposed
to auto-tune the parameters of ABR algorithms based on
network conditions. It detected changes in network states
using Bayesian change point detection algorithms based on
average and standard deviation of throughput measurements,
and then dynamically selected appropriate parameters for the
ABR algorithm to adapt to the current network condition.
Other approaches, such as [56] and [57], introduced meta-
reinforcement learning to perceive changes in network states
and tune the parameters of the policy network. In this way, the
generalization of the neural network can be improved when
encountering dynamic network conditions. In [58] and [59],
federated reinforcement learning was adopted to enable their
neural networks to handle various network conditions and
user-end characteristics. Taking advantage of the idea of
categorization and aggregation, the policy network can achieve
Fig. 2.
Overall architecture of ANT-powered adaptive video streaming.
faster and more accurate convergence. Additionally, [14], [53]
introduced automatic curriculum learning, which involved
a gradual migration of training from a simple to a com-
plex network environment, significantly improving training
performance and model generalization. However, these works
mainly rely on limited throughput statistics (i.e., average and
STD) to assess network dynamics and can easily lead to
inaccurate recognition of network condition changes, finally
degrading the ABR performances.
Learning network dynamics. In addition to optimizing
adaptive bitrate (ABR) algorithms, researchers have also
focused on learning network dynamics to enhance video
transmission performance. For example, in [60], a flow-based
throughput classification method was proposed to predict the
bitrate of traffic flow based on factors such as IP address,
network prefix, protocol, and start timestamp. Another study
by [61] conducted a systematic study for various prediction
algorithms and analyzed their performance when applied in
the prediction of throughput in mobile networks, promoting
the employment of throughput prediction in ABR algorithms.
Other related works, such as [13], [62], [63], [64], have
explored efficient methods for predicting throughput or band-
width and utilizing learned network dynamics to optimize
adaptive video streaming. However, these approaches often
face challenges in capturing comprehensive network statis-
tics across different layers and accurately predicting specific
throughput or bandwidth values. This limits their effectiveness
and efficiency when applied to enhance application-layer ABR
algorithms.
III. ANT DESIGN
State-of-the-art ABR algorithms attempt to train a general
neural network model for bitrate decisions to adapt to a wide
range of network conditions. However, during training, this
general model easily converges to a compromised policy with
average performance across all considered network conditions
rather than achieving optimal performance. To this end, we
propose a condition-wised multi-model framework, named
ANT, to optimize the performance of adaptive video streaming
under each network condition.
In this section, we will introduce the design details of
ANT, including the overall architecture, key modules, and their
corresponding implementation.
A. Architecture
The overall architecture of ANT-powered adaptive video
streaming is shown in Figure 2. On the media server, videos
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 4

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
811
are segmented into a series of time-aligned chunks, each of
which is further encoded at several bitrate levels for requests.
During video streaming, the ANT server decides to request
each video chunk at which bitrate based on network statistics
and client-side playback status. Then the client-side video
player downloads the video chunk at the decided bitrate and
stores them in a playback buffer for video decoding and
playing. This process continues until either the end of the
video is reached or the user chooses to quit the streaming
session.
For the ANT server, two key modules have been developed
to support superior-performance ABR decisions across dif-
ferent network conditions: network condition detection and
condition-wised multi-model ABR decision. In the network
condition detection module, a one-dimensional convolutional
neural network (1D-CNN) model is trained to accurately
detect the network condition by learning and recognizing
the temporal change pattern present in historical throughput
measurements. The multi-model ABR decision module stores
several RL-based ABR models, each of which is pre-trained
using a large dataset of throughput traces collected under
similar network conditions. Based on the output from the
network condition detection module, one of the pre-trained
models is dynamically selected to make adaptive bitrate
(ABR) decisions. The bitrate decision is made by taking into
account both network statistics and player status. The general
procedure for the proposed architecture can be formulated as
follows:
condition = f1D−CNN(throughputhistorical)
(1)
action = fABR

statenetwork, stateplayer, condition

(2)
B. Network Condition Detection
Different from existing approaches that rely on simple
statistical features of the throughput data like average and
STD values, our network condition detection module utilizes
a powerful CNN model to extract comprehensive features
from raw throughput data, enabling it to learn and accurately
determine the current network condition. This information is
then used to drive the selection of the appropriate model in the
subsequent condition-wise multi-model ABR decision module.
Label generation with unsupervised clustering. Existing
network datasets often lack reliable labels indicating real
network conditions, which poses a challenge for training and
validating neural networks in our model. To overcome this
issue, we propose a trace aggregation mechanism that dis-
tinguishes network conditions based on the distance between
network throughput traces (as illustrated in Figure 3). The
original network traces are first split into several equal-length
segments that contain throughput information in t seconds
or m throughput measurements, as shown in Eq. (3). Then
K-means [65], a classic clustering algorithm, is adopted to
cluster these trace segments based on the Euclidean distance
between them. As a result, we obtain k clusters (as shown in
Eq. (4)), where each cluster contains segments with similar
network behaviors or conditions. We denote the label of the
i-th segment in the same network trace as li. Finally, the entire
network trace can be assigned a label, denoted as labeltrace,
Fig. 3.
Illustration of the trace aggregation mechanism.
which represents the most frequent network condition across
all segments. However, if the frequency of the most dominant
network condition does not exceed a predefined threshold h,
we mark the trace as “uncertain” according to Eq. (5). This
accounts for cases where the network condition is ambiguous
or lacks a clear majority.
trace =
⎧
⎪⎨
⎪⎩
x1, x2, . . . , xm




Segment1(t second)
, xm+1, . . . , x2m




Segment2(t second)
, . . . , xn−m+1, . . . , xn




Segmentp(t second)
⎫
⎪⎬
⎪⎭
(3)
labelsegment = {l1, l2, . . . , lp}
= K −means.fit(Segment).labels
, ∈[0, k −1]
(4)
labeltrace =
⎧
⎨
⎩
li,
if numli/p ≥h
uncertain,
if numli/p < h,
li ∈labelsegment
(5)
CNN model for condition detection. Since we adopt
K-means as the clustering algorithm, the intuitive idea
is to perform condition detection directly based on the
Euclidean distance. However, due to the limited amount of
data used for clustering, only using the Euclidean distance
from a group of fixed centers for condition detection can
lead to inaccurate category judgments in real situations.
Specifically, when unseen network fluctuations occur, even
subtle changes may lead to large shifts in distance calculations.
To address this issue, we propose a CNN model that learns
the temporal change patterns within a series of network
throughput data. By extracting and utilizing these patterns as
features, our approach enables more accurate condition detec-
tion in real transmission environments. Experimental results
presented in Section IV-E1 validate the effectiveness of our
approach.
Using network trace segments and their corresponding
condition labels as training samples, we train a neural network
to detect the current condition in this module. This neu-
ral network extracts features from the input of historical
throughput measurements. The neural network structure of our
proposed model for network detection model is depicted in
Figure 4. The backbone of our network is a 1D-CNN, which is
well-suited for handling high-dimensional network throughput
data. The input to the neural network is a sequence of historical
network throughput data, and the output is the detected current
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 5

```text
812
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
Fig. 4.
The neural network structure of the proposed model for network condition detection.
network condition. In the neural network, three convolutional
layers are devised to extract hierarchical features. These layers
have the same structure but differ in their hyperparameters,
such as the size of the convolutional kernel and the number
of output channels. To improve feature extraction capability
and condition detection accuracy, we add several optimized
operations to the backbone network.
• Multiple perceptual field. Considering the diverse feature
scales present in network throughput data, we introduce a
multi-perceptual-field mechanism to our neural network.
This mechanism incorporates multi-scale convolutional
kernels within each convolutional layer, allowing for the
effective extraction of features at different scales from
the network throughput data. Specifically, we use three
distinct convolutional scales in each layer, namely 3 × 1,
5 × 1, and 7 × 1 kernels, and then concatenate features
from different scales of convolution operation in the
channel dimension.
• Channel shuffle. To improve the stability and generaliza-
tion of our neural model, we adopt the channel shuffle
operation to disturb the original order of concatenated
feature channels obtained from the multi-scale convo-
lution operation. The feature channels are first divided
into three equal-sized groups. Then, the feature matrix is
reshaped, transposed, and reshaped to make the feature
channels shuffled.
• Attention mechanism. Since different feature channels
contribute differently to the final output, we integrate
a squeeze-and-excitation (SE) module into the network
backbone. The SE module acts as an attention mech-
anism, assigning weights to the feature channels based
on their importance. The SE module consists of two
branches: one branch transmits the original signal, while
the other branch performs the SE operation. After per-
forming the SE operation, each channel is assigned a
weight value based on its importance. These weight
values are then multiplied element-wise with the corre-
sponding channels in the original signal.
• Residual structure. To address the issues of feature
submerging of the shallow layer and gradient van-
ishing/explosion in deeper CNNs, we incorporate the
residual structure [66] into the backbone. This structure
transmits shallow features directly to deeper layers and
combines them with abstract features, enabling more
efficient and stable training.
• Normalization and dropout. In addition to the optimized
operations mentioned earlier, we employ two normal-
ization techniques to further enhance the performance
of our neural network: mean standardization and batch
normalization. These two normalization operations lead
to faster convergence and improved training stability.
Furthermore, dropout is utilized in fully connected layers
to regularize the model and prevent overfitting during
training.
We use the binary cross-entropy loss function, as shown
in Eq. (6), to train the CNN model for network condition
detection. y and ˆy (in one-hot format) represent the label of the
network condition and the output of this model, respectively.
L

ˆy, y

= −

y log ˆy + (1 −y) log(1 −ˆy)

(6)
Network condition inference. After completing the training
of the detection model, the current segment’s network con-
dition can be inferred using previous raw throughput data as
input.
It is worth mentioning that each ABR model is trained using
a large number of traces that correspond to the same specific
network condition. Thus we have devised a sliding window-
based confidence mechanism for the accurate detection of
trace-level network conditions, enabling effective selections of
the appropriate ABR model in the subsequent module. The
chunk-level condition detection is conducted every 20 seconds,
and the results at each step are queued into a sliding window.
The chunk-level result is only accepted as the trace-level
network condition if it matches the results from two out of the
three previous time slots. Otherwise, the “uncertain” status is
designated as the trace-level network condition. In addition,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 6

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
813
Fig. 5.
Illustration of condition-wised multi-model ABR decision module.
when the video streaming system runs in the initial period (i.e.,
60 seconds in the beginning) and there is not enough historical
throughput data to perform condition learning, the general
status corresponding to all various network traces is selected
until the input requirement of the confidence mechanism is
met.
C. Condition-Wised Multi-Model ABR Decision
Multi-model switching mechanism for ABR decision. As
shown in Figure 5, the condition-wised multi-model ABR
decision module is constructed with multiple reinforcement
learning (RL) based ABR models, which share the same neural
network architecture but different model parameters. At a
set interval, one of these trained ABR models is selected to
make bitrate decisions according to the detection results by
the network condition detection module. For different network
conditions, there is a corresponding model trained specifically
for that condition using similar network traces to make ABR
decisions. This ensures that ANT can adapt its decision-making
process to different network conditions, providing optimal
streaming performance.
Training RL-based ABR models. With the trace aggregation
mechanism described in Section III-B, each ABR model can
be trained individually using network traces labeled with the
same condition. During the training of each ABR model, the
learning agent collects various observations from the video
streaming environment, which include network statistics such
as bandwidth or throughput, as well as player status at the
client side like buffer occupancy. These observations are
then fed into the RL neural network, prompting it to select
the appropriate bitrate for the next chunk. After making a
decision, the environment transitions to a new state, and the
agent receives a reward. The RL agent learns to maximize
the expected cumulative discounted reward by continuously
interacting with the video streaming environment.
Similar to the approach used in Pensieve [11], we employ
the state-of-the-art asynchronous advantage actor-critic (A3C)
method [67] as the basic training algorithm. The state input,
neural network structure, and reward function remain consis-
tent with those used in Pensieve’s framework.
D. Implementation
We implemented the CNN-based network condition detec-
tion module and the RL-based ABR decision module using
Tensorflow. For the neural network in the network condition
detection module, we used three types of CNN filters with
sizes 3×1, 5×1, and 7×1. The number of output channels for
each CNN layer was 64×3, 128×3, and 256×3 respectively.
The kernel size in the pooling layers we chose was 2 × 1.
The first layer of the fully connected network had 256 neurons
and 128 neurons were contained in the second layer. For all
convolution operations and pooling operations, we set stride
with 1 and add a padding operation to maintain the data width.
As for other hyper-parameters, we set the learning rate as
0.0001 and batch size as 80 in the training phase. For the
RL-based ABR decision module, we used 16 RL agents to
learn the control policy for bitrate adaptation. In the state
input, we considered the past eight observations from the
environment, which were normalized before being fed into the
neural network. Both the actor network and the critic network
consisted of one 1D-CNN layer with a kernel size of 4 and 128
output channels, as well as a fully connected layer with 128
neurons. The learning rates for the actor and critic networks
were set to 0.0001 and 0.001, respectively. The entropy weight
of the actor network was set to 0.5. We used a batch size of
100 for training. The training and testing of neural networks
were on a Ubuntu 16.04 server equipped with Intel Xeon CPU
E5-2683 v4 @2.10GHz and Nvidia GeForce GTX 1080Ti 11G
GPU.
IV. EXPERIMENT RESULTS AND ANALYSIS
A. Experiment Setup
Similar to Pensieve [11], we used a simulator with a 60-
second buffer capacity to conduct trace-driven video streaming
sessions for training and testing all the schemes considered.
The network traces, video information, and baselines used in
this paper are as follows.
Network traces. Since it is time-consuming to “experience”
video downloads in the real-world streaming environment,
we conducted simulations over a wide range of network
traces in the training and testing phases. These traces were
collected from public datasets (including a broadband dataset
provided by FCC [68], a 3G/HSDPA mobile dataset collected
in Norway [69], a 4G/LTE bandwidth from Belgium [70], a
mixed dataset provided in Oboe [15], and another mobile trace
dataset provided in the ACM multimedia grand challenge [71])
and a Tencent dataset (including WiFi network traces and
3G/4G network traces). The Tencent dataset was a proprietary
network trace dataset that was collected from the Tencent
video platform, in which the videos experienced actual queries
and downloads. There were nearly 2000 traces in the dataset,
each of which contained about 30 minutes of throughput data
on average. The average throughput of each trace ranged from
less than 1Mbps to more than 10Mbps. Benefiting from user
ends distributed widely throughout the world, these network
traces were collected from China, Philippines, Thailand, India,
and Indonesia. The network types of user ends included Wifi
and 3G/4G, which could cover a wide range of network
conditions and application scenarios. In the network trace
file, time information (second) and corresponding through-
put/bandwidth information (Mbit per second) were contained.
We randomly divided all 2658 traces into the training set and
the testing set, by the proportion of 80% and 20%, respectively.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 7

```text
814
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
The network throughput segments were generated in t-second
(t=20) duration, and the classification threshold in the trace
aggregation mechanism was set as 2/3. Consequently, ANT
conducted network condition detection every 20 seconds.
Video information. We collected a diverse set of videos
from the Tencent video platform, encompassing various types
of content such as newscasts, sports events, movies, and
shows. These videos were encoded by the NVENC codec
at bitrates in {135, 340, 835, 1350, 2640} Kbps according
to the Tencent video platform settings. Additionally, these
videos were divided into 200 chunks, with each chunk lasting
approximately 4 seconds, resulting in a total playback duration
exceeding 10 minutes.
Baselines. In the evaluation, we compared our approach
with two heuristic ABR algorithms: buffer-based (BB) [7]
and MPC [27], as well as two state-of-the-art learning-based
ABR algorithms: Pensieve [11] and Oboe [15]. For the Oboe
algorithm, we trained 5 neural network models for ABR
decisions using network traces with different average through-
put ranges: 0-3Mbps, 3-6Mbps, 6-9Mbps, 9-12Mbps, and
over 12Mbps. We retrained the RL-based models of Pensieve
and Oboe according to our specific settings. The validation
results demonstrated that these retrained models achieved QoE
improvements comparable to the original models in [11], [15],
when compared to rule-based methods. The training details
for each model were the same as the proposed ANT described
in Section III-C.
QoE metrics. We adopted the general QoE metric proposed
in MPC [27], which was defined as
QoE =
N

n=1
q(Rn) −µ
N

n=1
Tn −
N−1

n=1
|q(Rn+1) −q(Rn)| (7)
for a video with N chunks. The QoE metric is an objective
indicator used to assess the quality of the viewing experi-
ence. This study considers multiple optimization objectives,
including maximizing bitrate, minimizing rebuffering time,
and maximizing smoothness. The general QoE metric is
defined in Eq. (7), where Rn represents the video bitrate, and
q(Rn) is the mapping function that converts the bitrate to the
perceived user quality. As revealed in [72], the relationship
between quality and bitrate is approximately linear in the low
bitrate stage. Moreover, the linear QoE metric/reward function
can facilitate the derivation and gradient updating during the
training phase of the RL model, leading to easier convergence
in the complex environment, compared to other non-linear
forms. Considering that the maximum bitrate of the video
content adopted in this paper is 2.64Mbps, it is acceptable
to evaluate the viewing quality using the linear QoE metric.
Therefore, in this work, we set the linear form q(Rn) = Rn,
which is the same as the approach used in MPC, Pensieve, and
Oboe. Tn represents the rebuffering time for each video chunk,
and µ is the corresponding penalty coefficient. The rebuffering
time refers to the time interval from the buffer depletion to the
restoration of video playback. Similar to Pensieve, the rebuffer
penalty coefficient was configured as the maximum video
bitrate of 2.64 Mbps in this work, in order to minimize viewing
Fig. 6.
SSE and DBI results over different k values.
TABLE I
AVERAGE AND STANDARD DEVIATION VALUE OF
THE THROUGHPUT FOR EACH CONDITION
lag as much as possible. The last term penalizes the quality
fluctuation between adjacent chunks to favor smoothness.
B. Network Trace Clustering Performance
During network trace clustering, the number of clusters k
has a significant impact on the performance of the K-means
algorithm and the final ABR decision. To this end, we con-
ducted the K-means clustering with the parameter k varying
from 2 to 8 and found the best one on the metrics of
the sum of squared error (SSE) and Davies-Bouldin index
(DBI). The results using different values of k are shown in
Figure 6.
The SSE value gradually decreases with increasing number
of clusters k. When k approaches the most appropriate value,
the downward trend will slow down until convergence. In
contrast, the DBI value gradually increases with increasing
number of clusters, as DBI calculates the ratio of the degree of
separation between clusters to the degree of aggregation within
a cluster. Given these two indicators, we found the turning
point where the trend slowed down occurred at k = 5. Thus,
we set the number of clusters as 5 for trace segments and 6 for
entire traces considering an additional “uncertain” condition.
The average value and STD of throughput under each con-
dition were calculated and reported in Table I. Additionally,
we plotted the throughput distribution of each condition at
both segment and trace levels in Figure 7. From these results,
we found that the different conditions of the network traces
were well separated, which verified the effectiveness of the
proposed trace aggregation mechanism.
C. Network Condition Detection Performance
Through the network trace clustering, we obtained numer-
ous throughput trace segments and corresponding condition
labels as samples. These samples were randomly divided into
a 80% training set and a 20% testing set. The training of the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 8

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
815
Fig. 7.
The throughput distribution of each condition.
TABLE II
HYPER-PARAMETERS SETTINGS AND TESTING RESULTS OF
BASELINES AND OUR CNN-BASED DETECTION MODEL
CNN-based model for network condition detection converged
after 100 epochs.
To better evaluate our proposed CNN-based detection
model, we also trained a fully connected network (FC), a
convolutional-1D (CONV-1D) network only, a long-short-term
memory (LSTM) network, and a gated recurrent unit (GRU)
network for performance comparison. These models were
trained and tested using the same dataset as our CNN-based
detection model. The corresponding hyperparameter settings
for each considered model were listed in Table II. The testing
accuracy results were also reported in the table.
It can be found that our model achieves the best detection
accuracy, reaching 98.56%. While the baselines fail to get
a satisfactory accuracy, all below 75%. The superiority in
detection accuracy comes mainly from the multi-perceptual
field mechanism, channel weight learning, and residual struc-
ture in the proposed CNN-based model. These results also
demonstrated the effectiveness of adding related optimized
operations to baseline network architectures.
With the ability to accurately detect current network condi-
tions and the confidence mechanism for trace-level condition
inference, the network condition detection module can effec-
tively drive the model switching in the subsequent multi-model
ABR decision module for better bitrate decisions based on
historical throughput measurements.
D. Overall QoE Performance
Now we evaluated the performance of ANT for bitrate
adaptation on the considered QoE metric and its individual
components, including bitrate utility (in Mbps), rebuffering
penalty (in seconds), and smoothness penalty (in Mbps), under
P
O
P
O
P
O
P
O
Fig. 8.
Performance comparison on the considered QoE metrics under both
public traces and Tencent traces for the VoD scenario.
2
1
0
1
2
0.0
0.2
0.4
0.6
0.8
1.0
CDF
QoE
BB
MPC
Pensieve
Oboe
ANT
BeƩer
0.5
1.0
1.5
2.0
2.5
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Bitrate(Mbps)
BeƩer
BB
MPC
Pensieve
Oboe
ANT
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Rebuffering(s)
BB
MPC
Pensieve
Oboe
ANT
BeƩer
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Smoothness(Mbps)
BB
MPC
Pensieve
Oboe
ANT
BeƩer
Fig. 9.
Final CDF curve under public traces.
diverse network traces in the testing dataset. The results were
shown in Figure 8 to Figure 10.
As shown in Figure 8, the proposed ANT achieves the best
QoE performance compared to baselines, including heuristic
methods (BB and MPC) and learning-based methods (Pensieve
and Oboe), under both the public and Tencent network traces.
Specifically, ANT achieves 1.52 (1.79) of average QoE for
each video chunk under the public (Tencent) network traces,
which is 31.07% (12.65%) higher than that of the best state-
of-the-art Oboe. Compared to the results on the public dataset,
all considered ABR algorithms can achieve higher QoE on
the Tencent dataset. This is because the average bandwidth
of Tencent traces is significantly greater than that of public
traces, supporting a higher bitrate utility in video streaming as
shown in Figure 8. Along with the higher average bandwidth,
the STD of bandwidth in the Tencent dataset is also larger
than that in the public dataset, leading to frequent rebuffering
events for all considered algorithms. For the same reasons, the
QoE improvement of ANT gained over other algorithms on
the Tencent dataset is less than that on the public dataset.
To better understand the QoE gains obtained by ANT, we
analyzed its performance on the individual components in the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 9

```text
816
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
12
10
8
6
4
2
0
2
QoE
0.0
0.2
0.4
0.6
0.8
1.0
CDF
pensieve
oboe
ANT
MPC
buffer_based
pe
pensieve
oboe
ANT
MPC
buffer_based
BB
MPC
Pensieve
Oboe
ANT
BeƩer
0.5
1.0
1.5
2.0
2.5
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Bitrate(Mbps)
BB
MPC
Pensieve
Oboe
ANT
BeƩer
0
1
2
3
4
5
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Rebuffering(s)
BB
MPC
Pensieve
Oboe
ANT
BeƩer
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
1.0
CDF
BB
MPC
Pensieve
Oboe
ANT
Smoothness(Mbps)
BeƩer
Fig. 10.
Final CDF curve under Tencent traces.
TABLE III
THE SITUATIONS OF ABR MODEL SELECTION UNDER 4
RANDOMLY SELECTED NETWORK TRACES
general QoE definition in Eq. (7). We found ANT improved the
average bitrate utility by 16.05% (3.24%) compared to the sec-
ond best-performing Oboe under the public (Tencent) network
traces. On the rebuffering penalty, ANT rivals Pensieve and
Oboe under the public network traces and outperforms them
by respectively 37.39% and 23.54% under Tencent network
traces. Although the smoothness for ANT is slightly worse than
that for MPC, it is kept at an acceptable low level. So ANT
does not optimize every QoE goal, but balances each factor
to optimize the general QoE metric. We further calculated the
cumulative distribution function (CDF) of the general QoE
values and its individual components under both the public
traces and Tencent traces, and the results were shown in
Figure 9 and Figure 10 respectively. We observed that ANT
robustly performed better than all state-of-the-art algorithms
under different network traces. As Pensieve and Oboe were
the best-performing ABR algorithms among all the considered
baselines, we limited our evaluations to comparing ANT with
these two algorithms in the following.
These QoE improvements for ANT are mainly derived from
the effective representation of network throughput dynamics
and the accurate detection of network conditions. When
a change is detected in the network condition, ANT can
automatically switch to the appropriate ABR model for ABR
decisions, which is well-trained under the network traces
with similar temporal change patterns to the current. In
contrast, both Pensieve and Oboe fail to perceive condition
changes and choose the appropriate ABR model in time due
to their inability to learn accurate throughput dynamics. To
demonstrate this, we have captured the situations of ABR
3
2
1
0
1
2
0.0
0.2
0.4
0.6
0.8
1.0
ANT
ANT-DIST
Fig. 11.
Comparing the default ANT with ANT-DIST on the average QoE
and full CDF of QoE under unseen network traces. The average performances
are shown on the left and the CDF performances are shown on the right.
model selections in Table III for Pensieve, Oboe, and ANT
under 4 randomly selected traces. As shown, Pensieve always
utilized its general ABR model. Although Oboe supports auto-
tuning its model parameters to different network conditions,
Oboe did not conduct ABR model switching because it failed
to detect any network condition change. While only ANT
succeeded in detecting these changes and performed model
switching in time, leading to the final QoE improvements.
E. ANT Deep Dive
1) Ablation Study: To evaluate the necessity of the CNN
model introduced in the condition detection module, we
developed another version of ANT (called ANT-DIST) and
compared it with the default ANT for the ablation study. In
ANT-DIST, Euclidean distance is used to perform network con-
dition detection by calculating it from a group of fixed centers
already obtained in the trace clustering. In the following, we
compared the specific implementation of network condition
detection in ANT and ANT-DIST.
• ANT-DIST: distinguishes the network condition based
on the Euclidean distance from the clustering centers
obtained in Section IV-B. The network condition is
determined by the nearest distance between the current
throughput segment (20s) and a certain clustering center.
• ANT: discriminates the network condition based on
a powerful CNN-based model and a sliding window-
based confidence mechanism proposed in this paper (see
Section III-B). Besides the Euclidean distance, the CNN
model further extracts the temporal change pattern resid-
ing in the throughput sequence for segment-level network
condition detection. Then the confidence mechanism is
applied to determine the trace-level network condition.
Except for the network condition detection method, the
other details of ANT-DIST remain the same as ANT.
We set up a comparative experiment using a total of 100
network traces that were collected by the Tencent video plat-
form in Southeast Asia. Note that these traces are not included
in either the training dataset or the testing dataset mentioned
above. This indicates that the trained ABR models do not
possess knowledge about these unseen network conditions.
As shown in Figure 11, the default ANT also outperforms
ANT-DIST on both the average QoE by 21.7% and the
full CDF of QoE. Taking the individual QoE components
into account, ANT reduces the rebuffering time by 32%
compared to ANT-DIST at a similar bitrate utility. These
results demonstrate that ANT-DIST, which uses the Euclidean
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 10

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
817
8
6
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Pensieve
Oboe
ANT
Standard DeviaƟon of QoE
BeƩer
0
2
4
50
CDF
BeƩer
Standard DeviaƟon of QoE
Pensieve
Oboe
ANT
1.0
0.8
0.6
0.4
0.2
0.0
0
10
20
40
30
Fig. 12.
Comparing ANT with other algorithms on the standard deviation of
QoE in the form of full CDF.
distance to determine the network conditions, fails to select
the appropriate ABR model that matches the current network
condition for optimal bitrate decisions. This is because the
clustering centers are derived from limited throughput traces.
For more traces not taken into account, using the distance from
these fixed clustering centers for condition identification tends
to result in serious bias. For example, ANT-DIST can identify a
similar trace to labeled one as an alternate network condition,
even if its average throughput slightly differs but with the
throughput change trend preserved. In contrast, ANT further
learns the temporal change pattern residing in the throughput
sequence during training its CNN-based model, which serves
as an additional feature when detecting the network condition.
Benefiting from the accurate perception of network dynamics,
ANT can continuously select the appropriate ABR model
to perform better bitrate decisions, especially under unseen
network traces.
2) Performance Stability Analysis: As ANT performs ABR
model switching whenever a change of network condition is
detected, one concern is whether ANT can perform stably
across video chunks during video streaming. To evaluate the
stability performance of ANT, we compared the standard
deviation of QoE for ANT and two state-of-the-art ABR
algorithms (i.e., Oboe and Pensieve). The results are depicted
in Figure 12. We found that ANT either matched or exceeded
the stability performance of the best existing ABR algorithms.
On the public dataset, about 90% of traces are achieved with
better stability using ANT. And on the Tencent dataset, ANT
outperforms other algorithms on the stability in all considered
network traces.
To demonstrate the stability performance more clearly, we
provided the instantaneous QoE achieved and bitrate decision
for each chunk under a randomly selected network trace in
Figure 13. As shown, ANT always outperforms other algo-
rithms throughout the video streaming session. This is because
ANT can effectively detect the change of network conditions
(indicate by black dashed lines in Figure 13), enabling it to
switch between ABR models as needed. This ensures ANT to
make better bitrate decisions and achieve high instantaneous
QoE regardless of how network conditions change. In contrast,
Pensieve is unable to adapt its model parameters, and Oboe
fails to detect these network condition changes, resulting in
significant performance degradation on the instantaneous QoE
metric.
Bitrate(Mbps)
Pensieve
Oboe
ANT
QoE
Pensieve
Oboe
ANT
chunk
Fig. 13.
An example of performance comparison between ANT and other
algorithms on the instantaneous QoE metric.
P
O
Fig. 14.
Performance comparison in the real-world environment.
3) Resource Overhead and Time Consumption: During the
inference phase, the DNN-based condition detection model
consumed approximately 10% of the CPU utilization on the
Intel Xeon E5-2683 v4 @2.10GHz processor and 7GB of
memory on the Nvidia GeForce GTX 1080Ti 11G GPU.
The inference time for a batch of 20 input throughput data
segments was within 500ms. Meanwhile, the RL-based ABR
model consumed about 3-8% of the CPU utilization on the
Intel Xeon E5-2683 v4 @2.10GHz processor during inference,
with an inference time of approximately 10-30ms. Taking into
account the adequate buffer length for the adopted scenario,
the introduced latency of the overall learning-based ANT is
within acceptable limits during the actual inference.
4) Performance in Real Transmission Environments: We
further deployed our ANT into an actual video streaming
system of Tencent, and conducted extensive experiments on it
to evaluate ANT’s performance in the real-world environment.
The video content server is located in Shenzhen, China.
We integrated ANT and other ABR baseline algorithms into
separate video players, which were installed on the same
mobile device. The access networks at the user ends consisted
of WiFi and cellular wireless links. Users accessed the video
streaming services indoors (e.g., in a laboratory, office, dining
hall, dormitory, and corridor) or outdoors (e.g., on a road
or street). Users were free to be still or moving during the
streaming session. During the evaluation, video players that
run different ABR algorithms were randomly called at once
to conduct video queries and downloads. Each streaming
session for an ABR algorithm lasted about 30 minutes and
was repeated 10 times to eliminate random errors. Such video
streaming experiments were carried out in both Shanghai and
Shenzhen, covering a vast distance exceeding 1000 kilometers.
Figure 14
illustrates
the
average
QoE
performances
achieved using ANT, Pensieve, and Oboe in real-world
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 11

```text
818
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
P
O
P
O
Fig. 15.
Performance comparison on the average QoE under both public traces (left) and Tencent traces (right) in the live streaming scenario.
network environments. It can be seen that the proposed ANT
achieves the best performance on the average QoE metric.
Throughout the sessions conducted in Shanghai, ANT outper-
forms Pensieve and Oboe with improvement in average QoE
of 58.07% and 39.86%, respectively. In the Shenzhen sessions,
ANT also achieves a remarkable average QoE improvement
of 46.03% and 18.71% compared to Pensieve and Oboe,
respectively. The lower average QoE in the Shenzhen sessions
can be attributed to the poorer network conditions with
lower bandwidth compared to that in Shanghai during testing.
These results demonstrate the superiority and generalizability
of the proposed ANT when operating in real transmission
environments.
5) Extension in the Live Streaming Scenario: Besides the
aforementioned VoD scenario, we also evaluated ANT in the
latency-sensitive live streaming scenario. We implemented
ANT on the live streaming video platform offered by the
2019 ACM multimedia grand challenge [71], in which the
buffer capacity was limited to 2 seconds to meet the low
latency requirement. The video was also provided by the live
streaming platform, which covered a high dynamic range. The
bitrate ladder for live videos was configured as {500, 850,
1200, 1850} Kbps. We set q(Rn) = frame_time_length × Rn
as the video quality metric [71], where frame_time_length
equals 0.04 (in seconds) in our setting. The rebuffer penalty
coefficient was configured as 1.85 in this scenario. Each live
video was streamed through a sequence of frames, and bitrate
selections were made for every GoP, which comprised 50
frames and represented approximately 2 seconds of video
playback. In addition to very limited buffer capacity, the video
content was generated and streamed in real time, so content-
related information including the video length and future
chunk sizes was not available. These features brought a great
challenge for ABR algorithms to deal with underlying network
fluctuations in live streaming.
To accommodate the characteristics of live streaming,
we made essential modifications to ANT’s ABR models.
Specifically, the RL agent’s state input includes throughput
measurements, rebuffering time, the selected bitrate in the
past, and the current receiving frame rate. The first three
state components are fed into a gated recurrent unit (GRU)
layer with 128 units, while the last is input into a fully
connected layer with 128 neurons. Compared to the CNN
utilized in Pensieve, we employed GRU in the neural network
for the limited-buffer live streaming to ensure satisfactory
ABR performance. This is because GRU can more effectively
capture long-term dependencies within the sequential input
2
1
0
1
2
3
4
QoE
0.0
0.2
0.4
0.6
0.8
1.0
CDF
Pensieve
Oboe
ANT
BeƩer
5
0
5
QoE
CDF
Pensieve
Oboe
ANT
BeƩer
1.0
0.8
0.6
0.4
0.2
0.0
30
25
20
15
10
Fig. 16.
Final CDF curve of QoE under both public traces and Tencent
traces.
data. The outputs from these layers are then aggregated in a
hidden layer that applies the softmax function for the actor
network. Finally, the RL agent selects one bitrate from the
given options based on the output of the action probability
distribution. This selection decision is made per GoP to rapidly
adapt to the underlying network fluctuations. Similar to the
VoD scenario, several ABR models were finally trained for
different network conditions using corresponding clusters of
network throughput traces. During the inference phase, the
network condition was determined based on historical through-
put measurements spanning 20 seconds, which subsequently
derived the selection of appropriate ABR models to make
bitrate decisions.
Figure 15 shows the average QoE that each ABR algorithm
achieved on both the public dataset and the Tencent dataset.
Figure 16 provides more detailed results in the form of full
CDFs. It can be found that ANT outperforms Oboe and
Pensieve by 46.01%-98.15% and 60.81%-3.76×, respectively,
on the average QoE metric across a wide range of network con-
ditions (e.g., WiFi, 3G/4G, and broadband connections). The
CDF results also illustrate the superior QoE performance of
ANT in all sessions on the Tencent dataset and approximately
in 80% sessions on the public dataset, compared to these
state-of-the-art ABR algorithms. This is because ANT can
effectively represent and learn network throughput dynamics,
and always select the appropriate ABR model for the cur-
rent network condition to better handle network fluctuations.
We also observe that ABR algorithms with parameter auto-
tuning capabilities, such as Oboe and ANT, exhibit superior
performance in high-QoE sessions but inferior performance
in low-QoE sessions compared to the general-model Pensieve
algorithm. This can be attributed to the relatively aggressive
policy of Oboe and ANT in selecting higher video bitrates
while simultaneously minimizing rebuffering occurrences.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 12

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
819
However, due to the dominance of the rebuffering penalty in
the overall QoE metric defined for live streaming scenarios,
these algorithms fail to achieve QoE improvements in low-
QoE sessions.
On the other hand, ANT achieves a greater average QoE
improvement in the live streaming scenario than that in the
VoD scenario, compared to the best state-of-the-art Oboe and
Pensieve. This result can be attributed to the ability of ANT
to perceive and adapt to network dynamics, especially in
the absence of redundant buffer capacity and knowledge of
future video content. Furthermore, we find that all considered
algorithms perform better on the average QoE under public
traces in the live streaming scenario, which is opposite to that
in the VoD scenario. This is mainly due to about 10% sessions
with very low QoE achieved for all considered algorithms
in the Tencent dataset, as shown in Figure 16(b). Recall that
the network bandwidth in the Tencent dataset fluctuates more
severely than that in the public dataset, which brings greater
challenges for ABR algorithms in the latency-sensitive live
streaming scenario with a limited buffer capacity.
V. DISCUSSION
Handling more complex network conditions. Although the
network traces we use in this paper cover a wide range of
conditions, there is an opportunity for ANT to encounter more
complex network conditions in a real transmission environ-
ment. In this situation, the network condition detection module
may produce inaccurate results that cause inappropriate model
selection in the following bitrate decision module. Moreover,
these complex network conditions may occur without a label,
that is, not included in the trace clustering, bringing difficulty
for ANT to select the most appropriate ABR model for bitrate
decisions. Nevertheless, we train a general ABR model and
a dedicated “uncertain” ABR model in ANT additionally to
cover the above-mentioned network conditions for acceptable
QoE achievement.
Online training for ABR models. ANT server stores a
limited number of pre-trained ABR models, each of which
corresponds to a specific network condition. However, when an
absolutely different network condition appears, all pre-trained
models may be susceptible to experiencing performance degra-
dation. In this case, these pre-trained ABR models need to
be refined online, or a new ABR model should be trained to
match this unseen network condition. Further investigations
are required for this aspect, and it will be deferred to future
research endeavors. It is worth noting that during the model
refinement process, online training can be collaborated with
ANT’s network condition detection module to strike a balance
between training effectiveness and efficiency.
VI. CONCLUSION
In this paper, we propose ANT, a novel framework
to enhance adaptive video streaming by accurately learn-
ing network throughput dynamics. Unlike existing ABR
algorithms that rely on limited network statistics to auto-
tune model parameters, ANT takes a different approach by
characterizing and sensing the network dynamics using com-
prehensive features extracted from raw throughput sequences.
Based on the sensing output, ANT then selects the most
appropriate ABR model that has been well trained using
reinforcement learning under similar network conditions, to
make bitrate decisions. This allows ANT to optimize different
ABR policies for each specific network condition encountered.
Through extensive experimental evaluations, we demonstrate
the superior performance of ANT in bitrate adaptation across
a wide range of network conditions, both in the video-on-
demand and live-streaming scenarios.
REFERENCES
[1] “Cisco visual networking index: Global mobile data traffic forecast
update 2017-2022,” Cisco Technol. Co., San Jose, CA, USA, White
Paper, 2019.
[2] Y. Xu, J. Yin, Q. Yang, and L. Yang, “Media production using cloud
and edge computing: Recent progress and NBMP-based implementa-
tion,” IEEE Trans. Broadcast., vol. 68, no. 2, pp. 545–558, Jun. 2022.
[3] C. Liu, I. Bouazizi, and M. Gabbouj, “Rate adaptation for adaptive
HTTP streaming,” in Proc. 2nd Annu. ACM Conf. Multimedia Syst.,
2011, pp. 169–174.
[4] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and
stability in HTTP-based adaptive video streaming with FESTIVE,” in
Proc. 8th Int. Conf. Emerg. Netw. Exp. Technol., 2012, pp. 97–108.
[5] Y. Sun et al., “CS2P: Improving video bitrate selection and adaptation
with data-driven throughput prediction,” in Proc. ACM SIGCOMM
Conf., 2016, pp. 272–285.
[6] K. Miller, A.-K. Al-Tamimi, and A. Wolisz, “QoE-based low-delay
live streaming using throughput predictions,” ACM Trans. Multimedia
Comput. Commun. Appl., vol. 13, no. 1, pp. 1–24, Oct. 2016.
[7] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson, “A
buffer-based approach to rate adaptation: Evidence from a large video
streaming service,” in Proc. ACM Conf. SIGCOMM, 2014, pp. 187–198.
[8] T.-Y. Huang, R. Johari, and N. McKeown, “Downton abbey without the
hiccups: Buffer-based rate adaptation for HTTP video streaming,” in
Proc. ACM SIGCOMM Workshop Future Human-Centric Multimedia
Netw., 2013, pp. 9–14.
[9] K. Miller, E. Quacchio, G. Gennari, and A. Wolisz, “Adaptation
algorithm for adaptive streaming over HTTP,” in Proc. 19th Int. Packet
Video Workshop (PV), 2012, pp. 173–178.
[10] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
bitrate adaptation for online videos,” in Proc. IEEE 35th Annu. IEEE
Int. Conf. Comput. Commun. (INFOCOM), 2016, pp. 1–9.
[11] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video stream-
ing with pensieve,” in Proc. Conf. ACM Spec. Interest Group Data
Commun., 2017, pp. 197–210.
[12] H. Chen et al., “T-gaming: A cost-efficient cloud gaming system
at scale,” IEEE Trans. Parallel Distrib. Syst., vol. 30, no. 12,
pp. 2849–2865, Dec. 2019.
[13] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,” in Proc. 17th USENIX Symp. Netw. Syst. Design Implement.
(NSDI), 2020, pp. 495–511.
[14] Z. Xia, Y. Zhou, F. Y. Yan, and J. Jiang, “Genet: Automatic curricu-
lum generation for learning adaptation in networking,” in Proc. ACM
SIGCOMM Conf., 2022, pp. 397–413.
[15] Z. Akhtar et al., “Oboe: Auto-tuning video ABR algorithms to network
conditions,” in Proc. Conf. ACM Spec. Interest Group Data Commun.,
2018, pp. 44–58.
[16] E. Kurdoglu, Y. Liu, Y. Wang, Y. Shi, C. Gu, and J. Lyu, “Real-time
bandwidth prediction and rate adaptation for video calls over cellular
networks,” in Proc. 7th Int. Conf. Multimedia Syst., 2016, pp. 1–11.
[17] X. K. Zou et al., “Can accurate predictions improve video streaming in
cellular networks?” in Proc. 16th Int. Workshop Mobile Comput. Syst.
Appl., 2015, pp. 57–62.
[18] S. Kim and C. Kim, “XMAS: An efficient mobile adaptive streaming
scheme based on traffic shaping,” IEEE Trans. Multimedia, vol. 21, no. 2,
pp. 442–456, Feb. 2019.
[19] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari,
“Confused, timid, and unstable: Picking a video streaming rate is
hard,” in Proc. Internet Meas. Conf., 2012, pp. 225–238.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 13

```text
820
IEEE TRANSACTIONS ON BROADCASTING, VOL. 70, NO. 3, SEPTEMBER 2024
[20] A. Beben, P. Wiundefinedniewski, J. M. Batalla, and P. Krawiec,
“ABMA+: Lightweight and efficient algorithm for HTTP adaptive
streaming,” in Proc. 7th Int. Conf. Multimedia Syst., 2016, pp. 1–11.
[21] G. Tian and Y. Liu, “Towards agile and smooth video adaptation in
dynamic HTTP streaming,” in Proc. 8th Int. Conf. Emerg. Netw. Exp.
Technol., 2012, pp. 109–120.
[22] C. Zhou, C. Lin, X. Zhang, and Z. Guo, “Buffer-based smooth rate
adaptation for dynamic HTTP streaming,” in Proc. Asia-Pac. Signal Inf.
Process. Assoc. Annu. Summit Conf., 2013, pp. 1–9.
[23] Z. Li et al., “Probe and adapt: Rate adaptation for HTTP video streaming
at scale,” IEEE J. Sel. Areas Commun., vol. 32, no. 4, pp. 719–733,
Apr. 2014.
[24] C. Wang, A. Rizk, and M. Zink, “SQUAD: A spectrum-based quality
adaptation for dynamic adaptive streaming over HTTP,” in Proc. 7th Int.
Conf. Multimedia Syst., 2016, pp. 1–12.
[25] A. Mansy, B. Ver Steeg, and M. Ammar, “SABRE: A client based
technique for mitigating the buffer bloat effect of adaptive video
flows,” in Proc. 4th ACM Multimedia Syst. Conf., 2013, pp. 214–225.
[26] X. Yin, V. Sekar, and B. Sinopoli, “Toward a principled framework to
design dynamic adaptive streaming algorithms over HTTP,” in Proc.
13th ACM Workshop Hot Topics Netw., 2014, pp. 1–7.
[27] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
approach for dynamic adaptive video streaming over HTTP,” in Proc.
ACM Conf. Spec. Interest Group Data Commun., 2015, pp. 325–338.
[28] L. De Cicco, V. Caldaralo, V. Palmisano, and S. Mascolo, “ELASTIC:
A client-side controller for dynamic adaptive streaming over HTTP
(DASH),” in Proc. 20th Int. Packet Video Workshop, 2013, pp. 1–8.
[29] C. Zhou, C.-W. Lin, and Z. Guo, “mDASH: A Markov decision-based
rate adaptation approach for dynamic HTTP streaming,” IEEE Trans.
Multimedia, vol. 18, no. 4, pp. 738–751, Apr. 2016.
[30] J. Chen, Z. Luo, Z. Wang, M. Hu, and D. Wu, “Live360: Viewport-aware
transmission optimization in live 360-degree video streaming,” IEEE
Trans. Broadcast., vol. 69, no. 1, pp. 85–96, Mar. 2023.
[31] A. Yaqoob and G.-M. Muntean, “A combined field-of-view prediction-
assisted viewport adaptive delivery scheme for 360◦videos,” IEEE
Trans. Broadcast., vol. 67, no. 3, pp. 746–760, Sep. 2021.
[32] A. Polakoviˇc, G. Rozinaj, and G.-M. Muntean, “User gaze-driven
adaptation of omnidirectional video delivery using spatial tiling and
scalable video encoding,” IEEE Trans. Broadcast., vol. 68, no. 3,
pp. 609–619, Sep. 2022.
[33] L. Zhong, M. Wang, C. Xu, S. Yang, and G.-M. Muntean, “Decentralized
optimization for multicast adaptive video streaming in edge cache-
assisted networks,” IEEE Trans. Broadcast., vol. 69, no. 3, pp. 812–822,
Sep. 2023.
[34] Z. Ye et al., “VRCT: A viewport reconstruction-based 360◦video
caching solution for tile-adaptive streaming,” IEEE Trans. Broadcast.,
vol. 69, no. 3, pp. 691–703, Sep. 2023.
[35] M. A. Togou et al., “An innovative adaptive Web-based solution
for improved remote co-creation and delivery of artistic perfor-
mances,” IEEE Trans. Broadcast., early access, Mar. 13, 2024,
doi: 10.1109/TBC.2024.3363455.
[36] Y. Wang, J. Li, Z. Li, S. Shang, and Y. Liu, “Synergistic temporal-
spatial user-aware viewport prediction for optimal adaptive 360-degree
video streaming,” IEEE Trans. Broadcast., early access, Mar. 21, 2024,
doi: 10.1109/TBC.2024.3374119.
[37] Z.
Li,
Y.
Wang,
Y.
Liu,
J.
Li,
and
P.
Zhu,
“JUST360:
Optimizing
360-degree
video
streaming
systems
with
joint
utility,”
IEEE
Trans.
Broadcast.,
early
access,
Mar.
21,
2024,
doi: 10.1109/TBC.2024.3374066.
[38] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick:
A harmonious fusion of buffer-based and learning-based approach
for adaptive streaming,” in Proc. IEEE Conf. Comput. Commun.
(INFOCOM), 2020, pp. 1967–1976.
[39] R. Hong, Q. Shen, L. Zhang, and J. Wang, “Continuous bitrate & latency
control with deep reinforcement learning for live video streaming,” in
Proc. 27th ACM Int. Conf. Multimedia, 2019, pp. 2637–2641.
[40] X. Jiang and Y. Ji, “HD3: Distributed dueling DQN with discrete-
continuous hybrid action spaces for live video streaming,” in Proc. 27th
ACM Int. Conf. Multimedia, 2019, pp. 2632–2636.
[41] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Comyco:
Quality-aware adaptive video streaming via imitation learning,” in Proc.
27th ACM Int. Conf. Multimedia, 2019, pp. 429–437.
[42] H. Peng, Y. Zhang, Y. Yang, and J. Yan, “A hybrid control scheme
for adaptive live streaming,” in Proc. 27th ACM Int. Conf. Multimedia,
2019, pp. 2627–2631.
[43] T. Huang, R.-X. Zhang, C. Zhou, and L. Sun, “QARC: Video quality
aware rate control for real-time video streaming based on deep rein-
forcement learning,” in Proc. 26th ACM Int. Conf. Multimedia, 2018,
pp. 1208–1216.
[44] A. Elgabli and V. Aggarwal, “FastScan: Robust low-complexity rate
adaptation algorithm for video streaming over HTTP,” IEEE Trans.
Circuits Syst. Video Technol., vol. 30, no. 7, pp. 2240–2249, Jul. 2020.
[45] T.
Huang,
R.-X.
Zhang,
and
L.
Sun,
“Zwei:
A
self-play
reinforcement
learning
framework
for
video
transmission
services,” IEEE Trans. Multimedia, vol. 24, pp. 1350–1365, 2022,
doi: 10.1109/TMM.2021.3063620.
[46] L.
Cui,
D.
Su,
S.
Yang,
Z.
Wang,
and
Z.
Ming,
“TCLiVi:
Transmission control in live video streaming based on deep reinforce-
ment learning,” IEEE Trans. Multimedia, vol. 23, pp. 651–663, 2021,
doi: 10.1109/TMM.2020.2985631.
[47] T. Feng, H. Sun, Q. Qi, J. Wang, and J. Liao, “Vabis: Video adaptation
bitrate system for time-critical live streaming,” IEEE Trans. Multimedia,
vol. 22, no. 11, pp. 2963–2976, Nov. 2020.
[48] H. Yuan, X. Hu, J. Hou, X. Wei, and S. Kwong, “An ensemble rate
adaptation framework for dynamic adaptive streaming over HTTP,” IEEE
Trans. Broadcast., vol. 66, no. 2, pp. 251–263, Jun. 2020.
[49] Z. Jiang, X. Zhang, Y. Xu, Z. Ma, J. Sun, and Y. Zhang, “Reinforcement
learning based rate adaptation for 360-degree video streaming,” IEEE
Trans. Broadcast., vol. 67, no. 2, pp. 409–423, Jun. 2021.
[50] J. Fu, Z. Chen, X. Chen, and W. Li, “Sequential reinforced 360-degree
video adaptive streaming with cross-user attentive network,” IEEE Trans.
Broadcast., vol. 67, no. 2, pp. 383–394, Jun. 2021.
[51] A. Zhang et al., “Video super-resolution and caching—an edge-assisted
adaptive video streaming solution,” IEEE Trans. Broadcast., vol. 67,
no. 4, pp. 799–812, Dec. 2021.
[52] X. Ma et al., “QAVA: QoE-aware adaptive video bitrate aggregation
for HTTP live streaming based on smart edge computing,” IEEE Trans.
Broadcast., vol. 68, no. 3, pp. 661–676, Sep. 2022.
[53] Y.
Xie,
Y.
Zhang,
and
T.
Lin,
“Deep
curriculum
reinforce-
ment learning for adaptive 360◦video streaming with two-stage
training,” IEEE Trans. Broadcast., early access, Dec. 15, 2023,
doi: 10.1109/TBC.2023.3334137.
[54] G. Zhou, Z. Luo, M. Hu, and D. Wu, “PreSR: Neural-enhanced adaptive
streaming of VBR-encoded videos with selective prefetching,” IEEE
Trans. Broadcast., vol. 69, no. 1, pp. 49–61, Mar. 2023.
[55] T. P. Lillicrap et al., “Continuous control with deep reinforcement
learning,” 2019, arXiv:1509.02971.
[56] X. Xiao et al., “From ember to blaze: Swift interactive video adaptation
via meta-reinforcement learning,” 2023, arXiv:2301.05541.
[57] N. Kan, Y. Jiang, C. Li, W. Dai, J. Zou, and H. Xiong, “Improving
generalization for neural adaptive video streaming via meta reinforce-
ment learning,” in Proc. 30th ACM Int. Conf. Multimedia, 2022,
pp. 3006–3016.
[58] H. Zhang, A. Zhou, and H. Ma, “Improving mobile interactive video
QoE via two-level online cooperative learning,” IEEE Trans. Mobile
Comput., vol. 22, no. 10, pp. 5900–5917, Oct. 2023.
[59] Y. Gao, P. Zhou, Z. Liu, B. Han, and P. Hui, “FRAS: Federated reinforce-
ment learning empowered adaptive point cloud video streaming,” 2023,
arXiv:2207.07394.
[60] C. Hardegen, B. Pfülb, S. Rieger, A. Gepperth, and S. Reißmann, “Flow-
based throughput prediction using deep learning and real-world network
traffic,” in Proc. 15th Int. Conf. Netw. Service Manag. (CNSM), 2019,
pp. 1–9.
[61] Y. Liu and J. Y. B. Lee, “An empirical study of throughput prediction
in mobile data networks,” in Proc. IEEE Glob. Commun. Conf.
(GLOBECOM), 2015, pp. 1–6.
[62] D. Yuan, Y. Zhang, W. Zhang, X. Liu, H. Du, and Q. Zheng, “PRIOR:
Deep reinforced adaptive video streaming with attention-based through-
put prediction,” in Proc. 32nd Workshop Netw. Oper. Syst. Support Digit.
Audio Video, 2022, pp. 36–42.
[63] A. Bentaleb, C. Timmerer, A. C. Begen, and R. Zimmermann,
“Bandwidth prediction in low-latency chunked streaming,” in Proc. 29th
ACM Workshop Netw. Oper. Syst. Support Digit. Audio Video, 2019,
pp. 7–13.
[64] A. Bentaleb, A. C. Begen, S. Harous, and R. Zimmermann, “Data-
driven bandwidth prediction models and automated model selection for
low latency,” IEEE Trans. Multimedia, vol. 23, pp. 2588–2601, 2021,
doi: 10.1109/TMM.2020.3013387.
[65] J. B. Macqueen, “Some methods for classification and analysis of
multivariate observations,” in Proc. 5th Berkeley Symp. Math. Stat.
Probab., 1967, pp. 281–297.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```

### Página 14

```text
YIN et al.: LEARNING ACCURATE NETWORK DYNAMICS FOR ENHANCED ADAPTIVE VIDEO STREAMING
821
[66] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for
image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit.
(CVPR), 2016, pp. 770–778.
[67] V. Mnih et al., “Asynchronous methods for deep reinforcement learn-
ing,” in Proc. 33rd Int. Conf. Mach. Learn., 2016, pp. 1928–1937.
[68] (Federal Commun. Commiss. Gov. Agency, Washington, DC, USA).
Raw Data—Measuring Broadband America. (2016). [Online]. Available:
https://www.fcc.gov/reports-Res./reports/
[69] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute path
bandwidth traces from 3G networks: Analysis and applications,” in Proc.
4th ACM Multimedia Syst. Conf., 2013, pp. 114–118.
[70] “4G/LTE bandwidth dataset collection from Belgium.” 2017. [Online].
Available: http://users.ugent.be/ jvdrhoof/dataset-4g/logs/
[71] “ACM multimedia 2019 grand challenge–live video streaming.” 2019.
[Online]. Available: https://www.aitrans.online/MMGC/
[72] Z. Ma, M. Xu, Y.-F. Ou, and Y. Wang, “Modeling of rate and perceptual
quality of compressed video as functions of frame rate and Quantization
stepsize and its applications,” IEEE Trans. Circuits Syst. Video Technol.,
vol. 22, no. 5, pp. 671–682, May 2012.
Jiaoyang Yin received the B.S. degree in commu-
nication engineering from Xidian University, Xi’an,
China, in 2018. He is currently pursuing the Ph.D.
degree with the Cooperative Medianet Innovation
Center, Shanghai Jiao Tong University, China. His
research focuses on media transmission, wireless
communication, neural network, and quality of
experience.
Hao Chen (Member, IEEE) received the B.E. degree
in electronics and information engineering from
Northwestern Polytechnical University, China, in
2013, and the Ph.D. degree in information and com-
munication engineering from Shanghai Jiao Tong
University, China, in 2020. He is currently on the
faculty of the Electronic Science and Engineering
School, Nanjing University. His research interests
focus on video streaming, real-time video transmis-
sion, and machine learning. He is a co-recipient of
the 2019 IEEE Broadcast Technology Society Best
Paper Award.
Yiling Xu (Member, IEEE) received the B.S.,
M.S., and Ph.D. degrees from the University of
Electronic Science and Technology of China, China,
in 1999, 2001, and 2004, respectively. She is
a Full Researcher with the School of Electronic
Information and Electronic Engineering, Shanghai
Jiao Tong University, Shanghai, China. From 2004 to
2013, she was with the Multimedia Communication
Research Institute, Samsung Electronics Inc., South
Korea. Her main research interests include architec-
ture design for next generation multimedia systems,
dynamic data encapsulation, adaptive cross layer design, dynamic adaption
for heterogenous networks, and N-screen content presentation.
Zhan Ma (Senior Member, IEEE) received the B.S.
and M.S. degrees from the Huazhong University
of Science and Technology, Wuhan, China, in
2004
and
2006,
respectively,
and
the
Ph.D.
degree from New York University, New York,
in 2011. He is currently on the faculty of the
Electronic Science and Engineering School, Nanjing
University, Jiangsu, China. From 2011 to 2014,
he was with Samsung Research America, Dallas,
TX, USA, and Futurewei Technologies, Inc., Santa
Clara, CA, USA, respectively. His current research
focuses on the next-generation video coding, energy-efficient communication,
gigapixel streaming, and deep learning. He is a co-recipient of the 2018 ACM
SIGCOMM Student Research Competition Finalist, the 2018 PCM Best Paper
Finalist, and the 2019 IEEE Broadcast Technology Society Best Paper Award.
Xiaozhong Xu (Member, IEEE) received the B.S.
degree in electronics engineering from Tsinghua
University, Beijing, China, the M.S. degree in
electrical
and
computer
engineering
from
the
Polytechnic School of Engineering, New York
University, New York, NY, USA, and the Ph.D.
degree in electronics engineering from Tsinghua
University. He has been a Principal Researcher
and a Senior Manager of Multimedia Standards
with Tencent Media Laboratory, Palo Alto, CA,
USA, since 2017. His research interests include
multimedia, video and image coding, processing, and transmission. He was a
recipient of the Science and Technology Award from the China Association
for Standardization in 2020.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.
```
