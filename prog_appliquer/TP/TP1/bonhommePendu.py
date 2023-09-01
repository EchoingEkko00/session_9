import nltk, random
nltk.download('punkt')

# Lire le fichier bovary.txt et creer une liste de mots de 5 lettres
fichier = open("bovary.txt", encoding="utf-8")
texte = fichier.read()
bovary_liste = nltk.word_tokenize(texte)
mots = []
for i in bovary_liste:
    if len(i) == 5 and i.__contains__("'")==False and i.__contains__("-")==False:
        mots.append(i)
