# Turtle 2 : dessins de formes colorées

from turtle import * 
import keyboard

tortue = Turtle()

# Premier cercle bleu au-dessus du point central
tortue.fillcolor("blue")
tortue.pencolor("blue")
tortue.goto(0,0)
tortue.pendown()   
tortue.begin_fill()
tortue.circle(50)  # Cercle de rayon 50
tortue.end_fill()
# Deuxième cercle vide avec bordure rouge au dessus du premier cercle
tortue.fillcolor("")
tortue.pencolor("red")
tortue.penup()
tortue.goto(0,100)
tortue.pendown()   
tortue.begin_fill()
tortue.circle(50)
tortue.end_fill()
# Un rectangle vert en-dessous du premier cercle
tortue.penup()
tortue.goto(-50, -100)
tortue.pendown()
tortue.fillcolor("green")
tortue.pencolor("green")
tortue.begin_fill()
for _ in range(4):
    tortue.forward(100)
    tortue.left(90)
tortue.end_fill()
tortue.hideturtle()

keyboard.wait('q')
quit()