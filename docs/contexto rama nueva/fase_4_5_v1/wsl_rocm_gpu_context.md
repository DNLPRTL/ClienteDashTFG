# WSL2 ROCm GPU context

## Estado observado

El 2026-06-09 Daniel preparo WSL2 para entrenamiento IA con GPU AMD.

Resumen operativo extraido del log local:

```text
WSL distro: Ubuntu-24.04
Ubuntu: 24.04.4 LTS
Kernel: microsoft-standard-WSL2
GPU bridge: /dev/dxg presente
ROCm tool: /opt/rocm/bin/rocminfo
GPU detectada por rocminfo: AMD Radeon RX 7800 XT
GPU ISA: gfx1101 / gfx11-generic
Venv: ~/venvs/rocm721
Python WSL: 3.12.3
PyTorch: 2.9.1+rocm7.2.1
Torch CUDA API sobre ROCm: disponible
```

Comprobaciones realizadas en el log:

```bash
python3 -c "import torch; print(torch.__version__)"
python3 -c "import torch; print(torch.cuda.is_available())"
python3 -c "import torch; print(torch.cuda.get_device_name(0))"
```

Salida observada:

```text
2.9.1+rocm7.2.1.gitff65f5bc
True
AMD Radeon RX 7800 XT
```

Tambien se ejecuto un producto matricial en GPU con tensores `4096 x 4096` en
`cuda:0`, finalizando correctamente.

## Rol dentro del proyecto

WSL2/ROCm queda autorizado como entorno de entrenamiento IA pesado para Fase
4-5 v1 y futuras iteraciones de modelos.

No cambia estas responsabilidades:

- Windows fisico sigue siendo el entorno principal de Codex para desarrollar,
  testear rapido, commitear y pushear.
- WSL2 entrena modelos y genera artefactos pesados.
- Ubuntu cliente ejecuta validaciones reales y Phase 6.
- Ubuntu servidor solo sirve contenido DASH por HTTP.

## Rutas recomendadas

Dentro de WSL2 usar rutas Linux:

```bash
~/TFG/DashClientModular4
~/TFG/datasets_normalizados
~/TFG/manifests_trazas
~/TFG/runs_trazas
~/TFG/auditorias_trazas
~/TFG/modelos
```

Evitar como ruta principal:

```bash
/mnt/c/Users/danie/Documents/TFG/...
```

`/mnt/c/...` puede servir para consultar o copiar puntualmente, pero no para
entrenar ni mover grandes cantidades de datos.

Usar `~` en runbooks para evitar confusiones si el usuario WSL real es
`/home/danie` en vez de `/home/daniel`.

## Primer clonado del repo en WSL2

```bash
wsl -d Ubuntu-24.04
cd ~
mkdir -p ~/TFG
cd ~/TFG
git clone https://github.com/DNLPRTL/DashClientModular4.git
cd DashClientModular4
git checkout rebuild/phase3-from-phase2
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Salida esperada:

```text
True
AMD Radeon RX 7800 XT
```

## Uso diario

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git status --short --branch
git pull
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

## Politica de artefactos

No commitear:

- datasets derivados;
- CSVs de entrenamiento;
- logs de entrenamiento;
- checkpoints;
- modelos;
- bundles;
- graficas generadas;
- zips;
- paquetes de evidencia;
- runs de validacion.

Si un entrenamiento produce un candidato, versionar solo codigo, specs,
manifests pequenos reproducibles, model cards y documentacion. El artefacto
pesado debe quedarse fuera del repositorio bajo `~/TFG/modelos` o ruta externa
documentada.

## Relacion con Fase 4-5 v1

La disponibilidad de GPU elimina la restriccion de entrenar solo modelos
pequenos o CPU-first, pero no elimina los guardrails cientificos:

- primero decision tecnica desde papers;
- despues spec de dataset/simulador/modelo;
- despues entrenamiento;
- despues bundle reproducible;
- despues integracion plug-and-play;
- despues Phase 6 para evaluar.

Entrenar mas grande no autoriza por si solo ranking, ganador ni mejora QoE.
