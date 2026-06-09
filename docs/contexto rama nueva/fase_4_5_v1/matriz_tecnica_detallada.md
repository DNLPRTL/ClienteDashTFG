# Matriz tecnica detallada del corpus ABR IA

Status: auditoria_tecnica_v1.

Esta matriz complementa las fichas cortas de `paper_audits/`. Su objetivo es
responder, para cada PDF, que implementa exactamente el paper y que se puede
extrapolar al proyecto. No sustituye a una lectura academica completa del PDF,
pero si baja al nivel necesario para decidir modelos: estado, accion, reward,
arquitectura, entrenamiento, datos, evaluacion y utilidad practica.

## Lectura critica global

El corpus no contiene "un unico modelo ganador" que podamos copiar. Contiene
familias de ideas:

- RL ABR directo: Pensieve, PPO-ABR, PLL-ABR, ALVS.
- Imitation/pretraining: Comyco, SABR, Incendio.
- Meta/generalizacion: A2BR, MERINA, MetaABR, EAStream, Ahaggar, Fortuna.
- Especializacion por red/traza: Oboe, ANT, BETA, Gelato/Plume.
- Control seguro/smoothness: SODA.
- Prediccion de throughput: Fugu/Puffer, BPA, MamBRA.
- Objetivos extendidos: GreenABR, visual sensitivity, edge/fairness, live,
  short-video.

Para Fase 4-5 v1, lo mas solido academicamente no es escoger solo una familia,
sino construir un controller nuevo con:

- entrenamiento estable tipo BC/pretraining;
- optimizacion posterior controlada;
- sampler balanceado por trazas dificiles;
- riesgo de buffer explicito;
- decision auditada por chunk;
- runtime sin leakage.

## 01 - Pensieve

PDF: `pensievee.pdf`.

Implementa un controller ABR neural con reinforcement learning. El sistema
simula descarga chunk a chunk y entrena una politica que elige la calidad del
siguiente segmento.

- Estado usado: muestras recientes de throughput, tiempos de descarga recientes,
  buffer actual, ultimo bitrate, tamanos de los proximos chunks por calidad y
  chunks restantes.
- Accion: bitrate/calidad discreta del siguiente chunk.
- Reward: utilidad de calidad/bitrate menos rebuffering y smoothness. En el
  paper se experimenta con diferentes QoE objectives.
- Arquitectura: red neuronal actor-critic; Pensieve usa A3C.
- Entrenamiento: online RL en simulador trace-driven, con multiples agentes
  paralelos recogiendo experiencias.
- Datos/evaluacion: trazas de red, broadband/HSDPA y pruebas reales; compara
  contra rate-based, buffer-based, MPC y RobustMPC.
- Que aporta: formulacion canonica estado-accion-reward para ABR neural.
- Que no aporta: proteccion fuerte ante incertidumbre, balanceo de tail traces
  ni garantias de no-rebuffer. Puede aprender politicas agresivas si el reward o
  el corpus no castigan suficiente los casos dificiles.

Uso propuesto: referencia base, no implementacion literal.

## 02 - Comyco

PDF: `1908.02270v1.pdf`.

Implementa un ABR quality-aware entrenado por imitation learning. En vez de
explorar desde cero como Pensieve, genera acciones expertas con un solver y las
imita.

- Estado usado: features de red pasadas, buffer/download time, ultima accion,
  chunks restantes y features de contenido/video como VMAF y tamanos de chunks.
- Accion: calidad/bitrate del siguiente chunk.
- Reward/objetivo: no entrena principalmente maximizando reward RL desde cero;
  minimiza perdida de imitacion frente a experto. La calidad perceptual se usa
  para elegir mejores acciones que solo mirar bitrate.
- Arquitectura: NN con ramas para tipos de entrada; usa convoluciones/GRU segun
  el texto extraido; salida probabilistica por accion.
- Entrenamiento: instant solver genera trayectoria experta, virtual player
  reproduce estados y experience replay guarda muestras.
- Datos/evaluacion: dataset de videos DASH con VMAF, trazas de red y pruebas
  trace-driven/real-world; compara contra Pensieve, RobustMPC y otros.
- Que aporta: pretraining estable, alta eficiencia de muestras y aprendizaje de
  expertos.
- Que no aporta: si el experto es agresivo o el dataset no cubre redes malas, el
  modelo tambien falla. Ademas VMAF no esta activo en nuestro contrato.

