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
