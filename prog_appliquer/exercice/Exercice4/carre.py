from turtle import *
import keyboard

tortue = Turtle()
tortue.pencolor("red")
tortue.pensize(1)
tortue.goto(0,0)
tortue.pendown()
longeurTotal = 100
nombreDeDents = int(input("Combien de dents voulez-vous ?"))
longeur = longeurTotal/nombreDeDents*2
for i in range(4):
    for j in range(nombreDeDents):     
        tortue.forward(longeur)
        tortue.left(90)
        tortue.forward(longeur)
        tortue.right(90)
        tortue.forward(longeur)
        tortue.right(90)
        tortue.forward(longeur)
        tortue.left(90)
    tortue.forward(longeur)
    tortue.right(90)
keyboard.wait('esc')
quit()