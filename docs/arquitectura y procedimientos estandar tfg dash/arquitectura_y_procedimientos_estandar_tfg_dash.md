# Arquitectura operativa y procedimientos estándar del TFG DASH/ABR

Este documento define cómo se organiza el proyecto, qué papel tiene cada máquina y cuál debe ser el flujo estándar de trabajo entre Windows físico, WSL2 Ubuntu para entrenamiento IA, la VM cliente Ubuntu y la VM servidor Ubuntu.

El objetivo es evitar confusiones entre entorno de desarrollo, entorno de ejecución real, servidor de contenidos y entorno de benchmark. También sirve como guía para Codex: cuando modifique el proyecto, debe respetar esta arquitectura y no mezclar responsabilidades entre máquinas.

---

## 1. Idea principal

El proyecto no se trabaja como si todo ocurriera en una sola máquina.

Hay cuatro entornos con responsabilidades distintas:

1. **Windows físico**: entorno principal de desarrollo, edición, commits, push y validación rápida.
2. **WSL2 Ubuntu local con ROCm**: entorno de entrenamiento IA pesado con GPU AMD. Genera datasets derivados, checkpoints, bundles y auditorías de entrenamiento fuera de Git.
3. **VM cliente Ubuntu**: entorno real donde se sincroniza el repositorio y se ejecutan las fases finales, pruebas relevantes, scripts de benchmark y generación de evidencia.
4. **VM servidor Ubuntu**: servidor HTTP de contenidos DASH. Aloja los MPD, segmentos e inicializaciones, pero no define por sí misma la red del benchmark.

La regla más importante es:

> **Windows desarrolla y versiona; WSL2 entrena IA pesada; Ubuntu cliente valida lo que importa; Ubuntu servidor solo sirve contenido DASH.**

---

## 2. Mapa de arquitectura

```text
┌────────────────────────────────────────────────────────────┐
│ Windows físico                                             │
│                                                            │
│ - Codex desarrolla                                         │
│ - Codex modifica código, scripts y documentación            │
│ - Codex ejecuta tests y validaciones locales en Windows     │
│ - Codex hace commit                                        │
│ - Codex hace push a GitHub                                 │
│ - No es el entorno final de benchmark                       │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               │ git push / git pull
                               ▼
┌────────────────────────────────────────────────────────────┐
│ GitHub                                                     │
│                                                            │
│ - Punto limpio entre Windows, WSL2 y Ubuntu cliente         │
│ - Fuente canónica para llevar cambios a WSL2/VM cliente     │
│ - Evita copiar código manualmente si no es necesario        │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               │ git pull en WSL2 para entrenamiento IA
                               ▼
┌────────────────────────────────────────────────────────────┐
│ WSL2 Ubuntu local con ROCm                                 │
│                                                            │
│ - Clona/sincroniza el repo desde GitHub                     │
│ - Ejecuta entrenamientos IA con PyTorch/ROCm/GPU            │
│ - Usa rutas Linux bajo ~/TFG                                │
│ - Guarda datasets derivados, checkpoints y bundles fuera Git│
│ - No sustituye la validación formal en Ubuntu cliente       │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               │ git pull en Ubuntu cliente
                               ▼
┌────────────────────────────────────────────────────────────┐
│ VM cliente Ubuntu                                          │
│                                                            │
│ - Sincroniza el repo desde GitHub                           │
│ - Ejecuta scripts finales                                   │
│ - Aloja trazas normalizadas                                 │
│ - Aloja manifests finales                                   │
│ - Aloja bundle IA final                                     │
│ - Ejecuta Phase 6F                                          │
│ - Genera paquete de evidencia                               │
│ - Es el entorno que importa para validar funcionamiento real │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               │ HTTP: descarga MPD y segmentos
                               ▼
┌────────────────────────────────────────────────────────────┐
│ VM servidor Ubuntu                                         │
│                                                            │
│ - Aloja /var/www/html/dash                                  │
│ - Sirve MPDs y segmentos por HTTP                           │
│ - Aporta media_profile                                      │
│ - No aporta la red del benchmark                            │
└────────────────────────────────────────────────────────────┘
```

---

## 3. Responsabilidad de cada entorno

### 3.1. Windows físico

Windows es el entorno cómodo de desarrollo y control del repositorio.

En Windows:

- Codex desarrolla el código.
- Codex modifica scripts, documentación, tests y configuración.
- Codex ejecuta validaciones rápidas.
- Codex revisa estado de Git.
- Codex hace los commits.
- Codex hace push directamente a GitHub.
- Se mantiene el historial limpio y trazable.

Windows **no** debe tratarse como el entorno final del benchmark. Que algo pase en Windows ayuda, pero no basta para cerrar una fase experimental.

Windows sirve para producir una versión ordenada, testeada y subida a GitHub.

### 3.2. WSL2 Ubuntu local con ROCm

WSL2 Ubuntu es el entorno local de entrenamiento IA pesado cuando una fase
necesite usar GPU.

Estado observado tras la instalación:

- Distribución: `Ubuntu-24.04` en WSL2.
- Ubuntu observado: `Ubuntu 24.04.4 LTS`.
- Acceso GPU WSL: `/dev/dxg` presente.
- ROCm: `rocminfo` detecta la GPU AMD.
- GPU: `AMD Radeon RX 7800 XT`.
- PyTorch: `2.9.1+rocm7.2.1`.
- Entorno virtual: `~/venvs/rocm721`.
- Comprobación PyTorch: `torch.cuda.is_available()` devuelve `True`.

En WSL2:

- Se clona o sincroniza el repositorio desde GitHub.
- Se ejecutan entrenamientos, fine-tuning, generación de datasets derivados y
  validaciones offline de modelos.
- Se guardan outputs pesados bajo rutas Linux, preferiblemente `~/TFG/...`.
- No se usa `/mnt/c/Users/danie/Documents/TFG/...` como ruta principal para
  entrenamiento ni movimiento intensivo de ficheros.
- No se commitean checkpoints, modelos, bundles, runs, CSVs generados ni logs.

WSL2 no sustituye a la VM cliente Ubuntu. Si un modelo entrenado en WSL2 pasa a
ser candidato, debe integrarse como controller reproducible y después evaluarse
en Ubuntu cliente mediante los runbooks y gates correspondientes.

### 3.3. VM cliente Ubuntu

La VM cliente Ubuntu es el entorno donde el proyecto debe funcionar de verdad.

En la VM cliente:

- Se clona o sincroniza el repositorio desde GitHub.
- Se ejecutan los scripts finales.
- Se ejecutan las fases importantes de reproducción, evaluación y benchmark.
- Se mantienen las trazas normalizadas.
- Se mantienen los manifests finales.
- Se mantiene el bundle IA final.
- Se ejecuta Phase 6F.
- Se genera el paquete final de evidencia.

La VM cliente representa el entorno Linux real del cliente DASH/ABR. Por tanto, si hay una discrepancia entre Windows y Ubuntu cliente, **manda Ubuntu cliente**.

### 3.4. VM servidor Ubuntu

La VM servidor Ubuntu no desarrolla, no evalúa controllers y no decide las condiciones de red del benchmark.

Su función es servir el contenido multimedia DASH por HTTP.

En la VM servidor:

- Está el directorio real `/var/www/html/dash`.
- Se alojan los MPD.
- Se alojan los segmentos `.m4s`.
- Se alojan los ficheros de inicialización `.mp4`.
- Se exponen URLs HTTP accesibles desde la VM cliente.
- Se obtiene información del `media_profile`: duración, bitrates, resolutions, FPS, duración de segmentos, etc.

La VM servidor aporta el contenido sobre el que el cliente trabaja. No debe confundirse con el entorno de red experimental.

La red del benchmark debe venir de los mecanismos definidos para replay/emulación/control de red desde la arquitectura del proyecto, no simplemente del hecho de que exista una VM servidor.

---

## 4. Separación conceptual importante

### 4.1. Código

El código vive en el repositorio.

El código se desarrolla principalmente en Windows con Codex y después se sincroniza en WSL2 o Ubuntu cliente mediante GitHub, según el tipo de tarea.

WSL2 puede ejecutar scripts de entrenamiento IA, pero no debe convertirse en el
repositorio principal ni en el entorno que hace commits.

### 4.2. Datos pesados

Los datasets, trazas, bundles, manifests finales y paquetes de evidencia pueden estar fuera del repositorio si son grandes, generados o no deben versionarse.

Estos elementos deben tener rutas claras y manifests que permitan saber exactamente qué se ha usado.

Para entrenamiento IA en WSL2, los datos pesados deben estar bajo `~/TFG/...`
dentro del sistema de ficheros Linux de WSL2. Evitar usar `/mnt/c/...` como
workspace principal de entrenamiento por rendimiento, estabilidad de I/O y
separación operativa.

### 4.3. Contenido DASH

El contenido DASH vive en la VM servidor Ubuntu, bajo `/var/www/html/dash`.

Incluye:

- MPD.
- Segmentos `.m4s`.
- Inicializaciones `.mp4`.
- Vídeos fuente.
- Representations.
- Escaleras de bitrate.

Este contenido se consume por HTTP desde el cliente.

### 4.4. Benchmark

El benchmark real debe ejecutarse en la VM cliente Ubuntu.

Windows puede validar sintaxis, tests unitarios, estructura y documentación, pero no sustituye la validación final de ejecución en Ubuntu cliente.

---

## 5. Flujo estándar de trabajo

### 5.1. Flujo normal para cambios de código o documentación

```text
1. Codex trabaja en Windows.
2. Codex modifica código/documentación/scripts/tests.
3. Codex ejecuta validaciones en Windows.
4. Codex revisa git status.
5. Codex hace commit.
6. Codex hace push a GitHub.
7. Si la tarea requiere IA pesada, Daniel sincroniza WSL2 y ejecuta el
   entrenamiento indicado.
8. Si la tarea requiere validación formal, Daniel entra en la VM cliente Ubuntu.
9. Daniel hace git pull.
10. Daniel ejecuta la validación o fase correspondiente en Ubuntu cliente.
11. Si falla en Ubuntu cliente, se reporta el error y Codex corrige desde Windows.
```

### 5.2. Qué debe hacer Codex siempre en Windows

Codex debe encargarse de:

- Aplicar los cambios solicitados.
- Mantener coherencia de rutas y estructura.
- Ejecutar los tests o validaciones disponibles en Windows.
- Comprobar que no hay errores evidentes.
- Hacer commit.
- Hacer push a GitHub.
- Explicar qué ha cambiado.
- Dejar instrucciones claras para que Daniel solo tenga que sincronizar en Ubuntu cliente y ejecutar.

### 5.3. Qué debe hacer Daniel normalmente en Windows

Daniel no debería tener que hacer casi nada manualmente en Windows.

Como máximo:

- Mover carpetas grandes de datasets ya preparados.
- Mover repositorios o bundles completos si una fase lo exige.
- Lanzar algún script puntual si Codex lo indica de forma explícita.
- Revisar que Codex ha dejado commit y push hechos.

Pero el flujo deseado es que Daniel no tenga que hacer commits, push, tests manuales ni validaciones largas desde Windows.

### 5.4. Qué debe hacer Daniel en Ubuntu cliente

En Ubuntu cliente sí debe ejecutar lo importante:

```bash
cd ~/TFG/ClienteDashPrudente
git pull
```

Después debe lanzar la validación, smoke, fase o benchmark que corresponda según el runbook.

Ubuntu cliente es donde se comprueba si el sistema realmente funciona con:

- Linux.
- Dependencias reales.
- Rutas reales.
- Bundle IA real.
- Trazas reales.
- Cliente DASH real.
- Comunicación HTTP con la VM servidor.

---

## 6. Procedimiento estándar para Codex

Cuando Codex reciba una tarea del proyecto, debe actuar siguiendo este orden:

### 6.1. Antes de modificar

1. Entender si la tarea afecta a código, documentación, datasets, scripts, tests, bundles o evaluación.
2. No asumir que Windows es el entorno final.
3. Identificar si el resultado debe validarse después en Ubuntu cliente.
4. Evitar rutas hardcodeadas innecesarias.
5. Respetar la separación entre repo, datasets externos, bundles y servidor DASH.

### 6.2. Durante la modificación

1. Hacer cambios mínimos pero suficientes.
2. No romper rutas canónicas.
3. No mover datasets pesados al repositorio.
4. No meter paquetes de evidencia generados dentro del código salvo que esté previsto.
5. No mezclar el inventario del servidor con los resultados del benchmark.
6. Mantener documentación y scripts alineados.

### 6.3. Después de modificar

Codex debe ejecutar validaciones de Windows cuando existan.

Ejemplos orientativos:

```powershell
git status --short --branch
pytest
python scripts/comprobar_cliente.py --strict
git diff --check
```

No todos los comandos existirán siempre ni todos aplican a todas las fases. Codex debe elegir los que correspondan al estado real del proyecto.

### 6.4. Cierre obligatorio en Windows

Si todo está correcto, Codex debe:

```powershell
git status --short --branch
git add <ruta_o_rutas_explicitamente_revisadas>
git commit -m "mensaje claro"
git push
```

No se debe usar `git add .`. Cada cierre debe stagear solo las rutas que se han
revisado y que pertenecen al cambio actual.

