# Guia Ubuntu Paso A Paso

Ejecutar en la VM cliente Ubuntu.

## Sincronizar

```bash
cd ~/TFG/DashClientModular4
git status --short --branch
git pull --ff-only origin rebuild/phase3-from-phase2
git status --short --branch
```

## Validaciones base

```bash
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

## Comprobar servidor

```bash
curl -I "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd"
```

Debe devolver `HTTP/1.1 200 OK`.

## Ejecutar verificacion completa

```bash
python scripts/verificar_cliente_y_controllers_clasicos.py \
  --mpd-url "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd"
```

Salida esperada:

```text
Status: accepted
```

El informe queda en:

```text
/home/daniel/TFG/runs_trazas/fase_verificacion_cliente_y_controllers_clasicos/informe_verificacion_cliente_y_controllers_clasicos.md
```

## Ejecucion solo documental/probes

Si el servidor no esta disponible y se quiere probar solo la parte local:

```bash
python scripts/verificar_cliente_y_controllers_clasicos.py --skip-server-smokes
```

Salida esperada:

```text
Status: accepted_local_only
```

Eso no cierra la fase completa, pero valida los probes teoricos y el generador
de informe.

## Demo GStreamer opcional

Si se quiere anadir una prueba de integracion GStreamer:

```bash
python scripts/check_environment.py --profile gst --strict
python scripts/verificar_cliente_y_controllers_clasicos.py \
  --mpd-url "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd" \
  --run-gstreamer-demo
```

Esta demo no es benchmark. Solo prueba integracion.
