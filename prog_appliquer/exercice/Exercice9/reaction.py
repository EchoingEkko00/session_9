from gpiozero import Button, LED
from time import sleep
import random

led = LED(17)

joueur_1 = Button(26)
joueur_2 = Button(13)

delai = random.uniform(5, 10)
print("C'est parti!")
sleep(delai)
led.on()

while True:
    if joueur_1.is_pressed:
        print("Joueur 1 gagne!")
        break
    if joueur_2.is_pressed:
        print("Joueur 2 gagne!")
        break

led.off()