Después debe entregar a Daniel:

- Resumen de cambios.
- Commit o commits generados.
- Validaciones ejecutadas.
- Instrucciones exactas para Ubuntu cliente.
- Qué salida esperar.
- Qué hacer si falla.

---

## 7. Procedimiento estándar en Ubuntu cliente

Después del push de Codex, Daniel debe sincronizar Ubuntu cliente.

Ejemplo base:

```bash
cd ~/TFG/ClienteDashPrudente
git status --short --branch
git pull
git status --short --branch
```

Luego se ejecuta la fase correspondiente.

Para Phase 6F o fases finales, la VM cliente debe tener localizados:

- Repo actualizado.
- Trazas normalizadas.
- Manifests finales.
- Bundle IA final.
- Configuración local.
- Acceso HTTP a la VM servidor.
- Directorio de salida de runs/evidencia.

La validación realmente importante es la de Ubuntu cliente.

---

## 7.bis. Procedimiento estándar en WSL2 para entrenamiento IA

WSL2 se usa cuando el proyecto necesite entrenamiento IA con GPU AMD/ROCm.

Primer clonado recomendado:

```bash
wsl -d Ubuntu-24.04
cd ~
mkdir -p ~/TFG
cd ~/TFG
git clone https://github.com/DNLPRTL/ClienteDashPrudente.git
cd ClienteDashPrudente
git checkout rebuild/phase3-from-phase2
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Sincronización diaria si el repo ya existe:

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/ClienteDashPrudente
git status --short --branch
git pull
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

La salida esperada de la comprobación PyTorch es `True` y `AMD Radeon RX 7800 XT`
o nombre equivalente de la GPU AMD expuesta por ROCm.

Los outputs pesados de entrenamiento deben guardarse fuera del repositorio,
preferiblemente bajo:

```bash
~/TFG/datasets_normalizados
~/TFG/modelos
~/TFG/runs_trazas
~/TFG/auditorias_trazas
```

Si el usuario observado dentro de WSL2 no es `daniel`, usar siempre rutas con
`~` en los runbooks para evitar confusiones entre `/home/danie` y
`/home/daniel`.

---

## 8. Procedimiento estándar para la VM servidor Ubuntu

La VM servidor Ubuntu debe mantenerse simple y estable.

### 8.1. Función

La VM servidor:

- Aloja el contenido DASH.
- Sirve el contenido por HTTP.
- Permite que la VM cliente descargue MPDs y segmentos.
- Proporciona las URLs y características multimedia necesarias para construir `media_profile`.

### 8.2. Qué no debe hacer

La VM servidor no debe:

- Ejecutar el cliente ABR.
- Entrenar modelos.
- Ejecutar Phase 6F.
- Generar resultados finales de benchmark.
- Decidir por sí misma la red experimental.
- Guardar trazas normalizadas finales salvo que se documente expresamente.
- Ser tratada como repo principal.

### 8.3. Comprobaciones básicas

Desde la VM cliente, una comprobación mínima sería:

```bash
curl -I http://192.168.1.132/dash/
curl -I http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd
```

Si la VM cliente no puede acceder a esas URLs, el problema no es necesariamente del cliente DASH ni del ABR. Primero hay que revisar:

- IP de la VM servidor.
- Adaptador puente.
- Apache/Nginx activo.
- Firewall.
- Ruta `/var/www/html/dash`.
- Permisos de lectura.
- URL exacta del MPD.

---

## 9. Reglas de oro

1. **No cerrar una fase experimental solo porque pase en Windows.**
2. **Windows sirve para desarrollar, commitear y pushear.**
3. **Ubuntu cliente sirve para ejecutar lo que importa.**
4. **Ubuntu servidor sirve contenido DASH, no hace de benchmark.**
5. **GitHub es el puente limpio entre Windows y Ubuntu cliente.**
6. **Los datasets y bundles pesados deben estar documentados y manifestados.**
7. **Cada ejecución final debe dejar evidencia reproducible.**
8. **Los MPD y segmentos se consumen por HTTP, no copiándolos al cliente salvo necesidad explícita.**
9. **Si Windows y Ubuntu cliente discrepan, se prioriza Ubuntu cliente.**
10. **Codex debe dejar commit y push hechos siempre que cierre una tarea.**

---

## 10. Política de commits y push

El procedimiento estándar es:

```text
Codex modifica → Codex valida en Windows → Codex commit → Codex push → Daniel pull en Ubuntu cliente → Daniel ejecuta validación real
```

No se considera cerrada una tarea si:

- Hay cambios sin commitear.
- No se ha hecho push.
- No se ha explicado cómo validar en Ubuntu cliente.
- Se han creado rutas nuevas sin documentarlas.
- Se han movido datasets o bundles sin manifest.
- Se ha mezclado benchmark con servidor DASH.

---

## 11. Qué significa que Windows no sea el benchmark final

Windows puede pasar tests y aun así fallar en Ubuntu cliente por:

- Diferencias de rutas.
- Diferencias de dependencias.
- Diferencias de permisos.
- Diferencias de shell.
- Diferencias de red.
- Diferencias de GStreamer/ffmpeg/player.
- Diferencias de acceso HTTP al servidor DASH.
- Diferencias de paths para datasets, manifests o bundle IA.

Por eso, Windows es necesario pero no suficiente.

La prueba que importa es la de la VM cliente Ubuntu.

---

## 12. Qué significa que la VM servidor no aporte la red del benchmark

La VM servidor aporta el contenido, no el escenario de red.

Es decir:

- La VM servidor tiene los vídeos, MPD y segmentos.
- La VM cliente pide esos segmentos por HTTP.
- Las condiciones de red reproducibles deben venir de la fase de replay/emulación definida en el proyecto.
- La existencia de dos VMs no basta para decir que hay un benchmark controlado.
- El benchmark debe registrar qué traza, qué perfil, qué controller, qué MPD, qué configuración y qué resultados se han usado.

Esto evita un error conceptual grave: confundir “descargo desde otra VM” con “he reproducido una red experimental controlada”.

---

## 13. Checklist de cierre para Codex

Antes de declarar cerrada una tarea, Codex debe poder contestar:

- Qué archivos ha cambiado.
- Por qué los ha cambiado.
- Qué validaciones ha ejecutado en Windows.
- Qué commit ha creado.
- Si ha hecho push.
- Qué debe ejecutar Daniel en Ubuntu cliente.
- Qué rutas externas intervienen.
- Si se ha tocado algo relacionado con datasets, manifests o bundles.
- Si el cambio afecta al servidor DASH.
- Si el cambio afecta a Phase 6F o al paquete de evidencia.

---

## 14. Instrucciones tipo para entregar a Daniel tras cada cambio

Al cerrar una intervención, Codex debería dejar algo con esta forma:

```text
Hecho y subido a GitHub.

Commits:
- <hash> <mensaje>

Validado en Windows:
- <comando 1>: OK
- <comando 2>: OK

Ahora en Ubuntu cliente ejecuta:

cd ~/TFG/ClienteDashPrudente
git pull
<comando de validación real>

Resultado esperado:
- <archivo esperado>
- <log esperado>
- <métrica esperada>
- <paquete esperado>

Si falla:
- pega el error completo
- pega la ruta del run
- pega el último bloque del log
```

---

## 15. Inventario de la VM servidor Ubuntu DASH

La siguiente sección contiene el inventario completo de la VM servidor Ubuntu que aloja los MPD, segmentos e inicializaciones DASH.

**Importante:** este bloque se incluye literalmente a partir del inventario proporcionado y no debe reescribirse ni simplificarse, porque documenta las URLs, representations, bitrates, duración de segmentos, estructura física y contenido XML de los MPD.

---

# Inventario definitivo de la VM Ubuntu del servidor DASH

Documento generado a partir de los dos TXT adjuntos: `listado.txt` y `contenido_mpd_todos.txt`.

## 1. Datos de la máquina y del servidor HTTP

| Campo | Valor |
|---|---|
| Hostname observado | `TFGv1` |
| Usuario observado | `daniel` |
| IP de la VM servidor | `192.168.1.132` |
| Directorio real en Ubuntu | `/var/www/html/dash` |
| URL base pública/local | `http://192.168.1.132/dash/` |
| Uso previsto | Servidor HTTP que aloja MPD, segmentos `.m4s` y ficheros de inicialización `.mp4` para pruebas DASH/ABR. |

> Regla de conversión usada en este inventario: cualquier ruta relativa `./X/Y/Z.mpd` bajo `/var/www/html/dash` se expone como `http://192.168.1.132/dash/X/Y/Z.mpd`.

## 2. Resumen ejecutivo

| Elemento | Valor |
|---|---:|
| Contenidos de vídeo detectados | 8 |
| MPD detectados | 16 |
| Carpetas `chunk_*bps` detectadas | 96 |
| Segmentos `.m4s` detectados | 12216 |
| Ficheros de inicialización dentro de `chunk_*bps` | 96 |
| Vídeos fuente principales `.mp4` | 8 |
| Vídeos intermedios en `_reps_*` | 48 |
| Ficheros totales detectados en `listado.txt` | 12387 |
| Directorios totales detectados en `listado.txt` | 128 |
| Tamaño total aproximado de ficheros listados | 12.47 GiB |

Escalera de bitrates común detectada en los MPD:

| Orden ascendente | Bandwidth MPD | Equivalencia aproximada |
|---:|---:|---:|
| 1 | `300000` bps | `0.30` Mbps |
| 2 | `750000` bps | `0.75` Mbps |
| 3 | `1200000` bps | `1.20` Mbps |
| 4 | `1850000` bps | `1.85` Mbps |
| 5 | `2850000` bps | `2.85` Mbps |
| 6 | `4300000` bps | `4.30` Mbps |

### Validación rápida de consistencia

- Todos los MPD del TXT se han parseado correctamente.
- Todos los MPD tienen 6 `Representation`.
- Para cada MPD se han encontrado sus carpetas `chunk_*bps` correspondientes en el listado recursivo.

## 3. Estructura raíz detectada

| Tipo | Nombre | Tamaño listado | Permisos |
|---|---|---:|---|
| Directorio | `Blender_Sunflower_10min_30fps` | 4.00 KiB | `drwxrwxrwx` |
| Directorio | `Blender_Sunflower_10min_60fps` | 4.00 KiB | `drwxrwxrwx` |
| Directorio | `Blender_Sunflower_1min_30fps` | 4.00 KiB | `drwxrwxrwx` |
| Directorio | `Blender_Sunflower_1min_60fps` | 4.00 KiB | `drwxrwxrwx` |
| Fichero | `dash_batch_tool.sh` | 4.89 KiB | `-rwxrwxrwx` |
| Fichero | `listado.txt` | 0 B | `-rw-rw-r--` |
| Directorio | `Paseo_Almunecar_10min_30fps` | 4.00 KiB | `drwxrwxrwx` |
| Directorio | `Paseo_Almunecar_10min_60fps` | 4.00 KiB | `drwxrwxrwx` |
| Directorio | `Paseo_Almunecar_1min_30fps` | 4.00 KiB | `drwxrwxrwx` |
| Directorio | `Paseo_Almunecar_1min_60fps` | 4.00 KiB | `drwxrwxrwx` |
| Fichero | `video_tool.sh` | 2.99 KiB | `-rwxrwxrwx` |

## 4. Vídeos fuente principales

| Vídeo fuente | Ruta relativa | Tamaño | URL si se sirve directamente |
|---|---|---:|---|
| `Blender_Sunflower_10min_30fps.mp4` | `./Blender_Sunflower_10min_30fps/Blender_Sunflower_10min_30fps.mp4` | 263.34 MiB | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/Blender_Sunflower_10min_30fps.mp4` |
| `Blender_Sunflower_10min_60fps.mp4` | `./Blender_Sunflower_10min_60fps/Blender_Sunflower_10min_60fps.mp4` | 339.37 MiB | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/Blender_Sunflower_10min_60fps.mp4` |
| `Blender_Sunflower_1min_30fps.mp4` | `./Blender_Sunflower_1min_30fps/Blender_Sunflower_1min_30fps.mp4` | 25.57 MiB | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/Blender_Sunflower_1min_30fps.mp4` |
| `Blender_Sunflower_1min_60fps.mp4` | `./Blender_Sunflower_1min_60fps/Blender_Sunflower_1min_60fps.mp4` | 29.33 MiB | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/Blender_Sunflower_1min_60fps.mp4` |
| `Paseo_Almunecar_10min_30fps.mp4` | `./Paseo_Almunecar_10min_30fps/Paseo_Almunecar_10min_30fps.mp4` | 607.21 MiB | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/Paseo_Almunecar_10min_30fps.mp4` |
| `Paseo_Almunecar_10min_60fps.mp4` | `./Paseo_Almunecar_10min_60fps/Paseo_Almunecar_10min_60fps.mp4` | 693.87 MiB | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/Paseo_Almunecar_10min_60fps.mp4` |
| `Paseo_Almunecar_1min_30fps.mp4` | `./Paseo_Almunecar_1min_30fps/Paseo_Almunecar_1min_30fps.mp4` | 52.61 MiB | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/Paseo_Almunecar_1min_30fps.mp4` |
| `Paseo_Almunecar_1min_60fps.mp4` | `./Paseo_Almunecar_1min_60fps/Paseo_Almunecar_1min_60fps.mp4` | 59.46 MiB | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/Paseo_Almunecar_1min_60fps.mp4` |

