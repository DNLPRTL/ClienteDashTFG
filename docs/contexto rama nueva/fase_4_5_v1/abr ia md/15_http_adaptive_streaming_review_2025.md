# HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
**Archivo PDF:** `3736306.pdf`  **Identificador:** `15_http_adaptive_streaming_review_2025`  **Páginas:** 27  **SHA256 PDF:** `ae1d346b80c409b36321921522a0fd0bc0aa46a115c05e2e4499ef19e4620e83`  **Foco para Fase 4-5 v1:** HAS/DASH review; ABR algorithms; QoE; energy; future challenges; taxonomy for memory/defense.
> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.
## 1. Cómo usar este `.md`
- Leer primero secciones 2-5 para ubicar método, señales, datos, evaluación y limitaciones.
- Usar la extracción por categorías como material de diseño/contrato/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No convertir resultados del paper en promesas directas para DashClientModular4; deben transformarse en hipótesis, guardrails y tests Phase 6.
## 2. Metadatos extraídos
- **format:** PDF 2.0
- **title:** HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
- **subject:** -  Information systems  ->  Multimedia streaming;
- **creator:** LaTeX with acmart 2024/12/28 v2.12 Typesetting articles for the Association for Computing Machinery and hyperref 2024-11-05 v7.01l Hypertext links for LaTeX
- **producer:** LuaHBTeX, Version 1.21.0 (MiKTeX 25.3)
- **creationDate:** D:20250717174052+05'30'
- **modDate:** D:20250717174052+05'30'

## 3. Índice de secciones detectadas
- p.1: ACM 1551-6865/2025/7-ART198
- p.2: Introduction
- p.9: methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal
- p.11: results. To this end, several model-free methods exist that utilize the metadata observed from the
- p.20: References
- p.21: results. IEEE Journal on Selected Areas in Communications 20, 7 (2002), 1305–1314. DOI: https://doi.org/10.1109/JSAC.
- p.22: evaluation of network-assisted strategies for HTTP adaptive streaming. In Proceedings of the 7th International
- p.23: Experiments and Technologies (CoNEXT ’09). ACM, New York, NY, 1–12. DOI: https://doi.org/10.1145/1658939.1658941

## 4. Índice de páginas con palabras clave
- p.1: QoE, latency, quality
- p.2: QoE, bandwidth, quality
- p.3: QoE, throughput, bandwidth, download, chunk, baseline, PPO, fallback, network condition
- p.4: download, latency, quality
- p.5: state, QoE, buffer, bandwidth, download, PPO, quality, network condition
- p.6: state, bandwidth, inference, quality, visual
- p.7: PPO, quality, visual
- p.8: bandwidth, dataset, quality, VMAF, network condition
- p.9: quality
- p.10: QoE, PPO, latency, quality, VMAF
- p.11: QoE, bandwidth, PPO
- p.12: QoE, bandwidth, PPO, latency, quality
- p.13: buffer, bandwidth, download, quality
- p.14: state, QoE, stall, buffer, bandwidth, download, chunk, imitation, latency, quality
- p.15: state, QoE, stall, buffer, throughput, bandwidth, download, trace, latency, quality, visual, network condition
- p.16: state, action, QoE, rebuffer, buffer, throughput, bandwidth, training, latency, quality, VMAF, network condition
- p.17: state, QoE, rebuffer, stall, buffer, bandwidth, PPO, latency, quality, network condition
- p.18: action, PPO
- p.19: QoE, throughput, dataset, training, PPO, quality
- p.20: action, PPO, latency, quality, VMAF, SSIM
- p.21: action, QoE, throughput, download, latency, quality, VMAF, SSIM
- p.22: action, QoE, latency, quality
- p.23: state, action, QoE, dataset, BBA, PPO, latency, quality, VMAF
- p.24: action, bandwidth, PPO, SSIM
- p.25: action, bandwidth, dataset, quality, visual
- p.26: action, latency, SSIM, visual
- p.27: latency, quality

## 5. Extracción técnica cruda por categorías

### 5.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

RISTIAN TIMMERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future

**[Modelo / arquitectura / algoritmo | extracto 2 | p.1]**

furt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM Trans. Multimedia Comput. Commun. Appl. 21, 7, Article 198 (July 2025), 27 pages. https://doi.org/10.1145/3736306 Auth

**[Modelo / arquitectura / algoritmo | extracto 3 | p.1]**

ER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM Trans. Multimedia Comput. Commun. Appl. 21, 7, Article 198 (July 2025), 27 pages. https://doi.org/10.1145/3736306 Authors’ Contact Information: Christian Timmerer (corresponding author), Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria; e-mail: christ

**[Modelo / arquitectura / algoritmo | extracto 4 | p.2]**

g, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including Quality of Experience (QoE). For each of these phases, we will outline basic principles, current trends, and future challenges for HAS. The structure of this article is as follows. Section 2 covers the early history of video streaming on the Internet, the rise of HAS and its fundamental principles, a brief summary of international standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for HAS, including per-title encoding and recent optimizations, as well as energy-related concerns. Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Section 8 wraps up the article. 2 Background 2.1 A Brief History of Video Streaming The era of video streaming on the Internet dates back to the last decade of the previous century, when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994 [56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming event in 1995 with the Seattle Mariners vs. New York Yankees resulting in RealSystem G2 SureStream technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe adaptive streaming within the 3GPP packet-switched streaming service that uses the

**[Modelo / arquitectura / algoritmo | extracto 5 | p.2]**

198:2 C. Timmerer et al. 1 Introduction Over the last 20 years, video streaming has surged in popularity and now constitutes over more than half of global Internet traffic [99]. This trend can be attributed in part to advancements in video compression technologies, such as Advanced Video Coding (AVC) (2003) [122], High Effi- ciency Video Coding (HEVC) (2013) [108], and Versatile Video Coding (VVC) (2020) [30, 31]. Each new generation of video codecs offers more than a 50% improvement in bitrate and qual- ity, respectively. Additionally, developments in networking technology comply with Nielsen’s law of bandwidth, which asserts that “a high-end user’s connection speed grows by 50% per year” [88]. When combined with the increasing computational power of user devices (cf. Moore’s law), this allows for the creation and consumption of video content anywhere and at any time across various devices. Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based, unicast schemes utilizing existing Web-based infras- tructure to allow for better scalability. When referring to this streaming approach, we use the term HTTP Adaptive Streaming (HAS)1 consistently throughout this article. Standards helped facilitate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and Apple HTTP Live Streaming (HLS), although standa

**[Modelo / arquitectura / algoritmo | extracto 6 | p.3]**

dth conditions, and clients rendering the requested video for the end users. The video content is typically segmented over time (e.g., a few seconds per segment) and provided in multiple versions (e.g., resolutions, frame rates, bitrates, qualities, codecs, languages) referred to as bitrate ladder. In addition to the segments, a manifest is pro- vided that enables smart clients to issue timed HTTP requests for individual segments (or parts thereof) from one of the multiple versions provided at the server, depending on the clients’ context conditions including—but not limited to—device characteristics, network conditions, and user pref- erences in order to maximize QoE. An important design choice comprises that servers host those segments and its manifest, and clients decide which segments to request when. Thus, clients imple- ment an ABR algorithm, not normatively specified within existing standards, subject to research and development. 2.3 Overview of HAS Standards The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which replaced prior proprietary formats such as Microsoft Smooth Streaming and Adobe HDS. Both standards define formats allowing implementation of the basic HAS principles as outlined above with (minor) differences with respect to segment and manifest formats. The MPEG DASH data model is shown in Figure 2 which comprises an XML-based Media Presentation Description as manifest and allows the video content to be divided into periods for content slicing including ad support. 2We note that HAS is typically deployed via TCP for HTTP/1.1 and HTTP/2 unless explicitly mentioned for HTTP/3 or QUIC which uses UDP. ACM Trans. Multimedia

**[Modelo / arquitectura / algoritmo | extracto 7 | p.3]**

rver, depending on the clients’ context conditions including—but not limited to—device characteristics, network conditions, and user pref- erences in order to maximize QoE. An important design choice comprises that servers host those segments and its manifest, and clients decide which segments to request when. Thus, clients imple- ment an ABR algorithm, not normatively specified within existing standards, subject to research and development. 2.3 Overview of HAS Standards The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which replaced prior proprietary formats such as Microsoft Smooth Streaming and Adobe HDS. Both standards define formats allowing implementation of the basic HAS principles as outlined above with (minor) differences with respect to segment and manifest formats. The MPEG DASH data model is shown in Figure 2 which comprises an XML-based Media Presentation Description as manifest and allows the video content to be divided into periods for content slicing including ad support. 2We note that HAS is typically deployed via TCP for HTTP/1.1 and HTTP/2 unless explicitly mentioned for HTTP/3 or QUIC which uses UDP. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Modelo / arquitectura / algoritmo | extracto 8 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still d

**[Modelo / arquitectura / algoritmo | extracto 9 | p.4]**

ents. Each adaptation set provides multiple representations of the same content with various characteristics (e.g., resolution, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g., the source element) to allow JavaScript to generate media streams for playback, whereby an ABR algorithm could be implemented in JavaScript [92]. In general, DASH and HLS can be used interchangeably without impacting the performance of video streaming services [24]. 2.4 End-to-End Video Streaming Workflow End-to-end video streaming refers to the entire process involved in delivering video content from its source (content creation) to the end user (playback). This comprehensive process involves multiple phases, each critical to ensure a seamless and high-quality streaming experience. Figure 3 shows the five key phases of the end-to-end video streaming pipeline, described as follows: —Content Creation and Ingestion. This phase consists of two main procedures: Content creation and content ingestion. Content creation is the initial step that involves the production of video content, whether it is live broadcasts, pre-recorded shows, or user-gen

**[Modelo / arquitectura / algoritmo | extracto 10 | p.4]**

198:4 C. Timmerer et al. Fig. 1. Basic principles of HAS. Fig. 2. MPEG DASH data model. Each period comprises multiple adaptation sets of different modalities (e.g., video, audio, subtitles) for component selection by clients. Each adaptation set provides multiple representations of the same content with various characteristics (e.g., resolution, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, whic

**[Modelo / arquitectura / algoritmo | extracto 11 | p.5]**

45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player determines the quality of next segment to be downloaded. In Section 5, we will introduce various types of ABR algorithms. The device decodes the requested video stream and plays it back to the user. The video is rendered on the device’s display, and the quality of this rendering depends on the device’s capabilities, including screen resolution, processing power, and software optimizations. In this article, particular attention will be paid to video as a primary focus, given the preponder- ance of existing research articles centered on HAS and video. However, this emphasis should not overshadow the significance of other modalities, which remain crucial areas of study: these include, but are not limited to, audio, subtitles, haptics, and mulsemedia. In particular, audio streaming in conjunction with HAS is covered in [37, 95]

**[Modelo / arquitectura / algoritmo | extracto 12 | p.5]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:5 Fig. 3. Main phases of the end-to-end video streaming workflow. content is captured using cameras or created using digital tools. Once created, the video is ingested into the streaming platform’s infrastructure. Content ingestion involves uploading or feeding the video data into the system, where it can be processed and prepared for streaming. Several protocols are commonly used for content ingestion, each suited to different types of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to reduce its file size while maintaining quality, using various codecs that will be investigated in Section 3. After the encoding process, the encoded video is packaged in formats that can be efficiently delivered over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles, audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adapti

**[Modelo / arquitectura / algoritmo | extracto 13 | p.5]**

prepared for streaming. Several protocols are commonly used for content ingestion, each suited to different types of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to reduce its file size while maintaining quality, using various codecs that will be investigated in Section 3. After the encoding process, the encoded video is packaged in formats that can be efficiently delivered over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles, audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adaptive streaming and other advanced features [8]. —Content Delivery Network (CDN). The third phase focuses on distributing video segments and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 e

**[Modelo / arquitectura / algoritmo | extracto 14 | p.6]**

racy of earlier standards. Motion vectors can now extend beyond picture boundaries, and multiple reference pictures can be used for motion compensation, enhancing prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in encoding, while weighted prediction and improved motion inference further refine the compression process. Additional innovations include directional spatial prediction for intra-coding, in-the-loop deblocking filtering to reduce artifacts, and a smaller block-size transform for more localized signal representation. The introduction of hierarchical and short word-length transforms, exact-match inverse transforms, and advanced entropy coding methods like Context-Based Adaptive Binary Arithmetic Coding (CABAC) further boost efficiency. To enhance robustness and adaptability across network environments, AVC includes features such as parameter set structures, flexible slice sizes, flexible macroblock ordering, arbitrary slice ordering, redundant pictures, and data ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Modelo / arquitectura / algoritmo | extracto 15 | p.7]**

tions and new interpolation filters. Additionally, VVC enhances inter-frame prediction with improved motion vector coding, subblock-level motion prediction, and horizontal wrap- around for immersive formats. Extended transform and quantization techniques in VVC improve residual compression and adaptive quantization control, building upon HEVC’s capabilities to further enhance efficiency and quality. MPEG and ITU-T have jointly developed AVC, HEVC, and VVC standards, representing successive generations of video compression technology. In parallel, video codecs like VP9 and AV1 [53], developed by Google and the Alliance for Open Media, respectively, offer alternative approaches with a focus on open standards and royalty-free solutions. Looking ahead, the next generation of video codecs is anticipated to be driven by advances in Deep Neural Networks (DNNs), which promise to further enhance compression efficiency and video quality through machine learning techniques. Currently, two main exploration paths are being pursued: one focuses on replacing components of traditional codecs with DNNs while maintaining the same overall structure, and the other explores fully end-to-end neural network-based approaches. These developments aim to push the boundaries of video coding by leveraging AI-driven methods to optimize encoding and decoding processes in ways that traditional techniques may not achieve. Despite SVC [100] being highlighted as a promising method for HAS in studies such as [55, 83, 98], there has been a notable decline in its adoption or further exploration by both industrial practitioners and academic researchers in subsequent years. ACM Trans. Multimedia Comput. Commun. Appl.,

**[Modelo / arquitectura / algoritmo | extracto 16 | p.7]**

r directions and new interpolation filters. Additionally, VVC enhances inter-frame prediction with improved motion vector coding, subblock-level motion prediction, and horizontal wrap- around for immersive formats. Extended transform and quantization techniques in VVC improve residual compression and adaptive quantization control, building upon HEVC’s capabilities to further enhance efficiency and quality. MPEG and ITU-T have jointly developed AVC, HEVC, and VVC standards, representing successive generations of video compression technology. In parallel, video codecs like VP9 and AV1 [53], developed by Google and the Alliance for Open Media, respectively, offer alternative approaches with a focus on open standards and royalty-free solutions. Looking ahead, the next generation of video codecs is anticipated to be driven by advances in Deep Neural Networks (DNNs), which promise to further enhance compression efficiency and video quality through machine learning techniques. Currently, two main exploration paths are being pursued: one focuses on replacing components of traditional codecs with DNNs while maintaining the same overall structure, and the other explores fully end-to-end neural network-based approaches. These developments aim to push the boundaries of video coding by leveraging AI-driven methods to optimize encoding and decoding processes in ways that traditional techniques may not achieve. Despite SVC [100] being highlighted as a promising method for HAS in studies such as [55, 83, 98], there has been a notable decline in its adoption or further exploration by both industrial practitioners and academic researchers in subsequent years. ACM Trans. Multimedia Comput. Commun

### 5.x Estado / inputs / features

**[Estado / inputs / features | extracto 1 | p.1]**

Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM Trans. Multimedia Comput. Commun. Appl. 21, 7, Article 198 (July 2025), 27 pages. https://doi.org/10.1145/3736306 Authors’ Contact Information: Christian

**[Estado / inputs / features | extracto 2 | p.1]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges CHRISTIAN TIMMERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in ada

**[Estado / inputs / features | extracto 3 | p.2]**

198:2 C. Timmerer et al. 1 Introduction Over the last 20 years, video streaming has surged in popularity and now constitutes over more than half of global Internet traffic [99]. This trend can be attributed in part to advancements in video compression technologies, such as Advanced Video Coding (AVC) (2003) [122], High Effi- ciency Video Coding (HEVC) (2013) [108], and Versatile Video Coding (VVC) (2020) [30, 31]. Each new generation of video codecs offers more than a 50% improvement in bitrate and qual- ity, respectively. Additionally, developments in networking technology comply with Nielsen’s law of bandwidth, which asserts that “a high-end user’s connection speed grows by 50% per year” [88]. When combined with the increasing computational power of user devices (cf. Moore’s law), this allows for the creation and consumption of video content anywhere and at any time across various devices. Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based, unicast schemes utilizing existing Web-based infras- tructure to allow for better scalability. When referring to this streaming approach, we use the term HTTP Adaptive Streaming (HAS)1 consistently throughout this article. Standards helped facilitate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and Apple HTTP Live Streaming (HLS), although standards typically specify normative formats (i.e., bitstr

**[Estado / inputs / features | extracto 4 | p.2]**

d facilitate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and Apple HTTP Live Streaming (HLS), although standards typically specify normative formats (i.e., bitstream syntax) only, leaving non-normative parts open for (industry) competition. The research community can play a crucial role in this ecosystem by researching innovative solutions, specifically targeting non-normative aspects within these specifications. In this article, our aim is to provide a brief (historical) background of HAS and a comprehensive overview of research efforts related to key phases in modern HAS workflows; ranging from (i) video encoding, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including Quality of Experience (QoE). For each of these phases, we will outline basic principles, current trends, and future challenges for HAS. The structure of this article is as follows. Section 2 covers the early history of video streaming on the Internet, the rise of HAS and its fundamental principles, a brief summary of international standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for HAS, including per-title encoding and recent optimizations, as well as energy-related concerns. Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Sectio

**[Estado / inputs / features | extracto 5 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send the file as fast as possible. —Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The server paces transmission based on encoding rate. —Chunked streaming divides the content into short-duration chunks which enables live stream- ing and ad insertion. —Adaptive streaming facilitates multiple versions of the content that enables to adapt to network and device conditions.

**[Estado / inputs / features | extracto 6 | p.3]**

g basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The server paces transmission based on encoding rate. —Chunked streaming divides the content into short-duration chunks which enables live stream- ing and ad insertion. —Adaptive streaming facilitates multiple versions of the content that enables to adapt to network and device conditions. The latter two can be used jointly and collectively referred to as HAS; pseudo streaming is not used anymore, but progressive download is still used as a fallback mechanism. In the following, we will briefly describe the main principles of HAS and provide an overview of the standardization landscape. 2.2 HAS: Basic Principles The basic principles of HAS are shown in Figure 1, comprising an HTTP server that hosts the video content, a network with variable bandwidth conditions, and clients rendering the requested video for the end users. The video content is typically segmented over time (e.g., a few seconds per segment) and provided in multiple versions (e.g., resolutions, frame rates, bitrates, qualities, codecs, languages) referred to as bitrate ladder. In addition to the segments, a manifest is pro- vided that enables smart clients to issue timed HTTP requests for individual segments (or parts thereof) from one of the multiple versions provided at the server, depending on the clients’ context conditions including—but not limited to—device characteristics, network conditions, and user pref- erences in order to maximize QoE. An important design choice comprises that servers host those segments and its manifest, and clients decide which segments to request when. Thus, clients imple- ment an ABR alg

**[Estado / inputs / features | extracto 7 | p.3]**

: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send the file as fast as possible. —Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The server paces transmission based on encoding rate. —Chunked streaming divides the content into short-duration chunks which enables live stream- ing and ad insertion. —Adaptive streaming facilitates multiple versions of the content that enables to adapt to network and device conditions. The latter two can be used jointly and collectively referred to as HAS; pseudo streaming is not used anymore, but progressive download is still used as a fallback mechanism. In the following, we will briefly describe the main principles of HAS and pro

**[Estado / inputs / features | extracto 8 | p.3]**

e introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send the file as fast as possible. —Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The server paces transmission based on encoding rate. —Chunked streaming divides the content into short-duration chunks which enables live stream- ing and ad insertion. —Adaptive streaming facilitates multiple versions of the content that enables to adapt to network and device conditions. The latter two can be used jointly and collectively referred to as HAS; pseudo streaming is not used anymore, but progressive download is still used as a fallback mechanism. In the following, we will briefly describe the main principles of HAS and provide an overview of the standardization landscape. 2.2 HAS: Basic Principles The basic principles of HAS are shown in Figure 1, comprising an HTTP server that hosts the video content, a network with variable bandwidth conditions, and clients rendering the requested video for the end users. The video content is typically segmented over time (e.g., a few seconds per se

**[Estado / inputs / features | extracto 9 | p.3]**

n principles of HAS and provide an overview of the standardization landscape. 2.2 HAS: Basic Principles The basic principles of HAS are shown in Figure 1, comprising an HTTP server that hosts the video content, a network with variable bandwidth conditions, and clients rendering the requested video for the end users. The video content is typically segmented over time (e.g., a few seconds per segment) and provided in multiple versions (e.g., resolutions, frame rates, bitrates, qualities, codecs, languages) referred to as bitrate ladder. In addition to the segments, a manifest is pro- vided that enables smart clients to issue timed HTTP requests for individual segments (or parts thereof) from one of the multiple versions provided at the server, depending on the clients’ context conditions including—but not limited to—device characteristics, network conditions, and user pref- erences in order to maximize QoE. An important design choice comprises that servers host those segments and its manifest, and clients decide which segments to request when. Thus, clients imple- ment an ABR algorithm, not normatively specified within existing standards, subject to research and development. 2.3 Overview of HAS Standards The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which replaced prior proprietary formats such as Microsoft Smooth Streaming and Adobe HDS. Both standards define formats allowing implementation of the basic HAS principles as outlined above with (minor) differences with respect to segment and manifest formats. The MPEG DASH data model is shown in Figure 2 which comprises an XML-based Media Presentation Description as manifest and allows the video c

**[Estado / inputs / features | extracto 10 | p.4]**

198:4 C. Timmerer et al. Fig. 1. Basic principles of HAS. Fig. 2. MPEG DASH data model. Each period comprises multiple adaptation sets of different modalities (e.g., video, audio, subtitles) for component selection by clients. Each adaptation set provides multiple representations of the same content with various characteristics (e.g., resolution, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g., the source element) to allow JavaScript to generate media streams for playback, whereby an ABR algorithm could be implemented in JavaScript [92]. In general, DASH and HLS can be used interchangeably without impacting the performance of video streaming services [24]. 2.4 End-to-End Video Streaming Workflow End-to-end video streaming refers to the ent

**[Estado / inputs / features | extracto 11 | p.5]**

kers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adaptive streaming and other advanced features [8]. —Content Delivery Network (CDN). The third phase focuses on distributing video segments and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player determines the quality of next segment to be downloaded. In Section 5, we will introduce various types of ABR algorithms. The device decodes the requested video stream and plays it back to the user. The video is rendered on the device’s display, and the quality of this rendering depends on the device’s capabilities, including screen resolution, processing power, and software optimizations. In this article, particular attention will be paid to video as a primary focus, given the preponder- ance of existing resea

**[Estado / inputs / features | extracto 12 | p.5]**

ssaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to reduce its file size while maintaining quality, using various codecs that will be investigated in Section 3. After the encoding process, the encoded video is packaged in formats that can be efficiently delivered over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles, audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adaptive streaming and other advanced features [8]. —Content Delivery Network (CDN). The third phase focuses on distributing video segments and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s

**[Estado / inputs / features | extracto 13 | p.5]**

fic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player determines the quality of next segment to be downloaded. In Section 5, we will introduce various types of ABR algorithms. The device decodes the requested video stream and plays it back to the user. The video is rendered on the device’s display, and the quality of this rendering depends on the device’s capabilities, including screen resolution, processing power, and software optimizations. In this article, particular attention will be paid to video as a primary focus, given the preponder- ance of existing research articles centered on HAS and video. However, this emphasis should not overshadow the significance of other modalities, which remain crucial areas of study: these include, but are not limited to, audio, subtitles, haptics, and mulsemedia. In particular, audio st

**[Estado / inputs / features | extracto 14 | p.5]**

to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player determines the quality of next segment to be downloaded. In Section 5, we will introduce various types of ABR algorithms. The device decodes the requested video stream and plays it back to the user. The video is rendered on the device’s display, and the quality of this rendering depends on the device’s capabilities, including screen resolution, processing power, and software optimizations. In this article, particular attention will be paid to video as a primary focus, given the preponder- ance of existing research articles centered on HAS and video. However, this emphasis should not overshadow the significance of other modalities, which remain crucial areas of study: these include, but are not limited to, audio, subtitles, haptics, and mulsemedia. In particular, audio streaming in conjunction with HAS is

**[Estado / inputs / features | extracto 15 | p.5]**

rsed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player determines the quality of next segment to be downloaded. In Section 5, we will introduce various types of ABR algorithms. The device decodes the requested video stream and plays it back to the user. The video is rendered on the device’s display, and the quality of this rendering depends on the device’s capabilities, including screen resolution, processing power, and software optimizations. In this article, particular attention will be paid to video as a primary focus, given the preponder- ance of existing research articles centered on HAS and video. However, this emphasis should not overshadow the significance of other modalities, which remain crucial areas of study: these include, but are not limited to, audio, subtitles, haptics, and mulsemedia. In particular, audio streaming in conjunction with HAS is covered in [37, 95]. The integration of subtitles in HAS, as explored in ACM Trans. Mul

**[Estado / inputs / features | extracto 16 | p.5]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:5 Fig. 3. Main phases of the end-to-end video streaming workflow. content is captured using cameras or created using digital tools. Once created, the video is ingested into the streaming platform’s infrastructure. Content ingestion involves uploading or feeding the video data into the system, where it can be processed and prepared for streaming. Several protocols are commonly used for content ingestion, each suited to different types of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are s

### 5.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

enges CHRISTIAN TIMMERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances

**[Acción / decisión ABR | extracto 2 | p.2]**

198:2 C. Timmerer et al. 1 Introduction Over the last 20 years, video streaming has surged in popularity and now constitutes over more than half of global Internet traffic [99]. This trend can be attributed in part to advancements in video compression technologies, such as Advanced Video Coding (AVC) (2003) [122], High Effi- ciency Video Coding (HEVC) (2013) [108], and Versatile Video Coding (VVC) (2020) [30, 31]. Each new generation of video codecs offers more than a 50% improvement in bitrate and qual- ity, respectively. Additionally, developments in networking technology comply with Nielsen’s law of bandwidth, which asserts that “a high-end user’s connection speed grows by 50% per year” [88]. When combined with the increasing computational power of user devices (cf. Moore’s law), this allows for the creation and consumption of video content anywhere and at any time across various devices. Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based, unicast schemes utilizing existing Web-based infras- tructure to allow for better scalability. When referring to this streaming approach, we use the term HTTP Adaptive Streaming (HAS)1 consistently throughout this article. Standards helped facilitate this process, notably MPEG Dynamic Adaptive Streaming ov

**[Acción / decisión ABR | extracto 3 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send the file as fast as possible. —Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The server paces transmission based on encoding rate. —Chunked streaming divides the content into short-duration chunks which enables live stream- ing and ad insertion. —Adaptive streaming facilitates multiple versions of the content that enables to adapt to network and device conditions. The latter two can be used jointly

**[Acción / decisión ABR | extracto 4 | p.4]**

198:4 C. Timmerer et al. Fig. 1. Basic principles of HAS. Fig. 2. MPEG DASH data model. Each period comprises multiple adaptation sets of different modalities (e.g., video, audio, subtitles) for component selection by clients. Each adaptation set provides multiple representations of the same content with various characteristics (e.g., resolution, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g., the source element) to allow JavaScript to generate media streams for playback, whereby an ABR algorithm could be implemented in JavaScript [92]. In general, DASH and HLS can be used interchangeably without impacting the performan

**[Acción / decisión ABR | extracto 5 | p.5]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:5 Fig. 3. Main phases of the end-to-end video streaming workflow. content is captured using cameras or created using digital tools. Once created, the video is ingested into the streaming platform’s infrastructure. Content ingestion involves uploading or feeding the video data into the system, where it can be processed and prepared for streaming. Several protocols are commonly used for content ingestion, each suited to different types of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to reduce its file size while maintaining quality, using various codecs that will be investigated in Section 3. After the encoding process, the encoded video is packaged in formats that can be efficiently delivered over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles, audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adaptive streaming and other advanced features [8]. —Content Delivery Network (CDN). The third phase focuses on distributing video segments and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically disperse

**[Acción / decisión ABR | extracto 6 | p.6]**

198:6 C. Timmerer et al. [36], further expands the scope of audiovisual communication. Additionally, the rapidly growing interest in haptics and mulsemedia, as evidenced by works like [134] and [26], underscores the diverse research landscape beyond video. 3 Video Coding for HAS Video coding or compression is the core of video streaming, where uncompressed video is com- pressed to fit the available bandwidth. Over decades, video codecs have evolved into sophisticated systems that achieve a delicate balance between quality and efficiency. In Section 3.1, we review the current state of video codecs. In Section 3.2, we will examine advancements in bitrate ladder optimization. Additionally, while improving video codec efficiency, there is often an increase in power consumption. Section 3.3 will explore the tradeoffs between compression efficiency and energy consumption. 3.1 Overview of Video Codecs A video codec is a sophisticated compression system that combines various techniques to effi- ciently reduce the size of video data while maintaining high visual quality. It integrates both spatial and temporal compression methods to exploit redundancies within and between video frames. The process begins with partitioning, where each video frame is divided into smaller blocks for more precise processing. Intra-frame prediction compresses individual blocks based on previously encoded blocks within the same frame, exploiting temporal redundancy, while inter-frame predic- tion enhances compression

**[Acción / decisión ABR | extracto 7 | p.6]**

ral enhancements over prior video coding methods to improve coding efficiency. These include variable block-size motion compensation, allowing for flexible and smaller block sizes down to 4 × 4 pixels, and quarter-sample-accurate motion compensation, improving on the half-sample accuracy of earlier standards. Motion vectors can now extend beyond picture boundaries, and multiple reference pictures can be used for motion compensation, enhancing prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in encoding, while weighted prediction and improved motion inference further refine the compression process. Additional innovations include directional spatial prediction for intra-coding, in-the-loop deblocking filtering to reduce artifacts, and a smaller block-size transform for more localized signal representation. The introduction of hierarchical and short word-length transforms, exact-match inverse transforms, and advanced entropy coding methods like Context-Based Adaptive Binary Arithmetic Coding (CABAC) further boost efficiency. To enhance robustness and adaptability across network environments, AVC includes features such as parameter set structures, flexible slice sizes, flexible macroblock ordering, arbitrary slice ordering, redundant pictures, and data ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Acción / decisión ABR | extracto 8 | p.7]**

ructured bitstreams, parameter sets, and an emphasis on advanced functionalities such as random access and scalability. VVC introduces several sophisticated features to enhance coding efficiency and flexibility: random access is facilitated, which helps balance coding efficiency with end-to-end delay; reference picture resampling allows for resolution adjustments in inter-coded pictures to improve efficiency; and new subpicture and virtual boundary features provide enhanced flexibility for immersive and specialized video formats, such as 360-degree video. VVC also refines the use of CTUs, slices, tiles, and wavefronts to optimize processing and access. The standard supports Scalable Video Coding (SVC) with temporal, quality, spatial, and multiview scalability, simplifying the design compared to previous standards, and facilitating easier adaptation for various applications. Key advancements include more flexible block partitioning with larger sizes and varied shapes, separate partitioning for luma and chroma, and innovations in intra-frame prediction with finer angular directions and new interpolation filters. Additionally, VVC enhances inter-frame prediction with improved motion vector coding, subblock-level motion prediction, and horizontal wrap- around for immersive formats. Extended transform and quantization techniques in VVC improve residual compression and adaptive quantization control, building upon HEVC’s capabilities to further enhance efficiency and quality. MPEG and ITU-T have jointly developed AVC, HEVC, and VVC standards, representing successive generations of video compression technology. In parallel, video codecs like VP9 and AV1 [53], developed by Google and the Al

**[Acción / decisión ABR | extracto 9 | p.8]**

198:8 C. Timmerer et al. 3.2 From Static Bitrate Ladders to Dynamic, Live Per-Title Encoding To allow clients to adapt to fluctuating network conditions, the same video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in

**[Acción / decisión ABR | extracto 10 | p.8]**

e number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the best possible way while minimizing unnecessary bandwidth usage. Various methods have been proposed to optimize bitrate ladders. For instance, Tashtarian et al. [112] introduced a method where the desired bitrate requests of all users are collected and used to optimize the bitrates in the ladder. By analyzing the probabi

**[Acción / decisión ABR | extracto 11 | p.8]**

essary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the best possible way while minimizing unnecessary bandwidth usage. Various methods have been proposed to optimize bitrate ladders. For instance, Tashtarian et al. [112] introduced a method where the desired bitrate requests of all users are collected and used to optimize the bitrates in the ladder. By analyzing the probability distribution of these desired bitrates, the bitrates are selected to construct a more efficient and tailored bitrate ladder, ensuring that the encoded video representations better match the users’ needs and network conditions. However, this method requires a modification in the ABR algorithm of the clients. To address this issue, ARTEMIS [111] proposes a mega bitrate ladder, where a large number of representations are made available to clients, allowing them to select their desired representations. In this approach, not all the representations in the mega ladder are encoded initially; instead, they are used to gather data on users’ bandwidth requirements. Based on the probability distribution of these requirements, a more efficient set of representations is selected for encoding, optimizing the video streaming process to better align with the actual user demands. Similarly, COBIRAS [102] utilizes a b

**[Acción / decisión ABR | extracto 12 | p.9]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:9 resolution in the bitrate ladder. A similar approach is employed by Amirpour et al. [17], where not only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add dynamic range as an additional dimension for optimization. While the above-mentioned methods typically rely on a brute-force approach to determine optimal encoding parameters, such as resolution, other methods aim to predict these parameters more efficiently. These predictive approaches are particularly valuable for live video streaming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These pr

**[Acción / decisión ABR | extracto 13 | p.9]**

e a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These predictions often utilize video complexity features, with methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning- based methods to predict encoding parameters, showcasing the potential of AI-driven approaches in optimizing live video streaming. 3.3 Energy Efficiency in Video Coding The energy consumption of video encoding is influenced by multiple factors, including codec selection and encoding parameter configurations. Additionally, HAS encodes videos in multiple representations (bitrate ladder), typically a computationally intensive process. Encoding complexity directly correlates with energy consumption [63] due to the higher compu- tational power required for intricate algorithms and calculations. Each codec generation achieves approximately 50% coding efficiency gain over the previous generation, at the cost of increased computational complexity, longer encoding times, and higher energy consumption [96]. For exam- ple, AVC consumes over four times more power than earlier standards like MJPEG and MPEG-4 Part 2, due to more and refined compression techniques such as multiple reference frames in AVC [103, 119]. HEVC further enhances compression efficiency by 25.1% over AVC but also increases energy consumption by 17.4% [81]. Search Range (SR), a crucial parameter in ME, significantly contributes to this higher

**[Acción / decisión ABR | extracto 14 | p.9]**

aming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These predictions often utilize video complexity features, with methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning- based methods to predict encoding parameters, showcasing the potential of AI-driven approaches in optimizing live video streaming. 3.3 Energy Efficiency in Video Coding The energy consumption of video encoding is influenced by multiple factors, including codec selection and encoding parameter configurations. Additionally, HAS encodes videos in multiple representations (bitrate ladder), typically a computationally intensive process. Encoding complexity directly correlates with energy consumption [63] due to the higher compu- tational power required for intricate algorithms and calculations. Each codec generation achieves approximately 50% coding efficiency gain over the previous generation, at the cost of increased computational complexity, longer encoding times, and higher energy consumption [96]. For exam- ple, AVC consumes over four times more power than earlier standards like MJPEG and MPEG-4 Part 2, due to more and refined compression techniques such as multiple reference frames in AVC [103, 119]. HEVC further enhances compression efficiency by 25.1% over AVC but also increases energy consumption

**[Acción / decisión ABR | extracto 15 | p.9]**

t, AV1 offers a better tradeoff between coding efficiency and energy consumption compared to AVC, HEVC, VP9, and VVC [32]. Encoding parameters significantly influence energy consumption [80]. Resolution directly impacts energy consumption, with a linear relationship between pixel count and energy consumption. Frame rate directly correlates with energy consumption due to increased computational demands. Consequently, doubling the resolution while halving the frame rate maintains energy consumption. Presets (AVC, HEVC, and VVC) and speed settings (AV1 and VP9) determine the tradeoff between the encoding speed and the compression efficiency [14, 32, 105]. Higher quality settings (i.e., slower presets and lower speed settings) increase encoding time and energy consumption due to more complex tools and extensive search spaces [80] explored to choose the most efficient coding configurations [32]. For example, Silveira et al. [105] observed a 45-fold energy consumption increase when moving from the ultrafast to placebo x265 preset, with a corresponding 145% energy increase per 1% bitrate reduction. Notably, different quantization parameter configurations have an exponential impact on power consumption [103]. Other encoding parameters, such as the number of reference frames, SR, subpixel accuracy, and the ME algorithm significantly influence power consumption, with variations up to 10% reported in [103]. Monteiro et al. [81] found that while the ME range minimally affects the compression efficiency in HEVC, energy consumption increases disproportionately with increased ME range. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Acción / decisión ABR | extracto 16 | p.10]**

198:10 C. Timmerer et al. HAS bitrate ladder construction is computationally expensive. Eliminating perceptually redundant representations through VMAF score comparison and removal of higher bitrate representations when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder construction, considering the content type and user-perceived quality metrics, can further optimize energy efficiency by reducing unnecessary bitrates while maintaining video quality [68]. Video encoding distribution in the computing continuum addresses computational challenges by distributing video encoding tasks across multiple instances in cloud and fog infrastructures. Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding tasks in geographically distributed cloud data centers, optimizing total time and energy consump- t

### 5.x Reward / QoE / objetivo

**[Reward / QoE / objetivo | extracto 1 | p.1]**

RZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM Trans. Multi

**[Reward / QoE / objetivo | extracto 2 | p.1]**

ERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM Trans.

**[Reward / QoE / objetivo | extracto 3 | p.2]**

m HTTP Adaptive Streaming (HAS)1 consistently throughout this article. Standards helped facilitate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and Apple HTTP Live Streaming (HLS), although standards typically specify normative formats (i.e., bitstream syntax) only, leaving non-normative parts open for (industry) competition. The research community can play a crucial role in this ecosystem by researching innovative solutions, specifically targeting non-normative aspects within these specifications. In this article, our aim is to provide a brief (historical) background of HAS and a comprehensive overview of research efforts related to key phases in modern HAS workflows; ranging from (i) video encoding, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including Quality of Experience (QoE). For each of these phases, we will outline basic principles, current trends, and future challenges for HAS. The structure of this article is as follows. Section 2 covers the early history of video streaming on the Internet, the rise of HAS and its fundamental principles, a brief summary of international standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for HAS, including per-title encoding and recent optimizations, as well as energy-related concerns. Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE

**[Reward / QoE / objetivo | extracto 4 | p.2]**

pproach, we use the term HTTP Adaptive Streaming (HAS)1 consistently throughout this article. Standards helped facilitate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and Apple HTTP Live Streaming (HLS), although standards typically specify normative formats (i.e., bitstream syntax) only, leaving non-normative parts open for (industry) competition. The research community can play a crucial role in this ecosystem by researching innovative solutions, specifically targeting non-normative aspects within these specifications. In this article, our aim is to provide a brief (historical) background of HAS and a comprehensive overview of research efforts related to key phases in modern HAS workflows; ranging from (i) video encoding, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including Quality of Experience (QoE). For each of these phases, we will outline basic principles, current trends, and future challenges for HAS. The structure of this article is as follows. Section 2 covers the early history of video streaming on the Internet, the rise of HAS and its fundamental principles, a brief summary of international standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for HAS, including per-title encoding and recent optimizations, as well as energy-related concerns. Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including

**[Reward / QoE / objetivo | extracto 5 | p.2]**

streaming on the Internet dates back to the last decade of the previous century, when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994 [56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming event in 1995 with the Seattle Mariners vs. New York Yankees resulting in RealSystem G2 SureStream technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe adaptive streaming within the 3GPP packet-switched streaming service that uses the Real-Time Streaming Protocol, Session Description Protocol, and Real-Time Transfer Protocol (RTP) for the setup and streaming phases of a streaming session. The Real-Time Control Protocol is used to 1Other terms often used interchangeably or in specific contexts are ABR streaming, DASH, HLS, Smooth Streaming, HTTP Dynamic Streaming (HDS), Over-The-Top streaming, segmented HTTP streaming, Adaptive HTTP Streaming, and so on. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Reward / QoE / objetivo | extracto 6 | p.2]**

using on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Section 8 wraps up the article. 2 Background 2.1 A Brief History of Video Streaming The era of video streaming on the Internet dates back to the last decade of the previous century, when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994 [56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming event in 1995 with the Seattle Mariners vs. New York Yankees resulting in RealSystem G2 SureStream technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe adaptive streaming within the 3GPP packet-switched streaming service that uses the Real-Time Streaming Protocol, Session Description Protocol, and Real-Time Transfer Protocol (RTP) for the setup and streaming phases of a streaming session. The Real-Time Control Protocol is used to 1Other terms often used interchangeably or in specific contexts are ABR streaming, DASH, HLS, Smooth Streaming, HTTP Dynamic Streaming (HDS), Over-The-Top streaming, segmented HTTP streaming, Adaptive HTTP Streaming, and so on. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Reward / QoE / objetivo | extracto 7 | p.3]**

on landscape. 2.2 HAS: Basic Principles The basic principles of HAS are shown in Figure 1, comprising an HTTP server that hosts the video content, a network with variable bandwidth conditions, and clients rendering the requested video for the end users. The video content is typically segmented over time (e.g., a few seconds per segment) and provided in multiple versions (e.g., resolutions, frame rates, bitrates, qualities, codecs, languages) referred to as bitrate ladder. In addition to the segments, a manifest is pro- vided that enables smart clients to issue timed HTTP requests for individual segments (or parts thereof) from one of the multiple versions provided at the server, depending on the clients’ context conditions including—but not limited to—device characteristics, network conditions, and user pref- erences in order to maximize QoE. An important design choice comprises that servers host those segments and its manifest, and clients decide which segments to request when. Thus, clients imple- ment an ABR algorithm, not normatively specified within existing standards, subject to research and development. 2.3 Overview of HAS Standards The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which replaced prior proprietary formats such as Microsoft Smooth Streaming and Adobe HDS. Both standards define formats allowing implementation of the basic HAS principles as outlined above with (minor) differences with respect to segment and manifest formats. The MPEG DASH data model is shown in Figure 2 which comprises an XML-based Media Presentation Description as manifest and allows the video content to be divided into periods for content slic

**[Reward / QoE / objetivo | extracto 8 | p.3]**

bitrate ladder. In addition to the segments, a manifest is pro- vided that enables smart clients to issue timed HTTP requests for individual segments (or parts thereof) from one of the multiple versions provided at the server, depending on the clients’ context conditions including—but not limited to—device characteristics, network conditions, and user pref- erences in order to maximize QoE. An important design choice comprises that servers host those segments and its manifest, and clients decide which segments to request when. Thus, clients imple- ment an ABR algorithm, not normatively specified within existing standards, subject to research and development. 2.3 Overview of HAS Standards The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which replaced prior proprietary formats such as Microsoft Smooth Streaming and Adobe HDS. Both standards define formats allowing implementation of the basic HAS principles as outlined above with (minor) differences with respect to segment and manifest formats. The MPEG DASH data model is shown in Figure 2 which comprises an XML-based Media Presentation Description as manifest and allows the video content to be divided into periods for content slicing including ad support. 2We note that HAS is typically deployed via TCP for HTTP/1.1 and HTTP/2 unless explicitly mentioned for HTTP/3 or QUIC which uses UDP. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Reward / QoE / objetivo | extracto 9 | p.5]**

ase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to reduce its file size while maintaining quality, using various codecs that will be investigated in Section 3. After the encoding process, the encoded video is packaged in formats that can be efficiently delivered over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles, audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adaptive streaming and other advanced features [8]. —Content Delivery Network (CDN). The third phase focuses on distributing video segments and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the

**[Reward / QoE / objetivo | extracto 10 | p.8]**

oded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the best possible way while minimizing unne

**[Reward / QoE / objetivo | extracto 11 | p.8]**

video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the best possible way while minimizi

**[Reward / QoE / objetivo | extracto 12 | p.8]**

tion of these requirements, a more efficient set of representations is selected for encoding, optimizing the video streaming process to better align with the actual user demands. Similarly, COBIRAS [102] utilizes a bitrate slide and just-in-time encoding to request segments with any arbitrary bit rate together with a novel ABR algorithm. Some methods focus exclusively on the quality of representations when constructing a bitrate ladder, employing the concept of Just Noticeable Difference (JND). JND represents the smallest variation in quality that an average viewer can detect. These methods construct a bitrate ladder by including only those representations where the quality difference is perceptible, thereby reducing redundancy and optimizing the selection of representations. For instance, in terms of Video Multimethod Assessment Fusion (VMAF) [1], the JND is typically around six points, meaning that a quality difference of six VMAF units between two representations is noticeable to viewers. If the difference is less than six VMAF units, the two representations appear similar in quality [15, 132]. By carefully selecting representations based on this JND threshold, these approaches ensure that each step on the ladder reflects a significant improvement or decline in quality, thus enhancing both streaming efficiency and viewer experience [18, 78]. Other methods focus on optimizing encoding parameters beyond bitrate. De Cock et al. [39] encode a video at multiple bitrates and resolutions with quality assessments performed for each, and then the resolution that delivers the highest quality for each bitrate is selected, optimizing the ACM Trans. Multimedia Comput. Commun. Appl., Vo

**[Reward / QoE / objetivo | extracto 13 | p.10]**

y, and manageability of streaming applications. In the following, we briefly describe these functions and their evolution over the past two decades. Caching. Caching in the network is a major component that increases the scalability of video streaming applications. Caching hierarchies of CDNs take the load of the content provider’s origin server by caching hot objects [33, 74], specifically, hot video segments in the case of HAS. While the term hot video segments is not well defined, it usually refers to the segments that are being requested the most and especially are more likely to be requested in the future. In terms of performance and scalability, caching systems are measured through user- and content provider-facing metrics as well as internal metrics. The first category comprises metrics that directly influence the user experience (QoE), e.g., the round-trip delay from requesting the video segment until receiving it. Provider-facing metrics include, for example, the offloading ratio, i.e., the ratio of requests or traffic that are serviced by the caching hierarchy to the number of overall requests or data traffic. Finally, internal performance metrics of CDNs include the storage utilization of caches, ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Reward / QoE / objetivo | extracto 14 | p.10]**

198:10 C. Timmerer et al. HAS bitrate ladder construction is computationally expensive. Eliminating perceptually redundant representations through VMAF score comparison and removal of higher bitrate representations when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder construction, considering the content type and user-perceived quality metrics, can further optimize energy efficiency by reducing unnecessary bitrates while maintaining video quality [68]. Video encoding distribution in the computing continuum addresses computational challenges by distributing video encoding tasks across multiple instances in cloud and fog infrastructures. Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding tasks in geographically distributed cloud data centers, optimizing total time and energy consump- tion. The scheduler estimates performance metrics for each data center task assignment considering network distances, server capacity, and workload, potentially using Pareto optimality for efficient video transcoding in the cloud. MAPO [76] utilizes a genetic multi-objective optimization algorithm to determine task placement on fog instances, optimizing total time, energy consumption, and price. VE-MATCH [4] proposes a matching game-based task scheduling approach to optimize resource allocation between media and resource providers. GreenFog [84] optimizes energy use by utilizing renewable energy sources for fog computing. The framework employs optimization techniques, including a heuristic

**[Reward / QoE / objetivo | extracto 15 | p.11]**

a segment is requested vs. works that update the cache content on a discrete-time basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching systems is in general a complex problem which does not easily lend itself to analytical closed-form results. To this end, several model-free methods exist that utilize the metadata observed from the segment request processes to learn good cache content decisions or continuously optimize the content admission and retention policy. Software-Defined Networking (SDN) Support/Server and Network-Assisted DASH (SAND). With the emergence of SDN, new video distribution methods were introduced that incorporated in-network functionalities, diverging from the traditional end-to-end model of the Internet. The common goal of these approaches is to increase the viewers’ QoE by assisting clients in the appropriate selection of DASH segments’ representations. Cofano et al. [35] were among the first to propose a network-assisted approach that uses SDN to provide QoE fairness between DASH clients. An approach that uses SDN to facilitate bitrate adaptation support for DASH clients was introduced by Kleinrouweler et al. [67]. Similarly, SDNDASH [19] presents an SDN-supported resource allocation and management approach that also aims to maximize the QoE of the client. SAND is an MPEG standard [59] that was introduced to enable communication between streaming clients and network elements/servers like caches. It offers standard interfaces for the communication between these elements. The goals of SAND are optimized operations with caches, the support of consistent and high-level QoE for viewers, and QoE measurement

**[Reward / QoE / objetivo | extracto 16 | p.12]**

issued by a video player can be served by any cache that holds the content with that exact name of the segment, assuming the cache is located on the path between the client and the origin server. ICN approaches like CCN [60] and NDN [129] propose caching functionality at each router within the network. At first glance, video streaming would tremendously benefit from in-network caching since content (e.g., video segments) can be directly served from routers along the path to the origin. Although ICN has been a prominent research topic over the past decade, any large-scale deployments video streaming applications could benefit from have not been established. Since ICN replaces the IP layer of the current Internet, such a significant change is extremely hard to implement. In addition, the in-network caching approach can lead to significant QoE impairments due to bitrate oscillations, as demonstrated by Grandl et al. [49]. 4.2 Role of Endpoints for HAS Delivery In this section, we discuss the end-to-end support for HAS delivery which is usually found on end-clients as a layer bridging the HAS application and the network stack. Given this architectural view, we categorize this endpoint support into both directions, first in the direction of the HAS client application, i.e., in terms of the interface and the guarantees provided, and secondly into the direction of the network stack in terms of how the network data packets are formed and transmitted to provide these end-to-end guarantees. TCP/QUIC. Coming from the traditional TCP support for HAS, QUIC emerged as a proto- col with a high potential of solving traditional pain points of TCP support for HAS delivery. As Video-on-Demand

### 5.x Entrenamiento / optimización

**[Entrenamiento / optimización | extracto 1 | p.2]**

ons, specifically targeting non-normative aspects within these specifications. In this article, our aim is to provide a brief (historical) background of HAS and a comprehensive overview of research efforts related to key phases in modern HAS workflows; ranging from (i) video encoding, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including Quality of Experience (QoE). For each of these phases, we will outline basic principles, current trends, and future challenges for HAS. The structure of this article is as follows. Section 2 covers the early history of video streaming on the Internet, the rise of HAS and its fundamental principles, a brief summary of international standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for HAS, including per-title encoding and recent optimizations, as well as energy-related concerns. Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Section 8 wraps up the article. 2 Background 2.1 A Brief History of Video Streaming The era of video streaming on the Internet dates back to the last decade of the previous century, when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994 [56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming

**[Entrenamiento / optimización | extracto 2 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send the file as fast as possible. —Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The se

**[Entrenamiento / optimización | extracto 3 | p.5]**

r location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the final phase, the video is received by the end user’s device, a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player determines the quality of next segment to be downloaded. In Section 5, we will introduce various types of ABR algorithms. The device decodes the requested video stream and plays it back to the user. The video is rendered on the device’s display, and the quality of this rendering depends on the device’s capabilities, including screen resolution, processing power, and software optimizations. In this article, particular attention will be paid to video as a primary focus, given the preponder- ance of existing research articles centered on HAS and video. However, this emphasis should not overshadow the significance of other modalities, which remain crucial areas of study: these include, but are not limited to, audio, subtitles, haptics, and mulsemedia. In particular, audio streaming in conjunction with HAS is covered in [37, 95]. The integration of subtitles in HAS, as explored in ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Entrenamiento / optimización | extracto 4 | p.5]**

) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to reduce its file size while maintaining quality, using various codecs that will be investigated in Section 3. After the encoding process, the encoded video is packaged in formats that can be efficiently delivered over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles, audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS [90], CMAF [58]) format that supports adaptive streaming and other advanced features [8]. —Content Delivery Network (CDN). The third phase focuses on distributing video segments and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves spreading the video across a geographically dispersed CDN network (cf. Section 4). —Transmission. The transmission phase in video streaming is a critical component of the end- to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s device. This phase is heavily influenced by network conditions, which can vary widely based on factors such as user location, network congestion, and the type of Internet connection used. Section 4 explores various data transmission protocols and state-of-the-art approaches used in video streaming applications. —Playback and Rendering. In the fin

**[Entrenamiento / optimización | extracto 5 | p.6]**

198:6 C. Timmerer et al. [36], further expands the scope of audiovisual communication. Additionally, the rapidly growing interest in haptics and mulsemedia, as evidenced by works like [134] and [26], underscores the diverse research landscape beyond video. 3 Video Coding for HAS Video coding or compression is the core of video streaming, where uncompressed video is com- pressed to fit the available bandwidth. Over decades, video codecs have evolved into sophisticated systems that achieve a delicate balance between quality and efficiency. In Section 3.1, we review the current state of video codecs. In Section 3.2, we will examine advancements in bitrate ladder optimization. Additionally, while improving video codec efficiency, there is often an increase in power consumption. Section 3.3 will explore the tradeoffs between compression efficiency and energy consumption. 3.1 Overview of Video Codecs A video codec is a sophisticated compression system that combines various techniques to effi- ciently reduce the size of video data while maintaining high visual quality. It integrates both spatial and temporal compression methods to exploit redundancies within and between video frames. The process begins with partitioning, where each video frame is divided into smaller blocks for more precise processing. Intra-frame prediction compresses individual blocks based on previously encoded blocks within the same frame, exploiting temporal redundancy, while inter-frame predic- tion enhances compression by referencing bloc

**[Entrenamiento / optimización | extracto 6 | p.7]**

itudes by using a nonlinear amplitude mapping, further enhancing visual quality. The VVC [31] standard builds on the high-level syntax designs from AVC and HEVC, featuring structured bitstreams, parameter sets, and an emphasis on advanced functionalities such as random access and scalability. VVC introduces several sophisticated features to enhance coding efficiency and flexibility: random access is facilitated, which helps balance coding efficiency with end-to-end delay; reference picture resampling allows for resolution adjustments in inter-coded pictures to improve efficiency; and new subpicture and virtual boundary features provide enhanced flexibility for immersive and specialized video formats, such as 360-degree video. VVC also refines the use of CTUs, slices, tiles, and wavefronts to optimize processing and access. The standard supports Scalable Video Coding (SVC) with temporal, quality, spatial, and multiview scalability, simplifying the design compared to previous standards, and facilitating easier adaptation for various applications. Key advancements include more flexible block partitioning with larger sizes and varied shapes, separate partitioning for luma and chroma, and innovations in intra-frame prediction with finer angular directions and new interpolation filters. Additionally, VVC enhances inter-frame prediction with improved motion vector coding, subblock-level motion prediction, and horizontal wrap- around for immersive formats. Extended transform and quantization techniques in VVC improve residual compression and adaptive quantization control, building upon HEVC’s capabilities to further enhance efficiency and quality. MPEG and ITU-T have jointly develop

