import turtle
WaitingSeconds = 1
numberOfSeconds = 1


#Turtle program that have one container which add 0.1 second in waitingSeconds, another container which remove 0.1 seconds in waitingSeconds and a last container which stop the program
def addWaitingSeconds():
    global waitingSeconds
    waitingSeconds += 0.1
    print("Le temps d'attente est maintenant de " + str(waitingSeconds) + " secondes")

def removeWaitingSeconds():
    global waitingSeconds
    if waitingSeconds > 0.1:
        waitingSeconds -= 0.1
        print("Le temps d'attente est maintenant de " + str(waitingSeconds) + " secondes")
    else:
        print("Le temps d'attente ne peut pas être plus petit que 0.1 secondes")

def stopProgram():
    global programStarted
    programStarted = False
    print("Le programme est maintenant arrêté")

#Turtle program that have one square clickable which add 0.1 second in waitingSeconds with a label (+ 0.1 seconde), another square clickable which remove 0.1 seconds in waitingSeconds with a label (- 0.1 seconde) and a last sqaure clickable which stop the program with a label (Arret de la surveillance)
turtle.setup(1000, 1000)
turtle.title("Surveillance")
turtle.bgcolor("white")
turtle.color("black")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
#Draw a rectangle on the middle left of the screen
turtle.goto(-450, 0)
for i in range(4):
    turtle.pendown()
    if i % 2 == 0:
        turtle.forward(200)
    else:
        turtle.forward(100)
    turtle.right(90)
    turtle.penup()
#Write label in the middle of the square
turtle.penup()
turtle.goto(-425, -75)
turtle.write("+ 0.1 seconde", font=("Arial", 20, "normal"))


turtle.mainloop()


