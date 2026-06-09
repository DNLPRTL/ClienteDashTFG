# A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
**Archivo PDF:** `3591108.pdf`  **Identificador:** `13_visual_sensitivity_aware_drl_abr`  **Páginas:** 22  **SHA256 PDF:** `6b1c3e084ce52bcb5be65d713105b328502ec241c7254caff868f03aec97928b`  **Foco para Fase 4-5 v1:** Visual-sensitivity-aware DRL ABR; HVS/content features; perceptual QoE; trace-driven and subjective evaluation.
> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.
## 1. Cómo usar este `.md`
- Leer primero secciones 2-5 para ubicar método, señales, datos, evaluación y limitaciones.
- Usar la extracción por categorías como material de diseño/contrato/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No convertir resultados del paper en promesas directas para DashClientModular4; deben transformarse en hipótesis, guardrails y tests Phase 6.
## 2. Metadatos extraídos
- **format:** PDF 1.7
- **creator:** LaTeX with hyperref package
- **producer:** Acrobat Distiller 11.0 (Windows)
- **creationDate:** D:20231109074422+05'30'
- **modDate:** D:20231109074502+05'30'

## 3. Índice de secciones detectadas
- p.1: evaluation and compare its performance with several latest algorithms. Experimental results show that our
- p.2: INTRODUCTION
- p.3: RELATED WORKS
- p.4: results provide a video bitrate saving method for content providers. In addition, Gao et al. [18]
- p.5: methods fail to effectively capture the interaction between pixels [26, 27] since human perceives
- p.5: MOTIVATION
- p.7: SYSTEM DESIGN
- p.13: method is used to update the network parameters, and we generate multiple agents (8 numbers)
- p.13: EXPERIMENT AND EVALUATION
- p.14: Evaluation of Total Masking Effect Model
- p.15: Method
- p.15: SUR-FJND
- p.15: GPR-SUR
- p.15: Evaluation Results. This paper uses two commonly used metrics to evaluate the prediction
- p.15: Evaluation of ABR Algorithm
- p.16: VS-ABR
- p.18: method is helpful to guide the ABR algorithm to achieve higher perceptual video quality.
- p.19: VS-ABR
- p.19: GPR-SUR-ABR
- p.19: CONCLUSION
- p.19: REFERENCES

## 4. Índice de páginas con palabras clave
- p.1: QoE, buffer, bandwidth, trace, PPO, imitation, quality, visual, sensitivity
- p.2: state, QoE, rebuffer, buffer, throughput, bandwidth, chunk, imitation, quality, visual, sensitivity, network condition
- p.3: state, reward, QoE, rebuffer, buffer, throughput, download, chunk, trace, MPC, BBA, BOLA, quality, visual, sensitivity
- p.4: action, QoE, buffer, chunk, training, Pensieve, PPO, A3C, expert, quality, visual, sensitivity
- p.5: action, dataset, PPO, imitation, quality, visual, sensitivity
- p.6: QoE, chunk, dataset, Pensieve, PPO, quality, VMAF, visual, sensitivity
- p.7: state, buffer, throughput, download, chunk, quality, visual, sensitivity
- p.8: state, buffer, download, chunk, quality, visual, sensitivity
- p.9: chunk, visual, sensitivity
- p.10: chunk, dataset, training, quality, SSIM, visual, sensitivity
- p.11: chunk, quality, visual, sensitivity
- p.12: state, action, reward, QoE, buffer, throughput, download, chunk, training, A3C, quality, visual, sensitivity
- p.13: state, action, reward, QoE, rebuffer, buffer, chunk, training, quality, VMAF, visual, sensitivity
- p.14: state, action, reward, rebuffer, buffer, download, chunk, dataset, training, quality, visual, sensitivity
- p.15: action, chunk, baseline, visual, sensitivity
- p.16: QoE, rebuffer, buffer, throughput, bandwidth, chunk, dataset, trace, training, MPC, Pensieve, quality, VMAF, sensitivity
- p.17: QoE, rebuffer, buffer, throughput, trace, quality, VMAF, visual, sensitivity, network condition
- p.18: state, action, QoE, buffer, throughput, chunk, trace, MPC, Pensieve, quality, VMAF, visual, sensitivity, network condition
- p.19: QoE, training, baseline, MPC, Pensieve, imitation, quality, visual, sensitivity
- p.20: action, QoE, buffer, throughput, BOLA, Pensieve, PPO, imitation, inference, quality, visual
- p.21: action, bandwidth, dataset, trace, BBA, inference, quality, VMAF, visual, sensitivity
- p.22: action, quality

## 5. Extracción técnica cruda por categorías

### 5.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

77 A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocat

**[Modelo / arquitectura / algoritmo | extracto 2 | p.1]**

ingapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE

**[Modelo / arquitectura / algoritmo | extracto 3 | p.1]**

iver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transm

**[Modelo / arquitectura / algoritmo | extracto 4 | p.1]**

owever, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye a

**[Modelo / arquitectura / algoritmo | extracto 5 | p.1]**

HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project o

**[Modelo / arquitectura / algoritmo | extracto 6 | p.1]**

inal receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to

**[Modelo / arquitectura / algoritmo | extracto 7 | p.2]**

77:2 J. Ye et al. ACM Reference format: Jin Ye, Meng Dan, and Wenchao Jiang. 2023. A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversi

**[Modelo / arquitectura / algoritmo | extracto 8 | p.2]**

including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t perceive a certain degree of quality distortion due to the existence of the visual masking effect. In other words, user QoE can be improved by increasing the video quality of a more perceivable portion of video content. Inspired by this, we introduce visual sensitivity to measure the relationship between HVS characteristics and video content. We model the total ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Modelo / arquitectura / algoritmo | extracto 9 | p.2]**

ntinue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower

**[Modelo / arquitectura / algoritmo | extracto 10 | p.2]**

l Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server an

**[Modelo / arquitectura / algoritmo | extracto 11 | p.2]**

ically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t pe

**[Modelo / arquitectura / algoritmo | extracto 12 | p.3]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:3 masking effect of video content by fitting human perception to reflect the sensitivity of HVS to quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm to improve user QoE. The main contributions of this paper are threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in hum

**[Modelo / arquitectura / algoritmo | extracto 13 | p.3]**

g 77:3 masking effect of video content by fitting human perception to reflect the sensitivity of HVS to quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm to improve user QoE. The main contributions of this paper are threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-t

**[Modelo / arquitectura / algoritmo | extracto 14 | p.3]**

eo quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and performance analysis. Section 6 concludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are tw

**[Modelo / arquitectura / algoritmo | extracto 15 | p.3]**

aditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Modelo / arquitectura / algoritmo | extracto 16 | p.3]**

del adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, a

### 5.x Estado / inputs / features

**[Estado / inputs / features | extracto 1 | p.1]**

eo streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluati

**[Estado / inputs / features | extracto 2 | p.1]**

ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contr

**[Estado / inputs / features | extracto 3 | p.1]**

77 A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity a

**[Estado / inputs / features | extracto 4 | p.1]**

easibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in Data Center Network (NO.61872387), and the Key Project of Guangxi Science & Technology (NO.2021AB06002). This work was supported by the Ministry of Education, Singapore, under its Academic Research Fund Tier 2 (MOE- T2EP20221-0017); the National Research Foundation, Singapore and Infocomm Media Development Authority under its Future Communications Research & Development Programme; and the Key Project of Guangxi Science & Technology (NO.2021AB06002). Authors’ addresses: J. Ye and M. Dan, Guangxi Key Laboratory of Multimedia Communications and Network Technology, School of Computer and Electronic Information, Guangxi University, Nanning 530000, China; emails: yejin@gxu.edu.cn, 1913392006@st.gxu.edu.cn; W. Jiang, Information Systems Technology and Design, Singapore University of Technology and Design, 487372, Singapore; email: wenchaojiang@sutd.edu.sg. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work ow

**[Estado / inputs / features | extracto 5 | p.1]**

o cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respe

**[Estado / inputs / features | extracto 6 | p.1]**

order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and

**[Estado / inputs / features | extracto 7 | p.2]**

irst requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due

**[Estado / inputs / features | extracto 8 | p.2]**

eo, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to

**[Estado / inputs / features | extracto 9 | p.2]**

of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advanc

**[Estado / inputs / features | extracto 10 | p.2]**

a type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising d

**[Estado / inputs / features | extracto 11 | p.2]**

ivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains

**[Estado / inputs / features | extracto 12 | p.2]**

oncern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. T

**[Estado / inputs / features | extracto 13 | p.2]**

P (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environm

**[Estado / inputs / features | extracto 14 | p.2]**

77:2 J. Ye et al. ACM Reference format: Jin Ye, Meng Dan, and Wenchao Jiang. 2023. A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandw

**[Estado / inputs / features | extracto 15 | p.2]**

ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t perceive a certain degree of quality distortion due to the existence of the visual masking effect. In other words, user QoE can be improved by increasing the video quality of a more perceivable portion of video content. Inspired by this, we introduce visual sensitivity to measure the relationship between HVS characteristics and video content. We model the total ACM Trans.

**[Estado / inputs / features | extracto 16 | p.2]**

network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS t

### 5.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

77 A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulat

**[Acción / decisión ABR | extracto 2 | p.1]**

, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission The

**[Acción / decisión ABR | extracto 3 | p.2]**

77:2 J. Ye et al. ACM Reference format: Jin Ye, Meng Dan, and Wenchao Jiang. 2023. A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media

**[Acción / decisión ABR | extracto 4 | p.2]**

By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-

**[Acción / decisión ABR | extracto 5 | p.3]**

on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed b

**[Acción / decisión ABR | extracto 6 | p.3]**

fer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Acción / decisión ABR | extracto 7 | p.3]**

hows the experimental setup, evaluation method, and performance analysis. Section 6 concludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Acción / decisión ABR | extracto 8 | p.3]**

ate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Acción / decisión ABR | extracto 9 | p.4]**

at attracts visual attention, it may not be able to effectively improve the perceptual video quality, because it is uncertain whether users can perceive the video distortion. Therefore, the difference between our work and previous studies is that instead of proposing yet another quality metric, we consider the perception of HVS to video quality distortion for QoE optimization. This visual characteristic can be applied to optimize the ABR strategy in the case of limited network resources, for instance, switching to a lower bitrate when users can’t perceive the degradation of video quality. To our best knowledge, this is the first work to integrate the sensitivity of HVS to distortion into the ABR model for DASH. 2.2 Modeling of Visual Sensitivity Visual masking effect is a complex visual perception mechanism, which is caused by the inter- action or interference between stimuli. It refers to the reduced capability of HVS in perceiving stimuli such as distortion, edge, and motion under complex spatial or temporal background [22], mainly including luminance masking, spatial contrast masking and temporal masking. The luminance masking effect indicates that HVS is less sensitive to distortion in darker or brighter regions. The spatial contrast masking effect means that HVS is more likely to perceive the quality ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Acción / decisión ABR | extracto 10 | p.4]**

77:4 J. Ye et al. time-varying channel conditions, taking into account factors such as video playback quality, video bitrate switching frequency and amplitude, buffer overflow/underflow, and buffer occupancy. Although the idea is easy to understand and simple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider di

**[Acción / decisión ABR | extracto 11 | p.4]**

and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects. These research results provide a video bitrate saving method for content providers. In addition, Gao et al. [18] propose an interest-aware rate adaptive method, which identifies users’ interest for different video scenes through video semantics and users’ preference, and delivers the video of interest to users with higher quality. Hu et al. [19] propose a semantic-aware adaptation scheme for MPEG-DASH services, making bitrate decisions depending on content descriptors of the important content per- ceived by users. In his latest work [20], an affective content-aware adaptation scheme is proposed. The method analyzes the emotional demands of users, and introduces an affective relevancy mea- surement to quantify personalized emotional p

**[Acción / decisión ABR | extracto 12 | p.4]**

ve multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects. These research results provide a video bitrate saving method for content providers. In addition, Gao et al. [18] propose an interest-aware rate adaptive method, which identifies users’ interest for different video scenes through video semantics and users’ preference, and delivers the video of interest to users with higher quality. Hu et al. [19] propose a semantic-aware adaptation scheme for MPEG-DASH services, making bitrate decisions depending on content descriptors of the important content per- ceived by users. In his latest work [20], an affective content-aware adaptation scheme is proposed. The method analyzes the emotional demands of users, and introduces an affective relevancy mea- surement to quantify personalized emotional preference. In the above content-aware ABR algorithms, although different metrics are adopted to optimize video quality, they still ignore the visibility of video quality distortion, which is an important factor affecting users’ perceptual video quality. Even if a higher bitrate is selected for video content that attracts visual attention, it may not be able to effectively improve the perceptual video quality, because it is uncertain whether users can perceive the video distortion. Therefore, the difference between our work and previous stu

**[Acción / decisión ABR | extracto 13 | p.4]**

lement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects. These rese

**[Acción / decisión ABR | extracto 14 | p.4]**

et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects. These research results provide a video bitrate saving method for content providers. In addition, Gao et al. [18] propose an interest-aware rate adaptive method, which identifies users’ interest for different video scenes through video semantics and users’ preference, and delivers the video of interest to users with higher quality. Hu et al. [19] propose a semantic-aware adaptation scheme for MPEG-DASH services, making bitrate decisions depending on content descriptors of the important content per- ceived by users. In his latest work [20], an affective content-aware adaptation scheme is proposed. The method analyzes the emotional demands of users, and introduces an affective relevancy mea- surement to quantify personalized emotional preference. In the above content-aware ABR algorithms, although different metrics are adopted to optimize video quality, they still ignore the visibility of video quality distortion, which is an important factor affecting users’ perceptual video quality. Even if a higher bitrate is selected for video content that attracts visual attention, it may not be able to effectively improve the perceptual video quality, because it is uncertain whether users can perceive the video distortion. Ther

**[Acción / decisión ABR | extracto 15 | p.5]**

also shows that it is difficult to perceive the quality change for regions with fast and complex moving objects, and the speed exceeding a certain threshold will even lead to the loss of visual sensitivity. Since the visual masking effect can effectively reflect the inherent characteristics of HVS, it plays an important role in image and video processing [22–25]. Based on this, recent works have proposed the concept of just noticeable difference (JND), which means the minimum distortion HVS can perceive under the total masking effect of different picture/video contents (in the form of perception threshold). The traditional JND models can be divided into pixel-domain models and sub-band domain mod- els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these methods fail to effectively capture the interaction between pixels [26, 27] since human perceives the picture/video as a whole instead of focusing on individual pixels. Picture wise JND (PW- JND)/Video wise JND (VW-JND) is further proposed to represent the JND threshold between a distorted picture/video and its reference (e.g., undistorted). In order to subjectively measure the PW-JND and VW-JND, many JND-based picture/video quality datasets [28–31] have been devel- oped. MCL-JCI [28] is a picture quality dataset under the JPEG compression standard. It contains 50 source pictures, each corresponding to 100 distorted pictures. By analyzing and processing the original JND data, the staircase quality function (SQF) is calculated. VideoSet [31] is a large- scale dataset consisting of 220 source video sequences with a duration of 5 seconds and four res- olutions (1920×1080, 1280×720, 960×540,

**[Acción / decisión ABR | extracto 16 | p.6]**

77:6 J. Ye et al. Fig. 1. The distribution of video chunks in visual masking property and saliency, which can be divided into three categories: lower visual sensitivity; higher visual sensitivity; and others. 3.1 Video Preprocessing Similar to [34], we use the “EnvivioDash3” video in DASH-246 JavaScript client [45] and divide it into 48 chunks. In addition, 48 video chunks are randomly selected from VideoSet [31], and we have 96 video chunks in total for evaluation. All video chunks are encoded by H.264/MPEG-4 at six bitrates (300kbps, 750kbps, 1200kbps, 1850kbps, 2850kbps, 4300kbps), which pertain to YouTube video modes. Researches [23, 27, 46] have shown that the luminance masking effect, spatial contrast masking effect, temporal masking effect and saliency have a significant impact on visual sensitivity. Therefore, we calculate the chunk-level average of each feature for each video chunk and fuse it appropriately. Figure 1 shows the distribution of selected video chunks in visual masking property and saliency, the larger the normalized features, the stronger the visual masking effect or saliency. It can be observed that lower visual sensitivity chunks (marked in blue) typically are lower in saliency and higher in visual masking property, while higher visual sensitivity chunks (marked in red) are higher in saliency and lower in visual masking property. 3.2

### 5.x Reward / QoE / objetivo

**[Reward / QoE / objetivo | extracto 1 | p.1]**

77 A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further,

**[Reward / QoE / objetivo | extracto 2 | p.1]**

perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in Data Center Network (NO.61872387), and the Key Project of Guangxi Science & Technology (NO.2021AB06002). This work was supported by the Ministry of Education, Singapore, under its Academic Research Fund Tier 2 (MOE- T2EP20221-0017

**[Reward / QoE / objetivo | extracto 3 | p.2]**

77:2 J. Ye et al. ACM Reference format: Jin Ye, Meng Dan, and Wenchao Jiang. 2023. A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP serve

**[Reward / QoE / objetivo | extracto 4 | p.2]**

HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the vi

**[Reward / QoE / objetivo | extracto 5 | p.2]**

mission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same se

**[Reward / QoE / objetivo | extracto 6 | p.3]**

threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR st

**[Reward / QoE / objetivo | extracto 7 | p.3]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:3 masking effect of video content by fitting human perception to reflect the sensitivity of HVS to quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm to improve user QoE. The main contributions of this paper are threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining vi

**[Reward / QoE / objetivo | extracto 8 | p.3]**

and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Reward / QoE / objetivo | extracto 9 | p.3]**

mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Reward / QoE / objetivo | extracto 10 | p.4]**