## 5. URLs absolutas de todos los MPD

| # | MPD | Duración vídeo | Segmento objetivo | FPS máximo | URL absoluta |
|---:|---|---:|---:|---:|---|
| 1 | `./Blender_Sunflower_10min_30fps/2sec/Blender_Sunflower_10min_30fps_simple_2s.mpd` | `PT0H10M34.600S` | `PT0H0M2.000S` | `30` | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/Blender_Sunflower_10min_30fps_simple_2s.mpd` |
| 2 | `./Blender_Sunflower_10min_30fps/4sec/Blender_Sunflower_10min_30fps_simple_4s.mpd` | `PT0H10M34.600S` | `PT0H0M4.000S` | `30` | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/Blender_Sunflower_10min_30fps_simple_4s.mpd` |
| 3 | `./Blender_Sunflower_10min_60fps/2sec/Blender_Sunflower_10min_60fps_simple_2s.mpd` | `PT0H10M34.566S` | `PT0H0M2.000S` | `60` | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/Blender_Sunflower_10min_60fps_simple_2s.mpd` |
| 4 | `./Blender_Sunflower_10min_60fps/4sec/Blender_Sunflower_10min_60fps_simple_4s.mpd` | `PT0H10M34.566S` | `PT0H0M4.000S` | `60` | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/Blender_Sunflower_10min_60fps_simple_4s.mpd` |
| 5 | `./Blender_Sunflower_1min_30fps/2sec/Blender_Sunflower_1min_30fps_simple_2s.mpd` | `PT0H1M0.000S` | `PT0H0M2.000S` | `30` | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/Blender_Sunflower_1min_30fps_simple_2s.mpd` |
| 6 | `./Blender_Sunflower_1min_30fps/4sec/Blender_Sunflower_1min_30fps_simple_4s.mpd` | `PT0H1M0.000S` | `PT0H0M4.000S` | `30` | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/Blender_Sunflower_1min_30fps_simple_4s.mpd` |
| 7 | `./Blender_Sunflower_1min_60fps/2sec/Blender_Sunflower_1min_60fps_simple_2s.mpd` | `PT0H1M0.000S` | `PT0H0M2.000S` | `60` | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/Blender_Sunflower_1min_60fps_simple_2s.mpd` |
| 8 | `./Blender_Sunflower_1min_60fps/4sec/Blender_Sunflower_1min_60fps_simple_4s.mpd` | `PT0H1M0.000S` | `PT0H0M4.000S` | `60` | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/Blender_Sunflower_1min_60fps_simple_4s.mpd` |
| 9 | `./Paseo_Almunecar_10min_30fps/2sec/Paseo_Almunecar_10min_30fps_simple_2s.mpd` | `PT0H10M0.100S` | `PT0H0M2.000S` | `30` | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/Paseo_Almunecar_10min_30fps_simple_2s.mpd` |
| 10 | `./Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd` | `PT0H10M0.100S` | `PT0H0M4.000S` | `30` | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd` |
| 11 | `./Paseo_Almunecar_10min_60fps/2sec/Paseo_Almunecar_10min_60fps_simple_2s.mpd` | `PT0H10M0.016S` | `PT0H0M2.002S` | `60000/1001` | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/Paseo_Almunecar_10min_60fps_simple_2s.mpd` |
| 12 | `./Paseo_Almunecar_10min_60fps/4sec/Paseo_Almunecar_10min_60fps_simple_4s.mpd` | `PT0H10M0.016S` | `PT0H0M4.004S` | `60000/1001` | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/Paseo_Almunecar_10min_60fps_simple_4s.mpd` |
| 13 | `./Paseo_Almunecar_1min_30fps/2sec/Paseo_Almunecar_1min_30fps_simple_2s.mpd` | `PT0H1M0.000S` | `PT0H0M2.000S` | `30` | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/Paseo_Almunecar_1min_30fps_simple_2s.mpd` |
| 14 | `./Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd` | `PT0H1M0.000S` | `PT0H0M4.000S` | `30` | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd` |
| 15 | `./Paseo_Almunecar_1min_60fps/2sec/Paseo_Almunecar_1min_60fps_simple_2s.mpd` | `PT0H1M0.009S` | `PT0H0M2.002S` | `60000/1001` | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/Paseo_Almunecar_1min_60fps_simple_2s.mpd` |
| 16 | `./Paseo_Almunecar_1min_60fps/4sec/Paseo_Almunecar_1min_60fps_simple_4s.mpd` | `PT0H1M0.009S` | `PT0H0M4.004S` | `60000/1001` | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/Paseo_Almunecar_1min_60fps_simple_4s.mpd` |

## 6. Inventario técnico por MPD

