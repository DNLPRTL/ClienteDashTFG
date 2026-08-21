# Borrador 4.3 — Diseño de la descarga y la gestión del buffer

> BORRADOR para masticar y reescribir (12/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/descargador.py` (leído entero) + `reproductor.py`
> (constantes y bucle) + `core/configuracion_cliente.py` del entregable.

---

### 4.3. Descarga de segmentos y gestión del buffer

Entre el analizador del manifiesto y el motor de reproducción se sitúan las dos
piezas que mueven los datos: el descargador, que trae cada segmento del
servidor, y el buffer de reproducción, que amortigua la diferencia entre el
ritmo de descarga y el ritmo de consumo. Su diseño condiciona directamente la
calidad de las mediciones, así que las decisiones de este apartado tienen una
motivación tanto funcional como experimental.

**Descargador.** El descargador realiza las peticiones HTTP de segmentos sobre
una conexión persistente, reutilizada durante toda la sesión
\cite{rfc9110, rfc9112}. Cada petición se configura con tres cabeceras
deliberadas, pensadas para que la medición sea fiel:

- `Accept-Encoding: identity`: se rechaza la compresión al vuelo, de modo que
  los bytes recibidos coinciden exactamente con el tamaño real del segmento.
- `Cache-Control: no-cache` y `Pragma: no-cache`: se pide contenido fresco
  para evitar que una caché intermedia falsee los tiempos de descarga.
- `Connection: keep-alive`: la conexión se reutiliza entre segmentos, de forma
  que las medidas de tiempo no queden contaminadas por el coste de establecer
  una conexión nueva en cada petición.

El descargador admite también peticiones de rango de bytes (cabecera `Range`),
necesarias para el esquema de direccionamiento por fichero único descrito en
el apartado 4.2, y aplica un tiempo máximo por petición de 10 segundos. De
cada descarga devuelve, junto a los datos, un informe con el tamaño recibido,
el código de estado y el tiempo total empleado. De ese par tamaño-tiempo sale
la medida de throughput observado que alimenta la realimentación del
controlador (apartado 4.5).

**Robustez en dos niveles.** Los errores de descarga se tratan en dos capas
con responsabilidades distintas. La primera es la del propio descargador: ante
un fallo de transporte (error de conexión, código de error del servidor,
tiempo agotado) reintenta la misma petición hasta un máximo configurable, con
una espera breve entre intentos. La segunda es la del bucle de sesión: si la
descarga de un segmento sigue fallando, el reproductor espera con retroceso
exponencial (0,5 s duplicándose hasta un tope de 10 s) y, agotados seis
intentos, degrada la petición al nivel de calidad inferior y vuelve a
intentarlo; solo si el fallo persiste en el nivel más bajo se abandona el
segmento y se continúa con el siguiente. Esta separación mantiene la política
de recuperación (qué hacer cuando la red va mal) fuera del código de
transporte (cómo pedir bytes).

El descargador es, además, el punto de inserción de la emulación de red:
cuando la sesión se ejecuta bajo condiciones controladas, un envoltorio lo
sustituye de forma transparente y limita el caudal efectivo según una traza de
ancho de banda real. El resto del cliente no distingue una sesión real de una
emulada. El diseño de esa emulación se desarrolla en el apartado 4.7.

**Gestión del buffer.** El buffer de reproducción se modela por tiempo de
vídeo almacenado, no por bytes: lo que importa para decidir y para detectar
paradas es cuántos segundos de contenido quedan por reproducir. El esquema es
el clásico productor-consumidor: el bucle de sesión encola segmentos
descargados y el motor de reproducción los consume a velocidad real. Sobre ese
esquema se imponen dos reglas:

- **Tope de ocupación (60 s):** antes de descargar cada segmento, el cliente
  consulta la ocupación del buffer; si supera el máximo, espera en pasos de
  0,5 segundos hasta bajar del umbral. El tope acota el consumo de memoria y
  de red, y evita que un controlador conservador "resuelva" la sesión
  descargándolo todo por adelantado: con el buffer limitado, todos los
  controladores se enfrentan al mismo compromiso entre calidad y riesgo de
  parada.
- **Parada por agotamiento (stall):** si el buffer llega a vacío, el motor
  detiene la reproducción y lo notifica mediante eventos (inicio y fin de la
  parada). Esas paradas son el componente de rebuffering que penaliza la
  métrica de calidad de experiencia del capítulo 6.

Al agotar los segmentos del vídeo, el cliente señala el fin de flujo y drena
el buffer: deja que el motor consuma lo pendiente, con un límite temporal de
seguridad, antes de cerrar la sesión de forma ordenada.

Todos los parámetros de este apartado son configurables por sesión desde el
fichero de configuración; la Tabla 4.3 recoge sus valores por defecto, que son
los empleados en la evaluación del capítulo 6. La Figura 4.4 resume el modelo
del buffer con sus umbrales.

**[TABLA 4.3 — Parámetros de descarga y buffer]**

| Parámetro | Valor por defecto | Papel |
|---|---|---|
| Tope del buffer | 60 s | Ocupación máxima; por encima se pausa la descarga |
| Paso de espera | 0,5 s | Granularidad de la espera cuando el buffer está lleno |
| Tiempo máximo por petición | 10 s | Corte de peticiones colgadas |
| Reintentos de transporte | 3 | Reintento inmediato de la misma petición |
| Intentos por segmento | 6 | Tras agotarlos, se baja de nivel |
| Espera entre intentos | 0,5 s → 10 s | Retroceso exponencial |
| Ventana de arranque (preroll) | 10 s (0 en evaluación) | Marca los primeros segundos como fase de arranque en la telemetría (apartado 4.6) |

*Pie: Tabla 4.3: Parámetros de la descarga y del buffer, con los valores por
defecto de la configuración.*

**[FIGURA 4.4 — Modelo del buffer de reproducción. Fichero:
`figuras/fig_4_4_modelo_buffer.svg`]**
*Pie: Figura 4.4: Modelo del buffer de reproducción: el descargador lo llena a
ritmo variable (según la red), el motor lo consume a velocidad real, y dos
umbrales gobiernan la dinámica (parada al vaciarse; pausa de descarga al
superar el tope de 60 s).*

*(El apartado 4.4 continúa con el diseño de los motores de reproducción.)*

---

### Notas para Daniel (no van a la memoria)

- Citas usadas: `\cite{rfc9110, rfc9112}` (semántica HTTP / HTTP1.1 y conexión
  persistente). Nada más — el resto es diseño propio.
- Las tres cabeceras (identity / no-cache / keep-alive) están LITERALES en
  `core/descargador.py` — argumento de defensa potente: "el descargador está
  diseñado para que la medición sea fiel". Interiorízalo.
- OJO preroll: NO es "el motor espera 10 s para arrancar". Es una ventana de
  clasificación: los segmentos de los primeros `preroll_s` segundos se marcan
  `es_preroll`/fase de arranque en la telemetría y no puntúan en evaluación.
  En la evaluación formal va a 0 (la exclusión la hace el criterio de fases,
  apartado 4.6). Por eso en la tabla está descrito así.
- El umbral de stall de 1,2 s que verás en el código (UMBRAL_STALL_S) NO es
  de este apartado: es del detector de fases de la telemetría (clasifica
  "atascado"), no del motor. El stall real lo declara el motor al quedarse a
  cero. Va en 4.6.
- Valores verificados en código: BUFFER_MAXIMO_S=60.0, PASO_VACIADO_S=0.5,
  timeout=10, max_reintentos=3 (descargador), MAX_REINTENTOS=6 (reproductor),
  espera min(0.5·2^n, 10). Los tres primeros vienen de config.reproduccion /
  config.descargador (configurables por sesión).
- Longitud: ~800 palabras.
