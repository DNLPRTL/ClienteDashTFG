# Borrador 4.4 — Diseño de los motores de reproducción

> BORRADOR para masticar y reescribir (25/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/motores/` del entregable (base.py y simulado.py leídos
> enteros; gstreamer.py revisado).

---

### 4.4. Motores de reproducción

El motor de reproducción es el consumidor del buffer: recibe los segmentos
descargados, hace avanzar el tiempo de reproducción y detecta las paradas. En
el diseño del sistema, el motor cumple una función doble. Por un lado, cierra
el ciclo del streaming (sin consumo no hay dinámica de buffer que gobernar).
Por otro, es la fuente de verdad de las paradas de reproducción: el
rebuffering que penaliza la calidad de experiencia se mide aquí, no en la
descarga.

**Un contrato, dos motores.** El sistema define una interfaz común de motor
con cinco operaciones: arrancar y parar, encolar un segmento con su duración,
consultar la ocupación de la cola (en tiempo y en bytes) y suscribirse a sus
eventos. Sobre esa interfaz existen dos implementaciones intercambiables: un
motor simulado y un motor de reproducción real basado en GStreamer. El
reproductor no distingue cuál tiene delante; la elección se hace por
configuración. Ambos motores notifican los mismos eventos, que constituyen el
contrato de observación de la reproducción:

- *segmento encolado* y *segmento consumido*, que delimitan la vida de cada
  segmento en el buffer;
- *parada* (stall) y *recuperación*, con un identificador y la duración de la
  parada medida por reloj;
- *fin de la reproducción*, cuando se ha consumido todo el contenido.

**Motor simulado: el de la evaluación.** El motor simulado consume la cola a
velocidad real (1×) mediante un hilo propio: descuenta del segmento en cabeza
el tiempo transcurrido de reloj, sin decodificar los bytes. La reproducción
arranca cuando la cola alcanza un mínimo configurable (1 segundo por defecto);
si el buffer se vacía, el motor entra en parada, la notifica, y no reanuda
hasta volver a acumular ese mínimo, lo que introduce una histéresis realista
en la recuperación. Las duraciones de las paradas se miden con el reloj del
sistema, de modo que el rebuffering registrado corresponde a tiempo real
transcurrido.

Este es el motor empleado en toda la evaluación del capítulo 6, por una razón
de validez experimental: desacopla la medición de la capacidad de
decodificación de la máquina. Las sesiones de evaluación se ejecutan en una
máquina virtual sin aceleración gráfica; con un motor que decodificara, parte
de las paradas podrían deberse al coste de decodificar y no a la red, y el
experimento mediría la potencia de la máquina en lugar del comportamiento del
controlador. Con el motor simulado, la dinámica medida es exactamente la que
interesa: red, buffer y decisión. Conviene subrayar que no se trata de una
simulación acelerada: el tiempo transcurre a velocidad real, los stalls duran
lo que duran y una sesión de treinta segmentos de 4 segundos ocupa unos dos
minutos de reloj más sus paradas.

**Motor GStreamer: la reproducción real.** El segundo motor construye un
pipeline multimedia real con GStreamer \cite{gstreamerDocs}, integrado en
Python mediante PyGObject \cite{pygobjectDoc}: los segmentos se inyectan por
una fuente de aplicación (`appsrc`), se demultiplexan, se analiza el flujo
H.264 y, opcionalmente, se decodifica y presenta el vídeo en pantalla; también
puede descartarse la salida tras el demultiplexado, para reproducir sin coste
de decodificación. La ocupación y las paradas se calculan sobre la cola real
del pipeline y se notifican con el mismo contrato de eventos.

El papel del motor GStreamer en el proyecto es de verificación: demuestra que
el cliente es un reproductor completo (capaz de mostrar el vídeo descargado,
con su audio eliminado en la preparación del contenido) y sirve de contraste
del motor simulado en pruebas funcionales, ejecutando las mismas sesiones con
la misma telemetría. La evaluación formal, en cambio, no depende de él.

La Tabla 4.4 resume la comparación entre ambos motores y su papel en el
trabajo.

**[TABLA 4.4 — Comparando los dos motores de reproducción]**

| Aspecto a comparar | Motor simulado sin decodificación | Motor basado en GStreamer |
|---|---|---|
| Consumo del buffer | Se descuenta a velocidad real 1x | Pipeline multimedia real (appsrc, demux, H.264, sink) |
| Detección de paradas | Cuando la cola se vacía, el reloj mide la duración | Con la cola real del pipeline |
| Dependencias | No tiene (usa la biblioteca estándar) | GStreamer, PyGObject (en Linux) |
| Desempeño en el proyecto | La evaluación formal del capítulo 6 | Verificación funcional del cliente con reproducción real |
| Razón detrás | Confina la medida del coste de decodificación, es un comportamiento predecible | Para ver que el cliente es capaz de reproducir contenido real |

*Pie: Tabla 4.4: Comparación de los dos motores de reproducción y papel que desempeña
cada uno.*

*(El apartado 4.5 continúa con la interfaz común de los controladores ABR.)*

---

### Notas para Daniel (no van a la memoria)

- Citas usadas: `\cite{gstreamerDocs}` y `\cite{pygobjectDoc}` (las dos @misc
  del .bib, con versión real 1.16.3 / 3.36.0 en el 6.2). Nada más.
- Verificado en código: interfaz `MotorVideoBase` (start/stop/empujar_datos/
  obtener_tiempo_en_cola/obtener_bytes_en_cola + al_evento); MotorSimulado con
  hilo daemon, consumo por dt de perf_counter, arranque con
  tiempo_min_cola=1.0 s por defecto (config `motor_video.tiempo_min_cola`),
  umbral de vacío 0,01 s, stalls con id incremental y duración por reloj,
  eventos segmento_encolado/segmento_consumido/stall/stall_recuperado/
  reproduccion_terminada; MotorGStreamer con appsrc, sink configurable
  (autovideosink o fakesink si no decodifica), telemetría interna cada 200 ms.
- El argumento de defensa central del apartado: "con un motor que decodificara,
  el experimento mediría la potencia de la VM, no el controlador". Es TU
  respuesta a "¿por qué no evaluaste con reproducción real?" — y el GStreamer
  existe justo para demostrar que el cliente ES un reproductor real.
- La frase "unos dos minutos de reloj" sale de 30 segmentos × 4 s = 120 s.
  Coherente con la duración real del experimento (300 sesiones ≈ 10,4 h según
  el propio paquete: duración estimada 37500 s).
- El contenido no tiene audio (se eliminó al codificar con `-an`, cap 6.3/
  componentes) — por eso el pipeline es solo vídeo. Si el tribunal pregunta:
  decisión deliberada para aislar el problema ABR de vídeo.
- Longitud: ~750 palabras.
