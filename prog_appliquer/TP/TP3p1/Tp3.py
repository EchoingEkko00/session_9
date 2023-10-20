from threading import Thread
from gpiozero import MotionSensor, DistanceSensor, RGBLED, Buzzer
import adafruit_dht
import psutil
from time import sleep
from turtle import *

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

distanceSensor = DistanceSensor(echo=24, trigger=23)
motionDetector = MotionSensor(25)
rgbLed = RGBLED(red=13, green=19, blue=26, active_high=False)
humiditySensor = adafruit_dht.DHT11(21)
buzzer = Buzzer(6)

numberOfSeconds = 0
waitingSeconds = 1
coleur = ""
programStarted = False
turtle = Turtle()


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
    global rgbLed
    rgbLed.color = (0, 0, 0)
    rgbLed.close()
    programStarted = False
    print("Le programme est maintenant arrêté")
    proc.kill()

def getClick(x,y):
    global WaitingSeconds
    global numberOfSeconds
    if x >= -450 and x <= -250 and y >= -100 and y <= 100:
        addWaitingSeconds()
    elif x >= -200 and x <= 0 and y >= -100 and y <= 100:
        removeWaitingSeconds()
    elif x >= 50 and x <= 250 and y >= -100 and y <= 100:
        stopProgram()


def program():
    global distanceSensor
    global motionDetector
    global rgbLed
    global humiditySensor
    global buzzer

    global numberOfSeconds
    global waitingSeconds
    global coleur
    programStarted = False
    while True:
        sleep(1)
        print("Faite un mouvement pour commencer le programme")
        programStarted = motionDetector.wait_for_motion()
        while programStarted:
            if (numberOfSeconds == 0):
                numberOfSeconds = 1
                print("Merci, c'est parti!")
                buzzer.beep(0.1, 0.1, 1)
            try:
                temp = humiditySensor.temperature
                humidity = humiditySensor.humidity
                distance = distanceSensor.distance
                if distance * 100 < 10:
                    rgbLed.color = (1, 0, 0)
                    couleur = "rouge"
                elif distance * 100 <= 30 and distance * 100 >= 10:
                    rgbLed.color = (1, 1, 0)
                    couleur = "jaune"
                else:
                    rgbLed.color = (0, 1, 0)
                    couleur = "vert"
                print("Seconde " + str(numberOfSeconds) + " : Temperature: {}° Humidity: {}% ".format(temp, humidity) + "Distance: {} m".format(distance) + " La RGBLED est " + couleur)
            except RuntimeError as error:
                print(error.args[0])
                continue
            except Exception as error:
                humiditySensor.exit()
                raise error
            numberOfSeconds += waitingSeconds
            sleep(waitingSeconds)
        if programStarted == False:
            break

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
turtle.goto(-425, -50)
turtle.write("+ 0.1 seconde", font=("Arial", 20, "normal"))

turtle.goto(-200, 0)
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
turtle.goto(-175, -50)
turtle.write("- 0.1 seconde", font=("Arial", 20, "normal"))

turtle.goto(50, 0)
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
turtle.goto(65, -75)
turtle.write("Arreter la \r surveillance", font=("Arial", 20, "normal"))
onscreenclick(getClick,1)

#Start program as a thread and start turtle program
thread = Thread(target=program)
thread.start()
mainloop()


