# Notas del 6.6 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_6_exploratorio.docx` (≈1230 palabras de cuerpo, 3 páginas, 3
subapartados, Tabla 6.10, sin figura, sin ecuaciones, sin citas). Generado por `docs/memoria/apoyo/generar_cap6_6.py`.
Comprobador sin avisos; render con Word revisado.

## Qué hace el script (todo por programa)

- Tabla 6.10: toma los IC de `contrastes_prerregistrados.json → estratos` (fcc, oboe, videos_vistos, video_nuevo ×
  mpc_robusto / propio_cuantiles_recientes × QoE / paradas) y recalcula cada media con
  `contrastes.diferencias_por_ventana` del entregable con el filtro del estrato: 18/56/74/74 ventanas, 36/112/148/148
  escenarios, medias iguales.
- Medias absolutas por estrato desde `sesiones.csv` (propio FCC 2,620 / MPC 2,581; Oboe 2,524 / 2,537; vistos 2,503 /
  2,482; nuevo 2,591 / 2,614). Comprueba que los OCHO controladores tienen más QoE con Tears que con los vistos.
- Interacción: recalculada ventana a ventana (nuevo − visto de la diferencia propio − MPC): media −0,045 = JSON; 40/31/3;
  IC95 [−0,077; −0,014]; p signo bilateral 0,34.
- Ejemplo (regla fijada antes de mirar: la ventana con la interacción más negativa): ventana 59 (Oboe), Paseo 60 fps:
  propio 1,362 (0 paradas) / MPC 0,893 (1 parada); Tears: propio 1,286 (0) / MPC 1,396 (1); interacción −0,579;
  bitrate con Tears 1481 frente a 1647 kbit/s. Lección: la interacción extrema la causa una parada del MPC con el
  vídeo visto (QoE 0,893), no que el MPC «aproveche» el contenido nuevo; por eso el texto dice «cambia mucho de un
  vídeo al otro, a menudo por una sola parada».
- Sintéticas (3 × 8 = 24 sesiones): estable baja (propio 0,61, MPC 0,56, variantes 0,56–0,61); perfecta alta (los
  cinco que planifican 4,02; clásicos 2,92–3,73); oscilación periódica (propio 2,71, MPC 2,66, variantes 3,30–3,53,
  BBA 3,36). Medias: propio 2,448 / 0 paradas; MPC 2,416 / 1 parada en total (0,33 por sesión); BOLA 7 paradas.

## Fuente de cada número

| Dato | Fuente |
|---|---|
| Tabla 6.10 (medias e IC) | `contrastes_prerregistrados.json → estratos` (medias recalculadas) |
| FCC: +0,038 [+0,005; +0,076], −0,194 [−0,361; −0,056]; Oboe: −0,013 [−0,038; +0,011], −0,098 [−0,188; −0,027] | ídem |
| Vistos: +0,021 [−0,007; +0,051], −0,176 [−0,297; −0,081]; nuevo: −0,023 [−0,046; −0,000], −0,068 [−0,135; +0,000] | ídem |
| Interacción −0,045 [−0,077; −0,014], p 0,34, 40/31/3 | `contenido_nuevo_frente_a_visto` |
| CV 0,28–0,31 vs ≤ 0,19; primeros segmentos 2–6 % | 6.1 (descriptores) |
| Sintéticas | `sesiones.csv` (sintetica = 1) |

## Decisiones de redacción

- Todo marcado como exploratorio: sin corrección por multiplicidad, intervalos informativos, «ninguna cifra decide».
- Se dice que la interacción tiene dos lecturas que no coinciden del todo (IC excluye 0; signo p 0,34) en vez de elegir
  la favorable.
- Las dos hipótesis de trabajo (VBR mayor; primeros segmentos casi negros) se presentan como NO comprobadas y se mandan
  al 7.4. OJO: la segunda hipótesis dice que el MPC robusto «rebaja por su error máximo» las primeras medidas; el
  propio también las ensancha por el desacuerdo del ensemble, pero la red no vio descargas de 2–6 % del nominal. Es
  hipótesis, no afirmación.
- El dato «con Tears todos los controladores tienen más QoE» se explica por los tamaños reales menores que el nominal
  (8–12 % por debajo, 6.1): con la misma red, los segmentos de Tears bajan antes.
- Sintéticas: «ninguna contradice lo observado en las reales»; con la oscilación periódica el propio queda por debajo
  de sus variantes (2,71 frente a 3,30–3,53) porque amortigua; se dice tal cual.

## Preguntas probables del tribunal

1. **¿El controlador falla con contenido nuevo?** No: 0,041 paradas por sesión, igual que con los vistos, y la QoE
   sube (2,591). Lo que se estrecha es la ventaja sobre el MPC robusto (−0,068 paradas, IC roza 0; QoE −0,023 dentro
   del margen).
2. **¿Por qué el IC de la interacción excluye 0 pero el signo no?** El IC es sobre la media (sensible a magnitudes);
   el signo cuenta ventanas (40 frente a 31). Unas pocas ventanas con una parada del MPC con el vídeo visto mueven la
   media. Honestidad: se dan las dos.
3. **¿Por qué FCC va mejor?** Redes fijas estables: la predicción es fácil y el propio apura más sin riesgo; en Oboe
   (variable) paga su prudencia con ~0,013 de QoE.
4. **¿Por qué el propio pierde con la oscilación periódica sintética?** Amortigua la oscilación (CVaR sobre tres
   escenarios); las variantes la siguen y ganan QoE porque la oscilación no vacía el buffer. Con red real variable
   (Oboe) esa prudencia es la que evita paradas.

## Qué se puede recortar

El párrafo de las sintéticas a la mitad y la segunda hipótesis de trabajo. Mantener la Tabla 6.10 y la interacción.
