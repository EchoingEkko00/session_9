
# Petit programme permettant:
#   1. De générer 2 listes de nombres aléatoires entre 0 et 9
#   2. De fusionner les deux listes en une troisième liste en éliminant tous les doublons
#      pour que la liste finale ne contienne que des éléments distincts

# Initialisation des listes
taille1 = int(input("Entrez le nombre d'éléments de la 1ère liste : "))
taille2 = int(input("Entrez le nombre d'éléments de la 2ème liste : "))
from random import randrange
liste1 = []
liste2 = []
for indice in range(taille1):
    liste1.append(randrange(10))
for indice in range(taille2):
    liste2.append(randrange(10))
print("Liste 1:")
print(liste1)
print()
print("Liste 2:")
print(liste2)
print()

# Ajoutez ci-dessous le code nécessaire pour construire une troisième liste nommée "liste3"
# en fusionnant les 2 listes et en enlevant les doublons.
# Afficher ensuite la liste.
# ...

# Affichage de la liste résultante
print("Liste 3:")
print(liste3)
