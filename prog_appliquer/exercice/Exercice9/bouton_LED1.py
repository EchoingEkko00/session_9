from gpiozero import LED, Button
from signal import pause
import sys

led = LED(17)
button = Button(26)
compteur = 3
def allumerLED():
    global compteur
    led.on()
    compteur-=1
    print("Presse # "  + str(compteur))
def eteindreLED(l,s):
    global compteur
    l.off()
    print(s + " éteint!")
    if (compteur == 0):
        sys.exit()
        
button.when_pressed = allumerLED # ou encore led.on sans ()
button.when_released = lambda : eteindreLED(led,"bouton ") # avec des arguments
# Python fonction lambda:
# fonction = lambda a,b:a + b
# print(fonction(1,2)) # affiche 3
print("C'est parti!")
pause()
