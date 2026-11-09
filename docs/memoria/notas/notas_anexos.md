# Notas de los anexos (no van a la memoria) — 10/11/2026

Entregable: `docs/memoria/borradores_docx/anexos.docx` (23 páginas, 3036 palabras de cuerpo, 12 tablas, 6 listados,
1 cita en el texto más 4 de herramientas; comprobador sin avisos). Generado por `docs/memoria/apoyo/generar_anexos.py`
(ejecutar con `py -3.12`, porque importa el registro de controladores del entregable y ese arrastra torch).

Estructura (la anunciada en el 1.6 del cap 1, comprobada por el script):

- **Anexo A. Reproducción del experimento a partir del material entregado.** A.1 material (Tabla A.1 inventario por
  bloque con ficheros y tamaño), A.2 preparación del cliente (Listado A.1), A.3 servidor, A.4 comprobaciones previas y
  plan en seco (Listado A.2), A.5 ejecución (Tabla A.2 qué coincide y qué no), A.6 análisis, verificación e integridad
  (Listado A.3 con la huella de la lista `e5dc724b…3126`).
- **Anexo B. Manual de uso del cliente.** B.1 instalación, B.2 una sesión (Listado B.1 comando; Tabla B.1 claves de la
  configuración leídas de las clases de datos; Listado B.2 configuración real de la sesión 8 copiada del paquete),
  B.3 controladores (Tabla B.2 leída del registro, con la firma del constructor), B.4 salidas, B.5 evaluación
  comparativa (Tabla B.3 claves leídas de `CONFIG_EVALUACION_POR_DEFECTO`; Tabla B.4 opciones de línea de comandos
  leídas del `argparse` del ejecutor), B.6 GStreamer, B.7 contenido y entrenamiento (Tabla B.5 scripts; Listado B.3).
- **Anexo C. Documentación complementaria.** C.1 corpus por conjunto (Tabla C.1 = la T7 del plan, contada sobre el
  catálogo), C.2 contenido DASH (Tabla C.2 desde los 9 descriptores de tamaños), C.3 ficheros del paquete (Tabla C.3),
  C.4 columnas de `segmentos.csv` (Tabla C.4, 36 columnas), C.5 columnas principales de `sesiones.csv` (Tabla C.5).

## Qué comprueba el script (regla cero)

- Inventario: tamaño y número de ficheros de los 7 bloques por `os.walk` (el código son 103 ficheros SIN `.idea`,
  que sigue dentro de TFG Material y se excluye del recuento); 86 módulos de Python; 18 funciones de prueba; los 14
  scripts de `scripts/` existen y son todos los que hay; `main.py` admite `simulado` y `gst`.
- Las claves de la Tabla B.1 son EXACTAMENTE los campos de `ConfigCliente` y sus clases anidadas (si cambia una clave
  el script falla); las de la Tabla B.3, EXACTAMENTE las de `CONFIG_EVALUACION_POR_DEFECTO`; las opciones de la Tabla
  B.4, EXACTAMENTE las `add_argument` del ejecutor; los controladores de la Tabla B.2, los 9 del registro con los
  parámetros de `inspect.signature` (el MPC robusto hereda los del MPC básico vía `**parametros`).
- Preset `final_blindaje`: todas las ventanas de `eval`, 3 sintéticas, 160 s, 30 segmentos, 900 s, filtro Pensieve,
  `loop` con 1 vuelta. Configuración local: 8 controladores, semilla 606, 42 grupos excluidos, `verificar_hashes`.
- Paquete: 1208 configs, 1208 logs, 1208 carpetas de sesión cada una con exactamente los 6 artefactos; 35 032 filas
  en `segmentos.csv` y 1208 en `sesiones.csv`; 77 ventanas (3 sintéticas); 16 PNG + manifiesto; verificación «OK»;
  9699 ficheros = 9699 líneas de huellas; la huella de la lista del LEEME coincide con la citada en el 6.3; la
  auditoría suma 35 032 decisiones con 0 distintas y 0 respaldos; el simulador reproduce los niveles en 1184/1184.
