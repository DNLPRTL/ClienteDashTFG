# KAKEN 20K14740 - Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks

## 0. Identificacion del archivo

- Archivo fuente: `kaken.nii.ac.jp_20K14740seika.pdf`
- Paginas detectadas: `10`
- SHA256 PDF: `308da4391d26a6476c097a23cb49767d4ae88ef375d9fc8deaaaae0e70a01763`
- Texto crudo auxiliar PyMuPDF: `raw_text/20_kaken_20k14740_fair_high_qoe_multiuser_abr_report.txt`
- Texto crudo auxiliar pdftotext -layout: `raw_text_layout/20_kaken_20k14740_fair_high_qoe_multiuser_abr_report_layout.txt`

## 1. Uso previsto para Fase 4-5 v1

Informe de resultados de investigacion sobre ABR, QoE alta, fairness y redes multiusuario. Relevante como contexto amplio de fairness/estabilidad y control adaptativo, aunque no necesariamente sea fuente directa de implementacion del controller actual.

## 2. Advertencia de fidelidad

Este archivo NO es un resumen breve. Es una extraccion tecnica densa para que Codex pueda leer el paper sin depender de conversiones Markdown corruptas. El PDF original sigue siendo la fuente de verdad para formulas, tablas, figuras, simbolos y resultados exactos. Cuando una formula, tabla o figura sea decisiva, se debe verificar contra el PDF original.

## 3. Identificacion textual extraida de las primeras paginas

```text
早稲田大学・理工学術院・次席研究員
科学研究費助成事業　　研究成果報告書
様　式　Ｃ－１９、Ｆ－１９－１、Ｚ－１９ （共通）
機関番号：
研究種目：
課題番号：
研究課題名（和文）
研究代表者
研究課題名（英文）
交付決定額（研究期間全体）：（直接経費）
３２６８９
若手研究
2021
～
2020
Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming
in multi-user networks
Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming
in multi-user networks
００８４４４３２
研究者番号：
魏　博（Wei, Bo）
研究期間：
２０Ｋ１４７４０
年
月
日現在
４
６
１６
円
1,900,000
研究成果の概要（和文）：本研究は、マルチユーザーネットワークにおいて、高品質で公平な映像配信サービス
を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、
リソース割り当てなどのユーザー間要因を考慮した適応映像制御技術を提案した。緩和スキーム方法を提案し、
公平かつ安定した効率的な映像配信を実現した。一方、ライブ映像配信において、強化学習法を活用し、高品質
な配信を実現できる制御方法を提案した。また、アニーリングベースのパイロット割り当て方法を提案し、パイ
ロット割り当ての最適化とパイロット汚染の軽減を実現した。本研究の成果は、査読付きの国際学会と学術誌で
発表した。
研究成果の概要（英文）：This research focused on developing the adaptive bitrate (ABR) technology to
provide high quality and fair video streaming service in multi-user network. To this end, we have
designed ABR methods considering the inter-user factors such as fairness, resource allocation to
realize equal quality of experience (QoE) in multi-user networks. Through this research, we have
proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and
efficient video streaming. Meanwhile, DASH live video streaming control model was developed using
reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot
allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination.
The achievements of this research have been published in peer-reviewed flagship international
conferences and top journals.
研究分野：通信・ネットワーク工学
キーワード：Adaptive bitrate control　Video streaming　Multi-user network　QoE　Machine learning
１版
令和
研究成果の学術的意義や社会的意義
映像コンテンツは現在のIPトラフィックの８０％以上を占めている。また、リモートワーク、ミーティング、オ
ンライン授業などのあらゆる場面でも、映像配信がますます不可欠になっている。高品質な映像配信は、現在の
社会生活に対し、極めて重要と言える。本研究で提案している公平かつ高品質な映像配信技術は、適応映像制御
の研究分野に貢献できる。そして、動的且つ大規模なユーザーネットワークにおいて、知的な次世代超高解像度
映像伝送技術とSociety5.0の実現に資することが考えられる。
※科研費による研究は、研究者の自覚と責任において実施するものです。そのため、研究の実施や研究成果の公表等に
ついては、国の要請等に基づくものではなく、その研究成果に関する見解や責任は、研究者個人に帰属します。
様 式 Ｃ－１９、Ｆ－１９－１、Ｚ－１９（共通）
１．研究開始当初の背景
Video traffic has been the main part of the global IP traffic which account for over 80% of the total
internet traffic. It is essential to provide high-quality video streaming service to users. Among the
video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the
de facto standard which allows the video session on client side to select the video bitrate adaptively.
MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core
technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level
according to the network conditions to tradeoff between video quality and rebuffering risk. Existing
state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based
(BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future
bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such
as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy
and other information to adaptively control the bitrate. However, most of the methods are designed for
single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH
streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal
of ABR strategy is to achieve fair, stable, efficient video transmission among different users.
Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user
experience quality. Therefore, when designing the video streaming control method, there are many
factors need to be taken into consideration.
２．研究の目的
The purpose of this research is to study the adaptive video streaming for multi-user networks and
develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various
environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is
employed and new testbed framework is developed for evaluating and designing adaptation algorithms.
Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and
experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then,
novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video
streaming in various network conditions regardless of the network dynamics. Furthermore, the
characteristics of the next-generation 5G mobile network is investigated and the video streaming over
5G is carried out to analyze the low-latency feature for content delivery in various network conditions.
３．研究の方法
The method of this research was divided into multiple steps and was conducted as the details:
(1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR
methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one
unified developed testbed which is constructed in this research.
(2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video
transmission in multi-user network. The emerging advanced techniques such as reinforcement learning
(RL), Ising machine, etc. were utilized for constructing the video streaming control model.
```

## 4. Metadatos PDF detectados

```json
{
  "format": "PDF 1.7",
  "title": "20K14740 研究成果報告書",
  "author": "",
  "subject": "",
  "keywords": "",
  "creator": "",
  "producer": "",
  "creationDate": "",
  "modDate": "",
  "trapped": "",
  "encryption": "Standard V2 R3 128-bit RC4"
}
```

## 5. Mapa de secciones detectado

No se detectaron encabezados fiables automaticamente.

## 6. Figuras, tablas, algoritmos y ecuaciones detectadas

- p. 3: Fig. 2. Comparison of unfairness, inefficiency, and
- p. 3: Fig. 3. Reinforcement learning framework for ABR control. [3]
- p. 3: Table I. Comparison of QoE in two scenarios. [4]
- p. 3: Fig. 1. Framework of the testbed for multi-user
- p. 4: Fig. 4. The CDF of user’s average uplink SINR for
- p. 4: Fig. 5. MAC throughput characteristic in the
- p. 2: Fig. 1. Seven state-of-the-art
- p. 3: Fig. 2, results demonstrated that the
- p. 3: Fig. 3, in this method, the historical video
- p. 4: Fig. 4,
- p. 4: Fig. 5 shows the comparison of MAC throughput in user moving case. It

## 7. Lineas con posible contenido matematico/formal

- p. 1: `Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming`
- p. 1: `を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、`
- p. 1: `realize equal quality of experience (QoE) in multi-user networks. Through this research, we have`
- p. 1: `reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot`
- p. 1: `キーワード：Adaptive bitrate control　Video streaming　Multi-user network　QoE　Machine learning`
- p. 2: `develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various`
- p. 2: `environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is`
- p. 2: `(1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR`
- p. 2: `advantage of the proposals which could achieve high QoE and meet user requirements.`
- p. 2: `first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed`
- p. 3: `providing high and equal QoE for all users. While`
- p. 3: `demonstrate that the total QoE in Bus and Car`
- p. 3: `QoE of Tram case shows the lowest due to the`
- p. 3: `algorithms in terms of QoE, which`
- p. 3: `Table I. Comparison of QoE in two scenarios. [4]`
- p. 4: `contamination problem. The proposed method is a max k-cut-based approach, where the graph`
- p. 9: `High-QoE DASH live streaming using reinforcement learning`

## 8. Extraccion tecnica cruda por categorias


### 8.1. modelo algoritmo arquitectura

Palabras clave usadas: `model, algorithm, architecture, framework, policy, neural, network, deep reinforcement, reinforcement learning, DRL, DQN, PPO, A2C, A3C, actor, critic, agent, meta, meta-learning, MAML, offline reinforcement, curriculum, VAE, variational autoencoder, LSTM, BiLSTM, GRU, CNN, predictor, bandwidth prediction, Plume, Gelato, Ahaggar, CausalSim, IMDP, domain-specific prior`

**Fragmento 1 - p. 3 - score 5:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 2 - p. 1 - score 4:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 3 - p. 4 - score 4:**

[3] B. Wei, H. Song, Q.N. Nguyen, J. Katto, “DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method.” International Conference on Mobile Networks and Management, Springer, Cham, 2021. [4] B. Wei, H. Song, and J. Katto, “Adaptive Video Transmission Strategy Based on Ising Machine.” The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys’21), Coimbra, Portugal, November 15-17, 2021. [5] D. Maruyama, B. Wei, H. Song, and J. Katto, “Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO.” 2022 IEEE Wireless Communications and Networking Conference (WCNC), Austin, TX, USA, 10-13 April 2022. [6] K.

**Fragmento 4 - p. 6 - score 4:**

〔学会発表〕 計16件（うち招待講演 1件／うち国際学会 7件） 2022年 2022年 2021年 2021年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会） IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会） The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会） International Conference on Mobile Networks and Management（招待講演）（国際学会） ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 D. Maruyama, B. Wei, H. Song, and J. Katto B. Wei, H. Song, and J. Katto B. Wei, H. Song, Q.N. Nguyen, J. Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO Adaptive Video Transmission Strategy Based on Ising Machine DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method ４．発表年 ４．発表年 ４．発表年 K.