77:4 J. Ye et al. time-varying channel conditions, taking into account factors such as video playback quality, video bitrate switching frequency and amplitude, buffer overflow/underflow, and buffer occupancy. Although the idea is easy to understand and simple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video ada

**[Reward / QoE / objetivo | extracto 11 | p.4]**

ng frequency and amplitude, buffer overflow/underflow, and buffer occupancy. Although the idea is easy to understand and simple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object

**[Reward / QoE / objetivo | extracto 12 | p.4]**

mple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects.

**[Reward / QoE / objetivo | extracto 13 | p.4]**

C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects. These research results provide a video bitrate saving method for content providers. In addition, Gao et al. [18] propose an interest-aware rate adaptive method, which identifies users’ interest for different video scenes through video semantics and users’ preference, and delivers the video of interest to users with h

**[Reward / QoE / objetivo | extracto 14 | p.5]**

JND and VW-JND, many JND-based picture/video quality datasets [28–31] have been devel- oped. MCL-JCI [28] is a picture quality dataset under the JPEG compression standard. It contains 50 source pictures, each corresponding to 100 distorted pictures. By analyzing and processing the original JND data, the staircase quality function (SQF) is calculated. VideoSet [31] is a large- scale dataset consisting of 220 source video sequences with a duration of 5 seconds and four res- olutions (1920×1080, 1280×720, 960×540, and 640×360). It measures the distribution of the first three JND points by binary search method. These subjective scores can be regarded as the ground truth of JND, but subjective methods are expensive and time-consuming, resulting in many limita- tions in practical applications. There are many other studies devoted to developing objective JND prediction models. Liu et al. [26] describe the prediction of PW-JND as a multi-class classification problem, and predicts each JND point of the compressed picture using deep learning technology. However, this method only takes the original picture as input which makes it difficult to learn ef- fective features for multifaceted analysis. Huang et al. [27] define a spatiotemporal sensitivity map by multiplying different features pixel by pixel, and proposes a VW-JND prediction method based on support vector regression (SVR). Due to the complexity of visual signal processing mecha- nism in HVS, this empirical-fused feature limits its adaptability to different scenarios. Wang et al. [32] predict different JND points by the regression of satisfied user ratio (SUR) curves. Similarly, Zhang et al. [33] uses Gaussian process regression (GPR

**[Reward / QoE / objetivo | extracto 15 | p.5]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:5 distortion in smooth or highly structured regions. The temporal masking effect also shows that it is difficult to perceive the quality change for regions with fast and complex moving objects, and the speed exceeding a certain threshold will even lead to the loss of visual sensitivity. Since the visual masking effect can effectively reflect the inherent characteristics of HVS, it plays an important role in image and video processing [22–25]. Based on this, recent works have proposed the concept of just noticeable difference (JND), which means the minimum distortion HVS can perceive under the total masking effect of different picture/video contents (in the form of perception threshold). The traditional JND models can be divided into pixel-domain models and sub-band domain mod- els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these methods fail to effectively capture the interaction between pixels [26, 27] since human perceives the picture/video as a whole instead of focusing on individual pixels. Picture wise JND (PW- JND)/Video wise JND (VW-JND) is furthe

**[Reward / QoE / objetivo | extracto 16 | p.6]**

(denoted as VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The bitrates of two strategies are significantly different, and VS-ABR realizes a smoother range of VMAF scores in Figure 2(b). We find an interesting phenomenon from this experiment that carefully reducing the bitrate of lower visual sensitivity video chunks and allocating the saved resources to high visual sensitivity video chunks will achieve greater benefit. Since HVS can’t detect the existing distortion for the former, lowering a certain bitrate level has little impact on perceptual video quality. Therefore, if the differential allocation of bitrate resources is carried out based on visual sensitivity, the re- source utilization and user QoE are supposed to be further improved. However, it is worth noting ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

### 5.x Entrenamiento / optimización

**[Entrenamiento / optimización | extracto 1 | p.1]**

Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorith

**[Entrenamiento / optimización | extracto 2 | p.1]**

der a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in Data Center Network (NO.61872387), and the Key Project of Guangxi Science & Technology (NO.2021AB06002). This work was supported by the Ministry of Education, Singapore, under its Academic Research Fund Tier 2 (MOE- T2EP20221-0017); the National Research Foundation, Singapore and Infocomm Media Development Authority under its Future Communications Research & Development Programme; and the Key Project of Guangxi Science & Technology (NO.2021AB06002). Authors’ addresses: J. Ye and M. Dan, Guangxi Key Laboratory of Multimedia Communications and Network Technology, School of Computer and Electronic Information, Guangxi University, Nanning 530000, China; ema

**[Entrenamiento / optimización | extracto 3 | p.2]**

bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t perceive a certain degree of quality distortion due to the existence of the visual masking effect. In other words, user QoE can be improved by increasing the video quality of a more perceivable portion of video content. Inspired by this, we introduce visual sensitivity to measure the relationship between HVS characteristics and video content. We model the total ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 20

**[Entrenamiento / optimización | extracto 4 | p.3]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:3 masking effect of video content by fitting human perception to reflect the sensitivity of HVS to quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm to improve user QoE. The main contributions of this paper are threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivit

**[Entrenamiento / optimización | extracto 5 | p.3]**

tributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Entrenamiento / optimización | extracto 6 | p.4]**

77:4 J. Ye et al. time-varying channel conditions, taking into account factors such as video playback quality, video bitrate switching frequency and amplitude, buffer overflow/underflow, and buffer occupancy. Although the idea is easy to understand and simple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotar

**[Entrenamiento / optimización | extracto 7 | p.4]**

e adaptation scheme is proposed. The method analyzes the emotional demands of users, and introduces an affective relevancy mea- surement to quantify personalized emotional preference. In the above content-aware ABR algorithms, although different metrics are adopted to optimize video quality, they still ignore the visibility of video quality distortion, which is an important factor affecting users’ perceptual video quality. Even if a higher bitrate is selected for video content that attracts visual attention, it may not be able to effectively improve the perceptual video quality, because it is uncertain whether users can perceive the video distortion. Therefore, the difference between our work and previous studies is that instead of proposing yet another quality metric, we consider the perception of HVS to video quality distortion for QoE optimization. This visual characteristic can be applied to optimize the ABR strategy in the case of limited network resources, for instance, switching to a lower bitrate when users can’t perceive the degradation of video quality. To our best knowledge, this is the first work to integrate the sensitivity of HVS to distortion into the ABR model for DASH. 2.2 Modeling of Visual Sensitivity Visual masking effect is a complex visual perception mechanism, which is caused by the inter- action or interference between stimuli. It refers to the reduced capability of HVS in perceiving stimuli such as distortion, edge, and motion under complex spatial or temporal background [22], mainly including luminance masking, spatial contrast masking and temporal masking. The luminance masking effect indicates that HVS is less sensitive to distortion in darker or brighter

**[Entrenamiento / optimización | extracto 8 | p.4]**

y is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts the video quality relative to the location of the areas of maximum user interest (AMUI), and supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the video into multiple objects based on two video object representation methods, and allows for the quality-variant HTTP adaptive streaming of background and foreground objects. These research results provide a video bitrate saving method for content providers. In addition, Gao et al. [18] propose an interest-aware rate adaptive method, which identif

**[Entrenamiento / optimización | extracto 9 | p.5]**

ed in image/video processing [35–39], especially in simulating the HVS response mechanism [40, 41]. On this basis, we propose a data-driven multi-stream CNN-based VW-JND predictor, which can measure video characteristics from multiple aspects. By combining two kinds of manual features and the multi-stream CNN fusion network, the model can make full use of the respective features to acquire video characteristics more effectively. In addition, the proposed model also incorporates the feedback connection, which plays an important role in the visual cortex and is indispensable in the formation of quality perception [42–44]. 3 MOTIVATION In this section, we illustrate the importance of visual sensitivity in the ABR algorithm through an exploratory experiment, and prove that the existing ABR algorithm based on reinforcement learning still has limitations. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Entrenamiento / optimización | extracto 10 | p.5]**

40, and 640×360). It measures the distribution of the first three JND points by binary search method. These subjective scores can be regarded as the ground truth of JND, but subjective methods are expensive and time-consuming, resulting in many limita- tions in practical applications. There are many other studies devoted to developing objective JND prediction models. Liu et al. [26] describe the prediction of PW-JND as a multi-class classification problem, and predicts each JND point of the compressed picture using deep learning technology. However, this method only takes the original picture as input which makes it difficult to learn ef- fective features for multifaceted analysis. Huang et al. [27] define a spatiotemporal sensitivity map by multiplying different features pixel by pixel, and proposes a VW-JND prediction method based on support vector regression (SVR). Due to the complexity of visual signal processing mecha- nism in HVS, this empirical-fused feature limits its adaptability to different scenarios. Wang et al. [32] predict different JND points by the regression of satisfied user ratio (SUR) curves. Similarly, Zhang et al. [33] uses Gaussian process regression (GPR) to model SUR curves and derives the JND points, but it is worth noting that the indirect prediction method is more challenging than the direct prediction. In order to solve the above defects, this paper focuses on the effective modeling of the total masking effect of different video contents. In comparison to our previous work [34], this work shows new contributions. Deep learning and neural network technology have been widely used in image/video processing [35–39], especially in simulating the HVS r

**[Entrenamiento / optimización | extracto 11 | p.6]**

s VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The bitrates of two strategies are significantly different, and VS-ABR realizes a smoother range of VMAF scores in Figure 2(b). We find an interesting phenomenon from this experiment that carefully reducing the bitrate of lower visual sensitivity video chunks and allocating the saved resources to high visual sensitivity video chunks will achieve greater benefit. Since HVS can’t detect the existing distortion for the former, lowering a certain bitrate level has little impact on perceptual video quality. Therefore, if the differential allocation of bitrate resources is carried out based on visual sensitivity, the re- source utilization and user QoE are supposed to be further improved. However, it is worth noting ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Entrenamiento / optimización | extracto 12 | p.7]**

is section, we first present the overview of visual sensitivity aware ABR algorithm for DASH, and then introduce two main modules of the proposed video streaming system in detail: (1) Visual Sensitivity Model; and (2) Visual Sensitivity Aware ABR. 4.1 System Structure In this paper, we propose a visual sensitivity model based on the total masking effect analysis and use it for a novel ABR algorithm in a video streaming system. As shown in Figure 3, the visual sensitivity aware ABR controller outputs the bitrate of the next video chunk by integrating the state information from the DASH client and visual sensitivity values from the video server. The DASH client then requests the content delivery network (CDN) to download the corresponding video chunk. The system is composed of two main components: • Visual Sensitivity Model: We adopt a pre-trained deep multi-stream CNN model combined with HVS feedback mechanism to learn the total masking effect, and perform a normalization operation to calculate the relative visual sensitivity. The results are stored in MPD manifest files as an extended property for each video chunk, which can be downloaded from the video server directly when the video session starts. • Visual Sensitivity Aware ABR: We redesign the adaptive strategy based on deep re- inforcement learning. By comprehensively considering the estimated throughput, buffer occupancy, and visual sensitivity of different video chunks, the new video streaming system allows high-sensitivity video chunks to “borrow” bitrate resources from low-sensitivity chunks, so as to achieve our goal that quality should be optimized in proportion to the visual sensitivity. ACM Trans. Multimedia Comput

**[Entrenamiento / optimización | extracto 13 | p.8]**

77:8 J. Ye et al. Fig. 3. The structure of our visual sensitivity aware ABR algorithm for DASH. It can be seen that these two main components are deployed on the server side to avoid the resource constraints of client devices, and the performance of the ABR algorithm is not affected by the delay introduced by the packet switching between the client and the server to a great extent [4, 11], which can be masked by the playback buffer occupancy and chunk download time. 4.2 Visual Sensitivity Model In this subsection, we will describe the total masking effect model and the calculation of visual sensitivity in detail. We aim two tasks: (1) apply the state-of-the-art deep learning and the feed- back mechanism commonly existing in HVS to acquire an effective representation on the total masking effect of video content; and (2) analyze the relationship between the prediction result of the total masking effect model and the sensitivity of HVS to distortion to get the visual sensitivity of different video chunks for the ABR algorithm. As discussed in

**[Entrenamiento / optimización | extracto 14 | p.10]**

video), so the FJND point can accurately reflect the total masking effect of video content. Inspired by this, this paper models the total masking effect of video content as a predictor for the FJND point, and regresses the input features into it. The FJND point is generally represented by coding parameters (e.g., QP), bitrate, and quality metrics (e.g., PSNR [52], SSIM [53]). Among them, QP controls the quality of video coding, bitrate represents the amount of video data per unit time, while PSNR and SSIM are two popular objective quality metrics in picture and video processing. Considering the effectiveness of objective quality metrics in reflecting the degree of distortions and the insensitivity of SSIM to compression distortions, we measure the average PSNR of video frames sampled from a given compressed video as the FJND point. 4.2.3 Training of the Total Masking Effect Model. The structural design of the proposed model is shown in Figure 5. It is based on the advanced VGG network [54], which is inspired by the organization of the primate visual cortex. Firstly, four independent CNN subnetworks are used to convolute different feature maps. The spatial randomness map, the luminance map, the tempo- ral map, and the saliency map are fed into the Subnetwork-1, Subnetwork-2, Subnetwork-3, and Subnetwork-4, respectively to extract finer-grained features. Then the abstract features from four subnetworks and three attribute features are concatenated together and transported into the feed- back module, and the features processed after feedback are input to the fully connected layer to predict the FJND point. Finally, the loss value is calculated, followed by the target prediction.

**[Entrenamiento / optimización | extracto 15 | p.10]**

nvolute different feature maps. The spatial randomness map, the luminance map, the tempo- ral map, and the saliency map are fed into the Subnetwork-1, Subnetwork-2, Subnetwork-3, and Subnetwork-4, respectively to extract finer-grained features. Then the abstract features from four subnetworks and three attribute features are concatenated together and transported into the feed- back module, and the features processed after feedback are input to the fully connected layer to predict the FJND point. Finally, the loss value is calculated, followed by the target prediction. The whole process is formulated as: PSNRk = FB(Concat(sub1(SRMk (i, j)), sub2(LMk (i, j)), sub3(TMk (i, j)), sub4(SMk (i, j)), FRk, REk, BRk)) (6) where FB, Concat, subi denote the processes of the feedback, the concatenation, and the Subnetwork-i, respectively. Because the training of deep neural network needs a large number of samples, and the number of available JND datasets is limited, this paper adopts the patch-based training method to manually increase the data samples. Each input feature map is divided into multiple patches, and a certain number of patches are randomly selected and labeled as the FJND point of the corresponding video chunk for training. In order to accommodate the size of the input patch, the network is extended to three layers, namely conv1, conv2, and maxpool. The training process of the proposed model mainly includes three parts: feature fusion, feed- back looping, and spatial pooling. For feature fusion, we use a simple and commonly used concat() function to fuse the feature vectors extracted by convolution layers in each subnetwork and the attribute features, and then input them into th

**[Entrenamiento / optimización | extracto 16 | p.12]**

77:12 J. Ye et al. Fig. 6. The distribution of VS for sampled video chunks, which spans three different intervals. 4.3 Visual Sensitivity Aware ABR In this section, we will introduce the design and training of the proposed visual sensitivity aware ABR algorithm. The algorithm is based on the latest reinforcement learning (RL) algorithm A3C [21]. Reinforcement learning originated from animal learning in psychology and is an important branch of machine learning. It can imitate human learning ability and choose behaviors that can maximize long-term benefits in the interaction with the environment. RL is mainly composed of five parts: agent, environment, state, action, and reward. RL defines any decision-maker (learner) as an agent and anything other than an agent as an environment. A3C algorithm includes the training of two neural networks, namely actor network and critic network, which have the same network structure and input, but different functions and outputs. Actor network is a strategic function that makes an action according to the

### 5.x Datos / trazas / datasets

**[Datos / trazas / datasets | extracto 1 | p.1]**

with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mec

**[Datos / trazas / datasets | extracto 2 | p.1]**

77 A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We ex

**[Datos / trazas / datasets | extracto 3 | p.2]**

77:2 J. Ye et al. ACM Reference format: Jin Ye, Meng Dan, and Wenchao Jiang. 2023. A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, cont

**[Datos / trazas / datasets | extracto 4 | p.3]**

ts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and per

**[Datos / trazas / datasets | extracto 5 | p.3]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:3 masking effect of video content by fitting human perception to reflect the sensitivity of HVS to quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm to improve user QoE. The main contributions of this paper are threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy impr

**[Datos / trazas / datasets | extracto 6 | p.4]**

77:4 J. Ye et al. time-varying channel conditions, taking into account factors such as video playback quality, video bitrate switching frequency and amplitude, buffer overflow/underflow, and buffer occupancy. Although the idea is easy to understand and simple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR alg

**[Datos / trazas / datasets | extracto 7 | p.5]**

