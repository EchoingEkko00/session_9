
# Petit programme permettant:
#   1. D'initialiser une liste nommée "laListe" avec des noms de personnes
#   2. D'inverser cette liste avec une boucle "for" mais sans utiliser l'opérateur d'affectation
#   3. De revenir à la liste initiale en inversant de nouveau mais sans utiliser de boucle

# Initialisation d'une liste
laListe = ['Sylvie', 'Jacques', 'Rosaire', 'Xavier', 'Clothilde']
print(laListe)

# Ajoutez ci-dessous le code nécessaire pour inverser le contenu de la liste avec une boucle "for"
# mais sans utiliser l'opérateur d'affectation.
# Afficher ensuite la liste.
# ...
for i in range(len(laListe) // 2):
    laListe[i], laListe[len(laListe) - i - 1] = laListe[len(laListe) - i - 1], laListe[i]
print(laListe)

# Ajoutez ci-dessous le code nécessaire pour inverser de nouveau la liste mais sans utiliser de boucle.
# ...
laListe.reverse()

print(laListe)