Uso propuesto: BC/pretraining para un controller nuevo, con experto propio
risk-aware, no copiar Comyco tal cual.

## 03 - Puffer / Fugu

PDF: `2020_yan_puffer_learning_in_situ_nsdi.pdf`.

Implementa y evalua algoritmos ABR en una plataforma real. Fugu combina
prediccion de tiempo de transmision con decision ABR.

- Estado usado: informacion cliente/streaming real, historial de transmision,
  buffer y seniales disponibles en Puffer.
- Accion: bitrate del siguiente chunk.
- Modelo principal: Transmission Time Predictor para estimar distribucion/tiempo
  de descarga; el controller usa esa prediccion para decidir.
- Reward/objetivo: QoE real del streaming, con calidad perceptual/SSIM y stalls.
- Entrenamiento: aprendizaje in situ con datos recogidos de usuarios reales.
- Evaluacion: experimento aleatorizado a gran escala con usuarios reales.
- Que aporta: metodologia de evaluacion y separacion entre predictor y control.
- Que no aporta: no tenemos plataforma de usuarios reales ni SSIM/Puffer runtime.

Uso propuesto: inspiracion para un predictor conservador + decision segura y
para no sobreinterpretar simulaciones.

## 04 - Oboe

PDF: `Oboe.pdf`.

Implementa auto-tuning de parametros para ABR existentes. No aprende una politica
completa, sino que adapta parametros de BOLA/MPC a condiciones de red.

- Estado usado: representacion compacta de red mediante estadisticos como media,
  desviacion y caracteristicas recientes de throughput.
- Accion: seleccion de parametros del algoritmo ABR subyacente, no bitrate
  directamente.
- Reward/objetivo: QoE obtenido por cada configuracion en simulacion offline.
- Arquitectura: mapa offline condicion de red -> parametros.
- Entrenamiento/offline: barrido de parametros por condicion y seleccion de los
  mejores.
- Runtime: detecta condicion y aplica parametros precomputados.
- Evaluacion: compara algoritmos tuneados contra versiones fijas.
- Que aporta: idea interpretable de adaptacion por regimen.
- Que no aporta: deteccion de dinamica temporal compleja; papers como ANT/BETA
  muestran que media/desviacion pueden ser insuficientes.

Uso propuesto: selector/condicionador interpretable, no controller principal.

## 05 - CausalSim

PDF: `CausalSim.pdf`.

No implementa un ABR. Implementa un framework de simulacion causal para evitar
sesgos en trace-driven simulation.

- Problema: una traza recogida bajo un algoritmo puede no ser valida para evaluar
  otro algoritmo si la intervencion cambia el propio proceso observado.
- Implementacion: modelo causal que separa componentes simulados, componentes
  replayed y variables afectadas por la intervencion.
- Entrenamiento: aprende/estima componentes causales desde datos.
- Evaluacion: compara precision de simulacion frente a datos reales en Puffer y
  otro caso de load balancing.
- Que aporta: rigor metodologico para no llamar generalizacion real-world a
  cualquier replay.
- Que no aporta: controller ABR nuevo.

Uso propuesto: guardrail metodologico para Phase 6 y separacion real/sintetico.

## 06 - A2BR

PDFs: `A2BR.pdf` y duplicado `Learning_Tailored_...pdf`.

Implementa un ABR meta-RL para adaptar la politica a condiciones heterogeneas.

- Estado: observaciones del player/red similares a Pensieve, formalizadas en un
  Input-Driven MDP.
- Accion: bitrate discreto.
- Reward: QoE parametrizable; el paper considera preferencias de usuario.
- Arquitectura: meta-politica que puede adaptarse a tareas/entornos.
- Entrenamiento: offline meta-training sobre multiples condiciones; online
  adaptation/few-shot para personalizar la politica.
- Evaluacion: vehiculos, usuarios, tipos de red, 4G/5G y preferencias QoE;
  compara con Pensieve, Oboe, Comyco, RobustMPC.
- Que aporta: tratar cada regimen de red como tarea, no como ruido.
- Que no aporta: online fine-tuning complica reproducibilidad y auditoria en
  nuestro controller Phase 6.

Uso propuesto: adaptar por embedding/selector sin entrenamiento online.

## 07 - MERINA

PDF: `MERINA.pdf`.

Implementa meta-RL para mejorar generalizacion de ABR neural desacoplando
dinamica de throughput y politica de control.