**[Entrenamiento / optimización | extracto 7 | p.8]**

ils to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the best possible way while minimizing unnecessary bandwidth usage. Various methods have been proposed to optimize bitrate ladders. For instance, Tashtarian et al. [112] introduced a method where the desired bitrate requests of all users are collected and used to optimize the bitrates in the ladder. By analyzing the probability distribution of these desired bitrates, the bitrates are selected to construct a more efficient and tailored bitrate ladder, ensuring that the encoded video representations better match the users’ needs and network conditions. Howev

**[Entrenamiento / optimización | extracto 8 | p.9]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:9 resolution in the bitrate ladder. A similar approach is employed by Amirpour et al. [17], where not only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add dynamic range as an additional dimension for optimization. While the above-mentioned methods typically rely on a brute-force approach to determine optimal encoding parameters, such as resolution, other methods aim to predict these parameters more efficiently. These predictive approaches are particularly valuable for live video streaming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These predictions often utilize video complexity features, with methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and

**[Entrenamiento / optimización | extracto 9 | p.10]**

construction, considering the content type and user-perceived quality metrics, can further optimize energy efficiency by reducing unnecessary bitrates while maintaining video quality [68]. Video encoding distribution in the computing continuum addresses computational challenges by distributing video encoding tasks across multiple instances in cloud and fog infrastructures. Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding tasks in geographically distributed cloud data centers, optimizing total time and energy consump- tion. The scheduler estimates performance metrics for each data center task assignment considering network distances, server capacity, and workload, potentially using Pareto optimality for efficient video transcoding in the cloud. MAPO [76] utilizes a genetic multi-objective optimization algorithm to determine task placement on fog instances, optimizing total time, energy consumption, and price. VE-MATCH [4] proposes a matching game-based task scheduling approach to optimize resource allocation between media and resource providers. GreenFog [84] optimizes energy use by utilizing renewable energy sources for fog computing. The framework employs optimization techniques, including a heuristic linear regression approach and a machine learning-based Multi- Armed Bandit method. These techniques allow GreenFog to adapt to real-time energy availability. EFFECT [130] introduces an energy-efficient fog computing framework designed for real-time video processing. EFFECT tackles the challenge of balancing energy consumption with latency deadlines employing a two-fold approach. First, a centralized resource allocation scheme distribu

**[Entrenamiento / optimización | extracto 10 | p.10]**

ackles the challenge of balancing energy consumption with latency deadlines employing a two-fold approach. First, a centralized resource allocation scheme distributes sub-channels, transmission, and processing power considering task complexity and deadlines. Second, a distributed game-theoretic approach allows instances to strategically decide between local processing or offloading tasks to fog servers, minimizing their energy footprint. 4 Video Delivery in HAS The significant rise in the popularity of video streaming applications has created challenges for the scalable delivery of multimedia content to viewers. This section discusses various technologies developed to address these challenges, focusing on methods that operate within the network and those that function end-to-end between the content server and the client. 4.1 In-Network Support of HAS Delivery The distribution of video content in today’s Internet heavily relies on in-network functions that increase the scalability, quality, and manageability of streaming applications. In the following, we briefly describe these functions and their evolution over the past two decades. Caching. Caching in the network is a major component that increases the scalability of video streaming applications. Caching hierarchies of CDNs take the load of the content provider’s origin server by caching hot objects [33, 74], specifically, hot video segments in the case of HAS. While the term hot video segments is not well defined, it usually refers to the segments that are being requested the most and especially are more likely to be requested in the future. In terms of performance and scalability, caching systems are measured through user

**[Entrenamiento / optimización | extracto 11 | p.11]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:11 individual cache hit rates as well as the hierarchy hit rate and the midgress, i.e., the traffic sent between caches and caches and the origin server to update the content. Extensive work has been conducted on the evaluation of caching strategies for single (edge caching) systems as well as for entire hierarchies [3, 25, 133]. One main goal of these works is to use the object request patterns to determine which segments are admitted to the cache (and for how long) [48]. Along these lines, one can categorize these works into those that consider capacity- constrained caches vs. those that consider timer-based caches. Additionally, these works can be divided into event-based methods that update their decisions on segment admission and cache content whenever a segment is requested vs. works that update the cache content on a discrete-time basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching systems is in general a complex problem which does not easily lend itself to analytical closed-form results. To this end, several model-free methods exist that utilize the metadata observed from the segment request processes to learn good cache content decisions or continuously optimize the content admission and retention policy. Software-Defined Networking (SDN) Support/Server and Network-Assisted DASH (SAND). With the emergence of SDN, new video distribution met

**[Entrenamiento / optimización | extracto 12 | p.11]**

and the midgress, i.e., the traffic sent between caches and caches and the origin server to update the content. Extensive work has been conducted on the evaluation of caching strategies for single (edge caching) systems as well as for entire hierarchies [3, 25, 133]. One main goal of these works is to use the object request patterns to determine which segments are admitted to the cache (and for how long) [48]. Along these lines, one can categorize these works into those that consider capacity- constrained caches vs. those that consider timer-based caches. Additionally, these works can be divided into event-based methods that update their decisions on segment admission and cache content whenever a segment is requested vs. works that update the cache content on a discrete-time basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching systems is in general a complex problem which does not easily lend itself to analytical closed-form results. To this end, several model-free methods exist that utilize the metadata observed from the segment request processes to learn good cache content decisions or continuously optimize the content admission and retention policy. Software-Defined Networking (SDN) Support/Server and Network-Assisted DASH (SAND). With the emergence of SDN, new video distribution methods were introduced that incorporated in-network functionalities, diverging from the traditional end-to-end model of the Internet. The common goal of these approaches is to increase the viewers’ QoE by assisting clients in the appropriate selection of DASH segments’ representations. Cofano et al. [35] were among the first to propose a network-assisted

**[Entrenamiento / optimización | extracto 13 | p.11]**

nd delivery optimizations in the network and on servers, allowing clients to provide feedback on anticipated segments and bandwidth requirements and better adaptation of clients due to server- side/network information. While traditional CDNs provide some of the functionalities offered by SAND, they are rather limited and inert. Combining SDN and SAND [25, 67, 91] was a natural consequence, as it efficiently handles SAND communication between network elements. The common concept of these approaches is to use controllers in the network that provide network-assisted ABR streaming, intending to improve the viewers’ QoE. Edge Computing Support. Processing and storage facilities at the network edge, either at CDN edge servers or at edge cloudlets of mobile (4G/5G) networks, can improve HAS delivery [61, 62, 123]. To that end, both HAS clients’ behavior and (radio) network parameters can be taken into account at the edge. An edge node can utilize the information and behavioral parameters of all served clients to acquire a broader (beyond a single client’s) context to enhance the clients’ QoE and QoE fairness, perform bitrate adaptation that mitigates potentially harmful selfish client behavior, improve resource allocation, or save resources. Functions performed at the edge include segment prefetching [10] and caching, transcoding, and re-packaging, edge-based ABR algorithms [7, 9] and stream analytics, machine learning techniques, e.g., to learn and predict the clients’ segment ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Entrenamiento / optimización | extracto 14 | p.11]**

[48]. Along these lines, one can categorize these works into those that consider capacity- constrained caches vs. those that consider timer-based caches. Additionally, these works can be divided into event-based methods that update their decisions on segment admission and cache content whenever a segment is requested vs. works that update the cache content on a discrete-time basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching systems is in general a complex problem which does not easily lend itself to analytical closed-form results. To this end, several model-free methods exist that utilize the metadata observed from the segment request processes to learn good cache content decisions or continuously optimize the content admission and retention policy. Software-Defined Networking (SDN) Support/Server and Network-Assisted DASH (SAND). With the emergence of SDN, new video distribution methods were introduced that incorporated in-network functionalities, diverging from the traditional end-to-end model of the Internet. The common goal of these approaches is to increase the viewers’ QoE by assisting clients in the appropriate selection of DASH segments’ representations. Cofano et al. [35] were among the first to propose a network-assisted approach that uses SDN to provide QoE fairness between DASH clients. An approach that uses SDN to facilitate bitrate adaptation support for DASH clients was introduced by Kleinrouweler et al. [67]. Similarly, SDNDASH [19] presents an SDN-supported resource allocation and management approach that also aims to maximize the QoE of the client. SAND is an MPEG standard [59] that was introduced to ena

**[Entrenamiento / optimización | extracto 15 | p.12]**

198:12 C. Timmerer et al. request patterns, Super-Resolution (SR) and other computations offloaded from end devices, and enabling/supporting 360-degree and immersive video streaming. As an example, transcoding at the edge has the goal of reducing the load on the backhaul network by transcoding segment representations from already existing ones on edge devices, often just in time when a video segment is requested. To this end, the edge does not need to keep different segment representations in cache or treat these as individual objects, but rather uses the fact that quality representations can be deduced from each other. This was, for instance, intensely investigated in a scheme called Light-weight Transcoding at the Edge [41]. A popular application of edge transcoding lies within HAS streaming of 360-degree tiled content since in this case there are many more combinations of video tiles and quality representations leading to a high number of video segments. The transcodi

**[Entrenamiento / optimización | extracto 16 | p.13]**

r HTTP, can be summarized as follows: (i) TCP connection establishment is unnecessarily long. (ii) HAS is not a typical long-lived data stream that falls within the traditional scope of TCP (ramping up to long-term transmission rate fairness). Instead, HAS is known for an ON-OFF triggered transmission that is due to the segment-based requests, in the form of HTTP GET requests. This transmission is known to be TCP-submissive in terms of a lower expected long-term rate. Note that the ON-OFF triggered transmission is directly attributed to the HAS client and its use of the HTTP layer. For example, assuming a simple buffer-based quality adaptation mechanism at the HAS client and assuming a full playback buffer, the client periodically requests a segment with a period length corresponding to the segment playback length. It was shown that this behavior leads to suboptimal transmission rates, as TCP is not able to continuously keep a high transmission rate with such short bursts and very few network status signals (acknowledgments). (iii) HAS over TCP constitutes a double rate control loop, i.e., the quality adaptation module of the client estimates the end-to-end available bandwidth based on coarse signals, e.g., dividing the number of bits in a segment by its download duration, while TCP estimates this rate within its CC modules based on per-packet (per-ack) signals. (iv) Retransmissions of single packets within TCP lead to head-of-line blocking at the client side, i.e., the in-order delivery of the segment up to the application is throttled by the FIFO delivery of packets over the network. Especially at the server side (but also within the network) it is impossible to differentiate a

### 5.x Datos / trazas / datasets

**[Datos / trazas / datasets | extracto 1 | p.1]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges CHRISTIAN TIMMERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation

**[Datos / trazas / datasets | extracto 2 | p.2]**

reaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Section 8 wraps up the article. 2 Background 2.1 A Brief History of Video Streaming The era of video streaming on the Internet dates back to the last decade of the previous century, when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994 [56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming event in 1995 with the Seattle Mariners vs. New York Yankees resulting in RealSystem G2 SureStream technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe adaptive streaming within the 3GPP packet-switched streaming service that uses the Real-Time Streaming Protocol, Session Description Protocol, and Real-Time Transfer Protocol (RTP) for the setup and streaming phases of a streaming session. The Real-Time Control Protocol is used to 1Other terms often used interchangeably or in specific contexts are ABR streaming, DASH, HLS, Smooth Streaming, HTTP Dynamic Streaming (HDS), Over-The-Top streaming, segmented HTTP streaming, Adaptive HTTP Streaming, and so on. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Datos / trazas / datasets | extracto 3 | p.2]**

198:2 C. Timmerer et al. 1 Introduction Over the last 20 years, video streaming has surged in popularity and now constitutes over more than half of global Internet traffic [99]. This trend can be attributed in part to advancements in video compression technologies, such as Advanced Video Coding (AVC) (2003) [122], High Effi- ciency Video Coding (HEVC) (2013) [108], and Versatile Video Coding (VVC) (2020) [30, 31]. Each new generation of video codecs offers more than a 50% improvement in bitrate and qual- ity, respectively. Additionally, developments in networking technology comply with Nielsen’s law of bandwidth, which asserts that “a high-end user’s connection speed grows by 50% per year” [88]. When combined with the increasing computational power of user devices (cf. Moore’s law), this allows for the creation and consumption of video content anywhere and at any time across various devices. Video streamin

**[Datos / trazas / datasets | extracto 4 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send

**[Datos / trazas / datasets | extracto 5 | p.4]**

198:4 C. Timmerer et al. Fig. 1. Basic principles of HAS. Fig. 2. MPEG DASH data model. Each period comprises multiple adaptation sets of different modalities (e.g., video, audio, subtitles) for component selection by clients. Each adaptation set provides multiple representations of the same content with various characteristics (e.g., resolution, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g., the source element) to allow JavaScript to ge

**[Datos / trazas / datasets | extracto 6 | p.5]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:5 Fig. 3. Main phases of the end-to-end video streaming workflow. content is captured using cameras or created using digital tools. Once created, the video is ingested into the streaming platform’s infrastructure. Content ingestion involves uploading or feeding the video data into the system, where it can be processed and prepared for streaming. Several protocols are commonly used for content ingestion, each suited to different types of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable for streaming. This process compresses the video to r

**[Datos / trazas / datasets | extracto 7 | p.6]**

tandards like MPEG-2, without compromising video quality. The AVC standard introduces several enhancements over prior video coding methods to improve coding efficiency. These include variable block-size motion compensation, allowing for flexible and smaller block sizes down to 4 × 4 pixels, and quarter-sample-accurate motion compensation, improving on the half-sample accuracy of earlier standards. Motion vectors can now extend beyond picture boundaries, and multiple reference pictures can be used for motion compensation, enhancing prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in encoding, while weighted prediction and improved motion inference further refine the compression process. Additional innovations include directional spatial prediction for intra-coding, in-the-loop deblocking filtering to reduce artifacts, and a smaller block-size transform for more localized signal representation. The introduction of hierarchical and short word-length transforms, exact-match inverse transforms, and advanced entropy coding methods like Context-Based Adaptive Binary Arithmetic Coding (CABAC) further boost efficiency. To enhance robustness and adaptability across network environments, AVC includes features such as parameter set structures, flexible slice sizes, flexible macroblock ordering, arbitrary slice ordering, redundant pictures, and data ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Datos / trazas / datasets | extracto 8 | p.6]**

198:6 C. Timmerer et al. [36], further expands the scope of audiovisual communication. Additionally, the rapidly growing interest in haptics and mulsemedia, as evidenced by works like [134] and [26], underscores the diverse research landscape beyond video. 3 Video Coding for HAS Video coding or compression is the core of video streaming, where uncompressed video is com- pressed to fit the available bandwidth. Over decades, video codecs have evolved into sophisticated systems that achieve a delicate balance between quality and efficiency. In Section 3.1, we review the current state of video codecs. In Section 3.2, we will examine advancements in bitrate ladder optimization. Additionally, while improving video codec efficiency, there is often an increase in power consumption. Section 3.3 will explore the tradeoffs between compression efficiency and energy consumption. 3.1 Overview of Video Codecs A video codec is a sophisticated compression system that combines various techniques to effi- ciently reduce the size of video data while maintaining high visual quality. It integrates both spatial

**[Datos / trazas / datasets | extracto 9 | p.7]**

for a wide range of applications. In response to the growing demand for coding efficiency that surpasses the capabilities of AVC, particularly with the emergence of ultra-high-definition formats like 4K and 8K resolutions, HEVC was standardized in 2013 [108]. HEVC introduces several advanced features to enhance video compression efficiency, particularly for high-resolution formats like 4K and 8K. The Coding Tree Unit (CTU) structure is a key element, replacing the traditional macroblock with a larger and more flexible coding unit. This allows for better partitioning and precise processing through a quadtree structure that adapts the size of coding blocks and prediction blocks. HEVC also improves motion vector signaling with advanced motion vector prediction and motion compensation, using quarter-sample precision and more sophisticated filtering techniques. Intra-frame prediction is significantly enhanced, offering 33 directional modes, compared to just 8 in previous standards. The standard also includes improved quantization control, entropy coding through a more efficient CABAC system, and advanced in-loop deblocking filtering. Additionally, HEVC introduces sample adaptive offset, a technique designed to better reconstruct signal amplitudes by using a nonlinear amplitude mapping, further enhancing visual quality. The VVC [31] standard builds on the high-level syntax designs from AVC and HEVC, featuring structured bitstreams, parameter sets, and an emphasis on advanced functionalities such as random access and scalability. VVC introduces several sophisticated features to enhance coding efficiency and flexibility: random access is facilitated, which helps balance coding effi

**[Datos / trazas / datasets | extracto 10 | p.7]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:7 partitioning. These advancements make AVC a highly efficient and flexible video coding standard suitable for a wide range of applications. In response to the growing demand for coding efficiency that surpasses the capabilities of AVC, particularly with the emergence of ultra-high-definition formats like 4K and 8K resolutions, HEVC was standardized in 2013 [108]. HEVC introduces several advanced features to enhance video compression efficiency, particularly for high-resolution formats like 4K and 8K. The Coding Tree Unit (CTU) structure is a key element, replacing the traditional macroblock with a larger and more flexible coding unit. This allows for better partitioning and precise processing through a quadtree structure that adapts the size of coding blocks and prediction blocks. HEVC also improves motion vector signaling with advanced motion vector prediction and motion compensation, using quarter-sample precision

**[Datos / trazas / datasets | extracto 11 | p.8]**

198:8 C. Timmerer et al. 3.2 From Static Bitrate Ladders to Dynamic, Live Per-Title Encoding To allow clients to adapt to fluctuating network conditions, the same video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, req

**[Datos / trazas / datasets | extracto 12 | p.8]**

to fluctuating network conditions, the same video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is

**[Datos / trazas / datasets | extracto 13 | p.9]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:9 resolution in the bitrate ladder. A similar approach is employed by Amirpour et al. [17], where not only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add dynamic range as an additional dimension for optimization. While the above-mentioned methods typically rely on a brute-force approach to determine optimal encoding parameters, such as resolution, other methods aim to predict these parameters more efficiently. These predictive approaches are particularly valuable for live video streaming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These predictions often utilize video complexity features, with methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning- based methods to predict encoding parameters, showcasing the potential of AI-driven approaches in optimizing live video streaming. 3.3 Energy Efficiency in Video Coding The energy consumption of video encoding is influenced by multiple factors, including c

**[Datos / trazas / datasets | extracto 14 | p.10]**

198:10 C. Timmerer et al. HAS bitrate ladder construction is computationally expensive. Eliminating perceptually redundant representations through VMAF score comparison and removal of higher bitrate representations when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder construction, considering the content type and user-perceived quality metrics, can further optimize energy efficiency by reducing unnecessary bitrates while maintaining video quality [68]. Video encoding distribution in the computing continuum addresses computational challenges by distributing video encoding tasks across multiple instances in cloud and fog infrastructures. Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding tasks in geographically distributed cloud data centers, optimizing total time and energy consump- tion. The scheduler estimates performance metrics for each data center task assignment considering network distances, server capacity, and workload, potentially using Pareto optimality for efficient video transcoding in the cloud. MAPO [76] utilizes a genetic multi-objective optimization algorithm to determine task placement on fog instances, optimizing total time, energy consumption, and price. VE-MATCH [4] proposes a matching game-based task sc

**[Datos / trazas / datasets | extracto 15 | p.11]**

ncy of streaming sessions. Consequently, SAND enables intelligent caching, processing, and delivery optimizations in the network and on servers, allowing clients to provide feedback on anticipated segments and bandwidth requirements and better adaptation of clients due to server- side/network information. While traditional CDNs provide some of the functionalities offered by SAND, they are rather limited and inert. Combining SDN and SAND [25, 67, 91] was a natural consequence, as it efficiently handles SAND communication between network elements. The common concept of these approaches is to use controllers in the network that provide network-assisted ABR streaming, intending to improve the viewers’ QoE. Edge Computing Support. Processing and storage facilities at the network edge, either at CDN edge servers or at edge cloudlets of mobile (4G/5G) networks, can improve HAS delivery [61, 62, 123]. To that end, both HAS clients’ behavior and (radio) network parameters can be taken into account at the edge. An edge node can utilize the information and behavioral parameters of all served clients to acquire a broader (beyond a single client’s) context to enhance the clients’ QoE and QoE fairness, perform bitrate adaptation that mitigates potentially harmful selfish client behavior, improve resource allocation, or save resources. Functions performed at the edge include segment prefetching [10] and caching, transcoding, and re-packaging, edge-based ABR algorithms [7, 9] and stream analytics, machine learning techniques, e.g., to learn and predict the clients’ segment ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Datos / trazas / datasets | extracto 16 | p.11]**

of streaming sessions. Consequently, SAND enables intelligent caching, processing, and delivery optimizations in the network and on servers, allowing clients to provide feedback on anticipated segments and bandwidth requirements and better adaptation of clients due to server- side/network information. While traditional CDNs provide some of the functionalities offered by SAND, they are rather limited and inert. Combining SDN and SAND [25, 67, 91] was a natural consequence, as it efficiently handles SAND communication between network elements. The common concept of these approaches is to use controllers in the network that provide network-assisted ABR streaming, intending to improve the viewers’ QoE. Edge Computing Support. Processing and storage facilities at the network edge, either at CDN edge servers or at edge cloudlets of mobile (4G/5G) networks, can improve HAS delivery [61, 62, 123]. To that end, both HAS clients’ behavior and (radio) network parameters can be taken into account at the edge. An edge node can utilize the information and behavioral parameters of all served clients to acquire a broader (beyond a single client’s) context to enhance the clients’ QoE and QoE fairness, perform bitrate adaptation that mitigates potentially harmful selfish client behavior, improve resource allocation, or save resources. Functions performed at the edge include segment prefetching [10] and caching, transcoding, and re-packaging, edge-based ABR algorithms [7, 9] and stream analytics, machine learning techniques, e.g., to learn and predict the clients’ segment ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

### 5.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.2]**

delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Section 8 wraps up the article. 2 Background 2.1 A Brief History of Video Streaming The era of video streaming on the Internet dates back to the last decade of the previous century, when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994 [56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming event in 1995 with the Seattle Mariners vs. New York Yankees resulting in RealSystem G2 SureStream technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe adaptive streaming within the 3GPP packet-switched streaming service that uses the Real-Time Streaming Protocol, Session Description Protocol, and Real-Time Transfer Protocol (RTP) for the setup and streaming phases of a streaming session. The Real-Time Control Protocol is used to 1Other terms often used interchangeably or in specific contexts are ABR streaming, DASH, HLS, Smooth Streaming, HTTP Dynamic Streaming (HDS), Over-The-Top streaming, segmented HTTP streaming, Adaptive HTTP Streaming, and so on. ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Evaluación / baselines / experimentos | extracto 2 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progressively download large video files from a server. It enables playback while still downloading. The server aims to send the file as fast as possible. —Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables seeking via media indexing. The server paces transmission based on encoding rate. —Chunked streaming divides the content into short-duration chunks which enables live stream- ing and ad insertion. —Adaptive streaming facilitates multiple versions of the content that enables to adapt to network and device conditions. The latter two can be used jointly and collectively referred to as HAS; pseudo streaming is not used

**[Evaluación / baselines / experimentos | extracto 3 | p.4]**

, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g., the source element) to allow JavaScript to generate media streams for playback, whereby an ABR algorithm could be implemented in JavaScript [92]. In general, DASH and HLS can be used interchangeably without impacting the performance of video streaming services [24]. 2.4 End-to-End Video Streaming Workflow End-to-end video streaming refers to the entire process involved in delivering video content from its source (content creation) to the end user (playback). This comprehensive process involves multiple phases, each critical to ensure a seamless and high-quality streaming experience. Figure 3 shows the five key phases of the end-to-end video streaming pipeline, described as follows: —Content Creation and Ingestion. This phase consists of two main procedures: Content creation and content ingestion. Content creation is the initial step that involves the production of video content, whether it is live broadcasts, pre-recorded shows, or user-generated videos. This ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Evaluación / baselines / experimentos | extracto 4 | p.6]**

codecs use transform coding to convert spatial data into frequency coefficients, which allows the removal of high-frequency data that human perception is less sensitive to. This is followed by quantization, which reduces the precision of these coefficients to balance compression and visual quality. Finally, entropy coding further compresses the quantized data by using shorter codes for more frequent patterns. By integrating these methods, video codecs effectively compress data, making them essential for modern video streaming, broadcasting, storage, and so on. Over the years, several video coding standards have been developed, each offering improvements in compression efficiency. One of the most widely adopted standards is AVC [122]. Introduced in 2003, AVC revolutionized video compression by providing a significant reduction in bitrates compared to previous standards like MPEG-2, without compromising video quality. The AVC standard introduces several enhancements over prior video coding methods to improve coding efficiency. These include variable block-size motion compensation, allowing for flexible and smaller block sizes down to 4 × 4 pixels, and quarter-sample-accurate motion compensation, improving on the half-sample accuracy of earlier standards. Motion vectors can now extend beyond picture boundaries, and multiple reference pictures can be used for motion compensation, enhancing prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in encoding, while weighted prediction and improved motion inference further refine the compression process. Additional innovations include directional spatial prediction for intra-coding, in-the-loo

**[Evaluación / baselines / experimentos | extracto 5 | p.7]**

sses the capabilities of AVC, particularly with the emergence of ultra-high-definition formats like 4K and 8K resolutions, HEVC was standardized in 2013 [108]. HEVC introduces several advanced features to enhance video compression efficiency, particularly for high-resolution formats like 4K and 8K. The Coding Tree Unit (CTU) structure is a key element, replacing the traditional macroblock with a larger and more flexible coding unit. This allows for better partitioning and precise processing through a quadtree structure that adapts the size of coding blocks and prediction blocks. HEVC also improves motion vector signaling with advanced motion vector prediction and motion compensation, using quarter-sample precision and more sophisticated filtering techniques. Intra-frame prediction is significantly enhanced, offering 33 directional modes, compared to just 8 in previous standards. The standard also includes improved quantization control, entropy coding through a more efficient CABAC system, and advanced in-loop deblocking filtering. Additionally, HEVC introduces sample adaptive offset, a technique designed to better reconstruct signal amplitudes by using a nonlinear amplitude mapping, further enhancing visual quality. The VVC [31] standard builds on the high-level syntax designs from AVC and HEVC, featuring structured bitstreams, parameter sets, and an emphasis on advanced functionalities such as random access and scalability. VVC introduces several sophisticated features to enhance coding efficiency and flexibility: random access is facilitated, which helps balance coding efficiency with end-to-end delay; reference picture resampling allows for resolution adjustments in inter-cod

**[Evaluación / baselines / experimentos | extracto 6 | p.8]**

A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the best possible way while minimizing unnecessary bandwidth usage. Various methods have been proposed to optimize bitr

**[Evaluación / baselines / experimentos | extracto 7 | p.9]**