**Fragmento 5 - p. 2 - score 3:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 6 - p. 2 - score 3:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 7 - p. 2 - score 3:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 8 - p. 2 - score 3:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 9 - p. 9 - score 3:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 10 - p. 3 - score 2:**

(4) Ising machine-based video streaming control method [4] A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the high-quality video streaming model into the QUBO problem, which can be solved by quantum annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown in Table I, results indicated that the QUBO- ABR method outperforms existing algorithms in terms of QoE, which demonstrated the superiority and efficiency of the proposed QUBO-ABR method.

**Fragmento 11 - p. 3 - score 2:**

Fig. 2. Comparison of unfairness, inefficiency, and instability by different methods. [2] Fig. 3. Reinforcement learning framework for ABR control. [3] Table I. Comparison of QoE in two scenarios. [4] Fig. 1. Framework of the testbed for multi-user DASH video streaming. [1]

**Fragmento 12 - p. 4 - score 2:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 13 - p. 1 - score 1:**

早稲田大学・理工学術院・次席研究員 科学研究費助成事業 研究成果報告書 様 式 Ｃ－１９、Ｆ－１９－１、Ｚ－１９ （共通） 機関番号： 研究種目： 課題番号： 研究課題名（和文） 研究代表者 研究課題名（英文） 交付決定額（研究期間全体）：（直接経費） ３２６８９ 若手研究 2021 ～ 2020 Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks ００８４４４３２ 研究者番号： 魏 博（Wei, Bo） 研究期間： ２０Ｋ１４７４０ 年 月 日現在 ４ ６ １６ 円 1,900,000 研究成果の概要（和文）：本研究は、マルチユーザーネットワークにおいて、高品質で公平な映像配信サービス を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、 リソース割り当てなどのユーザー間要因を考慮した適応映像制御技術を提案した。緩和スキーム方法を提案し、 公平かつ安定した効率的な映像配信を実現した。一方、ライブ映像配信において、強化学習法を活用し、高品質 な配信を実現できる制御方法を提案した。また、アニーリングベースのパイロット割り当て方法を提案し、パイ ロット割り当ての最適化とパイロット汚染の軽減を実現した。本研究の成果は、査読付きの国際学会と学術誌で 発表した。 研究成果の概要（英文）：This research focused on developing the adaptive bitrate (ABR) technology to provide high quality and fair video streaming service in multi-user network.

**Fragmento 14 - p. 1 - score 1:**

研究分野：通信・ネットワーク工学 キーワード：Adaptive bitrate control Video streaming Multi-user network QoE Machine learning １版 令和 研究成果の学術的意義や社会的意義 映像コンテンツは現在のIPトラフィックの８０％以上を占めている。また、リモートワーク、ミーティング、オ ンライン授業などのあらゆる場面でも、映像配信がますます不可欠になっている。高品質な映像配信は、現在の 社会生活に対し、極めて重要と言える。本研究で提案している公平かつ高品質な映像配信技術は、適応映像制御 の研究分野に貢献できる。そして、動的且つ大規模なユーザーネットワークにおいて、知的な次世代超高解像度 映像伝送技術とSociety5.0の実現に資することが考えられる。 ※科研費による研究は、研究者の自覚と責任において実施するものです。そのため、研究の実施や研究成果の公表等に ついては、国の要請等に基づくものではなく、その研究成果に関する見解や責任は、研究者個人に帰属します。

**Fragmento 15 - p. 3 - score 1:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 16 - p. 3 - score 1:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 17 - p. 4 - score 1:**

(6) Investigation and evaluation of video streaming latency in 5G networks [6] Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network technologies. The performance of parameters such as the number of dropped segments, MAC throughput, and latency were evaluated in various situations such as stationary, moving in the urban area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It has been found that 5G SA can deliver more than 95% of the UHD video segment successfully within the required time window in all situations, while 5G NSA produced mixed results depending on the condition of the LTE network.

**Fragmento 18 - p. 4 - score 1:**

Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022. Fig. 4. The CDF of user’s average uplink SINR for different pilot allocation schemes. [5] Fig. 5. MAC throughput characteristic in the moving case. [6]

**Fragmento 19 - p. 7 - score 1:**

2022年 2022年 2022年 2022年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 電子情報通信学会総合大会 電子情報通信学会総合大会 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 甲藤二郎、金井謙治、孫鶴鳴、魏博、勝山裕、文鄭、中村裕一、近藤一晃、下西慶、小野浩司、根波健一、青木智資、片野淳一、吉岡修 一、作中剛、小林康雄、小沢基一、秋田純一 勝山裕、文鄭、金井謙治、孫鶴鳴、魏博、甲藤二郎 Kasidis Arunruangsirilert, Bo Wei, Jiro Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 ４．発表年 ４．発表年 ４．発表年 佐野優斗, 魏博, 宋航, 甲藤二郎 ３．学会等名 ３．学会等名 低遅延でインタラクティブなゼロレイテンシー映像・Somatic統合ネットワーク 低遅延でインタラクティブなゼロレイテンシー映像・Somatic統合ネットワーク－映像情報とSomatic情報の未来予測と統合技術 Evaluation of MPEG-DASH Response Time on Commercial 5G Network Q学習を用いた適応レート制御手法の検討

**Fragmento 20 - p. 8 - score 1:**

2021年 2021年 2021年 2021年 ２．発表標題 電子情報通信学会ソサイエティ大会 ３．学会等名 ３．学会等名 ３．学会等名 電子情報通信学会ソサイエティ大会 電子情報通信学会ソサイエティ大会 IEEE International Conference on Communications (ICC) 2021（国際学会） Bo Wei, Jiro Katto Bo Wei, Hang Song, and Jiro Katto ２．発表標題 ２．発表標題 １．発表者名 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 ４．発表年 魏博, 甲藤二郎: Throughput prediction of mmWave for 5G network FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi-user DASH Video Streaming 強化学習を用いたDASHライブ動画配信制御 4K映像配信におけるバッファ容量に基づくレート制御の性能評価 １．発表者名 佐野優斗, 魏博, 宋航, 甲藤二郎 ３．学会等名 ２．発表標題


### 8.2. estado inputs features

Palabras clave usadas: `state, input, feature, observation, throughput, bandwidth, buffer, download time, chunk size, history, past, remaining, TCP, RTT, CWND, device, resolution, content, CMCD, CMSD, network condition, environment, latent, context, trace features`

**Fragmento 1 - p. 2 - score 5:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 2 - p. 2 - score 5:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 3 - p. 3 - score 4:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 4 - p. 3 - score 3:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 5 - p. 3 - score 2:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 6 - p. 5 - score 2:**

５．主な発表論文等 〔雑誌論文〕 計4件（うち査読付論文 3件／うち国際共著 3件／うちオープンアクセス 1件） 2022年 2022年 2020年 2021年 オープンアクセスではない、又はオープンアクセスが困難 該当する 10.1109/JSEN.2021.3066785 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 Blockchain-based data collection with efficient anomaly detection for estimating battery state- of-health IEEE Sensors Journal - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセスではない、又はオープンアクセスが困難 該当する ４．巻 Ruochen Jin, Bo Wei, Yongmei Luo, Tao Ren, Ruoqian Wu - １．著者名 10.1109/JIOT.2020.2999210 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 WiEps: Measurement of Dielectric Property with Commodity WiFi Device-An Application to Ethanol/Water Mixture IEEE Internet of Things Journal 11667 - 11677 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセスとしている（また、その予定である） 該当する ４．巻 Hang Song, Bo Wei, Qun Yu, Xia Xiao, and Takamaro Kikkawa 7 １．著者名 10.3390/math10091593 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 Multimedia Applications Processing and Computation Resource Allocation in MEC-Assisted SIoT Systems with DVS Mathematics - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセス 国際共著 オープンアクセスではない、又はオープンアクセスが困難 － ４．巻 Xianwei Li, Guolong Chen, Liang Zhao, Bo Wei - １．著者名 RSSI-CSI Measurement and Variation Mitigation with Commodity WiFi Device arXiv - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 なし ３．雑誌名 ６．最初と最後の頁 無 ４．巻 Bo Wei, Hang Song, Jiro Katto, Takamaro Kikkawa - １．著者名 ２．論文標題 ５．発行年

**Fragmento 7 - p. 9 - score 2:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 8 - p. 1 - score 1:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 9 - p. 2 - score 1:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 10 - p. 2 - score 1:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 11 - p. 4 - score 1:**

(6) Investigation and evaluation of video streaming latency in 5G networks [6] Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network technologies. The performance of parameters such as the number of dropped segments, MAC throughput, and latency were evaluated in various situations such as stationary, moving in the urban area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It has been found that 5G SA can deliver more than 95% of the UHD video segment successfully within the required time window in all situations, while 5G NSA produced mixed results depending on the condition of the LTE network.

**Fragmento 12 - p. 4 - score 1:**

Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022. Fig. 4. The CDF of user’s average uplink SINR for different pilot allocation schemes. [5] Fig. 5. MAC throughput characteristic in the moving case. [6]

**Fragmento 13 - p. 8 - score 1:**