- Estado: historial de throughput/player.
- Accion: bitrate.
- Reward: QoE ABR.
- Arquitectura: meta-RL con modelado de incertidumbre de dinamica y busqueda de
  meta-politica.
- Entrenamiento: tareas con dinamicas mezcladas y replay buffer.
- Evaluacion: datasets de trazas, comparacion con clasicos/neuronales, fast
  adaptation a nuevos entornos.
- Que aporta: justificar que un modelo unico puede comprometerse demasiado.
- Que no aporta: implementacion simple y directa para nuestro primer v1.

Uso propuesto: soporte teorico para Plan B de contexto/expertos.

## 08 - MetaABR

PDF: `MetaABR_A_Meta-Learning_Approach...pdf`.

Implementa meta-learning para transferir conocimiento entre tareas ABR.

- Estado: features de red/player/video segun tarea.
- Accion: bitrate.
- Reward: QoE, con analisis de trade-offs entre metricas.
- Arquitectura: actores especificos y mecanismo meta/critic para transferencia.
- Entrenamiento: tareas especificas y aprendizaje de conocimiento transferible.
- Evaluacion: datasets de red, multi-video, varias metricas QoE.
- Que aporta: diseño task-aware y transferencia.
- Que no aporta: safety de buffer ni sampler tail-trace como foco principal.

Uso propuesto: referencia secundaria de meta-learning.

## 09 - Ahaggar bitrate guidance

PDF: `Bitrate_Adaptation_and_Guidance_With_Meta_Reinforcement_Learning.pdf`.

Implementa guia de bitrate server/edge-assisted con meta-RL y multiples
clientes.

- Estado: condiciones de red, estado cliente, resolucion/dispositivo, contenido
  y estado agregado multi-cliente.
- Accion: bitrate guidance para cada cliente.
- Reward: QoE individual y rendimiento multi-cliente; tambien considera
  resolucion y percepcion.
- Arquitectura: MARL/POMDP, centralized training/decentralized execution,
  A2C/DPPO y MAML.
- Comunicacion: CMCD/CMSD para intercambio cliente-servidor.
- Entrenamiento: meta-training offline y meta-testing/adaptacion.
- Evaluacion: multiples clientes, resoluciones, redes heterogeneas, fairness y
  QoE.
- Que aporta: separacion cliente ligero/servidor inteligente y fairness.
- Que no aporta: nuestro servidor Ubuntu no decide ABR ni usa CMCD/CMSD.

Uso propuesto: trabajo futuro multi-cliente/edge, no Fase 4-5 v1.

## 10 - ANT

PDF: `ANT.pdf`.

Implementa un framework multi-modelo que detecta dinamicas de red y activa el
ABR especializado correspondiente.

- Estado para detector: historial temporal de throughput.
- Estado para ABR: observaciones de red/player.
- Accion: seleccion de bitrate por modelo ABR especializado.
- Reward: QoE ABR durante entrenamiento de cada modelo.
- Arquitectura: clustering de Network Trace Segments + detector 1D-CNN +
  multiples modelos RL por condicion.
- Entrenamiento: clusterizar trazas, entrenar detector y entrenar un modelo por
  cluster/condicion.
- Runtime: detector recurrente identifica condicion actual y selecciona modelo.
- Evaluacion: VoD/live, datasets publicos y propietario, comparacion con
  Pensieve/Oboe/SOTA.
- Que aporta: especializacion por regimen y deteccion temporal.
- Que no aporta: simplicidad; multiples modelos elevan complejidad del bundle.

Uso propuesto: Plan B, o version ligera con detector + politica condicionada.

## 11 - BETA

PDF: `BETA.pdf`.

Implementa un framework spatial-temporal para atacar "ABR
under-generalization".

- Diagnostico: DRL ABR puede lograr buen promedio pero fallar en trazas
  dificiles, quedando lejos del optimo offline.
- Estado: historiales de throughput/download, buffer, bitrate previo, chunks
  restantes, etc. Usa configuracion tipo literatura DRL ABR.
- Accion: bitrate discreto.
- Reward: QoE con calidad, rebuffer y variacion.
- Modulo espacial: entrena modelo base, evalua por traza contra optimo offline,
  etiqueta trazas normales/dificiles y entrena clasificador.
- Modulo temporal: entrena con secuencias multi-step de estado-accion-reward para
  decisiones de horizonte mas largo.
