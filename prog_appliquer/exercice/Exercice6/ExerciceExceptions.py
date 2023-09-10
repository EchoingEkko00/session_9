# 1
# Définir les termes suivants :
# a. Gérer une exception : Gérer une exception signifie que l'on prévoit qu'une exception peut se produire et que l'on écrit du code pour la traiter.
# b. Lever une exception : Lever une exception signifie que l'on provoque volontairement une exception.
# c. Attraper une exception : Attraper une exception signifie que l'on écrit du code pour traiter une exception qui s'est produite.

# 2
# À quel moment est-ce que les exceptions suivantes sont
# levées par Python? Donnez un exemple de code pour chacune
# de vos réponses.
# a. ImportError : Lorsque l'on importe un module qui n'existe pas. Exemple : import moduleQuiNExistePas
# b. IOError : Lorsque l'on tente d'ouvrir un fichier qui n'existe pas. Exemple : open("fichierQuiNExistePas.txt", "r")
# c. NameError : Lorsque l'on tente d'utiliser une variable qui n'existe pas. Exemple : print(variableQuiNExistePas)

# 3
# L’instruction int("6x6") provoque une exception de type
# ValueError. Écrivez une fonction monint qui provoquera elle
# aussi une telle exception mais en étant plus précis sur ce qui
# ne va pas, comme dans cet exemple interactif :

def monint(chaine):
    if chaine.isdigit():
        return int(chaine)
    else:
        raise ValueError("La chaîne ne contient pas que des chiffres")

monint("6x6")

# 4
# Vous avez sans doute vu l’instruction assert en Java. Elle se
# comporte de façon similaire en Python. Réécrivez le script
# précédent en utilisant cette instruction.

def monint(chaine):
    assert chaine.isdigit(), "La chaîne ne contient pas que des chiffres"
    return int(chaine)

monint("6x6")

# 5. Voici un bloc de code en Python :
# Ajoutez le code nécessaire pour attraper au moins quatre
# exceptions susceptibles de se produire dans ce bloc.
#
# liste = [1,2,3]
# dic = {"zero":0, "un" :1, "deux" :2,"trois" :3}
# ind = int(input("Entrez un indice : "))
# cle = input("Entrez une clé : ")
# print(liste[ind] / dic[cle])

try:
    liste = [1,2,3]
    dic = {"zero":0, "un" :1, "deux" :2,"trois" :3}
    ind = int(input("Entrez un indice : "))
    cle = input("Entrez une clé : ")
    print(liste[ind] / dic[cle])
except IndexError:
    print("L'indice n'est pas valide")
except KeyError:
    print("La clé n'est pas valide")
except ValueError:
    print("La valeur n'est pas valide")
except ZeroDivisionError:
    print("La division par zéro n'est pas possible")