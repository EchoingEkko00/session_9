#1 de l'exercice 
liste = [17,38,99,52,27]

liste.sort()
print(liste)

liste.append(12)
print(liste)

liste.reverse()
print(liste)

print(liste.index(17), "est l'indice de 17")

liste.remove(38)
print(liste)

print(liste[1:3])

print(liste[:2])

print(liste[2:])

print(liste[-1])

#2 de l'exercice
def lexicaliser(chaine):
    return chaine.split()
    

lex = lexicaliser("Écrire une fonction lexicaliser ayant un argument (une chaîne de caractères) et qui renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.")
print(lex)

#3 de l'exercice