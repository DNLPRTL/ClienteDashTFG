# Notas del capítulo 7 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap7_conclusiones.docx` (≈2900 palabras de cuerpo, 6 páginas: apertura,
7.1 Cumplimiento de los objetivos (lista Objetivo 1–5 + párrafo), 7.2 Resultados principales (4 párrafos), 7.3
Limitaciones (3 clases en prosa), 7.4 Trabajo futuro (lista de 7 con entradilla), 7.5 Resultados negativos (intro + 4
párrafos + cierre); 4 citas; sin tablas ni figuras). Generado por `docs/memoria/apoyo/generar_cap7.py`. Comprobador
sin avisos. La biblia pide 4–6 páginas: la primera versión salía a 7 y se recortó (apertura, cierre del 7.1, último
párrafo del 7.2, frase de los rivales del 7.3 que repetía el 7.4, intro del 7.4 y del 7.5).

## Qué comprueba el script (regla cero)

- Del protocolo del experimento final: 5 hipótesis con referencia `controlador_propio`, margen 0,15, Holm, 8
  controladores, 1208 sesiones.
- Del bundle entregado (`03_modelos/modelo_propio/bundle`): 5 miembros, 4 cuantiles, horizonte 5, α = 0,75,
  tamaños `vbr_real_del_servidor`. De ahí «cinco redes recurrentes», «cuatro cuantiles», «cinco segmentos» y «con
  cuatro cuantiles α solo cambia la decisión en saltos de 0,25» (1/K; 07_RESULTADO §8 lo dice igual).
- Del `cap1_introduccion.docx`: existen «Objetivo 1:» … «Objetivo 5:» y la frase del objetivo general (el 7.1 la
  repite en pasado).
- Cada cifra que el 7 repite está ya en los .docx 5.6, 5.7 o 6.1–6.7: −0,001, [−0,018; +0,017], ±0,15, ±0,02, 0,041,
  0,162, 0,439, 0,149, 0,791, 1208, 35 032, 0,625, 74 ventanas, 0,25. Además, cualquier decimal del texto tiene que
  estar en esa lista y cualquier entero de 4+ cifras tiene que ser 1208 o 35 032: el capítulo no puede introducir
  números nuevos sin que el script falle.
- Frases de hecho del 7.1/7.2 ya dichas en los caps 5 y 6: «cuarto de ocho», «el más alto de los ocho», «ninguna
  recurrió al respaldo», «sin ningún respaldo», «segunda máquina», «No hubo ninguna» (desviaciones).
- Ningún nombre interno: SPBC, Q_H, mpc_prudente, Phase, Fase 6, v1, v2, Neural, tfg_final, benchmark_autorizado,
  ensemble temporal, Codex.
- Citas: todas en el .bib; grupos múltiples validados por el script (el comprobador no ve `netflixVmaf` porque el
  patrón de la clave empieza por minúscula seguida de mayúscula; está en el .bib y ya se citó en el 6.7).

## Citas (ya verificadas en capítulos anteriores)

| Clave | Afirmación en el cap 7 | Dónde se verificó |
|---|---|---|
| `yan2020puffer` | despliegue con usuarios reales (Puffer); Fugu reentrena con datos del propio despliegue | p. 1–3 (caps 1, 2 y 5.6) |
| `kan2021bayesmpc` | curva de compromiso al variar el mando de riesgo | p. 1–3 (caps 1 y 5.6) |
| `netflixVmaf` | VMAF como métrica perceptual por segmento | misc web (6.7) |
| `mao2017pensieve` | controladores con aprendizaje de extremo a extremo | p. 2, 5–6 (cap 1) |

## Fuentes de las descripciones del 7.5 (solo contexto; no se citan)

- (1) Clonación de comportamiento: `decision_phase45_v2_spbc_dpo_7b2.md` (CE contra la acción del maestro, pares de
  preferencia, pérdidas de utilidad y de rebuffering; el pilot base pedía de más en 2–5 Mbit/s, el conservador de
  menos) y `decision_phase45_v3_closedloop_spbc_spc_v1_20260615.md` (colapso al conectarla: la dinámica del buffer
  offline no coincidía con la del cliente).
