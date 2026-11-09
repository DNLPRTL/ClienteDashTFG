# Notas del resumen y el abstract (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/resumen_abstract.docx` (dos páginas: resumen en castellano y abstract en
inglés; cada una con título, autor, palabras clave y cuatro párrafos; biblia §3: 300–400 palabras y 6–8 palabras
clave, siglas definidas también aquí). Generado por `docs/memoria/apoyo/generar_resumen.py`. Comprobador sin avisos.

## Qué comprueba el script (regla cero)

- El título se lee del plan maestro §1 (opción A, «confirmar con tutor»); el abstract lleva su traducción.
- Del protocolo del experimento final: 5 hipótesis, margen 0,15, Holm, 8 controladores, 1208 sesiones, 5 perfiles de
  vídeo.
- Cada cifra del resumen ya está en los .docx del capítulo 6: −0,001, ±0,15, 0,041, 0,162, 1208, 74 ventanas,
  35 032. Cualquier otro decimal o entero largo hace fallar el script (en el abstract, con punto decimal y «35,032»).
- Siglas definidas en el propio resumen: DASH, ABR, MPC, CVaR, QoE (se comprueba sigla y expansión).
- Recuento por palabras separadas por espacio: resumen 300–400, abstract ≤ 420 (el inglés es algo más largo).
- Ningún nombre interno (SPBC, Q_H, v1/v2, Phase, etc.).

## Decisiones de redacción

- Cuatro párrafos como pide la biblia: encuadre (DASH, ABR, incertidumbre, VBR, simuladores sin fidelidad), qué se
  construyó (cliente, clásicos, controlador propio, entrenamiento fiel), qué se evaluó y qué salió (experimento único,
  cinco hipótesis aceptadas, equivalencia con cuatro veces menos paradas, variantes; «no tiene la QoE media más alta»),
  aportaciones y límites.
- Palabras clave (8): streaming adaptativo, MPEG-DASH, adaptación de tasa (ABR), calidad de experiencia (QoE),
  control predictivo (MPC), predicción de cuantiles, riesgo (CVaR), reproducibilidad. Sustituyen a las 9 del plan
  (se quitan «incertidumbre», «aprendizaje automático» y «predicción de throughput» para quedar en 8 y nombrar lo
  específico: cuantiles y CVaR).
- Título de la página como párrafo en negrita a 16 pt, no como «Capítulo»: con el estilo de capítulo (26 pt) el
  resumen pasaba a dos páginas. En la maqueta final se usa el estilo que marque la plantilla de la ETSIIT.
- Autor: «Daniel Pretel» tal como figura en el plan maestro. **Daniel debe poner su nombre completo** (segundo
  apellido) antes de maquetar.
- El comprobador se ha ajustado para excluir el abstract de la regla de la coma decimal (el inglés lleva punto):
  detecta la página por «Keywords:» y corta en «Abstract».
- La primera versión salía a 477 palabras; se recortó a 389 sin quitar ninguna de las cuatro partes.

## Pendiente de Daniel

- Confirmar el título con el tutor (plan maestro §1) y, si cambia, editar el plan: el script lo lee de ahí.
- Nombre completo del autor.
