from ADC_Composant import * # Assurez-vous qu’il soit présent
import RPi.GPIO as GPIO
import time, sys
adc = ADC_Composant() # Déclare un convertisseur 
if(adc.detecteI2C(0x4b)): # Le détecte
    adc = ADS7830()
else:
    sys.exit("I2C non connecté sur votre Pi et/ou ADS7830")
GPIO.setmode(GPIO.BCM) # nomenclature GPIO pour les numéros de broches
GPIO.setup(5,GPIO.OUT) # on met la broche en mode sortie
GPIO.output(5,GPIO.HIGH) # on l’allume (HIGH = 3.3 volts)
v5 = adc.lectureAnalogique(0) # on lit le canal A0 sur le convertisseur
vPot = adc.lectureAnalogique(1)
print(str(v5) + " " + str(vPot))
print("C'est le moment de faire varier votre potentiomètre ...")
time.sleep(3)
GPIO.output(5,GPIO.LOW)
v5 = adc.lectureAnalogique(0)
vPot = adc.lectureAnalogique(1)
print(str(v5) + " " + str(vPot))
GPIO.cleanup()
