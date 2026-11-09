# Notas del 6.7 y del cierre del capítulo 6 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_7_interpretacion_cierre.docx` (≈1280 palabras de cuerpo, 3 páginas:
6.7.1 qué se afirma y qué no, 6.7.2 limitaciones en lista con entradilla, 6.7.3 fidelidad al protocolo, y el
cierre del capítulo en dos párrafos SIN epígrafe, como en el capítulo 5). Una cita: `netflixVmaf` (misc, repositorio
web, sin PDF: se cita como lo que es). Generado por `docs/memoria/apoyo/generar_cap6_7.py`. Comprobador sin avisos.

## Qué hace el script

- Carga contrastes, agregados, protocolo y sesiones; comprueba 1184 reales, 74 ventanas (56 Oboe / 18 FCC), cociente
  de paradas MPC/propio = 4,00 exacto (0,16216/0,04054 = 24/6), y que el propio es el 4.º en QoE.
- Comprueba que CADA cifra que repite (−0,001, [−0,018; +0,017], 0,041, 0,162, 35 032, 1208, 41,3 h, 0,28 y 0,31,
  −0,045, p = 0,34, 2,547, 2,583, 0,625, ±0,02, +0,149, −0,791, −0,439, −0,122, 2,1 %) ya aparece en el texto de los
  .docx 6.1–6.6: el 6.7 no introduce ninguna cifra nueva (regla del cierre de capítulo).

## Decisiones de redacción

- Tres afirmaciones (equivalencia, menos paradas, aportación de cada pieza) y cuatro negaciones (no la mejor QoE,
  no mejora al MPC, no generaliza a TCP/otros contenidos/otras duraciones/perceptual, nada confirmatorio sobre el
  contenido nuevo): tomadas de 07_RESULTADO §6, redactadas sin «gana».
- Limitaciones en lista con entradilla en negrita (biblia §6.5 lo permite para limitaciones). Las 4 del protocolo
  (emulación, Oboe/FCC, un contenido nuevo, bitrate sin VMAF) + 4 identificadas al redactar: diseño elegido en
  validación (α, arquitectura, ensanchado), una sola referencia canónica con parámetros por defecto, una repetición y
  sesiones cortas (30 segmentos ≈ 2 min), métricas secundarias (QoE log por sesión, retardo de arranque no medido).
  «Las demás se han identificado al analizar y al redactar, y se declaran con el mismo peso»: honestidad explícita.
- «Ninguna de estas limitaciones afecta a la validez interna…; todas afectan a su alcance»: frase de defensa.
- 6.7.3: desviaciones del protocolo = ninguna (07_RESULTADO §7), con la lista de lo que se cumplió.
- Cierre: dos párrafos (recapitulación 6.1–6.3 y 6.4–6.7) que enlazan con el capítulo 7 (objetivos, resultados
  negativos de las líneas descartadas, trabajo futuro).

## Lo que NO se dice

- Nada del indicador `benchmark_autorizado`.
- No se citan cifras de desarrollo ni se compara con otras ejecuciones.
- No se promete trabajo futuro concreto (va en 7.4); solo se dice que parte de las limitaciones.

## Preguntas probables del tribunal

1. **¿Entonces el controlador es mejor o no?** Iguala en QoE a la referencia canónica y para cuatro veces menos; no
   tiene la QoE más alta. Es exactamente lo que se planteó demostrar, con hipótesis fijadas antes.
2. **¿Por qué no probar con red real?** Reproducibilidad: 1208 sesiones idénticas en red y contenido para los 8
   controladores; una red real no se repite. Es la limitación n.º 1 y el primer trabajo futuro.
3. **¿No es circular elegir α en validación y evaluar en eval?** No: son particiones sin grupos de captura en común;
   la de evaluación no se tocó hasta el experimento. Lo que sí es cierto es que el controlador evaluado es el
   resultado de esas elecciones: por eso se declara.
4. **¿Un MPC mejor ajustado ganaría?** Posiblemente en QoE; es la limitación «una sola referencia canónica». La
   comparativa aísla la predicción con el mismo planificador, que es lo que se quería medir.

## Qué se puede recortar

6.7.3 a dos frases (ya está dicho en 6.3) y el primer párrafo del cierre. Mantener 6.7.1 y la lista de limitaciones.