2021年 2021年 2021年 2021年 ２．発表標題 電子情報通信学会ソサイエティ大会 ３．学会等名 ３．学会等名 ３．学会等名 電子情報通信学会ソサイエティ大会 電子情報通信学会ソサイエティ大会 IEEE International Conference on Communications (ICC) 2021（国際学会） Bo Wei, Jiro Katto Bo Wei, Hang Song, and Jiro Katto ２．発表標題 ２．発表標題 １．発表者名 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 ４．発表年 魏博, 甲藤二郎: Throughput prediction of mmWave for 5G network FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi-user DASH Video Streaming 強化学習を用いたDASHライブ動画配信制御 4K映像配信におけるバッファ容量に基づくレート制御の性能評価 １．発表者名 佐野優斗, 魏博, 宋航, 甲藤二郎 ３．学会等名 ２．発表標題


### 8.3. accion decision abr

Palabras clave usadas: `action, bitrate, quality level, representation, decision, select, selection, guidance, recommendation, adaptation, cap, mask, quality, download, chunk, rate`

**Fragmento 1 - p. 2 - score 5:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 2 - p. 2 - score 4:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 3 - p. 3 - score 4:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 4 - p. 1 - score 3:**

早稲田大学・理工学術院・次席研究員 科学研究費助成事業 研究成果報告書 様 式 Ｃ－１９、Ｆ－１９－１、Ｚ－１９ （共通） 機関番号： 研究種目： 課題番号： 研究課題名（和文） 研究代表者 研究課題名（英文） 交付決定額（研究期間全体）：（直接経費） ３２６８９ 若手研究 2021 ～ 2020 Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks ００８４４４３２ 研究者番号： 魏 博（Wei, Bo） 研究期間： ２０Ｋ１４７４０ 年 月 日現在 ４ ６ １６ 円 1,900,000 研究成果の概要（和文）：本研究は、マルチユーザーネットワークにおいて、高品質で公平な映像配信サービス を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、 リソース割り当てなどのユーザー間要因を考慮した適応映像制御技術を提案した。緩和スキーム方法を提案し、 公平かつ安定した効率的な映像配信を実現した。一方、ライブ映像配信において、強化学習法を活用し、高品質 な配信を実現できる制御方法を提案した。また、アニーリングベースのパイロット割り当て方法を提案し、パイ ロット割り当ての最適化とパイロット汚染の軽減を実現した。本研究の成果は、査読付きの国際学会と学術誌で 発表した。 研究成果の概要（英文）：This research focused on developing the adaptive bitrate (ABR) technology to provide high quality and fair video streaming service in multi-user network.

**Fragmento 5 - p. 9 - score 3:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 6 - p. 1 - score 2:**

研究分野：通信・ネットワーク工学 キーワード：Adaptive bitrate control Video streaming Multi-user network QoE Machine learning １版 令和 研究成果の学術的意義や社会的意義 映像コンテンツは現在のIPトラフィックの８０％以上を占めている。また、リモートワーク、ミーティング、オ ンライン授業などのあらゆる場面でも、映像配信がますます不可欠になっている。高品質な映像配信は、現在の 社会生活に対し、極めて重要と言える。本研究で提案している公平かつ高品質な映像配信技術は、適応映像制御 の研究分野に貢献できる。そして、動的且つ大規模なユーザーネットワークにおいて、知的な次世代超高解像度 映像伝送技術とSociety5.0の実現に資することが考えられる。 ※科研費による研究は、研究者の自覚と責任において実施するものです。そのため、研究の実施や研究成果の公表等に ついては、国の要請等に基づくものではなく、その研究成果に関する見解や責任は、研究者個人に帰属します。

**Fragmento 7 - p. 2 - score 2:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 8 - p. 2 - score 2:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 9 - p. 3 - score 2:**

(4) Ising machine-based video streaming control method [4] A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the high-quality video streaming model into the QUBO problem, which can be solved by quantum annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown in Table I, results indicated that the QUBO- ABR method outperforms existing algorithms in terms of QoE, which demonstrated the superiority and efficiency of the proposed QUBO-ABR method.

**Fragmento 10 - p. 3 - score 2:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 11 - p. 3 - score 2:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 12 - p. 4 - score 2:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 13 - p. 1 - score 1:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 14 - p. 4 - score 1:**

(5) Annealing-based pilot allocation method [5] An annealing-based pilot allocation method was proposed using Ising machine for solving pilot contamination problem. The proposed method is a max k-cut-based approach, where the graph represents the potential strength of pilot contamination among users in other cells. By using this proposed method, users who have strong relationship with pilot contamination will be assigned different pilots. As shown in Fig. 4, experiment results show that the proposed method can realize optimal pilot allocation and mitigate pilot contamination. Compared with conventional methods, the proposal achieves the best performance which can increase the minimum achievable rate and show higher SINR, especially when the number of users and cells are large.

**Fragmento 15 - p. 4 - score 1:**

[3] B. Wei, H. Song, Q.N. Nguyen, J. Katto, “DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method.” International Conference on Mobile Networks and Management, Springer, Cham, 2021. [4] B. Wei, H. Song, and J. Katto, “Adaptive Video Transmission Strategy Based on Ising Machine.” The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys’21), Coimbra, Portugal, November 15-17, 2021. [5] D. Maruyama, B. Wei, H. Song, and J. Katto, “Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO.” 2022 IEEE Wireless Communications and Networking Conference (WCNC), Austin, TX, USA, 10-13 April 2022. [6] K.

**Fragmento 16 - p. 6 - score 1:**

〔学会発表〕 計16件（うち招待講演 1件／うち国際学会 7件） 2022年 2022年 2021年 2021年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会） IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会） The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会） International Conference on Mobile Networks and Management（招待講演）（国際学会） ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 D. Maruyama, B. Wei, H. Song, and J. Katto B. Wei, H. Song, and J. Katto B. Wei, H. Song, Q.N. Nguyen, J. Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO Adaptive Video Transmission Strategy Based on Ising Machine DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method ４．発表年 ４．発表年 ４．発表年 K.


### 8.4. reward qoe objetivo

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, latency, fairness, bitrate smoothness, video quality, tail, risk, severe`

**Fragmento 1 - p. 2 - score 4:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 2 - p. 2 - score 4:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 3 - p. 1 - score 3:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 4 - p. 2 - score 3:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 5 - p. 3 - score 3:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 6 - p. 3 - score 2:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 7 - p. 3 - score 2:**

Fig. 2. Comparison of unfairness, inefficiency, and instability by different methods. [2] Fig. 3. Reinforcement learning framework for ABR control. [3] Table I. Comparison of QoE in two scenarios. [4] Fig. 1. Framework of the testbed for multi-user DASH video streaming. [1]

**Fragmento 8 - p. 9 - score 2:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 9 - p. 1 - score 1:**

早稲田大学・理工学術院・次席研究員 科学研究費助成事業 研究成果報告書 様 式 Ｃ－１９、Ｆ－１９－１、Ｚ－１９ （共通） 機関番号： 研究種目： 課題番号： 研究課題名（和文） 研究代表者 研究課題名（英文） 交付決定額（研究期間全体）：（直接経費） ３２６８９ 若手研究 2021 ～ 2020 Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks ００８４４４３２ 研究者番号： 魏 博（Wei, Bo） 研究期間： ２０Ｋ１４７４０ 年 月 日現在 ４ ６ １６ 円 1,900,000 研究成果の概要（和文）：本研究は、マルチユーザーネットワークにおいて、高品質で公平な映像配信サービス を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、 リソース割り当てなどのユーザー間要因を考慮した適応映像制御技術を提案した。緩和スキーム方法を提案し、 公平かつ安定した効率的な映像配信を実現した。一方、ライブ映像配信において、強化学習法を活用し、高品質 な配信を実現できる制御方法を提案した。また、アニーリングベースのパイロット割り当て方法を提案し、パイ ロット割り当ての最適化とパイロット汚染の軽減を実現した。本研究の成果は、査読付きの国際学会と学術誌で 発表した。 研究成果の概要（英文）：This research focused on developing the adaptive bitrate (ABR) technology to provide high quality and fair video streaming service in multi-user network.

**Fragmento 10 - p. 1 - score 1:**

研究分野：通信・ネットワーク工学 キーワード：Adaptive bitrate control Video streaming Multi-user network QoE Machine learning １版 令和 研究成果の学術的意義や社会的意義 映像コンテンツは現在のIPトラフィックの８０％以上を占めている。また、リモートワーク、ミーティング、オ ンライン授業などのあらゆる場面でも、映像配信がますます不可欠になっている。高品質な映像配信は、現在の 社会生活に対し、極めて重要と言える。本研究で提案している公平かつ高品質な映像配信技術は、適応映像制御 の研究分野に貢献できる。そして、動的且つ大規模なユーザーネットワークにおいて、知的な次世代超高解像度 映像伝送技術とSociety5.0の実現に資することが考えられる。 ※科研費による研究は、研究者の自覚と責任において実施するものです。そのため、研究の実施や研究成果の公表等に ついては、国の要請等に基づくものではなく、その研究成果に関する見解や責任は、研究者個人に帰属します。

**Fragmento 11 - p. 2 - score 1:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 12 - p. 3 - score 1:**

(4) Ising machine-based video streaming control method [4] A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the high-quality video streaming model into the QUBO problem, which can be solved by quantum annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown in Table I, results indicated that the QUBO- ABR method outperforms existing algorithms in terms of QoE, which demonstrated the superiority and efficiency of the proposed QUBO-ABR method.

**Fragmento 13 - p. 3 - score 1:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 14 - p. 4 - score 1:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 15 - p. 4 - score 1:**

(6) Investigation and evaluation of video streaming latency in 5G networks [6] Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network technologies. The performance of parameters such as the number of dropped segments, MAC throughput, and latency were evaluated in various situations such as stationary, moving in the urban area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It has been found that 5G SA can deliver more than 95% of the UHD video segment successfully within the required time window in all situations, while 5G NSA produced mixed results depending on the condition of the LTE network.

**Fragmento 16 - p. 4 - score 1:**

Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022. Fig. 4. The CDF of user’s average uplink SINR for different pilot allocation schemes. [5] Fig. 5. MAC throughput characteristic in the moving case. [6]

**Fragmento 17 - p. 6 - score 1:**

〔学会発表〕 計16件（うち招待講演 1件／うち国際学会 7件） 2022年 2022年 2021年 2021年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会） IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会） The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会） International Conference on Mobile Networks and Management（招待講演）（国際学会） ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 D. Maruyama, B. Wei, H. Song, and J. Katto B. Wei, H. Song, and J. Katto B. Wei, H. Song, Q.N. Nguyen, J. Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO Adaptive Video Transmission Strategy Based on Ising Machine DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method ４．発表年 ４．発表年 ４．発表年 K.


### 8.5. entrenamiento optimizacion

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, experience replay, fine-tune, fine-tuning, pretrain, pre-training, behavior cloning, imitation, expert, simulation, simulator, offline, online, curriculum, loss function, joint optimization, dataset, sample`

