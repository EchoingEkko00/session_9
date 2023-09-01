# Turtle 4 : une course entre quatre tortues
from turtle import *
from random import randint
from time import sleep
import keyboard

# Fenêtre principale
setup(800, 500)
title("COURSE de TORTUES")
bgcolor("green")

tortue = Turtle()
tortue.speed(0)

# EN-TÊTE
tortue.penup()
tortue.goto(0, 200)
tortue.color("white")
tortue.write("COURSE de TORTUES", font=("Arial", 20, "bold"), align = 'center')

# PISTE
tortue.goto(-350, 200)
tortue.pendown()
tortue.color("brown")
tortue.begin_fill()
for _ in range(2):
    tortue.forward(600)
    tortue.right(90)
    tortue.forward(400)
    tortue.right(90)
tortue.end_fill()

# LIGNE D'ARRIVÉE

tortue.goto(250, 200)
tortue.pendown()
tortue.color("yellow")
tortue.begin_fill()
for _ in range(2):
    tortue.forward(100)
    tortue.right(90)
    tortue.forward(400)
    tortue.right(90)
tortue.end_fill()

tortue.hideturtle()

# TORTUE 1 - BLEU
tortue_bleu = Turtle()
tortue_bleu.color("cyan")
tortue_bleu.shape("turtle")
tortue_bleu.shapesize(1.5)
tortue_bleu.penup()
tortue_bleu.goto(-300, 150)
tortue_bleu.pendown()
    
# TORTUE 2 - ROSE
tortue_rose = Turtle()
tortue_rose.color("magenta")
tortue_rose.shape("turtle")
tortue_rose.shapesize(1.5)
tortue_rose.penup()
tortue_rose.goto(-300, 50)
tortue_rose.pendown()    
    
# TORTUE 3 - JAUNE
tortue_jaune = Turtle()
tortue_jaune.color("yellow")
tortue_jaune.shape("turtle")
tortue_jaune.shapesize(1.5)
tortue_jaune.penup()
tortue_jaune.goto(-300, -50)
tortue_jaune.pendown()    
  
# TORTUE 4 - VERTE
tortue_verte = Turtle()
tortue_verte.color("lime")
tortue_verte.shape("turtle")
tortue_verte.shapesize(1.5)
tortue_verte.penup()
tortue_verte.goto(-300, -150)
tortue_verte.pendown()    

# PAUSE DE 1 SECONDE AVANT LE DÉPART
sleep(1)

# ON FAIT BOUGER LES TORTUES
while tortue_bleu.xcor() <= 250 and tortue_rose.xcor() <= 250 and tortue_jaune.xcor() <= 250 and tortue_verte.xcor() <= 250 :
    tortue_bleu.forward(randint(3,8))
    tortue_rose.forward(randint(1,10))
    tortue_jaune.forward(randint(1,10))
    tortue_verte.forward(randint(1,10))

# CÉLÉBRATION DU GAGNANT : UN TOUR SUR LUI-MÊME
# LA TORTUE BLEUE CÉLÈBRE
if tortue_bleu.xcor() > tortue_rose.xcor() and tortue_bleu.xcor() > tortue_jaune.xcor() and tortue_bleu.xcor() > tortue_verte.xcor() :
    print("La tortue bleue gagne!")
    for i in range(72):
        tortue_bleu.right(5)
        tortue_bleu.shapesize(2.5)
# LA TORTUE ROSE CÉLÈBRE
elif tortue_rose.xcor() > tortue_bleu.xcor() and tortue_rose.xcor() > tortue_jaune.xcor() and tortue_rose.xcor() > tortue_verte.xcor() :
    print("La tortue rose gagne!")
    for i in range(72):
        tortue_rose.right(5)
        tortue_rose.shapesize(2.5)
# LA TORTUE VERTE CÉLÈBRE
elif tortue_verte.xcor() > tortue_rose.xcor() and tortue_verte.xcor() > tortue_jaune.xcor() and tortue_verte.xcor() > tortue_bleu.xcor() :
    print("La tortue verte gagne!")
    for i in range(72):
        tortue_verte.right(5)
        tortue_verte.shapesize(2.5)
# LA TORTUE JAUNE CÉLÈBRE
else:
    print("La tortue jaune gagne!")
    for i in range(72):
        tortue_jaune.right(5)
        
keyboard.wait('q')
quit()