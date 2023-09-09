from turtle import *
import keyboard
# Création de la fenêtre

tortue = Turtle()
longeur = 5
# Création du labyrinthe
tortue.pencolor("red")
tortue.goto(0,0)
tortue.pendown()
tortue.pensize(1)
for i in range(26):
    tortue.forward(longeur)
    tortue.left(90)
    tortue.forward(longeur)
    tortue.left(90)
    longeur = longeur + 5

keyboard.wait('esc')
quit()
