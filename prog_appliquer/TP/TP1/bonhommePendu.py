import nltk, random
from turtle import *
import keyboard
nltk.download('punkt')

# Lire le fichier bovary.txt et creer une liste de mots de 5 lettres
fichier = open("bovary.txt", encoding="utf-8")
texte = fichier.read()
bovary_liste = nltk.word_tokenize(texte)
mots = []
for i in bovary_liste:
    if len(i) == 5 and i.__contains__("'")==False and i.__contains__("-")==False:
        mots.append(i)

#Dessin du jeu bonhomme pendu
nombreDeLettreTotal = 5

turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)
turtle.fillcolor("black")
turtle.pensize(2)

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
positionPenduX = turtle.xcor()
positionPenduY = turtle.ycor()

positionX = -300
turtle.left(90)
for i in range(0,nombreDeLettreTotal):
    turtle.penup()
    turtle.goto(positionX,-250)
    turtle.pendown()
    turtle.forward(75)
    turtle.penup()
    positionX += 100
    turtle.goto(positionX,-250)


nombreDeVie = 6
vieCourante = 0
lettreEssai:str
playing = True
while playing:
    motHasard = "abaaa".upper()
    print(motHasard, "est le mot a deviner")
    while (vieCourante != nombreDeVie) :
        while True:
            lettreEssai = input("Entrez lettre essai : ").upper()
            if len(lettreEssai) == 1:
                break
        listeLettre = list(motHasard)
        if (lettreEssai in motHasard and listeLettre.count(lettreEssai) >= 1) :
            positionLettre = 0
            for i in range(0,listeLettre.count(lettreEssai)):
                positionLettre = listeLettre.index(lettreEssai,positionLettre)
                for i in range(0,len(motHasard)):
                    if positionLettre == i:
                        turtle.goto(-300 + (i*100),-250)
                        turtle.write(lettreEssai, font=("Arial", 80, "normal"))
                positionLettre += 1
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
    if (nombreDeVie == vieCourante) :
        print("Vous avez perdu, le mot etait", motHasard)
    print("Voulez-vous rejouer ?")
    reponse = input("Oui ou Non ? ").lower()
    if reponse == "oui" or reponse == "o" :
        vieCourante = 0
    else :
        print("Programme terminer!")
        playing = False
        quit()
keyboard.wait('esc')
quit()