- Evaluacion: A3C, PPO, TD3, DDPG, DQN, SAC y SOTA; reporta reduccion fuerte de
  rebuffer en condiciones variables.
- Que aporta: metodologia concreta para encontrar y entrenar sobre casos
  dificiles.
- Que no aporta: implementacion pequena lista para nuestro cliente.

Uso propuesto: construir escenarios de riesgo y sampler balanceado.

## 12 - EAStream

PDF: `EAStream.pdf`.

Implementa un ABR environment-aware con meta-RL basado en contexto latente
probabilistico.

- Estado fisico: observaciones ABR del player/red.
- Estado latente: belief/contexto de entorno inferido desde trayectoria
  historica.
- Accion: bitrate.
- Reward: QoE ABR.
- Arquitectura: encoder GRU/VAE que procesa tuplas historicas de accion, reward
  y estado; decoder reconstruye transiciones/rewards; policy recibe estado +
  belief.
- Entrenamiento: meta-RL/context-based sobre tareas de red; no requiere gradient
  updates online en runtime.
- Evaluacion: trazas reales y OOD; compara generalizacion frente a SOTA.
- Que aporta: modelar incertidumbre sin fine-tuning online.
- Que no aporta: alta complejidad y menor explicabilidad.

Uso propuesto: inspiracion para features/contexto de red, no VAE completo de
inicio.

## 13 - Fortuna

PDF: `Fortuna.pdf`.

Implementa offline RL + meta-learning para ABR en redes diversas.

- Estado: estado ABR con red/player.
- Accion: bitrate.
- Reward: QoE.
- Arquitectura/algoritmo: advantage-weighted regression, value/meta-policy,
  curriculum learning con longitudes crecientes.
- Datos: datasets offline y demostraciones/experiencias previas.
- Entrenamiento: offline, evitando exploracion real costosa; meta-learning para
  adaptacion a entornos.
- Evaluacion: trace-driven y escenarios reales; compara con SOTA RL/baselines.
- Que aporta: superar BC puro usando returns/offline RL.
- Que no aporta: offline RL puede extrapolar mal si no hay action masks y
  conservadurismo.

Uso propuesto: fine-tuning offline despues de BC, con safety estricto.

## 14 - SABR

PDF: `2509.10486v1.pdf`.

Implementa un framework de BC pretraining + PPO fine-tuning para ABR.

- Estado: sigue diseno de Pensieve; matriz/feature vector de historial, buffer,
  bitrate, chunks, etc.
- Accion: bitrate discreto.
- Reward: QoE tipo Pensieve durante fine-tuning.
- Pretraining: DPO-style behavior cloning por pares accion experta/preferida vs
  accion peor.
- Fine-tuning: PPO con actor y critic.
- Benchmarks: ABRBench-3G y ABRBench-4G+, con train/test/OOD y trazas como
  Lumos, FCC, Oboe, Puffer.
- Implementacion: PyTorch para BC, Stable-Baselines3/PPO para RL fine-tuning.
- Evaluacion: compara con BOLA, RobustMPC, Pensieve, Comyco, NetLLM; preserva
  granularidad de trace set en evaluacion.
- Que aporta: receta moderna y estable de entrenamiento.
- Que no aporta: no resuelve automaticamente safety si el reward no se adapta.

Uso propuesto: receta principal de entrenamiento, pero con reward y sampler
risk-aware.

## 15 - Gelato / Plume

PDF: `Gelato.pdf`.

Implementa un controller Gelato y un framework Plume para balancear trazas en
DRL ABR.

- Problema: skew de input traces. Las trazas lentas/dificiles son raras, pero
  dominan stalls y fallos.
- Estado/accion/reward: framework DRL ABR, con estado del player/red, bitrate
  como accion y reward QoE.
- Arquitectura Gelato: variante DRL evaluada tambien con Ape-X DQN en analisis.
- Plume etapa 1: extrae features de series temporales de trazas, usando tsfresh
  e informacion gain para quedarse con features criticas.
- Plume etapa 2: clusteriza trazas usando esas features.
- Plume etapa 3: prioriza clusters/trazas durante acting, no solo transiciones
  en replay buffer.
- Evaluacion: Puffer real durante mas de un ano, 59 stream-years, 280k usuarios;
  tambien TraceBench controlado.
- Que aporta: metodologia muy concreta para entrenar mas en casos dificiles.
- Que no aporta: infraestructura Puffer ni datos reales de usuarios.

