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


# Debut du jeu
nombreDeVie = 6
vieCourante = 0
motEssai:str
playing = True
while playing:
    motHasard = random.choice(mots).lower()
    print(motHasard, "est le mot a deviner")
    while (vieCourante != nombreDeVie) :
        print("Esssai no", vieCourante + 1)
        while True:
            motEssai = input("Entrez mot essai : ").lower()
            if len(motEssai) == 5:
                break
        listeLettre = list(motHasard)
        if (motEssai == motHasard) :
            print("Bravo, vous avez gagne")
            break
        else :
            for position in range(0,len(motEssai)) :
                if motEssai[position] == motHasard[position] and listeLettre.__contains__(motEssai[position]) :
                    print(motEssai[position], "✔ ")
                    listeLettre.remove(motEssai[position])
                elif motEssai[position] in motHasard and listeLettre.__contains__(motEssai[position]) :
                    print(motEssai[position], "➕")
                    listeLettre.remove(motEssai[position])
                else :
                    print(motEssai[position], "❌")
            vieCourante += 1
    if (nombreDeVie == vieCourante) :
        print("Vous avez perdu, le mot etait", motHasard)
    print("Voulez-vous rejouer ?")
    reponse = input("Oui ou Non ? ").lower()
    if reponse == "oui" or reponse == "o" :
        vieCourante = 0
    else :
        print("Programme terminer!")
        playing = False