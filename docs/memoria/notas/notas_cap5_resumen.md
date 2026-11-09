# Notas del resumen del capítulo 5 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap5_8_resumen_capitulo5.docx` (425 palabras, 3 párrafos, 1 página,
sin título, sin tablas, sin figuras, sin citas). Generado por `docs/memoria/apoyo/generar_cap5_resumen.py`.
Comprobador sin avisos; render con Word revisado.

## Forma elegida y por qué

- La biblia (§6.3) pide que cada capítulo «cierre con un resumen de dos o tres frases que enlaza con el
  siguiente». En el corpus, ningún TFG lleva un epígrafe «Resumen» por capítulo: el tutor (2017) cierra los
  capítulos 2, 5, 6 y 7 con párrafos de transición sin título; los de 2024 y 2025 no cierran. Por tanto el
  resumen va como **cierre del 5.7, sin epígrafe numerado ni rótulo**, pegado tras su último párrafo.
- Para no duplicar, se han quitado del último párrafo del 5.7 las dos frases de cierre que hacían ese papel
  («Con esto se cierra la implementación… El capítulo 6 presenta…»). `generar_cap5_7.py` y el `.docx` del 5.7
  se han regenerado (1702 palabras; antes 1735). Nada más cambia en el 5.7.
- Tres párrafos en vez de «dos o tres frases»: el capítulo tiene siete apartados y la biblia §6.4 limita los
  párrafos a 120 palabras; con tres párrafos cada apartado recibe una frase y el enlace con el 6 cabe entero.
  Si Daniel quiere la versión mínima, el tercer párrafo solo vale como cierre.

## Qué se recapitula de cada apartado y qué se deja fuera

| Apartado | Se recapitula | Se deja fuera (ya dicho allí) |
|---|---|---|
| 5.1 | Python compatible desde 3.8; tres dependencias externas; PyTorch aparte | versiones exactas, política de dependencias, PyYAML opcional |
| 5.2 | sesión desde configuración, dos hilos, descargador envuelto por la emulación, telemetría | manifiesto de ejecución, políticas de fin, formato de la traza |
| 5.3 | cinco MPD, plantillas de URL, sidx, salida (escalera y segmentos) | timescale/duration, redondeo a 150 segmentos, límites |
| 5.4 | preset y configuración → protocolo y plan deterministas, ejecución en serie, paquete de evidencia | embudo 873→831→707→74, semilla 606, reanudación, interfaz gráfica |
| 5.5 | cuatro clásicos; MPC robusto canónico (horizonte 5, QoE lineal, tamaños reales); planificador compartido | parámetros de cada clásico, 7776 secuencias, decisión real (F5.3) |
| 5.6 | 5 GRU, 4 cuantiles × 5 horizontes, ensanchado, 3 peores con α = 0,75, respaldo MPC robusto, 3 variantes | entradas (T5.10), ecuaciones, decisión real (F5.5), Tabla 5.12 |
| 5.7 | simulador con la física del cliente, ventanas de entrenamiento y validación, calibración antes de exportar | 4096/935 ventanas, 490 500 muestras, pinball, cobertura 0,070… |
| Enlace al 6 | 74 ventanas eval × (visto + nuevo) × 8 controladores = 1208 sesiones, VM cliente, protocolo previo, P1–P5 sobre QoE lineal y paradas, integridad, todo se informa | cifras de resultados (ninguna) |

## Verificación por programa

`generar_cap5_resumen.py` comprueba que cada cifra o hecho del resumen ya aparece en el texto del apartado
correspondiente: lee los `.docx` de 5.3–5.7 y los `.md` de Daniel (5.1 y 5.2, sin tocarlos) y falla si falta
alguno («3.8» y «tres paquetes externos» en 5.1; «dos hilos» en 5.2; «cinco manifiestos» y «sidx» en 5.3;
«1208», «74», «8» y «uno visto» en 5.4; «horizonte» en 5.5; «α = 0,75», «cuatro cuantiles», «respaldo»,
«ablación», «tres variantes», «5 GRU», «cinco segmentos» en 5.6; «calibración» y «simulador» en 5.7).

## Avisos

- El comprobador del 5.7 avisa de «Tabla 5.10 sin pie en este borrador»: es la referencia cruzada al 5.6,
  correcta; no es un error.
- «Cinco hipótesis prerregistradas» y «protocolo fijado antes de ejecutar» se enuncian aquí como anuncio del
  capítulo 6; la Tabla 5.11 del 5.6 ya nombra P1–P5 y el 5.4.4 el protocolo.

## Qué se puede recortar

El primer párrafo entero si el tribunal ve redundante repasar 5.1–5.4 (son los apartados menos propios);
quedarían dos párrafos: controladores y entrenamiento, y enlace con el 6.
