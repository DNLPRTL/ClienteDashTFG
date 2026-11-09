# Notas del 5.7 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap5_7_entorno_entrenamiento.docx` (≈1720 palabras de cuerpo,
5 páginas, 4 subapartados, Figura 5.6, Tablas 5.13 a 5.15, ecuaciones 5.13 y 5.14, sin citas nuevas).
Generado por `docs/memoria/apoyo/generar_cap5_7.py`; la calibración sale de
`apoyo/calibracion_validacion.py` → `calibracion_validacion.json` (12 s en CPU).

## Fuente de cada número

| Dato | Fuente |
|---|---|
| ventanas 120 s, 30 segmentos, ≤ 4 por traza, cuotas 35/50/15 %, pesos 5…1 y +1 variable | `plan_muestreo.json` (política) y `entrenamiento/corpus_trazas/muestreo.py` |
| 4096 pedidas y obtenidas de entrenamiento; 1024 pedidas y 935 obtenidas de validación | `plan_muestreo.json` |
| Tabla 5.13 (por origen), 615 y 154 sintéticas, 1799/1473 trazas/grupos (train), 416/356 (val), tramos | contados sobre `plan_muestreo.json` |
| 2895 de 4725 trazas de train con media > 20 Mbit/s | `catalogo_trazas.json` |
| 490 500 / 111 630 muestras; 26 ventanas omitidas (TraceReplayError: traza sin caudal) | `resumen_dataset.json`, `auditoria_no_contaminacion.json` |
| auditorías PASS, eval_usado false, 1829 grupos comprobados | `auditoria_muestreo.json`, `auditoria_no_contaminacion.json` |
| 8 descriptores de 4 s, rotación por SHA-256 del id de ventana, 1 min = 15 segmentos cíclicos | `entrenamiento/dataset_fiel.py`, `core/modelo_propio/perfil_video.py` |
| 4 reglas de recorrido (0,85·HM; +1 si buffer ≥ 8 s; mínimo si < 4 s, ≤ 1 si < 8 s; cíclica) | `dataset_cuantiles._elegir_accion_rollout` |
| etiqueta: media ponderada de la traza en los 4 s del horizonte, ε = 1 bit/s | `dataset_cuantiles._construir_objetivo`, `estado_sesion.EPSILON_THROUGHPUT_BPS` |
| 5 miembros, 80 épocas, lote 1024, lr 3e-4, AdamW wd 1e-5, clip 5, λ = 0,05, dropout 0,1, semillas 461000 + 101·m, mejor época por pinball de validación, tolerancia de cobertura 0,08 | `entrenamiento/entrenamiento_modelo.py` (perfil `full`) |
| GPU RX 7800 XT, ROCm 7.2.1, PyTorch 2.9.1 | `00_info_entorno/info_entorno_wsl.txt`, `docs/defensa/componentes_experimento.md` |
| Tabla 5.14 (cobertura 0,070 / 0,183 / 0,439 / 0,790; error máx 0,067; pinball 0,162; miembros 0,162–0,163; sin ensanchado q10 0,072) | `calibracion_validacion.json` |
| bundle: α 0,75, pesos 4,3 y 1, ensanchado 1,0, SHA-256 de 4 ficheros | `03_modelos/.../configuracion_planificador.json`, `manifiesto.json` |

## Lo que NO está en TFG Material (y se ha evitado afirmar)