ks have proposed the concept of just noticeable difference (JND), which means the minimum distortion HVS can perceive under the total masking effect of different picture/video contents (in the form of perception threshold). The traditional JND models can be divided into pixel-domain models and sub-band domain mod- els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these methods fail to effectively capture the interaction between pixels [26, 27] since human perceives the picture/video as a whole instead of focusing on individual pixels. Picture wise JND (PW- JND)/Video wise JND (VW-JND) is further proposed to represent the JND threshold between a distorted picture/video and its reference (e.g., undistorted). In order to subjectively measure the PW-JND and VW-JND, many JND-based picture/video quality datasets [28–31] have been devel- oped. MCL-JCI [28] is a picture quality dataset under the JPEG compression standard. It contains 50 source pictures, each corresponding to 100 distorted pictures. By analyzing and processing the original JND data, the staircase quality function (SQF) is calculated. VideoSet [31] is a large- scale dataset consisting of 220 source video sequences with a duration of 5 seconds and four res- olutions (1920×1080, 1280×720, 960×540, and 640×360). It measures the distribution of the first three JND points by binary search method. These subjective scores can be regarded as the ground truth of JND, but subjective methods are expensive and time-consuming, resulting in many limita- tions in practical applications. There are many other studies devoted to developing objective JND prediction models. Liu et al. [26] describe th

**[Datos / trazas / datasets | extracto 8 | p.5]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:5 distortion in smooth or highly structured regions. The temporal masking effect also shows that it is difficult to perceive the quality change for regions with fast and complex moving objects, and the speed exceeding a certain threshold will even lead to the loss of visual sensitivity. Since the visual masking effect can effectively reflect the inherent characteristics of HVS, it plays an important role in image and video processing [22–25]. Based on this, recent works have proposed the concept of just noticeable difference (JND), which means the minimum distortion HVS can perceive under the total masking effect of different picture/video contents (in the form of perception threshold). The traditional JND models can be divided into pixel-domain models and sub-band domain mod- els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these methods fail to effectively capture the interaction between pixels [26, 27] since human perceives the picture/video as a whole instead of focusing on individual pixels. Picture wise JND (PW- JND)/Video wise JND (VW-JND) is further proposed to represent the JND threshold between a distorted picture/video and its reference (e.g., undistorted). In order to subjectively measure the PW-JND and

**[Datos / trazas / datasets | extracto 9 | p.6]**

ower visual sensitivity chunks (marked in blue) typically are lower in saliency and higher in visual masking property, while higher visual sensitivity chunks (marked in red) are higher in saliency and lower in visual masking property. 3.2 Challenges for ABR Similar to [34], we select two types of video chunks (marked in red and blue) in Section 3.1 to compare different ABR strategies. VMAF [47], a full-reference quality metric is used to measure the video quality perceived by users, which has been proved to be closely related to subjective MOS scores. VMAF scores range from 0 to 100, where 0–20, 20–40, 40–60, 60–80, and 80–100 are considered as unacceptable, poor, fair, good, and excellent quality, respectively [48]. Figure 2 shows the bitrate and VMAF of Pensieve [11] and visual sensitivity aware ABR (denoted as VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The bitrates of two strategies are significantly different, and VS-ABR realizes a smoother range of VMAF scores in Figure 2(b). We find an interesting phenomenon from this experiment that carefully reducing the bitrate of lower visual sensitivity video chunks and allocating the saved resources to high visual sensitivity video chunks will achieve greater benefit. Since HVS can’t detect the existing distortion for the former, lowering a certain bitrate level has little impact on perceptual video quality. Therefore, if the differential allocation of bitrate resources is carried out based on visual sensitivity, the re- source utilization and user QoE are supposed to be further improved. How

**[Datos / trazas / datasets | extracto 10 | p.6]**

rved that lower visual sensitivity chunks (marked in blue) typically are lower in saliency and higher in visual masking property, while higher visual sensitivity chunks (marked in red) are higher in saliency and lower in visual masking property. 3.2 Challenges for ABR Similar to [34], we select two types of video chunks (marked in red and blue) in Section 3.1 to compare different ABR strategies. VMAF [47], a full-reference quality metric is used to measure the video quality perceived by users, which has been proved to be closely related to subjective MOS scores. VMAF scores range from 0 to 100, where 0–20, 20–40, 40–60, 60–80, and 80–100 are considered as unacceptable, poor, fair, good, and excellent quality, respectively [48]. Figure 2 shows the bitrate and VMAF of Pensieve [11] and visual sensitivity aware ABR (denoted as VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The bitrates of two strategies are significantly different, and VS-ABR realizes a smoother range of VMAF scores in Figure 2(b). We find an interesting phenomenon from this experiment that carefully reducing the bitrate of lower visual sensitivity video chunks and allocating the saved resources to high visual sensitivity video chunks will achieve greater benefit. Since HVS can’t detect the existing distortion for the former, lowering a certain bitrate level has little impact on perceptual video quality. Therefore, if the differential allocation of bitrate resources is carried out based on visual sensitivity, the re- source utilization and user QoE are supposed to be further

**[Datos / trazas / datasets | extracto 11 | p.6]**

bserved that lower visual sensitivity chunks (marked in blue) typically are lower in saliency and higher in visual masking property, while higher visual sensitivity chunks (marked in red) are higher in saliency and lower in visual masking property. 3.2 Challenges for ABR Similar to [34], we select two types of video chunks (marked in red and blue) in Section 3.1 to compare different ABR strategies. VMAF [47], a full-reference quality metric is used to measure the video quality perceived by users, which has been proved to be closely related to subjective MOS scores. VMAF scores range from 0 to 100, where 0–20, 20–40, 40–60, 60–80, and 80–100 are considered as unacceptable, poor, fair, good, and excellent quality, respectively [48]. Figure 2 shows the bitrate and VMAF of Pensieve [11] and visual sensitivity aware ABR (denoted as VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The bitrates of two strategies are significantly different, and VS-ABR realizes a smoother range of VMAF scores in Figure 2(b). We find an interesting phenomenon from this experiment that carefully reducing the bitrate of lower visual sensitivity video chunks and allocating the saved resources to high visual sensitivity video chunks will achieve greater benefit. Since HVS can’t detect the existing distortion for the former, lowering a certain bitrate level has little impact on perceptual video quality. Therefore, if the differential allocation of bitrate resources is carried out based on visual sensitivity, the re- source utilization and user QoE are supposed to be fu

**[Datos / trazas / datasets | extracto 12 | p.6]**

77:6 J. Ye et al. Fig. 1. The distribution of video chunks in visual masking property and saliency, which can be divided into three categories: lower visual sensitivity; higher visual sensitivity; and others. 3.1 Video Preprocessing Similar to [34], we use the “EnvivioDash3” video in DASH-246 JavaScript client [45] and divide it into 48 chunks. In addition, 48 video chunks are randomly selected from VideoSet [31], and we have 96 video chunks in total for evaluation. All video chunks are encoded by H.264/MPEG-4 at six bitrates (300kbps, 750kbps, 1200kbps, 1850kbps, 2850kbps, 4300kbps), which pertain to YouTube video modes. Researches [23, 27, 46] have shown that the luminance masking effect, spatial contrast masking effect, temporal masking effect and saliency have a significant impact on visual sensitivity. Therefore, we calculate the chunk-level average of each feature for each video chu

**[Datos / trazas / datasets | extracto 13 | p.7]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:7 Fig. 2. The evaluation of two ABR algorithms under the same network, including the bitrate and perceptual video quality of video chunks. that we only make a rough classification of visual sensitivity, and modeling it more accurately is required to obtain greater performance improvement. It is challenging because the complexity of HVS mechanism is usually difficult to quantify. Inspired by this, this paper attempts to model vi- sual sensitivity more accurately and integrates it into the ABR algorithm to optimize the existing algorithms. 4 SYSTEM DESIGN In this section, we first present the overview of visual sensitivity aware ABR algorithm for DASH, and then introduce two main modules of the proposed video streaming system in detail: (1) Visual Sensitivity Model; and (2) Visual Sensitivity Aware ABR. 4.1 System Structure In this paper, we propose a visual sensitivity model based on the total masking effect analysis and use it for a novel ABR algori

**[Datos / trazas / datasets | extracto 14 | p.8]**

77:8 J. Ye et al. Fig. 3. The structure of our visual sensitivity aware ABR algorithm for DASH. It can be seen that these two main components are deployed on the server side to avoid the resource constraints of client devices, and the performance of the ABR algorithm is not affected by the delay introduced by the packet switching between the client and the server to a great extent [4, 11], which can be masked by the playback buffer occupancy and chunk download time. 4.2 Visual Sensitivity Model In this subsection, we will describe the total masking effect model and the calculation of visual sensitivity in detail. We aim two tasks: (1) apply the state-of-the-art deep learning and the feed- back mechanism commonly existing in HVS to acquire an effective representation on the total masking effect of video content; and (2) analyze the relationship between the prediction result of the total masking effect model and the sensitivity of HVS to distortion to get the visual sensitivity of different video chunks for the ABR algorithm. As discussed in previous studies [32, 33, 46, 50], the perception of video quality distortion is closely related to two aspects (i.e., video content and video basic attributes), and different prior information can be calculated to model the features of these two aspects. Specifically, multiple manual feature maps reflecting different visual masking effects are extracted from the video frame as an important part of video content, and we develop a multi-stream CNN fusion network to cap- ture different features of video content more effectively. Instead of excessively relying on abstract features extracted by deep CNN

**[Datos / trazas / datasets | extracto 15 | p.9]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:9 Fig. 4. The description of the feature maps of frame 11 and frame 596 extracted from VideoSet, which cor- respond to the chunk 37 and chunk 98 in Figure 6. Since they contain the features with different spatial randomness, luminance, motion intensity and saliency, chunk 37 and chunk 98 are distributed in the range of higher and lower visual sensitivity, respectively. where N represents the amount of sampled video frames. FRk, REk, and BRk are the framerate, resolution, and bitrate, respectively, of the video chunk to which video frame k belongs. The four feature maps of video frame k are described as: SRMk (i, j) = Lk (i, j) −RLkLk R−1 Lk Lk (i, j) (2) LMk (i, j) = Lk (i, j) (3) TMk (i, j) = |Lk+d (i, j) −Lk (i, j)| (4) SMk (i, j) = F Lab k (i, j) −GLab k (i, j) (5) • For SRMk (i, j), Lk(i, j) is the luminance of the pixel at position (i, j) in video frame k, the spatial regularity of the pixel at position (i,

**[Datos / trazas / datasets | extracto 16 | p.10]**

, and the saliency map are fed into the Subnetwork-1, Subnetwork-2, Subnetwork-3, and Subnetwork-4, respectively to extract finer-grained features. Then the abstract features from four subnetworks and three attribute features are concatenated together and transported into the feed- back module, and the features processed after feedback are input to the fully connected layer to predict the FJND point. Finally, the loss value is calculated, followed by the target prediction. The whole process is formulated as: PSNRk = FB(Concat(sub1(SRMk (i, j)), sub2(LMk (i, j)), sub3(TMk (i, j)), sub4(SMk (i, j)), FRk, REk, BRk)) (6) where FB, Concat, subi denote the processes of the feedback, the concatenation, and the Subnetwork-i, respectively. Because the training of deep neural network needs a large number of samples, and the number of available JND datasets is limited, this paper adopts the patch-based training method to manually increase the data samples. Each input feature map is divided into multiple patches, and a certain number of patches are randomly selected and labeled as the FJND point of the corresponding video chunk for training. In order to accommodate the size of the input patch, the network is extended to three layers, namely conv1, conv2, and maxpool. The training process of the proposed model mainly includes three parts: feature fusion, feed- back looping, and spatial pooling. For feature fusion, we use a simple and commonly used concat() function to fuse the feature vectors extracted by convolution layers in each subnetwork and the attribute features, and then input them into the feedback module. The feedback module is designed to handle the feedback connections and genera

### 5.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

ual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterog

**[Evaluación / baselines / experimentos | extracto 2 | p.1]**

isting ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in Data Center Network (NO.61872387), and the Key Projec

**[Evaluación / baselines / experimentos | extracto 3 | p.1]**

needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traff

**[Evaluación / baselines / experimentos | extracto 4 | p.1]**

gorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in Data Center Network (NO.61872387), and the Key Project of Guan

**[Evaluación / baselines / experimentos | extracto 5 | p.1]**

locate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in Data Cente

**[Evaluación / baselines / experimentos | extracto 6 | p.1]**

with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con- tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively. Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning J. Ye and M. Dan contributed equally to this research. We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism

**[Evaluación / baselines / experimentos | extracto 7 | p.3]**

fect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows

**[Evaluación / baselines / experimentos | extracto 8 | p.3]**

design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and performance analysis. Section 6 concludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-o

**[Evaluación / baselines / experimentos | extracto 9 | p.3]**

iety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and performance a

**[Evaluación / baselines / experimentos | extracto 10 | p.3]**

ual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and performance analysis. Section 6 concludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art

**[Evaluación / baselines / experimentos | extracto 11 | p.3]**

aces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and performance analysis. Section 6 concludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, f

**[Evaluación / baselines / experimentos | extracto 12 | p.3]**

nt video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup

**[Evaluación / baselines / experimentos | extracto 13 | p.3]**

ludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Evaluación / baselines / experimentos | extracto 14 | p.3]**

two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our contributions are also presented at the end of each subsection. 2.1 Existing ABR Algorithms The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Evaluación / baselines / experimentos | extracto 15 | p.3]**

-art ABR algorithms mainly include the content-agnostic ABR algorithms and content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk size and download time to predict the future network throughput, and selects the bitrate to guide the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy, and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate adaptation scheme based on Markov decision to maximize the quality of user experience under ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Evaluación / baselines / experimentos | extracto 16 | p.4]**

77:4 J. Ye et al. time-varying channel conditions, taking into account factors such as video playback quality, video bitrate switching frequency and amplitude, buffer overflow/underflow, and buffer occupancy. Although the idea is easy to understand and simple to implement, the adaptability of the above works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm, continuously optimizes the ABR model by training two neural networks, and learns the adaptive strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy by imitating the expert trajectory given by the instant solver, which can avoid the repeated exploration and improve the sampling efficiency. The content-aware ABR algorithms additionally consider different objective and subjective fac- tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching, selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By adopting the same strategy for video chunks with similar content characteristics, it can both in- crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the region of interest-based adaptive multimedia streaming

### 5.x Limitaciones / riesgos / implementación

**[Limitaciones / riesgos / implementación | extracto 1 | p.1]**

l Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning JIN YE and MENG DAN, Guangxi University, China WENCHAO JIANG, Singapore University of Technology and Design, Singapore In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver of video, HVS has different sensitivity to the quality distortion of different video content, and video content with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and attribute features from the video, and consider the simulation of HVS to establish a total masking effect model that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual sensitivity are comprehensively considered under a deep reinforcement learning framework to select the appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven evaluation and compare its performance with several latest algorithms. Experimental results show that our algorith

**[Limitaciones / riesgos / implementación | extracto 2 | p.2]**

bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t perceive a certain degree of quality distortion due to the existence of the visual masking effect. In other words, user QoE can be improved by increasing the video quality of a more perceivable portion of video content. Inspired by this, we introduce visual sensitivity to measure the relationship between HVS characteristics and video content. We model the total ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 20

**[Limitaciones / riesgos / implementación | extracto 3 | p.2]**

pendence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t perceive a certain degree of quality distortion due to the existence of the visual masking effect. In other words, user QoE can be improved by increasing the video quality of a more perceivable portion of video content. Inspired by this, we introduce visual sensitivity to measure the relationship between HVS characteristics and video content. We model the total ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Limitaciones / riesgos / implementación | extracto 4 | p.2]**

ing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy- namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer, and CPU status). Specifically, when the network is in good condition, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13

**[Limitaciones / riesgos / implementación | extracto 5 | p.2]**

