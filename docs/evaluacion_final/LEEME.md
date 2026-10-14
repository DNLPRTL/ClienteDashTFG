# Evaluación final: paso a paso

> **SUPERADO (14/10/2026 por la noche).** El experimento lanzado con este kit se
> detuvo antes de terminar y no se analizó: es desarrollo. Este kit y los dos
> protocolos de esta carpeta sirven de base para la fase de blindaje
> (`docs/blindaje/00_HANDOFF_FASE_BLINDAJE.md`). El experimento final nuevo
> tendrá su propio protocolo y su propio kit, fijados antes de ejecutarlo.

La evaluación que presenta la memoria, con la versión final del controlador
propio. Qué se evalúa, qué cambió y cómo se analizará:
`PROTOCOLO_EVALUACION_FINAL.md` (fijado antes de ejecutar).

## Antes de empezar (una vez)

- **Windows, PowerShell como administrador:** que Windows no relegue la VM a los
  núcleos de eficiencia del procesador cuando su ventana no está delante.
  ```powershell
  powercfg /powerthrottling disable /path "C:\Program Files\Oracle\VirtualBox\VirtualBoxVM.exe"
  ```
- Las dos VM encendidas (cliente 192.168.1.160 y servidor 192.168.1.132).
- Durante la noche: el PC sin suspenderse, la ventana de la VM cliente visible
  (no minimizada) y sin usar WSL ni otras cargas pesadas.

## Paso 1 (VM cliente): apartar el código anterior

```bash
mv ~/TFG/ClienteDashTFG ~/TFG/ClienteDashTFG_antes_version_final
```

## Paso 2 (Windows, PowerShell): copiar el código final y este kit

```powershell
scp -r "C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG" daniel@192.168.1.160:~/TFG/
scp -r "C:\Users\danie\Documents\TFG\DashClientModular4\docs\evaluacion_final" daniel@192.168.1.160:~/TFG/
```

## Paso 3 (VM cliente): comprobar

```bash
bash ~/TFG/evaluacion_final/evaluacion_final.sh comprobar
```

Debe terminar con `TODO CORRECTO`: código, modelo y catálogo idénticos a los
del material, numpy y torch disponibles, servidor respondiendo, las 15
ventanas exactas de `ventanas_esperadas_final.txt` y el planificador en pocos
milisegundos.

## Paso 4 (VM cliente): prueba de humo (unos 11 minutos)

```bash
bash ~/TFG/evaluacion_final/evaluacion_final.sh humo
```

Ejecuta 5 sesiones reales (los cinco controladores en la primera ventana) en
`/tmp`, fuera del experimento. Debe terminar con `HUMO CORRECTO`, 5 de 5
sesiones completadas y 0 respaldos. Pega la salida a Claude antes de seguir.

## Paso 5 (VM cliente): lanzar el experimento, como siempre

```bash
cd ~/TFG/ClienteDashTFG && python3 scripts/3_evaluacion/gui_evaluacion.py
```

En la interfaz: preset `tfg_final`, los cinco controladores marcados y
"Ejecutar". No cierres la ventana de la interfaz. Dura unas 10,5 horas.

## Paso 6 (VM cliente, por la mañana): estado

```bash
bash ~/TFG/evaluacion_final/evaluacion_final.sh estado
```

Al terminar: `Sesiones completadas: 300 de 300`, la línea de compuertas y el
veredicto de la verificación. Muestra también la carpeta del paquete.

## Paso 7 (Windows, PowerShell): traer el paquete

Con el nombre de la carpeta que muestra `estado` (por ejemplo
`20261014_230000_tfg_final`):

```powershell
scp -r daniel@192.168.1.160:/home/daniel/TFG/validacion_comparativa/NOMBRE_DEL_PAQUETE "C:\Users\danie\Documents\TFG\"
```

## Si algo falla

| Fallo | Qué hacer |
|---|---|
| `comprobar`, pasos 1-3 (código, modelo o catálogo distintos) | No lances. Pega las líneas `FAILED` a Claude. |
| `comprobar`, paso 5 (servidor) | Enciende la VM servidor y repite. |
| `comprobar`, paso 6 (ventanas distintas) o `humo` incorrecto | No lances. Pega la salida a Claude. |
| `$'\r': command not found` | `sed -i 's/\r$//' ~/TFG/evaluacion_final/evaluacion_final.sh` y repite. |
| El experimento se cortó (apagón, reinicio) | `cd ~/TFG/ClienteDashTFG && python3 scripts/3_evaluacion/ejecutar_evaluacion.py --raiz-paquete ~/TFG/validacion_comparativa/NOMBRE_DEL_PAQUETE`: continúa el mismo paquete y omite las sesiones ya completadas. |

## Contenido del kit

| Fichero | Para qué |
|---|---|
| `evaluacion_final.sh` | Las órdenes comprobar, humo y estado |
| `PROTOCOLO_EVALUACION_FINAL.md` | Qué se evalúa y cómo se analizará, fijado antes de ejecutar |
| `hashes_codigo_final.sha256`, `hashes_bundle.sha256`, `hashes_catalogo.sha256` | Huellas del código final, del modelo y del catálogo |
| `ventanas_esperadas_final.txt` | Las 15 ventanas que debe sortear el experimento |
| `comparar_ventanas.py`, `medir_planificador.py`, `resumen_humo.py` | Auxiliares de las comprobaciones |
| `verificacion/` | Las verificaciones hechas en Windows antes de ejecutar (planificador, entradas, latencia) |
| `cambios_codigo_version_final.diff` | Diferencias exactas entre el código anterior (archivado) y la versión final |
