# Como Saber Que El Cliente Funciona

La verificacion sigue el flujo real del cliente:

```text
MPD
-> parser DASH
-> lista de representations y segmentos
-> downloader HTTP
-> media engine
-> buffer
-> feedback runtime
-> controller ABR
-> siguiente representation
-> CSV y manifest
```

## Prueba cliente-servidor

En Ubuntu cliente se usa una URL del servidor DASH, por ejemplo:

```text
http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd
```

El servidor solo sirve contenido. No define la red experimental ni decide
resultados.

## Que se comprueba

Para cada controller se comprueba que:

- `main.py` arranca con una config normal;
- el MPD se parsea;
- la ladder de rates viene del MPD;
- los segmentos se descargan;
- el buffer avanza;
- el controller recibe feedback;
- el controller devuelve un rate valido;
- `policy_chosen_level` pertenece a la ladder;
- el run termina con `status=completed`;
- los artifacts canonicos existen.

## Por que la red rapida no contamina esta fase

La red por adaptador puente puede ser muy rapida. Eso no contamina esta fase
porque aqui no se mide rendimiento ABR. Solo se verifica que el circuito
cliente-servidor funciona y que el pipeline deja evidencia coherente.

La comparacion de rendimiento queda para la fase de evaluacion formal con red,
trazas y protocolo autorizados.

