#heron1.py
import sys
def sqrt(x):
    """Calcul de la racine carrée avec la méthode d'Héron d'Alexandrie.
    Argument:
        x: le nombre à traiter.
    Retourne:
        La racine carrée de x.
    Exceptions levées:
        ValueError: Si x est négatif.
    """
    if x < 0:
        raise ValueError(f"Impossible de calculer la racine carrée de {x}")
    approximation = x
    i = 0
    while approximation * approximation != x and i < 20:
        approximation = (approximation + x / approximation) / 2.0
        i += 1
    return approximation
def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("Ligne impossible à atteindre")
    except ValueError as e:
        print(e, file=sys.stderr)
    print("L'exécution se poursuit ici.")
if __name__ == '__main__':
    main()
