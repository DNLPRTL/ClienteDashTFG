# Kit de la VM cliente (fase de blindaje)

Sirve para la **prueba corta** (semáforo 2) y, después, para el **experimento
final**. Todo se copia y se pega tal cual.

- **Windows:** usa PowerShell.
- **VM cliente** (192.168.1.160): usa su terminal.

---

## Prueba corta (una noche, ~6,5 h)

Son 10 ventanas de **validación** × 2 vídeos × 8 controladores = 160
sesiones. No gasta ninguna ventana del experimento final.

### 1. VM cliente: apartar el código anterior

```bash
mv ~/TFG/ClienteDashTFG ~/TFG/ClienteDashTFG_antes_blindaje
```

### 2. Windows: copiar el código y este kit a la VM

```bash
scp -r "C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG" daniel@192.168.1.160:~/TFG/
```

```bash
scp -r "C:\Users\danie\Documents\TFG\DashClientModular4\docs\blindaje\kit_vm" daniel@192.168.1.160:~/TFG/
```

### 3. VM cliente: comprobar (2–3 min)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh comprobar
```

Tiene que acabar con `TODO CORRECTO`. Comprueba:
- que el código, el modelo, el catálogo y los cuantiles fijos son idénticos a
  los del material;
- que el servidor sirve los 5 vídeos;
- que el plan en seco elige las ventanas esperadas;
- que los 8 controladores deciden con los 5 vídeos.

### 4. VM cliente: prueba de humo (~20 min)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh humo
```

Tiene que acabar con `HUMO CORRECTO`: 8 sesiones completadas y 0 respaldos.

### 5. VM cliente: lanzar la prueba corta (~6,5 h, en segundo plano)

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh previa
```

Puedes cerrar la terminal. Durante la noche:
- el PC sin suspenderse;
- la VM con su ventana visible;
- sin WSL ni otras cargas.

### 6. VM cliente, por la mañana: estado

```bash
bash ~/TFG/kit_vm/blindaje_vm.sh estado
```

Si pone `Terminado`, copia en PowerShell la línea `scp ...` que te muestra.
Así el paquete queda en `TFG\legacy\evidencia_desarrollo`. Avisa a Claude.

## Si algo falla

| Fallo | Qué hacer |
|---|---|
| `FALLO` en `comprobar` o `humo` | No sigas. Pega la salida a Claude. |
| `$'\r': command not found` | `sed -i 's/\r$//' ~/TFG/kit_vm/*.sh` y repite. |
| La prueba corta se cortó (apagón) | `cd ~/TFG/ClienteDashTFG && nohup python3 scripts/3_evaluacion/ejecutar_evaluacion.py --raiz-paquete <carpeta que muestra estado> > ~/TFG/previa_vm.log 2>&1 &`: continúa el mismo paquete y omite las sesiones ya completadas. |

---

## Experimento final

Se hace después de la prueba corta, con el semáforo 2 en verde y el protocolo
commiteado. Claude te dará entonces los comandos exactos: copiar el código
congelado, `comprobar`, `humo` y lanzar por la interfaz gráfica con el preset
`final_blindaje`.
