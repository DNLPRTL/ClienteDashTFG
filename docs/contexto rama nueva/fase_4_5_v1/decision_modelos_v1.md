# Decision inicial de modelos Fase 4-5 v1

Status: propuesta_inicial_no_implementada.

Esta decision se basa en la auditoria inicial de los 32 PDFs del corpus ABR/IA,
en el contrato tecnico de Phase 6 y en las trazas disponibles. Los dos
controllers propios anteriores se consideran pruebas de integracion cerradas:
demostraron que el pipeline puede cargar bundles, ejecutar inferencia real y
auditar fallback, pero no son la base cientifica ni tecnica de Fase 4-5 v1.

## Diagnostico de alto nivel

Fase 4-5 v1 empieza como diseno nuevo. El diagnostico de fondo no es "arreglar"
los modelos anteriores, sino evitar repetir las debilidades tipicas de muchos
ABR neuronales:

- aprender acciones discretas sin una nocion fuerte de riesgo;
- optimizar QoE medio y fallar en tail traces;
- subir demasiado tarde o bajar tarde ante caidas;
- tratar redes bajas, variables y altas como si fueran el mismo problema;
- usar prediccion de throughput sin incertidumbre;
- producir decisiones dificiles de explicar academicamente.

## Principio de diseno

Fase 4-5 v1 debe pasar de "modelo que imita una accion" a "controller IA con
riesgo explicito".

La estrategia recomendada combina cinco ideas del corpus:

- `SODA`: penalizar peligro de buffer antes del rebuffer, no solo cuando ya
  ocurrio.
- `Gelato/Plume`: balancear entrenamiento por clusters de trazas, sobre todo
  tail-end y redes bajas.
- `SABR/Comyco`: usar behavior cloning para arrancar estable.
- `Fortuna/BETA`: mejorar con offline RL o advantage-weighted updates sobre
  trayectorias y no solo labels.
- `ANT/EAStream/Oboe`: condicionar la decision al entorno/regimen de red.

## Plan A - `neural_abr_risk_guard_v1`

Prioridad: 1.

Tipo: policy/scorer neuronal con capa segura fuerte.

Objetivo:

- reducir rebuffering en redes bajas y variables;
- mantener fallback 0;
- que la accion segura sea explicable por presupuesto de descarga, buffer y
  throughput conservador.

Arquitectura propuesta:

- entrada runtime permitida: throughput pasado, download time pasado, buffer,
  bitrate/calidad previa, historial de switches, chunk duration, ladder;
- modelo: candidate scorer pequeno que estima utilidad/riesgo por representacion;
- salida: score por calidad, accion cruda y accion segura;
- safe layer: mascara por viabilidad de descarga con throughput conservador
  percentil bajo, buffer target y limite de salto.

Training propuesto:

1. Generar trayectorias offline con controllers clasicos reales y replay Phase 4.
2. Crear labels mixtos: robust_mpc, rate_based en redes peligrosas, BBA/BOLA en
   casos de buffer alto, y teacher hibrido solo si no induce rebuffer.
3. Pretraining BC/DPO-style al estilo Comyco/SABR.
4. Fine-tuning offline con recompensa `qoe_linear_v1` modificada solo en
   entrenamiento para riesgo: rebuffer esperado, low-buffer penalty,
   overshoot penalty y switch penalty.
5. Export bundle con schema nuevo y auditoria neural por chunk.

Por que primero:

- ataca directamente el fallo observado;
- usa el cliente actual sin requerir live playback speed, edge server ni VMAF;
- es defendible academicamente como "risk-aware guarded neural ABR";
- puede evaluarse limpio en Phase 6.

## Plan B - `neural_abr_env_expert_v1`

Prioridad: 2.

Tipo: mixture-of-experts o policy condicionada por entorno.

Inspiracion: `ANT`, `BETA`, `A2BR`, `MERINA`, `EAStream`, `Oboe`.

Idea:

- detectar regimen de red en runtime usando solo historial pasado;
- separar escenarios como baja estable, baja variable, media variable, alta
  estable, caidas a cero y sintetica diagnostica;
- elegir una politica especializada o condicionar el scorer con embedding de
  entorno.

Variante conservadora:

- detector ligero de regimen + selector entre experts clasicos/neuronales;
- el modelo aprende cuando debe parecerse a rate_based, bba, robust_mpc o al
  scorer de Plan A.

Variante mas ambiciosa:

- encoder GRU/VAE de historia al estilo EAStream;
- scorer condicionado por latent context;
- varios heads o experts especializados por cluster.

Por que no primero:

- necesita analisis fino de clusters de trazas y fallos actuales;
- puede ser mas dificil de explicar si se entrena antes de cerrar Plan A.

## Plan C - `neural_abr_predictive_mpc_v1`

Prioridad: 3.

Tipo: predictor IA de throughput + decision MPC conservadora.

Inspiracion: `BPA`, `MamBRA`, `ANT`, `SODA`.

Idea:

- entrenar un predictor supervisado de throughput a corto horizonte;
- usar una prediccion conservadora o cuantiles, no solo media;
- alimentar una decision MPC/risk guard que optimice QoE sin ver futuro real.

Modelo posible:

- GRU/TCN cuantile predictor como primera version robusta;
- explorar Mamba/SSM solo si el entorno Python lo soporta sin fragilidad;
- salida: p10/p50/p90 de throughput o distribucion discreta por horizonte.

Valor academico:

- muy defendible si se audita error de prediccion y relacion con rebuffer;
- separa "IA predice red" de "control seguro decide bitrate".

Riesgo:

- si el predictor esta mal calibrado, puede reintroducir agresividad;
- requiere validacion de incertidumbre, no solo MAE/RMSE.

## Plan D - `short_video_marl_expert_v1`

Prioridad: 4, deliberadamente al final.

Inspiracion: `Incendio`.

Motivo:

- es actual y atractivo por TikTok/Reels/Shorts;
- pero no encaja directamente con Phase 6, que evalua streaming DASH VoD por
  segmentos y no cola de videos cortos con prefetch por video-id.

Adaptacion posible:

- crear un modo experimental separado de short sessions;
- usar dos agentes solo si hay dos decisiones reales: prefetch/buffer target y
  bitrate;
- si Phase 6 no incorpora short-video semantics, mantenerlo como extension de
  memoria o fase posterior, no como primer controller formal.

## Trabajo previo obligatorio antes de entrenar

Antes de implementar Plan A:

1. Definir desde cero el contrato de `neural_abr_risk_guard_v1`.
2. Seleccionar las seniales runtime permitidas.
3. Definir escenarios de entrenamiento por regimen de red:
   - baja estable;
   - baja variable;
   - media variable;
   - alta estable;
   - caidas a cero;
   - recuperaciones bruscas;
   - sinteticas diagnosticas separadas.
4. Definir teachers o fuentes de supervision solo si ayudan al nuevo diseno:
   robust_mpc, rate_based, bba, mpc, solver offline propio o politica
   risk-aware. No usar los dos controllers IA anteriores como teacher.
5. Convertir los escenarios de riesgo en acceptance tests offline antes de
   entrenar.

## Decision actual

No entrenar todavia.

Primero cerrar:

- auditoria paper por paper;
- spec de `neural_abr_risk_guard_v1`;
- acceptance tests y telemetry esperada.

Despues iniciar implementacion Fase 4-5 v1 con Plan A.
