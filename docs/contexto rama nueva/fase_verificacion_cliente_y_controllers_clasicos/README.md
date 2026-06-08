# Fase de Verificacion del Cliente y Controllers Clasicos

Status: closed_on_ubuntu.

Esta fase verifica que DashClientModular4 funciona como cliente DASH y que los
controllers clasicos usados como comparadores tienen una implementacion
coherente con sus documentos locales.

No es una fase de benchmark. No compara QoE, no declara ganador, no crea ranking
y no afirma mejora de ningun controller. Su objetivo es mas basico y mas
defendible:

```text
saber que el cliente reproduce contenido DASH, registra los artifacts correctos
y entrega a cada controller solo senales runtime permitidas
```

## Que produce

La ejecucion recomendada genera fuera del repo:

```text
runs_trazas/fase_verificacion_cliente_y_controllers_clasicos/
```

Dentro de esa carpeta quedan:

- configs usadas por el verificador;
- logs de comandos;
- runs por controller;
- `resumen_verificacion_cliente_y_controllers_clasicos.json`;
- `informe_verificacion_cliente_y_controllers_clasicos.md`.

El informe final esta pensado para ser leido por un humano o por otra IA sin
tener que inspeccionar todos los CSV a mano.

## Cierre Ubuntu

Ubuntu cliente valido:

- `python scripts/check_client_readiness.py --strict`: `88 OK / 0 WARN / 0 FAIL`.
- `curl -I` del MPD de verificacion: `HTTP/1.1 200 OK`.
- `python scripts/verificar_cliente_y_controllers_clasicos.py --mpd-url ...`:
  `Status: accepted`.

Informe externo aceptado:

```text
/home/daniel/TFG/runs_trazas/fase_verificacion_cliente_y_controllers_clasicos/informe_verificacion_cliente_y_controllers_clasicos.md
```

Decision:

```text
ACCEPTED_AS_CLIENT_AND_CLASSIC_CONTROLLER_VERIFICATION
```

## Controllers verificados

```text
rate_based
bba
bola
mpc
robust_mpc
```

Los controllers de sanity/debug no forman parte del cierre academico de esta
fase.

## Documentos

```text
contrato_de_verificacion.md
como_saber_que_el_cliente_funciona.md
como_saber_que_no_contamina_las_pruebas.md
verificacion_de_controllers_clasicos.md
guia_ubuntu_paso_a_paso.md
informe_final_verificacion.md
```
