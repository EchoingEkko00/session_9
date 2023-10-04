# Turtle: Gestion d'événements (clics) avec threading
from turtle import *
import threading
import time
from gpiozero import LED, Button, Buzzer

tortue = Turtle()
led = True
buzzer = Buzzer(2)
bit1 = LED(3)
bit2 = LED(4)
bit3 = LED(17)
bit4 = LED(27)
bit5 = LED(22)
bit6 = LED(10)
bit7 = LED(9)
bit8 = LED(11)
rgbRed = LED(16)
rgbGreen = LED(20)
rgbBlue = LED(21)
rgbRed.on()
rgbGreen.on()
rgbBlue.on()

# Définir une fonction qui tournera dans son propre thread
def autre_tache():
    # Fonction qui va s'occuper des clics
    def attrapeClic(x, y): # x et y sont les coordonnées du clic
        global led
        if x >= -100 and x <= 0 and y >= 0 and y <= 100:
            led = True
        elif x >= 10 and x <= 110 and y >= 0 and y <= 100:
            led = False
    # On déclare quelle méthode va attraper les clics gauches
    onscreenclick(attrapeClic,1) # 1: clic gauche
    # on dessine un rectangle rouge en plein centre
    col = 'blue'
    tortue.speed(0)
    tortue.goto(-100, 0)
    tortue.fillcolor(col)
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(100)
        tortue.left(90)
    tortue.end_fill()
    tortue.goto(-50, 0)
    tortue.write("ON", align="center", font=("Arial", 12, "bold"))
    tortue.penup()

    tortue.goto(10, 0)
    tortue.pendown()
    tortue.fillcolor('red')
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(100)
        tortue.left(90)
    tortue.end_fill()
    tortue.goto(60, 0)
    tortue.write("OFF", align="center", font=("Arial", 12, "bold"))
    tortue.hideturtle()
    while True:
        if led:
            rgbRed.on()
            rgbGreen.off()
            rgbBlue.on()
            bit1.on()
            bit2.on()
            bit3.on()
            bit4.on()
            bit5.on()
            bit6.on()
            bit7.on()
            bit8.on()
            buzzer.on()
        else:
            rgbRed.on()
            rgbGreen.on()
            rgbBlue.on()
            bit1.off()
            bit2.off()
            bit3.off()
            bit4.off()
            bit5.off()
            bit6.off()
            bit7.off()
            bit8.off()
            buzzer.off()


# Créer un thread pour une autre tâche
autre_tache_thread = threading.Thread(target = autre_tache)

# Démarrer l'autre thread
autre_tache_thread.start()

mainloop() # pour garder le programme actif, sinon il s'arrête
