ma_chaine = 'Christopher William'
print((ma_chaine+" ")*3)

phrase1= "Bonjour"
phrase2= "tout le monde"
phrase3= "comment allez-vous ?"

print(len(phrase1 + phrase2 + phrase3))
print(len(phrase1) + len(phrase2) + len(phrase3))

texte = open("F:/session_9/prog_appliquer/exercice/Exercice2/bovary.txt", encoding="utf-8").read()
#. Comparez les scores de diversité lexicale pour la première et la seconde moitié du roman. Quelle moitié est le plus diversifiée sur le plan lexical ?
premiere_partie = texte[texte.rfind("PREMIÈRE PARTIE"):texte.find("DEUXIÈME PARTIE")]
premiere_partie = premiere_partie[premiere_partie.find("I\n")+3:]
print(len(set(premiere_partie.split())))
deuxieme_partie = texte[texte.rfind("DEUXIÈME PARTIE"):texte.rfind("TROISIÈME PARTIE")]
deuxieme_partie = deuxieme_partie[deuxieme_partie.find("I\n")+3:]
print(len(set(deuxieme_partie.split())))

#Trouvez tous les mots dans le roman commençant par la lettre b. Montrez-les par ordre alphabétique.
print(sorted(set([mot for mot in texte.split() if mot.startswith("b")])))

#En utilisant l'addition de listes, les opérations ensemblistes et de tri, donnez le vocabulaire des trois premières phrases du roman.
indexPhrase = texte.find(".")+1
phrase1 = texte[texte.find("I\n")+3:indexPhrase]
_ = indexPhrase
indexPhrase = texte.find(".", _)+1
phrase2 = texte[_: indexPhrase]
_ = indexPhrase
indexPhrase = texte.find(".", _)+1
phrase3 = texte[_: indexPhrase]
vocabulairePhrases = sorted(set(phrase1.split()+phrase2.split()+phrase3.split()))
print(vocabulairePhrases)

#Donnez l'expression qui extrait les deux derniers mots du roman.
indexdernierMot = texte.rfind(" ")
dernierMot = texte[indexdernierMot+1:texte.rfind(".")]
indexpremierMot = texte.rfind(" ", 0, indexdernierMot)
premierMot = texte[indexpremierMot+1:indexdernierMot]
print(premierMot+" "+dernierMot)

#Utilisez une combinaison d'instructions for et if pour parcourir les mots du roman et imprimez tous les mots débutant avec une majuscule, un par ligne.
for mot in texte.split():
    if mot[0].isupper():
        print(mot)


bovary_liste = set(texte.split())
print(sum(len(mot) for mot in bovary_liste))