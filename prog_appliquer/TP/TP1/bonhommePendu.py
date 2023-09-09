import nltk, random
from turtle import *
import keyboard
nltk.download('punkt')

# Lire le fichier bovary.txt et creer une liste de mots de 5 lettres
fichier = open("bovary.txt", encoding="utf-8")
texte = fichier.read()
fichier.close()
bovary_liste = nltk.word_tokenize(texte)
mots = []
for i in bovary_liste:
    if len(i) == 5 and i.__contains__("'")==False and i.__contains__("-")==False:
        mots.append(i)

#Dessin du jeu bonhomme pendu
nombreDeLettreTotal = 5
positionPenduX:int
positionPenduY:int
turtle = Turtle()

def dessinBonhommePendu() -> Vec2D:
    turtle.hideturtle()
    turtle.speed(0)
    turtle.fillcolor("black")
    turtle.pensize(2)

    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-50,0)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(350)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    position = turtle.position()

    turtle.left(90)
    positionX = -300
    for i in range(0,nombreDeLettreTotal):
        turtle.penup()
        turtle.goto(positionX,-250)
        turtle.pendown()
        turtle.forward(75)
        turtle.penup()
        positionX += 100
        turtle.goto(positionX,-250)
    return position

vecteurPosition = dessinBonhommePendu()
positionPenduX = vecteurPosition[0]
positionPenduY = vecteurPosition[1]


nombreDeVie = 6
vieCourante = 0
lettreEssai:str
playing = True
while playing:
    motHasard = random.choice(mots).upper()
    dictLettre = {}
    for i in range(0,len(motHasard)):
        dictLettre[i] = motHasard[i]
    while True:
        niveauDifficulte = input("Entrez le niveau de difficulte (1 ou 2) : ")
        if (niveauDifficulte.isnumeric() == False):
            continue
        if int(niveauDifficulte) == 1 or int(niveauDifficulte) == 2:
            niveauDifficulte = int(niveauDifficulte)
            break
    while (vieCourante != nombreDeVie) :
        while True:
            lettreEssai = input("Entrez lettre essai : ").upper()
            if len(lettreEssai) == 1:
                break
        if (lettreEssai in motHasard and lettreEssai in dictLettre.values() and niveauDifficulte == 1) :
            for i in range(0,len(motHasard)):
                if lettreEssai == dictLettre.get(i):
                    turtle.goto(-300 + (i*100),-250)
                    turtle.write(lettreEssai, font=("Arial", 80, "normal"))
                    dictLettre.pop(i)
        elif (lettreEssai in motHasard and lettreEssai in dictLettre.values() and niveauDifficulte == 2) :
            for i in range(0,len(motHasard)):
                if lettreEssai == dictLettre.get(i):
                    turtle.goto(-300 + (i*100),-250)
                    turtle.write(lettreEssai, font=("Arial", 80, "normal"))
                    dictLettre.pop(i)
                    break
        else  : 
            #Dessin du bonhomme pendu etape par etape selon le nombre de vie restante
            if vieCourante == 0:
                #Dessin de la tete
                turtle.goto(positionPenduX,positionPenduY)
                turtle.right(180)
                turtle.pendown()
                turtle.circle(50)
                turtle.penup()
            elif vieCourante == 1:
                #Dessin du corps
                turtle.left(90)
                positionPenduY = positionPenduY - 100
                turtle.goto(positionPenduX, positionPenduY)
                turtle.pendown()
                turtle.forward(100)
                turtle.penup()
            elif vieCourante == 2:
                #Dessin du bras gauche
                turtle.goto(positionPenduX,positionPenduY)
                turtle.right(45)
                turtle.pendown()
                turtle.forward(100)
                turtle.penup()
                turtle.right(-45)
            elif vieCourante == 3:
                #Dessin du bras droit
                turtle.goto(positionPenduX,positionPenduY)
                turtle.left(45)
                turtle.pendown()
                turtle.forward(100)
                turtle.penup()
                turtle.left(-45)
            elif vieCourante == 4:
                #Dessin de la jambe gauche
                positionPenduY = positionPenduY - 100
                turtle.goto(positionPenduX,positionPenduY)
                turtle.right(45)
                turtle.pendown()
                turtle.forward(100)
                turtle.penup()
                turtle.right(-45)
            elif vieCourante == 5:
                #Dessin de la jambe droite
                turtle.goto(positionPenduX,positionPenduY)
                turtle.left(45)
                turtle.pendown()
                turtle.forward(100)
                turtle.penup()
                turtle.left(-45)
            vieCourante += 1
        if (len(dictLettre) == 0) :
            print("Vous avez gagne!")
            break
    if (nombreDeVie == vieCourante) :
        print("Vous avez perdu, le mot etait", motHasard)
    print("Voulez-vous rejouer ?")
    while True:
        reponse = input("Oui ou Non ? ").lower()
        if reponse == "oui" or reponse == "o" :
            vieCourante = 0
            turtle.reset()
            vecteurPosition = dessinBonhommePendu()
            positionPenduX = vecteurPosition[0]
            positionPenduY = vecteurPosition[1]
            break
        elif reponse == "non" or reponse == "n" :
           print("Programme terminer!")
           playing = False
           quit()