import nltk, random
nltk.download('punkt')

# 1. Lire le fichier bovary.txt et creer une liste de mots de 5 lettres
fichier = open("bovary.txt", encoding="utf-8")
texte = fichier.read()
bovary_liste = nltk.word_tokenize(texte)
mots = []
for i in bovary_liste:
    if len(i) == 5 and i.__contains__("'")==False and i.__contains__("-")==False:
        mots.append(i)


# 2. Debut du jeu
nombreDeVie = 6
vieCourante = 0
motEssai:str
# random.choice(mots).lower()
motHasard = "allee"
print(motHasard, "est le mot a deviner")
while (vieCourante != nombreDeVie) :
    print("Esssai no", vieCourante + 1)
    while True:
        motEssai = input("Entrez mot essai : ")
        if len(motEssai) == 5:
            break
    if (motEssai == motHasard) :
        print("Bravo, vous avez gagne")
        break
    else :
        for position in range(0,len(motEssai)) :
            if motEssai[position] == motHasard[position] :
                print(motEssai[position], "✔ ")
            elif motEssai[position] in motHasard :
                print(motEssai[position], "➕")
            else :
                print(motEssai[position], "❌")
        vieCourante += 1
if (nombreDeVie == vieCourante) :
        print("Vous avez perdu, le mot etait", motHasard)