**Fragmento 1 - p. 3 - score 3:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 2 - p. 3 - score 2:**

(4) Ising machine-based video streaming control method [4] A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the high-quality video streaming model into the QUBO problem, which can be solved by quantum annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown in Table I, results indicated that the QUBO- ABR method outperforms existing algorithms in terms of QoE, which demonstrated the superiority and efficiency of the proposed QUBO-ABR method.

**Fragmento 3 - p. 2 - score 1:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.


### 8.6. datos trazas datasets

Palabras clave usadas: `dataset, trace, traces, network trace, bandwidth trace, FCC, HSDPA, Norway, LTE, 4G, WiFi, Puffer, Starlink, cellular, synthetic, simulation, testbed, Mahimahi, live streaming, real-world, stream-years, users, sessions, heavy-tailed, CMCD, CMSD`

**Fragmento 1 - p. 2 - score 5:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 2 - p. 3 - score 2:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 3 - p. 3 - score 2:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 4 - p. 4 - score 2:**

(6) Investigation and evaluation of video streaming latency in 5G networks [6] Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network technologies. The performance of parameters such as the number of dropped segments, MAC throughput, and latency were evaluated in various situations such as stationary, moving in the urban area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It has been found that 5G SA can deliver more than 95% of the UHD video segment successfully within the required time window in all situations, while 5G NSA produced mixed results depending on the condition of the LTE network.

**Fragmento 5 - p. 2 - score 1:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 6 - p. 2 - score 1:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 7 - p. 2 - score 1:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 8 - p. 3 - score 1:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 9 - p. 3 - score 1:**

Fig. 2. Comparison of unfairness, inefficiency, and instability by different methods. [2] Fig. 3. Reinforcement learning framework for ABR control. [3] Table I. Comparison of QoE in two scenarios. [4] Fig. 1. Framework of the testbed for multi-user DASH video streaming. [1]

**Fragmento 10 - p. 4 - score 1:**

(5) Annealing-based pilot allocation method [5] An annealing-based pilot allocation method was proposed using Ising machine for solving pilot contamination problem. The proposed method is a max k-cut-based approach, where the graph represents the potential strength of pilot contamination among users in other cells. By using this proposed method, users who have strong relationship with pilot contamination will be assigned different pilots. As shown in Fig. 4, experiment results show that the proposed method can realize optimal pilot allocation and mitigate pilot contamination. Compared with conventional methods, the proposal achieves the best performance which can increase the minimum achievable rate and show higher SINR, especially when the number of users and cells are large.

**Fragmento 11 - p. 4 - score 1:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 12 - p. 4 - score 1:**

Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022. Fig. 4. The CDF of user’s average uplink SINR for different pilot allocation schemes. [5] Fig. 5. MAC throughput characteristic in the moving case. [6]

**Fragmento 13 - p. 5 - score 1:**

５．主な発表論文等 〔雑誌論文〕 計4件（うち査読付論文 3件／うち国際共著 3件／うちオープンアクセス 1件） 2022年 2022年 2020年 2021年 オープンアクセスではない、又はオープンアクセスが困難 該当する 10.1109/JSEN.2021.3066785 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 Blockchain-based data collection with efficient anomaly detection for estimating battery state- of-health IEEE Sensors Journal - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセスではない、又はオープンアクセスが困難 該当する ４．巻 Ruochen Jin, Bo Wei, Yongmei Luo, Tao Ren, Ruoqian Wu - １．著者名 10.1109/JIOT.2020.2999210 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 WiEps: Measurement of Dielectric Property with Commodity WiFi Device-An Application to Ethanol/Water Mixture IEEE Internet of Things Journal 11667 - 11677 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセスとしている（また、その予定である） 該当する ４．巻 Hang Song, Bo Wei, Qun Yu, Xia Xiao, and Takamaro Kikkawa 7 １．著者名 10.3390/math10091593 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 Multimedia Applications Processing and Computation Resource Allocation in MEC-Assisted SIoT Systems with DVS Mathematics - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセス 国際共著 オープンアクセスではない、又はオープンアクセスが困難 － ４．巻 Xianwei Li, Guolong Chen, Liang Zhao, Bo Wei - １．著者名 RSSI-CSI Measurement and Variation Mitigation with Commodity WiFi Device arXiv - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 なし ３．雑誌名 ６．最初と最後の頁 無 ４．巻 Bo Wei, Hang Song, Jiro Katto, Takamaro Kikkawa - １．著者名 ２．論文標題 ５．発行年

**Fragmento 14 - p. 6 - score 1:**

〔学会発表〕 計16件（うち招待講演 1件／うち国際学会 7件） 2022年 2022年 2021年 2021年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会） IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会） The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会） International Conference on Mobile Networks and Management（招待講演）（国際学会） ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 D. Maruyama, B. Wei, H. Song, and J. Katto B. Wei, H. Song, and J. Katto B. Wei, H. Song, Q.N. Nguyen, J. Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO Adaptive Video Transmission Strategy Based on Ising Machine DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method ４．発表年 ４．発表年 ４．発表年 K.

**Fragmento 15 - p. 9 - score 1:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題


### 8.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, baseline, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, Rate-based, Comyco, Oboe, A2BR, Fugu, Puffer, Ahaggar, Gelato, Plume, results, performance, ablation`

**Fragmento 1 - p. 3 - score 4:**

(4) Ising machine-based video streaming control method [4] A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the high-quality video streaming model into the QUBO problem, which can be solved by quantum annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown in Table I, results indicated that the QUBO- ABR method outperforms existing algorithms in terms of QoE, which demonstrated the superiority and efficiency of the proposed QUBO-ABR method.

**Fragmento 2 - p. 3 - score 4:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 3 - p. 4 - score 4:**

(5) Annealing-based pilot allocation method [5] An annealing-based pilot allocation method was proposed using Ising machine for solving pilot contamination problem. The proposed method is a max k-cut-based approach, where the graph represents the potential strength of pilot contamination among users in other cells. By using this proposed method, users who have strong relationship with pilot contamination will be assigned different pilots. As shown in Fig. 4, experiment results show that the proposed method can realize optimal pilot allocation and mitigate pilot contamination. Compared with conventional methods, the proposal achieves the best performance which can increase the minimum achievable rate and show higher SINR, especially when the number of users and cells are large.

**Fragmento 4 - p. 4 - score 4:**

(6) Investigation and evaluation of video streaming latency in 5G networks [6] Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network technologies. The performance of parameters such as the number of dropped segments, MAC throughput, and latency were evaluated in various situations such as stationary, moving in the urban area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It has been found that 5G SA can deliver more than 95% of the UHD video segment successfully within the required time window in all situations, while 5G NSA produced mixed results depending on the condition of the LTE network.

**Fragmento 5 - p. 3 - score 3:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 6 - p. 2 - score 2:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 7 - p. 2 - score 2:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 8 - p. 3 - score 2:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 9 - p. 4 - score 2:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 10 - p. 4 - score 2:**

Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022. Fig. 4. The CDF of user’s average uplink SINR for different pilot allocation schemes. [5] Fig. 5. MAC throughput characteristic in the moving case. [6]

**Fragmento 11 - p. 6 - score 2:**

〔学会発表〕 計16件（うち招待講演 1件／うち国際学会 7件） 2022年 2022年 2021年 2021年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会） IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会） The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会） International Conference on Mobile Networks and Management（招待講演）（国際学会） ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 D. Maruyama, B. Wei, H. Song, and J. Katto B. Wei, H. Song, and J. Katto B. Wei, H. Song, Q.N. Nguyen, J. Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO Adaptive Video Transmission Strategy Based on Ising Machine DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method ４．発表年 ４．発表年 ４．発表年 K.

**Fragmento 12 - p. 9 - score 2:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 13 - p. 2 - score 1:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 14 - p. 2 - score 1:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 15 - p. 3 - score 1:**

Fig. 2. Comparison of unfairness, inefficiency, and instability by different methods. [2] Fig. 3. Reinforcement learning framework for ABR control. [3] Table I. Comparison of QoE in two scenarios. [4] Fig. 1. Framework of the testbed for multi-user DASH video streaming. [1]

**Fragmento 16 - p. 7 - score 1:**

