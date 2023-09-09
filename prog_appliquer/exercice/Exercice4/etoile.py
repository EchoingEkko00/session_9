from turtle import *
import keyboard

tortue = Turtle()
tortue.pencolor("green")
tortue.pensize(1)
tortue.goto(0,0)
tortue.pendown()
for i in range(7):
    tortue.forward(100)
    tortue.left(180+180/7)

keyboard.wait('esc')
quit()
