from os import makedirs, path

# Programme permettant de présenter:
#    - Les opérations d'écriture et de lecture dans les fichiers

######################
# ECRITURE DE FICHIERS
######################

# Ecriture dans un fichier en mode "Write" (w)
# Sans mettre de caractères de fin de ligne (\n)
print("Exemple 1")
print("Ouverture du fichier")
mesResultats = open("res0.txt", "w", encoding = "utf-8")
print("Écriture dans le fichier")
mesResultats.write("Salut comment ça va?")
for i in range(10):
    mesResultats.write(str(i))
mesResultats.write("Voici une autre phrase")
print("Fermeture du fichier")
mesResultats.close()
print()

# Écriture dans un fichier en mode "Write" (w)
# Avec des caractères de fin de ligne (\n) et des caractères spéciaux comme la tabulation (\t)
print("Exemple 2:")
print("Ouverture du fichier")
mesResultats = open("res1.txt", "w", encoding = "utf-8")
print("Écriture dans le fichier")
mesResultats.write("Salut comment ça va?\n")
for i in range(10):
    mesResultats.write("\t" + str(i) + "\n")
mesResultats.write("Voici une autre ligne\n")
print("Fermeture du fichier")
mesResultats.close()
print()

# Écriture dans un fichier en mode "Append" (a) pour permettre d'ajouter des lignes au fichier existant
print("Exemple 3:")
mesResultats = open("res2.txt", "a", encoding="utf-8")
mesResultats.write("Salut comment ça va?\n")
for i in range(10):
    mesResultats.write("\t" + str(i) + "\n")
mesResultats.write("Voici une autre ligne\n")
mesResultats.close()
#Et on ajoute dans un deuxième temps...
mesResultats = open("res2.txt", "a", encoding = "utf-8")
mesResultats.write("Et voici une ligne qui avait été oubliée.....\n")
mesResultats.close()
print()

# Écriture d'un fichier dans un sous-répertoire qui n'existe pas déjà
print("Exemple 4:")
if not path.isdir("resultat") : # existe-t-il? non, alors je le crée
    makedirs("resultat")
mesResultats = open("resultat/res3.txt", "a", encoding = "utf-8")
mesResultats.write("Salut comment ça va?\n")
for i in range(10):
    mesResultats.write("\t" + str(i) + "\n")
mesResultats.write("Voici une autre ligne\n")
mesResultats.close()
print()

# Écriture d'un fichier dans le répertoire parent
print("Exemple 5:")
mesResultats = open("../res3.txt", "a", encoding = "utf-8")
mesResultats.write("Salut comment ça va?\n")
for i in range(10):
    mesResultats.write("\t" + str(i) + "\n")
mesResultats.write("Voici une deuxième ligne\n")
mesResultats.close()
print()

# Erreur d'ouverture d'un fichier
# print("Exemple 6:")
# mesResultats = open("abc/res5.txt", "a", encoding = "utf-8")
# mesResultats.write("Salut comment ça va?\n")
# for i in range(10):
#    mesResultats.write(str(i+1) + "\n")
# mesResultats.write("Voici une\tdeuxième ligne\n")
# mesResultats.close()


#####################
# LECTURE DE FICHIERS
#####################

