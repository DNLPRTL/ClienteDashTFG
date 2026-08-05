# Renombrado del proyecto a ClienteDashTFG + scripts y fase6 en castellano

| Campo | Valor |
|---|---|
| Fecha | 2026-08-05 |
| Nombre nuevo | **ClienteDashTFG** (antes DashClientModular4) — elegido por Daniel: el cliente DASH del TFG, a secas |
| Validación | 489 tests OK · comprobar_cliente --strict 104 OK/0 FAIL |

## 1. Paquete y scripts renombrados (git mv)

| Antes | Ahora |
|---|---|
| core/phase6/ | **core/fase6/** (analisis, catalogo, seleccion, configuracion, verificacion) |
| scripts/run_phase6_validacion_comparativa.py | **scripts/ejecutar_fase6.py** |
| scripts/phase6_gui.py | **scripts/gui_fase6.py** |
| scripts/analyze_phase6_results.py | scripts/analizar_resultados_fase6.py |
| scripts/verificar_paquete_phase6.py | scripts/verificar_paquete_fase6.py |
| scripts/run_phase6_verificacion_clasica_controlada.py | scripts/verificacion_clasica_controlada_fase6.py |
| scripts/check_client_readiness.py | **scripts/comprobar_cliente.py** |
| scripts/run_mpc_prudente_multimedia_dataset_wsl.sh | scripts/generar_dataset_multimedia_mpc_prudente_wsl.sh |
| scripts/run_mpc_prudente_temporal_training_wsl.sh | scripts/entrenar_temporal_mpc_prudente_wsl.sh |
| scripts/run_mpc_prudente_temporal_bundle_wsl.sh | scripts/exportar_bundle_temporal_mpc_prudente_wsl.sh |
| (resto de wrappers run_/export_/package_ mpc_prudente) | generar_/entrenar_/exportar_/empaquetar_/diagnostico_..._wsl.sh |
| tests/test_phase6_*.py, test_client_readiness_check.py | tests/test_fase6_*.py, test_comprobar_cliente.py |
| config/phase6.example.yaml | config/fase6.example.yaml |

Identificadores `*_PHASE6*`/`*_phase6*` → `*_FASE6*`/`*_fase6*` (p. ej.
`analizar_paquete_fase6`, `cargar_config_fase6`, `VERSION_SCHEMA_FASE6`); el
prefijo de progreso runner→GUI pasa a `FASE6_PROGRESO` (ambos lados actualizados).

**Compatibilidad conservada:** la config local `config/phase6.local.json` de
Ubuntu sigue funcionando (se pasa con `--config`); además la búsqueda por defecto
acepta `fase6.local.yaml` y el nombre antiguo `phase6.local.yaml`. NO cambian:
schema_version (`phase6_*_v1`), claves de datos, preset `tfg_final`, claves
`mpc_prudente_v1/v2`, ni rutas externas (`~/TFG/runs_trazas/phase6/...`).
Los módulos de líneas congeladas (phase45_*) no se tocan.

## 2. Renombrado del proyecto

- Repo GitHub: `DNLPRTL/DashClientModular4` → `DNLPRTL/ClienteDashTFG`
  (GitHub redirige la URL antigua, así que los `git pull` viejos no se rompen,
  pero conviene actualizar el remote).
- Referencias internas actualizadas: CLAUDE.md, AGENTS.md, README, arquitectura
  estándar, TFG_PLAN_GENERICO, HANDOFF, docs/defensa, todos los scripts/*.sh
  (`cd ~/TFG/ClienteDashTFG`), defaults de `core/fase6/configuracion.py` y
  `config/fase6.example.yaml` (`/home/daniel/TFG/ClienteDashTFG`).
- Renombrado de carpetas: Ubuntu cliente y WSL → `~/TFG/ClienteDashTFG`
  (+ `git remote set-url` + ajustar `repo_root` en `config/phase6.local.json`
  del cliente). **Windows: Daniel decidió NO renombrar la carpeta**
  (`C:\Users\danie\Documents\TFG\DashClientModular4`) para conservar el
  proyecto/memoria de Claude Code; solo se actualizó el remote. El nombre de la
  carpeta local es irrelevante para git y para los tests.
- El paquete de evidencia y los artefactos externos NO se mueven (viven bajo
  `~/TFG/...`, fuera del repo; sus rutas no contienen el nombre del repo).
