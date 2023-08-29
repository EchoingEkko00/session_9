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
    mots = chaine.split()
    lexique = {}
    for mot in mots:
        if mot in lexique:
            lexique[mot] += 1
        else:
            lexique[mot] = 1
    return lexique
    

lex = lexicaliser("Écrire une fonction lexicaliser ayant un argument (une chaîne de caractères) et qui renvoie un dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.")
print(lex)

#3 de l'exercice
dictionnaire = {
    "Au" : {
        "Te/Tf" : [2970, 1063],
        "Z/A" : [79, 196.967],
    },
    "Ga" : {
        "Te/Tf" : [2237, 29.8],
        "Z/A" : [31, 69.72],
    }}

print(dictionnaire["Ga"]["Z/A"][0])