# Lire un fichier par bloc (un bloc = un nombre de caractères précisé)
print("Exemple 7:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
# Lecture du premier caractère du fichier
leCar = mesDonnees.read(1)
print(leCar)
mesDonnees.close()
print()

# Lire plusieurs caractères dans le bloc (méthode read)
print("Exemple 8:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
print("Partie 1 (lecture de 7 caractères)")
partie1 = mesDonnees.read(7)
print(partie1)
print("Partie 2 (lecture de 3 caractères)")
partie2 = mesDonnees.read(3)
print(partie2)
print("Partie 3 (lecture de 16 caractères: 12 caractères + 2 tabulations + 2 fins de ligne)")
partie3 = mesDonnees.read(16)
print(partie3)
print("Partie 4 (lecture de 1000 caractères : tout le reste du fichier en fait)")
partie4 = mesDonnees.read(1000)
print(partie4)
print("Partie 5 (lecture de 5 caractères mais on a atteint la fin du fichier...)")
partie5 = mesDonnees.read(5)
print(partie5)
mesDonnees.close()
print()

# Lire un fichier par ligne (méthode readline)
# Attention, la variable uneLigne contient les caractères réguliers de la ligne + le caractère de fin de ligne (\n)
print("Exemple 9:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
uneLigne = mesDonnees.readline()
print(uneLigne)
print("La ligne précédente comporte", len(uneLigne), "caractères.")
uneLigne = mesDonnees.readline()
print(uneLigne)
print("La ligne précédente comporte", len(uneLigne), "caractères.")
mesDonnees.close()
print()

# Lire un fichier par ligne (méthode readline) en enlevant le dernier caractère de fin de ligne pour ne pas le traiter
print("Exemple 10:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
uneLigne = mesDonnees.readline()
print(uneLigne[0:len(uneLigne)-1])
uneLigne = mesDonnees.readline()
print(uneLigne[0:len(uneLigne)-1])
mesDonnees.close()
print()

# Lecture du fichier au complet, ligne par ligne en enlevant le dernier caractère de la ligne si c'est un caractère "\n".
# On arrête lorsque la ligne lue ne comporte aucun caractère
print("Exemple 11:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
uneLigne = "N'importe quoi"
while (uneLigne != ""):
    uneLigne = mesDonnees.readline()
    if uneLigne == "":
        break
    lg = len(uneLigne)
    if (uneLigne[lg-1] == "\n"):
        print(uneLigne[0:lg-1])
    else:
        print(uneLigne[0:lg])
mesDonnees.close()
print()

# Lecture du fichier au complet, d'un seul bloc (méthode read sans paramètre).
print("Exemple 12:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
unBloc = mesDonnees.read()
print(unBloc)
print("Le bloc lu contient", len(unBloc), "caractères.")
mesDonnees.close()
print()

# Lecture du fichier au complet, un caractère à la fois.
# Même les caractères de fin de ligne sont lus et affichés.

print("Exemple 13:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
unCar = "S"
while (unCar != ""):
    unCar = mesDonnees.read(1)
    if (unCar == ""):
        break
    print(unCar)
mesDonnees.close()
print()

# Lecture du fichier au complet et conversion de chaque ligne dans un élément de liste (méthode readlines).
print("Exemple 14:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
uneListe = mesDonnees.readlines()
mesDonnees.close()
print(uneListe)
print()

# Si on veut enlever les derniers caractères ("\n") de la liste
for i in range(len(uneListe)):
    if (uneListe[i][len(uneListe[i])-1] == "\n"):
        uneListe[i] = uneListe[i][0:len(uneListe[i])-1]
print(uneListe)
print()

# Reprise de l'exemple 14 mais on traite ensuite la liste en enlevant
# les blancs non significatifs au début et à la fin des chaînes.
print("Exemple 15:")
mesDonnees = open("res1.txt", "r", encoding = "utf-8")
uneListe = mesDonnees.readlines()
mesDonnees.close()
print(uneListe)
print()

# Si on veut enlever les derniers caractères ("\n") des membres de la liste
for i in range(len(uneListe)):
    uneListe[i] = uneListe[i].strip()
print(uneListe)
print()

# Écrire et lire dans un fichier via une liste
print("Exemple 16:") 
L = ["Prêt\n", "pas\n", "prêt!\n"]
 
# Écrire dans un fichier
fichier1 = open('res4.txt', 'w', encoding = "utf-8")
fichier1.writelines(L)
fichier1.close()
 
# Lire en utilisant readlines()
fichier1 = open('res4.txt', 'r', encoding = "utf-8")
lignes = fichier1.readlines()
fichier1.close()

cpt = 0
# Enlever les \n
for ligne in lignes:
    cpt += 1
    print("Ligne {}: {}".format(cpt, ligne.strip()))
