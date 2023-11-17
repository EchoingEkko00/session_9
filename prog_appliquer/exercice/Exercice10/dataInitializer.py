from gpiozero import PWMLED
from ADC_Composant import * # Assurez-vous qu’il soit présent
import time, sys

# Initialization for ADC
adc = ADC_Composant() # Déclare un convertisseur
if(adc.detecteI2C(0x4b)): # Le détecte
 adc = ADS7830()
else:
 sys.exit("I2C non connecté sur votre Pi et/ou ADS7830")

ampoule = PWMLED(20)
ampoule.on()
i = 0
while True:
    ampoule.value = i
    time.sleep(5)
    print(str(i) + " " + str(adc.lectureAnalogique(0)))
    i += 0.1
    if i > 1:
        i = 0
