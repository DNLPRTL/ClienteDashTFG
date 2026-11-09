# Notas del 6.4 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_4_resultados_hipotesis.docx` (≈970 palabras de cuerpo, 3 páginas,
Tabla 6.7, Figura 6.2, sin ecuaciones, sin citas). Generado por `docs/memoria/apoyo/generar_cap6_4.py`, que
también dibuja la figura (`figuras/fig_6_2_diferencias_por_ventana.svg/png`, matplotlib 3.10 en py -3.12).
Comprobador sin avisos; render con Word revisado.

## Qué hace el script (todo por programa)

- Lee `contrastes_prerregistrados.json` (lo escrito por la VM) y lo coteja campo a campo con
  `apoyo/contrastes_reproducidos.json` (análisis repetido en Windows, 6.3): medias, p, p Holm, recuentos.
- Recalcula Holm con `contrastes.holm` sobre los cinco p: coincide.
- Recalcula las diferencias por ventana con `contrastes.diferencias_por_ventana` del entregable sobre
  `sesiones.csv`: 74 ventanas, 148 escenarios, medias y recuentos +/−/= iguales a los del JSON.
- P1: TOST a mano sobre las 74 medias por ventana: z mínimo 13,9 → p ≈ 0 (el JSON guarda 0,0; se escribe «< 10⁻¹⁰»).
  Margen mínimo en que cabría el IC90: 0,02 (≈ 0,13 s de rebuffering = 0,02·29/4,3).
- P2: `_cola_binomial(13, 1) = 0,0017` = p del JSON.
- Medias absolutas por controlador (148 sesiones reales): paradas propio 0,041 / MPC 0,162 / recientes 0,480 /
  mediana 0,831 / fijos 0,027; QoE propio 2,547 / MPC 2,548 / fijos 2,398; sesiones con alguna parada: propio 6,
  MPC 22, recientes 49, mediana 69, fijos 4.
- Ejemplo (ventana 1, la de la sesión 8): Paseo 30 fps propio 3,974 / MPC 4,024; Tears propio 4,024 / MPC 4,024;
  media −0,025; 0 paradas en los cuatro → uno de los 61 empates de P2.

## Fuente de cada número

| Dato | Fuente |
|---|---|
| Tabla 6.7 entera | `contrastes_prerregistrados.json → principales` (= reproducido) |
| mayor diferencia por ventana a favor del MPC 0,208 y del propio 0,258 | medias por ventana recalculadas |
| «4 veces menos» (0,041 frente a 0,162), «12 veces» (0,480), «20 veces» (0,831) | medias de `sesiones.csv`; cocientes 3,95 / 11,7 / 20,3 redondeados en el texto («cerca de cuatro», «unas 12», «unas 20») |
| 6 / 22 sesiones con parada | `sesiones.csv` |
| Figura 6.2 | medias por ventana + IC del JSON |

## Decisiones de redacción

- Cada hipótesis: cifra con intervalo, recuento de ventanas, valor absoluto de los dos controladores, qué significa y
  qué no. P1 se dice explícitamente que NO es superioridad.
- P2 se califica de «el más frágil de los cinco en términos de recuento» (13 ventanas deciden). Honestidad; el IC95
  excluye el cero y Holm lo mantiene (0,0017).
- No se adelantan ni la tabla completa de los 8 controladores ni la descomposición por componentes (6.5), ni los
  estratos (6.6), ni «el propio no tiene la QoE más alta» (6.5/6.7).
- Figura rehecha con matplotlib, no la PNG del paquete (no hay una equivalente en `03_graficas`): puntos por ventana
  ordenados, margen en amarillo, media e IC en azul, ventanas en contra en rojo. Comprobada a ojo en el PNG; sin
  getBBox porque es matplotlib (los textos se colocan en zonas sin datos).

## Preguntas probables del tribunal

1. **¿Equivalencia con un margen tan ancho como 0,15?** El IC90 observado es [−0,018; +0,017]: cabría en ±0,02, que es
   0,13 s de rebuffering por sesión. El margen prerregistrado era conservador y sobró.
2. **¿Un solo punto en contra en P2 (ventana roja)?** Una ventana donde el propio paró y el MPC no (+0,5 = una parada
   en uno de los dos vídeos). El resultado no depende de ella: 12 frente a 1.
3. **¿61 empates no es poca información?** La prueba del signo solo usa las 13 que difieren y aun así p = 0,0017; los
   empates son el resultado en sí: en la mayoría de las ventanas ninguno de los dos para.
4. **¿Por qué P4 en QoE y no en paradas?** La variante fija ya es prudente (0,027 paradas): la pregunta útil es si la
   red recupera calidad sin perder seguridad; la seguridad se mira en 6.5 (diferencia de paradas no significativa).
5. **¿Y frente a los clásicos?** Descriptivo, en 6.5 (BBA +0,315, basado en tasa +0,796, BOLA +1,353 de QoE).

## Qué se puede recortar

El párrafo final del ejemplo de la ventana 1 (dejar solo la frase de Holm). Mantener la Tabla 6.7, la Figura 6.2
y los cinco párrafos.
