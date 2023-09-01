# Turtle 1 : fenêtre, déplacement, écriture

from turtle import *  # Le module https://docs.python.org/fr/2/library/turtle.html#module-turtle
from time import sleep 
import keyboard  # pip install keyboard

# Préparation de l'écran
setup(1200, 500)
title("Fenêtre pour une tortue")
bgcolor("blue")

# On défini notre tortue
tortue = Turtle() # Une variable (objet) pour dessiner
tortue.speed(5) # 0 instantané (donc sans animation), 1 à 10 (de plus en plus vite)
tortue.color("red")  # blue, green, yellow, etc.
tortue.pensize(5) # Un entier positif
tortue.shape("turtle")  # Aussi arrow, circle, square, triangle, classic
tortue.color("white")
# On fait cligmoter la tortue à sa position de départ par défault (0,0). Elle pointe par défaut vers l'est.
for i in range(3):
    tortue.showturtle() # montre la tortue
    sleep(1)
    tortue.hideturtle() # la cache
    sleep(1)

# On déplace la tortue sans laisser de trace
tortue.showturtle() 
tortue.penup()
tortue.goto(0, 205)
sleep(2)
tortue.write("Un peu de texte centré à (0,250) dans la fenêtre.", font = ('Arial',12,'normal'), align = "center")
print("Un peu de texte dans la console")

# On se repositionne au centre
tortue.goto(0, 0)

sleep(2)

# On dessine un carré
tortue.pendown()  # Dépose du crayon
tortue.forward(100) # donc vers l'est
tortue.left(90) # Pointe vers le nord
tortue.penup()  # Prêt à écrire
tortue.forward(100)
tortue.left(90)  # Vers l'ouest
tortue.pendown()  
tortue.forward(100)
tortue.left(90) # Vers le sud
tortue.forward(100)
#On termine
tortue.penup()
tortue.goto(-100, -205)
tortue.hideturtle()
tortue.write("Pressez la touche 'q' pour terminer.")
# Si vous avez des problèmes de rafraîchissement, utilisez tortue.update(), cela forcera la mise-à-jour immédiate de l'écran
keyboard.wait('q')
quit() 