- El informe de entrenamiento (`reporte_entrenamiento_temporal.json`: mejor época de cada miembro,
  cobertura en el momento del entrenamiento, horas de GPU) no está en `03_modelos` ni en `TFG\modelos`.
  Por eso la calibración de la Tabla 5.14 se RECALCULA con el bundle entregado sobre el dataset
  entregado, en vez de citar el informe. Si Daniel lo tiene en WSL
  (`~/TFG/modelos/modelo_propio/entrenamiento/full_multimedia/reporte_entrenamiento_temporal.json`),
  copiarlo a `TFG Material\03_modelos\modelo_propio\` permitiría citar las mejores épocas y el tiempo.
- La duración del entrenamiento y la fecha no se dicen (no hay registro en el material).

## Citas

Ninguna nueva. GRU, pinball y deep ensembles ya se citan en el 5.6. AdamW no está en el .bib
(Loshchilov y Hutter 2019); se nombra sin cita. Si Daniel quiere citarlo: arXiv 1711.05101.

## PDF descargados en este turno (permiso de Daniel, 09/11)

- `biblioteca_final/10_fundamentos_matematicos/cho2014gru.pdf` (arXiv 1406.1078, 1,1 MB): verificado
  p. 3 (reset gate, update gate).
- `.../lakshminarayanan2017ensembles.pdf` (arXiv 1612.01474, 1,5 MB): verificado p. 4 («random
  initialization of the NN parameters, along with random shuffling... was sufficient»).
- `.../rockafellar2000cvar.pdf` (web del autor, 0,2 MB): verificado p. 2 («α-CVaR is the conditional
  expectation of losses above that amount α»).
- Koenker y Bassett 1978: JSTOR devolvió la página HTML de acceso; el PDF libre de la web de Koenker es
  otro artículo (Quantile Regression, 2001) y NO se ha guardado como el de 1978. Queda sin PDF, anotado
  en `02_BIBLIOGRAFIA_DEFINITIVA.md`; Daniel puede bajarlo con el acceso UGR a JSTOR (stable/1913643).

## Preguntas probables del tribunal

1. **¿Por qué no entrenar con el cliente real?** Coste: 5031 ventanas × 4 recorridos × 2 min ≈ 670 h; el
   simulador comparte la física (modelo de red y tamaños reales) y produce lo mismo en minutos. La
   fidelidad del simulador se comprobó además en el blindaje (modo forzado, mediana |ΔQoE| = 0).
2. **¿Las reglas de recorrido no sesgan al modelo?** Solo deciden qué estados se visitan; la etiqueta es
   el futuro de la traza, independiente de la acción. Cuatro reglas distintas cubren buffers altos y
   bajos y todos los niveles (la cíclica).
3. **¿La etiqueta es el throughput que medirá el cliente?** No exactamente: es el ancho de banda medio de
   la traza en los 4 s siguientes. Está declarado como límite.
4. **¿Está calibrado?** Error máximo de cobertura 0,067 < 0,08; sesgo prudente (cuantiles bajos cubren
   menos). El q10 del primer horizonte es el más pesimista (0,036).
5. **¿Validación = evaluación?** No: validación es la partición `test` del catálogo (sin grupos en común
   con train); evaluación es `eval`, prohibida en el muestreo y auditada. La calibración de la Tabla 5.14
   es sobre validación, con la que también se eligió α: lo dice el texto.
6. **¿Por qué 80 épocas si hay parada temprana?** El entrenador no para: entrena las 80 y conserva la
   mejor época según la pinball de validación.

## Detalles que el texto no cuenta

- La semilla del muestreo es una cadena con nombre interno de fase (`phase45_v3_full_qh_dataset_seed`);
  los identificadores de ventana llevan `phase45v1`: nombres heredados, datos, no entradas del modelo.
- `FASE_DATASET_QH = "dataset_qh_bucle_cerrado"` y `estado_linea = "puntuador_qh_no_es_el_controlador"`
  siguen en los metadatos del dataset: restos de la línea Q_H abandonada (7.5).
- El `plan_muestreo.json` del dataset guarda `id_perfil_video: paseo_10min_30fps_4s` aunque el dataset
  rotó 8 vídeos (el resumen sí dice `vbr_real_del_servidor` y el primer perfil).
- `max_bucles = 5` en el simulador (frente a 1 en la evaluación).
- La validación del dataset solo inspecciona las 50 primeras muestras de cada fichero (`_errores_muestra`).

## Qué se puede recortar

El párrafo de límites (a la mitad) y la Tabla 5.15 si el Anexo A recoge los parámetros. Mantener la
Tabla 5.14 y la ecuación (5.13).
