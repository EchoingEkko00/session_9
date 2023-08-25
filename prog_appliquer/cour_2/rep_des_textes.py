import nltk
#préparation
#nltk.download("punkt")  # Pour la ponctuation
abs_path=__file__
print(abs_path)
print(abs_path[0:abs_path.rfind('/')])
fichier = open("bovary.txt", encoding = "utf-8")
bovary_string = fichier.read() # Python pure
bovary_liste = nltk.word_tokenize(bovary_string)
print(type(bovary_liste))
bovary_texte = nltk.Text(bovary_liste)
print(type(bovary_texte))
bovary_phrase1 = bovary_liste[10:37]
print(type(bovary_phrase1))
print(bovary_phrase1)
#Concordances
print("Voici les concordances avec 'Emma' :")
bovary_texte.concordance("Emma")
#Similarités
print("Combien de fois le mot 'beau' : ", bovary_texte.count("pauvre"))
print("Voici les similarités avec le mot 'village' : ")
bovary_texte.similar("village")
#Génération de texte aléatoire
print("Voici une génération de texte : ")
bovary_texte.generate()
#Diversité lexicale
print("Diversité lexicale : ")
print("Nombre de mots = ", len(bovary_liste))
print("Taille du dictionnaire : ", len(set(bovary_liste)))
print("Diversité lexicale = ", len(set(bovary_liste)) / len(bovary_liste))
#Autres statistiques élémentaires
print("Combien de fois le mot 'Rodolphe' : ", bovary_texte.count("Rodolphe"))
print("La première apparition du mot 'Rodolphe' : ", bovary_texte.index("Rodolphe"))
print("la proportion de 'le' dans le texte: ", 100 * bovary_texte.count("le") / len(bovary_texte))