ation achieves approximately 50% coding efficiency gain over the previous generation, at the cost of increased computational complexity, longer encoding times, and higher energy consumption [96]. For exam- ple, AVC consumes over four times more power than earlier standards like MJPEG and MPEG-4 Part 2, due to more and refined compression techniques such as multiple reference frames in AVC [103, 119]. HEVC further enhances compression efficiency by 25.1% over AVC but also increases energy consumption by 17.4% [81]. Search Range (SR), a crucial parameter in ME, significantly contributes to this higher energy demand, among other factors. VVC’s complexity is eight times higher than HEVC [27], resulting in a fourfold increase in energy consumption [32]. In contrast, AV1 offers a better tradeoff between coding efficiency and energy consumption compared to AVC, HEVC, VP9, and VVC [32]. Encoding parameters significantly influence energy consumption [80]. Resolution directly impacts energy consumption, with a linear relationship between pixel count and energy consumption. Frame rate directly correlates with energy consumption due to increased computational demands. Consequently, doubling the resolution while halving the frame rate maintains energy consumption. Presets (AVC, HEVC, and VVC) and speed settings (AV1 and VP9) determine the tradeoff between the encoding speed and the compression efficiency [14, 32, 105]. Higher quality settings (i.e., slower presets and lower speed settings) increase encoding time and energy consumption due to more complex tools and extensive search spaces [80] explored to choose the most efficient coding configurations [32]. For example, Silveira et al. [105]

**[Evaluación / baselines / experimentos | extracto 8 | p.9]**

tly correlates with energy consumption [63] due to the higher compu- tational power required for intricate algorithms and calculations. Each codec generation achieves approximately 50% coding efficiency gain over the previous generation, at the cost of increased computational complexity, longer encoding times, and higher energy consumption [96]. For exam- ple, AVC consumes over four times more power than earlier standards like MJPEG and MPEG-4 Part 2, due to more and refined compression techniques such as multiple reference frames in AVC [103, 119]. HEVC further enhances compression efficiency by 25.1% over AVC but also increases energy consumption by 17.4% [81]. Search Range (SR), a crucial parameter in ME, significantly contributes to this higher energy demand, among other factors. VVC’s complexity is eight times higher than HEVC [27], resulting in a fourfold increase in energy consumption [32]. In contrast, AV1 offers a better tradeoff between coding efficiency and energy consumption compared to AVC, HEVC, VP9, and VVC [32]. Encoding parameters significantly influence energy consumption [80]. Resolution directly impacts energy consumption, with a linear relationship between pixel count and energy consumption. Frame rate directly correlates with energy consumption due to increased computational demands. Consequently, doubling the resolution while halving the frame rate maintains energy consumption. Presets (AVC, HEVC, and VVC) and speed settings (AV1 and VP9) determine the tradeoff between the encoding speed and the compression efficiency [14, 32, 105]. Higher quality settings (i.e., slower presets and lower speed settings) increase encoding time and energy consumption due to

**[Evaluación / baselines / experimentos | extracto 9 | p.10]**

198:10 C. Timmerer et al. HAS bitrate ladder construction is computationally expensive. Eliminating perceptually redundant representations through VMAF score comparison and removal of higher bitrate representations when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder construction, considering the content type and user-perceived quality metrics, can further optimize energy efficiency by reducing unnecessary bitrates while maintaining video quality [68]. Video encoding distribution in the computing continuum addresses computational challenges by distributing video encoding tasks across multiple instances in cloud and fog infrastructures. Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding tasks in geographically distributed cloud data centers, optimizing total time and energy consump- tion. The scheduler estimates performance metrics for each data center task assignment considering network distances, server capacit

**[Evaluación / baselines / experimentos | extracto 10 | p.10]**

tationally expensive. Eliminating perceptually redundant representations through VMAF score comparison and removal of higher bitrate representations when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder construction, considering the content type and user-perceived quality metrics, can further optimize energy efficiency by reducing unnecessary bitrates while maintaining video quality [68]. Video encoding distribution in the computing continuum addresses computational challenges by distributing video encoding tasks across multiple instances in cloud and fog infrastructures. Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding tasks in geographically distributed cloud data centers, optimizing total time and energy consump- tion. The scheduler estimates performance metrics for each data center task assignment considering network distances, server capacity, and workload, potentially using Pareto optimality for efficient video transcoding in the cloud. MAPO [76] utilizes a genetic multi-objective optimization algorithm to determine task placement on fog instances, optimizing total time, energy consumption, and price. VE-MATCH [4] proposes a matching game-based task scheduling approach to optimize resource allocation between media and resource providers. GreenFog [84] optimizes energy use by utilizing renewable energy sources for fog computing. The framework employs optimization techniques, including a heuristic linear regression approach and a machine learning-based Multi- Armed Bandit method. These techniques allow GreenFog to adapt to real-time energy availability. EFFECT [130] introduces an energy

**[Evaluación / baselines / experimentos | extracto 11 | p.11]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:11 individual cache hit rates as well as the hierarchy hit rate and the midgress, i.e., the traffic sent between caches and caches and the origin server to update the content. Extensive work has been conducted on the evaluation of caching strategies for single (edge caching) systems as well as for entire hierarchies [3, 25, 133]. One main goal of these works is to use the object request patterns to determine which segments are admitted to the cache (and for how long) [48]. Along these lines, one can categorize these works into those that consider capacity- constrained caches vs. those that consider timer-based caches. Additionally, these works can be divided into event-based methods that update their decisions on segment admission and cache content whenever a segment is requested vs. works that update the cache content on a discrete-time basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching systems is in general a complex problem which does not easily lend itself to analytical closed-form results. To this end, s

**[Evaluación / baselines / experimentos | extracto 12 | p.11]**

ucted on the evaluation of caching strategies for single (edge caching) systems as well as for entire hierarchies [3, 25, 133]. One main goal of these works is to use the object request patterns to determine which segments are admitted to the cache (and for how long) [48]. Along these lines, one can categorize these works into those that consider capacity- constrained caches vs. those that consider timer-based caches. Additionally, these works can be divided into event-based methods that update their decisions on segment admission and cache content whenever a segment is requested vs. works that update the cache content on a discrete-time basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching systems is in general a complex problem which does not easily lend itself to analytical closed-form results. To this end, several model-free methods exist that utilize the metadata observed from the segment request processes to learn good cache content decisions or continuously optimize the content admission and retention policy. Software-Defined Networking (SDN) Support/Server and Network-Assisted DASH (SAND). With the emergence of SDN, new video distribution methods were introduced that incorporated in-network functionalities, diverging from the traditional end-to-end model of the Internet. The common goal of these approaches is to increase the viewers’ QoE by assisting clients in the appropriate selection of DASH segments’ representations. Cofano et al. [35] were among the first to propose a network-assisted approach that uses SDN to provide QoE fairness between DASH clients. An approach that uses SDN to facilitate bitrate adaptation suppo

**[Evaluación / baselines / experimentos | extracto 13 | p.11]**

o et al. [35] were among the first to propose a network-assisted approach that uses SDN to provide QoE fairness between DASH clients. An approach that uses SDN to facilitate bitrate adaptation support for DASH clients was introduced by Kleinrouweler et al. [67]. Similarly, SDNDASH [19] presents an SDN-supported resource allocation and management approach that also aims to maximize the QoE of the client. SAND is an MPEG standard [59] that was introduced to enable communication between streaming clients and network elements/servers like caches. It offers standard interfaces for the communication between these elements. The goals of SAND are optimized operations with caches, the support of consistent and high-level QoE for viewers, and QoE measurement features to improve streaming. By providing real-time information about network and client performance, SAND enhances the efficiency of streaming sessions. Consequently, SAND enables intelligent caching, processing, and delivery optimizations in the network and on servers, allowing clients to provide feedback on anticipated segments and bandwidth requirements and better adaptation of clients due to server- side/network information. While traditional CDNs provide some of the functionalities offered by SAND, they are rather limited and inert. Combining SDN and SAND [25, 67, 91] was a natural consequence, as it efficiently handles SAND communication between network elements. The common concept of these approaches is to use controllers in the network that provide network-assisted ABR streaming, intending to improve the viewers’ QoE. Edge Computing Support. Processing and storage facilities at the network edge, either at CDN edge servers or at

**[Evaluación / baselines / experimentos | extracto 14 | p.13]**

sly keep a high transmission rate with such short bursts and very few network status signals (acknowledgments). (iii) HAS over TCP constitutes a double rate control loop, i.e., the quality adaptation module of the client estimates the end-to-end available bandwidth based on coarse signals, e.g., dividing the number of bits in a segment by its download duration, while TCP estimates this rate within its CC modules based on per-packet (per-ack) signals. (iv) Retransmissions of single packets within TCP lead to head-of-line blocking at the client side, i.e., the in-order delivery of the segment up to the application is throttled by the FIFO delivery of packets over the network. Especially at the server side (but also within the network) it is impossible to differentiate and hence expedite the transmission of an urgent retransmitted packet in comparison to previously scheduled packets that, however, belong to a later segment. In the context of HTTP/3, QUIC has emerged as a viable alternative to TCP. While it does not explicitly address all the shortcomings listed above, it provides the protocol architectural tools to address these. In addition, it was shown to perform better than TCP due to the new design. With respect to HAS, the main difference in using HTTP/3 over QUIC is that it introduces the concepts of streams and subflows on top of connectionless UDP flows. The QUIC library allows, hence, to rapidly prototype different CC and reliability schemes in user space on top of simple connectionless flows. While stream multiplexing has been known from the Stream Control Transmission Protocol it received an Internet-wide deployment with QUIC. Stream multiplexing allows concurrency between

**[Evaluación / baselines / experimentos | extracto 15 | p.13]**

ile stream multiplexing has been known from the Stream Control Transmission Protocol it received an Internet-wide deployment with QUIC. Stream multiplexing allows concurrency between the data streams and hence differentiated transmission scheduling of application-defined streams. This differentiation can be, for example, in terms of a stream for fresh segments (or their packets) and a stream for retransmitted segments (or their packets), where the second stream possesses a higher priority than the first one. This would solve the above head-of-line blocking problem. The stream multiplexing and demultiplexing mechanism of QUIC lends itself well to multipath delivery of HAS since it allows QUIC, in contrast to Multi-Path TCP, to map streams to subflows that are bound to physical network interfaces. This flexibility allows tying the measured performance metrics (e.g., packet loss, delays) on a certain network interface to scheduling decisions of different streams such as scheduling fresh segment packets or retransmitted ones. As the QUIC library runs in user space, it also allows rapid prototyping of such strategies, e.g., for retransmissions, scheduling, interface bandwidth estimation, and mapping of streams to interfaces. CC. The impact of CC on the performance of HAS delivery has been widely studied, specially, as new CC mechanisms, such as bottleneck bandwidth and round-trip propagation time, are known to be unfair to older TCP CC connections. It is evident that the CC mechanism, which throttles the packet sending rate on the HAS server side, has a direct implication on two available bandwidth estimates on the HAS client side, the first being the transport layer estimate in CC or QU

**[Evaluación / baselines / experimentos | extracto 16 | p.14]**

well as decisions on the quality of the requested segments. These neural networks can be trained in a federated fashion, first, to learn optimal transmission decisions from a larger number of HAS clients without centrally collecting data and, secondly, they can be trained in an online reinforcement learning manner to adapt the transmission behavior at runtime. LL DASH and HLS. As introduced in Section 2, CMAF facilitates LL video streaming services: fragmented segment transmission (delivery in so-called chunks) allows a segment to start playing before being fully received by the client. Both relevant HAS standards have LL versions, LL-DASH and LL-HLS, allowing the end-to-end latency to be reduced to a few seconds only [24]. The body of research addressing LL HAS encompasses earlier works such as [28], focusing on overhead and performance evaluations, and extends to more sophisticated and recent contributions, e.g., [70], which provides a novel LL ABR algorithm for HAS. Additionally, a comprehensive, up-to-date survey has been conducted and is documented in [21]. Various performance assessments have been performed, including those over satellite communication channels as detailed in [131], and those concerning player performance, which are addressed in [128]. 5 Video Consumption in HAS Content consumption in HAS refers to the final end points facing the end user. It mostly concerns the player which hosts the ABR algorithm responsible for requesting video segments over best- effort networks, and, recently, energy-aware/-efficient ABR algorithms have been proposed in the literature, which are briefly reviewed in this section. 5.1 ABR Algorithms: State of the Art and Recent Advances Th

### 5.x Limitaciones / riesgos / implementación

**[Limitaciones / riesgos / implementación | extracto 1 | p.1]**

Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery technologies. CCS Concepts: • Information systems →Multimedia streaming; Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery, Video Consumption, Quality of Experience, QoE ACM Reference format: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM Trans. Multimedia Comput. Commun. Appl. 21, 7, Article 198 (July 2025), 27 pages. https://doi.org/10.1145/3736306 Authors’ Contact Information: Christian

**[Limitaciones / riesgos / implementación | extracto 2 | p.1]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges CHRISTIAN TIMMERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria AMR RIZK, Leibniz University Hannover, Hannover, Germany MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming (HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive bitr

**[Limitaciones / riesgos / implementación | extracto 3 | p.2]**

itate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and Apple HTTP Live Streaming (HLS), although standards typically specify normative formats (i.e., bitstream syntax) only, leaving non-normative parts open for (industry) competition. The research community can play a crucial role in this ecosystem by researching innovative solutions, specifically targeting non-normative aspects within these specifications. In this article, our aim is to provide a brief (historical) background of HAS and a comprehensive overview of research efforts related to key phases in modern HAS workflows; ranging from (i) video encoding, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including Quality of Experience (QoE). For each of these phases, we will outline basic principles, current trends, and future challenges for HAS. The structure of this article is as follows. Section 2 covers the early history of video streaming on the Internet, the rise of HAS and its fundamental principles, a brief summary of international standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for HAS, including per-title encoding and recent optimizations, as well as energy-related concerns. Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in- network optimizations. Section 5 examines the client-side consumption aspects of video streaming, focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6 discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7 explores potential future directions for HAS, and Section 8 wraps

**[Limitaciones / riesgos / implementación | extracto 4 | p.3]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:3 adaptively change the transmission and content rates to the current network conditions. The first YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP [2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of smartphones (e.g., iPhone introduced in 2007). In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by Wang et al. [121] who concluded that “TCP generally provides good streaming performance when the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup delay,” providing a baseline for future development at that time. In general, video streaming over HTTP can be roughly divided into the following techniques: —Progressive download utilizes a single TCP connection to progre

**[Limitaciones / riesgos / implementación | extracto 5 | p.4]**

198:4 C. Timmerer et al. Fig. 1. Basic principles of HAS. Fig. 2. MPEG DASH data model. Each period comprises multiple adaptation sets of different modalities (e.g., video, audio, subtitles) for component selection by clients. Each adaptation set provides multiple representations of the same content with various characteristics (e.g., resolution, bitrate). Each representation provides means to construct HTTP URLs for individual segments to be used by the client to download these segments in a timely manner from the HTTP server. The Common Media Application Format (CMAF) [58] aims to harmonize segment formats towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it enables the implementation of Low-Latency (LL) live video streaming services by introducing fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g., the source element) to allow JavaScript to generate media streams for playback, whereby an ABR algorithm could be implemented in JavaScript [92]. In general, DASH and HLS can be used interchangeably without impacting the performance of video streaming services [24]. 2.4 End-to-End Video Streaming Workflow End-to-end video streaming refers to the entire process involved in delivering video content from its source (content creation) to the end user (playback). This comprehensive process involves multiple phases, each critical to ensure a seamless and high-quality streaming experience. Figure 3 shows the five key ph

**[Limitaciones / riesgos / implementación | extracto 6 | p.5]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:5 Fig. 3. Main phases of the end-to-end video streaming workflow. content is captured using cameras or created using digital tools. Once created, the video is ingested into the streaming platform’s infrastructure. Content ingestion involves uploading or feeding the video data into the system, where it can be processed and prepared for streaming. Several protocols are commonly used for content ingestion, each suited to different types of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer Protocols (FTP, SFTP, Aspera). —Encoding and Packaging. The next phase requires encoding and packaging the video data into different representations and formats. The video data is encoded into digital formats that are suitable fo

**[Limitaciones / riesgos / implementación | extracto 7 | p.6]**

ed standards is AVC [122]. Introduced in 2003, AVC revolutionized video compression by providing a significant reduction in bitrates compared to previous standards like MPEG-2, without compromising video quality. The AVC standard introduces several enhancements over prior video coding methods to improve coding efficiency. These include variable block-size motion compensation, allowing for flexible and smaller block sizes down to 4 × 4 pixels, and quarter-sample-accurate motion compensation, improving on the half-sample accuracy of earlier standards. Motion vectors can now extend beyond picture boundaries, and multiple reference pictures can be used for motion compensation, enhancing prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in encoding, while weighted prediction and improved motion inference further refine the compression process. Additional innovations include directional spatial prediction for intra-coding, in-the-loop deblocking filtering to reduce artifacts, and a smaller block-size transform for more localized signal representation. The introduction of hierarchical and short word-length transforms, exact-match inverse transforms, and advanced entropy coding methods like Context-Based Adaptive Binary Arithmetic Coding (CABAC) further boost efficiency. To enhance robustness and adaptability across network environments, AVC includes features such as parameter set structures, flexible slice sizes, flexible macroblock ordering, arbitrary slice ordering, redundant pictures, and data ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Limitaciones / riesgos / implementación | extracto 8 | p.6]**

, improving on the half-sample accuracy of earlier standards. Motion vectors can now extend beyond picture boundaries, and multiple reference pictures can be used for motion compensation, enhancing prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in encoding, while weighted prediction and improved motion inference further refine the compression process. Additional innovations include directional spatial prediction for intra-coding, in-the-loop deblocking filtering to reduce artifacts, and a smaller block-size transform for more localized signal representation. The introduction of hierarchical and short word-length transforms, exact-match inverse transforms, and advanced entropy coding methods like Context-Based Adaptive Binary Arithmetic Coding (CABAC) further boost efficiency. To enhance robustness and adaptability across network environments, AVC includes features such as parameter set structures, flexible slice sizes, flexible macroblock ordering, arbitrary slice ordering, redundant pictures, and data ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.

**[Limitaciones / riesgos / implementación | extracto 9 | p.7]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:7 partitioning. These advancements make AVC a highly efficient and flexible video coding standard suitable for a wide range of applications. In response to the growing demand for coding efficiency that surpasses the capabilities of AVC, particularly with the emergence of ultra-high-definition formats like 4K and 8K resolutions, HEVC was standardized in 2013 [108]. HEVC introduces several advanced features to enhance video compression efficiency, particularly for high-resolution formats like 4K and 8K. The Coding Tree Unit (CTU) structure is a key element, replacing the traditional macroblock with a larger and more flexible coding unit. This allows for better partitioning and precise processing through a quadtree structure that adapts the size of coding blocks and prediction blocks. HEVC also improves motion vector signaling with adv

**[Limitaciones / riesgos / implementación | extracto 10 | p.8]**

ts to adapt to fluctuating network conditions, the same video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that co

**[Limitaciones / riesgos / implementación | extracto 11 | p.8]**

ing network conditions, the same video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fine-tuned. These include the number of representations, their corresponding bitrate, resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content is delivered in the

**[Limitaciones / riesgos / implementación | extracto 12 | p.8]**

198:8 C. Timmerer et al. 3.2 From Static Bitrate Ladders to Dynamic, Live Per-Title Encoding To allow clients to adapt to fluctuating network conditions, the same video is encoded at multiple representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame- ters such as bitrates and resolutions for each representation of the video. The size of the bitrate ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for various video coding standards up to 8K resolution. Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional processing, it is suboptimal because it fails to account for the specific characteristics of the video content and the varying bandwidth requirements of users. For example, encoding all video content at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low- and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition to optimizing the maximum bitrate required to achieve high quality, other encoding parameters can also be fi

**[Limitaciones / riesgos / implementación | extracto 13 | p.9]**

employed by Amirpour et al. [17], where not only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add dynamic range as an additional dimension for optimization. While the above-mentioned methods typically rely on a brute-force approach to determine optimal encoding parameters, such as resolution, other methods aim to predict these parameters more efficiently. These predictive approaches are particularly valuable for live video streaming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These predictions often utilize video complexity features, with methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning- based methods to predict encoding parameters, showcasing the potential of AI-driven approaches in optimizing live video streaming. 3.3 Energy Efficiency in Video Coding The energy consumption of video encoding is influenced by multiple factors, including codec selection and encoding parameter configurations. Additionally, HAS encodes videos in multiple representations (bitrate ladder), typically a computationally intensive process. Encoding complexity directly correlates with energy consumption [63] due to the higher compu- tational power required for intricate algorithms and calculations. Each codec generation achieves approximatel

**[Limitaciones / riesgos / implementación | extracto 14 | p.9]**

. Guionnet et al. [50] add dynamic range as an additional dimension for optimization. While the above-mentioned methods typically rely on a brute-force approach to determine optimal encoding parameters, such as resolution, other methods aim to predict these parameters more efficiently. These predictive approaches are particularly valuable for live video streaming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlining the encoding process. These predictions often utilize video complexity features, with methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning- based methods to predict encoding parameters, showcasing the potential of AI-driven approaches in optimizing live video streaming. 3.3 Energy Efficiency in Video Coding The energy consumption of video encoding is influenced by multiple factors, including codec selection and encoding parameter configurations. Additionally, HAS encodes videos in multiple representations (bitrate ladder), typically a computationally intensive process. Encoding complexity directly correlates with energy consumption [63] due to the higher compu- tational power required for intricate algorithms and calculations. Each codec generation achieves approximately 50% coding efficiency gain over the previous generation, at the cost of increased computational complexity, longer enco

**[Limitaciones / riesgos / implementación | extracto 15 | p.9]**

HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges 198:9 resolution in the bitrate ladder. A similar approach is employed by Amirpour et al. [17], where not only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add dynamic range as an additional dimension for optimization. While the above-mentioned methods typically rely on a brute-force approach to determine optimal encoding parameters, such as resolution, other methods aim to predict these parameters more efficiently. These predictive approaches are particularly valuable for live video streaming, where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine learning method that predicts the crossover bitrate between optimized resolutions, improving encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further streamlini

**[Limitaciones / riesgos / implementación | extracto 16 | p.10]**

tal time, energy consumption, and price. VE-MATCH [4] proposes a matching game-based task scheduling approach to optimize resource allocation between media and resource providers. GreenFog [84] optimizes energy use by utilizing renewable energy sources for fog computing. The framework employs optimization techniques, including a heuristic linear regression approach and a machine learning-based Multi- Armed Bandit method. These techniques allow GreenFog to adapt to real-time energy availability. EFFECT [130] introduces an energy-efficient fog computing framework designed for real-time video processing. EFFECT tackles the challenge of balancing energy consumption with latency deadlines employing a two-fold approach. First, a centralized resource allocation scheme distributes sub-channels, transmission, and processing power considering task complexity and deadlines. Second, a distributed game-theoretic approach allows instances to strategically decide between local processing or offloading tasks to fog servers, minimizing their energy footprint. 4 Video Delivery in HAS The significant rise in the popularity of video streaming applications has created challenges for the scalable delivery of multimedia content to viewers. This section discusses various technologies developed to address these challenges, focusing on methods that operate within the network and those that function end-to-end between the content server and the client. 4.1 In-Network Support of HAS Delivery The distribution of video content in today’s Internet heavily relies on in-network functions that increase the scalability, quality, and manageability of streaming applications. In the following, we briefly describe th

## 6. Figuras / tablas / algoritmos / ecuaciones detectados por texto
- p.3: Figure 1, comprising an HTTP server that hosts the
- p.3: Figure 2 which comprises an XML-based Media Presentation Description as manifest
- p.4: Fig. 1. Basic principles of HAS.
- p.4: Fig. 2. MPEG DASH data model.
- p.4: Figure 3 shows
- p.5: Fig. 3. Main phases of the end-to-end video streaming workflow.

## 7. Líneas con posible contenido matemático/formal
- p.2: `than half of global Internet traffic [99]. This trend can be attributed in part to advancements in`
- p.2: `video compression technologies, such as Advanced Video Coding (AVC) (2003) [122], High Effi-`
- p.2: `ciency Video Coding (HEVC) (2013) [108], and Versatile Video Coding (VVC) (2020) [30, 31].`
- p.2: `[88]. When combined with the increasing computational power of user devices (cf. Moore’s law),`
- p.2: `[56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming`
- p.2: `technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe`
- p.3: `[2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of`
- p.3: `Wang et al. [121] who concluded that “TCP generally provides good streaming performance when`
- p.3: `The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which`
- p.4: `The Common Media Application Format (CMAF) [58] aims to harmonize segment formats`
- p.4: `algorithm could be implemented in JavaScript [92].`
- p.4: `video streaming services [24].`
- p.5: `audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS`
- p.5: `[90], CMAF [58]) format that supports adaptive streaming and other advanced features [8].`
- p.5: `and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves`
- p.5: `conjunction with HAS is covered in [37, 95]. The integration of subtitles in HAS, as explored in`
- p.6: `[36], further expands the scope of audiovisual communication. Additionally, the rapidly growing`
- p.6: `interest in haptics and mulsemedia, as evidenced by works like [134] and [26], underscores the`
- p.6: `in compression efficiency. One of the most widely adopted standards is AVC [122]. Introduced`
- p.7: `was standardized in 2013 [108]. HEVC introduces several advanced features to enhance video`
- p.7: `The VVC [31] standard builds on the high-level syntax designs from AVC and HEVC, featuring`
- p.7: `generations of video compression technology. In parallel, video codecs like VP9 and AV1 [53],`
- p.7: `Despite SVC [100] being highlighted as a promising method for HAS in studies such as`
- p.7: `[55, 83, 98], there has been a notable decline in its adoption or further exploration by both industrial`
- p.8: `ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for`
- p.8: `[112] introduced a method where the desired bitrate requests of all users are collected and used`
- p.8: `issue, ARTEMIS [111] proposes a mega bitrate ladder, where a large number of representations are`
- p.8: `process to better align with the actual user demands. Similarly, COBIRAS [102] utilizes a bitrate`
- p.8: `Multimethod Assessment Fusion (VMAF) [1], the JND is typically around six points, meaning`
- p.8: `[15, 132]. By carefully selecting representations based on this JND threshold, these approaches`
- p.8: `enhancing both streaming efficiency and viewer experience [18, 78].`
- p.8: `Other methods focus on optimizing encoding parameters beyond bitrate. De Cock et al. [39]`
- p.9: `resolution in the bitrate ladder. A similar approach is employed by Amirpour et al. [17], where not`
- p.9: `only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add`
- p.9: `where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine`
- p.9: `encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further`
- p.9: `methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal`
- p.9: `complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning-`
- p.9: `Encoding complexity directly correlates with energy consumption [63] due to the higher compu-`
- p.9: `computational complexity, longer encoding times, and higher energy consumption [96]. For exam-`
- p.9: `[103, 119]. HEVC further enhances compression efficiency by 25.1% over AVC but also increases`
- p.9: `energy consumption by 17.4% [81]. Search Range (SR), a crucial parameter in ME, significantly`
- p.9: `higher than HEVC [27], resulting in a fourfold increase in energy consumption [32]. In contrast,`
- p.9: `HEVC, VP9, and VVC [32].`
- p.9: `Encoding parameters significantly influence energy consumption [80]. Resolution directly impacts`
- p.9: `the encoding speed and the compression efficiency [14, 32, 105]. Higher quality settings (i.e.,`
- p.9: `to more complex tools and extensive search spaces [80] explored to choose the most efficient`
- p.9: `coding configurations [32]. For example, Silveira et al. [105] observed a 45-fold energy consumption`
- p.9: `have an exponential impact on power consumption [103]. Other encoding parameters, such as the`
- p.9: `power consumption, with variations up to 10% reported in [103]. Monteiro et al. [81] found that`
- p.10: `when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder`
- p.10: `energy efficiency by reducing unnecessary bitrates while maintaining video quality [68].`
- p.10: `Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding`
- p.10: `video transcoding in the cloud. MAPO [76] utilizes a genetic multi-objective optimization algorithm`
- p.10: `price. VE-MATCH [4] proposes a matching game-based task scheduling approach to optimize`
- p.10: `resource allocation between media and resource providers. GreenFog [84] optimizes energy use`
- p.10: `EFFECT [130] introduces an energy-efficient fog computing framework designed for real-time`
- p.10: `server by caching hot objects [33, 74], specifically, hot video segments in the case of HAS. While`
- p.11: `caching) systems as well as for entire hierarchies [3, 25, 133]. One main goal of these works is to`
- p.11: `how long) [48]. Along these lines, one can categorize these works into those that consider capacity-`
- p.11: `appropriate selection of DASH segments’ representations. Cofano et al. [35] were among the first`
- p.11: `introduced by Kleinrouweler et al. [67]. Similarly, SDNDASH [19] presents an SDN-supported`
- p.11: `SAND is an MPEG standard [59] that was introduced to enable communication between streaming`
- p.11: `Combining SDN and SAND [25, 67, 91] was a natural consequence, as it efficiently handles SAND`
- p.11: `edge servers or at edge cloudlets of mobile (4G/5G) networks, can improve HAS delivery [61, 62, 123].`
- p.11: `prefetching [10] and caching, transcoding, and re-packaging, edge-based ABR algorithms [7, 9]`
- p.12: `investigated in a scheme called Light-weight Transcoding at the Edge [41]. A popular application of`
- p.12: `proposed and evaluated, e.g., in [44, 46]. Such systems are designed to reduce both the latency of`
- p.12: `is a “rich design space for jointly optimized SDN-assisted caching architectures” [25] for HAS, and`
- p.12: `prefetching strategies, and load balancing [74]. The paradigm of ICN [11] has the goal of replacing`
- p.12: `between the client and the origin server. ICN approaches like CCN [60] and NDN [129] propose`
- p.12: `significant QoE impairments due to bitrate oscillations, as demonstrated by Grandl et al. [49].`
- p.14: `push out other competing, less aggressive dataflows. Studies as early as [107, 110] showed that given`
- p.14: `and LL-HLS, allowing the end-to-end latency to be reduced to a few seconds only [24]. The body of`
- p.14: `research addressing LL HAS encompasses earlier works such as [28], focusing on overhead and`
- p.14: `performance evaluations, and extends to more sophisticated and recent contributions, e.g., [70],`
- p.14: `survey has been conducted and is documented in [21]. Various performance assessments have been`
- p.14: `performed, including those over satellite communication channels as detailed in [131], and those`
- p.14: `concerning player performance, which are addressed in [128].`
- p.14: `Multiple surveys related to HAS, ABR, and QoE have been published in the past [23, 101] and`

