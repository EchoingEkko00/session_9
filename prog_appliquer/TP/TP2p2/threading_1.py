# Turtle: Gestion d'événements (clics) avec threading
from turtle import *
import keyboard, threading
from time import sleep
tortue = Turtle()
led = True
# Fonction qui va s'occuper des clics
def attrapeClic(x, y): # x et y sont les coordonnées du clic
    global led
    if x >= -50 and x <= 50 and y >= -50 and y <= 50:
        led = not led 
# On déclare quelle méthode va attraper les clics gauches
onscreenclick(attrapeClic,1) # 1: clic gauche
# on dessine un rectangle rouge en plein centre
col = 'red'
tortue.speed(0)
tortue.goto(-50, -50)
tortue.fillcolor(col)
tortue.begin_fill()
for _ in range(4):
    tortue.forward(100)
    tortue.left(90)
tortue.end_fill()
tortue.hideturtle()
# Définir une fonction qui tournera dans son propre thread
def autre_tache():
    while True:
        print("La led est " + str(led))
        sleep(1)
        # Vous pouvez mettre votre code ici
# Créer un thread pour une autre tâche
autre_tache_thread = threading.Thread(target = autre_tache)
# Démarrer l'autre thread
autre_tache_thread.start()
mainloop() # pour garder le programme actif, sinon il s'arrête