Uso propuesto: sampler Phase 4-5 v1 por buckets/clusters de throughput, minima,
varianza, caidas y burstiness.

## 16 - SODA

PDF: `SODA.pdf`.

Implementa un controller ABR de control/optimizacion para suavidad y buffer
estable.

- Estado: buffer, bitrate previo, predicciones de throughput y dinamica temporal
  del stream.
- Accion: bitrate para intervalo/segmento.
- Coste/reward: minimiza coste de distorsion/calidad, coste de buffer y coste de
  switching.
- Idea clave: no penaliza solo rebuffer cuando buffer llega a cero; penaliza
  alejarse de un buffer target antes, usando una funcion suave.
- Arquitectura: no es red neuronal principal; es optimizacion basada en smoothed
  online convex optimization.
- Evaluacion: simulacion, prototipo y produccion; reduce switching y mejora
  QoE/duracion.
- Que aporta: principio de safety mas importante del corpus para nuestro caso.
- Que no aporta: IA representativa por si sola; es mas control que ML.

Uso propuesto: safe layer y reward shaping de `neural_abr_risk_guard_v1`.

## 17 - Incendio short-video MARL

PDF: `3592473.3592564.pdf`.

Implementa un ABR para short-video con multi-agent RL y expert guidance.

- Estado: throughput pasado, buffer por video de la cola, tamanos de chunks,
  user retention, rebuffer reciente y estado de prefetch.
- Accion BM-agent: dormir o elegir que video prefetchar.
- Accion BA-agent: bitrate del chunk del video elegido.
- Reward: utility de short-video = QoE menos rebuffer y ancho de banda
  desperdiciado, ponderado por retention.
- Arquitectura: dos agentes actor-critic; GRU para ancho de banda y CNN/FC para
  vectores de cola; CTDE.
- Entrenamiento: primero imitation learning desde reglas expertas PDAS; luego
  multi-agent PPO.
- Evaluacion: compara contra PDAS, MPC y otros en short-video; mide utility,
  bitrate, rebuffer, smoothness, bandwidth wastage e inference time.
- Que aporta: separacion de decisiones y pretraining experto + MARL.
- Que no aporta: nuestro Phase 6 no tiene cola de videos, retention ni prefetch
  multi-video.

Uso propuesto: fase posterior short-video, no primer controller Phase 6.

## 18 - PPO-ABR

PDF: `PPO-ABR_...pdf`.

Implementa ABR con PPO.

- Estado: throughput/buffer/bitrate historico.
- Accion: bitrate.
- Reward: QoE con calidad, rebuffer y smoothness.
- Arquitectura: actor-critic PPO.
- Entrenamiento: on-policy PPO en simulador.
- Evaluacion: trazas y comparacion con ABR/DRL existentes.
- Que aporta: PPO como alternativa estable a A3C.
- Que no aporta: no aporta por si solo sampler, safety ni generalizacion.

Uso propuesto: tecnica de fine-tuning, no plan completo.

## 19 - ALVS live

PDF: `1-s2.0-S1084804522001035-main.pdf`.

Implementa live streaming DRL con decision conjunta bitrate + playback speed.

- Estado: bitrate actual, bandwidth, download time, buffer, live latency,
  tamanos de proximos segmentos y segmentos restantes.
- Accion: par discreto `(bitrate, playback_speed)`.
- Reward: QoE de live, incluyendo calidad, freezing, smoothness y latencia.
- Arquitectura: actor-critic/A3C.
- Entrenamiento: simulador DASH/CMAF live con trazas.
- Evaluacion: trazas 4G reales, baselines live/rule-based/DRL.
- Que aporta: control conjunto de dos palancas.
- Que no aporta: nuestro runtime no permite playback speed ABR formal.

Uso propuesto: trabajo futuro live, no Fase 4-5 v1.

## 20 - Edge-assisted RL

PDF: `1-s2.0-S1084804523000231-main.pdf`.

Implementa adaptacion HTTP con asistencia edge para multiples clientes.

- Estado: informacion QoE de clientes, red, buffer, video, competencia de ancho
  de banda.
- Accion: bitrate/calidad por cliente.
- Reward: QoE individual + fairness.
- Arquitectura: RL actor-critic en edge server.
- Entrenamiento: simulacion multi-cliente con redes variables.
- Evaluacion: trazas reales, videos distintos, comparacion con esquemas edge y
  heuristicas.
- Que aporta: fairness y calidad subjetiva multi-cliente.
- Que no aporta: Phase 6 actual es single-client y servidor pasivo.

