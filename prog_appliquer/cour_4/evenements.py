# Turtle 3 : Gestion d'événements (clics)

from turtle import *
import keyboard

tortue = Turtle()

DEDANS = "dedans!"
DEHORS = "dehors!"

# Fonction qui va s'occuper des clics
def attrapeClic(x, y): # x et y sont les coordonnées du clic
    global DEDANS, DEHORS 	# inutile ici puisqu'on ne les modifie pas et
                            # en plus ce sont des constantes, mais autrement
                            # il faut préciser qu'elles sont globales
    if x >= -50 and x <= 50 and y >= -50 and y <= 50:
        print(DEDANS)
    else:
        print(DEHORS)
   
# On déclare quelle méthode va attraper les clics gauches
onscreenclick(attrapeClic,1) # 1: clic gauche

# on dessine un rectangle rouge en plein centre
col = "red"
tortue.fillcolor(col)
tortue.speed(1)
tortue.goto(-50, -50)
tortue.fillcolor('red')
tortue.begin_fill()
for _ in range(4):
    tortue.forward(100)
    tortue.left(90)
tortue.end_fill()

tortue.hideturtle()

mainloop() # pour garder le programme actif, sinon il s'arrête