, the player can select a high bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer- ings once the network becomes worse. The existing works on ABR can be classified into two categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms. The content-agnostic ABR algorithms mainly focus on the network environment and player state, and select the bitrate of video chunks by predicting the future network throughput [3, 4], observing the current buffer occupancy [5, 6], or comprehensively considering these two factors [7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa- rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances [10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi- tation is that it is assumed users have the same sense of video quality throughout the video, so the video quality is optimized using the same standard in different parts of the video. The content-aware ABR algorithms further consider different characteristics of video con- tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to the inherent limitations of human visual system (HVS), we find that a promising direction is to optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g., highlights and objects), and ignore the perception ability of HVS to video distortion. It is found that HVS can’t perceive a certain degree of quality distorti

**[Limitaciones / riesgos / implementación | extracto 6 | p.2]**

ticle 77 (November 2023), 22 pages. https://doi.org/10.1145/3591108 1 INTRODUCTION With the rapid development of multimedia streaming technologies, there has been a surge in video services and applications. As predicted in [1], by 2022, video streaming will account for more than 82% of total Internet traffic, and users’ demand for high-quality video services will continue to in- crease. The quality of experience (QoE) of users has become a central concern for video content providers to increase revenue. Traditional content providers provide users with several bitrates (e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video streaming services due to the instability of network bandwidth and the diversity of user demands. Many studies have proposed adaptive video streaming technology to meet this challenge and max- imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be- come the main standard. By using the HTTP protocol to transmit video, content providers can make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto- col is compatible with many client applications. In the adaptive transmission framework of DASH, each video file on the HTTP server is divided into multiple video chunks with equal duration and encoded into multiple bitrate levels representing different qualities. A manifest--media presen- tation description (MPD) is adopted to describe the information of all video chunks. The DASH client first requests the MPD file from the server and obtains information such as media type, res- olution, optional coding scheme and accessibility characteristics, and so on. Then,

**[Limitaciones / riesgos / implementación | extracto 7 | p.3]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:3 masking effect of video content by fitting human perception to reflect the sensitivity of HVS to quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm to improve user QoE. The main contributions of this paper are threefold: • Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of different visual masking effects on the perception of HVS to quality distortion, we propose a total masking effect model for different video contents. The model adopts a variety of video features as input, and trains features by a multi-stream deep convolutional neural network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement

**[Limitaciones / riesgos / implementación | extracto 8 | p.3]**

existing in human visual cortex is integrated into the model to achieve accuracy improvement. • We give the definition of visual sensitivity based on the total masking effect model, which is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining visual sensitivity with the input state and reward function of reinforcement learning (RL) algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information to further optimize the resource utilization and user QoE. • We conduct extensive evaluations with both real-world and synthetic network traces. Compared with the latest visual sensitivity prediction methods, the total masking effect model proposed in this paper has a higher prediction accuracy and is robust to the video resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi- cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective experimental results. The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the architecture of proposed system is presented in Section 4, followed by the design of total masking effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR. Section 5 shows the experimental setup, evaluation method, and performance analysis. Section 6 concludes the paper. 2 RELATED WORKS This section includes a review of the literature for the areas covered by this work. It can be mainly

**[Limitaciones / riesgos / implementación | extracto 9 | p.4]**

quality. Even if a higher bitrate is selected for video content that attracts visual attention, it may not be able to effectively improve the perceptual video quality, because it is uncertain whether users can perceive the video distortion. Therefore, the difference between our work and previous studies is that instead of proposing yet another quality metric, we consider the perception of HVS to video quality distortion for QoE optimization. This visual characteristic can be applied to optimize the ABR strategy in the case of limited network resources, for instance, switching to a lower bitrate when users can’t perceive the degradation of video quality. To our best knowledge, this is the first work to integrate the sensitivity of HVS to distortion into the ABR model for DASH. 2.2 Modeling of Visual Sensitivity Visual masking effect is a complex visual perception mechanism, which is caused by the inter- action or interference between stimuli. It refers to the reduced capability of HVS in perceiving stimuli such as distortion, edge, and motion under complex spatial or temporal background [22], mainly including luminance masking, spatial contrast masking and temporal masking. The luminance masking effect indicates that HVS is less sensitive to distortion in darker or brighter regions. The spatial contrast masking effect means that HVS is more likely to perceive the quality ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Limitaciones / riesgos / implementación | extracto 10 | p.5]**

sed in image/video processing [35–39], especially in simulating the HVS response mechanism [40, 41]. On this basis, we propose a data-driven multi-stream CNN-based VW-JND predictor, which can measure video characteristics from multiple aspects. By combining two kinds of manual features and the multi-stream CNN fusion network, the model can make full use of the respective features to acquire video characteristics more effectively. In addition, the proposed model also incorporates the feedback connection, which plays an important role in the visual cortex and is indispensable in the formation of quality perception [42–44]. 3 MOTIVATION In this section, we illustrate the importance of visual sensitivity in the ABR algorithm through an exploratory experiment, and prove that the existing ABR algorithm based on reinforcement learning still has limitations. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.

**[Limitaciones / riesgos / implementación | extracto 11 | p.5]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:5 distortion in smooth or highly structured regions. The temporal masking effect also shows that it is difficult to perceive the quality change for regions with fast and complex moving objects, and the speed exceeding a certain threshold will even lead to the loss of visual sensitivity. Since the visual masking effect can effectively reflect the inherent characteristics of HVS, it plays an important role in image and video processing [22–25]. Based on this, recent works have proposed the concept of just noticeable difference (JND), which means the minimum distortion HVS can perceive under the total masking effect of different picture/video contents (in the form of perception threshold). The traditional JND models can be divided into pixel-domain models and sub-band domain mod- els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these methods fail to effectively capture the interaction between pixels [26, 27] since human perceives the picture/video as a whole instead of focu

**[Limitaciones / riesgos / implementación | extracto 12 | p.5]**

tion of the first three JND points by binary search method. These subjective scores can be regarded as the ground truth of JND, but subjective methods are expensive and time-consuming, resulting in many limita- tions in practical applications. There are many other studies devoted to developing objective JND prediction models. Liu et al. [26] describe the prediction of PW-JND as a multi-class classification problem, and predicts each JND point of the compressed picture using deep learning technology. However, this method only takes the original picture as input which makes it difficult to learn ef- fective features for multifaceted analysis. Huang et al. [27] define a spatiotemporal sensitivity map by multiplying different features pixel by pixel, and proposes a VW-JND prediction method based on support vector regression (SVR). Due to the complexity of visual signal processing mecha- nism in HVS, this empirical-fused feature limits its adaptability to different scenarios. Wang et al. [32] predict different JND points by the regression of satisfied user ratio (SUR) curves. Similarly, Zhang et al. [33] uses Gaussian process regression (GPR) to model SUR curves and derives the JND points, but it is worth noting that the indirect prediction method is more challenging than the direct prediction. In order to solve the above defects, this paper focuses on the effective modeling of the total masking effect of different video contents. In comparison to our previous work [34], this work shows new contributions. Deep learning and neural network technology have been widely used in image/video processing [35–39], especially in simulating the HVS response mechanism [40, 41]. On this basis, we pro

**[Limitaciones / riesgos / implementación | extracto 13 | p.5]**

regions. The temporal masking effect also shows that it is difficult to perceive the quality change for regions with fast and complex moving objects, and the speed exceeding a certain threshold will even lead to the loss of visual sensitivity. Since the visual masking effect can effectively reflect the inherent characteristics of HVS, it plays an important role in image and video processing [22–25]. Based on this, recent works have proposed the concept of just noticeable difference (JND), which means the minimum distortion HVS can perceive under the total masking effect of different picture/video contents (in the form of perception threshold). The traditional JND models can be divided into pixel-domain models and sub-band domain mod- els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these methods fail to effectively capture the interaction between pixels [26, 27] since human perceives the picture/video as a whole instead of focusing on individual pixels. Picture wise JND (PW- JND)/Video wise JND (VW-JND) is further proposed to represent the JND threshold between a distorted picture/video and its reference (e.g., undistorted). In order to subjectively measure the PW-JND and VW-JND, many JND-based picture/video quality datasets [28–31] have been devel- oped. MCL-JCI [28] is a picture quality dataset under the JPEG compression standard. It contains 50 source pictures, each corresponding to 100 distorted pictures. By analyzing and processing the original JND data, the staircase quality function (SQF) is calculated. VideoSet [31] is a large- scale dataset consisting of 220 source video sequences with a duration of 5 seconds and four res- o

**[Limitaciones / riesgos / implementación | extracto 14 | p.6]**

(300kbps, 750kbps, 1200kbps, 1850kbps, 2850kbps, 4300kbps), which pertain to YouTube video modes. Researches [23, 27, 46] have shown that the luminance masking effect, spatial contrast masking effect, temporal masking effect and saliency have a significant impact on visual sensitivity. Therefore, we calculate the chunk-level average of each feature for each video chunk and fuse it appropriately. Figure 1 shows the distribution of selected video chunks in visual masking property and saliency, the larger the normalized features, the stronger the visual masking effect or saliency. It can be observed that lower visual sensitivity chunks (marked in blue) typically are lower in saliency and higher in visual masking property, while higher visual sensitivity chunks (marked in red) are higher in saliency and lower in visual masking property. 3.2 Challenges for ABR Similar to [34], we select two types of video chunks (marked in red and blue) in Section 3.1 to compare different ABR strategies. VMAF [47], a full-reference quality metric is used to measure the video quality perceived by users, which has been proved to be closely related to subjective MOS scores. VMAF scores range from 0 to 100, where 0–20, 20–40, 40–60, 60–80, and 80–100 are considered as unacceptable, poor, fair, good, and excellent quality, respectively [48]. Figure 2 shows the bitrate and VMAF of Pensieve [11] and visual sensitivity aware ABR (denoted as VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The bitrates of two strategies are significantly different, and VS-ABR realizes a smoo

**[Limitaciones / riesgos / implementación | extracto 15 | p.7]**

A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning 77:7 Fig. 2. The evaluation of two ABR algorithms under the same network, including the bitrate and perceptual video quality of video chunks. that we only make a rough classification of visual sensitivity, and modeling it more accurately is required to obtain greater performance improvement. It is challenging because the complexity of HVS mechanism is usually difficult to quantify. Inspired by this, this paper attempts to model vi- sual sensitivity more accurately and integrates it into the ABR algorithm to optimize the existing algorithms. 4 SYSTEM DESIGN In this section, we first present the overview of visual sensitivity aware ABR algorithm for DASH, and then introduce two main modules of the proposed video streaming system in detail: (1) Visual Sensitivity Model; and (2) Visual Sensitivity Aware ABR. 4.1 System Structure In this paper, we propose a visual sensitivity model based on the total masking effect analysis and use it for a novel ABR algorithm in a video streaming system. As shown in Figure 3, the visual sensitivity aware ABR controller outputs the bitrate of the next video chunk by integrating the state information from the DASH client and visual se

**[Limitaciones / riesgos / implementación | extracto 16 | p.15]**

evaluate the prediction accuracy, namely MAE and its variance (VAR). For a full evaluation, we use the 5-fold cross validation method, and the results are shown in Table 2. GJND has the largest prediction error in the two metrics due to the inaccuracy of the manual-fused features. Although GPR-SUR achieves relatively better performance, the method of combining video content features with multi-stream CNN network can decrease the MAE and VAR by at least 12.32% and 9.85% respectively, which benefits from the effectiveness of the considered features and model structure. More importantly, the model incorporating video attribute features and HVS feedback module has a better prediction accuracy and reduces the prediction error to less than 0.9. What’s more, the average MAE and VAR of four resolutions are 0.74 and 0.75, which further proves the robustness and effectiveness of proposed model in simulating the HVS perception mechanism. An ablation study is carried out in this paper to further analyze the effectiveness of four feature maps. For video frame k, we define three feature subsets with randomly selected feature maps of 1, 2 and 3 numbers. We take three feature subsets and the feature set containing all feature maps as the inputs of the proposed model for testing. The settings of three feature subsets are: (1) only SRM; (2) Containing SRM and LM; and (3) Containing SRM, LM, and TM. As shown in Figure 7, compared with Figures 7(a), (b) and (c), most points in Figure 7(d) are more concentrated near the line of y = x, indicating that the combination of four features can achieve the minimum prediction error. 5.2 Evaluation of ABR Algorithm 5.2.1 Simulation Experiment. In this paper,

## 6. Figuras / tablas / algoritmos / ecuaciones detectados por texto
- p.6: Fig. 1. The distribution of video chunks in visual masking property and saliency, which can be divided into
- p.6: Figure 1 shows the distribution of selected video chunks in visual masking property
- p.6: Figure 2
- p.6: Figure 2(b).
- p.7: Fig. 2. The evaluation of two ABR algorithms under the same network, including the bitrate and perceptual
- p.7: Figure 3, the visual
- p.8: Fig. 3. The structure of our visual sensitivity aware ABR algorithm for DASH.
- p.9: Fig. 4. The description of the feature maps of frame 11 and frame 596 extracted from VideoSet, which cor-
- p.9: Figure 6. Since they contain the features with different spatial
- p.9: Figure 4 shows the feature maps of two frames in video chunk 37 and 98 in VideoSet [31]. As
- p.9: Figure 4(b) is slightly darker than that in Figure 4(f).
- p.9: Figure 4(d)
- p.10: Figure 4(h). As mentioned earlier, higher spatial randomness,
- p.10: Figure 6).
- p.10: Figure 5. It is based on the advanced VGG network [54], which is inspired by the
- p.11: Fig. 5. Design of the total masking effect model.
- p.11: Figure 6 shows the distribution of VS for some video chunks
- p.11: Figure 4 correspond to chunk 37 and
- p.12: Fig. 6. The distribution of VS for sampled video chunks, which spans three different intervals.
- p.14: Table 1. Notation and Definition
- p.14: Table 1 summarizes the key notations used in this paper.
- p.15: Table 2. Evaluation of Six Methods
- p.15: Table 2. GJND has the largest prediction error in
- p.15: Figure 7, compared
- p.15: Figure 7(d) are more concentrated near the line of y =
- p.15: Algorithm 5.2.1
- p.16: Fig. 7. Results of ablation study, for each video frame in the sample, different number of feature maps
- p.16: Table 3. Bitrate of Three ABR Algorithms on 3G/HSDPA
- p.16: Table 3 shows the average
- p.16: Figure 8 shows the distribution of the VMAF, rebuffering time, quality smoothness, and overall
- p.16: Figure 8(a), all video sessions
- p.16: Figure 8(b) only describes the distribution of non-zero video rebuffering
- p.17: Fig. 8. QoE components of three ABR algorithms in each video session.
- p.17: Fig. 9. Comparison of three ABR algorithms on synthetic traces.
- p.17: Figure 9 shows the average normalized QoE of different ABR
- p.17: Figure 9(a), VS-ABR can achieve the QoE improvement at a minimum of
- p.18: Fig. 10. Comparison of three VS prediction methods and ABR algorithms.
- p.18: Figure 9(b) can effectively achieve a higher
- p.18: Figure 9(a) under the high throughput.
- p.18: Figure 10(a) shows the prediction results of three methods. The predicted
- p.18: Figure 10(b)
- p.18: Table 4. The total number of votes for each video type in
- p.19: Table 4. The Number of Votes for VS-ABR and Other Three Algorithms

## 7. Líneas con posible contenido matemático/formal
- p.2: `services and applications. As predicted in [1], by 2022, video streaming will account for more than`
- p.2: `imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be-`
- p.2: `state, and select the bitrate of video chunks by predicting the future network throughput [3, 4],`
- p.2: `observing the current buffer occupancy [5, 6], or comprehensively considering these two factors`
- p.2: `[7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa-`
- p.2: `[10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi-`
- p.2: `tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to`
- p.3: `network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages`
- p.3: `a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk`
- p.3: `the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for`
- p.3: `events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses`
- p.3: `near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy,`
- p.3: `and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate`
- p.4: `works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to`
- p.4: `networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm,`
- p.4: `strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy`
- p.4: `tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching,`
- p.4: `high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By`
- p.4: `crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the`
- p.4: `supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the`
- p.4: `results provide a video bitrate saving method for content providers. In addition, Gao et al. [18]`
- p.4: `with higher quality. Hu et al. [19] propose a semantic-aware adaptation scheme for MPEG-DASH`
- p.4: `ceived by users. In his latest work [20], an affective content-aware adaptation scheme is proposed.`
- p.4: `[22], mainly including luminance masking, spatial contrast masking and temporal masking. The`
- p.5: `in image and video processing [22–25]. Based on this, recent works have proposed the concept of`
- p.5: `methods fail to effectively capture the interaction between pixels [26, 27] since human perceives`
- p.5: `PW-JND and VW-JND, many JND-based picture/video quality datasets [28–31] have been devel-`
- p.5: `oped. MCL-JCI [28] is a picture quality dataset under the JPEG compression standard. It contains`
- p.5: `original JND data, the staircase quality function (SQF) is calculated. VideoSet [31] is a large-`
- p.5: `prediction models. Liu et al. [26] describe the prediction of PW-JND as a multi-class classification`
- p.5: `fective features for multifaceted analysis. Huang et al. [27] define a spatiotemporal sensitivity map`
- p.5: `[32] predict different JND points by the regression of satisfied user ratio (SUR) curves. Similarly,`
- p.5: `Zhang et al. [33] uses Gaussian process regression (GPR) to model SUR curves and derives the`
- p.5: `masking effect of different video contents. In comparison to our previous work [34], this work`
- p.5: `in image/video processing [35–39], especially in simulating the HVS response mechanism [40, 41].`
- p.5: `in the formation of quality perception [42–44].`
- p.6: `Similar to [34], we use the “EnvivioDash3” video in DASH-246 JavaScript client [45] and divide`
- p.6: `it into 48 chunks. In addition, 48 video chunks are randomly selected from VideoSet [31], and we`
- p.6: `video modes. Researches [23, 27, 46] have shown that the luminance masking effect, spatial contrast`
- p.6: `Similar to [34], we select two types of video chunks (marked in red and blue) in Section 3.1 to`
- p.6: `compare different ABR strategies. VMAF [47], a full-reference quality metric is used to measure`
- p.6: `are considered as unacceptable, poor, fair, good, and excellent quality, respectively [48]. Figure 2`
- p.6: `shows the bitrate and VMAF of Pensieve [11] and visual sensitivity aware ABR (denoted as`
- p.6: `VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual`
- p.8: `[4, 11], which can be masked by the playback buffer occupancy and chunk download time.`
- p.8: `As discussed in previous studies [32, 33, 46, 50], the perception of video quality distortion is`
- p.8: `Fk = {SRMk (i, j), LMk (i, j), TMk (i, j), SMk (i, j), FRk, REk, BRk}, 1 ≤k ≤N`
- p.9: `j) = {Lk(i, j+1), Lk(i+1, j), Lk(i, j-1), Lk(i-1, j)}. RLkLk is the covariance matrix of Lk (i, j) and`
- p.9: `• For SMk (i, j), we use the frequency-tuned saliency detection method [51], which is better`
- p.9: `than the method in our previous work [34]. F Lab`
- p.9: `Figure 4 shows the feature maps of two frames in video chunk 37 and 98 in VideoSet [31]. As`
- p.10: `generally represented by coding parameters (e.g., QP), bitrate, and quality metrics (e.g., PSNR [52],`
- p.10: `SSIM [53]). Among them, QP controls the quality of video coding, bitrate represents the amount of`
- p.10: `is shown in Figure 5. It is based on the advanced VGG network [54], which is inspired by the`
- p.11: `sampled from VideoSet [31]. It can be seen that it is distributed in different intervals for different`
- p.12: `[21]. Reinforcement learning originated from animal learning in psychology and is an important`
- p.13: `πθ (st,at ) →[0, 1], a probability of taking at at st, and θ is a parameter set of actor network. Critic`
- p.13: `network also outputs the predicted valueV πθ (st ) based on this policy. After the actionat is applied,`
- p.13: `in parallel to speed up the training process as suggested by [11].`
- p.13: `commonly used linear QoE model [12] and visual sensitivity, which is similar to the idea of our`
- p.13: `previous work [34], but it worth noting that we have more accurate visual sensitivity information.`
- p.13: `[VMAF (Rt+1) −VMAF (Rt )]+`
- p.13: `[VMAF (Rt+1) −VMAF (Rt )]−`
- p.13: `loaded at bitrate Rt, which promotes the fluent video playback. [VMAF (Rt+1) −VMAF (Rt )]+ and`
- p.13: `[VMAF (Rt+1)−VMAF (Rt )]−represents the positive and negative quality smoothness, respectively.`
- p.13: `αV St , β, γ and δ are the aggressive parameters of perceptual video quality, video rebuffering time,`
- p.13: `αV St = VSt · μ + ξ`
- p.13: `VMAF (Rt ) in the range of [ξ, μ + ξ], i.e., αV St . By assigning higher weight to the video chunk`
- p.14: `VideoSet [31] dataset to train and test the evaluated model. The dataset is a JND based video`
- p.15: `Adam [55] is used as the optimization method of gradient descent, and the learning rate of batch`
- p.15: `optimization is adaptively controlled. As recommended in [55], the learning rate is initialized`
- p.15: `In addition to the three existing baseline prediction methods GJND [27], SUR-FJND [32], and`
- p.15: `GPR-SUR [33], this paper also compares the prediction method of only combining video content`
- p.15: `SVR regression of the data samples from VideoSet [31] are exactly the same as the framework of`
- p.16: `are randomly selected as the input of the total masking effect model( {SRM}, {SRM,LM}, {SRM,LM,TM},`
- p.16: `{SRM,LM,TM,SM} ), it is shown that the combination of four feature maps can achieve the minimum pre-`
- p.16: `simulator provided by [11]. We adopt two kinds of real network traces, 3G/HSDPA mobile dataset`
- p.16: `[49] and FCC bandwidth dataset [56]. The 3G/HSDPA dataset includes 30 minute throughput mea-`
- p.16: `cludes the “EnvivioDash3” [45], and seven videos consisting of 8-18 video sequences from VideoSet`
- p.16: `[31]. This experiment tests all eight videos, and compares the VS-ABR with RobustMPC [7] and`

