# Réplica del experimento final con ventanas de evaluación nuevas

Preparado el 13/10/2026. Resuelve el aviso de la reutilización de las ventanas de
evaluación: las 12 ventanas reales del experimento de agosto ya se habían usado
en las comparativas de junio para diagnosticar fallos durante el desarrollo.

## Qué se hace y qué no cambia

- **No cambia nada del sistema:** mismo código de entrega, mismo modelo, mismo
  protocolo (preset `tfg_final`: 5 controladores, 4 vídeos, 300 sesiones) y misma
  semilla de selección (606).
- **Solo cambia el bombo del sorteo:** se retiran de la selección las 23 trazas
  de evaluación que pertenecen a los 11 grupos de captura ya evaluados. Salen 12
  ventanas reales nuevas sin ninguna traza ni grupo en común con las de agosto,
  con una composición parecida (FCC 7, Lumos5G 1, NYU-METS 2, Puffer 2). Las 3
  sintéticas, solo de diagnóstico, son las mismas.
- **No hace falta WSL ni reentrenar:** el modelo y el dataset no se tocan.
- **No hace falta GitHub:** el experimento de agosto se ejecutó con el código de
  entrega copiado en la VM cliente (sin git), y la réplica usa ese mismo código.
  El paso 3 lo comprueba fichero a fichero.

## Regla de uso de los resultados (fijada ANTES de ejecutar)

1. La réplica se ejecuta una sola vez, con el sistema congelado.
2. Las conclusiones de la memoria se formulan solo con lo que se cumpla en las dos
   evaluaciones (agosto y réplica); lo que solo se cumpla en una se presenta como
   no confirmado.
3. Si la réplica contradice a la evaluación de agosto, se dice así en el capítulo
   6 y en las conclusiones.
4. No se cambia nada ni se repite con otras ventanas a la vista de los resultados.

## Antes de empezar

- Las dos VM encendidas (cliente 192.168.1.160 y servidor 192.168.1.132). Apache
  arranca solo con la VM servidor.
- **El PC no debe suspenderse durante unas 11 horas** (en Windows 11:
  Configuración > Sistema > Energía > Pantalla y suspensión > Suspender: Nunca).
  Si el PC se suspende, las VM se congelan y las sesiones en curso fallan.
- Mejor de noche y sin usar el PC para otra cosa pesada: la emulación de red
  depende del tiempo real.

## Paso a paso

**Paso 1 (Windows, PowerShell):** copiar este kit a la VM cliente.

```powershell
scp -r "C:\Users\danie\Documents\TFG\DashClientModular4\docs\replica_ventanas_nuevas" daniel@192.168.1.160:~/TFG/
```

**Paso 2 (VM cliente):** hacer las seis comprobaciones. No ejecuta ninguna sesión.

```bash
bash ~/TFG/replica_ventanas_nuevas/replica.sh comprobar
```

Debe terminar con `TODO CORRECTO`. Comprueba que el código, el modelo y el
catálogo de la VM son idénticos a los del material de entrega, que el servidor
responde, genera el catálogo de la réplica y planifica en seco las 300 sesiones
verificando que salen exactamente las ventanas de `ventanas_esperadas.txt`.

**Paso 3 (VM cliente):** lanzar la réplica.

```bash
bash ~/TFG/replica_ventanas_nuevas/replica.sh lanzar
```

Puedes cerrar la terminal; sigue corriendo. Dura unas 10-11 horas.

**Paso 4 (VM cliente, cuando quieras):** ver cómo va.

```bash
bash ~/TFG/replica_ventanas_nuevas/replica.sh estado
```

Al terminar muestra `Gates superados: si` y la carpeta del paquete.

**Paso 5 (Windows, PowerShell):** traer el resultado.

```powershell
scp -r daniel@192.168.1.160:/home/daniel/TFG/validacion_comparativa_replica "C:\Users\danie\Documents\TFG\replica_resultado"
```

Después avisa a Claude: verifica el paquete, lo analiza junto al de agosto y lo
coloca en `TFG Material\04_evidencia_final\`.

## Si algo falla

| Fallo | Qué hacer |
|---|---|
| Paso 2, comprobación 1, 2 o 3 (código, modelo o catálogo distintos) | No copies nada todavía. Pega a Claude las líneas que salen como `FAILED`: hay que ver qué difiere antes de decidir. |
| Paso 2, comprobación 4 (servidor) | Enciende la VM servidor y repite el paso 2. |
| Paso 2, comprobación 6 (ventanas distintas) | No lances. Pega a Claude la salida. |
| `$'\r': command not found` | `sed -i 's/\r$//' ~/TFG/replica_ventanas_nuevas/replica.sh` y repite. |
| La réplica se cortó (apagón, reinicio) | `bash ~/TFG/replica_ventanas_nuevas/replica.sh reanudar`: continúa en el mismo paquete y omite las sesiones ya completadas. |

## Contenido del kit

| Fichero | Para qué |
|---|---|
| `replica.sh` | Las cuatro órdenes: comprobar, lanzar, estado, reanudar |
| `evaluacion.replica.json` | Configuración de agosto con dos rutas cambiadas (catálogo de la réplica y carpeta de salida) |
| `generar_catalogo_replica.py` | Crea el catálogo de la réplica retirando del sorteo los grupos ya evaluados |
| `comparar_ventanas.py` | Verifica que el plan en seco selecciona las ventanas esperadas |
| `grupos_excluidos.txt` | Los 11 grupos de captura de las 12 ventanas reales de agosto |
| `ventanas_esperadas.txt` | Las 15 ventanas que debe seleccionar la réplica |
| `hashes_*.sha256` | Huellas del código de entrega, del bundle y del catálogo |

Probado en Windows el 13/10/2026 con el código de entrega: catálogo con 23 trazas
retiradas, plan en seco de 300 sesiones con las 15 ventanas esperadas.
