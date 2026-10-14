"""Comprueba que el plan en seco selecciona exactamente las ventanas esperadas.

Uso: python3 comparar_ventanas.py <ventanas_trazas.csv del plan> <ventanas_esperadas.txt>
"""
import csv
import sys


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as fichero:
        plan = [fila["id_ventana_traza"] for fila in csv.DictReader(fichero)]
    with open(sys.argv[2], encoding="utf-8") as fichero:
        esperadas = [linea.strip() for linea in fichero if linea.strip()]
    if plan == esperadas:
        print("   OK: {0} ventanas, todas las esperadas y en el mismo orden".format(len(plan)))
        return 0
    print("   ERROR: el plan no coincide con las ventanas esperadas")
    print("   en el plan y no esperadas:", sorted(set(plan) - set(esperadas)))
    print("   esperadas y no en el plan:", sorted(set(esperadas) - set(plan)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