### 6.1. `Blender_Sunflower_10min_30fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_10min_30fps/2sec/Blender_Sunflower_10min_30fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/Blender_Sunflower_10min_30fps_simple_2s.mpd` |
| Título MPD | `Blender_Sunflower_10min_30fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:29:11.023Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M34.600S` ≈ `634.600` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_2s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `30720` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_30fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_30fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_10min_30fps/2sec/chunk_300000bps` | [`Blender_Sunflower_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_300000bps/Blender_Sunflower_10min_30fps_2s.mp4) | 318 | `1–318` | 22.44 MiB | [`Blender_Sunflower_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_300000bps/Blender_Sunflower_10min_30fps_2s1.m4s) | [`Blender_Sunflower_10min_30fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_300000bps/Blender_Sunflower_10min_30fps_2s318.m4s) |
| `750000` | `./Blender_Sunflower_10min_30fps/2sec/chunk_750000bps` | [`Blender_Sunflower_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_750000bps/Blender_Sunflower_10min_30fps_2s.mp4) | 318 | `1–318` | 55.21 MiB | [`Blender_Sunflower_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_750000bps/Blender_Sunflower_10min_30fps_2s1.m4s) | [`Blender_Sunflower_10min_30fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_750000bps/Blender_Sunflower_10min_30fps_2s318.m4s) |
| `1200000` | `./Blender_Sunflower_10min_30fps/2sec/chunk_1200000bps` | [`Blender_Sunflower_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_1200000bps/Blender_Sunflower_10min_30fps_2s.mp4) | 318 | `1–318` | 87.98 MiB | [`Blender_Sunflower_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_1200000bps/Blender_Sunflower_10min_30fps_2s1.m4s) | [`Blender_Sunflower_10min_30fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_1200000bps/Blender_Sunflower_10min_30fps_2s318.m4s) |
| `1850000` | `./Blender_Sunflower_10min_30fps/2sec/chunk_1850000bps` | [`Blender_Sunflower_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_1850000bps/Blender_Sunflower_10min_30fps_2s.mp4) | 318 | `1–318` | 135.18 MiB | [`Blender_Sunflower_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_1850000bps/Blender_Sunflower_10min_30fps_2s1.m4s) | [`Blender_Sunflower_10min_30fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_1850000bps/Blender_Sunflower_10min_30fps_2s318.m4s) |
| `2850000` | `./Blender_Sunflower_10min_30fps/2sec/chunk_2850000bps` | [`Blender_Sunflower_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_2850000bps/Blender_Sunflower_10min_30fps_2s.mp4) | 318 | `1–318` | 206.50 MiB | [`Blender_Sunflower_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_2850000bps/Blender_Sunflower_10min_30fps_2s1.m4s) | [`Blender_Sunflower_10min_30fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_2850000bps/Blender_Sunflower_10min_30fps_2s318.m4s) |
| `4300000` | `./Blender_Sunflower_10min_30fps/2sec/chunk_4300000bps` | [`Blender_Sunflower_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_4300000bps/Blender_Sunflower_10min_30fps_2s.mp4) | 318 | `1–318` | 308.95 MiB | [`Blender_Sunflower_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_4300000bps/Blender_Sunflower_10min_30fps_2s1.m4s) | [`Blender_Sunflower_10min_30fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/2sec/chunk_4300000bps/Blender_Sunflower_10min_30fps_2s318.m4s) |

### 6.2. `Blender_Sunflower_10min_30fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_10min_30fps/4sec/Blender_Sunflower_10min_30fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/Blender_Sunflower_10min_30fps_simple_4s.mpd` |
| Título MPD | `Blender_Sunflower_10min_30fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:29:13.143Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M34.600S` ≈ `634.600` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_4s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `61440` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_30fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_30fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_10min_30fps/4sec/chunk_300000bps` | [`Blender_Sunflower_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_300000bps/Blender_Sunflower_10min_30fps_4s.mp4) | 159 | `1–159` | 22.48 MiB | [`Blender_Sunflower_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_300000bps/Blender_Sunflower_10min_30fps_4s1.m4s) | [`Blender_Sunflower_10min_30fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_300000bps/Blender_Sunflower_10min_30fps_4s159.m4s) |
| `750000` | `./Blender_Sunflower_10min_30fps/4sec/chunk_750000bps` | [`Blender_Sunflower_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_750000bps/Blender_Sunflower_10min_30fps_4s.mp4) | 159 | `1–159` | 55.25 MiB | [`Blender_Sunflower_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_750000bps/Blender_Sunflower_10min_30fps_4s1.m4s) | [`Blender_Sunflower_10min_30fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_750000bps/Blender_Sunflower_10min_30fps_4s159.m4s) |
| `1200000` | `./Blender_Sunflower_10min_30fps/4sec/chunk_1200000bps` | [`Blender_Sunflower_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_1200000bps/Blender_Sunflower_10min_30fps_4s.mp4) | 159 | `1–159` | 88.03 MiB | [`Blender_Sunflower_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_1200000bps/Blender_Sunflower_10min_30fps_4s1.m4s) | [`Blender_Sunflower_10min_30fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_1200000bps/Blender_Sunflower_10min_30fps_4s159.m4s) |
| `1850000` | `./Blender_Sunflower_10min_30fps/4sec/chunk_1850000bps` | [`Blender_Sunflower_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_1850000bps/Blender_Sunflower_10min_30fps_4s.mp4) | 159 | `1–159` | 135.23 MiB | [`Blender_Sunflower_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_1850000bps/Blender_Sunflower_10min_30fps_4s1.m4s) | [`Blender_Sunflower_10min_30fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_1850000bps/Blender_Sunflower_10min_30fps_4s159.m4s) |
| `2850000` | `./Blender_Sunflower_10min_30fps/4sec/chunk_2850000bps` | [`Blender_Sunflower_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_2850000bps/Blender_Sunflower_10min_30fps_4s.mp4) | 159 | `1–159` | 206.55 MiB | [`Blender_Sunflower_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_2850000bps/Blender_Sunflower_10min_30fps_4s1.m4s) | [`Blender_Sunflower_10min_30fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_2850000bps/Blender_Sunflower_10min_30fps_4s159.m4s) |
| `4300000` | `./Blender_Sunflower_10min_30fps/4sec/chunk_4300000bps` | [`Blender_Sunflower_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_4300000bps/Blender_Sunflower_10min_30fps_4s.mp4) | 159 | `1–159` | 309.00 MiB | [`Blender_Sunflower_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_4300000bps/Blender_Sunflower_10min_30fps_4s1.m4s) | [`Blender_Sunflower_10min_30fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_30fps/4sec/chunk_4300000bps/Blender_Sunflower_10min_30fps_4s159.m4s) |

### 6.3. `Blender_Sunflower_10min_60fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_10min_60fps/2sec/Blender_Sunflower_10min_60fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/Blender_Sunflower_10min_60fps_simple_2s.mpd` |
| Título MPD | `Blender_Sunflower_10min_60fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:58:09.939Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M34.566S` ≈ `634.566` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_2s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `30720` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_60fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_60fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_10min_60fps/2sec/chunk_300000bps` | [`Blender_Sunflower_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_300000bps/Blender_Sunflower_10min_60fps_2s.mp4) | 318 | `1–318` | 22.71 MiB | [`Blender_Sunflower_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_300000bps/Blender_Sunflower_10min_60fps_2s1.m4s) | [`Blender_Sunflower_10min_60fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_300000bps/Blender_Sunflower_10min_60fps_2s318.m4s) |
| `750000` | `./Blender_Sunflower_10min_60fps/2sec/chunk_750000bps` | [`Blender_Sunflower_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_750000bps/Blender_Sunflower_10min_60fps_2s.mp4) | 318 | `1–318` | 55.97 MiB | [`Blender_Sunflower_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_750000bps/Blender_Sunflower_10min_60fps_2s1.m4s) | [`Blender_Sunflower_10min_60fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_750000bps/Blender_Sunflower_10min_60fps_2s318.m4s) |
| `1200000` | `./Blender_Sunflower_10min_60fps/2sec/chunk_1200000bps` | [`Blender_Sunflower_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_1200000bps/Blender_Sunflower_10min_60fps_2s.mp4) | 318 | `1–318` | 88.91 MiB | [`Blender_Sunflower_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_1200000bps/Blender_Sunflower_10min_60fps_2s1.m4s) | [`Blender_Sunflower_10min_60fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_1200000bps/Blender_Sunflower_10min_60fps_2s318.m4s) |
| `1850000` | `./Blender_Sunflower_10min_60fps/2sec/chunk_1850000bps` | [`Blender_Sunflower_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_1850000bps/Blender_Sunflower_10min_60fps_2s.mp4) | 318 | `1–318` | 136.20 MiB | [`Blender_Sunflower_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_1850000bps/Blender_Sunflower_10min_60fps_2s1.m4s) | [`Blender_Sunflower_10min_60fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_1850000bps/Blender_Sunflower_10min_60fps_2s318.m4s) |
| `2850000` | `./Blender_Sunflower_10min_60fps/2sec/chunk_2850000bps` | [`Blender_Sunflower_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_2850000bps/Blender_Sunflower_10min_60fps_2s.mp4) | 318 | `1–318` | 208.62 MiB | [`Blender_Sunflower_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_2850000bps/Blender_Sunflower_10min_60fps_2s1.m4s) | [`Blender_Sunflower_10min_60fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_2850000bps/Blender_Sunflower_10min_60fps_2s318.m4s) |
| `4300000` | `./Blender_Sunflower_10min_60fps/2sec/chunk_4300000bps` | [`Blender_Sunflower_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_4300000bps/Blender_Sunflower_10min_60fps_2s.mp4) | 318 | `1–318` | 312.61 MiB | [`Blender_Sunflower_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_4300000bps/Blender_Sunflower_10min_60fps_2s1.m4s) | [`Blender_Sunflower_10min_60fps_2s318.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/2sec/chunk_4300000bps/Blender_Sunflower_10min_60fps_2s318.m4s) |

### 6.4. `Blender_Sunflower_10min_60fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_10min_60fps/4sec/Blender_Sunflower_10min_60fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/Blender_Sunflower_10min_60fps_simple_4s.mpd` |
| Título MPD | `Blender_Sunflower_10min_60fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:58:12.519Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M34.566S` ≈ `634.566` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_4s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `61440` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_60fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_10min_60fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_10min_60fps/4sec/chunk_300000bps` | [`Blender_Sunflower_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_300000bps/Blender_Sunflower_10min_60fps_4s.mp4) | 159 | `1–159` | 22.83 MiB | [`Blender_Sunflower_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_300000bps/Blender_Sunflower_10min_60fps_4s1.m4s) | [`Blender_Sunflower_10min_60fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_300000bps/Blender_Sunflower_10min_60fps_4s159.m4s) |
| `750000` | `./Blender_Sunflower_10min_60fps/4sec/chunk_750000bps` | [`Blender_Sunflower_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_750000bps/Blender_Sunflower_10min_60fps_4s.mp4) | 159 | `1–159` | 56.09 MiB | [`Blender_Sunflower_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_750000bps/Blender_Sunflower_10min_60fps_4s1.m4s) | [`Blender_Sunflower_10min_60fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_750000bps/Blender_Sunflower_10min_60fps_4s159.m4s) |
| `1200000` | `./Blender_Sunflower_10min_60fps/4sec/chunk_1200000bps` | [`Blender_Sunflower_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_1200000bps/Blender_Sunflower_10min_60fps_4s.mp4) | 159 | `1–159` | 89.03 MiB | [`Blender_Sunflower_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_1200000bps/Blender_Sunflower_10min_60fps_4s1.m4s) | [`Blender_Sunflower_10min_60fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_1200000bps/Blender_Sunflower_10min_60fps_4s159.m4s) |
| `1850000` | `./Blender_Sunflower_10min_60fps/4sec/chunk_1850000bps` | [`Blender_Sunflower_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_1850000bps/Blender_Sunflower_10min_60fps_4s.mp4) | 159 | `1–159` | 136.32 MiB | [`Blender_Sunflower_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_1850000bps/Blender_Sunflower_10min_60fps_4s1.m4s) | [`Blender_Sunflower_10min_60fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_1850000bps/Blender_Sunflower_10min_60fps_4s159.m4s) |
| `2850000` | `./Blender_Sunflower_10min_60fps/4sec/chunk_2850000bps` | [`Blender_Sunflower_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_2850000bps/Blender_Sunflower_10min_60fps_4s.mp4) | 159 | `1–159` | 208.74 MiB | [`Blender_Sunflower_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_2850000bps/Blender_Sunflower_10min_60fps_4s1.m4s) | [`Blender_Sunflower_10min_60fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_2850000bps/Blender_Sunflower_10min_60fps_4s159.m4s) |
| `4300000` | `./Blender_Sunflower_10min_60fps/4sec/chunk_4300000bps` | [`Blender_Sunflower_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_4300000bps/Blender_Sunflower_10min_60fps_4s.mp4) | 159 | `1–159` | 312.73 MiB | [`Blender_Sunflower_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_4300000bps/Blender_Sunflower_10min_60fps_4s1.m4s) | [`Blender_Sunflower_10min_60fps_4s159.m4s`](http://192.168.1.132/dash/Blender_Sunflower_10min_60fps/4sec/chunk_4300000bps/Blender_Sunflower_10min_60fps_4s159.m4s) |

### 6.5. `Blender_Sunflower_1min_30fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_1min_30fps/2sec/Blender_Sunflower_1min_30fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/Blender_Sunflower_1min_30fps_simple_2s.mpd` |
| Título MPD | `Blender_Sunflower_1min_30fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:59:19.392Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.000S` ≈ `60.000` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_2s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `30720` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_30fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_30fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_1min_30fps/2sec/chunk_300000bps` | [`Blender_Sunflower_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_300000bps/Blender_Sunflower_1min_30fps_2s.mp4) | 30 | `1–30` | 2.10 MiB | [`Blender_Sunflower_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_300000bps/Blender_Sunflower_1min_30fps_2s1.m4s) | [`Blender_Sunflower_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_300000bps/Blender_Sunflower_1min_30fps_2s30.m4s) |
| `750000` | `./Blender_Sunflower_1min_30fps/2sec/chunk_750000bps` | [`Blender_Sunflower_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_750000bps/Blender_Sunflower_1min_30fps_2s.mp4) | 30 | `1–30` | 5.16 MiB | [`Blender_Sunflower_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_750000bps/Blender_Sunflower_1min_30fps_2s1.m4s) | [`Blender_Sunflower_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_750000bps/Blender_Sunflower_1min_30fps_2s30.m4s) |
| `1200000` | `./Blender_Sunflower_1min_30fps/2sec/chunk_1200000bps` | [`Blender_Sunflower_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_1200000bps/Blender_Sunflower_1min_30fps_2s.mp4) | 30 | `1–30` | 8.15 MiB | [`Blender_Sunflower_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_1200000bps/Blender_Sunflower_1min_30fps_2s1.m4s) | [`Blender_Sunflower_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_1200000bps/Blender_Sunflower_1min_30fps_2s30.m4s) |
| `1850000` | `./Blender_Sunflower_1min_30fps/2sec/chunk_1850000bps` | [`Blender_Sunflower_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_1850000bps/Blender_Sunflower_1min_30fps_2s.mp4) | 30 | `1–30` | 12.53 MiB | [`Blender_Sunflower_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_1850000bps/Blender_Sunflower_1min_30fps_2s1.m4s) | [`Blender_Sunflower_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_1850000bps/Blender_Sunflower_1min_30fps_2s30.m4s) |
| `2850000` | `./Blender_Sunflower_1min_30fps/2sec/chunk_2850000bps` | [`Blender_Sunflower_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_2850000bps/Blender_Sunflower_1min_30fps_2s.mp4) | 30 | `1–30` | 19.10 MiB | [`Blender_Sunflower_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_2850000bps/Blender_Sunflower_1min_30fps_2s1.m4s) | [`Blender_Sunflower_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_2850000bps/Blender_Sunflower_1min_30fps_2s30.m4s) |
| `4300000` | `./Blender_Sunflower_1min_30fps/2sec/chunk_4300000bps` | [`Blender_Sunflower_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_4300000bps/Blender_Sunflower_1min_30fps_2s.mp4) | 30 | `1–30` | 28.24 MiB | [`Blender_Sunflower_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_4300000bps/Blender_Sunflower_1min_30fps_2s1.m4s) | [`Blender_Sunflower_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/2sec/chunk_4300000bps/Blender_Sunflower_1min_30fps_2s30.m4s) |

### 6.6. `Blender_Sunflower_1min_30fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_1min_30fps/4sec/Blender_Sunflower_1min_30fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/Blender_Sunflower_1min_30fps_simple_4s.mpd` |
| Título MPD | `Blender_Sunflower_1min_30fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:59:20.102Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.000S` ≈ `60.000` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_4s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `61440` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_30fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_30fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_1min_30fps/4sec/chunk_300000bps` | [`Blender_Sunflower_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_300000bps/Blender_Sunflower_1min_30fps_4s.mp4) | 15 | `1–15` | 2.10 MiB | [`Blender_Sunflower_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_300000bps/Blender_Sunflower_1min_30fps_4s1.m4s) | [`Blender_Sunflower_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_300000bps/Blender_Sunflower_1min_30fps_4s15.m4s) |
| `750000` | `./Blender_Sunflower_1min_30fps/4sec/chunk_750000bps` | [`Blender_Sunflower_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_750000bps/Blender_Sunflower_1min_30fps_4s.mp4) | 15 | `1–15` | 5.17 MiB | [`Blender_Sunflower_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_750000bps/Blender_Sunflower_1min_30fps_4s1.m4s) | [`Blender_Sunflower_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_750000bps/Blender_Sunflower_1min_30fps_4s15.m4s) |
| `1200000` | `./Blender_Sunflower_1min_30fps/4sec/chunk_1200000bps` | [`Blender_Sunflower_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_1200000bps/Blender_Sunflower_1min_30fps_4s.mp4) | 15 | `1–15` | 8.16 MiB | [`Blender_Sunflower_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_1200000bps/Blender_Sunflower_1min_30fps_4s1.m4s) | [`Blender_Sunflower_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_1200000bps/Blender_Sunflower_1min_30fps_4s15.m4s) |
| `1850000` | `./Blender_Sunflower_1min_30fps/4sec/chunk_1850000bps` | [`Blender_Sunflower_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_1850000bps/Blender_Sunflower_1min_30fps_4s.mp4) | 15 | `1–15` | 12.54 MiB | [`Blender_Sunflower_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_1850000bps/Blender_Sunflower_1min_30fps_4s1.m4s) | [`Blender_Sunflower_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_1850000bps/Blender_Sunflower_1min_30fps_4s15.m4s) |
| `2850000` | `./Blender_Sunflower_1min_30fps/4sec/chunk_2850000bps` | [`Blender_Sunflower_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_2850000bps/Blender_Sunflower_1min_30fps_4s.mp4) | 15 | `1–15` | 19.10 MiB | [`Blender_Sunflower_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_2850000bps/Blender_Sunflower_1min_30fps_4s1.m4s) | [`Blender_Sunflower_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_2850000bps/Blender_Sunflower_1min_30fps_4s15.m4s) |
| `4300000` | `./Blender_Sunflower_1min_30fps/4sec/chunk_4300000bps` | [`Blender_Sunflower_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_4300000bps/Blender_Sunflower_1min_30fps_4s.mp4) | 15 | `1–15` | 28.24 MiB | [`Blender_Sunflower_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_4300000bps/Blender_Sunflower_1min_30fps_4s1.m4s) | [`Blender_Sunflower_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_30fps/4sec/chunk_4300000bps/Blender_Sunflower_1min_30fps_4s15.m4s) |

### 6.7. `Blender_Sunflower_1min_60fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_1min_60fps/2sec/Blender_Sunflower_1min_60fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/Blender_Sunflower_1min_60fps_simple_2s.mpd` |
| Título MPD | `Blender_Sunflower_1min_60fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:01:00.681Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.000S` ≈ `60.000` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_2s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `30720` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_60fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_60fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_1min_60fps/2sec/chunk_300000bps` | [`Blender_Sunflower_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_300000bps/Blender_Sunflower_1min_60fps_2s.mp4) | 30 | `1–30` | 2.14 MiB | [`Blender_Sunflower_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_300000bps/Blender_Sunflower_1min_60fps_2s1.m4s) | [`Blender_Sunflower_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_300000bps/Blender_Sunflower_1min_60fps_2s30.m4s) |
| `750000` | `./Blender_Sunflower_1min_60fps/2sec/chunk_750000bps` | [`Blender_Sunflower_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_750000bps/Blender_Sunflower_1min_60fps_2s.mp4) | 30 | `1–30` | 5.22 MiB | [`Blender_Sunflower_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_750000bps/Blender_Sunflower_1min_60fps_2s1.m4s) | [`Blender_Sunflower_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_750000bps/Blender_Sunflower_1min_60fps_2s30.m4s) |
| `1200000` | `./Blender_Sunflower_1min_60fps/2sec/chunk_1200000bps` | [`Blender_Sunflower_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_1200000bps/Blender_Sunflower_1min_60fps_2s.mp4) | 30 | `1–30` | 8.34 MiB | [`Blender_Sunflower_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_1200000bps/Blender_Sunflower_1min_60fps_2s1.m4s) | [`Blender_Sunflower_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_1200000bps/Blender_Sunflower_1min_60fps_2s30.m4s) |
| `1850000` | `./Blender_Sunflower_1min_60fps/2sec/chunk_1850000bps` | [`Blender_Sunflower_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_1850000bps/Blender_Sunflower_1min_60fps_2s.mp4) | 30 | `1–30` | 12.75 MiB | [`Blender_Sunflower_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_1850000bps/Blender_Sunflower_1min_60fps_2s1.m4s) | [`Blender_Sunflower_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_1850000bps/Blender_Sunflower_1min_60fps_2s30.m4s) |
| `2850000` | `./Blender_Sunflower_1min_60fps/2sec/chunk_2850000bps` | [`Blender_Sunflower_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_2850000bps/Blender_Sunflower_1min_60fps_2s.mp4) | 30 | `1–30` | 19.45 MiB | [`Blender_Sunflower_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_2850000bps/Blender_Sunflower_1min_60fps_2s1.m4s) | [`Blender_Sunflower_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_2850000bps/Blender_Sunflower_1min_60fps_2s30.m4s) |
| `4300000` | `./Blender_Sunflower_1min_60fps/2sec/chunk_4300000bps` | [`Blender_Sunflower_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_4300000bps/Blender_Sunflower_1min_60fps_2s.mp4) | 30 | `1–30` | 28.57 MiB | [`Blender_Sunflower_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_4300000bps/Blender_Sunflower_1min_60fps_2s1.m4s) | [`Blender_Sunflower_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/2sec/chunk_4300000bps/Blender_Sunflower_1min_60fps_2s30.m4s) |

### 6.8. `Blender_Sunflower_1min_60fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Blender_Sunflower_1min_60fps/4sec/Blender_Sunflower_1min_60fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/Blender_Sunflower_1min_60fps_simple_4s.mpd` |
| Título MPD | `Blender_Sunflower_1min_60fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:01:01.401Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.000S` ≈ `60.000` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_4s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `61440` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_60fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_%24Bandwidth%24bps/Blender_Sunflower_1min_60fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Blender_Sunflower_1min_60fps/4sec/chunk_300000bps` | [`Blender_Sunflower_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_300000bps/Blender_Sunflower_1min_60fps_4s.mp4) | 15 | `1–15` | 2.15 MiB | [`Blender_Sunflower_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_300000bps/Blender_Sunflower_1min_60fps_4s1.m4s) | [`Blender_Sunflower_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_300000bps/Blender_Sunflower_1min_60fps_4s15.m4s) |
| `750000` | `./Blender_Sunflower_1min_60fps/4sec/chunk_750000bps` | [`Blender_Sunflower_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_750000bps/Blender_Sunflower_1min_60fps_4s.mp4) | 15 | `1–15` | 5.23 MiB | [`Blender_Sunflower_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_750000bps/Blender_Sunflower_1min_60fps_4s1.m4s) | [`Blender_Sunflower_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_750000bps/Blender_Sunflower_1min_60fps_4s15.m4s) |
| `1200000` | `./Blender_Sunflower_1min_60fps/4sec/chunk_1200000bps` | [`Blender_Sunflower_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_1200000bps/Blender_Sunflower_1min_60fps_4s.mp4) | 15 | `1–15` | 8.35 MiB | [`Blender_Sunflower_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_1200000bps/Blender_Sunflower_1min_60fps_4s1.m4s) | [`Blender_Sunflower_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_1200000bps/Blender_Sunflower_1min_60fps_4s15.m4s) |
| `1850000` | `./Blender_Sunflower_1min_60fps/4sec/chunk_1850000bps` | [`Blender_Sunflower_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_1850000bps/Blender_Sunflower_1min_60fps_4s.mp4) | 15 | `1–15` | 12.77 MiB | [`Blender_Sunflower_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_1850000bps/Blender_Sunflower_1min_60fps_4s1.m4s) | [`Blender_Sunflower_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_1850000bps/Blender_Sunflower_1min_60fps_4s15.m4s) |
| `2850000` | `./Blender_Sunflower_1min_60fps/4sec/chunk_2850000bps` | [`Blender_Sunflower_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_2850000bps/Blender_Sunflower_1min_60fps_4s.mp4) | 15 | `1–15` | 19.46 MiB | [`Blender_Sunflower_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_2850000bps/Blender_Sunflower_1min_60fps_4s1.m4s) | [`Blender_Sunflower_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_2850000bps/Blender_Sunflower_1min_60fps_4s15.m4s) |
| `4300000` | `./Blender_Sunflower_1min_60fps/4sec/chunk_4300000bps` | [`Blender_Sunflower_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_4300000bps/Blender_Sunflower_1min_60fps_4s.mp4) | 15 | `1–15` | 28.58 MiB | [`Blender_Sunflower_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_4300000bps/Blender_Sunflower_1min_60fps_4s1.m4s) | [`Blender_Sunflower_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Blender_Sunflower_1min_60fps/4sec/chunk_4300000bps/Blender_Sunflower_1min_60fps_4s15.m4s) |

### 6.9. `Paseo_Almunecar_10min_30fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_10min_30fps/2sec/Paseo_Almunecar_10min_30fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/Paseo_Almunecar_10min_30fps_simple_2s.mpd` |
| Título MPD | `Paseo_Almunecar_10min_30fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:13:23.933Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M0.100S` ≈ `600.100` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_2s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `30720` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_30fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_30fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_10min_30fps/2sec/chunk_300000bps` | [`Paseo_Almunecar_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_300000bps/Paseo_Almunecar_10min_30fps_2s.mp4) | 301 | `1–301` | 21.64 MiB | [`Paseo_Almunecar_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_300000bps/Paseo_Almunecar_10min_30fps_2s1.m4s) | [`Paseo_Almunecar_10min_30fps_2s301.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_300000bps/Paseo_Almunecar_10min_30fps_2s301.m4s) |
| `750000` | `./Paseo_Almunecar_10min_30fps/2sec/chunk_750000bps` | [`Paseo_Almunecar_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_750000bps/Paseo_Almunecar_10min_30fps_2s.mp4) | 301 | `1–301` | 53.64 MiB | [`Paseo_Almunecar_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_750000bps/Paseo_Almunecar_10min_30fps_2s1.m4s) | [`Paseo_Almunecar_10min_30fps_2s301.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_750000bps/Paseo_Almunecar_10min_30fps_2s301.m4s) |
| `1200000` | `./Paseo_Almunecar_10min_30fps/2sec/chunk_1200000bps` | [`Paseo_Almunecar_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_1200000bps/Paseo_Almunecar_10min_30fps_2s.mp4) | 301 | `1–301` | 85.87 MiB | [`Paseo_Almunecar_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_1200000bps/Paseo_Almunecar_10min_30fps_2s1.m4s) | [`Paseo_Almunecar_10min_30fps_2s301.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_1200000bps/Paseo_Almunecar_10min_30fps_2s301.m4s) |
| `1850000` | `./Paseo_Almunecar_10min_30fps/2sec/chunk_1850000bps` | [`Paseo_Almunecar_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_1850000bps/Paseo_Almunecar_10min_30fps_2s.mp4) | 301 | `1–301` | 132.25 MiB | [`Paseo_Almunecar_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_1850000bps/Paseo_Almunecar_10min_30fps_2s1.m4s) | [`Paseo_Almunecar_10min_30fps_2s301.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_1850000bps/Paseo_Almunecar_10min_30fps_2s301.m4s) |
| `2850000` | `./Paseo_Almunecar_10min_30fps/2sec/chunk_2850000bps` | [`Paseo_Almunecar_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_2850000bps/Paseo_Almunecar_10min_30fps_2s.mp4) | 301 | `1–301` | 203.41 MiB | [`Paseo_Almunecar_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_2850000bps/Paseo_Almunecar_10min_30fps_2s1.m4s) | [`Paseo_Almunecar_10min_30fps_2s301.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_2850000bps/Paseo_Almunecar_10min_30fps_2s301.m4s) |
| `4300000` | `./Paseo_Almunecar_10min_30fps/2sec/chunk_4300000bps` | [`Paseo_Almunecar_10min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_4300000bps/Paseo_Almunecar_10min_30fps_2s.mp4) | 301 | `1–301` | 306.87 MiB | [`Paseo_Almunecar_10min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_4300000bps/Paseo_Almunecar_10min_30fps_2s1.m4s) | [`Paseo_Almunecar_10min_30fps_2s301.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/2sec/chunk_4300000bps/Paseo_Almunecar_10min_30fps_2s301.m4s) |

### 6.10. `Paseo_Almunecar_10min_30fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd` |
| Título MPD | `Paseo_Almunecar_10min_30fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:13:26.511Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M0.100S` ≈ `600.100` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_4s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `61440` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_30fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_30fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_10min_30fps/4sec/chunk_300000bps` | [`Paseo_Almunecar_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_300000bps/Paseo_Almunecar_10min_30fps_4s.mp4) | 151 | `1–151` | 21.68 MiB | [`Paseo_Almunecar_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_300000bps/Paseo_Almunecar_10min_30fps_4s1.m4s) | [`Paseo_Almunecar_10min_30fps_4s151.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_300000bps/Paseo_Almunecar_10min_30fps_4s151.m4s) |
| `750000` | `./Paseo_Almunecar_10min_30fps/4sec/chunk_750000bps` | [`Paseo_Almunecar_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_750000bps/Paseo_Almunecar_10min_30fps_4s.mp4) | 151 | `1–151` | 53.69 MiB | [`Paseo_Almunecar_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_750000bps/Paseo_Almunecar_10min_30fps_4s1.m4s) | [`Paseo_Almunecar_10min_30fps_4s151.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_750000bps/Paseo_Almunecar_10min_30fps_4s151.m4s) |
| `1200000` | `./Paseo_Almunecar_10min_30fps/4sec/chunk_1200000bps` | [`Paseo_Almunecar_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_1200000bps/Paseo_Almunecar_10min_30fps_4s.mp4) | 151 | `1–151` | 85.92 MiB | [`Paseo_Almunecar_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_1200000bps/Paseo_Almunecar_10min_30fps_4s1.m4s) | [`Paseo_Almunecar_10min_30fps_4s151.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_1200000bps/Paseo_Almunecar_10min_30fps_4s151.m4s) |
| `1850000` | `./Paseo_Almunecar_10min_30fps/4sec/chunk_1850000bps` | [`Paseo_Almunecar_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_1850000bps/Paseo_Almunecar_10min_30fps_4s.mp4) | 151 | `1–151` | 132.29 MiB | [`Paseo_Almunecar_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_1850000bps/Paseo_Almunecar_10min_30fps_4s1.m4s) | [`Paseo_Almunecar_10min_30fps_4s151.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_1850000bps/Paseo_Almunecar_10min_30fps_4s151.m4s) |
| `2850000` | `./Paseo_Almunecar_10min_30fps/4sec/chunk_2850000bps` | [`Paseo_Almunecar_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_2850000bps/Paseo_Almunecar_10min_30fps_4s.mp4) | 151 | `1–151` | 203.46 MiB | [`Paseo_Almunecar_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_2850000bps/Paseo_Almunecar_10min_30fps_4s1.m4s) | [`Paseo_Almunecar_10min_30fps_4s151.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_2850000bps/Paseo_Almunecar_10min_30fps_4s151.m4s) |
| `4300000` | `./Paseo_Almunecar_10min_30fps/4sec/chunk_4300000bps` | [`Paseo_Almunecar_10min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_4300000bps/Paseo_Almunecar_10min_30fps_4s.mp4) | 151 | `1–151` | 306.91 MiB | [`Paseo_Almunecar_10min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_4300000bps/Paseo_Almunecar_10min_30fps_4s1.m4s) | [`Paseo_Almunecar_10min_30fps_4s151.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/chunk_4300000bps/Paseo_Almunecar_10min_30fps_4s151.m4s) |

### 6.11. `Paseo_Almunecar_10min_60fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_10min_60fps/2sec/Paseo_Almunecar_10min_60fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/Paseo_Almunecar_10min_60fps_simple_2s.mpd` |
| Título MPD | `Paseo_Almunecar_10min_60fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:48:33.369Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M0.016S` ≈ `600.016` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.002S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60000/1001` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_2s.mp4` |
| `timescale` | `60000` |
| `startNumber` | `1` |
| `duration` | `120000` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_60fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_60fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60000/1001` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60000/1001` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60000/1001` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60000/1001` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60000/1001` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60000/1001` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_10min_60fps/2sec/chunk_300000bps` | [`Paseo_Almunecar_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_300000bps/Paseo_Almunecar_10min_60fps_2s.mp4) | 300 | `1–300` | 21.81 MiB | [`Paseo_Almunecar_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_300000bps/Paseo_Almunecar_10min_60fps_2s1.m4s) | [`Paseo_Almunecar_10min_60fps_2s300.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_300000bps/Paseo_Almunecar_10min_60fps_2s300.m4s) |
| `750000` | `./Paseo_Almunecar_10min_60fps/2sec/chunk_750000bps` | [`Paseo_Almunecar_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_750000bps/Paseo_Almunecar_10min_60fps_2s.mp4) | 300 | `1–300` | 53.96 MiB | [`Paseo_Almunecar_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_750000bps/Paseo_Almunecar_10min_60fps_2s1.m4s) | [`Paseo_Almunecar_10min_60fps_2s300.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_750000bps/Paseo_Almunecar_10min_60fps_2s300.m4s) |
| `1200000` | `./Paseo_Almunecar_10min_60fps/2sec/chunk_1200000bps` | [`Paseo_Almunecar_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_1200000bps/Paseo_Almunecar_10min_60fps_2s.mp4) | 300 | `1–300` | 86.15 MiB | [`Paseo_Almunecar_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_1200000bps/Paseo_Almunecar_10min_60fps_2s1.m4s) | [`Paseo_Almunecar_10min_60fps_2s300.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_1200000bps/Paseo_Almunecar_10min_60fps_2s300.m4s) |
| `1850000` | `./Paseo_Almunecar_10min_60fps/2sec/chunk_1850000bps` | [`Paseo_Almunecar_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_1850000bps/Paseo_Almunecar_10min_60fps_2s.mp4) | 300 | `1–300` | 132.62 MiB | [`Paseo_Almunecar_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_1850000bps/Paseo_Almunecar_10min_60fps_2s1.m4s) | [`Paseo_Almunecar_10min_60fps_2s300.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_1850000bps/Paseo_Almunecar_10min_60fps_2s300.m4s) |
| `2850000` | `./Paseo_Almunecar_10min_60fps/2sec/chunk_2850000bps` | [`Paseo_Almunecar_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_2850000bps/Paseo_Almunecar_10min_60fps_2s.mp4) | 300 | `1–300` | 204.04 MiB | [`Paseo_Almunecar_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_2850000bps/Paseo_Almunecar_10min_60fps_2s1.m4s) | [`Paseo_Almunecar_10min_60fps_2s300.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_2850000bps/Paseo_Almunecar_10min_60fps_2s300.m4s) |
| `4300000` | `./Paseo_Almunecar_10min_60fps/2sec/chunk_4300000bps` | [`Paseo_Almunecar_10min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_4300000bps/Paseo_Almunecar_10min_60fps_2s.mp4) | 300 | `1–300` | 307.78 MiB | [`Paseo_Almunecar_10min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_4300000bps/Paseo_Almunecar_10min_60fps_2s1.m4s) | [`Paseo_Almunecar_10min_60fps_2s300.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/2sec/chunk_4300000bps/Paseo_Almunecar_10min_60fps_2s300.m4s) |

### 6.12. `Paseo_Almunecar_10min_60fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_10min_60fps/4sec/Paseo_Almunecar_10min_60fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/Paseo_Almunecar_10min_60fps_simple_4s.mpd` |
| Título MPD | `Paseo_Almunecar_10min_60fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:48:36.103Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H10M0.016S` ≈ `600.016` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.004S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60000/1001` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_4s.mp4` |
| `timescale` | `60000` |
| `startNumber` | `1` |
| `duration` | `240000` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_60fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_10min_60fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60000/1001` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60000/1001` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60000/1001` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60000/1001` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60000/1001` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60000/1001` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_10min_60fps/4sec/chunk_300000bps` | [`Paseo_Almunecar_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_300000bps/Paseo_Almunecar_10min_60fps_4s.mp4) | 150 | `1–150` | 21.92 MiB | [`Paseo_Almunecar_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_300000bps/Paseo_Almunecar_10min_60fps_4s1.m4s) | [`Paseo_Almunecar_10min_60fps_4s150.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_300000bps/Paseo_Almunecar_10min_60fps_4s150.m4s) |
| `750000` | `./Paseo_Almunecar_10min_60fps/4sec/chunk_750000bps` | [`Paseo_Almunecar_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_750000bps/Paseo_Almunecar_10min_60fps_4s.mp4) | 150 | `1–150` | 54.08 MiB | [`Paseo_Almunecar_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_750000bps/Paseo_Almunecar_10min_60fps_4s1.m4s) | [`Paseo_Almunecar_10min_60fps_4s150.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_750000bps/Paseo_Almunecar_10min_60fps_4s150.m4s) |
| `1200000` | `./Paseo_Almunecar_10min_60fps/4sec/chunk_1200000bps` | [`Paseo_Almunecar_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_1200000bps/Paseo_Almunecar_10min_60fps_4s.mp4) | 150 | `1–150` | 86.27 MiB | [`Paseo_Almunecar_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_1200000bps/Paseo_Almunecar_10min_60fps_4s1.m4s) | [`Paseo_Almunecar_10min_60fps_4s150.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_1200000bps/Paseo_Almunecar_10min_60fps_4s150.m4s) |
| `1850000` | `./Paseo_Almunecar_10min_60fps/4sec/chunk_1850000bps` | [`Paseo_Almunecar_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_1850000bps/Paseo_Almunecar_10min_60fps_4s.mp4) | 150 | `1–150` | 132.73 MiB | [`Paseo_Almunecar_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_1850000bps/Paseo_Almunecar_10min_60fps_4s1.m4s) | [`Paseo_Almunecar_10min_60fps_4s150.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_1850000bps/Paseo_Almunecar_10min_60fps_4s150.m4s) |
| `2850000` | `./Paseo_Almunecar_10min_60fps/4sec/chunk_2850000bps` | [`Paseo_Almunecar_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_2850000bps/Paseo_Almunecar_10min_60fps_4s.mp4) | 150 | `1–150` | 204.15 MiB | [`Paseo_Almunecar_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_2850000bps/Paseo_Almunecar_10min_60fps_4s1.m4s) | [`Paseo_Almunecar_10min_60fps_4s150.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_2850000bps/Paseo_Almunecar_10min_60fps_4s150.m4s) |
| `4300000` | `./Paseo_Almunecar_10min_60fps/4sec/chunk_4300000bps` | [`Paseo_Almunecar_10min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_4300000bps/Paseo_Almunecar_10min_60fps_4s.mp4) | 150 | `1–150` | 307.90 MiB | [`Paseo_Almunecar_10min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_4300000bps/Paseo_Almunecar_10min_60fps_4s1.m4s) | [`Paseo_Almunecar_10min_60fps_4s150.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_10min_60fps/4sec/chunk_4300000bps/Paseo_Almunecar_10min_60fps_4s150.m4s) |

### 6.13. `Paseo_Almunecar_1min_30fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_1min_30fps/2sec/Paseo_Almunecar_1min_30fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/Paseo_Almunecar_1min_30fps_simple_2s.mpd` |
| Título MPD | `Paseo_Almunecar_1min_30fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:49:51.785Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.000S` ≈ `60.000` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_2s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `30720` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_30fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_30fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_1min_30fps/2sec/chunk_300000bps` | [`Paseo_Almunecar_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_300000bps/Paseo_Almunecar_1min_30fps_2s.mp4) | 30 | `1–30` | 2.19 MiB | [`Paseo_Almunecar_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_300000bps/Paseo_Almunecar_1min_30fps_2s1.m4s) | [`Paseo_Almunecar_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_300000bps/Paseo_Almunecar_1min_30fps_2s30.m4s) |
| `750000` | `./Paseo_Almunecar_1min_30fps/2sec/chunk_750000bps` | [`Paseo_Almunecar_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_750000bps/Paseo_Almunecar_1min_30fps_2s.mp4) | 30 | `1–30` | 5.42 MiB | [`Paseo_Almunecar_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_750000bps/Paseo_Almunecar_1min_30fps_2s1.m4s) | [`Paseo_Almunecar_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_750000bps/Paseo_Almunecar_1min_30fps_2s30.m4s) |
| `1200000` | `./Paseo_Almunecar_1min_30fps/2sec/chunk_1200000bps` | [`Paseo_Almunecar_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_1200000bps/Paseo_Almunecar_1min_30fps_2s.mp4) | 30 | `1–30` | 8.65 MiB | [`Paseo_Almunecar_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_1200000bps/Paseo_Almunecar_1min_30fps_2s1.m4s) | [`Paseo_Almunecar_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_1200000bps/Paseo_Almunecar_1min_30fps_2s30.m4s) |
| `1850000` | `./Paseo_Almunecar_1min_30fps/2sec/chunk_1850000bps` | [`Paseo_Almunecar_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_1850000bps/Paseo_Almunecar_1min_30fps_2s.mp4) | 30 | `1–30` | 13.31 MiB | [`Paseo_Almunecar_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_1850000bps/Paseo_Almunecar_1min_30fps_2s1.m4s) | [`Paseo_Almunecar_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_1850000bps/Paseo_Almunecar_1min_30fps_2s30.m4s) |
| `2850000` | `./Paseo_Almunecar_1min_30fps/2sec/chunk_2850000bps` | [`Paseo_Almunecar_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_2850000bps/Paseo_Almunecar_1min_30fps_2s.mp4) | 30 | `1–30` | 20.46 MiB | [`Paseo_Almunecar_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_2850000bps/Paseo_Almunecar_1min_30fps_2s1.m4s) | [`Paseo_Almunecar_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_2850000bps/Paseo_Almunecar_1min_30fps_2s30.m4s) |
| `4300000` | `./Paseo_Almunecar_1min_30fps/2sec/chunk_4300000bps` | [`Paseo_Almunecar_1min_30fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_4300000bps/Paseo_Almunecar_1min_30fps_2s.mp4) | 30 | `1–30` | 30.97 MiB | [`Paseo_Almunecar_1min_30fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_4300000bps/Paseo_Almunecar_1min_30fps_2s1.m4s) | [`Paseo_Almunecar_1min_30fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/2sec/chunk_4300000bps/Paseo_Almunecar_1min_30fps_2s30.m4s) |

### 6.14. `Paseo_Almunecar_1min_30fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd` |
| Título MPD | `Paseo_Almunecar_1min_30fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:49:52.483Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.000S` ≈ `60.000` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.000S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `30` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s.mp4` |
| `timescale` | `15360` |
| `startNumber` | `1` |
| `duration` | `61440` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_30fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_30fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `30` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `30` | `avc1.64001F` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `30` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `30` | `avc1.64001E` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `30` | `avc1.640015` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `30` | `avc1.64000C` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_1min_30fps/4sec/chunk_300000bps` | [`Paseo_Almunecar_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_300000bps/Paseo_Almunecar_1min_30fps_4s.mp4) | 15 | `1–15` | 2.19 MiB | [`Paseo_Almunecar_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_300000bps/Paseo_Almunecar_1min_30fps_4s1.m4s) | [`Paseo_Almunecar_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_300000bps/Paseo_Almunecar_1min_30fps_4s15.m4s) |
| `750000` | `./Paseo_Almunecar_1min_30fps/4sec/chunk_750000bps` | [`Paseo_Almunecar_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_750000bps/Paseo_Almunecar_1min_30fps_4s.mp4) | 15 | `1–15` | 5.42 MiB | [`Paseo_Almunecar_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_750000bps/Paseo_Almunecar_1min_30fps_4s1.m4s) | [`Paseo_Almunecar_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_750000bps/Paseo_Almunecar_1min_30fps_4s15.m4s) |
| `1200000` | `./Paseo_Almunecar_1min_30fps/4sec/chunk_1200000bps` | [`Paseo_Almunecar_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_1200000bps/Paseo_Almunecar_1min_30fps_4s.mp4) | 15 | `1–15` | 8.65 MiB | [`Paseo_Almunecar_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_1200000bps/Paseo_Almunecar_1min_30fps_4s1.m4s) | [`Paseo_Almunecar_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_1200000bps/Paseo_Almunecar_1min_30fps_4s15.m4s) |
| `1850000` | `./Paseo_Almunecar_1min_30fps/4sec/chunk_1850000bps` | [`Paseo_Almunecar_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_1850000bps/Paseo_Almunecar_1min_30fps_4s.mp4) | 15 | `1–15` | 13.32 MiB | [`Paseo_Almunecar_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_1850000bps/Paseo_Almunecar_1min_30fps_4s1.m4s) | [`Paseo_Almunecar_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_1850000bps/Paseo_Almunecar_1min_30fps_4s15.m4s) |
| `2850000` | `./Paseo_Almunecar_1min_30fps/4sec/chunk_2850000bps` | [`Paseo_Almunecar_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_2850000bps/Paseo_Almunecar_1min_30fps_4s.mp4) | 15 | `1–15` | 20.47 MiB | [`Paseo_Almunecar_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_2850000bps/Paseo_Almunecar_1min_30fps_4s1.m4s) | [`Paseo_Almunecar_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_2850000bps/Paseo_Almunecar_1min_30fps_4s15.m4s) |
| `4300000` | `./Paseo_Almunecar_1min_30fps/4sec/chunk_4300000bps` | [`Paseo_Almunecar_1min_30fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_4300000bps/Paseo_Almunecar_1min_30fps_4s.mp4) | 15 | `1–15` | 30.98 MiB | [`Paseo_Almunecar_1min_30fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_4300000bps/Paseo_Almunecar_1min_30fps_4s1.m4s) | [`Paseo_Almunecar_1min_30fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/chunk_4300000bps/Paseo_Almunecar_1min_30fps_4s15.m4s) |

### 6.15. `Paseo_Almunecar_1min_60fps_simple_2s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_1min_60fps/2sec/Paseo_Almunecar_1min_60fps_simple_2s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/Paseo_Almunecar_1min_60fps_simple_2s.mpd` |
| Título MPD | `Paseo_Almunecar_1min_60fps_simple_2s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:51:45.302Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.009S` ≈ `60.009` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M2.002S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60000/1001` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_2s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_2s.mp4` |
| `timescale` | `60000` |
| `startNumber` | `1` |
| `duration` | `120000` |
| Duración calculada por segmento | `2.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_60fps_2s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_60fps_2s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60000/1001` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60000/1001` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60000/1001` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60000/1001` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60000/1001` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60000/1001` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_1min_60fps/2sec/chunk_300000bps` | [`Paseo_Almunecar_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_300000bps/Paseo_Almunecar_1min_60fps_2s.mp4) | 30 | `1–30` | 2.20 MiB | [`Paseo_Almunecar_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_300000bps/Paseo_Almunecar_1min_60fps_2s1.m4s) | [`Paseo_Almunecar_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_300000bps/Paseo_Almunecar_1min_60fps_2s30.m4s) |
| `750000` | `./Paseo_Almunecar_1min_60fps/2sec/chunk_750000bps` | [`Paseo_Almunecar_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_750000bps/Paseo_Almunecar_1min_60fps_2s.mp4) | 30 | `1–30` | 5.44 MiB | [`Paseo_Almunecar_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_750000bps/Paseo_Almunecar_1min_60fps_2s1.m4s) | [`Paseo_Almunecar_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_750000bps/Paseo_Almunecar_1min_60fps_2s30.m4s) |
| `1200000` | `./Paseo_Almunecar_1min_60fps/2sec/chunk_1200000bps` | [`Paseo_Almunecar_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_1200000bps/Paseo_Almunecar_1min_60fps_2s.mp4) | 30 | `1–30` | 8.70 MiB | [`Paseo_Almunecar_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_1200000bps/Paseo_Almunecar_1min_60fps_2s1.m4s) | [`Paseo_Almunecar_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_1200000bps/Paseo_Almunecar_1min_60fps_2s30.m4s) |
| `1850000` | `./Paseo_Almunecar_1min_60fps/2sec/chunk_1850000bps` | [`Paseo_Almunecar_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_1850000bps/Paseo_Almunecar_1min_60fps_2s.mp4) | 30 | `1–30` | 13.38 MiB | [`Paseo_Almunecar_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_1850000bps/Paseo_Almunecar_1min_60fps_2s1.m4s) | [`Paseo_Almunecar_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_1850000bps/Paseo_Almunecar_1min_60fps_2s30.m4s) |
| `2850000` | `./Paseo_Almunecar_1min_60fps/2sec/chunk_2850000bps` | [`Paseo_Almunecar_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_2850000bps/Paseo_Almunecar_1min_60fps_2s.mp4) | 30 | `1–30` | 20.59 MiB | [`Paseo_Almunecar_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_2850000bps/Paseo_Almunecar_1min_60fps_2s1.m4s) | [`Paseo_Almunecar_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_2850000bps/Paseo_Almunecar_1min_60fps_2s30.m4s) |
| `4300000` | `./Paseo_Almunecar_1min_60fps/2sec/chunk_4300000bps` | [`Paseo_Almunecar_1min_60fps_2s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_4300000bps/Paseo_Almunecar_1min_60fps_2s.mp4) | 30 | `1–30` | 31.10 MiB | [`Paseo_Almunecar_1min_60fps_2s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_4300000bps/Paseo_Almunecar_1min_60fps_2s1.m4s) | [`Paseo_Almunecar_1min_60fps_2s30.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/2sec/chunk_4300000bps/Paseo_Almunecar_1min_60fps_2s30.m4s) |

### 6.16. `Paseo_Almunecar_1min_60fps_simple_4s.mpd`

| Campo | Valor |
|---|---|
| Ruta relativa | `./Paseo_Almunecar_1min_60fps/4sec/Paseo_Almunecar_1min_60fps_simple_4s.mpd` |
| URL MPD | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/Paseo_Almunecar_1min_60fps_simple_4s.mpd` |
| Título MPD | `Paseo_Almunecar_1min_60fps_simple_4s.mpd generated by GPAC` |
| Comentario de generación | `MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:51:46.053Z` |
| Tipo MPD | `static` |
| Perfil DASH | `urn:mpeg:dash:profile:isoff-live:2011` |
| Duración de presentación | `PT0H1M0.009S` ≈ `60.009` s |
| `minBufferTime` | `PT1.500S` |
| `maxSegmentDuration` | `PT0H0M4.004S` |
| Mime type | `video/mp4` |
| Resolución máxima del AdaptationSet | `1920x1080` |
| FPS máximo del AdaptationSet | `60000/1001` |
| `segmentAlignment` | `true` |
| `startWithSAP` | `1` |

**SegmentTemplate**

| Campo | Valor |
|---|---|
| `media` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_4s$Number$.m4s` |
| `initialization` | `chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_4s.mp4` |
| `timescale` | `60000` |
| `startNumber` | `1` |
| `duration` | `240000` |
| Duración calculada por segmento | `4.000` s (`duration / timescale`) |
| Plantilla absoluta de segmentos | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_60fps_4s%24Number%24.m4s` |
| Plantilla absoluta de inicialización | `http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_%24Bandwidth%24bps/Paseo_Almunecar_1min_60fps_4s.mp4` |

**Representations declaradas en el MPD**

| id | bandwidth | Mbps aprox. | resolución | frameRate | codecs | SAR |
|---:|---:|---:|---:|---:|---|---|
| `1` | `4300000` | `4.30` | `1920x1080` | `60000/1001` | `avc1.640032` | `1:1` |
| `2` | `2850000` | `2.85` | `1280x720` | `60000/1001` | `avc1.640020` | `1:1` |
| `3` | `1850000` | `1.85` | `854x480` | `60000/1001` | `avc1.64001F` | `1280:1281` |
| `4` | `1200000` | `1.20` | `640x360` | `60000/1001` | `avc1.64001F` | `1:1` |
| `5` | `750000` | `0.75` | `426x240` | `60000/1001` | `avc1.64001E` | `640:639` |
| `6` | `300000` | `0.30` | `256x144` | `60000/1001` | `avc1.64000D` | `1:1` |

**Segmentos físicos detectados por bitrate**

| bandwidth | carpeta | init `.mp4` | segmentos `.m4s` | rango numérico | tamaño total aprox. | ejemplo primer segmento | ejemplo último segmento |
|---:|---|---|---:|---:|---:|---|---|
| `300000` | `./Paseo_Almunecar_1min_60fps/4sec/chunk_300000bps` | [`Paseo_Almunecar_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_300000bps/Paseo_Almunecar_1min_60fps_4s.mp4) | 15 | `1–15` | 2.21 MiB | [`Paseo_Almunecar_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_300000bps/Paseo_Almunecar_1min_60fps_4s1.m4s) | [`Paseo_Almunecar_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_300000bps/Paseo_Almunecar_1min_60fps_4s15.m4s) |
| `750000` | `./Paseo_Almunecar_1min_60fps/4sec/chunk_750000bps` | [`Paseo_Almunecar_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_750000bps/Paseo_Almunecar_1min_60fps_4s.mp4) | 15 | `1–15` | 5.45 MiB | [`Paseo_Almunecar_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_750000bps/Paseo_Almunecar_1min_60fps_4s1.m4s) | [`Paseo_Almunecar_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_750000bps/Paseo_Almunecar_1min_60fps_4s15.m4s) |
| `1200000` | `./Paseo_Almunecar_1min_60fps/4sec/chunk_1200000bps` | [`Paseo_Almunecar_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_1200000bps/Paseo_Almunecar_1min_60fps_4s.mp4) | 15 | `1–15` | 8.71 MiB | [`Paseo_Almunecar_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_1200000bps/Paseo_Almunecar_1min_60fps_4s1.m4s) | [`Paseo_Almunecar_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_1200000bps/Paseo_Almunecar_1min_60fps_4s15.m4s) |
| `1850000` | `./Paseo_Almunecar_1min_60fps/4sec/chunk_1850000bps` | [`Paseo_Almunecar_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_1850000bps/Paseo_Almunecar_1min_60fps_4s.mp4) | 15 | `1–15` | 13.39 MiB | [`Paseo_Almunecar_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_1850000bps/Paseo_Almunecar_1min_60fps_4s1.m4s) | [`Paseo_Almunecar_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_1850000bps/Paseo_Almunecar_1min_60fps_4s15.m4s) |
| `2850000` | `./Paseo_Almunecar_1min_60fps/4sec/chunk_2850000bps` | [`Paseo_Almunecar_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_2850000bps/Paseo_Almunecar_1min_60fps_4s.mp4) | 15 | `1–15` | 20.60 MiB | [`Paseo_Almunecar_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_2850000bps/Paseo_Almunecar_1min_60fps_4s1.m4s) | [`Paseo_Almunecar_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_2850000bps/Paseo_Almunecar_1min_60fps_4s15.m4s) |
| `4300000` | `./Paseo_Almunecar_1min_60fps/4sec/chunk_4300000bps` | [`Paseo_Almunecar_1min_60fps_4s.mp4`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_4300000bps/Paseo_Almunecar_1min_60fps_4s.mp4) | 15 | `1–15` | 31.11 MiB | [`Paseo_Almunecar_1min_60fps_4s1.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_4300000bps/Paseo_Almunecar_1min_60fps_4s1.m4s) | [`Paseo_Almunecar_1min_60fps_4s15.m4s`](http://192.168.1.132/dash/Paseo_Almunecar_1min_60fps/4sec/chunk_4300000bps/Paseo_Almunecar_1min_60fps_4s15.m4s) |

## 7. Contenido XML completo de cada MPD

Los siguientes bloques conservan el contenido XML de los MPD tal como aparece en `contenido_mpd_todos.txt`. No se han reindentado ni reescrito.

### 7.1. `./Blender_Sunflower_10min_30fps/2sec/Blender_Sunflower_10min_30fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:29:11.023Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M34.600S" maxSegmentDuration="PT0H0M2.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_10min_30fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M34.600S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_2s.mp4" timescale="15360" startNumber="1" duration="30720"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.2. `./Blender_Sunflower_10min_30fps/4sec/Blender_Sunflower_10min_30fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:29:13.143Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M34.600S" maxSegmentDuration="PT0H0M4.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_10min_30fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M34.600S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_10min_30fps_4s.mp4" timescale="15360" startNumber="1" duration="61440"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.3. `./Blender_Sunflower_10min_60fps/2sec/Blender_Sunflower_10min_60fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:58:09.939Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M34.566S" maxSegmentDuration="PT0H0M2.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_10min_60fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M34.566S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_2s.mp4" timescale="15360" startNumber="1" duration="30720"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.4. `./Blender_Sunflower_10min_60fps/4sec/Blender_Sunflower_10min_60fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:58:12.519Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M34.566S" maxSegmentDuration="PT0H0M4.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_10min_60fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M34.566S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_10min_60fps_4s.mp4" timescale="15360" startNumber="1" duration="61440"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.5. `./Blender_Sunflower_1min_30fps/2sec/Blender_Sunflower_1min_30fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:59:19.392Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.000S" maxSegmentDuration="PT0H0M2.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_1min_30fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.000S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_2s.mp4" timescale="15360" startNumber="1" duration="30720"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.6. `./Blender_Sunflower_1min_30fps/4sec/Blender_Sunflower_1min_30fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T11:59:20.102Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.000S" maxSegmentDuration="PT0H0M4.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_1min_30fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.000S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_1min_30fps_4s.mp4" timescale="15360" startNumber="1" duration="61440"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.7. `./Blender_Sunflower_1min_60fps/2sec/Blender_Sunflower_1min_60fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:01:00.681Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.000S" maxSegmentDuration="PT0H0M2.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_1min_60fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.000S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_2s.mp4" timescale="15360" startNumber="1" duration="30720"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.8. `./Blender_Sunflower_1min_60fps/4sec/Blender_Sunflower_1min_60fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:01:01.401Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.000S" maxSegmentDuration="PT0H0M4.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Blender_Sunflower_1min_60fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.000S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Blender_Sunflower_1min_60fps_4s.mp4" timescale="15360" startNumber="1" duration="61440"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.9. `./Paseo_Almunecar_10min_30fps/2sec/Paseo_Almunecar_10min_30fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:13:23.933Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M0.100S" maxSegmentDuration="PT0H0M2.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_10min_30fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M0.100S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_2s.mp4" timescale="15360" startNumber="1" duration="30720"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.10. `./Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:13:26.511Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M0.100S" maxSegmentDuration="PT0H0M4.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_10min_30fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M0.100S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_30fps_4s.mp4" timescale="15360" startNumber="1" duration="61440"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.11. `./Paseo_Almunecar_10min_60fps/2sec/Paseo_Almunecar_10min_60fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:48:33.369Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M0.016S" maxSegmentDuration="PT0H0M2.002S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_10min_60fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M0.016S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60000/1001" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_2s.mp4" timescale="60000" startNumber="1" duration="120000"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60000/1001" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60000/1001" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60000/1001" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60000/1001" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60000/1001" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60000/1001" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.12. `./Paseo_Almunecar_10min_60fps/4sec/Paseo_Almunecar_10min_60fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:48:36.103Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H10M0.016S" maxSegmentDuration="PT0H0M4.004S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_10min_60fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H10M0.016S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60000/1001" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_10min_60fps_4s.mp4" timescale="60000" startNumber="1" duration="240000"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60000/1001" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60000/1001" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60000/1001" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60000/1001" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60000/1001" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60000/1001" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.13. `./Paseo_Almunecar_1min_30fps/2sec/Paseo_Almunecar_1min_30fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:49:51.785Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.000S" maxSegmentDuration="PT0H0M2.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_1min_30fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.000S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_2s.mp4" timescale="15360" startNumber="1" duration="30720"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.14. `./Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:49:52.483Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.000S" maxSegmentDuration="PT0H0M4.000S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_1min_30fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.000S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="30" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s.mp4" timescale="15360" startNumber="1" duration="61440"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="30" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.64001F" width="1280" height="720" frameRate="30" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="30" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001E" width="640" height="360" frameRate="30" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.640015" width="426" height="240" frameRate="30" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000C" width="256" height="144" frameRate="30" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.15. `./Paseo_Almunecar_1min_60fps/2sec/Paseo_Almunecar_1min_60fps_simple_2s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:51:45.302Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.009S" maxSegmentDuration="PT0H0M2.002S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_1min_60fps_simple_2s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.009S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60000/1001" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_2s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_2s.mp4" timescale="60000" startNumber="1" duration="120000"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60000/1001" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60000/1001" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60000/1001" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60000/1001" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60000/1001" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60000/1001" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

### 7.16. `./Paseo_Almunecar_1min_60fps/4sec/Paseo_Almunecar_1min_60fps_simple_4s.mpd`

```xml
<?xml version="1.0"?>
<!-- MPD file Generated with GPAC version 2.5-DEV-revUNKNOWN-master at 2026-02-17T12:51:46.053Z -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" minBufferTime="PT1.500S" type="static" mediaPresentationDuration="PT0H1M0.009S" maxSegmentDuration="PT0H0M4.004S" profiles="urn:mpeg:dash:profile:isoff-live:2011">
 <ProgramInformation moreInformationURL="https://gpac.io">
  <Title>Paseo_Almunecar_1min_60fps_simple_4s.mpd generated by GPAC</Title>
 </ProgramInformation>

 <Period duration="PT0H1M0.009S">
  <AdaptationSet segmentAlignment="true" maxWidth="1920" maxHeight="1080" maxFrameRate="60000/1001" par="16:9" mimeType="video/mp4" startWithSAP="1">
   <SegmentTemplate media="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_4s$Number$.m4s" initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_60fps_4s.mp4" timescale="60000" startNumber="1" duration="240000"/>
   <Representation id="1" codecs="avc1.640032" width="1920" height="1080" frameRate="60000/1001" sar="1:1" bandwidth="4300000">
   </Representation>
   <Representation id="2" codecs="avc1.640020" width="1280" height="720" frameRate="60000/1001" sar="1:1" bandwidth="2850000">
   </Representation>
   <Representation id="3" codecs="avc1.64001F" width="854" height="480" frameRate="60000/1001" sar="1280:1281" bandwidth="1850000">
   </Representation>
   <Representation id="4" codecs="avc1.64001F" width="640" height="360" frameRate="60000/1001" sar="1:1" bandwidth="1200000">
   </Representation>
   <Representation id="5" codecs="avc1.64001E" width="426" height="240" frameRate="60000/1001" sar="640:639" bandwidth="750000">
   </Representation>
   <Representation id="6" codecs="avc1.64000D" width="256" height="144" frameRate="60000/1001" sar="1:1" bandwidth="300000">
   </Representation>
  </AdaptationSet>
 </Period>
</MPD>
```

## 8. Script automático recomendado para Ubuntu

Este script regenera el inventario desde la VM servidor leyendo directamente `/var/www/html/dash`. No depende de los TXT intermedios y evita tocar o modificar los MPD/segmentos.

Uso recomendado dentro de la VM Ubuntu:

```bash
cd /var/www/html/dash
nano generate_dash_inventory_md.sh
# pega el script
chmod +x generate_dash_inventory_md.sh
./generate_dash_inventory_md.sh /var/www/html/dash 192.168.1.132 dash_inventory.md
```

El resultado quedará en:

```bash
/var/www/html/dash/dash_inventory.md
```

```bash
#!/usr/bin/env bash
set -euo pipefail

WEB_ROOT="${1:-/var/www/html/dash}"
SERVER_IP="${2:-$(hostname -I | awk '{print $1}')}"
OUTPUT_NAME="${3:-dash_inventory.md}"
BASE_URL="http://${SERVER_IP}/dash"
OUTPUT_PATH="${WEB_ROOT%/}/${OUTPUT_NAME}"

python3 - "$WEB_ROOT" "$BASE_URL" "$OUTPUT_PATH" <<'PYGEN'
from pathlib import Path
import sys, re
import xml.etree.ElementTree as ET
from urllib.parse import quote
from datetime import datetime
from collections import defaultdict

web_root = Path(sys.argv[1]).resolve()
base_url = sys.argv[2].rstrip('/')
out_path = Path(sys.argv[3])
ns = {'m': 'urn:mpeg:dash:schema:mpd:2011'}

def human_size(n):
    n = float(n)
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    for u in units:
        if n < 1024 or u == units[-1]:
            if u == 'B': return f'{int(n)} {u}'
            return f'{n:.2f} {u}'
        n /= 1024

def rel_to_url(path):
    rel = Path(path).resolve().relative_to(web_root).as_posix()
    return base_url + '/' + '/'.join(quote(p) for p in rel.split('/'))

def parse_iso_duration_to_seconds(s):
    if not s or not s.startswith('P'):
        return None
    m = re.match(r'P(?:([0-9.]+)D)?T?(?:([0-9.]+)H)?(?:([0-9.]+)M)?(?:([0-9.]+)S)?', s)
    if not m:
        return None
    days, hours, mins, secs = [float(x) if x else 0.0 for x in m.groups()]
    return days*86400 + hours*3600 + mins*60 + secs

mpd_paths = sorted(web_root.rglob('*.mpd'))
all_files = [p for p in web_root.rglob('*') if p.is_file()]
all_dirs = [p for p in web_root.rglob('*') if p.is_dir()]
source_videos = sorted([p for p in all_files if p.suffix == '.mp4' and p.parent.parent == web_root])
rep_videos = sorted([p for p in all_files if p.suffix == '.mp4' and '/_reps_' in p.as_posix()])
m4s_files = sorted([p for p in all_files if p.suffix == '.m4s'])
init_mp4 = sorted([p for p in all_files if p.suffix == '.mp4' and '/chunk_' in p.as_posix()])

chunk_summaries = []
for d in sorted([p for p in all_dirs if re.search(r'chunk_\d+bps$', p.name)]):
    children = [p for p in d.iterdir() if p.is_file()]
    m4s = [p for p in children if p.suffix == '.m4s']
    init = [p for p in children if p.suffix == '.mp4']
    nums = []
    for p in m4s:
        m = re.search(r'(\d+)\.m4s$', p.name)
        if m: nums.append(int(m.group(1)))
    bw = int(re.search(r'chunk_(\d+)bps', d.name).group(1))
    chunk_summaries.append({
        'dir': d,
        'bandwidth': bw,
        'm4s_count': len(m4s),
        'first_number': min(nums) if nums else None,
        'last_number': max(nums) if nums else None,
        'init_name': init[0].name if init else '',
        'total_size': sum(p.stat().st_size for p in children),
    })
chunk_by_parent = defaultdict(list)
for c in chunk_summaries:
    chunk_by_parent[c['dir'].parent].append(c)

blocks = []
for mpd in mpd_paths:
    raw = mpd.read_text(errors='replace')
    root = ET.fromstring(raw)
    period = root.find('.//m:Period', ns)
    adaptation = root.find('.//m:AdaptationSet', ns)
    seg_template = root.find('.//m:SegmentTemplate', ns)
    title_el = root.find('.//m:Title', ns)
    reps = [r.attrib for r in root.findall('.//m:Representation', ns)]
    st = seg_template.attrib if seg_template is not None else {}
    ad = adaptation.attrib if adaptation is not None else {}
    attrs = root.attrib
    seg_seconds = None
    try:
        seg_seconds = float(st['duration']) / float(st['timescale'])
    except Exception:
        pass
    blocks.append({
        'path': mpd,
        'rel': './' + mpd.relative_to(web_root).as_posix(),
        'url': rel_to_url(mpd),
        'xml': raw.strip(),
        'title': title_el.text if title_el is not None else '',
        'attrs': attrs,
        'period': period.attrib if period is not None else {},
        'adaptation': ad,
        'segment_template': st,
        'representations': reps,
        'duration_seconds': parse_iso_duration_to_seconds(attrs.get('mediaPresentationDuration', '')),
        'segment_seconds': seg_seconds,
        'chunks': sorted(chunk_by_parent[mpd.parent], key=lambda x: x['bandwidth']),
    })

ladder = sorted({int(r['bandwidth']) for b in blocks for r in b['representations'] if 'bandwidth' in r})

lines = []
lines.append('# Inventario automático de la VM Ubuntu del servidor DASH')
lines.append('')
lines.append(f'- Generado: `{datetime.now().isoformat(timespec="seconds")}`')
lines.append(f'- Directorio Ubuntu: `{web_root}`')
lines.append(f'- URL base: `{base_url}/`')
lines.append('')
lines.append('## Resumen')
lines.append('')
lines.append('| Elemento | Valor |')
lines.append('|---|---:|')
lines.append(f'| MPD | {len(blocks)} |')
lines.append(f'| Carpetas chunk_*bps | {len(chunk_summaries)} |')
lines.append(f'| Segmentos .m4s | {len(m4s_files)} |')
lines.append(f'| Inicializaciones .mp4 en chunks | {len(init_mp4)} |')
lines.append(f'| Vídeos fuente principales | {len(source_videos)} |')
lines.append(f'| Vídeos intermedios _reps_* | {len(rep_videos)} |')
lines.append(f'| Tamaño total ficheros | {human_size(sum(p.stat().st_size for p in all_files))} |')
lines.append('')
lines.append('## URLs de MPD')
lines.append('')
lines.append('| # | MPD | Duración | Segmento máximo | FPS | URL |')
lines.append('|---:|---|---:|---:|---:|---|')
for i,b in enumerate(blocks,1):
    lines.append(f'| {i} | `{b["rel"]}` | `{b["attrs"].get("mediaPresentationDuration","")}` | `{b["attrs"].get("maxSegmentDuration","")}` | `{b["adaptation"].get("maxFrameRate","")}` | `{b["url"]}` |')
lines.append('')
lines.append('## Escalera de bitrates detectada')
lines.append('')
lines.append('| Orden | Bandwidth | Mbps aprox. |')
lines.append('|---:|---:|---:|')
for i,bw in enumerate(ladder,1):
    lines.append(f'| {i} | `{bw}` | `{bw/1_000_000:.2f}` |')
lines.append('')
lines.append('## Inventario por MPD')
lines.append('')
for i,b in enumerate(blocks,1):
    st=b['segment_template']
    lines.append(f'### {i}. `{b["rel"]}`')
    lines.append('')
    lines.append(f'- URL: `{b["url"]}`')
    lines.append(f'- Media template: `{st.get("media","")}`')
    lines.append(f'- Init template: `{st.get("initialization","")}`')
    if b['segment_seconds'] is not None:
        lines.append(f'- Duración calculada por segmento: `{b["segment_seconds"]:.3f}` s')
    lines.append('')
    lines.append('| id | bandwidth | resolución | frameRate | codecs | SAR |')
    lines.append('|---:|---:|---:|---:|---|---|')
    for r in sorted(b['representations'], key=lambda x: int(x.get('bandwidth',0)), reverse=True):
        lines.append(f'| `{r.get("id","")}` | `{r.get("bandwidth","")}` | `{r.get("width","")}x{r.get("height","")}` | `{r.get("frameRate","")}` | `{r.get("codecs","")}` | `{r.get("sar","")}` |')
    lines.append('')
    lines.append('| bandwidth | carpeta | init | segmentos | rango | tamaño |')
    lines.append('|---:|---|---|---:|---:|---:|')
    for c in b['chunks']:
        rel_dir = './' + c['dir'].relative_to(web_root).as_posix()
        rng = f'{c["first_number"]}–{c["last_number"]}' if c['first_number'] is not None else ''
        lines.append(f'| `{c["bandwidth"]}` | `{rel_dir}` | `{c["init_name"]}` | {c["m4s_count"]} | `{rng}` | {human_size(c["total_size"])} |')
    lines.append('')
    lines.append('```xml')
    lines.append(b['xml'])
    lines.append('```')
    lines.append('')

out_path.write_text('\n'.join(lines), encoding='utf-8')
print(f'Inventario generado: {out_path}')
PYGEN
```

## 9. Notas para el TFG

- Para las pruebas ABR, los campos más importantes son la URL del MPD, la escalera `bandwidth`, la duración de segmento y las plantillas `SegmentTemplate`.
- Las URLs de segmentos no necesitan enumerarse una a una: el cliente DASH las deriva sustituyendo `$Bandwidth$` y `$Number$` en la plantilla del MPD.
- Si cambia la IP de la VM, no cambian los MPD ni los segmentos: solo cambia la parte inicial de la URL, es decir, `http://IP/dash/...`.
- Si regeneras el contenido DASH o añades vídeos, vuelve a ejecutar el script y tendrás un inventario actualizado.
