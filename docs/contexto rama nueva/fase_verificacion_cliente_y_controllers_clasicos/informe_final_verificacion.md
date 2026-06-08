# Informe Final de Verificacion

Status: closed_on_ubuntu.

El cierre se completo en Ubuntu cliente con:

```text
python scripts/check_client_readiness.py --strict
-> 88 OK / 0 WARN / 0 FAIL

curl -I "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd"
-> HTTP/1.1 200 OK

python scripts/verificar_cliente_y_controllers_clasicos.py --mpd-url "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd"
-> Status: accepted
```

La evidencia generada no se commitea al repositorio. El informe externo aceptado
quedo en:

```text
/home/daniel/TFG/runs_trazas/fase_verificacion_cliente_y_controllers_clasicos/informe_verificacion_cliente_y_controllers_clasicos.md
```

Daniel copio una version del informe a:

```text
C:\Users\danie\Desktop\TFG\informe_verificacion_cliente_y_controllers_clasicos.md
```

## Resultado

La fase queda aceptada como:

```text
ACCEPTED_AS_CLIENT_AND_CLASSIC_CONTROLLER_VERIFICATION
```

## Que demuestra

- el cliente carga un MPD real servido por HTTP;
- el servidor responde correctamente;
- los cinco controllers clasicos pasan probes controlados;
- los cinco controllers clasicos ejecutan reproducciones contra servidor;
- los artifacts canonicos existen;
- los artifacts legacy no aparecen;
- `evaluation_segments.csv` sigue limpio;
- no hay columnas IA en runs clasicos;
- no se declara benchmark, ranking, ganador ni mejora QoE.

## Que no demuestra

Esta fase no demuestra que ningun controller sea mejor que otro. La red rapida
por adaptador puente sirve para verificar funcionamiento estructural, no para
medir rendimiento ABR. La comparacion formal queda reservada para Phase 6.