## 8. Texto crudo completo por página

> Mantener este bloque para Codex si necesita comprobar contexto literal. Puede contener errores de orden por columnas del PDF. Para fórmulas exactas o tablas complejas, usar PDF original.


### Página 1

```text
77
A Visual Sensitivity Aware ABR Algorithm for DASH via
Deep Reinforcement Learning
JIN YE and MENG DAN, Guangxi University, China
WENCHAO JIANG, Singapore University of Technology and Design, Singapore
In order to cope with the fluctuation of network bandwidth and provide smooth video services, adaptive
video streaming technology is proposed. In particular, the adaptive bitrate (ABR) algorithm is widely used in
dynamic adaptive streaming over HTTP (DASH) to improve quality of experience (QoE). However, existing
ABR algorithms still ignore the inherent visual sensitivity of human visual system (HVS). As the final receiver
of video, HVS has different sensitivity to the quality distortion of different video content, and video content
with high visual sensitivity needs to allocate more bitrate resources. Therefore, existing ABR algorithms
still have limitations in reasonably allocating bitrate and maximizing QoE. To solve this problem, this paper
designs an adaptive bitrate strategy from the perspective of user vision, studies the modeling of visual
sensitivity, and proposes a visual sensitivity aware ABR algorithm. We extract a set of content features and
attribute features from the video, and consider the simulation of HVS to establish a total masking effect model
that reflects the visual sensitivity more accurately. Further, the network status, buffer occupancy, and visual
sensitivity are comprehensively considered under a deep reinforcement learning framework to select the
appropriate bitrate for maximizing QoE. We implement the proposed algorithm over a realistic trace-driven
evaluation and compare its performance with several latest algorithms. Experimental results show that our
algorithm can align ABR strategy with visual sensitivity to achieve better QoE in high visual sensitivity con-
tent, and improves the average perceptual video quality and overall user QoE by 18.3% and 22.8%, respectively.
Additionally, we prove the feasibility of our algorithm through subjective evaluation in the real environment.
CCS Concepts: • Information systems →Multimedia streaming;
Additional Key Words and Phrases: ABR, DASH, QoE, visual sensitivity, deep reinforcement learning
J. Ye and M. Dan contributed equally to this research.
We would like to acknowledge the support from the Project of End to End Transmission Theory and Key Technologies
Ensuring Deterministic Delay (NO.62132022), the Research on Load Balancing Mechanism for Heterogeneous Traffic in
Data Center Network (NO.61872387), and the Key Project of Guangxi Science & Technology (NO.2021AB06002).
This work was supported by the Ministry of Education, Singapore, under its Academic Research Fund Tier 2 (MOE-
T2EP20221-0017); the National Research Foundation, Singapore and Infocomm Media Development Authority under its
Future Communications Research & Development Programme; and the Key Project of Guangxi Science & Technology
(NO.2021AB06002).
Authors’ addresses: J. Ye and M. Dan, Guangxi Key Laboratory of Multimedia Communications and Network Technology,
School of Computer and Electronic Information, Guangxi University, Nanning 530000, China; emails: yejin@gxu.edu.cn,
1913392006@st.gxu.edu.cn; W. Jiang, Information Systems Technology and Design, Singapore University of Technology
and Design, 487372, Singapore; email: wenchaojiang@sutd.edu.sg.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be
honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists,
requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
1551-6857/2023/11-ART77 $15.00
https://doi.org/10.1145/3591108
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 2

```text
77:2
J. Ye et al.
ACM Reference format:
Jin Ye, Meng Dan, and Wenchao Jiang. 2023. A Visual Sensitivity Aware ABR Algorithm for DASH via Deep
Reinforcement Learning. ACM Trans. Multimedia Comput. Commun. Appl. 20, 3, Article 77 (November 2023),
22 pages.
https://doi.org/10.1145/3591108
1
INTRODUCTION
With the rapid development of multimedia streaming technologies, there has been a surge in video
services and applications. As predicted in [1], by 2022, video streaming will account for more than
82% of total Internet traffic, and users’ demand for high-quality video services will continue to in-
crease. The quality of experience (QoE) of users has become a central concern for video content
providers to increase revenue. Traditional content providers provide users with several bitrates
(e.g., 1200 kbps and 1850 kbps) to choose from, but a fixed bitrate can’t achieve satisfactory video
streaming services due to the instability of network bandwidth and the diversity of user demands.
Many studies have proposed adaptive video streaming technology to meet this challenge and max-
imize users’ QoE. Among them, dynamic adaptive streaming over HTTP (DASH) [2] has be-
come the main standard. By using the HTTP protocol to transmit video, content providers can
make full use of the existing content delivery network (CDN) infrastructure, and HTTP proto-
col is compatible with many client applications. In the adaptive transmission framework of DASH,
each video file on the HTTP server is divided into multiple video chunks with equal duration and
encoded into multiple bitrate levels representing different qualities. A manifest--media presen-
tation description (MPD) is adopted to describe the information of all video chunks. The DASH
client first requests the MPD file from the server and obtains information such as media type, res-
olution, optional coding scheme and accessibility characteristics, and so on. Then, the client-side
player uses an adaptive bitrate (ABR) algorithm to request future video chunks, which can dy-
namically select the bitrate according to different inputs (e.g., network bandwidth, player buffer,
and CPU status). Specifically, when the network is in good condition, the player can select a high
bitrate to ensure high video quality, and switch to a lower bitrate to avoid frequent video rebuffer-
ings once the network becomes worse. The existing works on ABR can be classified into two
categories: the content-agnostic ABR algorithms and the content-aware ABR algorithms.
The content-agnostic ABR algorithms mainly focus on the network environment and player
state, and select the bitrate of video chunks by predicting the future network throughput [3, 4],
observing the current buffer occupancy [5, 6], or comprehensively considering these two factors
[7–9]. However, due to the ideal assumptions about the environment and heavy dependence on pa-
rameter fine-tuning, these early works can’t adapt to various network conditions. Recent advances
[10–13] have proposed learning-based ABR algorithms to improve the robustness, but a key limi-
tation is that it is assumed users have the same sense of video quality throughout the video, so the
video quality is optimized using the same standard in different parts of the video.
The content-aware ABR algorithms further consider different characteristics of video con-
tent, including attracting visual attention [14–17] and users’ subjective preference [18–20]. Due to
the inherent limitations of human visual system (HVS), we find that a promising direction is to
optimize ABR strategy from the perspective of HVS. However, existing algorithms only consider
a single characteristic (e.g., motion) or the information with diverse and complex distribution (e.g.,
highlights and objects), and ignore the perception ability of HVS to video distortion.
It is found that HVS can’t perceive a certain degree of quality distortion due to the existence of
the visual masking effect. In other words, user QoE can be improved by increasing the video quality
of a more perceivable portion of video content. Inspired by this, we introduce visual sensitivity
to measure the relationship between HVS characteristics and video content. We model the total
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 3

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:3
masking effect of video content by fitting human perception to reflect the sensitivity of HVS to
quality distortion more accurately, and further explore a visual sensitivity aware ABR algorithm
to improve user QoE. The main contributions of this paper are threefold:
• Due to the complexity of the HVS interactive mechanism, existing visual sensitivity models
are still insufficient in simulating HVS characteristics. Based on the analysis of the impact of
different visual masking effects on the perception of HVS to quality distortion, we propose
a total masking effect model for different video contents. The model adopts a variety of
video features as input, and trains features by a multi-stream deep convolutional neural
network (CNN). Besides, the feedback mechanism of HVS widely existing in human visual
cortex is integrated into the model to achieve accuracy improvement.
• We give the definition of visual sensitivity based on the total masking effect model, which
is adopted to design a visual sensitivity aware ABR algorithm for DASH. By combining
visual sensitivity with the input state and reward function of reinforcement learning (RL)
algorithm, our ABR algorithm aims to align higher/lower video quality with higher/lower
visual sensitivity, and allocate bitrate based on more accurate visual sensitivity information
to further optimize the resource utilization and user QoE.
• We conduct extensive evaluations with both real-world and synthetic network traces.
Compared with the latest visual sensitivity prediction methods, the total masking effect
model proposed in this paper has a higher prediction accuracy and is robust to the video
resolution. Compared with the state-of-the-art ABR algorithms, our algorithm can signifi-
cantly improve the user QoE by 22.8%, and shows better video viewing quality in subjective
experimental results.
The remainder of this paper is organized as follows. Section 2 discusses the related works on ABR
strategies and visual sensitivity. In Section 3, we give our research motivation. The overview of the
architecture of proposed system is presented in Section 4, followed by the design of total masking
effect model, the definition of visual sensitivity, and the details of visual sensitivity aware ABR.
Section 5 shows the experimental setup, evaluation method, and performance analysis. Section 6
concludes the paper.
2
RELATED WORKS
This section includes a review of the literature for the areas covered by this work. It can be mainly
divided into two parts: (1) Adaptive bitrate algorithms; and (2) Modeling of visual sensitivity. Our
contributions are also presented at the end of each subsection.
2.1
Existing ABR Algorithms
The state-of-the-art ABR algorithms mainly include the content-agnostic ABR algorithms and
content-aware ABR algorithms. In the traditional content-agnostic methods, the estimated
network throughput and measured buffer occupancy are two main concerns. CS2P [3] leverages
a data-driven approach to learn the throughput prediction. Festive [4] adopts the video chunk
size and download time to predict the future network throughput, and selects the bitrate to guide
the trade-off between stability, fairness, and efficiency. BBA [5] designs a mapping function for
the bitrate and buffer occupancy, and controls the size of the available buffer to avoid rebuffering
events. BOLA [6] formulates bitrate adaptation as a utility-maximization problem and uses
Lyapunov optimization to minimize rebuffering and maximize video quality, which can achieve
near-optimal utility. MPC [7] jointly considers the throughput prediction and buffer occupancy,
and proposes a model predictive control framework to maximize QoE. mDASH [9] adopts a rate
adaptation scheme based on Markov decision to maximize the quality of user experience under
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 4

