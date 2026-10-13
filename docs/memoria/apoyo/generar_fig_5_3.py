"""Genera la Figura 5.3 (decision real del experimento) a partir de ejemplo_decision.json."""
import json
from pathlib import Path

AQUI = Path(r"C:\Users\danie\Documents\TFG\apoyo_memoria")
DESTINO = Path(r"C:\Users\danie\Documents\TFG\DashClientModular4\docs\memoria\figuras\fig_5_3_decision_real.svg")
r = json.loads((AQUI / "ejemplo_decision.json").read_text(encoding="utf-8"))

NIVELES = [300, 750, 1200, 1850, 2850, 4300]
AZUL, GRIS, GRIS_OSC, ROJO, AMAR = "#1971c2", "#868e96", "#495057", "#c92a2a", "#f08c00"


def coma(v, d=2):
    return f"{v:.{d}f}".replace(".", ",").replace("-", "\u2212")


pred = [[v / 1e6 for v in fila] for fila in r["pred_bps"]]
medido = r["tp_siguiente_bps"] / 1e6

# ---------- panel (a) ----------
X0, X1, Y0, Y1 = 78, 458, 78, 338
YMAX = 3.2
ancho = (X1 - X0) / 5.0


def py(mbps):
    return Y1 - (Y1 - Y0) * mbps / YMAX


partes = []
add = partes.append
add('<svg xmlns="http://www.w3.org/2000/svg" width="960" height="420" viewBox="0 0 960 420" font-family="Helvetica, Arial, sans-serif">')
add('<rect x="0" y="0" width="960" height="420" fill="#ffffff"/>')
add(f'<text x="20" y="26" font-size="14" font-weight="bold" fill="#212529">(a) Escenarios de throughput predichos</text>')
add(f'<text x="20" y="46" font-size="12" fill="{GRIS_OSC}">Paseo 30 fps · traza de banda ancha fija (FCC) · buffer {coma(r["buffer_s"], 1)} s · nivel actual {NIVELES[r["nivel_previo"]]} kbit/s</text>')

# bandas escalonadas
def banda(qi, qj, color, opac):
    pts_sup = []
    pts_inf = []
    for h in range(5):
        xa, xb = X0 + h * ancho, X0 + (h + 1) * ancho
        pts_sup += [(xa, py(pred[h][qj])), (xb, py(pred[h][qj]))]
        pts_inf += [(xa, py(pred[h][qi])), (xb, py(pred[h][qi]))]
    pts = pts_sup + pts_inf[::-1]
    add('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{color}" fill-opacity="{opac}" stroke="none"/>')


# niveles de la escalera (debajo de las bandas)
for kbps in NIVELES:
    m = kbps / 1000.0
    if m > YMAX:
        continue
    if kbps == 1850:
        add(f'<line x1="{X0}" y1="{py(m):.1f}" x2="{X1}" y2="{py(m):.1f}" stroke="{AZUL}" stroke-width="6" stroke-opacity="0.35"/>')
    elif kbps == 2850:
        add(f'<line x1="{X0}" y1="{py(m):.1f}" x2="{X1}" y2="{py(m):.1f}" stroke="{ROJO}" stroke-width="2" stroke-dasharray="7 4"/>')
    else:
        add(f'<line x1="{X0}" y1="{py(m):.1f}" x2="{X1}" y2="{py(m):.1f}" stroke="#ced4da" stroke-width="1" stroke-dasharray="3 3"/>')
add(f'<text x="{X0 + 6}" y="{py(1.2) + 15:.1f}" font-size="11" fill="{GRIS}">1200 kbit/s</text>')
add(f'<text x="{X0 + 6}" y="{py(0.75) + 15:.1f}" font-size="11" fill="{GRIS}">750 kbit/s</text>')
add(f'<text x="{X0 + 6}" y="{py(0.3) - 5:.1f}" font-size="11" fill="{GRIS}">300 kbit/s</text>')
# leyenda de las dos secuencias, en la zona libre superior
add(f'<line x1="{X0 + 8}" y1="{py(3.05):.1f}" x2="{X0 + 30}" y2="{py(3.05):.1f}" stroke="{ROJO}" stroke-width="2" stroke-dasharray="7 4"/>')
add(f'<text x="{X0 + 36}" y="{py(3.05) + 4:.1f}" font-size="11.5" fill="{ROJO}">2850 kbit/s: mejor secuencia si solo se mira la mediana</text>')
add(f'<line x1="{X0 + 8}" y1="{py(2.55):.1f}" x2="{X0 + 30}" y2="{py(2.55):.1f}" stroke="{AZUL}" stroke-width="6" stroke-opacity="0.35"/>')
add(f'<text x="{X0 + 36}" y="{py(2.55) + 4:.1f}" font-size="11.5" fill="{AZUL}" font-weight="bold">1850 kbit/s: secuencia elegida por el CVaR</text>')