Uso propuesto: futuro multi-cliente/edge.

## 21 - Quality-distance DRL

PDF: `applsci-13-11697.pdf`.

Implementa ABR DRL que introduce distancia de calidad entre segmentos
consecutivos.

- Estado: bandwidth/throughput, buffer y calidad previa.
- Accion: bitrate/calidad siguiente.
- Reward: suma de calidad menos rebuffering menos penalizacion por distancia de
  calidad.
- Arquitectura: DRL/DQN-style segun formulacion del paper.
- Entrenamiento: simulacion DASH wireless.
- Evaluacion: redes wireless y videos diversos; compara QoE y estabilidad.
- Que aporta: penalizar saltos grandes de calidad.
- Que no aporta: risk-aware buffer ni generalizacion avanzada.

Uso propuesto: `large_jump_penalty` complementario.

## 22 - PLL-ABR

PDF: `075042_1_5.0277381.pdf`.

Implementa PPO con LSTM y local attention para ABR.

- Estado: buffer, throughput historico, descarga, bitrate/calidad y seniales del
  player.
- Accion: bitrate.
- Reward: QoE con bitrate utilization, rebuffer penalty y smoothness penalty.
- Arquitectura: actor-critic PPO con dual clipping + LSTM local attention.
- Entrenamiento: PPO en simulador ABR.
- Evaluacion: buffer-based, rate-based, RobustMPC, BOLA y otros; reporta mejora
  media de QoE.
- Que aporta: memoria temporal y atencion local para patrones de red.
- Que no aporta: no ataca por si solo tail traces ni safety.

Uso propuesto: GRU/LSTM ligero si el scorer necesita memoria.

## 23 - BPA bandwidth prediction + DRL

PDF: `Enhancing_Adaptive_...Bandwidth_Prediction...pdf`.

Implementa dos modulos: prediccion de bandwidth y seleccion de bitrate.

- BPM: BiLSTM para predecir throughput/bandwidth.
- BSM: actor-critic para elegir bitrate.
- Estado BSM: buffer, bitrate y prediccion/estado de red.
- Accion: bitrate.
- Reward: QoE + termino relacionado con precision de prediccion.
- Entrenamiento: loss conjunta/end-to-end con error de prediccion y RL.
- Evaluacion: compara predictor BiLSTM/LSTM y ABR frente a baselines.
- Que aporta: separar prediccion y decision.
- Que no aporta: BiLSTM puede ser no causal si se usa mal; precision de
  prediccion no garantiza menos rebuffer.

Uso propuesto: predictor causal cuantile para Plan C, no BiLSTM literal.

## 24 - MamBRA

PDF: `v1_covered_4254418a-5dc6-4da1-be54-5ccdcf966b39.pdf`.

Implementa prediccion de bandwidth por sesion usando Mamba/SSM.

- Estado/datos: secuencias de sesion con features numericas/categoricas.
- Accion: no es un ABR controller directo; produce predicciones de bandwidth.
- Objetivo: minimizar error de prediccion y mejorar estabilidad temporal/QoE
  derivada.
- Arquitectura: selective state-space model tipo Mamba.
- Entrenamiento: supervised time-series, splits por sesiones disjuntas para
  evitar leakage.
- Evaluacion: accuracy, MAE/RMSE o equivalentes, estabilidad y QoE con ancho de
  banda predicho.
- Que aporta: split por sesion y modelos secuenciales eficientes.
- Que no aporta: decision ABR completa ni safety.

Uso propuesto: variante avanzada de predictor si el entorno lo soporta.

## 25 - GreenABR

PDF: `3524273.3528188.pdf`.

Implementa ABR DRL energy-aware.

- Estado: red/player y posiblemente seniales de dispositivo/energia.
- Accion: bitrate.
- Reward: QoE menos coste energetico.
- Arquitectura: DRL para control ABR.
- Entrenamiento/evaluacion: compara trade-off energia/QoE frente a baselines.
- Que aporta: multiobjetivo energia.
- Que no aporta: no tenemos medicion energetica ni objetivo de energia en Phase
  6.

Uso propuesto: memoria/trabajo futuro.

## 26 - Visual sensitivity aware ABR

PDF: `3591108.pdf`.

Implementa ABR DRL con sensibilidad visual/contenido.

