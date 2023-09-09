import nltk
import re

#Exercice fichier
# 1.a
fichier = open("fichier1.txt")
texte = fichier.read()
fichier.close()
listeMot = nltk.word_tokenize(texte)

print(len(texte.split()))

# 1.b

listeVoyelles = ['a', 'e', 'i', 'o', 'u', 'y']
nbVoyelle = 0
for mot in listeMot:
    for lettre in mot:
        if lettre in listeVoyelles:
            nbVoyelle += 1
print(nbVoyelle)

# 1.c
fichier = open("fichier1.txt")
nbDeligne = fichier.readlines()
fichier.close()
print(len(nbDeligne))

fichier = open("resultat.txt", "w")
fichier.write("Nombre de mots : " + str(len(texte.split())) 
              + "\n" + "Nombre de voyelles : " + str(nbVoyelle)
              + "\n" + "Nombre de lignes : " + str(len(nbDeligne)))


# 2
moyenne:int = 0
somme:int = 0
fichier = open("nombres.txt", "r+")
texte = fichier.read()
texte = re.sub(r'[a-zA-Z].+', "", texte)
listeNombre = texte.split()
for i in range(len(listeNombre)):
    moyenne += int(listeNombre[i])
    somme += int(listeNombre[i])
moyenne = moyenne / len(listeNombre)
fichier.write("\nSomme : " + str(somme) + "\n" 
              + "Moyenne : " + str(moyenne))
fichier.close()
fichier = open("nombres.txt", "r+")
texte = fichier.read()
print(texte)