## 8. Texto crudo completo por página

> Mantener este bloque para Codex si necesita comprobar contexto literal. Puede contener errores de orden por columnas del PDF. Para fórmulas exactas o tablas complejas, usar PDF original.


### Página 1

```text
HTTP Adaptive Streaming: A Review on Current Advances
and Future Challenges
CHRISTIAN TIMMERER, HADI AMIRPOUR, FARZAD TASHTARIAN, and SAMIRA
AFZAL, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria
AMR RIZK, Leibniz University Hannover, Hannover, Germany
MICHAEL ZINK, University of Massachusetts Amherst, Amherst, Massachusetts, USA
HERMANN HELLWAGNER, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität
Klagenfurt, Klagenfurt, Austria
Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated hard-/software
infrastructures to pull-based unicast schemes utilizing existing Web-based infrastructure to allow for better
scalability. In this article, we provide an overview of the foundational principles of HTTP Adaptive Streaming
(HAS), from video encoding to end user consumption, while focusing on the key advancements in adaptive
bitrate algorithms, Quality of Experience (QoE), and energy efficiency. Furthermore, the article highlights the
ongoing challenges of optimizing network infrastructure, minimizing latency, and managing the environmental
impact of video streaming. Finally, future directions for HAS, including immersive media streaming and neural
network-based video codecs, are discussed, positioning HAS at the forefront of next-generation video delivery
technologies.
CCS Concepts: • Information systems →Multimedia streaming;
Additional Key Words and Phrases: HTTP Adaptive Streaming, HAS, DASH, Video Coding, Video Delivery,
Video Consumption, Quality of Experience, QoE
ACM Reference format:
Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, and Hermann
Hellwagner. 2025. HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges. ACM
Trans. Multimedia Comput. Commun. Appl. 21, 7, Article 198 (July 2025), 27 pages.
https://doi.org/10.1145/3736306
Authors’ Contact Information: Christian Timmerer (corresponding author), Christian Doppler Laboratory ATHENA,
Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria; e-mail: christian.timmerer@aau.at; Hadi Amirpour, Christian
Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria; e-mail: hadi.amirpour@aau.at;
Farzad Tashtarian, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt, Klagenfurt, Austria; e-mail:
farzad.tashtarian@aau.at; Samira Afzal, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt,
Klagenfurt, Austria; e-mail: samira.afzal@aau.at; Amr Rizk, Leibniz University Hannover, Hannover, Germany; e-mail:
amr.rizk@ikt.uni-hannover.de; Michael Zink, University of Massachusetts Amherst, Amherst, Massachusetts, USA; e-mail:
zink@ecs.umass.edu; Hermann Hellwagner, Christian Doppler Laboratory ATHENA, Alpen-Adria-Universität Klagenfurt,
Klagenfurt, Austria; e-mail: hermann.hellwagner@aau.at.
This work is licensed under Creative Commons Attribution International 4.0.
© 2025 Copyright held by the owner/author(s).
ACM 1551-6865/2025/7-ART198
https://doi.org/10.1145/3736306
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 2

```text
198:2
C. Timmerer et al.
1
Introduction
Over the last 20 years, video streaming has surged in popularity and now constitutes over more
than half of global Internet traffic [99]. This trend can be attributed in part to advancements in
video compression technologies, such as Advanced Video Coding (AVC) (2003) [122], High Effi-
ciency Video Coding (HEVC) (2013) [108], and Versatile Video Coding (VVC) (2020) [30, 31].
Each new generation of video codecs offers more than a 50% improvement in bitrate and qual-
ity, respectively. Additionally, developments in networking technology comply with Nielsen’s
law of bandwidth, which asserts that “a high-end user’s connection speed grows by 50% per year”
[88]. When combined with the increasing computational power of user devices (cf. Moore’s law),
this allows for the creation and consumption of video content anywhere and at any time across
various devices.
Video streaming has evolved from push-based, broad-/multicasting approaches with dedicated
hard-/software infrastructures to pull-based, unicast schemes utilizing existing Web-based infras-
tructure to allow for better scalability. When referring to this streaming approach, we use the
term HTTP Adaptive Streaming (HAS)1 consistently throughout this article. Standards helped
facilitate this process, notably MPEG Dynamic Adaptive Streaming over HTTP (DASH) and
Apple HTTP Live Streaming (HLS), although standards typically specify normative formats
(i.e., bitstream syntax) only, leaving non-normative parts open for (industry) competition. The
research community can play a crucial role in this ecosystem by researching innovative solutions,
specifically targeting non-normative aspects within these specifications.
In this article, our aim is to provide a brief (historical) background of HAS and a comprehensive
overview of research efforts related to key phases in modern HAS workflows; ranging from (i) video
encoding, (ii) delivery/networking, (iii) consumption/player, and (iv) end-to-end aspects including
Quality of Experience (QoE). For each of these phases, we will outline basic principles, current
trends, and future challenges for HAS.
The structure of this article is as follows. Section 2 covers the early history of video streaming
on the Internet, the rise of HAS and its fundamental principles, a brief summary of international
standards, and introduces key phases of HAS workflows. Section 3 describes the video coding for
HAS, including per-title encoding and recent optimizations, as well as energy-related concerns.
Section 4 addresses the delivery mechanisms in HAS, highlighting various transport options and in-
network optimizations. Section 5 examines the client-side consumption aspects of video streaming,
focusing on Adaptive Bitrate (ABR) algorithms and energy-related considerations. Section 6
discusses end-to-end aspects of video streaming, including QoE and energy efficiency. Section 7
explores potential future directions for HAS, and Section 8 wraps up the article.
2
Background
2.1
A Brief History of Video Streaming
The era of video streaming on the Internet dates back to the last decade of the previous century,
when The Rolling Stones were the first band to perform live on the Internet on 18 November 1994
[56]. It was the era of the Multicast Backbone (MBone) [42] and the first major broadcast streaming
event in 1995 with the Seattle Mariners vs. New York Yankees resulting in RealSystem G2 SureStream
technology (1998) as the first commercial ABR streaming system [38]. Frojdh et al. [47] describe
adaptive streaming within the 3GPP packet-switched streaming service that uses the Real-Time
Streaming Protocol, Session Description Protocol, and Real-Time Transfer Protocol (RTP) for
the setup and streaming phases of a streaming session. The Real-Time Control Protocol is used to
1Other terms often used interchangeably or in specific contexts are ABR streaming, DASH, HLS, Smooth Streaming, HTTP
Dynamic Streaming (HDS), Over-The-Top streaming, segmented HTTP streaming, Adaptive HTTP Streaming, and so on.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 3

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:3
adaptively change the transmission and content rates to the current network conditions. The first
YouTube video was uploaded on 23 April 2005 to herald a new era of video streaming over HTTP
[2] (although back then it required the Adobe Flash Player plug-in) supported by the emergence of
smartphones (e.g., iPhone introduced in 2007).
In early 2000, video streaming over HTTP, and consequently over TCP,2 was investigated by
Wang et al. [121] who concluded that “TCP generally provides good streaming performance when
the achievable TCP throughput is roughly twice the media bitrate, with only a few seconds of startup
delay,” providing a baseline for future development at that time. In general, video streaming over
HTTP can be roughly divided into the following techniques:
—Progressive download utilizes a single TCP connection to progressively download large video
files from a server. It enables playback while still downloading. The server aims to send the
file as fast as possible.
—Pseudo streaming basically mimics R(S)TP-based streaming as indicated above but enables
seeking via media indexing. The server paces transmission based on encoding rate.
—Chunked streaming divides the content into short-duration chunks which enables live stream-
ing and ad insertion.
—Adaptive streaming facilitates multiple versions of the content that enables to adapt to network
and device conditions.
The latter two can be used jointly and collectively referred to as HAS; pseudo streaming is not
used anymore, but progressive download is still used as a fallback mechanism. In the following, we
will briefly describe the main principles of HAS and provide an overview of the standardization
landscape.
2.2
HAS: Basic Principles
The basic principles of HAS are shown in Figure 1, comprising an HTTP server that hosts the
video content, a network with variable bandwidth conditions, and clients rendering the requested
video for the end users. The video content is typically segmented over time (e.g., a few seconds
per segment) and provided in multiple versions (e.g., resolutions, frame rates, bitrates, qualities,
codecs, languages) referred to as bitrate ladder. In addition to the segments, a manifest is pro-
vided that enables smart clients to issue timed HTTP requests for individual segments (or parts
thereof) from one of the multiple versions provided at the server, depending on the clients’ context
conditions including—but not limited to—device characteristics, network conditions, and user pref-
erences in order to maximize QoE. An important design choice comprises that servers host those
segments and its manifest, and clients decide which segments to request when. Thus, clients imple-
ment an ABR algorithm, not normatively specified within existing standards, subject to research
and development.
2.3
Overview of HAS Standards
The two main international standards in this space are (i) HLS [90] and (ii) MPEG DASH [57], which
replaced prior proprietary formats such as Microsoft Smooth Streaming and Adobe HDS. Both
standards define formats allowing implementation of the basic HAS principles as outlined above
with (minor) differences with respect to segment and manifest formats. The MPEG DASH data model
is shown in Figure 2 which comprises an XML-based Media Presentation Description as manifest
and allows the video content to be divided into periods for content slicing including ad support.
2We note that HAS is typically deployed via TCP for HTTP/1.1 and HTTP/2 unless explicitly mentioned for HTTP/3 or
QUIC which uses UDP.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 4

```text
198:4
C. Timmerer et al.
Fig. 1. Basic principles of HAS.
Fig. 2. MPEG DASH data model.
Each period comprises multiple adaptation sets of different modalities (e.g., video, audio, subtitles)
for component selection by clients. Each adaptation set provides multiple representations of the
same content with various characteristics (e.g., resolution, bitrate). Each representation provides
means to construct HTTP URLs for individual segments to be used by the client to download these
segments in a timely manner from the HTTP server.
The Common Media Application Format (CMAF) [58] aims to harmonize segment formats
towards the ISO base media file format adopted within both HLS and DASH. Furthermore, it
enables the implementation of Low-Latency (LL) live video streaming services by introducing
fragmented segment delivery. For HAS on Web browsers, W3C Media Source Extensions and
Encrypted Media Extensions are worth mentioning, which extend the HTML media elements (e.g.,
the source element) to allow JavaScript to generate media streams for playback, whereby an ABR
algorithm could be implemented in JavaScript [92].
In general, DASH and HLS can be used interchangeably without impacting the performance of
video streaming services [24].
2.4
End-to-End Video Streaming Workflow
End-to-end video streaming refers to the entire process involved in delivering video content from its
source (content creation) to the end user (playback). This comprehensive process involves multiple
phases, each critical to ensure a seamless and high-quality streaming experience. Figure 3 shows
the five key phases of the end-to-end video streaming pipeline, described as follows:
—Content Creation and Ingestion. This phase consists of two main procedures: Content creation
and content ingestion. Content creation is the initial step that involves the production of video
content, whether it is live broadcasts, pre-recorded shows, or user-generated videos. This
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 5

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:5
Fig. 3. Main phases of the end-to-end video streaming workflow.
content is captured using cameras or created using digital tools. Once created, the video is
ingested into the streaming platform’s infrastructure. Content ingestion involves uploading or
feeding the video data into the system, where it can be processed and prepared for streaming.
Several protocols are commonly used for content ingestion, each suited to different types
of content (e.g., live or on-demand) and network conditions such as Real-Time Messaging
Protocol, Secure Reliable Transport, RTP, Web Real-Time Communication, and File Transfer
Protocols (FTP, SFTP, Aspera).
—Encoding and Packaging. The next phase requires encoding and packaging the video data
into different representations and formats. The video data is encoded into digital formats
that are suitable for streaming. This process compresses the video to reduce its file size while
maintaining quality, using various codecs that will be investigated in Section 3. After the
encoding process, the encoded video is packaged in formats that can be efficiently delivered
over the Internet. Packaging involves segmenting the video, adding metadata (e.g., subtitles,
audio tracks, chapter markers), and wrapping it into a container (e.g., MPEG-DASH [57], HLS
[90], CMAF [58]) format that supports adaptive streaming and other advanced features [8].
—Content Delivery Network (CDN). The third phase focuses on distributing video segments
and optimizing traffic across multiple CDN servers to enhance QoE [20, 45]. This involves
spreading the video across a geographically dispersed CDN network (cf. Section 4).
—Transmission. The transmission phase in video streaming is a critical component of the end-
to-end pipeline, where the encoded video data is sent over the Internet to reach the user’s
device. This phase is heavily influenced by network conditions, which can vary widely based
on factors such as user location, network congestion, and the type of Internet connection
used. Section 4 explores various data transmission protocols and state-of-the-art approaches
used in video streaming applications.
—Playback and Rendering. In the final phase, the video is received by the end user’s device,
a smartphone, tablet, smart TV, computer, and so on. Based on the current situation of the
player (e.g., buffer occupancy and available bandwidth), the ABR algorithm of the player
determines the quality of next segment to be downloaded. In Section 5, we will introduce
various types of ABR algorithms. The device decodes the requested video stream and plays
it back to the user. The video is rendered on the device’s display, and the quality of this
rendering depends on the device’s capabilities, including screen resolution, processing power,
and software optimizations.
In this article, particular attention will be paid to video as a primary focus, given the preponder-
ance of existing research articles centered on HAS and video. However, this emphasis should not
overshadow the significance of other modalities, which remain crucial areas of study: these include,
but are not limited to, audio, subtitles, haptics, and mulsemedia. In particular, audio streaming in
conjunction with HAS is covered in [37, 95]. The integration of subtitles in HAS, as explored in
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 6

```text
198:6
C. Timmerer et al.
[36], further expands the scope of audiovisual communication. Additionally, the rapidly growing
interest in haptics and mulsemedia, as evidenced by works like [134] and [26], underscores the
diverse research landscape beyond video.
3
Video Coding for HAS
Video coding or compression is the core of video streaming, where uncompressed video is com-
pressed to fit the available bandwidth. Over decades, video codecs have evolved into sophisticated
systems that achieve a delicate balance between quality and efficiency. In Section 3.1, we review
the current state of video codecs. In Section 3.2, we will examine advancements in bitrate ladder
optimization. Additionally, while improving video codec efficiency, there is often an increase in
power consumption. Section 3.3 will explore the tradeoffs between compression efficiency and
energy consumption.
3.1
Overview of Video Codecs
A video codec is a sophisticated compression system that combines various techniques to effi-
ciently reduce the size of video data while maintaining high visual quality. It integrates both spatial
and temporal compression methods to exploit redundancies within and between video frames.
The process begins with partitioning, where each video frame is divided into smaller blocks for
more precise processing. Intra-frame prediction compresses individual blocks based on previously
encoded blocks within the same frame, exploiting temporal redundancy, while inter-frame predic-
tion enhances compression by referencing blocks in other frames, leveraging temporal redundancy.
Inter-frame prediction includes Motion Estimation (ME) and motion compensation, where the
movement of blocks across frames is encoded using motion vectors. Additionally, video codecs use
transform coding to convert spatial data into frequency coefficients, which allows the removal of
high-frequency data that human perception is less sensitive to. This is followed by quantization,
which reduces the precision of these coefficients to balance compression and visual quality. Finally,
entropy coding further compresses the quantized data by using shorter codes for more frequent
patterns. By integrating these methods, video codecs effectively compress data, making them
essential for modern video streaming, broadcasting, storage, and so on.
Over the years, several video coding standards have been developed, each offering improvements
in compression efficiency. One of the most widely adopted standards is AVC [122]. Introduced
in 2003, AVC revolutionized video compression by providing a significant reduction in bitrates
compared to previous standards like MPEG-2, without compromising video quality. The AVC
standard introduces several enhancements over prior video coding methods to improve coding
efficiency. These include variable block-size motion compensation, allowing for flexible and smaller
block sizes down to 4 × 4 pixels, and quarter-sample-accurate motion compensation, improving
on the half-sample accuracy of earlier standards. Motion vectors can now extend beyond picture
boundaries, and multiple reference pictures can be used for motion compensation, enhancing
prediction accuracy. The decoupling of referencing and display orders provides greater flexibility in
encoding, while weighted prediction and improved motion inference further refine the compression
process. Additional innovations include directional spatial prediction for intra-coding, in-the-loop
deblocking filtering to reduce artifacts, and a smaller block-size transform for more localized signal
representation. The introduction of hierarchical and short word-length transforms, exact-match
inverse transforms, and advanced entropy coding methods like Context-Based Adaptive Binary
Arithmetic Coding (CABAC) further boost efficiency. To enhance robustness and adaptability
across network environments, AVC includes features such as parameter set structures, flexible
slice sizes, flexible macroblock ordering, arbitrary slice ordering, redundant pictures, and data
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 7

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:7
partitioning. These advancements make AVC a highly efficient and flexible video coding standard
suitable for a wide range of applications.
In response to the growing demand for coding efficiency that surpasses the capabilities of AVC,
particularly with the emergence of ultra-high-definition formats like 4K and 8K resolutions, HEVC
was standardized in 2013 [108]. HEVC introduces several advanced features to enhance video
compression efficiency, particularly for high-resolution formats like 4K and 8K. The Coding Tree
Unit (CTU) structure is a key element, replacing the traditional macroblock with a larger and
more flexible coding unit. This allows for better partitioning and precise processing through a
quadtree structure that adapts the size of coding blocks and prediction blocks. HEVC also improves
motion vector signaling with advanced motion vector prediction and motion compensation, using
quarter-sample precision and more sophisticated filtering techniques. Intra-frame prediction is
significantly enhanced, offering 33 directional modes, compared to just 8 in previous standards.
The standard also includes improved quantization control, entropy coding through a more efficient
CABAC system, and advanced in-loop deblocking filtering. Additionally, HEVC introduces sample
adaptive offset, a technique designed to better reconstruct signal amplitudes by using a nonlinear
amplitude mapping, further enhancing visual quality.
The VVC [31] standard builds on the high-level syntax designs from AVC and HEVC, featuring
structured bitstreams, parameter sets, and an emphasis on advanced functionalities such as random
access and scalability. VVC introduces several sophisticated features to enhance coding efficiency
and flexibility: random access is facilitated, which helps balance coding efficiency with end-to-end
delay; reference picture resampling allows for resolution adjustments in inter-coded pictures to
improve efficiency; and new subpicture and virtual boundary features provide enhanced flexibility
for immersive and specialized video formats, such as 360-degree video. VVC also refines the use of
CTUs, slices, tiles, and wavefronts to optimize processing and access. The standard supports Scalable
Video Coding (SVC) with temporal, quality, spatial, and multiview scalability, simplifying the
design compared to previous standards, and facilitating easier adaptation for various applications.
Key advancements include more flexible block partitioning with larger sizes and varied shapes,
separate partitioning for luma and chroma, and innovations in intra-frame prediction with finer
angular directions and new interpolation filters. Additionally, VVC enhances inter-frame prediction
with improved motion vector coding, subblock-level motion prediction, and horizontal wrap-
around for immersive formats. Extended transform and quantization techniques in VVC improve
residual compression and adaptive quantization control, building upon HEVC’s capabilities to
further enhance efficiency and quality.
MPEG and ITU-T have jointly developed AVC, HEVC, and VVC standards, representing successive
generations of video compression technology. In parallel, video codecs like VP9 and AV1 [53],
developed by Google and the Alliance for Open Media, respectively, offer alternative approaches
with a focus on open standards and royalty-free solutions. Looking ahead, the next generation of
video codecs is anticipated to be driven by advances in Deep Neural Networks (DNNs), which
promise to further enhance compression efficiency and video quality through machine learning
techniques. Currently, two main exploration paths are being pursued: one focuses on replacing
components of traditional codecs with DNNs while maintaining the same overall structure, and
the other explores fully end-to-end neural network-based approaches. These developments aim to
push the boundaries of video coding by leveraging AI-driven methods to optimize encoding and
decoding processes in ways that traditional techniques may not achieve.
Despite SVC [100] being highlighted as a promising method for HAS in studies such as
[55, 83, 98], there has been a notable decline in its adoption or further exploration by both industrial
practitioners and academic researchers in subsequent years.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 8

