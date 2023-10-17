from threading import Thread
from gpiozero import MotionSensor, DistanceSensor, RGBLED, Buzzer
import adafruit_dht
import psutil
from time import sleep
from signal import pause
import turtle

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

distanceSensor = DistanceSensor(echo=24, trigger=23)
motionDetector = MotionSensor(25)
rgbLed = RGBLED(red=13, green=19, blue=26, active_high=False)
humiditySensor = adafruit_dht.DHT11(21)
buzzer = Buzzer(6)

numberOfSeconds = 1
waitingSeconds = 1
coleur = ""
programStarted = False


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
turtle.setup(500, 500)
turtle.title("Surveillance")
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)
turtle.goto(-200, 200)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.goto(-100, 100)
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.goto(50, 50)
turtle.goto(50, -50)
turtle.goto(-50, -50)
turtle.goto(-50, 50)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.goto(100, 0)
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()




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
        print("Faite un mouvement pour commencer le programme")
        programStarted = motionDetector.wait_for_motion()
        while programStarted:
            if (numberOfSeconds == 1):
                print("Merci, c'est parti!")
                buzzer.beep(0.1, 0.1, 1)
            try:
                temp = humiditySensor.temperature
                humidity = humiditySensor.humidity
                #distance in meter
                distance = distanceSensor.distance
                if distance * 100 < 10:
                    rgbLed.color = (0, 1, 1)
                    couleur = "rouge"
                elif distance * 100 <= 30 and distance * 100 >= 10:
                    rgbLed.color = (0, 0, 1)
                    couleur = "jaune"
                else:
                    rgbLed.color = (1, 0, 1)
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

#Start program as a thread and start turtle program
thread = Thread(target=program)
thread.start()
turtle.mainloop()


