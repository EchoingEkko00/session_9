#heron.py
def sqrt(x):
    """Calcul de la racine carrée avec la méthode d'Héron d'Alexandrie.
    Argument:
        x: le nombre à traiter.
    Retourne:
        La racine carrée de x.
    """
    approximation = x
    i = 0
    while approximation * approximation != x and i < 20:
        approximation = (approximation + x / approximation) / 2.0
        i += 1
    return approximation
def main():
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))
if __name__ == '__main__':
    main()
