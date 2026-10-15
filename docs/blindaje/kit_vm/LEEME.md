# Kit de la VM cliente (fase de blindaje)

Sirve para el **experimento final**. Todo se copia y se pega tal cual.

- **Windows:** usa PowerShell.
- **VM cliente** (192.168.1.160): usa su terminal.

El protocolo está en `docs/blindaje/06_PROTOCOLO_FINAL.md`. La prueba corta ya
se hizo el 14/10 (`05_SEMAFORO_2.md`).

---

## Experimento final (~42–44 h)

1208 sesiones: 74 ventanas de `eval` × 2 vídeos × 8 controladores, más 3
sintéticas.

### 0. Windows, una vez: que el PC no se suspenda

- Configuración > Sistema > Energía > suspender: **Nunca** (con el cargador
  enchufado).
- En PowerShell **como administrador**, para que Windows no frene la VM en
  segundo plano:

```bash
powercfg /powerthrottling disable /path "C:\Program Files\Oracle\VirtualBox\VirtualBoxVM.exe"
```

### 1. VM cliente: apartar el código de la prueba corta

```bash
mv ~/TFG/ClienteDashTFG ~/TFG/ClienteDashTFG_previa && mv ~/TFG/kit_vm ~/TFG/kit_vm_previa
```

### 2. Windows: copiar el código congelado y este kit a la VM

```bash
scp -r "C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG" daniel@192.168.1.160:~/TFG/
```

```bash
scp -r "C:\Users\danie\Documents\TFG\DashClientModular4\docs\blindaje\kit_vm" daniel@192.168.1.160:~/TFG/
```

### 3. VM cliente: comprobar (3–4 min)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh comprobar
```

Tiene que acabar con `TODO CORRECTO`. Comprueba (9 pasos):
- huellas del código, el modelo, el catálogo y los cuantiles fijos;
- que no sobra ningún fichero viejo;
- las 18 pruebas en la VM;
- los 5 vídeos del servidor;
- las ventanas del plan en seco;
- los 8 controladores.

### 4. VM cliente: humo (~20 min)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh humo
```

Tiene que acabar con `HUMO CORRECTO`:
- 8 sesiones completadas y 0 respaldos;
- latencia de decisión p99 < 20 ms;
- primera decisión del propio < 20 ms.

### 5. VM cliente: lanzar el experimento final (en segundo plano)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh final
```

Puedes cerrar la terminal. Durante las ~42 h:
- el PC sin suspenderse;
- la VM con su ventana abierta;
- nada de WSL ni copias desde el servidor.

### 6. VM cliente: ver cómo va (cuando quieras)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh estado
```

Muestra las sesiones completadas de 1208 y las horas que faltan. Cuando ponga
`Terminado`, copia en PowerShell la línea `scp ...` que te muestra (lleva el
paquete a `TFG Material\04_evidencia_final`) y avisa a Claude.

## Si algo falla

| Fallo | Qué hacer |
|---|---|
| `FALLO` en `comprobar` o `humo` | No sigas. Pega la salida a Claude. |
| `$'\r': command not found` | `sed -i 's/\r$//' ~/TFG/kit_vm/*.sh` y repite. |
| `estado` dice que se cortó (apagón, cuelgue) | `bash ~/TFG/kit_vm/blindaje_vm.sh reanudar`: sigue el mismo paquete, conserva las sesiones completadas y repite solo las que faltan. |
| Necesitas pararlo a propósito | No lo pares salvo emergencia, y pregunta antes a Claude. |
