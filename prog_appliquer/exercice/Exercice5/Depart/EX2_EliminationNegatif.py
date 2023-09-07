
# Petit programme permettant:
#   1. De générer aléatoirement 20 nombres entiers entre -50 et 50 inclusivement
#   2. De conserver ces nombres dans une liste
#   3. D'afficher la liste des nombres
#   4. D'éliminer les nombres négatifs de la liste sans construire une nouvelle liste
#   5. D'afficher la liste résultante

# Initialisation de la liste avec des nombres aléatoires entre -50 et 50
from random import randrange
liste = []
for indice in range(20):
    liste.append(randrange(-50, 51))

# Affichage de la liste
print("Liste avant l'élimination des nombres négatifs:")
print(liste)
print()

# Élimination des nombres négatifs de la liste
# Ajoutez ci-dessous le code nécessaire pour épurer la liste en enlevant les nombres négatifs.
# Afficher ensuite la liste.
# ...
i = 0
while i < len(liste):
    if liste[i] < 0:
        del liste[i]
    else:
        i += 1

# Affichage de la liste épurée
print("Liste épurée:")
print(liste)