2022年 2022年 2022年 2022年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 電子情報通信学会総合大会 電子情報通信学会総合大会 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 甲藤二郎、金井謙治、孫鶴鳴、魏博、勝山裕、文鄭、中村裕一、近藤一晃、下西慶、小野浩司、根波健一、青木智資、片野淳一、吉岡修 一、作中剛、小林康雄、小沢基一、秋田純一 勝山裕、文鄭、金井謙治、孫鶴鳴、魏博、甲藤二郎 Kasidis Arunruangsirilert, Bo Wei, Jiro Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 ４．発表年 ４．発表年 ４．発表年 佐野優斗, 魏博, 宋航, 甲藤二郎 ３．学会等名 ３．学会等名 低遅延でインタラクティブなゼロレイテンシー映像・Somatic統合ネットワーク 低遅延でインタラクティブなゼロレイテンシー映像・Somatic統合ネットワーク－映像情報とSomatic情報の未来予測と統合技術 Evaluation of MPEG-DASH Response Time on Commercial 5G Network Q学習を用いた適応レート制御手法の検討


### 8.8. resultados numericos

Palabras clave usadas: `improve, improvement, outperform, gain, %, QoE gain, higher, lower, average, result, achieve, compared to, reduce, decrease, increase, stall time, stream-years, users, ms, latency`

**Fragmento 1 - p. 4 - score 5:**

(5) Annealing-based pilot allocation method [5] An annealing-based pilot allocation method was proposed using Ising machine for solving pilot contamination problem. The proposed method is a max k-cut-based approach, where the graph represents the potential strength of pilot contamination among users in other cells. By using this proposed method, users who have strong relationship with pilot contamination will be assigned different pilots. As shown in Fig. 4, experiment results show that the proposed method can realize optimal pilot allocation and mitigate pilot contamination. Compared with conventional methods, the proposal achieves the best performance which can increase the minimum achievable rate and show higher SINR, especially when the number of users and cells are large.

**Fragmento 2 - p. 2 - score 4:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 3 - p. 3 - score 4:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 4 - p. 4 - score 4:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 5 - p. 3 - score 3:**

(4) Ising machine-based video streaming control method [4] A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the high-quality video streaming model into the QUBO problem, which can be solved by quantum annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown in Table I, results indicated that the QUBO- ABR method outperforms existing algorithms in terms of QoE, which demonstrated the superiority and efficiency of the proposed QUBO-ABR method.

**Fragmento 6 - p. 4 - score 3:**

(6) Investigation and evaluation of video streaming latency in 5G networks [6] Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network technologies. The performance of parameters such as the number of dropped segments, MAC throughput, and latency were evaluated in various situations such as stationary, moving in the urban area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It has been found that 5G SA can deliver more than 95% of the UHD video segment successfully within the required time window in all situations, while 5G NSA produced mixed results depending on the condition of the LTE network.

**Fragmento 7 - p. 2 - score 2:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 8 - p. 2 - score 2:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 9 - p. 3 - score 2:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 10 - p. 3 - score 2:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 11 - p. 4 - score 2:**

Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022. Fig. 4. The CDF of user’s average uplink SINR for different pilot allocation schemes. [5] Fig. 5. MAC throughput characteristic in the moving case. [6]

**Fragmento 12 - p. 6 - score 2:**

〔学会発表〕 計16件（うち招待講演 1件／うち国際学会 7件） 2022年 2022年 2021年 2021年 ２．発表標題 ２．発表標題 ２．発表標題 ２．発表標題 The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会） IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会） The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会） International Conference on Mobile Networks and Management（招待講演）（国際学会） ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 D. Maruyama, B. Wei, H. Song, and J. Katto B. Wei, H. Song, and J. Katto B. Wei, H. Song, Q.N. Nguyen, J. Katto １．発表者名 １．発表者名 １．発表者名 １．発表者名 ４．発表年 Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO Adaptive Video Transmission Strategy Based on Ising Machine DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method ４．発表年 ４．発表年 ４．発表年 K.

**Fragmento 13 - p. 9 - score 2:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 14 - p. 1 - score 1:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 15 - p. 2 - score 1:**

４．研究成果 (1) Testbed establishment for evaluation of state-of-the-art algorithms [1] A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed

**Fragmento 16 - p. 4 - score 1:**

[3] B. Wei, H. Song, Q.N. Nguyen, J. Katto, “DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method.” International Conference on Mobile Networks and Management, Springer, Cham, 2021. [4] B. Wei, H. Song, and J. Katto, “Adaptive Video Transmission Strategy Based on Ising Machine.” The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys’21), Coimbra, Portugal, November 15-17, 2021. [5] D. Maruyama, B. Wei, H. Song, and J. Katto, “Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO.” 2022 IEEE Wireless Communications and Networking Conference (WCNC), Austin, TX, USA, 10-13 April 2022. [6] K.

**Fragmento 17 - p. 5 - score 1:**

５．主な発表論文等 〔雑誌論文〕 計4件（うち査読付論文 3件／うち国際共著 3件／うちオープンアクセス 1件） 2022年 2022年 2020年 2021年 オープンアクセスではない、又はオープンアクセスが困難 該当する 10.1109/JSEN.2021.3066785 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 Blockchain-based data collection with efficient anomaly detection for estimating battery state- of-health IEEE Sensors Journal - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセスではない、又はオープンアクセスが困難 該当する ４．巻 Ruochen Jin, Bo Wei, Yongmei Luo, Tao Ren, Ruoqian Wu - １．著者名 10.1109/JIOT.2020.2999210 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 WiEps: Measurement of Dielectric Property with Commodity WiFi Device-An Application to Ethanol/Water Mixture IEEE Internet of Things Journal 11667 - 11677 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセスとしている（また、その予定である） 該当する ４．巻 Hang Song, Bo Wei, Qun Yu, Xia Xiao, and Takamaro Kikkawa 7 １．著者名 10.3390/math10091593 ３．雑誌名 ６．最初と最後の頁 有 オープンアクセス 国際共著 ２．論文標題 ５．発行年 Multimedia Applications Processing and Computation Resource Allocation in MEC-Assisted SIoT Systems with DVS Mathematics - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 オープンアクセス 国際共著 オープンアクセスではない、又はオープンアクセスが困難 － ４．巻 Xianwei Li, Guolong Chen, Liang Zhao, Bo Wei - １．著者名 RSSI-CSI Measurement and Variation Mitigation with Commodity WiFi Device arXiv - 掲載論文のDOI（デジタルオブジェクト識別子） 査読の有無 なし ３．雑誌名 ６．最初と最後の頁 無 ４．巻 Bo Wei, Hang Song, Jiro Katto, Takamaro Kikkawa - １．著者名 ２．論文標題 ５．発行年


### 8.9. limitaciones riesgos

Palabras clave usadas: `limitation, future work, challenge, overhead, complexity, generalization, real-world, deployment, cost, computational, unstable, fail, failure, heterogeneous, bias, biased, unbiased, trace-driven, heavy-tailed, unseen, uncertainty, unpredictable, privacy, fairness`

**Fragmento 1 - p. 1 - score 1:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 2 - p. 2 - score 1:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 3 - p. 3 - score 1:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 4 - p. 3 - score 1:**

Fig. 2. Comparison of unfairness, inefficiency, and instability by different methods. [2] Fig. 3. Reinforcement learning framework for ABR control. [3] Table I. Comparison of QoE in two scenarios. [4] Fig. 1. Framework of the testbed for multi-user DASH video streaming. [1]

**Fragmento 5 - p. 4 - score 1:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.


### 8.10. ideas phase45 v1 controller

Palabras clave usadas: `safe, safety, risk, risk-aware, risk-calibrated, conservative, fallback, uncertainty, lower bound, buffer, low buffer, variable, fluctuation, tail, severe, rebuffering, stall, guidance, expert, hybrid, meta, environment-aware, trace skew, cluster, prioritize, fairness, multi-user, TCP, BPM, BSM`

**Fragmento 1 - p. 2 - score 5:**