```text
77:4
J. Ye et al.
time-varying channel conditions, taking into account factors such as video playback quality, video
bitrate switching frequency and amplitude, buffer overflow/underflow, and buffer occupancy.
Although the idea is easy to understand and simple to implement, the adaptability of the above
works is poor. D-DASH [10] utilizes deep learning and reinforcement learning techniques to
optimize the QoE, the adaptive strategy is realized by using the architecture with two dual neural
networks based on deep Q-learning. Pensieve [11] adopts the most advanced A3C [21] algorithm,
continuously optimizes the ABR model by training two neural networks, and learns the adaptive
strategy only based on the results of past decisions. Comyco [12] generates the ABR strategy
by imitating the expert trajectory given by the instant solver, which can avoid the repeated
exploration and improve the sampling efficiency.
The content-aware ABR algorithms additionally consider different objective and subjective fac-
tors. Hu et al. [14] firstly use the scene type and motion intensity information for bitrate switching,
selecting a high bitrate to improve the QoE when the motion intensity of the video scene is at a
high level. Wilk et al. [15] propose a video adaptive service (VAS) supporting mobile devices. By
adopting the same strategy for video chunks with similar content characteristics, it can both in-
crease the perceptual quality as well as reduce the data traffic. Ciubotaru et al. [16] introduce the
region of interest-based adaptive multimedia streaming scheme (ROIAS), which adjusts
the video quality relative to the location of the areas of maximum user interest (AMUI), and
supports multiple regions of interest in the same video frame. Wijnants et al. [17] decompose the
video into multiple objects based on two video object representation methods, and allows for the
quality-variant HTTP adaptive streaming of background and foreground objects. These research
results provide a video bitrate saving method for content providers. In addition, Gao et al. [18]
propose an interest-aware rate adaptive method, which identifies users’ interest for different video
scenes through video semantics and users’ preference, and delivers the video of interest to users
with higher quality. Hu et al. [19] propose a semantic-aware adaptation scheme for MPEG-DASH
services, making bitrate decisions depending on content descriptors of the important content per-
ceived by users. In his latest work [20], an affective content-aware adaptation scheme is proposed.
The method analyzes the emotional demands of users, and introduces an affective relevancy mea-
surement to quantify personalized emotional preference.
In the above content-aware ABR algorithms, although different metrics are adopted to optimize
video quality, they still ignore the visibility of video quality distortion, which is an important factor
affecting users’ perceptual video quality. Even if a higher bitrate is selected for video content that
attracts visual attention, it may not be able to effectively improve the perceptual video quality,
because it is uncertain whether users can perceive the video distortion. Therefore, the difference
between our work and previous studies is that instead of proposing yet another quality metric,
we consider the perception of HVS to video quality distortion for QoE optimization. This visual
characteristic can be applied to optimize the ABR strategy in the case of limited network resources,
for instance, switching to a lower bitrate when users can’t perceive the degradation of video quality.
To our best knowledge, this is the first work to integrate the sensitivity of HVS to distortion into
the ABR model for DASH.
2.2
Modeling of Visual Sensitivity
Visual masking effect is a complex visual perception mechanism, which is caused by the inter-
action or interference between stimuli. It refers to the reduced capability of HVS in perceiving
stimuli such as distortion, edge, and motion under complex spatial or temporal background
[22], mainly including luminance masking, spatial contrast masking and temporal masking. The
luminance masking effect indicates that HVS is less sensitive to distortion in darker or brighter
regions. The spatial contrast masking effect means that HVS is more likely to perceive the quality
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 5

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:5
distortion in smooth or highly structured regions. The temporal masking effect also shows that it
is difficult to perceive the quality change for regions with fast and complex moving objects, and the
speed exceeding a certain threshold will even lead to the loss of visual sensitivity. Since the visual
masking effect can effectively reflect the inherent characteristics of HVS, it plays an important role
in image and video processing [22–25]. Based on this, recent works have proposed the concept of
just noticeable difference (JND), which means the minimum distortion HVS can perceive under
the total masking effect of different picture/video contents (in the form of perception threshold).
The traditional JND models can be divided into pixel-domain models and sub-band domain mod-
els, calculating the JND threshold for each pixel or each sub-band, respectively. However, these
methods fail to effectively capture the interaction between pixels [26, 27] since human perceives
the picture/video as a whole instead of focusing on individual pixels. Picture wise JND (PW-
JND)/Video wise JND (VW-JND) is further proposed to represent the JND threshold between a
distorted picture/video and its reference (e.g., undistorted). In order to subjectively measure the
PW-JND and VW-JND, many JND-based picture/video quality datasets [28–31] have been devel-
oped. MCL-JCI [28] is a picture quality dataset under the JPEG compression standard. It contains
50 source pictures, each corresponding to 100 distorted pictures. By analyzing and processing the
original JND data, the staircase quality function (SQF) is calculated. VideoSet [31] is a large-
scale dataset consisting of 220 source video sequences with a duration of 5 seconds and four res-
olutions (1920×1080, 1280×720, 960×540, and 640×360). It measures the distribution of the first
three JND points by binary search method. These subjective scores can be regarded as the ground
truth of JND, but subjective methods are expensive and time-consuming, resulting in many limita-
tions in practical applications. There are many other studies devoted to developing objective JND
prediction models. Liu et al. [26] describe the prediction of PW-JND as a multi-class classification
problem, and predicts each JND point of the compressed picture using deep learning technology.
However, this method only takes the original picture as input which makes it difficult to learn ef-
fective features for multifaceted analysis. Huang et al. [27] define a spatiotemporal sensitivity map
by multiplying different features pixel by pixel, and proposes a VW-JND prediction method based
on support vector regression (SVR). Due to the complexity of visual signal processing mecha-
nism in HVS, this empirical-fused feature limits its adaptability to different scenarios. Wang et al.
[32] predict different JND points by the regression of satisfied user ratio (SUR) curves. Similarly,
Zhang et al. [33] uses Gaussian process regression (GPR) to model SUR curves and derives the
JND points, but it is worth noting that the indirect prediction method is more challenging than the
direct prediction.
In order to solve the above defects, this paper focuses on the effective modeling of the total
masking effect of different video contents. In comparison to our previous work [34], this work
shows new contributions. Deep learning and neural network technology have been widely used
in image/video processing [35–39], especially in simulating the HVS response mechanism [40, 41].
On this basis, we propose a data-driven multi-stream CNN-based VW-JND predictor, which can
measure video characteristics from multiple aspects. By combining two kinds of manual features
and the multi-stream CNN fusion network, the model can make full use of the respective features
to acquire video characteristics more effectively. In addition, the proposed model also incorporates
the feedback connection, which plays an important role in the visual cortex and is indispensable
in the formation of quality perception [42–44].
3
MOTIVATION
In this section, we illustrate the importance of visual sensitivity in the ABR algorithm through
an exploratory experiment, and prove that the existing ABR algorithm based on reinforcement
learning still has limitations.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 6

```text
77:6
J. Ye et al.
Fig. 1. The distribution of video chunks in visual masking property and saliency, which can be divided into
three categories: lower visual sensitivity; higher visual sensitivity; and others.
3.1
Video Preprocessing
Similar to [34], we use the “EnvivioDash3” video in DASH-246 JavaScript client [45] and divide
it into 48 chunks. In addition, 48 video chunks are randomly selected from VideoSet [31], and we
have 96 video chunks in total for evaluation. All video chunks are encoded by H.264/MPEG-4 at six
bitrates (300kbps, 750kbps, 1200kbps, 1850kbps, 2850kbps, 4300kbps), which pertain to YouTube
video modes. Researches [23, 27, 46] have shown that the luminance masking effect, spatial contrast
masking effect, temporal masking effect and saliency have a significant impact on visual sensitivity.
Therefore, we calculate the chunk-level average of each feature for each video chunk and fuse it
appropriately. Figure 1 shows the distribution of selected video chunks in visual masking property
and saliency, the larger the normalized features, the stronger the visual masking effect or saliency.
It can be observed that lower visual sensitivity chunks (marked in blue) typically are lower in
saliency and higher in visual masking property, while higher visual sensitivity chunks (marked in
red) are higher in saliency and lower in visual masking property.
3.2
Challenges for ABR
Similar to [34], we select two types of video chunks (marked in red and blue) in Section 3.1 to
compare different ABR strategies. VMAF [47], a full-reference quality metric is used to measure
the video quality perceived by users, which has been proved to be closely related to subjective
MOS scores. VMAF scores range from 0 to 100, where 0–20, 20–40, 40–60, 60–80, and 80–100
are considered as unacceptable, poor, fair, good, and excellent quality, respectively [48]. Figure 2
shows the bitrate and VMAF of Pensieve [11] and visual sensitivity aware ABR (denoted as
VS-ABR) on 3G/HSDPA [49] dataset. There are a large number of video chunks with lower visual
sensitivity in region 1, while video chunks with higher visual sensitivity dominate region 2. The
bitrates of two strategies are significantly different, and VS-ABR realizes a smoother range of
VMAF scores in Figure 2(b).
We find an interesting phenomenon from this experiment that carefully reducing the bitrate of
lower visual sensitivity video chunks and allocating the saved resources to high visual sensitivity
video chunks will achieve greater benefit. Since HVS can’t detect the existing distortion for the
former, lowering a certain bitrate level has little impact on perceptual video quality. Therefore,
if the differential allocation of bitrate resources is carried out based on visual sensitivity, the re-
source utilization and user QoE are supposed to be further improved. However, it is worth noting
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 7

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:7
Fig. 2. The evaluation of two ABR algorithms under the same network, including the bitrate and perceptual
video quality of video chunks.
that we only make a rough classification of visual sensitivity, and modeling it more accurately is
required to obtain greater performance improvement. It is challenging because the complexity of
HVS mechanism is usually difficult to quantify. Inspired by this, this paper attempts to model vi-
sual sensitivity more accurately and integrates it into the ABR algorithm to optimize the existing
algorithms.
4
SYSTEM DESIGN
In this section, we first present the overview of visual sensitivity aware ABR algorithm for DASH,
and then introduce two main modules of the proposed video streaming system in detail: (1) Visual
Sensitivity Model; and (2) Visual Sensitivity Aware ABR.
4.1
System Structure
In this paper, we propose a visual sensitivity model based on the total masking effect analysis and
use it for a novel ABR algorithm in a video streaming system. As shown in Figure 3, the visual
sensitivity aware ABR controller outputs the bitrate of the next video chunk by integrating the
state information from the DASH client and visual sensitivity values from the video server. The
DASH client then requests the content delivery network (CDN) to download the corresponding
video chunk. The system is composed of two main components:
• Visual Sensitivity Model: We adopt a pre-trained deep multi-stream CNN model combined
with HVS feedback mechanism to learn the total masking effect, and perform a normalization
operation to calculate the relative visual sensitivity. The results are stored in MPD manifest
files as an extended property for each video chunk, which can be downloaded from the video
server directly when the video session starts.
• Visual Sensitivity Aware ABR: We redesign the adaptive strategy based on deep re-
inforcement learning. By comprehensively considering the estimated throughput, buffer
occupancy, and visual sensitivity of different video chunks, the new video streaming system
allows high-sensitivity video chunks to “borrow” bitrate resources from low-sensitivity
chunks, so as to achieve our goal that quality should be optimized in proportion to the visual
sensitivity.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 8

```text
77:8
J. Ye et al.
Fig. 3. The structure of our visual sensitivity aware ABR algorithm for DASH.
It can be seen that these two main components are deployed on the server side to avoid the
resource constraints of client devices, and the performance of the ABR algorithm is not affected
by the delay introduced by the packet switching between the client and the server to a great extent
[4, 11], which can be masked by the playback buffer occupancy and chunk download time.
4.2
Visual Sensitivity Model
In this subsection, we will describe the total masking effect model and the calculation of visual
sensitivity in detail. We aim two tasks: (1) apply the state-of-the-art deep learning and the feed-
back mechanism commonly existing in HVS to acquire an effective representation on the total
masking effect of video content; and (2) analyze the relationship between the prediction result of
the total masking effect model and the sensitivity of HVS to distortion to get the visual sensitivity
of different video chunks for the ABR algorithm.
As discussed in previous studies [32, 33, 46, 50], the perception of video quality distortion is
closely related to two aspects (i.e., video content and video basic attributes), and different prior
information can be calculated to model the features of these two aspects. Specifically, multiple
manual feature maps reflecting different visual masking effects are extracted from the video frame
as an important part of video content, and we develop a multi-stream CNN fusion network to cap-
ture different features of video content more effectively. Instead of excessively relying on abstract
features extracted by deep CNN networks, we integrate the video attribute features into abstract
CNN-based features to realize the mutual complement. In addition, we develop a computational
feedback mechanism in the deep neural network, which has not been fully exploited in the existing
VW-JND prediction methods.
4.2.1
Input of the Total Masking Effect Model. The input of the proposed model consists of
two parts: the features reflecting the visual masking effect and the features reflecting the intrinsic
properties of video. We adopt three basic attribute features, including the framerate (denoted as
FR), the resolution (denoted as RE), and the bitrate (denoted as BR) of each video chunk. Besides,
we sample each video chunk uniformly to obtain a group of video frames. Then we calculate four
feature maps for each video frame, including spatial randomness map (denoted as SRM), luminance
map (denoted as LM), temporal map (denoted as TM), and saliency map (denoted as SM). We define
a feature set Fk containing the above features for video frame k, expressed as:
Fk = {SRMk (i, j), LMk (i, j), TMk (i, j), SMk (i, j), FRk, REk, BRk}, 1 ≤k ≤N
(1)
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 9

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:9
Fig. 4. The description of the feature maps of frame 11 and frame 596 extracted from VideoSet, which cor-
respond to the chunk 37 and chunk 98 in Figure 6. Since they contain the features with different spatial
randomness, luminance, motion intensity and saliency, chunk 37 and chunk 98 are distributed in the range
of higher and lower visual sensitivity, respectively.
where N represents the amount of sampled video frames. FRk, REk, and BRk are the framerate,
resolution, and bitrate, respectively, of the video chunk to which video frame k belongs. The four
feature maps of video frame k are described as:
SRMk (i, j) = Lk (i, j) −RLkLk R−1
Lk
Lk (i, j)
(2)
LMk (i, j) = Lk (i, j)
(3)
TMk (i, j) = |Lk+d (i, j) −Lk (i, j)|
(4)
SMk (i, j) = F Lab
k
(i, j) −GLab
k
(i, j)
(5)
• For SRMk (i, j), Lk(i, j) is the luminance of the pixel at position (i, j) in video frame k, the
spatial regularity of the pixel at position (i, j) is measured by the neighborhood prediction
error of Lk(i, j). Lk(i, j) is a vector composed of four neighborhood pixels of Lk(i, j), i.e., Lk(i,
j) = {Lk(i, j+1), Lk(i+1, j), Lk(i, j-1), Lk(i-1, j)}. RLkLk is the covariance matrix of Lk (i, j) and
Lk (i, j), RLk is the self-correlation matrix of Lk(i, j);
• For LMk (i, j), it is directly represented by the luminance Lk (i, j) in video frame k;
• ForTMk (i, j), we calculate the luminance difference between sampled video frames to reflect
the motion intensity, and d is the interval between two frames;
• For SMk (i, j), we use the frequency-tuned saliency detection method [51], which is better
than the method in our previous work [34]. F Lab
k
(i, j) is the arithmetic mean value of the
pixel at position (i, j) on Lab color space in video frame k. GLab
k
(i, j) is the Gaussian blurred
value of the pixel at position (i, j) on Lab color space in video frame k.
Figure 4 shows the feature maps of two frames in video chunk 37 and 98 in VideoSet [31]. As
shown in Figures 4(a) and 4(e), frame 596 has richer textures than frame 11, and shows higher spa-
tial randomness. The luminance of the pixels in Figure 4(b) is slightly darker than that in Figure 4(f).
Compared with Figures 4(g) and 4(c) contains more black pixels, indicating that the frame differ-
ence is small and the motion intensity is low. In addition, the distribution of saliency in Figure 4(d)
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 10

```text
77:10
J. Ye et al.
is more concentrated than that in Figure 4(h). As mentioned earlier, higher spatial randomness,
higher motion intensity and lower saliency will lead to lower visual sensitivity (see chunk 98 in
Figure 6).
4.2.2
Output of the Total Masking Effect Model. As a VW-JND predictor, the output of proposed
model is the prediction of the first just noticeable difference (FJND) point. FJND point is a
transition point between the best quality level (lossless perception) and the secondary quality level
(lossy perception) whose value is the smallest distortion level that can be perceived by the observer.
In a compressed video corresponding to the FJND point, HVS can’t perceive the distortion relative
to the original video (i.e., uncompressed video), so the FJND point can accurately reflect the total
masking effect of video content. Inspired by this, this paper models the total masking effect of video
content as a predictor for the FJND point, and regresses the input features into it. The FJND point is
generally represented by coding parameters (e.g., QP), bitrate, and quality metrics (e.g., PSNR [52],
SSIM [53]). Among them, QP controls the quality of video coding, bitrate represents the amount of
video data per unit time, while PSNR and SSIM are two popular objective quality metrics in picture
and video processing. Considering the effectiveness of objective quality metrics in reflecting the
degree of distortions and the insensitivity of SSIM to compression distortions, we measure the
average PSNR of video frames sampled from a given compressed video as the FJND point.
4.2.3
Training of the Total Masking Effect Model. The structural design of the proposed model
is shown in Figure 5. It is based on the advanced VGG network [54], which is inspired by the
organization of the primate visual cortex. Firstly, four independent CNN subnetworks are used
to convolute different feature maps. The spatial randomness map, the luminance map, the tempo-
ral map, and the saliency map are fed into the Subnetwork-1, Subnetwork-2, Subnetwork-3, and
Subnetwork-4, respectively to extract finer-grained features. Then the abstract features from four
subnetworks and three attribute features are concatenated together and transported into the feed-
back module, and the features processed after feedback are input to the fully connected layer to
predict the FJND point. Finally, the loss value is calculated, followed by the target prediction. The
whole process is formulated as:
PSNRk
= FB(Concat(sub1(SRMk (i, j)), sub2(LMk (i, j)), sub3(TMk (i, j)), sub4(SMk (i, j)), FRk,
REk, BRk))
(6)
where FB, Concat, subi denote the processes of the feedback, the concatenation, and the
Subnetwork-i, respectively. Because the training of deep neural network needs a large number
of samples, and the number of available JND datasets is limited, this paper adopts the patch-based
training method to manually increase the data samples. Each input feature map is divided into
multiple patches, and a certain number of patches are randomly selected and labeled as the FJND
point of the corresponding video chunk for training. In order to accommodate the size of the input
patch, the network is extended to three layers, namely conv1, conv2, and maxpool.
The training process of the proposed model mainly includes three parts: feature fusion, feed-
back looping, and spatial pooling. For feature fusion, we use a simple and commonly used concat()
function to fuse the feature vectors extracted by convolution layers in each subnetwork and the
attribute features, and then input them into the feedback module. The feedback module is designed
to handle the feedback connections and generate powerful high-level representations, which can
realize the guidance function of the high-level region of visual cortex to the low-level region. The
processed features are sent to the subsequent regression part of the network for further mapping.
We adopt the weighted-average patch aggregation strategy to aggregate local patches with differ-
ent spatial distributions and weights, the weight ω∗
p of the patch p is activated by ReLU function
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 11

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:11
Fig. 5. Design of the total masking effect model.
and is always positive. The prediction 
PSNRk of video frame k is expressed as:

PSNRk = 1
Np
·
Np
p=1 ω∗
p · 
PSNRp
Np
p=1 ω∗
p
(7)
where Np represents the total number of patches sampled in each feature map, and 
PSNRp is the
estimate of patch p. In this paper, the mean absolute error (MAE) is used as the loss function to
measure the error between the predicted 
PSNRp and the real PSNRp, expressed as:
E = 1
Np
·
Np

p=1
|
PSNRp −PSNRp|
(8)
4.2.4
Calculation of Visual Sensitivity. Based on the total masking effect model, we define vi-
sual sensitivity by analyzing the relationship between the FJND point and the sensitivity of HVS
to distortion. The frame-level prediction value is averaged to obtain the chunk-level result. The
larger the FJND point, the higher the video quality, and the lower the distortion level of the corre-
sponding video, indicating that HVS is more likely to perceive the distortion for the video, so the
total masking effect is weak. Therefore, visual sensitivity increases with the increase of the FJND
point (in the form of PSNR metric). Based on this proportional relationship, the PSNR of the video
chunk is normalized to represent the relative visual sensitivity (VS):
VSt =
PSNRt −Min(PSNRt )
Max(PSNRt ) −Min(PSNRt )
(9)
where, for video chunk t, Max(PSNRt ) and Min(PSNRt ) are the maximum and minimum PSNR of
all given video chunks, respectively. Figure 6 shows the distribution of VS for some video chunks
sampled from VideoSet [31]. It can be seen that it is distributed in different intervals for different
video chunks, and it is worth noting that the video frames in Figure 4 correspond to chunk 37 and
chunk 98 in this figure, which are distributed in the range of higher and lower visual sensitivity,
respectively.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 12