- (2) Función de puntuación con horizonte: `decision_phase45_v3_qh_scorer_hardneg_20260612.md` y `_v2` (top-1 alta,
  arrepentimiento medio sobre el umbral; error concentrado en 2–5 Mbit/s y buffers bajos/medios; reponderaciones
  saturadas). La explicación «no aprendible desde el estado observable» es la del plan maestro (§Capítulo 7).
- (3) Más datos no mejoran: `decision_phase45_v3_neural_mpc_full_v2_after_rapid_20260615.md` (escalar a full
  manteniendo lo demás «para aislar la causa»), CLAUDE.md §5 (v2 más agresiva, más rebuffer) y la memoria
  `vbr-media-fidelity-gap` (entrenamiento CBR frente a cliente VBR → `decision_mpc_prudente_paso0_medio_fiel`).
- (4) Variante MLP: `decision_mpc_prudente_predictor_temporal_opcionB_20260623.md` (el MLP «se pasó de optimista» en
  ventanas duras; GRU + ensemble con ensanchado epistémico). Las 27 ventanas eran de validación (00_HANDOFF_FASE_BLINDAJE §4).
- Regla aplicada: ninguna cifra de esas ejecuciones; descripciones funcionales (04_CORRESPONDENCIAS §5). Si el
  tribunal pide números, están en el histórico (`docs/contexto rama nueva/fase_4_5_v1/`).

## Decisiones de redacción

- 7.1 en lista con entradilla «Objetivo n» (misma forma que el 1.4) y la palabra «Cumplido» al principio de cada
  entrada: el tribunal ve la correspondencia sin buscar. Cada entrada remite a los apartados donde está la evidencia.
- 7.2 repite cifras (la biblia §7 marca como error «conclusiones sin cifras») pero solo las ya dadas; se evita
  «gana»: «equivalencia con menos paradas», «cuarto de ocho», «lo que no se afirma queda dicho».
- 7.3 agrupa las 8 limitaciones del 6.7 en tres clases en prosa en vez de repetir la lista; la frase «validez
  interna sí, alcance no» se mantiene.
- 7.4 en lista con entradilla (biblia §4 lo pide para el trabajo futuro), ordenado de menor a mayor desarrollo;
  condicional en todas («permitiría», «alinearía»). «Redes de mayor capacidad» se limita a la escalera más alta
  (la idea de redefinir el filtro de relevancia sobre la ventana no se ha comprobado y se omite).
- 7.5 abre declarando que las cifras de desarrollo no son comparables con las del cap 6 (regla del experimento
  único) y cierra enlazando con las cuatro decisiones del 1.3. Sin epígrafe de cierre adicional: el cierre del
  capítulo es el último párrafo del 7.5 (último capítulo; el corpus del tutor termina en el trabajo futuro).
- «Objetivo 5 cumplido ≠ mejor resultado»: párrafo pensado para la defensa.

## Preguntas probables del tribunal

1. **¿Se cumplieron todos los objetivos si el controlador no es el mejor?** Sí: el Objetivo 5 era evaluar y declarar
   con exactitud; las hipótesis prerregistradas se aceptaron y lo que no se afirma está dicho (7.1 último párrafo).
2. **¿Por qué contar fracasos?** Explican el diseño final (acotar el aprendizaje, fidelidad al medio) y ahorran camino
   a quien siga; es la cuarta aportación declarada en el 1.3.
3. **¿Cuál es el trabajo futuro más importante?** La red real (pila TCP y tráfico competidor), porque es la
   limitación que más acota el alcance; el cliente ya separa el descargador de la emulación.
4. **¿Por qué no más cuantiles ya?** Con 4 cuantiles el mando α salta de 0,25 en 0,25; predecir más cuantiles cambia
   el modelo y exige reentrenar y recalibrar: queda como trabajo futuro.

## Qué se puede recortar

El tercer párrafo del 7.2 (cuadro completo) a dos frases y las entradas «Redes de mayor capacidad» y «Rivales
adicionales» del 7.4. Mantener el 7.1 completo, el primer párrafo del 7.2 y los cuatro párrafos del 7.5.