```text
198:8
C. Timmerer et al.
3.2
From Static Bitrate Ladders to Dynamic, Live Per-Title Encoding
To allow clients to adapt to fluctuating network conditions, the same video is encoded at multiple
representations, collectively known as a bitrate ladder. A bitrate ladder specifies encoding parame-
ters such as bitrates and resolutions for each representation of the video. The size of the bitrate
ladders varies by application and, in the past, a large number of datasets emerged, e.g., [109] for
various video coding standards up to 8K resolution.
Although a fixed bitrate ladder is simple and convenient to use, since it does not require additional
processing, it is suboptimal because it fails to account for the specific characteristics of the video
content and the varying bandwidth requirements of users. For example, encoding all video content
at 8,100 kbps with a resolution of 1,920 × 1,080 in the HEVC format, may be suboptimal for both low-
and high-complexity videos. Low-complexity videos might achieve perceptually lossless quality
at a much lower bitrate, such as 2,000 kbps, which would result in a significant 6,100 kbps of
wasted bandwidth with no corresponding improvement in quality. Conversely, for high-complexity
videos, 8,100 kbps may be insufficient to achieve a high-quality representation, requiring a higher
bitrate to meet the quality standards necessary for optimal video streaming experiences. In addition
to optimizing the maximum bitrate required to achieve high quality, other encoding parameters
can also be fine-tuned. These include the number of representations, their corresponding bitrate,
resolution, frame rate, encoding preset, dynamic range, and more. By carefully adjusting these
parameters, it is possible to enhance video quality and streaming efficiency, ensuring that content
is delivered in the best possible way while minimizing unnecessary bandwidth usage.
Various methods have been proposed to optimize bitrate ladders. For instance, Tashtarian et al.
[112] introduced a method where the desired bitrate requests of all users are collected and used
to optimize the bitrates in the ladder. By analyzing the probability distribution of these desired
bitrates, the bitrates are selected to construct a more efficient and tailored bitrate ladder, ensuring
that the encoded video representations better match the users’ needs and network conditions.
However, this method requires a modification in the ABR algorithm of the clients. To address this
issue, ARTEMIS [111] proposes a mega bitrate ladder, where a large number of representations are
made available to clients, allowing them to select their desired representations. In this approach,
not all the representations in the mega ladder are encoded initially; instead, they are used to gather
data on users’ bandwidth requirements. Based on the probability distribution of these requirements,
a more efficient set of representations is selected for encoding, optimizing the video streaming
process to better align with the actual user demands. Similarly, COBIRAS [102] utilizes a bitrate
slide and just-in-time encoding to request segments with any arbitrary bit rate together with a
novel ABR algorithm.
Some methods focus exclusively on the quality of representations when constructing a bitrate
ladder, employing the concept of Just Noticeable Difference (JND). JND represents the smallest
variation in quality that an average viewer can detect. These methods construct a bitrate ladder by
including only those representations where the quality difference is perceptible, thereby reducing
redundancy and optimizing the selection of representations. For instance, in terms of Video
Multimethod Assessment Fusion (VMAF) [1], the JND is typically around six points, meaning
that a quality difference of six VMAF units between two representations is noticeable to viewers.
If the difference is less than six VMAF units, the two representations appear similar in quality
[15, 132]. By carefully selecting representations based on this JND threshold, these approaches
ensure that each step on the ladder reflects a significant improvement or decline in quality, thus
enhancing both streaming efficiency and viewer experience [18, 78].
Other methods focus on optimizing encoding parameters beyond bitrate. De Cock et al. [39]
encode a video at multiple bitrates and resolutions with quality assessments performed for each,
and then the resolution that delivers the highest quality for each bitrate is selected, optimizing the
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 9

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:9
resolution in the bitrate ladder. A similar approach is employed by Amirpour et al. [17], where not
only the resolution but also the frame rate is optimized for each bitrate. Guionnet et al. [50] add
dynamic range as an additional dimension for optimization.
While the above-mentioned methods typically rely on a brute-force approach to determine
optimal encoding parameters, such as resolution, other methods aim to predict these parameters
more efficiently. These predictive approaches are particularly valuable for live video streaming,
where real-time decision-making is essential. For instance, Katsenou et al. [64] propose a machine
learning method that predicts the crossover bitrate between optimized resolutions, improving
encoding efficiency. Similarly, OPTE [77] predicts the optimal resolution for each bitrate, further
streamlining the encoding process. These predictions often utilize video complexity features, with
methods like VCA [79], EVCA [13], and DeepVCA [16] proposed to extract spatial and temporal
complexity parameters. Finally, Telili et al. [116] benchmark both hand-crafted and deep learning-
based methods to predict encoding parameters, showcasing the potential of AI-driven approaches
in optimizing live video streaming.
3.3
Energy Efficiency in Video Coding
The energy consumption of video encoding is influenced by multiple factors, including codec
selection and encoding parameter configurations. Additionally, HAS encodes videos in multiple
representations (bitrate ladder), typically a computationally intensive process.
Encoding complexity directly correlates with energy consumption [63] due to the higher compu-
tational power required for intricate algorithms and calculations. Each codec generation achieves
approximately 50% coding efficiency gain over the previous generation, at the cost of increased
computational complexity, longer encoding times, and higher energy consumption [96]. For exam-
ple, AVC consumes over four times more power than earlier standards like MJPEG and MPEG-4
Part 2, due to more and refined compression techniques such as multiple reference frames in AVC
[103, 119]. HEVC further enhances compression efficiency by 25.1% over AVC but also increases
energy consumption by 17.4% [81]. Search Range (SR), a crucial parameter in ME, significantly
contributes to this higher energy demand, among other factors. VVC’s complexity is eight times
higher than HEVC [27], resulting in a fourfold increase in energy consumption [32]. In contrast,
AV1 offers a better tradeoff between coding efficiency and energy consumption compared to AVC,
HEVC, VP9, and VVC [32].
Encoding parameters significantly influence energy consumption [80]. Resolution directly impacts
energy consumption, with a linear relationship between pixel count and energy consumption.
Frame rate directly correlates with energy consumption due to increased computational demands.
Consequently, doubling the resolution while halving the frame rate maintains energy consumption.
Presets (AVC, HEVC, and VVC) and speed settings (AV1 and VP9) determine the tradeoff between
the encoding speed and the compression efficiency [14, 32, 105]. Higher quality settings (i.e.,
slower presets and lower speed settings) increase encoding time and energy consumption due
to more complex tools and extensive search spaces [80] explored to choose the most efficient
coding configurations [32]. For example, Silveira et al. [105] observed a 45-fold energy consumption
increase when moving from the ultrafast to placebo x265 preset, with a corresponding 145%
energy increase per 1% bitrate reduction. Notably, different quantization parameter configurations
have an exponential impact on power consumption [103]. Other encoding parameters, such as the
number of reference frames, SR, subpixel accuracy, and the ME algorithm significantly influence
power consumption, with variations up to 10% reported in [103]. Monteiro et al. [81] found that
while the ME range minimally affects the compression efficiency in HEVC, energy consumption
increases disproportionately with increased ME range.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 10

```text
198:10
C. Timmerer et al.
HAS bitrate ladder construction is computationally expensive. Eliminating perceptually redundant
representations through VMAF score comparison and removal of higher bitrate representations
when perceptually lossless can significantly reduce energy consumption [125]. Content-ABR ladder
construction, considering the content type and user-perceived quality metrics, can further optimize
energy efficiency by reducing unnecessary bitrates while maintaining video quality [68].
Video encoding distribution in the computing continuum addresses computational challenges
by distributing video encoding tasks across multiple instances in cloud and fog infrastructures.
Oikonomou et al. [89] propose a multi-objective heuristic approach for scheduling video transcoding
tasks in geographically distributed cloud data centers, optimizing total time and energy consump-
tion. The scheduler estimates performance metrics for each data center task assignment considering
network distances, server capacity, and workload, potentially using Pareto optimality for efficient
video transcoding in the cloud. MAPO [76] utilizes a genetic multi-objective optimization algorithm
to determine task placement on fog instances, optimizing total time, energy consumption, and
price. VE-MATCH [4] proposes a matching game-based task scheduling approach to optimize
resource allocation between media and resource providers. GreenFog [84] optimizes energy use
by utilizing renewable energy sources for fog computing. The framework employs optimization
techniques, including a heuristic linear regression approach and a machine learning-based Multi-
Armed Bandit method. These techniques allow GreenFog to adapt to real-time energy availability.
EFFECT [130] introduces an energy-efficient fog computing framework designed for real-time
video processing. EFFECT tackles the challenge of balancing energy consumption with latency
deadlines employing a two-fold approach. First, a centralized resource allocation scheme distributes
sub-channels, transmission, and processing power considering task complexity and deadlines.
Second, a distributed game-theoretic approach allows instances to strategically decide between
local processing or offloading tasks to fog servers, minimizing their energy footprint.
4
Video Delivery in HAS
The significant rise in the popularity of video streaming applications has created challenges for
the scalable delivery of multimedia content to viewers. This section discusses various technologies
developed to address these challenges, focusing on methods that operate within the network and
those that function end-to-end between the content server and the client.
4.1
In-Network Support of HAS Delivery
The distribution of video content in today’s Internet heavily relies on in-network functions that
increase the scalability, quality, and manageability of streaming applications. In the following, we
briefly describe these functions and their evolution over the past two decades.
Caching. Caching in the network is a major component that increases the scalability of video
streaming applications. Caching hierarchies of CDNs take the load of the content provider’s origin
server by caching hot objects [33, 74], specifically, hot video segments in the case of HAS. While
the term hot video segments is not well defined, it usually refers to the segments that are being
requested the most and especially are more likely to be requested in the future.
In terms of performance and scalability, caching systems are measured through user- and content
provider-facing metrics as well as internal metrics. The first category comprises metrics that directly
influence the user experience (QoE), e.g., the round-trip delay from requesting the video segment
until receiving it. Provider-facing metrics include, for example, the offloading ratio, i.e., the ratio of
requests or traffic that are serviced by the caching hierarchy to the number of overall requests or
data traffic. Finally, internal performance metrics of CDNs include the storage utilization of caches,
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 11

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:11
individual cache hit rates as well as the hierarchy hit rate and the midgress, i.e., the traffic sent
between caches and caches and the origin server to update the content.
Extensive work has been conducted on the evaluation of caching strategies for single (edge
caching) systems as well as for entire hierarchies [3, 25, 133]. One main goal of these works is to
use the object request patterns to determine which segments are admitted to the cache (and for
how long) [48]. Along these lines, one can categorize these works into those that consider capacity-
constrained caches vs. those that consider timer-based caches. Additionally, these works can be
divided into event-based methods that update their decisions on segment admission and cache
content whenever a segment is requested vs. works that update the cache content on a discrete-time
basis. Finally, as observed in the literature, the analysis and optimization of video streaming caching
systems is in general a complex problem which does not easily lend itself to analytical closed-form
results. To this end, several model-free methods exist that utilize the metadata observed from the
segment request processes to learn good cache content decisions or continuously optimize the
content admission and retention policy.
Software-Defined Networking (SDN) Support/Server and Network-Assisted DASH (SAND).
With the emergence of SDN, new video distribution methods were introduced that incorporated
in-network functionalities, diverging from the traditional end-to-end model of the Internet. The
common goal of these approaches is to increase the viewers’ QoE by assisting clients in the
appropriate selection of DASH segments’ representations. Cofano et al. [35] were among the first
to propose a network-assisted approach that uses SDN to provide QoE fairness between DASH
clients. An approach that uses SDN to facilitate bitrate adaptation support for DASH clients was
introduced by Kleinrouweler et al. [67]. Similarly, SDNDASH [19] presents an SDN-supported
resource allocation and management approach that also aims to maximize the QoE of the client.
SAND is an MPEG standard [59] that was introduced to enable communication between streaming
clients and network elements/servers like caches. It offers standard interfaces for the communication
between these elements. The goals of SAND are optimized operations with caches, the support of
consistent and high-level QoE for viewers, and QoE measurement features to improve streaming.
By providing real-time information about network and client performance, SAND enhances the
efficiency of streaming sessions. Consequently, SAND enables intelligent caching, processing, and
delivery optimizations in the network and on servers, allowing clients to provide feedback on
anticipated segments and bandwidth requirements and better adaptation of clients due to server-
side/network information. While traditional CDNs provide some of the functionalities offered by
SAND, they are rather limited and inert.
Combining SDN and SAND [25, 67, 91] was a natural consequence, as it efficiently handles SAND
communication between network elements. The common concept of these approaches is to use
controllers in the network that provide network-assisted ABR streaming, intending to improve the
viewers’ QoE.
Edge Computing Support. Processing and storage facilities at the network edge, either at CDN
edge servers or at edge cloudlets of mobile (4G/5G) networks, can improve HAS delivery [61, 62, 123].
To that end, both HAS clients’ behavior and (radio) network parameters can be taken into account
at the edge. An edge node can utilize the information and behavioral parameters of all served
clients to acquire a broader (beyond a single client’s) context to enhance the clients’ QoE and
QoE fairness, perform bitrate adaptation that mitigates potentially harmful selfish client behavior,
improve resource allocation, or save resources. Functions performed at the edge include segment
prefetching [10] and caching, transcoding, and re-packaging, edge-based ABR algorithms [7, 9]
and stream analytics, machine learning techniques, e.g., to learn and predict the clients’ segment
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 12