```text
77:12
J. Ye et al.
Fig. 6. The distribution of VS for sampled video chunks, which spans three different intervals.
4.3
Visual Sensitivity Aware ABR
In this section, we will introduce the design and training of the proposed visual sensitivity aware
ABR algorithm. The algorithm is based on the latest reinforcement learning (RL) algorithm A3C
[21]. Reinforcement learning originated from animal learning in psychology and is an important
branch of machine learning. It can imitate human learning ability and choose behaviors that can
maximize long-term benefits in the interaction with the environment. RL is mainly composed of
five parts: agent, environment, state, action, and reward. RL defines any decision-maker (learner)
as an agent and anything other than an agent as an environment. A3C algorithm includes the
training of two neural networks, namely actor network and critic network, which have the same
network structure and input, but different functions and outputs. Actor network is a strategic
function that makes an action according to the calculated probability distribution, while the critic
network is a value function that evaluates the action according to the current state and predicts the
possible value of the action. RL agents usually make decisions based on the environmental infor-
mation at each time step, and receive corresponding rewards to update the model. By interacting
with the environment, agents learn continuously and respond to actions with higher cumulative
rewards.
In this paper, we classify the state inputs of RL agent into four parts, which contain more
extensive information: player environment features, low visual sensitivity video chunk features,
medium visual sensitivity video chunk features, and high visual sensitivity video chunk features.
Meanwhile, we integrate the QoE model with VS to design a reward function that stimulates the
ABR policy consistent with visual sensitivity. Our algorithm aims at the following goals: when
HVS is about to become more sensitive, carefully reducing the quality of the current chunk and
ensuring that high visual sensitivity video chunk has higher video quality. Similarly, the bitrates
of current few chunks will be increased if the visual sensitivity will drop in the future.
State: The RL agent transmits the state st = (s1,s2,s3,s4) to the actor network and critic net-
work after the download of video chunk t. s1 = (⃗xt, ⃗et,bt,lt ) represents the player environment
features. Here ⃗xt and ⃗et includes the throughput and the download time of past K video chunks,
respectively. bt represents the current buffer size, and lt is the perceptual video quality of last
video chunk. s2 = (⃗qt, ⃗τt,ct ) is the low visual sensitivity video chunk features. ⃗qt contains the
perceptual video quality of each bitrate for the next low visual sensitivity chunk. ⃗τt is the vector
of the next low visual sensitivity video chunk sizes with different bitrates. ct indicates the num-
ber of remaining low visual sensitivity chunks. s3 = (⃗pt, ⃗ηt,mt ) is the medium visual sensitivity
video chunk features. ⃗pt includes the perceptual video quality of each bitrate for the next medium
visual sensitivity chunk. ⃗ηt is the vector of the next medium visual sensitivity video chunk sizes
with different bitrates. mt represents the number of remaining medium visual sensitivity chunks.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 13

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:13
s4 = ( ⃗Qt, ⃗φt,Ct ) is the high visual sensitivity video chunk features. ⃗Qt includes the perceptual
video quality of each bitrate for the next high visual sensitivity chunk. ⃗φt is the vector of the
next high visual sensitivity video chunk sizes with different bitrates. Ct describes the number of
remaining high visual sensitivity chunks.
Training: Based on the current state, actor network takes a certain policy to output an action
at, that is, the bitrate decision of the next video chunk in our algorithm. The policy is defined as
πθ (st,at ) →[0, 1], a probability of taking at at st, and θ is a parameter set of actor network. Critic
network also outputs the predicted valueV πθ (st ) based on this policy. After the actionat is applied,
the environment provides the agent with the reward of chunk t, i.e., Rewardt. The learning goal
of the RL agent is to maximize the cumulative reward, which can be described as the process of
finding the optimal policy π ∗(st,at ). In the training of our ABR algorithm, the gradient descent
method is used to update the network parameters, and we generate multiple agents (8 numbers)
in parallel to speed up the training process as suggested by [11].
Reward: The reward function is the standard to optimize the action of the RL agent. In the
problem of adaptive bitrate decision, the goal is to maximize user QoE. Therefore, the reward
function is typically defined as a specific QoE model. In this paper, we define it based on the
commonly used linear QoE model [12] and visual sensitivity, which is similar to the idea of our
previous work [34], but it worth noting that we have more accurate visual sensitivity information.
The reward function is expressed as:
Rewardt = αV St
Nv

t=1
VMAF (Rt ) −β
Nv

t=1
Ht
+ γ
Nv −1

t=1
[VMAF (Rt+1) −VMAF (Rt )]+
−δ
Nv −1

t=1
[VMAF (Rt+1) −VMAF (Rt )]−
(10)
where Nv represents the number of chunks contained in a video session. Rt represents the bitrate
level of chunk t.VMAF (Rt ) map the Rt to a VMAF score. Ht represents the rebuffering time down-
loaded at bitrate Rt, which promotes the fluent video playback. [VMAF (Rt+1) −VMAF (Rt )]+ and
[VMAF (Rt+1)−VMAF (Rt )]−represents the positive and negative quality smoothness, respectively.
αV St , β, γ and δ are the aggressive parameters of perceptual video quality, video rebuffering time,
and positive/negative quality smoothness. In particular, the first term of Rewardt is defined as a
bitrate utility function related to visual sensitivity:
BU (Rt,VSt ) = αV St · VMAF (Rt )
(11)
αV St = VSt · μ + ξ
(12)
where VSt in Equation (9) is mapped to the positive weight of the perceptual video quality
VMAF (Rt ) in the range of [ξ, μ + ξ], i.e., αV St . By assigning higher weight to the video chunk
with higher VS, transmitting it with higher quality can produce greater bitrate utility value, so as
to obtain more reward, which covers the optimization goal of our ABR algorithm.
5
EXPERIMENT AND EVALUATION
The evaluation in this section consists of two parts. Firstly, we compare the performance of pro-
posed total masking effect model and existing VW-JND prediction methods. The accuracy of the
model is evaluated by comparing the real data label with the model output. Secondly, we present
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 14

```text
77:14
J. Ye et al.
Table 1. Notation and Definition
Notation
Definition
SRMk (i, j)
The spatial randomness map of video frame k
LMk (i, j)
The luminance map of video frame k
TMk (i, j)
The temporal map of video frame k
SMk (i, j)
The saliency map of video frame k
FRk
The framerate of video chunk to which video frame k belongs
REk
The resolution of video chunk to which video frame k belongs
BRk
The bitrate of video chunk to which video frame k belongs
Fk
The feature set of video frame k

PSNRk
The PSNR prediction value of video frame k
PSNRt
The PSNR value of video chunk t
VSt
The visual sensitivity value of video chunk t
st
The environment status for RL agent after the download of video chunk t
at
The action of RL agent for given state st
Rewardt
The reward of video chunk t
K
The horizon of future video chunks
Rt
The selected bitrate for video chunk t
αV St
The weight of the reward for video quality
β
The weight of the penalty for rebuffering time
γ
The weight of the reward for positive quality smoothness
δ
The weight of the penalty for negative quality smoothness
BU (Rt,VSt )
The bitrate utility of Rt and VSt
μ
The weight of parameter αV St
ξ
The offset of parameter αV St
intensive evaluations on proposed ABR algorithm and several latest works in simulated and real
environments. Table 1 summarizes the key notations used in this paper.
5.1
Evaluation of Total Masking Effect Model
5.1.1
Experimental Dataset and Setting. We adopt the largest-scale and most widely used
VideoSet [31] dataset to train and test the evaluated model. The dataset is a JND based video
quality dataset under the H.264/AVC compression standard, including 220 original videos with
resolutions of 640×360 (360p), 960×540 (540p), 1280×720 (720p), and 1920×1080 (1080p). For each
original video, 51 distorted videos are generated using different QP encodings. This experiment
uses the original videos of each resolution and calculated FJND points as the samples, which are
randomly divided into three subsets: the training set, verification set, and test set, accounting
for 60%, 20%, and 20%, respectively. As mentioned earlier, the random patch selection strategy
is adopted for data expansion, and we have more than 500,000 available data samples for model
training and testing.
The experimental environment of this paper is: the server with NVIDIA GeForce RTX 2080ti,
16GB memory and Windows system; Pycharm software with Python 3.6.8 and Pytorch 1.4.0. The
training details of the proposed model are as follows: the whole training includes about 3,000
iterations, and each iteration is defined as a time period in which each sample in the training set
is used once. In each iteration, the training set is divided into small batches for batch optimization.
Each batch contains four input pictures, and each picture is represented by 32 patches, which
are sampled only once at the beginning. Therefore, the size of batch training is 128 patches. The
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 15

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:15
Table 2. Evaluation of Six Methods
Method
MAE
VAR
360p
540p
720p
1080p
360p
540p
720p
1080p
GJND
2.23
2.08
1.97
1.88
2.76
1.98
1.62
1.57
SUR-FJND
1.94
1.89
1.72
1.64
1.63
1.59
1.56
1.48
GPR-SUR
1.47
1.38
1.31
1.26
1.51
1.42
1.38
1.33
Content features + CNN
1.18
1.21
1.05
0.98
1.30
1.28
1.13
1.04
Content and attribute features + CNN
0.95
0.82
0.78
0.81
0.93
0.87
0.82
0.79
Work of this paper
0.87
0.76
0.69
0.65
0.89
0.78
0.66
0.65
back-propagation error is the average error of the patches in each batch. In this experiment,
Adam [55] is used as the optimization method of gradient descent, and the learning rate of batch
optimization is adaptively controlled. As recommended in [55], the learning rate is initialized
to 1e-4 and decreases linearly with the increase of the number of iterations. We also apply the
dropout regularization with a ratio of 0.5 to the full connection layer to prevent over-fitting.
In addition to the three existing baseline prediction methods GJND [27], SUR-FJND [32], and
GPR-SUR [33], this paper also compares the prediction method of only combining video content
features with multi-stream CNN network, and the prediction method of combining video content
features, video attribute features with multi-stream CNN network. GJND predicts the average
of group-based FJND point by SVR. In our experiment, the feature extraction, feature fusion and
SVR regression of the data samples from VideoSet [31] are exactly the same as the framework of
GJND. SUR-FJND also uses SVR to predict multiple SUR curves and derives the FJND point from
the predicted SUR curves, while GPR-SUR uses GPR to model the SUR curves and predicts the
bitrate under a given SUR value as the FJND point. For comparison, we calculate the PSNR under
a given SUR value.
5.1.2
Evaluation Results. This paper uses two commonly used metrics to evaluate the prediction
accuracy, namely MAE and its variance (VAR). For a full evaluation, we use the 5-fold cross
validation method, and the results are shown in Table 2. GJND has the largest prediction error in
the two metrics due to the inaccuracy of the manual-fused features. Although GPR-SUR achieves
relatively better performance, the method of combining video content features with multi-stream
CNN network can decrease the MAE and VAR by at least 12.32% and 9.85% respectively, which
benefits from the effectiveness of the considered features and model structure. More importantly,
the model incorporating video attribute features and HVS feedback module has a better prediction
accuracy and reduces the prediction error to less than 0.9. What’s more, the average MAE and
VAR of four resolutions are 0.74 and 0.75, which further proves the robustness and effectiveness
of proposed model in simulating the HVS perception mechanism.
An ablation study is carried out in this paper to further analyze the effectiveness of four feature
maps. For video frame k, we define three feature subsets with randomly selected feature maps of 1,
2 and 3 numbers. We take three feature subsets and the feature set containing all feature maps as
the inputs of the proposed model for testing. The settings of three feature subsets are: (1) only SRM;
(2) Containing SRM and LM; and (3) Containing SRM, LM, and TM. As shown in Figure 7, compared
with Figures 7(a), (b) and (c), most points in Figure 7(d) are more concentrated near the line of y =
x, indicating that the combination of four features can achieve the minimum prediction error.
5.2
Evaluation of ABR Algorithm
5.2.1
Simulation Experiment. In this paper, we implement and evaluate the proposed visual
sensitivity aware ABR (i.e., VS-ABR) based on Python 3.6.8, Tensorflow 1.5, and the chunk-level
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 16

```text
77:16
J. Ye et al.
Fig. 7. Results of ablation study, for each video frame in the sample, different number of feature maps
are randomly selected as the input of the total masking effect model( {SRM}, {SRM,LM}, {SRM,LM,TM},
{SRM,LM,TM,SM} ), it is shown that the combination of four feature maps can achieve the minimum pre-
diction error.
Table 3. Bitrate of Three ABR Algorithms on 3G/HSDPA
Algorithm
Average Bitrate for
Low VS
Average Bitrate for
Medium VS
Average Bitrate for
High VS
Average
Bitrate
Standard Deviation
of Bitrate
RobustMPC
938.71 kbps
920.35 kbps
904.36 kbps
924.76 kbps
18.37
Pensieve
960.64 kbps
937.52 kbps
958.57 kbps
943.47 kbps
15.96
VS-ABR
885.32 kbps
980.86 kbps
1117.56 kbps
958.24 kbps
20.25
simulator provided by [11]. We adopt two kinds of real network traces, 3G/HSDPA mobile dataset
[49] and FCC bandwidth dataset [56]. The 3G/HSDPA dataset includes 30 minute throughput mea-
surements generated by mobile devices that transmit video in different traffic environments (e.g.,
buses, trains). The FCC dataset contains more than 1 million throughput traces, each recording the
average throughput of more than 2,100 seconds at a granularity of 5 seconds. The video traces in-
cludes the “EnvivioDash3” [45], and seven videos consisting of 8-18 video sequences from VideoSet
[31]. This experiment tests all eight videos, and compares the VS-ABR with RobustMPC [7] and
Pensieve [11]. For each video session, 80% of the random network traces are selected as the training
set of VS-ABR and Pensieve, and the remaining 20% are in the test set. The QoE model proposed
by Huang et al. [12] is used for evaluation, which has been proved to be superior to recent works.
Comparison on real network traces: We first divide the VS of all video chunks into three
levels: [0.6, 1.5) for “Low VS”, [1.5, 2.0) for “Medium VS”, and [2.0, 2.6] for “High VS”, where the
parameters μ and ξ in Equation (12) are set to 2 and 0.6, respectively. Table 3 shows the average
bitrates of different ABR algorithms at three VS levels on 3G/HSDPA dataset. We can observe that
due to the equal treatment of each video chunk, the average bitrates between video chunks with
different VS are close in RobustMPC and Pensieve, while VS-ABR transmits the high sensitivity
video chunks at higher bitrates, so it has a larger bitrate standard deviation. Similar results are
also shown on the FCC dataset.
Figure 8 shows the distribution of the VMAF, rebuffering time, quality smoothness, and overall
QoE of three ABR algorithms in each video session. As shown in Figure 8(a), all video sessions
show that the VMAF of VS-ABR is distributed in a more compact and higher range, with an average
VMAF improvement of 2.08%-18.34%. Since the rebuffering time of most video chunks can still be
maintained at 0 seconds, Figure 8(b) only describes the distribution of non-zero video rebuffering
time. Due to the preference of VS-ABR for transmitting high sensitivity video chunks at higher
bitrates, its rebuffering time will increase in some cases, such as in video session 4 and video session
7. But the average difference between three algorithms is less than 0.5 seconds, which indicates that
the performance of other metrics can be improved without causing larger rebuffering time. Since
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 17

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:17
Fig. 8. QoE components of three ABR algorithms in each video session.
Fig. 9. Comparison of three ABR algorithms on synthetic traces.
the VMAF is encouraged to fluctuate in a smoother range, the proposed algorithm can effectively
reduce the quality smoothness. Finally, the overall average QoE of VS-ABR has an increase of 2.44%-
22.82%. To sum up, it can be summarized that our ABR algorithm achieves a good tradeoff between
minimizing the rebuffering time, video quality smoothness and maximizing the perceptual video
quality, so as to effectively improve user QoE.
Comparison on synthetic network traces: We synthesize three groups of network traces rep-
resenting different network conditions to fully evaluate the performance of each algorithm. Specifi-
cally, it varies in the range of 0-2 Mbps for “Low Throughput”, 0-4 Mbps for “Medium Throughput”,
and 0-9 Mbps for “High Throughput”. Figure 9 shows the average normalized QoE of different ABR
algorithms. As shown in Figure 9(a), VS-ABR can achieve the QoE improvement at a minimum of
17.65% and 14.94% under the low and medium throughput. Besides, we find that under the high
throughput, the bitrates are usually maintained at a higher level, and further improving it leads
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 18

```text
77:18
J. Ye et al.
Fig. 10. Comparison of three VS prediction methods and ABR algorithms.
to a small increase of perceptual video quality while lowering it will easily produce a poor quality.
To further improve the performance of VS-ABR under the high throughput, we carefully reduce
the parameter μ in Equation (12) to 1, so the degree of differential bitrate allocation is weakened.
The experimental results demonstrate that VS-ABR in Figure 9(b) can effectively achieve a higher
QoE improvement than Figure 9(a) under the high throughput.
Comparison for different VS prediction methods: We introduce the prediction results of
SUR-FJND [32] and GPR-SUR [33] on FJND points into the ABR algorithm for comparison (in the
same way as VS-ABR). Figure 10(a) shows the prediction results of three methods. The predicted
PSNR is normalized to the VS, and the proposed method is closest to the real value. Figure 10(b)
compares the VMAF of different ABR algorithms under the same network trace. It can be observed
that VS-ABR has the same or higher VMAF as other algorithms in most cases, with an average
VMAF improvement of at least 2.93%. For video chunk 3, 5, 15 (high visual sensitivity) and video
chunk 7, 13, 22 (medium visual sensitivity), VMAF decreases to a certain extent due to the pre-
diction error of SUR-FJND or GPR-SUR. Therefore, a more accurate visual sensitivity prediction
method is helpful to guide the ABR algorithm to achieve higher perceptual video quality.
5.2.2
Real Experiment. We implement the above ABR algorithms based on dash.js [57]. The
client player adopts a Google Chrome browser, and the video server is Apache version 2.4.7, which
runs on the same machine (on a PC) as the client with Ubuntu 12.04. The interaction between the
client player and the server is achieved using XMLHttpRequests, such as sending the request with
playback state, and receiving the response with bitrate decision. The DASH player is configured
to have a buffer capacity of 60 seconds. The network traces and video traces used for evaluation
are similar to those in 5.2.1, we use Mahimahi [58] to emulate different network conditions, and
divide the video traces into four video types: covering cartoon, sports, nature, and indoor scene.
We invite 16 subjects for subjective evaluation, all the subjects are students with normal or
corrected-to-normal vision in our university. Half of the volunteers are male and half are female.
They are absolutely ignorant of streaming adaptation technology, but are briefly informed about
the purpose and rules of our experiment. The duration for all test videos is 30-50 seconds. We
adopt the paired comparison method based on [18]. Each subject is requested to watch a video
two times under a pair of different ABR algorithms, and vote on the video they think is better. It
will not be counted in the vote if the volunteer is indifferent to the two videos.
We compare the proposed VS-ABR with the other three algorithms (RobustMPC, Pensieve, GPR-
SUR-ABR), the results are shown in Table 4. The total number of votes for each video type in
each group may be less than 16. VS-ABR receives more votes than RobustMPC and Pensieve by
considering the viewer’s visual sensitivity to improve subjective viewing experiences, and is more
effective for cartoon and sports (the temporal masking effect is stronger). Among the three groups
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 19

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:19
Table 4. The Number of Votes for VS-ABR and Other Three Algorithms
Video Type
Group of Algorithms
1
2
3
Pensieve
VS-ABR
RobustMPC
VS-ABR
GPR-SUR-ABR
VS-ABR
Cartoon
3
12
2
11
4
8
Sports
2
11
1
13
4
9
Nature
3
11
2
10
5
8
Indoor Scene
4
10
4
11
6
7
of comparisons, more volunteers are indifferent to the comparison between VS-ABR and GPR-
SUR-ABR, because they both adopt the visual sensitivity aware mechanism for bitrate adaptation.
However, VS-ABR still gets a few more votes due to more precise prediction information. Affected
by the understanding of the video content and the judgment on the video quality, users may be
indifferent to the viewing experience. In most cases, our algorithm shows better performance than
the baseline algorithms.
5.3
System Overhead
We measure the overhead of training the total masking effect model and using RL to generate ABR
algorithms. For the training of the total masking effect model, we adopt the GPU parallel mode,
and the total training takes about 5 hours offline. Using the proposed method to train an ABR
algorithm takes 310 ms for each iteration and corresponds to eight agents updating parameters
asynchronously. Compared with Pensieve [11], the runtime overhead of proposed algorithm is
less than 1% in terms of CPU cycles and RAM usage. To sum up, the algorithm proposed in this
paper adopts the offline training strategy and online server deployment to make bitrate decisions
without large-scale modifications of the existing architecture.
6
CONCLUSION
This paper mainly focuses on the visual sensitivity aware ABR algorithm. Aiming at the shortcom-
ings of existing ABR algorithms in bitrate allocation and resource utilization, the ABR algorithm
is optimized from the inherent limitations of HVS. This paper summarizes the shortcomings of
existing visual sensitivity models in simulating HVS characteristics, and proposes a total masking
effect model for video content. The model combines multi-stream feedforward neural network and
feedback network, which can extract, process and fit multiple video features in a finer granular-
ity, and achieve more accurate visual sensitivity prediction. On the basis of this model, this paper
applies the visual sensitivity information to the ABR algorithm based on reinforcement learning,
and proposes the visual sensitivity aware ABR algorithm. The algorithm can make bitrate deci-
sions based on visual sensitivity, further improve the utilization of bitrate resources, and provide
better QoE without introducing additional resource overhead.
In future work, we hope to define a more accurate visual sensitivity model by combining more ex-
tensive features and more HVS inherent mechanisms. In addition, with the development of scalable
video coding technology, we will also consider a more fine-grained adaptive strategy to provide
more precise quality decisions for video content, so as to further optimize the user QoE.
REFERENCES
[1] Cisco. 2017. Cisco visual networking index: Forecast and methodology, 2016–2021.
[2] T. Stockhammer. 2011. Dynamic adaptive streaming over HTTP–standards and design principles. In Proceedings of
the Second Annual ACM Conference on Multimedia Systems (MMSys’11). San Jose, CA, USA, 133–144.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 20

