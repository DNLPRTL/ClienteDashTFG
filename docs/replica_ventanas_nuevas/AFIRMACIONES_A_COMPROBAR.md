# Afirmaciones que se comprobarán con la réplica

Fijado el 14/10/2026, con la réplica ya terminada y ANTES de abrir ninguno de
sus resultados de calidad. Completa la regla de uso de `LEEME.md`.

## Criterio

Una afirmación de la evaluación de agosto "se cumple" si en la réplica va en el
mismo sentido y, cuando es una prueba estadística, llega a la misma conclusión
al 5 %. Los números los calcula el programa de análisis del propio paquete
(`estadistica.json`, `agregados_por_controlador.json`), sin cálculos
elegidos a mano. Solo cuentan las sesiones con trazas reales; las sintéticas
son diagnóstico.

## Afirmaciones (las de agosto)

1. El controlador propio obtiene la QoE lineal media más alta de los cinco.
2. Propio frente a MPC robusto: la diferencia pareada no es significativa
   (IC95 que incluye el 0 y prueba del signo con p ≥ 0,05).
3. Propio mejor que BBA y que BOLA, con significación (prueba del signo
   p < 0,05).
4. Propio mejor que el basado en tasa en la prueba del signo (p < 0,05).
5. Propio con menos paradas por sesión y menos sesiones con más de 5 s de
   rebuffering que el MPC robusto.
6. Ningún uso del respaldo y todas las inferencias del controlador propio
   auditadas.

Lo que solo se cumpla en una de las dos evaluaciones se presenta como no
confirmado; lo que se contradiga, como contradicción.

## Si una compuerta no se supera

1. Se diagnostica la causa leyendo solo las compuertas, la verificación y los
   registros de ejecución, sin abrir métricas de calidad.
2. Si la causa es del sistema evaluado (por ejemplo, el controlador recurrió
   al respaldo), es un resultado: se informa tal cual y no se repite nada.
3. Si la causa es un defecto del banco de pruebas ajeno a las decisiones
   (registro, auditoría, análisis), se corrige sin cambiar el controlador, el
   modelo ni las ventanas, se documenta y se declara en la memoria. El paquete
   original se conserva intacto.

## Diagnóstico de la réplica y decisión (14/10, sin abrir métricas de calidad)

**Qué falló.** El paquete `20261013_233745_tfg_final` completó 300/300
sesiones sin fallos y su verificación técnica es correcta, pero no supera dos
compuertas: `propios_sin_respaldo_en_evaluables` y
`propios_con_inferencia_verificada`. Las dos se deben a la misma y única
decisión: la primera decisión de la sesión
`s00005_controlador_propio_paseo_10min_30fps_4s_real_001_0eabc04a0b_r1`, la
primera sesión del controlador propio en la réplica. Su inferencia tardó
149,6 ms, por encima del límite de 50 ms, y la salvaguarda delegó en el
respaldo (motivo `latencia_excedida`). Las otras 1739 decisiones terminaron
con `exito_red`.

**Por qué.** Fue una ralentización pasajera de la máquina virtual. Las
decisiones de esa sesión tardaron 335 ms de media, frente a unos 175 ms en
las demás sesiones, y la primera inferencia de las otras 59 sesiones de la
réplica tardó como máximo 7,4 ms (en agosto, como máximo 7,3 ms). No es un
fallo del modelo ni del código, que son idénticos a los de agosto.

**Qué cambió en la sesión.** Nada en las acciones: el planificador había
elegido el nivel 0 (`accion_bruta_red` = 0) y el respaldo eligió también el
nivel 0. El tiempo añadido por el respaldo es de milisegundos.

**Decisión.** Se aplica el punto 2: el uso del respaldo es un resultado, se
informa tal cual y no se repite ninguna sesión. El veredicto automático del
paquete (compuertas no superadas) se conserva sin modificar. Para decidir si
sus números pueden usarse en las conclusiones, se fija este criterio antes de
reproducir las decisiones y antes de abrir ninguna métrica de calidad:

1. Se reproducen fuera de línea las 1740 decisiones del controlador propio con
   el bundle de entrega, igual que las de agosto.
2. Si el modelo elige, sin respaldo, exactamente la acción registrada en las
   1740 decisiones (incluida la delegada), las sesiones del controlador propio
   son decisiones del modelo y el paquete se usa para comprobar las
   afirmaciones, con la salvedad declarada en la memoria.
3. En ese caso, las afirmaciones se comprueban también sin el escenario
   afectado (ventana `real_001_0eabc04a0b` con Paseo 30 fps, sus cinco
   controladores). Si alguna conclusión cambia al excluirlo, se declara.
4. Si la reproducción no confirma la coincidencia, el paquete queda como
   diagnóstico, como dicta la compuerta, y sus números no sustentan
   conclusiones.
