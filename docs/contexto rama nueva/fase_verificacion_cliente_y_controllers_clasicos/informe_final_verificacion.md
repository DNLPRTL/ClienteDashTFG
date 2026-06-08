# Informe Final de Verificacion

Status: pending_ubuntu_execution.

El cierre se completara cuando Daniel ejecute en Ubuntu:

```bash
python -m unittest discover
python scripts/check_client_readiness.py --strict
python scripts/verificar_cliente_y_controllers_clasicos.py \
  --mpd-url "http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd"
```

La evidencia generada no se commitea al repositorio. El resultado esperado sera
un informe externo:

```text
runs_trazas/fase_verificacion_cliente_y_controllers_clasicos/informe_verificacion_cliente_y_controllers_clasicos.md
```

## Criterio de aceptacion

Se aceptara la fase si:

- los cinco controllers clasicos pasan;
- los runs terminan con `status=completed`;
- los artifacts canonicos existen;
- los artifacts legacy no aparecen;
- `evaluation_segments.csv` sigue limpio;
- no hay columnas IA en runs clasicos;
- no se declara benchmark, ranking, ganador ni mejora QoE.