```text
77:20
J. Ye et al.
[3] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, et al. 2016. CS2P: Improving video bitrate selection and adaptation with
data-driven throughput prediction. In Proceedings of the 2016 ACM SIGCOMM Conference (SIGCOMM’16). Association
for Computing Machinery, New York, NY, USA, 272–285.
[4] J. Jiang, V. Sekar, and H. Zhang. 2014. Improving fairness, efficiency, and stability in HTTP-based adaptive video
streaming with Festive. IEEE/ACM Transactions on Networking 22, 1 (2014), 326–340.
[5] T. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson. 2014. A buffer-based approach to rate adaptation:
Evidence from a large video streaming service. In Proceedings of the 2014 ACM Conference on SIGCOMM (SIGCOMM’14).
Association for Computing Machinery, New York, NY, USA, 187–198.
[6] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman. 2016. BOLA: Near-optimal bitrate adaptation for online videos. The 35th
Annual IEEE International Conference on Computer Communications (INFOCOM’16). San Francisco, CA, USA, 1–9.
[7] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A control-theoretic approach for dynamic adaptive
video streaming over HTTP. In Proceedings of the 2015 ACM Conference on Special Interest Group on Data Communi-
cation (SIGCOMM’15). Association for Computing Machinery, New York, NY, USA, 325–338.
[8] A. Bokani, M. Hassan, S. Kanhere, and X. Zhu. 2015. Optimizing HTTP-based adaptive streaming in vehicular envi-
ronment using Markov decision process. IEEE Transactions on Multimedia 17, 12 (2015), 2297–2309.
[9] C. Zhou, C.-W. Lin, and Z. Guo. 2016. mDASH: A Markov decision-based rate adaptation approach for dynamic HTTP
streaming. IEEE Transactions on Multimedia 18, 4 (2016), 738–751.
[10] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella. 2017. D-DASH: A deep Q-Learning framework for DASH video
streaming. IEEE Transactions on Cognitive Communications and Networking 3, 4 (2017), 703–718.
[11] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural adaptive video streaming with Pensieve. In
Proceedings of the Conference of the ACM Special Interest Group on Data Communication (SIGCOMM’17). Association
for Computing Machinery, New York, NY, USA, 197–210.
[12] T. Huang, C. Zhou, R. Zhang, C. Wu, X. Yao, and L. Sun. 2019. Comyco: Quality-aware adaptive video streaming via
imitation learning. In Proceedings of the 27th ACM International Conference on Multimedia (MM’19). Association for
Computing Machinery, New York, NY, USA, 429–437.
[13] T. Huang, X. Yao, C. Wu, et al. 2019. Tiyuntsong: A self-play reinforcement learning approach for ABR video streaming.
2019 IEEE International Conference on Multimedia and Expo (ICME). Shanghai, China, 1678–1683.
[14] S. Hu, L. Sun, C. Gui, E. Jammeh, and I. Mkwawa. 2014. Content-aware adaptation scheme for QoE optimized DASH
applications. 2014 IEEE Global Communications Conference. Austin, TX, 1336–1341.
[15] Stefan Wilk, Denny Stohr, and Wolfgang Effelsberg. 2016. A content-aware video adaptation service to support mobile
video. ACM Trans. Multimedia Comput. Commun. Appl 12, 5, Article 82 (November 2016), 1–23.
[16] B. Ciubotaru, G. Ghinea, and G. Muntean. 2014. Subjective assessment of region of interest-aware adaptive multimedia
streaming quality. IEEE Transactions on Broadcasting 60, 1 (March 2014), 50–60.
[17] Maarten Wijnants, Sven Coppers, Gustavo Rovelo Ruiz, Peter Quax, and Wim Lamotte. 2019. Talking video heads:
Saving streaming bitrate by adaptively applying object-based video principles to interview-like footage. In Proceedings
of the 27th ACM International Conference on Multimedia (MM’19). Association for Computing Machinery, New York,
NY, USA, 2449–2458.
[18] G. Gao et al. 2018. Optimizing quality of experience for adaptive bitrate streaming via viewer interest inference. IEEE
Transactions on Multimedia 20, 12 (Dec. 2018), 3399–3413.
[19] Shenghong Hu, Lingfen Sun, Chunxia Xiao, and Chao Gui. 2017. Semantic-aware adaptation scheme for soccer video
over MPEG-DASH. In Proceedings of the IEEE International Conference on Multimedia & Expo (ICME’17). Hong Kong,
China, 493–498.
[20] Shenghong Hu, Min Xu, Haimin Zhang, Chunxia Xiao, and Chao Gui. 2020. Affective content-aware adaptation
scheme on QoE optimization of adaptive streaming over HTTP. ACM Trans. Multimedia Comput. Commun. Appl
15, 3, Article 100 (January 2020), 1–18.
[21] H. V. Mnih et al. 2016. Asynchronous methods for deep reinforcement learning. In Proceedings of the 33rd International
Conference on Machine Learning (ICML’16). New York, NY, USA, 1928–1937.
[22] A. B. Watson, R. Borthwick, and M. Taylor. 1997. Image quality and entropy masking. Electronic Imaging’97. Interna-
tional Society for Optics and Photonics, 2–12.
[23] P. Gao, P. Zhang, and A. Smolic. 2022. Quality assessment for omnidirectional video: A spatio-temporal distortion
modeling approach. IEEE Transactions on Multimedia, 24, 1–16.
[24] L. K. Choi and A. C. Bovik. 2018. Video quality assessment accounting for temporal visual masking of local flicker.
Signal Processing Image Communication 67 (Sep. 2018), 182–198.
[25] H. Roodaki, Z. Iravani, M. R. Hashemi, and S. Shirmohammadi. 2016. A view-level rate distortion model for multi-
view/3D video. IEEE Transactions on Multimedia 18, 1 (Jan. 2016), 14–24.
[26] H. Liu et al. 2020. Deep learning-based picture-wise just noticeable distortion prediction model for image compression.
IEEE Transactions on Image Processing, 29, 641–656.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 21

```text
A Visual Sensitivity Aware ABR Algorithm for DASH via Deep Reinforcement Learning
77:21
[27] Q. Huang, H. Wang, S. C. Lim, H. Y. Kim, S. Y. Jeong, and C.-C.-J. Kuo. 2017. Measure and prediction of HEVC per-
ceptually lossy/lossless boundary QP values. In 2017 Data Compression Conference (DCC’17). Snowbird, UT, USA,
42–51.
[28] L. Jin, J. Lin, S. Hu, et al. 2016. Statistical study on perceived JPEG image quality via MCL-JCI dataset construction
and analysis. IS&T/SPIE Electronic Imaging, International Society for Optics and Photonics, 13, 1–9.
[29] X. Shen, Z. Ni, W. Yang, X. Zhang, S. Wang, and S. Kwong. 2020. A JND dataset based on VVC compressed images. In
IEEE International Conference on Multimedia & Expo Workshops (ICMEW’20). London, UK, 1–6.
[30] H. Wang et al. 2016. MCL-JCV: A JND-based H.264/AVC video quality assessment dataset. In 2016 IEEE International
Conference on Image Processing (ICIP’16). Phoenix, AZ, USA, 1509–1513.
[31] H. Wang et al. 2017. VideoSet: A large-scale compressed video quality dataset based on JND measurement. J. Vis.
Commun. Image Represent 46 (Jul. 2017), 292–302.
[32] H. Wang, I. Katsavounidis, Q. Huang, X. Zhou, and C.-C. J. Kuo. 2018. Prediction of satisfied user ratio for com-
pressed video. In 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP’18). Calgary,
AB, Canada, 6747–6751.
[33] X. Zhang, C. Yang, H. Wang, W. Xu, and C. -C. J. Kuo. 2020. Satisfied-user-ratio modeling for compressed video. IEEE
Transactions on Image Processing, 29, 3777–3789.
[34] Meng Dan, Jin Ye, Wenchao Jiang, and Yuanchao Shan. 2021. Visual sensitivity aware rate adaptation for video stream-
ing via deep reinforcement learning. In 23rd IEEE International Conference on High Performance Computing and Com-
munications (HPCC’21). To appear.
[35] W. Zhou, Y. Zhu, J. Lei, J. Wan, and L. Yu. 2022. CCAFNet: Crossflow and cross-scale adaptive fusion network for
detecting salient objects in RGB-D images. IEEE Transactions on Multimedia, 24, 2192–2204.
[36] Kai Lin, Chuanmin Jia, Xinfeng Zhang, Shanshe Wang, Siwei Ma, and Wen Gao. 2022. NR-CNN: Nested-residual
guided CNN In-loop filtering for video coding. ACM Trans. Multimedia Comput. Commun. Appl 18, 4 (2022), 1–22.
[37] D. Zhang, L. Yao, K. Chen, S. Wang, X. Chang, and Y. Liu. 2020. Making sense of spatio-temporal preserving represen-
tations for EEG-based human intention recognition. IEEE Transactions on Cybernetics 50, 7 (2020), 3033–3044.
[38] M. Luo, X. Chang, L. Nie, Y. Yang, A. G. Hauptmann, and Q. Zheng. 2018. An adaptive semisupervised feature analysis
for video semantic recognition. IEEE Transactions on Cybernetics 48, 2 (2018), 648–660.
[39] K. Chen, L. Yao, D. Zhang, X. Wang, X. Chang, and F. Nie. 2020. A semisupervised recurrent convolutional atten-
tion model for human activity recognition. IEEE Transactions on Neural Networks and Learning Systems 31, 5 (2020),
1747–1756.
[40] W. Kim, A.-D. Nguyen, S. Lee, and A. C. Bovik. 2020. Dynamic receptive field generation for full-reference image
quality assessment. IEEE Transactions on Image Processing, 29, 4219–4231.
[41] J. Kim and S. Lee. 2017. Deep learning of human visual sensitivity in image quality assessment framework. 2017 IEEE
Conference on Computer Vision and Pattern Recognition (CVPR). Honolulu, HI, USA, 1676–1684.
[42] N. Kruger et al. 2013. Deep hierarchies in the primate visual cortex: What can we learn for computer vision? IEEE
Transactions on Pattern Analysis and Machine Intelligence 35, 8 (Aug. 2013), 1847–1871.
[43] T. S. Lee and D. Mumford. 2003. Hierarchical Bayesian inference in the visual cortex. JOSA A 20, 7, 1434–1448.
[44] R. M. Cichy, D. Pantazis, and A. Oliva. 2014. Resolving human object recognition in space and time. Nature Publishing
Group 17, 3 (Jan. 2014), 455–462.
[45] DASH Industry Form. 2016. Reference Client 2.4.0. Retrieved 2016 from http://mediapm.edgesuite.net/dash/public/
nightly/samples/dash-if-reference-player/index.html.
[46] X. Liu, X. Tao, M. Xu, Y. Zhan, and J. Lu. 2020. An EEG-based study on perception of video distortion under various
content motion conditions. IEEE Transactions on Multimedia 22, 4 (April 2020), 949–960.
[47] Netflix. 2018. VMAF - Video Multi-Method Assessment Fusion. Retrieved December, 2018 from https://github.com/
Netflix/vmaf.
[48] Nabajeet Barman, Steven Schmidt, Saman Zadtootaghaj, Maria G. Martini, and Sebastian Möller. 2018. An evalua-
tion of video quality assessment metrics for passive gaming video streaming. In Proceedings of the 23rd Packet Video
Workshop (PV’18). Amsterdam, the Netherlands, 7–12.
[49] H. Riiser et al. 2013. Commute path bandwidth traces from 3G networks: Analysis and applications. In Proceedings of
the 4th ACM Multimedia Systems Conference (MMSys’13). Association for Computing Machinery, New York, NY, USA,
114–118.
[50] Y.-F. Ou, Y. Xue, and Y. Wang. 2014. Q-star: A perceptual video quality model considering impact of spatial, temporal,
and amplitude resolutions. IEEE Transactions on Image Processing 23, 6, 2473–2486.
[51] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk. 2009. Frequency-tuned salient region detection. 2009 IEEE Con-
ference on Computer Vision and Pattern Recognition. Miami, FL, USA, 1597–1604.
[52] Chun Hsien Chou and Yun Chin Li. 1995. A perceptually tuned subband image coder based on the measure of just-
noticeable-distortion profile. IEEE Transactions on Circuits and Systems for Video Technology 5, 6, 467–476.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```

### Página 22

```text
77:22
J. Ye et al.
[53] Zhou Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli. 2004. Image quality assessment: From error visibility to
structural similarity. IEEE Transactions on Image Processing 13, 4 (April 2004), 600–612.
[54] J. Long, E. Shelhamer, and T. Darrell. 2015. Fully convolutional networks for semantic segmentation. In Proceedings
of IEEE Conference on Computer Vision and Pattern Recognition (CVPR’15). Boston, MA, USA, 3431–3440.
[55] D. P. Kingma and J. Ba. 2014. Adam: A method for stochastic optimization. Retrieved 2014 from https://arxiv.org/abs/
1412.6980.
[56] Federal Communications Commission. 2016. Raw Data - Measuring Broadband America. Retrieved 2016 from
https://www.fcc.gov/reportsresearch/reports/.
[57] Akamai. 2016. dash.js. Retrieved 2016 from https://github.com/Dash-Industry-Forum/dash.js/.
[58] R. Netravali et al. 2015. Mahimahi: Accurate record-and-replay for HTTP. In Proceedings of USENIX ATC.
Received 16 April 2022; revised 28 December 2022; accepted 26 March 2023
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 20, No. 3, Article 77. Publication date: November 2023.
```
