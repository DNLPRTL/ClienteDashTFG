"""Genera el catalogo de la replica.

Copia el catalogo de trazas y marca como no utilizables en evaluacion las trazas
reales de los grupos de captura (grupo_fuga) que ya uso la evaluacion de agosto.
El algoritmo de seleccion y la semilla no cambian: solo cambia el bombo del sorteo.

Uso: python3 generar_catalogo_replica.py <codigo> <catalogo> <grupos_excluidos.txt> <salida>
Compatible con Python 3.8 (VM cliente).
"""
import json
import sys

GRUPOS_ESPERADOS = 11
TRAZAS_RETIRADAS_ESPERADAS = 23


def main():
    if len(sys.argv) != 5:
        print(__doc__)
        return 2
    codigo, ruta_catalogo, ruta_grupos, ruta_salida = sys.argv[1:5]
    sys.dont_write_bytecode = True
    sys.path.insert(0, codigo)
    from core.evaluacion.seleccion import es_traza_sintetica

    with open(ruta_grupos, encoding="utf-8") as fichero:
        grupos = sorted({linea.strip() for linea in fichero if linea.strip()})
    with open(ruta_catalogo, encoding="utf-8") as fichero:
        catalogo = json.load(fichero)

    retiradas = 0
    for traza in catalogo["trazas"]:
        if traza.get("grupo_fuga") in grupos and not es_traza_sintetica(traza):
            if traza.get("particion") == "eval" and traza.get("usable_en_eval", True) is not False:
                retiradas += 1
            traza["usable_en_eval"] = False

    catalogo["nota_replica"] = {
        "motivo": "replica con ventanas de evaluacion no usadas durante el desarrollo",
        "grupos_excluidos": grupos,
        "trazas_eval_retiradas": retiradas,
    }
    with open(ruta_salida, "w", encoding="utf-8") as fichero:
        json.dump(catalogo, fichero, ensure_ascii=False)

    print("   grupos excluidos: {0}; trazas de evaluacion retiradas del sorteo: {1}".format(len(grupos), retiradas))
    if len(grupos) != GRUPOS_ESPERADOS or retiradas != TRAZAS_RETIRADAS_ESPERADAS:
        print("   ERROR: se esperaban {0} grupos y {1} trazas".format(GRUPOS_ESPERADOS, TRAZAS_RETIRADAS_ESPERADAS))
        return 1
    print("   OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
