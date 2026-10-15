# Pruebas de la fase de blindaje

Desde el pulido F8 (15/10/2026), las pruebas viven con el código entregado, en
`TFG Material\01_codigo\ClienteDashTFG\pruebas\`. Así viajan con él a la VM y
se ejecutan allí en `comprobar`.

Se ejecutan desde la carpeta del código:

```bash
python -m unittest discover -s pruebas
```

| Fichero | Qué comprueba |
|---|---|
| `test_mpc_canonico.py` | C3: el MPC robusto coincide con el bucle de Pensieve (`test/mpc.py`) |
| `test_paradas_y_variantes.py` | C2 (paradas del reproductor) y C4 (variantes de ablación) |
| `test_contrastes.py` | Contrastes prerregistrados P1–P5, Holm y bootstrap por ventanas |
| `test_carga_modelo.py` | F8: el modelo se carga al crear el controlador; si falla, decide el respaldo |

`artefactos.py` localiza el bundle y los cuantiles fijos en las dos máquinas:
- Windows: `TFG Material\03_modelos`;
- VM: `~/TFG/modelos`.