- La sesión de ejemplo (s00008) es la primera del plan con el controlador propio, y su configuración tiene los
  valores que el texto describe (ventana 296 s + 160 s, `loop` 1, simulado 0,1 s, 30 segmentos, 60 s, respaldo MPC
  robusto, huellas activadas).
- Corpus: 6768 trazas, 12 conjuntos, particiones por grupo de captura, 213 excluidas por calidad + 11 duplicadas de
  6981; 6992 CSV con esquema `tiempo_s,duracion_s,throughput_kbps`. Modelos: 5 ficheros en el manifiesto, 5 GRU,
  alfa 0,75; cuantiles fijos con horizonte 5 y 4 cuantiles. Contenido: 9 descriptores, escalera 300–4300, carpeta y
  MPD de 4 s de cada vídeo presentes en `05_contenido_dash`.
- Remisiones: «Tabla 6.3» existe en el 6.1, «Tabla 5.5» en el 5.4, la frase del 1.6 sobre los anexos está en el cap 1.
- Sin nombres internos (lista PROHIBIDOS, por programa); citas del texto en el `.bib`.

## Decisiones de redacción

- Tres anexos con letra («Anexo A» en el estilo «Capitulo numero» + título en Heading 1; apartados «A.1.»), como
  los apéndices de la plantilla UGR y el TFG del tutor de 2025 (anexo de manual de usuario). El comprobador acepta
  ahora numeración por letra en títulos y pies, excluye los párrafos de estilo «Codigo» de la regla de la coma
  decimal (reproducen ficheros y comandos tal cual) y no toma la IP del servidor por un decimal.
- El manual NO repite el diseño (caps 4 y 5): solo cómo usar. Las tablas de claves se generan del código para que no
  puedan desincronizarse. Listado B.2 es un volcado íntegro de una configuración real del paquete (48 líneas; la
  biblia limita a 10 líneas en el cuerpo, no en los anexos, y el corpus del tutor vuelca ficheros enteros en los
  apéndices); es el único volcado largo.
- Los nombres de preset no se listan (uno de ellos es un nombre interno prohibido); solo se nombra `final_blindaje`,
  que es imprescindible para el comando de reproducción y aparece en el protocolo del paquete.
- En A.6 el texto es CONDICIONAL: si los programas de auditoría (`auditar_decisiones.py`, `validar_simulador.py`,
  que necesitan `simulador.py` del mismo directorio) se copian a
  `TFG Material\04_evidencia_final\verificacion_windows_20261016\`, el script los detecta y el párrafo dice que van
  junto a los informes; si no, dice solo que los informes se generaron con programas que leen la telemetría y crean
  los controladores con el código entregado. Hoy NO están en TFG Material: solo en `docs/blindaje/simulador/` del
  repo, que la memoria no cita.
- Cifras: ninguna de resultados (se remite a 6.3 y 6.4). Las únicas cifras son conteos y tamaños del material y
  cuatro de contexto ya publicadas en el cuerpo (41,3 h, 144 s por sesión, 74 ventanas, 4,3 de la QoE).
- Tabla C.2 muestra que Tears of Steel tiene cociente mayor/menor de 61,7 en el nivel alto y Paseo 30 fps 14,6
  (coherente con el «> 14» del 1.2); Paseo 60 fps y los de 1 min son casi CBR.

## Pendiente de Daniel

- Decidir si copia `auditar_decisiones.py`, `validar_simulador.py` y `simulador.py` del repo a la carpeta de
  verificación de TFG Material (entonces regenerar: `py -3.12 docs/memoria/apoyo/generar_anexos.py`).
- `.idea\` sigue en el código de TFG Material (5 ficheros); el anexo cuenta 103 ficheros sin ella.
- `config/client.example.yaml` y `config/evaluacion.example.json`, que el código nombra como ficheros de valores por
  defecto, no existen en el entregable (el código los trata como opcionales; `--escribir-config-ejemplo` crea el
  segundo). No afecta al texto, que describe los valores por defecto de las clases de datos.