banda(0, 2, AZUL, 0.20)
banda(2, 3, GRIS, 0.22)

# escalones de cada cuantil
estilos = {0: (AZUL, 2.0, ""), 1: (AZUL, 1.4, ""), 2: (AZUL, 1.4, ' stroke-dasharray="5 3"'), 3: (GRIS, 1.4, "")}
for q, (color, ancho_l, extra) in estilos.items():
    pts = []
    for h in range(5):
        xa, xb = X0 + h * ancho, X0 + (h + 1) * ancho
        pts += [(xa, py(pred[h][q])), (xb, py(pred[h][q]))]
    add('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="none" stroke="{color}" stroke-width="{ancho_l}"{extra}/>')

# etiquetas de cuantiles a la derecha
etiquetas = [(3, "q75", GRIS), (2, "q50", AZUL), (1, "q25", AZUL), (0, "q10", AZUL)]
for q, nombre, color in etiquetas:
    add(f'<text x="{X1 + 6}" y="{py(pred[4][q]) + 4:.1f}" font-size="11.5" fill="{color}" font-weight="bold">{nombre}</text>')

# throughput medido despues
xm = X0 + 0.5 * ancho
add(f'<circle cx="{xm:.1f}" cy="{py(medido):.1f}" r="4.5" fill="#212529"/>')
add(f'<line x1="{xm:.1f}" y1="{py(medido) + 5:.1f}" x2="{xm + 70:.1f}" y2="{py(0.56):.1f}" stroke="#212529" stroke-width="0.9"/>')
add(f'<text x="{xm + 73:.1f}" y="{py(0.56) + 4:.1f}" font-size="11" fill="#212529">medido en la descarga siguiente: {coma(medido)} Mbit/s</text>')

