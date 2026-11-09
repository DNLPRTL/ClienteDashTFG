# Notas del 5.4 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap5_4_ejecutor_configuracion.docx` (1634 palabras de cuerpo,
5 páginas, 5 subapartados, Figura 5.2, Tablas 5.5 y 5.6, ecuaciones 5.2 y 5.3, 1 cita). Generado por
`docs/memoria/apoyo/generar_cap5_4.py`. Comprobador sin avisos; render con Word a PDF revisado.

## Reproducción que hace el script (regla del ejemplo real)

- Carga la configuración real del entregable (`config/evaluacion.local.json`), redirige el catálogo
  y las rutas de las trazas a `TFG Material\02_corpus_red` (con la regla `reescrituras_rutas_trazas`
  del propio código) y llama a `seleccionar_ventanas_trazas` del entregable con el preset
  `final_blindaje`. Las 77 ventanas (id de traza e inicio) coinciden exactamente con
  `00_protocolo/ventanas_trazas.csv` del paquete final; si no coincidieran, el script falla.
- El embudo de la Tabla 5.6 (873 → 831 → 707 → 74) se calcula con los mismos filtros del código.
  Precisión: la fila 2 aplica a la vez «duración ≥ 160 s» y «apta para evaluación»
  (`usable_en_eval`); el código los aplica juntos.
- Comprueba contra el paquete: 1208 sesiones; preset efectivo (160 s, 30 segmentos, 900 s);
  configuración de la sesión 1 (paso 0,01 s, preroll 0, cola 0,1 s, bucle con 1 vuelta, nivel 0 sin
  decisión inicial); 8 controladores; órdenes distintos en las dos primeras ventanas; 592 sesiones de
  Tears of Steel (74 × 8).

## Fuente de cada número

| Dato | Fuente |
|---|---|
| 873, 831, 707, 74 (Tabla 5.6) | reproducción con `seleccion.py` sobre `catalogo_trazas.json` y las trazas de `02_corpus_red` |
| Oboe 56, FCC 18 | `ventanas_trazas.csv` del paquete y reproducción |
| ventana 1: traza FCC de 1651,6 s, 373 inicios posibles, desplazamiento 74, inicio 296 s, media 5,04 Mbit/s, mínimo 4,38 Mbit/s | `catalogo_trazas.json` (duración), ecuación (5.2) aplicada en el script, `ventanas_trazas.csv` |
| Tabla 5.5 entera | `protocolo_validacion.json` (preset_efectivo, controladores, grupos excluidos), `catalogo.py` (preset `final_blindaje`), `configs_cliente/s00001_*.yaml`, `config/evaluacion.local.json` |
| 42 grupos excluidos (39 reales y 3 sintéticos) | `config/evaluacion.local.json` |
| id de la sesión 1 y orden sorteado | `plan_sesiones.json` |
| 1208 = (74·2 + 3)·8 | `plan_sesiones.json`; ecuación (5.3) |
| «77 ventanas esperadas», comprobaciones previas al lanzamiento | `docs/blindaje/kit_vm/blindaje_vm.sh` (comprobar: huellas, pruebas, plan en seco) y `06_PROTOCOLO_FINAL.md` |
| 8 compuertas, 15 comprobaciones (figura) | `analisis.evaluar_gates`, `verificacion.py`, `verificacion_paquete.json` |

## Cita verificada

- `mao2017pensieve`, p. 7 del PDF (sección 5.1, «Trace datasets»): «we only considered original
  traces whose average throughput is less than 6 Mbps, and whose minimum throughput is above 0.2 Mbps».
  Aquí el criterio se aplica a la ventana de 160 s, no a la traza entera (dicho en el texto).

## Preguntas probables del tribunal

1. **¿Por qué SHA-256 y no `random.seed`?** Para que cada traza tenga un inicio fijo que no dependa
   del orden en que se recorre el catálogo ni del tamaño del preset; cambiar el preset no cambia el
   inicio de una ventana ya elegida. El orden de controladores sí usa `random.Random` con una cadena
   semilla derivada (`"606|ventana|vídeo|repetición"`), también determinista.
2. **¿La selección «balanceada por origen» del código?** Existe (`_seleccion_balanceada` reparte por
   dataset, semántica, condición y tramo), pero con `ventanas_reales = "todas"` toma todas las
   candidatas relevantes, así que el balanceo no recorta nada. Por eso el texto no habla de balanceo.
3. **¿Por qué 160 s y no 300 s?** Una sesión de 30 segmentos consume ≤ 145 s de traza; 300 s exigía
   trazas largas y dejaba pocas candidatas en eval sin los grupos de desarrollo. Con 160 s y el
   filtro, 74 ventanas. El bucle de una vuelta es salvaguarda (06_PROTOCOLO).
4. **¿Qué pasa si la VM se apaga?** `--reanudar` sobre el mismo paquete: se omiten las sesiones con
   manifiesto `completado` y se repiten las demás. En el final no hizo falta (0 reanudaciones).
5. **¿La GUI se usó en el final?** No: `nohup` por script (`blindaje_vm.sh final`), para sobrevivir al
   cierre de la terminal. La GUI existe y funciona; se dice así.
6. **¿Por qué en serie si el ejecutor admite paralelo?** Para que ninguna sesión comparta CPU ni
   temporización con otra; la opción `--paralelo` se añadió en el blindaje y no se usó.

## Detalles que el texto no cuenta

- El tiempo límite de 900 s por sesión no saltó en ninguna de las 1208 (duración media 123 s).
- Los ficheros de configuración por sesión se escriben con extensión `.yaml` y contenido JSON; el
  cargador lo detecta por la llave inicial. Funciona; no se toca.
- `configuracion_cliente.py` aún nombra `config/client.example.yaml` y `client.local.yaml` como
  rutas por defecto del cliente suelto; no existen y se saltan. Resto de la poda.
- Claves con nombre en inglés en la configuración de la evaluación (`decision_interval_s`,
  `min_media_throughput_kbps_for_formal`, `min_max_throughput_kbps_for_formal`): con el filtro de
  Pensieve el suelo de throughput de la traza entera no se usa.
- El protocolo marca `apto_benchmark = true` pero `benchmark_autorizado` queda en falso en el
  resumen (lista de presets antigua en `evaluar_gates`; ver aviso 1 de la revisión del cap 4). El
  5.4 no menciona ese indicador.
- `preset_efectivo.duracion_estimada_total_s` = 173 952 s (48,3 h) frente a las 41,3 h reales.

## Qué se puede recortar

El párrafo de la interfaz gráfica (a dos frases) y la enumeración de secciones de la configuración
de la evaluación. Mantener la Tabla 5.6 y el ejemplo de la ventana 1 (son la prueba de que la
selección es reproducible).

## Cambios de tooling en este turno

- `memoria_docx.py`: subíndices con `V~r~`; las filas de tabla llevan `keep_with_next` y
  `cantSplit` para que la cabecera no quede sola al pie de página.
- `svg_a_png.py` ahora pasa por Word (COM): importa el SVG con Arial y exporta un PDF del tamaño
  exacto de la figura, que PyMuPDF rasteriza. PyMuPDF solo no aplica el `<style>` CSS ni las
  fuentes; por eso la figura 5.2 lleva todos los estilos inline (también más cómodo para Boxy SVG).
- `.claude/launch.json`: servidor local de `docs/memoria/figuras` para comprobar solapes de los SVG
  con `getBBox` en el navegador (F5.2: 35 textos, 0 solapes, 0 cruces de borde).
