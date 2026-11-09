# Notas de 2.3 y 2.4 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap2_3_4_problema_familias.docx` (≈2190 palabras de cuerpo, 6 páginas:
2.3 el problema de la adaptación de tasa (3 párrafos) y 2.4 familias con siete subapartados 2.4.1–2.4.7, Tabla 2.1
y párrafo de síntesis; 15 citas, sin figuras). Generado por `docs/memoria/apoyo/generar_cap2_3_4.py` (comprueba
que todas las claves existen en el .bib). Comprobador sin avisos.

## Citas verificadas (página del PDF en `biblioteca_final/`)

| Clave | Afirmación | Dónde |
|---|---|---|
| `yin2015mpc` | cuatro objetivos en conflicto (calidad, rebuffering, arranque, suavidad) | p. 1 (resumen) y p. 3 («these objectives are conflicting») |
| ídem | horizonte deslizante («moving look-ahead horizon»); errores de predicción degradan; variante robusta | p. 2, 9, 13 (horizonte); p. 5–7 (prediction error) |
| `bentaleb2019survey` | cliente / servidor / red (p. 3); cinco clases de cliente: ancho de banda, buffer, propietarias, mixtas, MDP | p. 3 y p. 7 (§III-A) |
| `liu2011rateAdaptation` | tiempo de descarga del segmento frente a su duración; subida escalonada y bajada agresiva | p. 1–2 |
| `huang2014bba` | reservorio y colchón; función buffer → nivel | p. 4–6 |
| `spiteri2020bola` | utilidad, optimización de Lyapunov, cota O(1/V) frente al óptimo | p. 1–2 |
| `akhtar2018oboe` | ajuste automático de parámetros según el estado de la red (media y desviación del throughput); mejora BOLA y MPC | p. 1–2, 6 |
| `mao2017pensieve` | A3C; entradas; simulador con trazas; «generalizes well» | p. 1 (generaliza), p. 2 y 5–6 (A3C) |
| `huang2020comyco` | imitación de trayectorias de un experto; recompensa consciente de la calidad | p. 1 |
| `patel2024gelato` | despliegue en Puffer, más de 280 000 usuarios | p. 1 («over 280,000 users on the live streaming platform Puffer») |
| `kan2022merina` | meta-RL para adaptarse rápido a redes no vistas | p. 1–3 |
| `huang2022a2br` | meta-RL con etapa fuera de línea (política inicial) y en línea (ajuste al usuario); «unseen environments» | p. 1 (resumen). OJO: NO es adversario; la primera redacción lo decía y se corrigió |
| `yan2020puffer` | plataforma real; los algoritmos buenos en simulador no lo son en la red real; Fugu = predictor supervisado del tiempo de transmisión, probabilístico, con MPC; entrenamiento in situ | p. 1–3, 7–8 |
| `kan2021bayesmpc` | BNN que separa incertidumbres, región de confianza, decisión por el peor caso dentro de la región | p. 1–3 (ya verificadas para el 5.6) |
| `chen2024soda` | optimización convexa en línea suavizada; calidad consistente; sin redes neuronales | p. 1 |
| `xie2026safesabr` | Starlink; compromiso QoE–riesgo grave; calibración del riesgo; PREPRINT arXiv 2026 | p. 1 |

## Decisiones de redacción

- 2.3 sin ecuación: el problema se formula en prosa (objetivos, información disponible, horizonte, tamaño real);
  la QoE formal va en 2.5 y en 6.2. Dos rasgos destacados (horizonte y tamaño real) enlazan con la aportación.
- 2.4 organizado por señal (biblia: «tabla comparativa de familias»), siete subapartados cortos, un representante
  por familia + ampliación donde el .bib lo permite (Comyco, Gelato; MERINA, A2BR; Fugu, BayesMPC, SODA, SafeSABR).
  Cada párrafo termina diciendo qué aporta, qué limita y, cuando toca, qué relación tiene con este trabajo (patrón
  del tutor 2024: «en qué se diferencia de este»).
- Tabla 2.1 con seis columnas (familia, idea, señal, aporta, limita, ejemplo); última fila incluye «este trabajo».
- NO se citan: luo2025sabr, mao2020abrl, patel2023plume, huang2023deepbuffer, bentaleb2024ahaggar, yin2024ant,
  zhang2025beta, yi2025fortuna, huang2026eastream, wang2026nmoeabr, yi2025airl, hussein2026mambra (reserva). Si
  se quiere más amplitud en 2.4.6, añadir una frase con `yin2024ant` (dinámica de red) y `wang2026nmoeabr`
  (mixture-of-experts) tras verificar página.
- Pensieve: «fijó la escalera, los pesos de la QoE y el filtro de trazas que este trabajo reutiliza» (coherente con
  5.5, 6.1 y 6.2); se cita como contexto, no como implementación (regla del repo).
- Puffer/Fugu: «paradigma que este trabajo adopta» — consistente con el 5.6 (`yan2020puffer` p. 2–3).

## Preguntas probables del tribunal

1. **¿Por qué no comparar con Pensieve o un RL?** El comparador fuerte prerregistrado es el MPC robusto canónico,
   que la propia literatura RL usa como referencia; un RL entrenado por nosotros sería «nuestro RL», no el de la
   literatura, y su resultado dependería del entrenamiento. Limitación «una sola referencia canónica» (6.7).
2. **¿Qué diferencia tu controlador de Fugu?** Fugu predice tiempos de transmisión con una red entrenada in situ en
   un despliegue real; aquí se predicen cuantiles del throughput con un ensemble entrenado en un simulador fiel
   al medio y se agrega el riesgo con CVaR en el planificador.
3. **¿Y del MPC bayesiano?** Región de confianza + peor caso frente a cuantiles + promedio de los escenarios
   desfavorables (prudencia graduable con α).
4. **¿Por qué no una política aprendida de extremo a extremo?** Opacidad, coste y salto simulador-realidad
   (Pensieve, Puffer, Hoffman): el aprendizaje se pone en la predicción, que se puede calibrar y auditar.

## Qué se puede recortar

2.4.4 (Oboe) a tres frases y 2.4.6 a un párrafo corto. Mantener 2.3, 2.4.3, 2.4.7 y la Tabla 2.1.
