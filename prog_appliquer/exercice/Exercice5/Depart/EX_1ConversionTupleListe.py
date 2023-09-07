# Petit programme permettant:
#   1. De convertir un tuple en liste avec une boucle for
#   2. De convertir un tuple en liste avec une boucle while
#   3. De convertir un tuple en liste sans boucle explicite et sans la fonction list

# Initialisation du tuple de départ
leTuple = ('Sylvie', 'Jacques', 'Rosaire', 'Xavier', 'Clothilde')
print(" Le tuple initial:", leTuple)

# Avec une boucle for
# Ajoutez ci-dessous le code nécessaire pour construire une liste nommée "liste1" avec une boucle for
# et qui contiendra les mêmes éléments que le tuple plus haut.
# Afficher ensuite la liste.
# ...

liste1 = []
for i in leTuple:
    liste1.append(i)
print("Liste avec boucle for:", liste1)

# Avec une boucle while
# Ajoutez ci-dessous le code nécessaire pour construire une liste nommée "liste2" avec une boucle while
# et qui contiendra les mêmes éléments que le tuple plus haut.
# Afficher ensuite la liste.
# ...

liste2 = []
i = 0
while i < len(leTuple):
    liste2.append(leTuple[i])
    i += 1
print("Liste avec boucle while:", liste2)

# Sans boucle explicite
# Ajoutez ci-dessous le code nécessaire pour construire une liste nommée "liste3" sans utiliser de boucle explicite
# et qui contiendra les mêmes éléments que le tuple plus haut.
# Afficher ensuite la liste.
# ...
liste3 = list(leTuple)
print("Liste sans boucle:", liste3)