１．研究開始当初の背景 Video traffic has been the main part of the global IP traffic which account for over 80% of the total internet traffic. It is essential to provide high-quality video streaming service to users. Among the video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the de facto standard which allows the video session on client side to select the video bitrate adaptively. MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level according to the network conditions to tradeoff between video quality and rebuffering risk. Existing state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based (BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy and other information to adaptively control the bitrate. However, most of the methods are designed for single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal of ABR strategy is to achieve fair, stable, efficient video transmission among different users. Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user experience quality. Therefore, when designing the video streaming control method, there are many factors need to be taken into consideration.

**Fragmento 2 - p. 3 - score 3:**

The idea of FRAB is to “relax” the change of the video quality based on current buffer level, which can enhance the stability of video streaming. Meanwhile, by flexibly adjusting the relaxation, the efficiency and fairness among all users are improved. FRAB was evaluated in real experiments under different network conditions and compared with conventional multi-user ABR algorithms. As shown in Fig. 2, results demonstrated that the proposed method has superior performance in multi-user DASH video streaming compared with conventional methods. (3) Reinforcement learning-based video streaming control method [3] An ABR method was proposed to control the live video streaming using the actor-critic reinforcement learning (RL) technique.

**Fragmento 3 - p. 1 - score 2:**

To this end, we have designed ABR methods considering the inter-user factors such as fairness, resource allocation to realize equal quality of experience (QoE) in multi-user networks. Through this research, we have proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and efficient video streaming. Meanwhile, DASH live video streaming control model was developed using reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination. The achievements of this research have been published in peer-reviewed flagship international conferences and top journals.

**Fragmento 4 - p. 2 - score 2:**

３．研究の方法 The method of this research was divided into multiple steps and was conducted as the details: (1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one unified developed testbed which is constructed in this research. (2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video transmission in multi-user network. The emerging advanced techniques such as reinforcement learning (RL), Ising machine, etc. were utilized for constructing the video streaming control model. (3) The proposed methods were evaluated by simulation and real experiments, showing the advantage of the proposals which could achieve high QoE and meet user requirements. (4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency characteristic in various communication scenarios.

**Fragmento 5 - p. 3 - score 2:**

testbed, the performance of current adaptation methods was analyzed and compared in multi-user network. It was found that in the excessive user and limited bandwidth cases, machine learning and scheduling techniques showed superiority in providing high and equal QoE for all users. While in the high-delay case, the buffer-based approaches showed robust performance. The findings gave an insight for designing adaptive streaming strategies in different multi-user network conditions. (2) Fair, stable, and efficient multi-user video streaming control method [2] A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to achieve fair, stable and efficient video streaming among different users.

**Fragmento 6 - p. 3 - score 2:**

As shown in Fig. 3, in this method, the historical video streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration as the states of RL, then the model is established to map the states to an action such as bitrate decision. In this study, the live streaming simulation was utilized to evaluate the method since the model needs training and the simulation can generate data much faster than real experiment. Experiments were conducted to evaluate the proposed method. Results demonstrate that the total QoE in Bus and Car scenarios show the best performance. The QoE of Tram case shows the lowest due to the low bandwidth during communication.

**Fragmento 7 - p. 3 - score 2:**

Fig. 2. Comparison of unfairness, inefficiency, and instability by different methods. [2] Fig. 3. Reinforcement learning framework for ABR control. [3] Table I. Comparison of QoE in two scenarios. [4] Fig. 1. Framework of the testbed for multi-user DASH video streaming. [1]

**Fragmento 8 - p. 9 - score 2:**

2021年 2021年 2021年 2021年 ２．発表標題 ２．発表標題 電子情報通信学会総合大会 ３．学会等名 ３．学会等名 ３．学会等名 ３．学会等名 IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会） Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei, Hang Song, and Jiro Katto Bo Wei and Jiro Katto IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会） 信学会CQ研究会 ４．発表年 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming High-QoE DASH live streaming using reinforcement learning Latency evaluation of DASH live streaming using throughput prediction The influence of target buffer on the user experience in live video streaming １．発表者名 １．発表者名 ２．発表標題 ２．発表標題

**Fragmento 9 - p. 1 - score 1:**

早稲田大学・理工学術院・次席研究員 科学研究費助成事業 研究成果報告書 様 式 Ｃ－１９、Ｆ－１９－１、Ｚ－１９ （共通） 機関番号： 研究種目： 課題番号： 研究課題名（和文） 研究代表者 研究課題名（英文） 交付決定額（研究期間全体）：（直接経費） ３２６８９ 若手研究 2021 ～ 2020 Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming in multi-user networks ００８４４４３２ 研究者番号： 魏 博（Wei, Bo） 研究期間： ２０Ｋ１４７４０ 年 月 日現在 ４ ６ １６ 円 1,900,000 研究成果の概要（和文）：本研究は、マルチユーザーネットワークにおいて、高品質で公平な映像配信サービス を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、 リソース割り当てなどのユーザー間要因を考慮した適応映像制御技術を提案した。緩和スキーム方法を提案し、 公平かつ安定した効率的な映像配信を実現した。一方、ライブ映像配信において、強化学習法を活用し、高品質 な配信を実現できる制御方法を提案した。また、アニーリングベースのパイロット割り当て方法を提案し、パイ ロット割り当ての最適化とパイロット汚染の軽減を実現した。本研究の成果は、査読付きの国際学会と学術誌で 発表した。 研究成果の概要（英文）：This research focused on developing the adaptive bitrate (ABR) technology to provide high quality and fair video streaming service in multi-user network.

**Fragmento 10 - p. 1 - score 1:**

研究分野：通信・ネットワーク工学 キーワード：Adaptive bitrate control Video streaming Multi-user network QoE Machine learning １版 令和 研究成果の学術的意義や社会的意義 映像コンテンツは現在のIPトラフィックの８０％以上を占めている。また、リモートワーク、ミーティング、オ ンライン授業などのあらゆる場面でも、映像配信がますます不可欠になっている。高品質な映像配信は、現在の 社会生活に対し、極めて重要と言える。本研究で提案している公平かつ高品質な映像配信技術は、適応映像制御 の研究分野に貢献できる。そして、動的且つ大規模なユーザーネットワークにおいて、知的な次世代超高解像度 映像伝送技術とSociety5.0の実現に資することが考えられる。 ※科研費による研究は、研究者の自覚と責任において実施するものです。そのため、研究の実施や研究成果の公表等に ついては、国の要請等に基づくものではなく、その研究成果に関する見解や責任は、研究者個人に帰属します。

**Fragmento 11 - p. 2 - score 1:**

２．研究の目的 The purpose of this research is to study the adaptive video streaming for multi-user networks and develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is employed and new testbed framework is developed for evaluating and designing adaptation algorithms. Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video streaming in various network conditions regardless of the network dynamics. Furthermore, the characteristics of the next-generation 5G mobile network is investigated and the video streaming over 5G is carried out to analyze the low-latency feature for content delivery in various network conditions.

**Fragmento 12 - p. 4 - score 1:**

The results also revealed that the LTE network failed to deliver more than 20% of the video segment within the deadline, which showed that 5G SA is absolutely necessary for low-latency UHD video streaming and 5G NSA may not be good enough for such task as it relies on the legacy control signal. <引用文献> [1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference (WCNC) 2021, Nanjing, China, 29 March-1 April 2021. [2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi- user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, Montreal, QC, Canada, 14-23 June 2021.

**Fragmento 13 - p. 8 - score 1:**

2021年 2021年 2021年 2021年 ２．発表標題 電子情報通信学会ソサイエティ大会 ３．学会等名 ３．学会等名 ３．学会等名 電子情報通信学会ソサイエティ大会 電子情報通信学会ソサイエティ大会 IEEE International Conference on Communications (ICC) 2021（国際学会） Bo Wei, Jiro Katto Bo Wei, Hang Song, and Jiro Katto ２．発表標題 ２．発表標題 １．発表者名 ４．発表年 ４．発表年 ４．発表年 １．発表者名 １．発表者名 ４．発表年 魏博, 甲藤二郎: Throughput prediction of mmWave for 5G network FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi-user DASH Video Streaming 強化学習を用いたDASHライブ動画配信制御 4K映像配信におけるバッファ容量に基づくレート制御の性能評価 １．発表者名 佐野優斗, 魏博, 宋航, 甲藤二郎 ３．学会等名 ２．発表標題


## 9. Checklist de informacion que Codex debe extraer de este paper

- Modelo/algoritmo exacto propuesto.
- Inputs/features realmente usados en decision o entrenamiento.
- Accion ABR y espacio de acciones.
- Reward/QoE/objetivo/loss.
- Teacher, experto, simulador o politica base si existe.
- Datos/trazas/datasets y splits.
- Baselines y evaluacion.
- Resultados numericos utiles.
- Limitaciones, costes, dependencias y riesgos de implementacion.
- Elementos transferibles a un controller propio en DashClientModular4.
- Elementos que NO deben copiarse por complejidad, leakage, GPU, dependencia o falta de defensa.


## 10. Extraccion cruda pagina a pagina

Texto extraido por pagina. Puede contener artefactos de dos columnas, referencias mezcladas, pies de figura o formulas degradadas. Para formulas/tablas/figuras, verificar PDF original.


### Pagina 1

```text
早稲田大学・理工学術院・次席研究員
科学研究費助成事業　　研究成果報告書
様　式　Ｃ－１９、Ｆ－１９－１、Ｚ－１９ （共通）
機関番号：
研究種目：
課題番号：
研究課題名（和文）
研究代表者
研究課題名（英文）
交付決定額（研究期間全体）：（直接経費）
３２６８９
若手研究
2021
～
2020
Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming
 in multi-user networks
Adaptive bitrate control strategy for ensuring high-QoE and fair video streaming
 in multi-user networks
００８４４４３２
研究者番号：
魏　博（Wei, Bo）
研究期間：
２０Ｋ１４７４０
年
月
日現在
  ４
  ６
１６
円
     1,900,000
研究成果の概要（和文）：本研究は、マルチユーザーネットワークにおいて、高品質で公平な映像配信サービス
を提供する適応制御技術の開発を目的としている。公平なユーザ体感品質（QoE）を実現するために、公平性、
リソース割り当てなどのユーザー間要因を考慮した適応映像制御技術を提案した。緩和スキーム方法を提案し、
公平かつ安定した効率的な映像配信を実現した。一方、ライブ映像配信において、強化学習法を活用し、高品質
な配信を実現できる制御方法を提案した。また、アニーリングベースのパイロット割り当て方法を提案し、パイ
ロット割り当ての最適化とパイロット汚染の軽減を実現した。本研究の成果は、査読付きの国際学会と学術誌で
発表した。
研究成果の概要（英文）：This research focused on developing the adaptive bitrate (ABR) technology to
 provide high quality and fair video streaming service in multi-user network. To this end, we have 
designed ABR methods considering the inter-user factors such as fairness, resource allocation to 
realize equal quality of experience (QoE) in multi-user networks. Through this research, we have 
proposed ABR models using flexible relaxation scheme, which was able to achieve fair, stable and 
efficient video streaming. Meanwhile, DASH live video streaming control model was developed using 
reinforcement learning method to realize high-QoE content delivery. Further, Annealing-based pilot 
allocation method was proposed to realize optimal pilot allocation and mitigate pilot contamination.
 The achievements of this research have been published in peer-reviewed flagship international 
conferences and top journals. 
研究分野：通信・ネットワーク工学
キーワード：Adaptive bitrate control　Video streaming　Multi-user network　QoE　Machine learning
  １版
令和
研究成果の学術的意義や社会的意義
映像コンテンツは現在のIPトラフィックの８０％以上を占めている。また、リモートワーク、ミーティング、オ
ンライン授業などのあらゆる場面でも、映像配信がますます不可欠になっている。高品質な映像配信は、現在の
社会生活に対し、極めて重要と言える。本研究で提案している公平かつ高品質な映像配信技術は、適応映像制御
の研究分野に貢献できる。そして、動的且つ大規模なユーザーネットワークにおいて、知的な次世代超高解像度
映像伝送技術とSociety5.0の実現に資することが考えられる。
※科研費による研究は、研究者の自覚と責任において実施するものです。そのため、研究の実施や研究成果の公表等に
ついては、国の要請等に基づくものではなく、その研究成果に関する見解や責任は、研究者個人に帰属します。
```


### Pagina 2

```text
様 式 Ｃ－１９、Ｆ－１９－１、Ｚ－１９（共通） 
 
１．研究開始当初の背景 
Video traffic has been the main part of the global IP traffic which account for over 80% of the total 
internet traffic. It is essential to provide high-quality video streaming service to users. Among the 
video transmission technologies, Dynamic Adaptive Streaming over HTTP (DASH) has become the 
de facto standard which allows the video session on client side to select the video bitrate adaptively. 
MPEG-DASH has been widely adopted in modern video streaming services. In DASH, the core 
technique is adaptive bitrate (ABR) control which can adjust the requested video bitrate level 
according to the network conditions to tradeoff between video quality and rebuffering risk. Existing 
state-of-the-art ABR methods can be classified into three categories: Rate-based (RB), Buffer-based 
(BB), and Hybrid methods. RB methods employ the throughput prediction to determine the future 
bitrate selection. BB methods utilize the current buffer state to choose bitrate. Hybrid methods, such 
as learning-based methods and control-theoretic methods, use bandwidth prediction, buffer occupancy 
and other information to adaptively control the bitrate. However, most of the methods are designed for 
single-user case. It is a challenge for the ABR methods in the scenarios when multiple DASH 
streaming users compete over the network bottleneck. In multi-user DASH streaming, the design goal 
of ABR strategy is to achieve fair, stable, efficient video transmission among different users. 
Meanwhile, in the real-time streaming, low latency is also an essential factor to ensure the high user 
experience quality. Therefore, when designing the video streaming control method, there are many 
factors need to be taken into consideration. 
 
２．研究の目的 
  The purpose of this research is to study the adaptive video streaming for multi-user networks and 
develop ABR techniques for ensuring high-QoE (Quality of Experience) and fair service under various 
environments. The objectives of the research are as follows: The newly unified ITU-T QoE metric is 
employed and new testbed framework is developed for evaluating and designing adaptation algorithms. 
Meanwhile, the state-of-the-art bitrate adaptation algorithms is incorporated into the framework, and 
experiments are conducted to evaluate the performance of these methods in multi-user scenarios. Then, 
novel ABR methods are developed to realize high-quality, fair, stable, efficient multi-user DASH video 
streaming in various network conditions regardless of the network dynamics. Furthermore, the 
characteristics of the next-generation 5G mobile network is investigated and the video streaming over 
5G is carried out to analyze the low-latency feature for content delivery in various network conditions.  
 
３．研究の方法 
  The method of this research was divided into multiple steps and was conducted as the details:  
(1) The newest standard ITU-T P.1203 model was implemented to estimate the QoE of ABR 
methods. Therefore, all the state-of-the-art methods were compared, analyzed and evaluated under one 
unified developed testbed which is constructed in this research. 
(2) Adaptive bitrate control methods were developed to realize fair, stable, efficient video 
transmission in multi-user network. The emerging advanced techniques such as reinforcement learning 
(RL), Ising machine, etc. were utilized for constructing the video streaming control model. 
(3) The proposed methods were evaluated by simulation and real experiments, showing the 
advantage of the proposals which could achieve high QoE and meet user requirements. 
(4) The real implementation of Ultra High Definition (UHD) live streaming via MPEG-DASH over 
different mobile networks were conducted, including LTE, WiFi, 5G NSA (Non-Stand Alone) and 5G 
SA (Stand Alone). The characteristics of different networks were analyzed to evaluate the latency 
characteristic in various communication scenarios. 
 
４．研究成果 
(1) Testbed establishment for evaluation of state-of-the-art algorithms [1] 
A new mininet-based testbed framework was proposed as shown in Fig. 1. Seven state-of-the-art 
adaptation methods were incorporated into the testbed. Meanwhile, ITU-T P.1203 model, the world’s 
first standard for measuring QoE of HTTP adaptive streaming was implemented. Using the developed
```


### Pagina 3

```text
testbed, the performance of current adaptation 
methods was analyzed and compared in multi-user 
network. It was found that in the excessive user and 
limited bandwidth cases, machine learning and 
scheduling techniques showed superiority in 
providing high and equal QoE for all users. While 
in the high-delay case, the buffer-based approaches 
showed robust performance. The findings gave an 
insight for designing adaptive streaming strategies 
in different multi-user network conditions.  
(2) Fair, stable, and efficient multi-user video streaming control method [2] 
A client-side ABR control method was proposed, flexible relaxation assisted by buffer (FRAB), to 
achieve fair, stable and efficient video streaming among different users. The idea of FRAB is to “relax” 
the change of the video quality based on current buffer level, which can enhance the stability of video 
streaming. Meanwhile, by flexibly adjusting 
the relaxation, the efficiency and fairness 
among all users are improved. FRAB was 
evaluated in real experiments under different 
network conditions and compared with 
conventional multi-user ABR algorithms. As 
shown in Fig. 2, results demonstrated that the 
proposed method has superior performance 
in multi-user DASH video streaming 
compared with conventional methods.  
(3) Reinforcement learning-based video streaming control method [3] 
An ABR method was proposed to control the live video streaming using the actor-critic 
reinforcement learning (RL) technique. As shown in Fig. 3, in this method, the historical video 
streaming logs such as throughput, buffer size, rebuffering time, latency are taken into consideration 
as the states of RL, then the model is established to map the states to an action such as bitrate decision. 
In this study, the live streaming simulation was 
utilized to evaluate the method since the 
model needs training and the simulation can 
generate 
data 
much 
faster 
than 
real 
experiment. Experiments were conducted to 
evaluate the proposed method. Results 
demonstrate that the total QoE in Bus and Car 
scenarios show the best performance. The 
QoE of Tram case shows the lowest due to the 
low bandwidth during communication.  
(4) Ising machine-based video streaming control method [4] 
A novel ABR strategy was proposed based on Ising machine by using the quadratic unconstrained 
binary optimization (QUBO) method for the first time. The purpose of this method is to formulate the 
high-quality video streaming model into the QUBO problem, which can be solved by quantum 
annealing or simulated annealing. This is the first proposal which utilizes Ising machine/QUBO 
approach to solve the adaptive video streaming problem. Experiments were conducted to evaluate the 
proposed QUBO-ABR method and compare the performance with other ABR algorithms. As shown 
in Table I, results indicated that the QUBO-
ABR 
method 
outperforms 
existing 
algorithms in terms of QoE, which 
demonstrated the superiority and efficiency 
of the proposed QUBO-ABR method.  
 
Fig. 2. Comparison of unfairness, inefficiency, and 
instability by different methods. [2] 
Fig. 3. Reinforcement learning framework for ABR control. [3] 
Table I. Comparison of QoE in two scenarios. [4] 
Fig. 1. Framework of the testbed for multi-user 
DASH video streaming. [1]
```


### Pagina 4

```text
(5) Annealing-based pilot allocation method [5] 
An annealing-based pilot allocation method was proposed using Ising machine for solving pilot 
contamination problem. The proposed method is a max k-cut-based approach, where the graph 
represents the potential strength of pilot 
contamination among users in other cells. By 
using this proposed method, users who have 
strong relationship with pilot contamination will 
be assigned different pilots. As shown in Fig. 4, 
experiment results show that the proposed 
method can realize optimal pilot allocation and 
mitigate pilot contamination. Compared with 
conventional methods, the proposal achieves the 
best performance which can increase the 
minimum achievable rate and show higher 
SINR, especially when the number of users and 
cells are large.  
(6) Investigation and evaluation of video streaming latency in 5G networks [6] 
Real-time UHD live streaming via MPEG-DASH was carried out over different mobile network 
technologies. The performance of parameters such as the number of dropped segments, MAC 
throughput, and latency were evaluated in various situations such as stationary, moving in the urban 
area, moving at high speed. Fig. 5 shows the comparison of MAC throughput in user moving case. It 
has been found that 5G SA can deliver more 
than 95% of the UHD video segment 
successfully within the required time window 
in all situations, while 5G NSA produced 
mixed results depending on the condition of the 
LTE network. The results also revealed that the 
LTE network failed to deliver more than 20% 
of the video segment within the deadline, 
which showed that 5G SA is absolutely 
necessary 
for 
low-latency 
UHD 
video 
streaming and 5G NSA may not be good 
enough for such task as it relies on the legacy 
control signal. 
 
 
<引用文献> 
[1] B. Wei, H. Song, S. Wang, and J. Katto, “Performance Analysis of Adaptive Bitrate Algorithms for 
Multi-user DASH Video Streaming.” IEEE Wireless Communications and Networking Conference 
(WCNC) 2021, Nanjing, China, 29 March-1 April 2021. 
[2] B. Wei, H. Song, and J. Katto, “FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi-
user DASH Video Streaming.” IEEE International Conference on Communications (ICC) 2021, 
Montreal, QC, Canada, 14-23 June 2021. 
[3] B. Wei, H. Song, Q.N. Nguyen, J. Katto, “DASH Live Video Streaming Control Using Actor-Critic 
Reinforcement Learning Method.” International Conference on Mobile Networks and Management, 
Springer, Cham, 2021. 
[4] B. Wei, H. Song, and J. Katto, “Adaptive Video Transmission Strategy Based on Ising Machine.” The 
19th ACM Conference on Embedded Networked Sensor Systems (SenSys’21), Coimbra, Portugal, 
November 15-17, 2021. 
[5] D. Maruyama, B. Wei, H. Song, and J. Katto, “Pilot Allocation Optimization using Digital Annealer 
for Multi-cell Massive MIMO.” 2022 IEEE Wireless Communications and Networking Conference 
(WCNC), Austin, TX, USA, 10-13 April 2022. 
[6] K. Arunruangsirilert, B. Wei, H. Song, and J. Katto, “Performance Evaluation of Low-Latency Live 
Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network.” The 4th 
International Workshop on Smart City Communication and Networking, ICCCN 2022. 
Fig. 4. The CDF of user’s average uplink SINR for 
different pilot allocation schemes. [5] 
Fig. 5. MAC throughput characteristic in the 
moving case. [6]
```


### Pagina 5

```text
５．主な発表論文等
〔雑誌論文〕　計4件（うち査読付論文　3件／うち国際共著　3件／うちオープンアクセス　1件）
2022年
2022年
2020年
2021年
オープンアクセスではない、又はオープンアクセスが困難
該当する
10.1109/JSEN.2021.3066785
 ３．雑誌名
 ６．最初と最後の頁
有
 オープンアクセス
 国際共著
 ２．論文標題
 ５．発行年
Blockchain-based data collection with efficient anomaly detection for estimating battery state-
of-health
IEEE Sensors Journal
-
 掲載論文のDOI（デジタルオブジェクト識別子）
 査読の有無
オープンアクセスではない、又はオープンアクセスが困難
該当する
 ４．巻
Ruochen Jin, Bo Wei, Yongmei Luo, Tao Ren, Ruoqian Wu
-
 １．著者名
10.1109/JIOT.2020.2999210
 ３．雑誌名
 ６．最初と最後の頁
有
 オープンアクセス
 国際共著
 ２．論文標題
 ５．発行年
WiEps: Measurement of Dielectric Property with Commodity WiFi Device-An Application to
Ethanol/Water Mixture
IEEE Internet of Things Journal
11667 - 11677
 掲載論文のDOI（デジタルオブジェクト識別子）
 査読の有無
オープンアクセスとしている（また、その予定である）
該当する
 ４．巻
Hang Song, Bo Wei, Qun Yu, Xia Xiao, and Takamaro Kikkawa
7
 １．著者名
10.3390/math10091593
 ３．雑誌名
 ６．最初と最後の頁
有
 オープンアクセス
 国際共著
 ２．論文標題
 ５．発行年
Multimedia Applications Processing and Computation Resource Allocation in MEC-Assisted SIoT
Systems with DVS
Mathematics
-
 掲載論文のDOI（デジタルオブジェクト識別子）
 査読の有無
 オープンアクセス
 国際共著
オープンアクセスではない、又はオープンアクセスが困難
－
 ４．巻
Xianwei Li, Guolong Chen, Liang Zhao, Bo Wei
-
 １．著者名
RSSI-CSI Measurement and Variation Mitigation with Commodity WiFi Device
arXiv
-
 掲載論文のDOI（デジタルオブジェクト識別子）
 査読の有無
なし
 ３．雑誌名
 ６．最初と最後の頁
無
 ４．巻
Bo Wei, Hang Song, Jiro Katto, Takamaro Kikkawa
-
 １．著者名
 ２．論文標題
 ５．発行年
```


### Pagina 6

```text
〔学会発表〕　計16件（うち招待講演　1件／うち国際学会　7件）
2022年
2022年
2021年
2021年
 ２．発表標題
 ２．発表標題
 ２．発表標題
 ２．発表標題
The 4th International Workshop on Smart City Communication and Networking, ICCCN 2022（国際学会）
IEEE Wireless Communications and Networking Conference (WCNC) 2022（国際学会）
The 19th ACM Conference on Embedded Networked Sensor Systems (SenSys ’21)（国際学会）
International Conference on Mobile Networks and Management（招待講演）（国際学会）
 ３．学会等名
 ３．学会等名
 ３．学会等名
 ３．学会等名
D. Maruyama, B. Wei, H. Song, and J. Katto
B. Wei, H. Song, and J. Katto
B. Wei, H. Song, Q.N. Nguyen, J. Katto
 １．発表者名
 １．発表者名
 １．発表者名
 １．発表者名
 ４．発表年
Performance Evaluation of Low-Latency Live Streaming of MPEG-DASH UHD video over Commercial 5G NSA/SA Network
Pilot Allocation Optimization using Digital Annealer for Multi-cell Massive MIMO
Adaptive Video Transmission Strategy Based on Ising Machine
DASH Live Video Streaming Control Using Actor-Critic Reinforcement Learning Method
 ４．発表年
 ４．発表年
 ４．発表年
K. Arunruangsirilert, B. Wei, H. Song, and J. Katto
```


### Pagina 7

```text
2022年
2022年
2022年
2022年
 ２．発表標題
 ２．発表標題
 ２．発表標題
 ２．発表標題
電子情報通信学会総合大会
電子情報通信学会総合大会
電子情報通信学会総合大会
電子情報通信学会総合大会
 ３．学会等名
 ３．学会等名
甲藤二郎、金井謙治、孫鶴鳴、魏博、勝山裕、文鄭、中村裕一、近藤一晃、下西慶、小野浩司、根波健一、青木智資、片野淳一、吉岡修
一、作中剛、小林康雄、小沢基一、秋田純一
勝山裕、文鄭、金井謙治、孫鶴鳴、魏博、甲藤二郎
Kasidis Arunruangsirilert, Bo Wei, Jiro Katto
 １．発表者名
 １．発表者名
 １．発表者名
 １．発表者名
 ４．発表年
 ４．発表年
 ４．発表年
 ４．発表年
佐野優斗, 魏博, 宋航, 甲藤二郎
 ３．学会等名
 ３．学会等名
低遅延でインタラクティブなゼロレイテンシー映像・Somatic統合ネットワーク
低遅延でインタラクティブなゼロレイテンシー映像・Somatic統合ネットワーク－映像情報とSomatic情報の未来予測と統合技術
Evaluation of MPEG-DASH Response Time on Commercial 5G Network
Q学習を用いた適応レート制御手法の検討
```


### Pagina 8

```text
2021年
2021年
2021年
2021年
 ２．発表標題
電子情報通信学会ソサイエティ大会
 ３．学会等名
 ３．学会等名
 ３．学会等名
電子情報通信学会ソサイエティ大会
電子情報通信学会ソサイエティ大会
IEEE International Conference on Communications (ICC) 2021（国際学会）
Bo Wei, Jiro Katto
Bo Wei, Hang Song, and Jiro Katto
 ２．発表標題
 ２．発表標題
 １．発表者名
 ４．発表年
 ４．発表年
 ４．発表年
 １．発表者名
 １．発表者名
 ４．発表年
魏博, 甲藤二郎:
Throughput prediction of mmWave for 5G network
FRAB: A Flexible Relaxation Method for Fair, Stable, Efficient Multi-user DASH Video Streaming
強化学習を用いたDASHライブ動画配信制御
4K映像配信におけるバッファ容量に基づくレート制御の性能評価
 １．発表者名
佐野優斗, 魏博, 宋航, 甲藤二郎
 ３．学会等名
 ２．発表標題
```


### Pagina 9

```text
2021年
2021年
2021年
2021年
 ２．発表標題
 ２．発表標題
電子情報通信学会総合大会
 ３．学会等名
 ３．学会等名
 ３．学会等名
 ３．学会等名
IEEE Wireless Communications and Networking Conference (WCNC) 2021（国際学会）
Bo Wei, Hang Song, Shangguang Wang, and Jiro Katto
Bo Wei, Hang Song, and Jiro Katto
Bo Wei, Hang Song, and Jiro Katto
Bo Wei and Jiro Katto
IEEE/ACM International Symposium on Quality of Service (IWQoS) 2021（国際学会）
信学会CQ研究会
 ４．発表年
 ４．発表年
 ４．発表年
 ４．発表年
 １．発表者名
 １．発表者名
Performance Analysis of Adaptive Bitrate Algorithms for Multi-user DASH Video Streaming
High-QoE DASH live streaming using reinforcement learning
Latency evaluation of DASH live streaming using throughput prediction
The influence of target buffer on the user experience in live video streaming
 １．発表者名
 １．発表者名
 ２．発表標題
 ２．発表標題
```


### Pagina 10

```text
〔図書〕　計0件
〔産業財産権〕
〔その他〕
－
６．研究組織
７．科研費を使用して開催した国際研究集会
〔国際研究集会〕　計0件
８．本研究に関連して実施した国際共同研究の実施状況
中国
Tianjin University
所属研究機関・部局・職
（機関番号）
氏名
（ローマ字氏名）
（研究者番号）
備考
共同研究相手国
相手方研究機関
```