# ejes
add(f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{GRIS_OSC}" stroke-width="1.2"/>')
add(f'<line x1="{X0}" y1="{Y1}" x2="{X0}" y2="{Y0 - 6}" stroke="{GRIS_OSC}" stroke-width="1.2"/>')
for v in (0, 1, 2, 3):
    add(f'<line x1="{X0 - 4}" y1="{py(v):.1f}" x2="{X0}" y2="{py(v):.1f}" stroke="{GRIS_OSC}"/>')
    add(f'<text x="{X0 - 8}" y="{py(v) + 4:.1f}" font-size="11" fill="{GRIS_OSC}" text-anchor="end">{v}</text>')
add(f'<text x="{X0 - 8}" y="{Y0 - 12}" font-size="11" fill="{GRIS_OSC}" text-anchor="end">Mbit/s</text>')
for h in range(5):
    add(f'<text x="{X0 + (h + 0.5) * ancho:.1f}" y="{Y1 + 17}" font-size="11.5" fill="{GRIS_OSC}" text-anchor="middle">k+{h + 1}</text>')
add(f'<text x="{(X0 + X1) / 2:.1f}" y="{Y1 + 35}" font-size="11.5" fill="{GRIS_OSC}" text-anchor="middle">segmento futuro</text>')

# leyenda de bandas
add(f'<rect x="{X0}" y="{Y1 + 50}" width="14" height="10" fill="{AZUL}" fill-opacity="0.20"/>')
add(f'<text x="{X0 + 20}" y="{Y1 + 59}" font-size="11" fill="{GRIS_OSC}">escenarios que pondera el CVaR (q10 a q50)</text>')
add(f'<rect x="{X0 + 280}" y="{Y1 + 50}" width="14" height="10" fill="{GRIS}" fill-opacity="0.22"/>')
add(f'<text x="{X0 + 300}" y="{Y1 + 59}" font-size="11" fill="{GRIS_OSC}">escenario optimista (excluido)</text>')

# ---------- panel (b) ----------
add('<line x1="530" y1="20" x2="530" y2="400" stroke="#e9ecef" stroke-width="1.5"/>')
add('<text x="552" y="26" font-size="14" font-weight="bold" fill="#212529">(b) Puntuación de cada secuencia por escenario</text>')
add(f'<text x="552" y="46" font-size="12" fill="{GRIS_OSC}">Σ de (Mbit/s − 4,3 · rebuffering − |Δ Mbit/s|) en 5 segmentos</text>')

TX = [552, 700, 818]  # columnas: escenario | 1850x5 | 2850x5
fila_y = 84
add(f'<rect x="548" y="62" width="392" height="32" fill="#f1f3f5"/>')
add(f'<text x="{TX[0]}" y="{fila_y}" font-size="12" font-weight="bold" fill="#212529">Escenario</text>')
add(f'<text x="{TX[1]}" y="{fila_y}" font-size="12" font-weight="bold" fill="{AZUL}">1850 × 5</text>')
add(f'<text x="{TX[2]}" y="{fila_y}" font-size="12" font-weight="bold" fill="{ROJO}">2850 × 5</text>')

pc, pz = r["puntos_cvar_sec"], r["puntos_central_sec"]
rc, rz = r["rebuf_cvar_sec"], r["rebuf_central_sec"]
nombres = ["q10 (pesimista)", "q25", "q50 (mediana)", "q75 (optimista)"]
y = 118
for q in range(4):
    color_fila = GRIS if q == 3 else "#212529"
    add(f'<text x="{TX[0]}" y="{y}" font-size="12" fill="{color_fila}">{nombres[q]}</text>')
    add(f'<text x="{TX[1]}" y="{y}" font-size="12" fill="{color_fila}">{coma(pc[q])}</text>')
    txt = coma(pz[q]) + (f"  ({coma(rz[q], 1)} s de rebuf.)" if rz[q] > 0.05 else "")
    add(f'<text x="{TX[2]}" y="{y}" font-size="12" fill="{color_fila}">{txt}</text>')
    add(f'<line x1="548" y1="{y + 9}" x2="940" y2="{y + 9}" stroke="#e9ecef"/>')
    y += 28

cvar_c = r["cvar_de_cvar"]
cvar_z = r["cvar_de_central"]
add(f'<rect x="548" y="{y - 18}" width="392" height="28" fill="#e7f0fa"/>')
add(f'<text x="{TX[0]}" y="{y}" font-size="12" font-weight="bold" fill="{AZUL}">CVaR (α = 0,75)</text>')
add(f'<text x="{TX[1]}" y="{y}" font-size="12.5" font-weight="bold" fill="{AZUL}">{coma(cvar_c)}  ← elige</text>')
add(f'<text x="{TX[2]}" y="{y}" font-size="12" fill="#212529">{coma(cvar_z)}</text>')
y += 30
add(f'<text x="{TX[0]}" y="{y}" font-size="12" fill="{GRIS_OSC}">Solo la mediana</text>')
add(f'<text x="{TX[1]}" y="{y}" font-size="12" fill="{GRIS_OSC}">{coma(pc[2])}</text>')
add(f'<text x="{TX[2]}" y="{y}" font-size="12" font-weight="bold" fill="{ROJO}">{coma(pz[2])}  ← elige</text>')

y += 34
notas = [
    "La secuencia de 2850 kbit/s gana con la mediana, pero con",
    "q25 y q10 acumula rebuffering; el CVaR promedia los tres",
    "escenarios no optimistas y mantiene 1850 kbit/s.",
    "Tamaño real del segmento siguiente: +9 % (1850) y +11 %",
    "(2850) sobre el nominal; la simulación usa el real.",
]
for linea in notas:
    add(f'<text x="{TX[0]}" y="{y}" font-size="11.5" fill="{GRIS_OSC}">{linea}</text>')
    y += 17

add("</svg>")
DESTINO.write_text("\n".join(partes), encoding="utf-8")
print("escrita", DESTINO, "medido", medido, "cvar", cvar_c, cvar_z)