- Estado: red, buffer y features de sensibilidad visual por segmento/video.
- Accion: bitrate.
- Reward: QoE perceptual considerando HVS/sensibilidad.
- Arquitectura: modelo de sensibilidad + politica DRL.
- Entrenamiento/evaluacion: evalua modelo HVS y ABR frente a baselines; mide
  overhead.
- Que aporta: bitrate no equivale a calidad perceptual.
- Que no aporta: nuestro pipeline no tiene VMAF/content features cerrados.

Uso propuesto: futuro content-aware.

## 27 - KPCA/GWO/LSSVM bit rate selection

PDF: `1-s2.0-S1687850724002206-main.pdf`.

Implementa una tecnica AI hibrida para seleccion/prediccion de bitrate, mas
cercana a regresion/optimizacion que a ABR secuencial moderno.

- Estado/features: variables de red/imagen/streaming segun paper.
- Accion/salida: seleccion o prediccion de bitrate.
- Modelo: Kernel PCA + Grey Wolf Optimization + least-squares SVM/BP.
- Entrenamiento: supervisado/optimizacion de parametros.
- Evaluacion: accuracy/error de seleccion.
- Que aporta: ejemplo de AI no-RL.
- Que no aporta: buffer dynamics, rebuffer risk, QoE secuencial.

Uso propuesto: no usar como base.

## 28 - DQNReg

PDF: `v1_covered.pdf`.

Implementa rate adaptation con DQN/regresion.

- Estado: throughput, bitrate y buffer.
- Accion: calidad/bitrate.
- Reward: QoE con calidad, starvation/rebuffer, switching y estabilidad.
- Arquitectura: DQNReg.
- Entrenamiento: RL en simulacion.
- Evaluacion: entornos dinamicos, QoE, rebuffer/starvation, switching.
- Que aporta: variante DRL historica.
- Que no aporta: safety ni generalizacion por regimen.

Uso propuesto: referencia secundaria.

## 29 - Review learning-based 2025

PDF: `A_Review_of_Learning-Based_Methods_for_Adaptive_Video_Streaming_Over_HTTP.pdf`.

No implementa un modelo concreto. Es un survey actualizado de learning-based
adaptive streaming.

- Cubre: supervised learning, RL, imitation, meta-learning, QoE-aware,
  encoding, super-resolution y optimizacion.
- Evaluacion: taxonomica, no benchmark propio.
- Que aporta: mapa bibliografico para memoria.
- Que no aporta: spec implementable.

Uso propuesto: antecedentes y justificacion de familias.

## 30 - HAS review 2025

PDF: `3736306.pdf`.

Survey amplio de HTTP Adaptive Streaming.

- Cubre: codificacion, delivery, consumption, ABR, QoE, energia, low latency,
  codecs, retos futuros.
- Evaluacion: revision, no controller.
- Que aporta: contexto general y limites del TFG.
- Que no aporta: modelo IA ABR.

Uso propuesto: memoria y trabajo futuro.

## 31 - KAKEN fair multi-user report

PDF: `kaken.nii.ac.jp_20K14740seika.pdf`.

Informe de investigacion sobre high-QoE y fairness en multi-user networks.

- Implementacion: no se identifica una spec reproducible directa desde el PDF
  extraido; es mas informe de resultados.
- Objetivo: fairness/QoE multiusuario.
- Que aporta: tema futuro multi-cliente.
- Que no aporta: controller plug-and-play para Phase 6.

Uso propuesto: no implementar en v1.

## 32 - Lectura final para Fase 4-5 v1

Los papers mas accionables para construir algo nuevo son:

1. `SODA`: convertir rebuffer en riesgo temprano de buffer.
2. `Gelato/Plume`: entrenar con trazas dificiles y no dejar que la media mande.
3. `SABR`: BC pretraining + PPO fine-tuning como receta estable.
4. `Comyco`: usar expertos para arrancar sin exploracion inutil.
5. `Fortuna`: usar offline RL/advantage para superar la imitacion simple.
6. `BETA`: identificar condiciones donde el modelo fallaria y entrenarlas aparte.
7. `ANT/Oboe/EAStream`: adaptar la politica al regimen de red.

Eso apunta a un controller nuevo, no derivado de los anteriores:

```text
neural_abr_risk_guard_v1
  = scorer/policy neuronal
  + entrenamiento balanceado por escenarios dificiles
  + pretraining experto
  + fine-tuning offline controlado
  + safe layer de buffer target/riesgo
  + telemetria por chunk
```