```text
198:12
C. Timmerer et al.
request patterns, Super-Resolution (SR) and other computations offloaded from end devices, and
enabling/supporting 360-degree and immersive video streaming.
As an example, transcoding at the edge has the goal of reducing the load on the backhaul network
by transcoding segment representations from already existing ones on edge devices, often just
in time when a video segment is requested. To this end, the edge does not need to keep different
segment representations in cache or treat these as individual objects, but rather uses the fact
that quality representations can be deduced from each other. This was, for instance, intensely
investigated in a scheme called Light-weight Transcoding at the Edge [41]. A popular application of
edge transcoding lies within HAS streaming of 360-degree tiled content since in this case there are
many more combinations of video tiles and quality representations leading to a high number of
video segments. The transcoding service at the edge aggregates requests of segments of the same
tiles in different representations and transcodes the replies individually, or it creates individual
representations on the fly from cached ones.
Several sophisticated collaborative SDN-based and edge-assisted HAS delivery architectures were
proposed and evaluated, e.g., in [44, 46]. Such systems are designed to reduce both the latency of
serving segments to HAS clients and, for instance, the delivery (bandwidth) costs. In general, there
is a “rich design space for jointly optimized SDN-assisted caching architectures” [25] for HAS, and
these designs are initial attempts to explore this design space.
Information-Centric Networking (ICN)/Named Data Networking (NDN). While CDNs have
been a significant contributor to the success of video streaming, they also introduce a significant
amount of complexity. One of the major reasons for this complexity is that one of the Internet
Protocols’ major principles is that content can only be addressed by a hostname or an IP address.
Consequently, CDNs operate a complex ecosystem of dynamic DNS approaches, caching and
prefetching strategies, and load balancing [74]. The paradigm of ICN [11] has the goal of replacing
this tight coupling between data and location by introducing named data as a core principle. At
first sight, ICN seems to be an ideal approach to natively support video streaming applications. For
example, a request for a DASH segment issued by a video player can be served by any cache that
holds the content with that exact name of the segment, assuming the cache is located on the path
between the client and the origin server. ICN approaches like CCN [60] and NDN [129] propose
caching functionality at each router within the network. At first glance, video streaming would
tremendously benefit from in-network caching since content (e.g., video segments) can be directly
served from routers along the path to the origin. Although ICN has been a prominent research topic
over the past decade, any large-scale deployments video streaming applications could benefit from
have not been established. Since ICN replaces the IP layer of the current Internet, such a significant
change is extremely hard to implement. In addition, the in-network caching approach can lead to
significant QoE impairments due to bitrate oscillations, as demonstrated by Grandl et al. [49].
4.2
Role of Endpoints for HAS Delivery
In this section, we discuss the end-to-end support for HAS delivery which is usually found on
end-clients as a layer bridging the HAS application and the network stack. Given this architectural
view, we categorize this endpoint support into both directions, first in the direction of the HAS
client application, i.e., in terms of the interface and the guarantees provided, and secondly into the
direction of the network stack in terms of how the network data packets are formed and transmitted
to provide these end-to-end guarantees.
TCP/QUIC. Coming from the traditional TCP support for HAS, QUIC emerged as a proto-
col with a high potential of solving traditional pain points of TCP support for HAS delivery.
As Video-on-Demand (VoD) delivery requires in-order delivery guarantees, TCP with its
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 13

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:13
connection management, retransmission mechanisms, and Congestion Control (CC) has been
the primary vehicle for HAS VoD for a long time. The major drawbacks associated with the tradi-
tional narrow waist of HAS delivery, i.e., TCP under HTTP, can be summarized as follows: (i) TCP
connection establishment is unnecessarily long. (ii) HAS is not a typical long-lived data stream
that falls within the traditional scope of TCP (ramping up to long-term transmission rate fairness).
Instead, HAS is known for an ON-OFF triggered transmission that is due to the segment-based
requests, in the form of HTTP GET requests. This transmission is known to be TCP-submissive
in terms of a lower expected long-term rate. Note that the ON-OFF triggered transmission is
directly attributed to the HAS client and its use of the HTTP layer. For example, assuming a simple
buffer-based quality adaptation mechanism at the HAS client and assuming a full playback buffer,
the client periodically requests a segment with a period length corresponding to the segment
playback length. It was shown that this behavior leads to suboptimal transmission rates, as TCP
is not able to continuously keep a high transmission rate with such short bursts and very few
network status signals (acknowledgments). (iii) HAS over TCP constitutes a double rate control
loop, i.e., the quality adaptation module of the client estimates the end-to-end available bandwidth
based on coarse signals, e.g., dividing the number of bits in a segment by its download duration,
while TCP estimates this rate within its CC modules based on per-packet (per-ack) signals. (iv)
Retransmissions of single packets within TCP lead to head-of-line blocking at the client side, i.e., the
in-order delivery of the segment up to the application is throttled by the FIFO delivery of packets
over the network. Especially at the server side (but also within the network) it is impossible to
differentiate and hence expedite the transmission of an urgent retransmitted packet in comparison
to previously scheduled packets that, however, belong to a later segment.
In the context of HTTP/3, QUIC has emerged as a viable alternative to TCP. While it does not
explicitly address all the shortcomings listed above, it provides the protocol architectural tools to
address these. In addition, it was shown to perform better than TCP due to the new design. With
respect to HAS, the main difference in using HTTP/3 over QUIC is that it introduces the concepts
of streams and subflows on top of connectionless UDP flows. The QUIC library allows, hence, to
rapidly prototype different CC and reliability schemes in user space on top of simple connectionless
flows. While stream multiplexing has been known from the Stream Control Transmission Protocol it
received an Internet-wide deployment with QUIC. Stream multiplexing allows concurrency between
the data streams and hence differentiated transmission scheduling of application-defined streams.
This differentiation can be, for example, in terms of a stream for fresh segments (or their packets)
and a stream for retransmitted segments (or their packets), where the second stream possesses a
higher priority than the first one. This would solve the above head-of-line blocking problem. The
stream multiplexing and demultiplexing mechanism of QUIC lends itself well to multipath delivery
of HAS since it allows QUIC, in contrast to Multi-Path TCP, to map streams to subflows that
are bound to physical network interfaces. This flexibility allows tying the measured performance
metrics (e.g., packet loss, delays) on a certain network interface to scheduling decisions of different
streams such as scheduling fresh segment packets or retransmitted ones. As the QUIC library
runs in user space, it also allows rapid prototyping of such strategies, e.g., for retransmissions,
scheduling, interface bandwidth estimation, and mapping of streams to interfaces.
CC. The impact of CC on the performance of HAS delivery has been widely studied, specially,
as new CC mechanisms, such as bottleneck bandwidth and round-trip propagation time, are known
to be unfair to older TCP CC connections. It is evident that the CC mechanism, which throttles the
packet sending rate on the HAS server side, has a direct implication on two available bandwidth
estimates on the HAS client side, the first being the transport layer estimate in CC or QUIC while
the second is the coarse available bandwidth estimate within the HAS client application. Hence,
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 14

```text
198:14
C. Timmerer et al.
more aggressive CC in terms of expected sending rates higher than the fair share or small-scale
bursty transmission behavior are expected to provide higher QoE in HAS delivery as long as they
push out other competing, less aggressive dataflows. Studies as early as [107, 110] showed that given
varying network contexts, i.e., different measured network performance metrics, different common
configurations of the HAS stream and the network stack provide varying HAS performance. This
observation comes in line not only with the idea of adaptivity within the CC mechanism, but also
as a basis for data-driven CC. In this sense, HAS players would train neural networks that map the
number of signals received by the HAS delivery mechanism to decisions on the transmission rate
of segments, as well as decisions on the quality of the requested segments. These neural networks
can be trained in a federated fashion, first, to learn optimal transmission decisions from a larger
number of HAS clients without centrally collecting data and, secondly, they can be trained in an
online reinforcement learning manner to adapt the transmission behavior at runtime.
LL DASH and HLS. As introduced in Section 2, CMAF facilitates LL video streaming services:
fragmented segment transmission (delivery in so-called chunks) allows a segment to start playing
before being fully received by the client. Both relevant HAS standards have LL versions, LL-DASH
and LL-HLS, allowing the end-to-end latency to be reduced to a few seconds only [24]. The body of
research addressing LL HAS encompasses earlier works such as [28], focusing on overhead and
performance evaluations, and extends to more sophisticated and recent contributions, e.g., [70],
which provides a novel LL ABR algorithm for HAS. Additionally, a comprehensive, up-to-date
survey has been conducted and is documented in [21]. Various performance assessments have been
performed, including those over satellite communication channels as detailed in [131], and those
concerning player performance, which are addressed in [128].
5
Video Consumption in HAS
Content consumption in HAS refers to the final end points facing the end user. It mostly concerns
the player which hosts the ABR algorithm responsible for requesting video segments over best-
effort networks, and, recently, energy-aware/-efficient ABR algorithms have been proposed in the
literature, which are briefly reviewed in this section.
5.1
ABR Algorithms: State of the Art and Recent Advances
The ABR algorithm (or logic), as introduced earlier, is the central component in every HAS player
and explicitly impacts the QoE. It is typically located at the end user devices and issues timely
HTTP GET requests for segments depending on the client’s context characteristics and conditions.
Multiple surveys related to HAS, ABR, and QoE have been published in the past [23, 101] and
specifically Bentaleb et al. [23] cluster ABR algorithms into (i) client-based, (ii) server-based,
(iii) network-assisted, and (iv) hybrid adaptation schemes. Client-based adaptation schemes are
further subdivided into (a) bandwidth-based, (b) buffer-based, (c) proprietary solutions, (d) mixed,
and (e) Markov decision process-based adaptation schemes. While existing surveys provide a good
basis to get an overview, new ABR algorithms have been proposed in the meantime, which are
briefly outlined as follows.
DoFP+ [85] introduces a novel ABR algorithm that takes advantage of the features of HTTP/3 to
enhance QoE in HAS. The authors present the DoFP+ algorithm as a solution to the limitations of
existing ABR algorithms, which often fail to capitalize on advances in HTTP versions, particularly
HTTP/3. DoFP+ utilizes key features of HTTP/3 such as stream multiplexing, stream priority, and
request cancelation. These features allow the algorithm to improve low-quality video segments in
the client’s buffer while concurrently downloading new segments. Experimental results show that
DoFP+ significantly improves QoE, reducing the number of stalls (i.e., buffering events) by 86%
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 15

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:15
and stall duration by 92% compared to other state-of-the-art ABR algorithms. Moreover, DoFP+
achieves up to a 33% improvement in QoE and saves up to 16% of downloaded data, making it both
effective and efficient.
Another promising ABR is termed Weighted Sum Model for HTTP Adaptive Streaming
(WISH) [86], which provides a user-centric bitrate adaptation method designed to improve QoE
for mobile video streaming. The primary idea behind WISH is to allow users to prioritize different
aspects of streaming, such as video quality, stall events, and data usage, according to their prefer-
ences. The WISH algorithm does this by calculating an overall cost for each video segment, which
is a weighted sum of three factors: (i) throughput cost, (ii) buffer cost, and (iii) quality cost. The
segment with the lowest overall cost is selected for streaming. WISH significantly improves QoE,
improving performance by up to 17.6% while saving 36.4% in data usage, making it efficient for
mobile networks. It also allows users to customize their streaming experience by adjusting the
weights of different factors such as video quality and data usage. However, this flexibility can lead
to increased video instability, with more frequent quality switches, and the algorithm’s complexity
may make its implementation more challenging. Additionally, under severe network fluctuations,
WISH might cause occasional video stalls, though it generally minimizes these issues. Despite these
drawbacks, WISH is a notable advancement in adaptive streaming.
Nguyen et al. [87] introduce a novel approach leveraging a lightweight SR network called SR-ABR
Net. This approach improves video quality on mobile devices while reducing bandwidth usage.
One of the primary advantages of this method is its ability to run in real time on mobile devices,
improving visual quality by up to 7% and reducing data usage by as much as 43% compared to
traditional methods. However, the complexity of integrating SR with ABR algorithms may pose
implementation challenges, particularly in ensuring compatibility across diverse mobile devices.
Additionally, while the approach effectively minimizes stalls and improves quality, it may require
high computational power on some devices, which could limit its applicability. Despite these
challenges, the method represents a significant advance in mobile video streaming, offering a
balance between high-quality viewing experiences and efficient data usage. LiveNAS [66] also
utilizes SR but for ingest at the origin server showing 1,269% QoE improvement, which has been
extended to NeuroScaler [124] to enable efficient and scalable neural network enhancements for
live streams.
COBIRAS, as introduced earlier, comes with the MinOff ABR algorithm [102] that can work
on top of existing algorithms (in this article MinOff extends dash.js’ Dynamic ABR algorithm) to
minimize OFF phases. Therefore, MinOff utilizes both the throughput factor and the buffer size
to determine the bitrate for the next video segment, keeping the video buffer at the given target
level below the maximum buffer size. Testbed results have shown that MinOff increases bandwidth
utilization to approximately 90% compared to state-of-the-art ABR algorithms that operate at
approximately 60% bandwidth utilization.
Bentaleb et al. [22] propose the Ahaggar ABR algorithm using meta-reinforcement learning
and Common Media Client Data/Common Media Server Data (CMCD/CMSD) including
a comprehensive evaluation. The meta-reinforcement learning is located at the server taking
content (i.e., the actual content to be streamed to the client) and context conditions (i.e., network
conditions and client/device characteristics) as input to guide bitrate decision-making at the
client. For communication between server and client, CMCD and CMSD are used, respectively.
Experimental results confirm that Ahaggar improves streaming performance using a wide range of
network conditions (i.e., various network traces) and client configurations (i.e., resolutions ranging
from mobile devices up to ultra high definition compared to state-of-the-art ABR algorithms.
LL ABR algorithms in the context of HAS are surveyed in [21] which comprehensively reviews
the evolution of live video streaming with respect to latency, ranging from high latency (45 s) to
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 16

```text
198:16
C. Timmerer et al.
near-real-time latency (100 ms). Several LL ABR algorithms are reviewed, notably Low-on-Latency,
Learn-to-Adapt (L2A), and Standard Low-Latency Video Control, which have been evaluated
in the context of the Twitch grand challenge on adaptation algorithms for near-second latency at
ACM MMSys 2020 where L2A has been announced as the winner due to its accurate bandwidth
measurements and innovative learning-based rules for bitrate selection. The survey concludes with
the need for more work regarding LL streaming, specifically for immersive video applications
potentially utilizing analytics and AI-assisted solutions.
5.2
Energy-Aware/Energy-Efficient ABRs
Energy-aware ABR algorithms are designed to optimize video delivery by dynamically adjusting
the quality of video streams based on the user’s network conditions and the energy efficiency of
the device [118]. Unlike traditional ABR algorithms, which primarily focus on network bandwidth,
energy-aware ABR considers the power consumption of the user’s device, aiming to balance
video quality with energy usage across all processes involved, from encoding to playback. This
approach is particularly important for mobile devices, where conserving battery life is critical while
maintaining an acceptable viewing experience [72]. By intelligently managing both bitrate and
energy consumption, energy-aware ABR enhances user satisfaction by providing longer streaming
times without compromising video quality too much.
GreenABR [118] and GreenABR+ [117] introduce a novel ABR streaming algorithm designed to
optimize energy consumption during video streaming without compromising users’ QoE. The key
idea behind GreenABR is its focus on reducing the energy usage of mobile devices by incorporating
energy consumption as a critical factor in its decision-making process. Unlike traditional ABR
algorithms that primarily aim to optimize video quality and reduce buffering, GreenABR utilizes
Deep Reinforcement Learning (DRL) to intelligently select bitrates based on real-time network
conditions and the energy consumption patterns of the device. GreenABR offers significant energy
savings of up to 57% over other ABR algorithms while enhancing video quality by using VMAF to
optimize bitrate decisions and reduce rebuffering. However, its reliance on DRL adds complexity
and demands substantial computational resources for training, which may pose challenges for
implementation on low-power devices. LL-GABR [93] extends GreenABR with respect to LL based
on existing bandwidth measurements to stay within given latency limits while improving QoE
(44%) and energy efficiency (73%).
Lorenzi et al. [72] extend WISH to E-WISH by integrating energy awareness into its decision-
making process, considering available throughput, player buffer, video quality, and energy costs.
The key advantage of E-WISH is its ability to reduce energy consumption by up to 12% while im-
proving QoE by up to 52% compared to other state-of-the-art approaches. However, the algorithm’s
complexity, including the need to balance multiple costs, may present implementation challenges,
particularly in determining the optimal weight for energy consumption in diverse scenarios.
6
End-to-End Video Streaming Aspects
6.1
End-to-End Optimizations
End-to-end optimization is essential in video streaming, especially for live applications, where LL
and high QoE are critical. Live streaming requires real-time content delivery across varying network
conditions and devices, making efficient solutions necessary to address challenges throughout the
streaming pipeline. Solutions like HxL3 [113], LALISA [112], QuaLA [114], ARTEMIS [111], and
ALPHAS [115] focus on optimizing this entire process.
HxL3 [113] proposes a novel architecture to address the end-to-end challenges of LL live streaming
over HAS. The HxL3 architecture is designed to be protocol-agnostic, working with both HTTP/1.1
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 17

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:17
and HTTP/2.0, and supports various codecs like DASH and HLS. It optimizes live streaming
by leveraging efficient caching, prefetching, and transcoding mechanisms at the edge, reducing
rebuffering, startup delay, and overall end-to-end latency. Experimental results demonstrate HxL3’s
ability to provide high-quality viewing experiences across geographically distributed networks,
outperforming traditional live streaming methods in terms of latency and viewer QoE. QuaLA [114]
is a distributed end-to-end approach designed to optimize video quality and latency for live UGC
streaming. It leverages 5G and edge computing, using the ProxJ-ADMM technique to efficiently
manage multiple concurrent streams without additional signaling. Real-world experiments on
CloudLAB show that QuaLA improves video quality by over 57% while maintaining fairness and
LL compared to traditional methods.
In another end-to-end study, we proposed LALISA [112]. It is a content-aware and LL ABR
streaming approach that dynamically adjusts video bitrates based on the complexity of the video
content and available network conditions, aiming to improve both latency and QoE for viewers.
The main drawback of LALISA is that it requires modifications to the video player in order to send
the desired bitrate, which can limit its deployment flexibility. This approach demands changes
in the client-side infrastructure, making it more difficult to implement in environments where
modifying players is impractical or not feasible, such as with a wide variety of heterogeneous
devices. This contrasts with solutions like ARTEMIS [111], which operate transparently without
requiring any modifications to the player, allowing for easier integration and broader scalability.
Similar to LALISA, ARTEMIS also focuses on optimizing bitrate ladders but goes beyond content-
awareness by incorporating real-time, client-side metrics such as stall duration and bitrate requests,
as well as origin-side video quality information measured through PSNR. ARTEMIS dynamically
constructs and adjusts bitrate ladders during live streaming sessions, allowing it to adapt not only to
the video content but also to fluctuating network conditions and heterogeneous client capabilities.
This enables ARTEMIS to deliver significant performance improvements over static ladders, such as
reducing encoding computation by 25%, lowering end-to-end latency by 18%, and enhancing QoE by
11%. The system’s ability to optimize both content and network utilization makes it a scalable and
efficient solution for live video streaming environments. ALPHAS [115], an extension of ARTEMIS,
tackles the challenge of determining optimal bitrate ladders for multi-live streaming. It introduces
an optimized encoding service that coordinates CDN-assisted bitrate ladder adaptation, optimizing
the delivery of multiple live streams to heterogeneous clients across different zones via CDN edge
servers. ALPHAS accounts for CDNs’ bandwidth constraints, encoders’ computational capabilities,
and supports stream prioritization. Additionally, ALPHAS consistently outperforms ARTEMIS
in multi-objective performance, achieving QoE improvements of up to 10% in static subscription
scenarios and 20% in dynamic ones.
6.2
Energy Efficiency
Video streaming involves various key phases as outlined above. These phases collectively account
for the majority of the energy consumption in video streaming. Accurate estimation of this energy
consumption is essential for assessing its environmental impact and driving sustainability initia-
tives. Existing estimates vary widely due to methodological differences and reliance on outdated
data, e.g., [75].
The state-of-the-art methods used to measure energy consumption in video streaming can be cat-
egorized into two groups: (i) top-down and (ii) bottom-up. These approaches offer different perspec-
tives on the assessment of carbon emissions and energy consumption within the digital landscape.
—Top-down approaches offer a broad overview of energy consumption at a large scale, attempting
to derive overall trends and patterns. The top-down approach involves calculating the carbon
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 18

```text
198:18
C. Timmerer et al.
intensity or energy intensity based on total historical estimates. It considers factors such as real
energy consumption data over a specified period of time divided by the total data processed
or transferred through the network, as well as the number of end users. This approach has
been employed in various studies, e.g., [40, 75].
—Bottom-up approaches provide finer-granular insights into energy consumption by analyzing
individual components. Bottom-up methods involve summing up the carbon emissions or
electricity consumption of components. These methods are more accurate than the top-down
approaches since they focus on detailed measurements. However, they can be more complex
and time-consuming to implement, especially for large-scale systems. Energy-intensive com-
ponents often include encoding schemes, resource scheduling, storage, CDNs, routers, access
points, content retrieval, decoding, and display. Studies like [97, 126] have used the bottom-up
approach to analyze specific components.
Although it is essential to carefully optimize the energy consumption of individual components
in video streaming systems to avoid unnecessary processing burdens [68], it is equally important
to consider the whole system [6]. Optimizing one component can inadvertently increase the
energy consumption or computational load of another. For example, advanced video codecs can
effectively reduce data transmission and its associated energy costs, but may also introduce higher
encoding and decoding complexities, demanding additional resources from other components [54].
Therefore, a comprehensive system design that takes into account the interactions and dependencies
between components is crucial to maximize energy savings. Considering the system as a whole,
it is possible to identify and implement optimizations that benefit the overall energy efficiency
without introducing new bottlenecks or inefficiencies.
7
Possible Future Work for HAS


Video Coding. The current reference for video coding (for HAS) is VVC and the future, at least from
an MPEG/ITU-T point of view, can be divided into enhanced compression beyond VVC capability
and neural network-based video coding. While the former aims to improve compression capabilities
with traditional methods, the latter targets AI-based techniques. Therefore, we witnessed several
emerging techniques: (i) learned video coding also known as end-to-end deep video coding [73],
(ii) deep learning-based video coding [71], and (iii) neural implicit representation for videos [34].
However, its integration with HAS remains underexplored in existing literature. An exception is
LapisGS [104], which is based on 3D Gaussian Splatting [65], a technique to generate 3D repre-
sentations from images. Interestingly, LapisGS proposes a layered approach for 3DGS encoding,
similar to SVC, supporting adaptive streaming and seamless rendering.
Video Delivery. CDNs are carrying the majority of Internet traffic today and will continue to
serve as a major backbone for popular content and media data distribution, with improved and
specific services for HAS. With both CDN providers and mobile network operators opening up
their network edges for third parties to inject code, e.g., content providers or streaming services
providers, edge support for HAS will grow. In particular, machine learning at the edge is expected
to play an increasing role in implementing many of the edge functions described in Section 4.
Immersive content, e.g., point cloud streaming, will significantly benefit from this, e.g., for view
prediction or (partial) rendering at the edge. With SDN in place and Network Function Virtualization
being facilitated by network operators, sophisticated caching and distribution architectures as
indicated in Section 4 will gain ground. Delivery systems thus can be tailored to the needs of
content/service providers, customers, contents, or events; the complexity of designing, setting up,
and running such systems will be challenging to manage. A further open challenge is to realize
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 19

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:19
LL live streaming both at scale and at reasonable costs. Recently, IETF started Media over QUIC
(MoQ) with the aim to converge traditional video streaming with conversational services (e.g.,
video calls) towards a single solution. Initial findings are reported [52], a testbed is available [51],
and adoption for immersive media is ongoing [94], but it is still in its infancy. Additionally, L4S (LL,
Low Loss, Scalable throughput) [29] has been the subject of several research articles related to HAS.
Notable contributions include, for example, the development of adaptable L4S CC mechanisms
[106]. In addition, there has been research dedicated to the selective enablement of L4S transport
protocols [69]. Furthermore, the application of L4S in private 5G industrial networks, particularly
in the context of facilitating real-time video streaming, has also been explored [82]. Thus, further
integration between application and transport/network layers is anticipated in future research.
Video Consumption. While ABR algorithms, their impact on QoE, and LL aspects for VoD and
live services have been extensively researched in the past two decades, future work in this area
will certainly increase efforts in energy efficiency, which is currently in its infancy. Other aspects
will be related to novel use cases and content modalities collectively referred to immersive media
ranging from 360-degree video to volumetric content, e.g., point clouds or/and holographic content,
as outlined in [120]. Independent of the actual use case, the ABR algorithm at the end user device
will certainly be a critical component of the streaming workflow.
End-to-End Video Streaming. Optimizing end-to-end video streaming at scale for both live
and VoD services remains a challenge. Various approaches reviewed in this article suggest in-
network/edge (AI) support while others favor keeping complexity at end points, but with explicit
communication among them (e.g., CMCD/SD) in the context of MoQ. Apart from that, approaches
like DeepStream [12], LiveNAS [66], or NeuroScaler [124] effectively combine traditional video
streaming with neural network-based quality enhancements to improve video streaming perfor-
mance leveraging GPU-based compute capabilities along the video delivery pipeline including
client devices. Further research in this direction is crucial to increase efficiency, reduce costs, and
environmental impact of deployed solutions at scale. With the emergence of large language models,
generative AI has entered our everyday’s life which will also impact video coding and streaming,
respectively. First video generation models have been proposed already [127] but its integration
with video streaming workflows remains an open challenge subject to future work.
Energy Consumption. Video streaming has a considerable environmental impact which shall
not be neglected. Recent surveys in this space [5, 43] outline open research challenges covering
a broad range of topics: (i) holistic, energy-efficient system design (specifically, but not limited
to, AI-based solutions including training); (ii) measurements, datasets, and analyses thereof; (iii)
regulation and standardization; and (iv) green service-level agreements.
8
Conclusions
HAS has revolutionized video streaming by offering scalable, high-quality content delivery over the
Internet. This article explored key advancements in HAS, including video coding innovations, ABR
algorithms, energy-efficient streaming, and network optimizations. While HAS has significantly
enhanced streaming experiences, several challenges remain. (i) The integration of machine learning
in HAS can enhance ABR selection, CC, and network resource allocation. DRL has already shown
promising results, but real-time adaptability and computational efficiency need further exploration.
(ii) With video streaming consuming an increasing share of global energy, future work should focus
on optimizing encoding processes, transmission protocols, and playback mechanisms to reduce
power consumption. Dynamic bitrate ladders and AI-driven encoding presets could help strike a
balance between quality and energy efficiency. (iii) Standardization efforts, such as MoQ, could
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 20

```text
198:20
C. Timmerer et al.
shape the next generation of HAS. The adoption of QUIC-based protocols for HAS can offer reduced
latency, improved CC, and better multiplexing capabilities, enhancing end-user experiences.
To further push the boundaries of HAS, interdisciplinary collaboration is needed between
researchers in video coding, networking, machine learning, and energy-efficient computing. Open
source initiatives, standardization efforts, and industry-academic partnerships will play a vital role
in shaping the future of adaptive streaming. Addressing these challenges will ensure that HAS
continues to evolve to meet the growing demands of global video consumption. By advancing in
these areas, HAS can maintain its position as the cornerstone of modern video delivery, providing
efficient, high-quality streaming experiences for users worldwide.
References
[1] Netflix TechBlog. 2018. VMAF: The Journey Continues. By Zhi Li, Christos Bampis, Julie Novak, Anne Aaron, Kyle
Swanson, Anush Moorthy and Jan De Cock. Netflix Technology Blog. Retrieved from https://netflixtechblog.com/
vmaf-the-journey-continues-44b51ee9ed12
[2] Me at the Zoo. 2024. Page Version ID: 1230002553. Retrieved from https://en.wikipedia.org/w/index.php?title=Me_at_
the_zoo&oldid=1230002553
[3] Vijay K. Adhikari, Yang Guo, Fang Hao, Volker Hilt, Zhi-Li Zhang, Matteo Varvello, and Moritz Steiner. 2015.
Measurement study of Netflix, Hulu, and a tale of three CDNs. IEEE/ACM Transactions on Networking 23, 6 (2015),
1984–1997. DOI: https://doi.org/10.1109/TNET.2014.2354262
[4] Samira Afzal, Narges Mehran, Sandro Linder, Christian Timmerer, and Radu Prodan. 2023. VE-Match: Video encoding
matching-based model for cloud and edge computing instances. In Proceedings of the 1st International Workshop on
Green Multimedia Systems. ACM, 1–6.
[5] Samira Afzal, Narges Mehran, Zoha Azimi Ourimi, Farzad Tashtarian, Hadi Amirpour, Radu Prodan, and Christian
Timmerer. 2024. A survey on energy consumption and environmental impact of video streaming. arXiv:2401.09854.
Retrieved from https://arxiv.org/abs/2401.09854
[6] Samira Afzal, Christian Timmerer, and Radu Prodan. 2024. Green video streaming: Challenges and opportunities. ACM
SIGMultimedia Records 15, 1 (2024), Article 3, page 1. Retrieved from https://records.sigmm.org/2023/01/08/green-
video-streaming-challenges-and-opportunities/
[7] Jesús Aguilar-Armijo, Ekrem Çetinkaya, Christian Timmerer, and Hermann Hellwagner. 2022. ECAS-ML: Edge
computing assisted adaptation scheme with machine learning for HTTP adaptive streaming. In Proceedings of the
International Conference on Multimedia Modeling. Springer, 394–406. DOI: https://doi.org/10.1007/978-3-030-98355-
0_33
[8] Jesús Aguilar-Armijo, Babak Taraghi, Christian Timmerer, and Hermann Hellwagner. 2020. Dynamic segment
repackaging at the edge for HTTP adaptive streaming. In Proceedings of the 2020 IEEE International Symposium on
Multimedia (ISM). IEEE, 17–24.
[9] Jesús Aguilar-Armijo, Christian Timmerer, and Hermann Hellwagner. 2021. EADAS: Edge assisted adaptation scheme
for HTTP adaptive streaming. In Proceedings of the 2021 IEEE 46th Conference on Local Computer Networks (LCN),
487–494. DOI: https://doi.org/10.1109/LCN52139.2021.9524883
[10] Jesús Aguilar-Armijo, Christian Timmerer, and Hermann Hellwagner. 2023. SPACE: Segment prefetching and caching
at the edge for adaptive video streaming. IEEE Access 11 (2023), 21783–21798. DOI: https://doi.org/10.1109/ACCESS.
2023.3252365
[11] Bengt Ahlgren, Christian Dannewitz, Claudio Imbrenda, Dirk Kutscher, and Borje Ohlman. 2012. A survey of
information-centric networking. IEEE Communications Magazine 50, 7 (2012), 26–36. DOI: https://doi.org/10.1109/
MCOM.2012.6231276
[12] Hadi Amirpour, Mohammad Ghanbari, and Christian Timmerer. 2022. DeepStream: Video streaming enhancements
using compressed deep neural networks. IEEE Transactions on Circuits and Systems for Video Technology 35, 4 (2022), 1.
DOI: https://doi.org/10.1109/TCSVT.2022.3229079
[13] Hadi Amirpour, Mohammad Ghasempour, Lingfeng Qu, Wassim Hamidouche, and Christian Timmerer. 2024. EVCA:
Enhanced video complexity analyzer. In Proceedings of the 15th ACM Multimedia Systems Conference (MMSys ’24).
ACM, New York, NY, 285–291. DOI: https://doi.org/10.1145/3625468.3652171
[14] Hadi Amirpour, Vignesh V. Menon, Samira Afzal, Radu Prodan, and Christian Timmerer. 2023. Optimizing video
streaming for sustainability and quality: The role of preset selection in per-title encoding. In Proceedings of the
2023 IEEE International Conference on Multimedia and Expo (ICME). IEEE, 1679–1684. DOI: https://doi.org/10.1109/
ICME55011.2023.00289
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 21

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:21
[15] Hadi Amirpour, Raimund Schatz, and Christian Timmerer. 2022. Between two and six? Towards correct estimation of
JND step sizes for VMAF-based bitrate laddering. In Proceedings of the 2022 14th International Conference on Quality
of Multimedia Experience (QoMEX), 1–4. DOI: https://doi.org/10.1109/QoMEX55416.2022.9900896
[16] Hadi Amirpour, Klaus Shoeffmann, Mohammad Ghanbari, and Christian Timmerer. 2024. DeepVCA: Deep video
complexity analyzer. IEEE Transactions on Circuits and Systems for Video Technology 34, 9 (2024), 8836–8847. DOI:
https://doi.org/10.1109/TCSVT.2024.3382366
[17] Hadi Amirpour, Christian Timmerer, and Mohammad Ghanbari. 2021. PSTR: Per-title encoding using spatio-temporal
resolutions. In Proceedings of the 2021 IEEE International Conference on Multimedia and Expo (ICME), 1–6. DOI:
https://doi.org/10.1109/ICME51207.2021.9428247
[18] Hadi Amirpour, Jingwen Zhu, Raimund Schatz, Patrick Le Callet, and Christian Timmerer. 2024. Exploring bitrate
costs for enhanced user satisfaction: A Just Noticeable Difference (JND) perspective. In Proceedings of the 2024 Data
Compression Conference (DCC), 432–441. DOI: https://doi.org/10.1109/DCC58796.2024.00051
[19] Abdelhak Bentaleb, Ali C. Begen, and Roger Zimmermann. 2016. SDNDASH: Improving QoE of HTTP adaptive
streaming using software defined networking. In Proceedings of the 24th ACM International Conference on Multimedia
(MM ’16). ACM, New York, NY, 1296–1305. DOI: https://doi.org/10.1145/2964284.2964332
[20] Abdelhak Bentaleb, Reza Farahani, Farzad Tashtarian, Hermann Hellwagner, and Roger Zimmermann. 2023. Which
CDN to download from? A client and server strategies. In Proceedings of the 2nd Mile-High Video Conference, 135–136.
[21] Abdelhak Bentaleb, May Lim, Mehmet N. Akcay, Ali C. Begen, Sarra Hammoudi, and Roger Zimmermann. 2023.
Toward one-second latency: Evolution of live media streaming. arXiv:2310.03256. Retrieved from https://arxiv.org/
abs/2310.03256
[22] Abdelhak Bentaleb, May Lim, Mehmet N. Akcay, Ali C. Begen, and Roger Zimmermann. 2024. Bitrate adaptation
and guidance with meta reinforcement learning. IEEE Transactions on Mobile Computing 23, 11 (2024), 1–14. DOI:
https://doi.org/10.1109/TMC.2024.3376560
[23] Abdelhak Bentaleb, Bayan Taani, Ali C. Begen, Christian Timmerer, and Roger Zimmermann. 2019. A survey on
bitrate adaptation schemes for streaming media over HTTP. IEEE Communications Surveys Tutorials 21, 1 (2019),
562–585. DOI: https://doi.org/10.1109/COMST.2018.2862938
[24] Abdelhak Bentaleb, Zhengdao Zhan, Farzad Tashtarian, May Lim, Saad Harous, Christian Timmerer, Hermann
Hellwagner, and Roger Zimmermann. 2022. Low latency live streaming implementation in DASH and HLS. In
Proceedings of the 30th ACM International Conference on Multimedia (MM ’22). ACM, New York, NY, 7343–7346. DOI:
https://doi.org/10.1145/3503161.3548544
[25] Divyashri Bhat, Amr Rizk, Michael Zink, and Ralf Steinmetz. 2018. SABR: Network-assisted content distribution for
QoE-driven ABR video streaming. ACM Transactions on Multimedia Computing, Communications, and Applications
14, 2s, Article 32 (Apr. 2018), 25 pages. DOI: https://doi.org/10.1145/3183516
[26] Ting Bi, Roisin Lyons, Grace Fox, and Gabriel-Miro Muntean. 2021. Improving student learning satisfaction by using
an innovative DASH-based multiple sensorial media delivery solution. IEEE Transactions on Multimedia 23 (2021),
3494–3505. DOI: https://doi.org/10.1109/TMM.2020.3025669
[27] Frank Bossen, Karsten Sühring, Adam Wieckowski, and Shan Liu. 2021. VVC complexity and software implementation
analysis. IEEE Transactions on Circuits and Systems for Video Technology 31, 10 (2021), 3765–3778.
[28] Nassima Bouzakaria, Cyril Concolato, and Jean Le Feuvre. 2014. Overhead and performance of low latency live
streaming using MPEG-DASH. In Proceedings of the 5th International Conference on Information, Intelligence, Systems
and Applications (IISA ’14), 92–97. DOI: https://doi.org/10.1109/IISA.2014.6878732
[29] B. Briscoe, K. De Schepper, M. Bagnulo, and G. White. 2023. RFC 9330: Low Latency, Low Loss, and Scalable Throughput
(L4S) Internet Service: Architecture. RFC Editor, USA. Retrieved from https://dl.acm.org/doi/10.17487/RFC9330
[30] Benjamin Bross, Jianle Chen, Jens-Rainer Ohm, Gary J. Sullivan, and Ye-Kui Wang. 2021. Developments in interna-
tional video coding standardization after AVC, with an overview of Versatile Video Coding (VVC). Proceedings of the
IEEE 109, 9 (Sept. 2021), 1463–1493. DOI: https://doi.org/10.1109/JPROC.2020.3043399
[31] Benjamin Bross, Ye-Kui Wang, Yan Ye, Shan Liu, Jianle Chen, Gary J. Sullivan, and Jens-Rainer Ohm. 2021. Overview
of the Versatile Video Coding (VVC) standard and its applications. IEEE Transactions on Circuits and Systems for
Video Technology 31, 10 (Oct. 2021), 3736–3764. DOI: https://doi.org/10.1109/TCSVT.2021.3101953
[32] Taieb Chachou, Wassim Hamidouche, Sid Ahmed Fezza, and Ghalem Belalem. 2023. Energy consumption and carbon
emissions of modern software video encoders. IEEE Consumer Electronics Magazine 13, 6 (2023), 73–91.
[33] Hao Che, Ye Tung, and Zhijun Wang. 2002. Hierarchical Web caching systems: Modeling, design and experimental
results. IEEE Journal on Selected Areas in Communications 20, 7 (2002), 1305–1314. DOI: https://doi.org/10.1109/JSAC.
2002.801752
[34] Hao Chen, Bo He, Hanyu Wang, Yixuan Ren, Ser NamLim, and AbhinavShrivastava. 2021. NeRV: Neural rep-
resentations for videos. In Proceedings of the Advances in Neural Information Processing Systems, Vol. 34. Cur-
ran Associates, Inc., 21557–21568. Retrieved from https://proceedings.neurips.cc/paper_files/paper/2021/hash/
b44182379bf9fae976e6ae5996e13cd8-Abstract.html
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 22

```text
198:22
C. Timmerer et al.
[35] G. Cofano, L. De Cicco, T. Zinner, A. Nguyen-Ngoc, P. Tran-Gia, and S. Mascolo. 2016. Design and experimental
evaluation of network-assisted strategies for HTTP adaptive streaming. In Proceedings of the 7th International
Conference on Multimedia Systems (MMSys ’16). ACM, New York, NY, Article 3, 12 pages. DOI: https://doi.org/10.
1145/2910017.2910597
[36] Cyril Concolato and Jean Le Feuvre. 2013. Live HTTP streaming of video and subtitles within a browser. In
Proceedings of the 4th ACM Multimedia Systems Conference (MMSys ’13). ACM, New York, NY, 146–150. DOI:
https://doi.org/10.1145/2483977.2483997
[37] Cyril Concolato, Jean Le Feuvre, and Romain Bouqueau. 2011. Usages of DASH for rich media services. In Proceedings
of the 2nd Annual ACM Conference on Multimedia Systems (MMSys ’11). ACM, New York, NY, 265–270. DOI:
https://doi.org/10.1145/1943552.1943587
[38] G. J. Conklin, G. S. Greenbaum, K. O. Lillevold, A. F. Lippman, and Y. A. Reznik. 2001. Video coding for streaming
media delivery on the Internet. IEEE Transactions on Circuits and Systems for Video Technology 11, 3 (Mar. 2001),
269–281. DOI: https://doi.org/10.1109/76.911155
[39] Jan De Cock, Zhi Li, Megha Manohara, and Anne Aaron. 2016. Complexity-based consistent-quality encoding in
the cloud. In Proceedings of the 2016 IEEE International Conference on Image Processing (ICIP), 1484–1488. DOI:
https://doi.org/10.1109/ICIP.2016.7532605
[40] DIMPACT Publication. 2022. Methodology: Estimating the Carbon Impacts of Serving Digital Media and Entertain-
ment Products. Version. Retrieved October 21, 2022 from https://dimpact.org/resource?resource=2
[41] Alireza Erfanian, Hadi Amirpour, Farzad Tashtarian, Christian Timmerer, and Hermann Hellwagner. 2021. LwTE:
Light-weight transcoding at the edge. IEEE Access 9 (2021), 112276–112289. DOI: https://doi.org/10.1109/ACCESS.
2021.3102633
[42] Hans Eriksson. 1994. MBONE: The multicast backbone. Communications of the ACM 37, 8 (Aug. 1994), 54–60. DOI:
https://doi.org/10.1145/179606.179627
[43] Reza Farahani, Zoha Azimi, Christian Timmerer, and Radu Prodan. 2024. Towards AI-assisted sustainable adaptive
video streaming systems: Tutorial and survey. arXiv:2406.02302. Retrieved from https://arxiv.org/abs/2406.02302
[44] Reza Farahani, Mohammad Shojafar, Christian Timmerer, Farzad Tashtarian, Mohammad Ghanbari, and Hermann
Hellwagner. 2023. ARARAT: A collaborative edge-assisted framework for HTTP adaptive video streaming. IEEE
Transactions on Network and Service Management 20, 1 (2023), 625–643. DOI: https://doi.org/10.1109/TNSM.2022.
3210595
[45] Reza Farahani, Farzad Tashtarian, Hadi Amirpour, Christian Timmerer, Mohammad Ghanbari, and Hermann Hell-
wagner. 2021. CSDN: CDN-aware QoE optimization in SDN-assisted HTTP adaptive video streaming. In Proceedings
of the 2021 IEEE 46th Conference on Local Computer Networks (LCN). IEEE, 525–532.
[46] Reza Farahani, Farzad Tashtarian, Christian Timmerer, Mohammad Ghanbari, and Hermann Hellwagner. 2022.
LEADER: A collaborative edge-and SDN-assisted framework for HTTP adaptive video streaming. In Proceedings of
the IEEE International Conference on Communications (ICC ’22). DOI: https://doi.org/10.1109/ICC45855.2022.9838949
[47] Per Frojdh, Uwe Horn, Markus Kampmann, Anders Nohlgren, and Magnus Westerlund. 2006. Adaptive streaming
within the 3GPP packet-switched streaming service. IEEE Network 20, 2 (Mar. 2006), 34–40. DOI: https://doi.org/10.
1109/MNET.2006.1607894
[48] Huda S. Goian, Omar Y. Al-Jarrah, Sami Muhaidat, Yousof Al-Hammadi, Paul Yoo, and Mehrdad Dianati. 2019.
Popularity-based video caching techniques for cache-enabled networks: A survey. IEEE Access 7 (2019), 27699–27719.
DOI: https://doi.org/10.1109/ACCESS.2019.2898734
[49] R. Grandl, K. Su, and C. Westphal. 2013. On the interaction of adaptive video streaming with content-centric
networking. In Proceedings of the 2013 20th International Packet Video Workshop, 1–8. DOI: https://doi.org/10.1109/
PV.2013.6691451
[50] Thomas Guionnet, Mickaél Raulet, and Thomas Burnichon. 2020. Forward-looking content aware encoding for
next generation UHD, HDR, WCG, and HFR. SMPTE Motion Imaging Journal 129, 7 (Aug. 2020), 26–32. DOI:
https://doi.org/10.5594/JMI.2020.3001797
[51] Zafer Gurel, Tugce Erkilic Civelek, Deniz Ugur, Yigit K. Erinc, and Ali C. Begen. 2024. Media-over-QUIC transport
vs. low-latency DASH: A deathmatch testbed. In Proceedings of the 15th ACM Multimedia Systems Conference (MMSys
’24). ACM, New York, NY, 448–452. DOI: https://doi.org/10.1145/3625468.3652191
[52] Zafer Gurel, Tugce Erkilic Civelek, Atakan Bodur, Senem Bilgin, Deniz Yeniceri, and Ali C. Begen. 2023. Media over
QUIC: Initial testing, findings and results. In Proceedings of the 14th ACM Multimedia Systems Conference (MMSys
’23). ACM, New York, NY, 301–306. DOI: https://doi.org/10.1145/3587819.3593937
[53] Jingning Han, Bohan Li, Debargha Mukherjee, Ching-Han Chiang, Adrian Grange, Cheng Chen, Hui Su, Sarah
Parker, Sai Deng, Urvang Joshi, et al. 2021. A technical overview of AV1. Proceedings of the IEEE 109, 9 (Sept. 2021),
1435–1462. DOI: https://doi.org/10.1109/JPROC.2021.3058584
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 23

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:23
[54] Christian Herglotz, Werner Robitza, Matthias Kränzler, Andre Kaup, and Alexander Raake. 2022. Modeling of energy
consumption and streaming video QoE using a crowdsourcing dataset. In Proceedings of the 2022 14th International
Conference on Quality of Multimedia Experience (QoMEX). IEEE, 1–6.
[55] Xuehui Huang, Miska M. Hannuksela, and Houqiang Li. 2015. Improved downstream rate-distortion performance of
SHVC in DASH using sub-layer-selective interlayer prediction. In Proceedings of the 2015 IEEE 17th International
Workshop on Multimedia Signal Processing (MMSP), 1–6. DOI: https://doi.org/10.1109/MMSP.2015.7340848
[56] Becca Inglis. 2023. The Rolling Stones vs Silicon Valley: How a Band of Geeks Beat Jagger to Rock’s First Livestream.
The Telegraph. Retrieved July 2023 from https://www.telegraph.co.uk/music/artists/the-rolling-stones-severe-tire-
damage-livestream-concert/
[57] ISO/IEC. 2022. Information Technology—Dynamic Adaptive Streaming over HTTP (DASH)—Part 1: Media Presenta-
tion Description and Segment Formats. Retrieved from https://www.iso.org/standard/83314.html
[58] ISO/IEC. 2024. Information Technology—Multimedia Application Format (MPEG-A)—Part 19: Common Media
Application Format (CMAF) for Segmented Media. Retrieved from https://www.iso.org/standard/85623.html
[59] ISO/IEC 23009-5. 2017. Information Technology—Dynamic Adaptive Streaming over HTTP (DASH)—Part 5: Server
and Network Assisted DASH (SAND). Standard. International Organization for Standardization, Geneva, CH.
[60] Van Jacobson, Diana K. Smetters, James D. Thornton, Michael F. Plass, Nicholas H. Briggs, and Rebecca L. Bray-
nard. 2009. Networking named content. In Proceedings of the 5th International Conference on Emerging Networking
Experiments and Technologies (CoNEXT ’09). ACM, New York, NY, 1–12. DOI: https://doi.org/10.1145/1658939.1658941
[61] Behrouz Jedari, Gopika Premsankar, Gazi Illahi, Mario Di Francesco, Abbas Mehrabi, and Antti Ylä-Jääski. 2021.
Video caching, analytics, and delivery at the wireless edge: A survey and future directions. IEEE Communications
Surveys & Tutorials 23, 1 (2021), 431–471. DOI: https://doi.org/10.1109/COMST.2020.3035427
[62] Xiantao Jiang, F. Richard Yu, Tian Song, and Victor C. M. Leung. 2021. A survey on multi-access edge computing
applied to video streaming: Some research issues and challenges. IEEE Communications Surveys & Tutorials 23, 2
(2021), 871–903. DOI: https://doi.org/10.1109/COMST.2021.3065237
[63] Angeliki Katsenou, Jingwei Mao, and Ioannis Mavromatis. 2022. Energy-rate-quality tradeoffs of state-of-the-art
video codecs. In Proceedings of the 2022 Picture Coding Symposium (PCS). IEEE, 265–269.
[64] Angeliki V. Katsenou, Fan Zhang, Kyle Swanson, Mariana Afonso, Joel Sole, and David R. Bull. 2021. VMAF-based
bitrate ladder estimation for adaptive streaming. In Proceedings of the 2021 Picture Coding Symposium (PCS), 1–5.
DOI: https://doi.org/10.1109/PCS50896.2021.9477469
[65] Bernhard Kerbl, Georgios Kopanas, Thomas Leimkuehler, and George Drettakis. 2023. 3D Gaussian splatting for
real-time radiance field rendering. ACM Transactions on Graphics 42, 4, Article 139 (July 2023), 14 pages. DOI:
https://doi.org/10.1145/3592433
[66] Jaehong Kim, Youngmok Jung, Hyunho Yeo, Juncheol Ye, and Dongsu Han. 2020. Neural-enhanced live stream-
ing: Improving live video ingest via online learning. In Proceedings of the Annual Conference of the ACM Special
Interest Group on Data Communication on the Applications, Technologies, Architectures, and Protocols for Computer
Communication (SIGCOMM ’20). ACM, New York, NY, 107–125. DOI: https://doi.org/10.1145/3387514.3405856
[67] Jan Willem Kleinrouweler, Sergio Cabrero, and Pablo Cesar. 2016. Delivering stable high-quality video: An SDN
architecture with DASH assisting network elements. In Proceedings of the 7th International Conference on Multimedia
Systems (MMSys ’16). ACM, New York, NY, Article 4, 10 pages. DOI: https://doi.org/10.1145/2910017.2910599
[68] Maria G. Koziri, Panos K. Papadopoulos, Nikos Tziritas, Thanasis Loukopoulos, Samee U. Khan, and Albert Y. Zomaya.
2018. Efficient cloud provisioning for video transcoding: Review, open challenges and future opportunities. IEEE
Internet Computing 22, 5 (2018), 46–55.
[69] Dhananjay Lal and Christopher Phillips. 2024. Selective enablement of L4S transport for latency-sensitive multimedia
delivery. In Proceedings of the 2024 IEEE 26th International Workshop on Multimedia Signal Processing (MMSP), 1–6.
DOI: https://doi.org/10.1109/MMSP61759.2024.10743691
[70] May Lim, Mehmet N. Akcay, Abdelhak Bentaleb, Ali C. Begen, and Roger Zimmermann. 2020. When they go high,
we go low: Low-latency live streaming in dash.js with LoL. In Proceedings of the 11th ACM Multimedia Systems
Conference (MMSys ’20). ACM, New York, NY, 321–326. DOI: https://doi.org/10.1145/3339825.3397043
[71] Dong Liu, Yue Li, Jianping Lin, Houqiang Li, and Feng Wu. 2020. Deep learning-based video coding: A review and a
case study. ACM Computing Surveys 53, 1 (Feb. 2020), Article 11, 1–35. DOI: https://doi.org/10.1145/3368405
[72] Daniele Lorenzi, Minh Nguyen, Farzad Tashtarian, and Christian Timmerer. 2024. E-WISH: An energy-aware ABR
algorithm for green HTTP adaptive video streaming. In Proceedings of the 3rd Mile-High Video Conference (MHV ’24).
ACM, New York, NY, 28–33. DOI: https://doi.org/10.1145/3638036.3640802
[73] Guo Lu, Xiaoyun Zhang, Wanli Ouyang, Li Chen, Zhiyong Gao, and Dong Xu. 2021. An end-to-end learning
framework for video compression. IEEE Transactions on Pattern Analysis and Machine Intelligence 43, 10 (Oct. 2021),
3292–3308. DOI: https://doi.org/10.1109/TPAMI.2020.2988453
[74] Bruce M. Maggs and Ramesh K. Sitaraman. 2015. Algorithmic nuggets in content delivery. ACM SIGCOMM Computer
Communication Review 45, 3 (July 2015), 52–66. DOI: https://doi.org/10.1145/2805789.2805800
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 24

```text
198:24
C. Timmerer et al.
[75] Stephen Makonin, Laura U. Marks, Radek Przedpełski, Alejandro Rodriguez-Silva, and Ramy ElMallah. 2022. Calcu-
lating the carbon footprint of streaming media: Beyond the myth of efficiency. In Proceedings of the 8th Workshop on
Computing within Limits 2022. LIMITS.
[76] Narges Mehran, Dragi Kimovski, and Radu Prodan. 2019. MAPO: A multi-objective model for IoT application
placement in a fog environment. In Proceedings of the 9th International Conference on the Internet of Things, 1–8.
[77] Vignesh V. Menon, Hadi Amirpour, Mohammad Ghanbari, and Christian Timmerer. 2022. OPTE: Online per-title
encoding for live video streaming. In Proceedings of the 2022 IEEE International Conference on Acoustics, Speech and
Signal Processing (ICASSP ’22), 1865–1869. DOI: https://doi.org/10.1109/ICASSP43922.2022.9746745
[78] Vignesh V. Menon, Hadi Amirpour, Mohammad Ghanbari, and Christian Timmerer. 2022. Perceptually-aware per-
title encoding for adaptive video streaming. In Proceedings of the 2022 IEEE International Conference on Multimedia
and Expo (ICME). IEEE, 1–6. DOI: https://doi.org/10.1109/ICME52920.2022.9859744
[79] Vignesh V. Menon, Christian Feldmann, Hadi Amirpour, Mohammad Ghanbari, and Christian Timmerer. 2022.
VCA: Video complexity analyzer. In Proceedings of the 13th ACM Multimedia Systems Conference, 259–264. DOI:
https://doi.org/10.1145/3524273.3532896
[80] Alexandre Mercat, Florian Arrestier, Wassim Hamidouche, Maxime Pelcat, and Daniel Menard. 2017. Energy reduction
opportunities in an HEVC real-time encoder. In Proceedings of the 2017 IEEE International Conference on Acoustics,
Speech and Signal Processing (ICASSP). IEEE, 1158–1162.
[81] Eduarda Monteiro, Mateus Grellert, Sergio Bampi, and Bruno Zatt. 2015. Rate-distortion and energy performance of
HEVC and H.264/AVC encoders: A comparative analysis. In Proceedings of the 2015 IEEE International Symposium on
Circuits and Systems (ISCAS). IEEE, 1278–1281.
[82] Lucas V. Monteiro, Vinícius S. Simão, Rodrigo de B. Lira, Leandro C. de Almeida, Ruan D. Gomes, and Paulo Ditarso
Maciel. 2024. L4S in private 5G industrial networks: A case study for real-time video transmission in programmable
networks. In Proceedings of the 2024 IEEE Conference on Network Function Virtualization and Software Defined Networks
(NFV-SDN), 1–4. DOI: https://doi.org/10.1109/NFV-SDN61811.2024.10807467
[83] Christopher Müller, Daniele Renzi, Stefan Lederer, Stefano Battista, and Christian Timmerer. 2012. Using scalable
video coding for dynamic adaptive streaming over HTTP in mobile environments. In Proceedings of the 20th European
Signal Processing Conference (EUSIPCO), 2208–2212.
[84] Adel N. Toosi, Chayan Agarwal, Lena Mashayekhy, Sara K. Moghaddam, Redowan Mahmud, and Zahir Tari.
2022. GreenFog: A framework for sustainable fog computing. In Service-Oriented Computing. Javier Troya, Brahim
Medjahed, Mario Piattini, Lina Yao, Pablo Fernández, and Antonio Ruiz-Cortés (Eds.), Springer, Cham, 540–549.
DOI: https://doi.org/10.1007/978-3-031-20984-0_38
[85] Minh Nguyen, Daniele Lorenzi, Farzad Tashtarian, Hermann Hellwagner, and Christian Timmerer. 2022. DoFP+: An
HTTP/3-based adaptive bitrate approach using retransmission techniques. IEEE Access 10 (2022), 109565–109579.
DOI: https://doi.org/10.1109/ACCESS.2022.3214827
[86] Minh Nguyen, Ekrem Çetinkaya, Hermann Hellwagner, and Christian Timmerer. 2021. WISH: User-centric bitrate
adaptation for HTTP adaptive streaming on mobile devices. In Proceedings of the 2021 IEEE 23rd International
Workshop on Multimedia Signal Processing (MMSP), 1–6. DOI: https://doi.org/10.1109/MMSP53017.2021.9733605
[87] Minh Nguyen, Ekrem Çetinkaya, Hermann Hellwagner, and Christian Timmerer. 2022. Super-resolution based
bitrate adaptation for HTTP adaptive streaming for mobile devices. In Proceedings of the 1st Conference on Mile-High
Video (MHV ’22). ACM, New York, NY, 70–76. DOI: https://doi.org/10.1145/3510450.3517322
[88] Jakob Nielsen. 2023. Nielsen’s Law of Internet Bandwidth. Retrieved from https://www.nngroup.com/articles/law-
of-bandwidth/
[89] Panagiotis Oikonomou, Maria G. Koziri, Nikos Tziritas, Antonios N. Dadaliaris, Thanasis Loukopoulos, Georgios I.
Stamoulis, and Samee U. Khan. 2018. Scheduling video transcoding jobs in the cloud. In Proceedings of the 2018 IEEE
International Conference on Internet of Things (iThings) and IEEE Green Computing and Communications (GreenCom)
and IEEE Cyber, Physical and Social Computing (CPSCom) and IEEE Smart Data (SmartData). IEEE, 442–449.
[90] Roger Pantos and William May. 2017. HTTP Live Streaming. Request for Comments RFC 8216. Internet Engineering
Task Force, 60. DOI: https://doi.org/10.17487/RFC8216
[91] Stefan Pham, Patrick Heeren, Calvin Schmidt, Daniel Silhavy, and Stefan Arbanowski. 2020. Evaluation of shared
resource allocation using SAND for ABR streaming. ACM Transactions on Multimedia Computing, Communications,
and Applications 16, 2s, Article 70 (July 2020), 18 pages. DOI: https://doi.org/10.1145/3388926
[92] Benjamin Rainer, Stefan Lederer, Christopher Müller, and Christian Timmerer. 2012. A seamless Web integration
of adaptive HTTP streaming. In Proceedings of the 2012 20th European Signal Processing Conference (EUSIPCO),
1519–1523.
[93] Adithya Raman, Bekir Turkkan, and Tevfik Kosar. 2024. LL-GABR: Energy efficient live video streaming using
reinforcement learning. arXiv:2402.09392. Retrieved from https://arxiv.org/abs/2402.09392
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 25

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:25
[94] Hemanth Kumar Ravuri, Maria Torres Vega, Jeroen Der Van Hooft, Tim Wauters, and Filip De Turck. 2023. Adaptive
partially reliable delivery of immersive media over QUIC-HTTP/3. IEEE Access 11 (2023), 38094–38111. DOI: https:
//doi.org/10.1109/ACCESS.2023.3268008
[95] Rafael Rodrigues, Peter Pocta, Hugh Melvin, Marco V. Bernardo, Manuela Pereira, and Antonio M. G. Pinheiro.
2020. Audiovisual quality of live music streaming over mobile networks using MPEG-DASH. Multimedia Tools and
Applications 79, 33 (Sept. 2020), 24595–24619. DOI: https://doi.org/10.1007/s11042-020-09047-6
[96] David Ronca. 2023. Encoder Complexity Hits the Wall! Retrieved July 31, 2024 from https://www.linkedin.com/
pulse/encoder-complexity-hits-wall-david-ronca/
[97] Mohammadhassan Safavi, Saeed Bastani, Zhi Zhang, Martti Forsell, Olli Mämmelä, and Björn Landfeldt. 2016.
A study on energy used to deliver H.264/AVC and H.265/HEVC video content. In Proceedings of the 2016 IEEE 21st
International Workshop on Computer Aided Modelling and Design of Communication Links and Networks (CAMAD).
IEEE, 170–176.
[98] Yago Sánchez de la Fuente, Thomas Schierl, Cornelius Hellge, Thomas Wiegand, Dohy Hong, Danny De Vleeschauwer,
Werner Van Leekwijck, and Yannick Le Louédec. 2011. iDASH: Improved dynamic adaptive streaming over HTTP
using scalable video coding. In Proceedings of the 2nd Annual ACM Conference on Multimedia Systems (MMSys ’11).
ACM, New York, NY, 257–264. DOI: https://doi.org/10.1145/1943552.1943586
[99] Sandvine. 2024. 2024 Global Internet Phenomena Report. Technical Report. Sandvine. Retrieved from https://www.
sandvine.com/phenomena
[100] Heiko Schwarz, Detlev Marpe, and Thomas Wiegand. 2007. Overview of the scalable video coding extension of the
H.264/AVC standard. IEEE Transactions on Circuits and Systems for Video Technology 17, 9 (2007), 1103–1120. DOI:
https://doi.org/10.1109/TCSVT.2007.905532
[101] Michael Seufert, Sebastian Egger, Martin Slanina, Thomas Zinner, Tobias Hoßfeld, and Phuoc Tran-Gia. 2015.
A survey on quality of experience of HTTP adaptive streaming. IEEE Communications Surveys & Tutorials 17, 1
(2015), 469–492. DOI: https://doi.org/10.1109/COMST.2014.2360940
[102] Michael Seufert, Marius Spangenberger, Fabian Poignée, Florian Wamser, Werner Robitza, Christian Timmerer,
and Tobias Hossfeld. 2024. COBIRAS: Offering a continuous bit rate slide to maximize DASH streaming bandwidth
utilization. ACM Transactions on Multimedia Computing, Communications and Applications 20, 10 (July 2024), 1–24.
DOI: https://doi.org/10.1145/3677379
[103] Yousef O. Sharrab and Nabil J. Sarhan. 2013. Aggregate power consumption modeling of live video streaming systems.
In Proceedings of the 4th ACM Multimedia Systems Conference. ACM, 60–71.
[104] Yuang Shi, Géraldine Morin, Simone Gasparini, and Wei Tsang Ooi. 2025. LapisGS: Layered progressive 3D Gaussian
splatting for adaptive streaming. arXiv:2408.14823. Retrieved from https://arxiv.org/abs/2408.14823
[105] Dieison Silveira, Marcelo Porto, and Sergio Bampi. 2017. Performance and energy consumption analysis of the X265
video encoder. In Proceedings of the 2017 25th European Signal Processing Conference (EUSIPCO). IEEE, 1519–1523.
[106] Jangwoo Son, Yago Sanchez, Cornelius Hellge, and Thomas Schierl. 2024. Adaptable L4S congestion control for
cloud-based real-time streaming over 5G. IEEE Open Journal of Signal Processing 5 (2024), 841–849. DOI: https:
//doi.org/10.1109/OJSP.2024.3405719
[107] Denny Stohr, Alexander Frömmgen, Amr Rizk, Michael Zink, Ralf Steinmetz, and Wolfgang Effelsberg. 2017.
Where are the sweet spots? A systematic approach to reproducible DASH player comparisons. In Proceedings
of the 25th ACM International Conference on Multimedia (MM ’17). ACM, New York, NY, 1113–1121. DOI: https:
//doi.org/10.1145/3123266.3123426
[108] Gary J. Sullivan, Jens-Rainer Ohm, Woo-Jin Han, and Thomas Wiegand. 2012. Overview of the high efficiency
video coding (HEVC) standard. IEEE Transactions on Circuits and Systems for Video Technology 22, 12 (Dec. 2012),
1649–1668. DOI: https://doi.org/10.1109/TCSVT.2012.2221191
[109] Babak Taraghi, Hadi Amirpour, and Christian Timmerer .2022. Multi-codec ultra high definition 8K MPEG-DASH
dataset. In Proceedings of the 13th ACM Multimedia Systems Conference (MMSys ’22). ACM, New York, NY, 216–220.
DOI: https://doi.org/10.1145/3524273.3532889
[110] Babak Taraghi, Abdelhak Bentaleb, Christian Timmerer, Roger Zimmermann, and Hermann Hellwagner. 2022.
CAdViSE or how to find the sweet spots of ABR systems. In Proceedings of the 1st Conference on Mile-High Video
(MHV ’22). ACM, New York, NY, 94. DOI: https://doi.org/10.1145/3510450.3517274
[111] Farzad Tashtarian, Abdelhak Bentaleb, Hadi Amirpour, Sergey Gorinsky, Junchen Jiang, Hermann Hellwagner, and
Christian Timmerer. 2024. ARTEMIS: Adaptive bitrate ladder optimization for live video streaming. In 21st USENIX
Symposium on Networked Systems Design and Implementation (NSDI 24). USENIX Association, Santa Clara, CA,
591–611. Retrieved from https://www.usenix.org/conference/nsdi24/presentation/tashtarian
[112] Farzad Tashtarian, Abdelhak Bentaleb, Hadi Amirpour, Babak Taraghi, Christian Timmerer, Hermann Hellwagner,
and Roger Zimmermann. 2023. LALISA: Adaptive bitrate ladder optimization in HTTP-based adaptive live streaming.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 26

```text
198:26
C. Timmerer et al.
In Proceedings of the NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium (IEEE/IFIP NOMS).
IEEE, 1–9. DOI: https://doi.org/10.1109/NOMS56928.2023.10154347
[113] Farzad Tashtarian, Abdelhak Bentaleb, Alireza Erfanian, Hermann Hellwagner, Christian Timmerer, and Roger
Zimmermann. 2022. HxL3: Optimized delivery architecture for HTTP low-latency live streaming. IEEE Transactions
on Multimedia 25 (2022), 1. DOI: https://doi.org/10.1109/TMM.2022.3148587
[114] Farzad Tashtarian, Abdelhak Bentaleb, Reza Farahani, Minh Nguyen, Christian Timmerer, Hermann Hellwagner,
and Roger Zimmermann. 2021. A distributed delivery architecture for user generated content live streaming over
HTTP. In Proceedings of the 2021 IEEE 46th Conference on Local Computer Networks (LCN). IEEE, 162–169.
[115] Farzad Tashtarian, Mahdi Dolati, Daniele Lorenzi, Mojtaba Mozhganfar, Sergey Gorinsky, Ahmad Khonsari, Christian
Timmerer, Hermann Hellwagner, et al. 2025. ALPHAS: Adaptive bitrate ladder optimization for multi-live video
streaming. In Proceedings of the IEEE International Conference on Computer Communications.
[116] Ahmed Telili, Wassim Hamidouche, Sid Ahmed Fezza, and Luce Morin. 2022. Benchmarking learning-based bitrate
ladder prediction methods for adaptive video streaming. In Proceedings of the 2022 Picture Coding Symposium (PCS),
325–329. DOI: https://doi.org/10.1109/PCS56426.2022.10018038
[117] Bekir Oguzhan Turkkan, Ting Dai, Adithya Raman, Tevfik Kosar, Changyou Chen, Muhammed Bulut, Jaroslav
Zola, and Daby Sow. 2024. GreenABR+: Generalized energy-aware adaptive bitrate streaming. ACM Transactions
on Multimedia Computing, Communications, and Applications 20, 9 (Aug. 2024), Article 269, 1–24. DOI: https:
//doi.org/10.1145/3649898
[118] Bekir Oguzhan Turkkan, Ting Dai, Adithya Raman, Tevfik Kosar, Changyou Chen, Muhammed FatihBulut, Jaroslaw-
Zola, and Daby Sow. 2022. GreenABR: Energy-aware adaptive bitrate streaming with deep reinforcement learning.
In Proceedings of the 13th ACM Multimedia Systems Conference (MMSys ’22). ACM, New York, NY, 150–163. DOI:
https://doi.org/10.1145/3524273.3528188
[119] Mikko Uitto. 2016. Energy consumption evaluation of H.264 and HEVC video encoders in high-resolution live
streaming. In Proceedings of the 2016 IEEE 12th International Conference on Wireless and Mobile Computing, Networking
and Communications (WiMob), 1–7.
[120] Jeroen Van Der Hooft, Hadi Amirpour, Maria Torres Vega, Yago Sanchez, Raimund Schatz, Thomas Schierl, and
Christian Timmerer. 2023. A tutorial on immersive video delivery: From omnidirectional video to holography. IEEE
Communications Surveys & Tutorials 25, 2 (2023), 1336–1375. DOI: https://doi.org/10.1109/COMST.2023.3263252
[121] Bing Wang, Jim Kurose, Prashant Shenoy, and Don Towsley. 2004. Multimedia streaming via TCP: An analytic
performance study. In Proceedings of the 12th Annual ACM International Conference on Multimedia (MULTIMEDIA
’04). ACM, New York, NY, 908–915. DOI: https://doi.org/10.1145/1027527.1027735
[122] T. Wiegand, G.J. Sullivan, G. Bjontegaard, and A. Luthra. 2003. Overview of the H.264/AVC video coding standard.
IEEE Transactions on Circuits and Systems for Video Technology 13, 7 (July 2003), 560–576. DOI: https://doi.org/10.
1109/TCSVT.2003.815165
[123] Zhisheng Yan, Jingteng Xue, and Chang Wen Chen. 2017. Prius: Hybrid edge cloud and client adaptation for HTTP
adaptive streaming in cellular networks. IEEE Transactions on Circuits and Systems for Video Technology 27, 1 (2017),
209–222. DOI: https://doi.org/10.1109/TCSVT.2016.2539827
[124] Hyunho Yeo, Hwijoon Lim, Jaehong Kim, Youngmok Jung, Juncheol Ye, and Dongsu Han. 2022. NeuroScaler: Neural
video enhancement at scale. In Proceedings of the ACM SIGCOMM 2022 Conference (SIGCOMM ’22). ACM, New York,
NY, 795–811. DOI: https://doi.org/10.1145/3544216.3544218
[125] Di Yuan, Tiesong Zhao, Yiwen Xu, Hong Xue, and Liqun Lin. 2019. Visual JND: A perceptual measurement in video
coding. IEEE Access 7 (2019), 29014–29022.
[126] Chaoqun Yue, Subhabrata Sen, Bing Wang, Yanyuan Qin, and Feng Qian. 2020. Energy considerations for ABR video
streaming to smartphones: Measurements, models and insights. In Proceedings of the 11th ACM Multimedia Systems
Conference, 153–165.
[127] Yan Zeng, Guoqiang Wei, Jiani Zheng, Jiaxin Zou, Yang Wei, Yuchen Zhang, and Hang Li .2024. Make pixels dance:
High-dynamic video generation. In 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
IEEE, Los Alamitos, CA, 8850–8860. Retrieved from https://openaccess.thecvf.com/content/CVPR2024/html/Zeng_
Make_Pixels_Dance_High-Dynamic_Video_Generation_CVPR_2024_paper.html
[128] Bo Zhang, Thiago Teixeira, and Yuriy Reznik. 2021. Performance of low-latency HTTP-based streaming players.
In Proceedings of the 12th ACM Multimedia Systems Conference (MMSys ’21). ACM, New York, NY, 356–362. DOI:
https://doi.org/10.1145/3458305.3478442
[129] Lixia Zhang, Alexander Afanasyev, Jeffrey Burke, Van Jacobson, kc claffy, Patrick Crowley, Christos Papadopoulos,
Lan Wang, and Beichuan Zhang. 2014. Named data networking. ACM SIGCOMM Computer Communication Review
44, 3 (July 2014), 66–73. DOI: https://doi.org/10.1145/2656877.2656887
[130] Xiaojie Zhang, Amitangshu Pal, and Saptarshi Debroy. 2021. Effect: Energy-efficient fog computing framework for
real-time video processing. In Proceedings of the 2021 IEEE/ACM 21st International Symposium on Cluster, Cloud and
Internet Computing (CCGrid). IEEE, 493–503.
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```

### Página 27

```text
HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
198:27
[131] Jinwei Zhao and Jianping Pan. 2024. Low-latency live video streaming over a low-earth-orbit satellite network with
DASH. In Proceedings of the 15th ACM Multimedia Systems Conference (MMSys ’24). ACM, New York, NY, 109–120.
DOI: https://doi.org/10.1145/3625468.3647616
[132] Jingwen Zhu, Hadi Amirpour, Raimund Schatz, Patrick Le Callet, and Christian Timmerer. 2024. Beyond curves and
thresholds—Introducing uncertainty estimation to satisfied user ratios for compressed video. In Proceedings of the
2024 Picture Coding Symposium (PCS), 1–5. DOI: https://doi.org/10.1109/PCS60826.2024.10566451
[133] Michael Zink, Kyoungwon Suh, Yu Gu, and Jim Kurose. 2009. Characteristics of YouTube network traffic at a
campus network—Measurements, models, and implications. Computer Networks 53, 4 (2009), 501–514. DOI: https:
//doi.org/10.1016/j.comnet.2008.09.022
[134] Longhao Zou, Ting Bi, and Gabriel-Miro Muntean. 2019. A DASH-based adaptive multiple sensorial content delivery
solution for improved user quality of experience. IEEE Access 7 (2019), 89172–89187. DOI: https://doi.org/10.1109/
ACCESS.2019.2926207
Received 17 September 2024; revised 21 February 2025; accepted 21 March 2025
ACM Trans. Multimedia Comput. Commun. Appl., Vol. 21, No. 7, Article 198. Publication date: July 2025.
```
