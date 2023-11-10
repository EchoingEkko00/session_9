from ADC_Composant import * # Assurez-vous qu’il soit présent
import time, sys
from PCF8574 import *
from Adafruit_LCD1602 import *
from gpiozero import PWMLED

# Initialization for ADC
adc = ADC_Composant() # Déclare un convertisseur
if(adc.detecteI2C(0x4b)): # Le détecte
 adc = ADS7830()
else:
 sys.exit("I2C non connecté sur votre Pi et/ou ADS7830")

#LCD screen
pcf = PCF8574_GPIO(0x27)
pcf.output(3,1)
lcd = Adafruit_CharLCD(pin_rs = 0, pin_e = 2, pins_db = [4,5,6,7], GPIO = pcf)
lcd.numlines = 2
lcd.begin(0, 0)
lcd.message("Bonjour")

#LED
calorifere = PWMLED(12)

#RGB LED
ampoule = PWMLED(25)

# Thermo resistance plus c'est chaud, le Vpot est plus petit
# Photo resistance plus c'est lumineux, le Vpot est petit


actualPhotoResistance = 0
actualThermoResistance = 0
equilibrePhotoResistance = [0,100,0.5]
equilibreThermoResistance = [0,100,0.5]
actualPotentiometre = 0
moyennePhotoResistance = []
moyenneThermoResistance = []
moyennePotentiometre = []
ADC_max = 255
ADC_min = 0
PWM_max = 1


def afficherTemperature():
    textTempature = "T  {equilibre:>{width}.0f} {actual:>{width}.0f}  {value:>{width}.2f}"
    lcd.setCursor(0,0)
    lcd.message(textTempature.format(equilibre = equilibreThermoResistance[1], actual = actualThermoResistance, value = calorifere.value, width=3))

def afficherPhoto():
    textPhoto = "P  {equilibre:>{width}.0f} {actual:>{width}.0f}  {value:>{width}.2f}"
    lcd.setCursor(0,1)
    lcd.message(textPhoto.format(equilibre = equilibrePhotoResistance[1], actual = actualPhotoResistance, value = ampoule.value, width=3))

def calculateAmpoule():
    if actualPhotoResistance == round(equilibrePhotoResistance[0]):
        return equilibrePhotoResistance[2]
    elif actualPhotoResistance > equilibrePhotoResistance[0]:
        return equilibrePhotoResistance[2] + equilibrePhotoResistance[2] * ((actualPhotoResistance - equilibrePhotoResistance[0]) / (ADC_max - equilibrePhotoResistance[0]))
    else:
        return actualPhotoResistance * equilibrePhotoResistance[2] / equilibrePhotoResistance[0]

def calculateCarolifere():
    if actualThermoResistance == round(equilibreThermoResistance[0]):
        return equilibreThermoResistance[2]
    elif actualThermoResistance > equilibreThermoResistance[0]:
        return equilibreThermoResistance[2] + equilibreThermoResistance[2] * ((actualThermoResistance - equilibreThermoResistance[0]) / (ADC_max - equilibreThermoResistance[0]))
    else:
        return actualThermoResistance * equilibreThermoResistance[2] / equilibreThermoResistance[0]

try:
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.message("Calibrage en")
    lcd.setCursor(0,1)
    lcd.message("Cours...")
    ampoule.on()
    ampoule.value = equilibrePhotoResistance[2]
    calorifere.on()
    calorifere.value = equilibreThermoResistance[2]
    for i in range(0, 20):
        moyennePhotoResistance.append(ADC_max - adc.lectureAnalogique(0))
        moyenneThermoResistance.append(ADC_max - adc.lectureAnalogique(1))
        time.sleep(0.5)
    equilibrePhotoResistance[0] = sum(moyennePhotoResistance) / len(moyennePhotoResistance)
    equilibreThermoResistance[0] = sum(moyenneThermoResistance) / len(moyenneThermoResistance)
    # equilibrePhotoResistance = 100
    # equilibreThermoResistance = 100
    lcd.clear()
    while True :
        actualPhotoResistance = ADC_max - adc.lectureAnalogique(0)
        actualThermoResistance = ADC_max - adc.lectureAnalogique(1)
        thermostat = ADC_max - adc.lectureAnalogique(2)
        equilibreThermoResistance[0] = thermostat
        ampoule.value = PWM_max - calculateAmpoule()
        calorifere.value = PWM_max - calculateCarolifere()
        afficherTemperature()
        afficherPhoto()
except KeyboardInterrupt:
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.message("Au revoir")
    sleep(2)
    lcd.clear()
    ampoule.off()
    calorifere.off()
    print("Au revoir")
    sys.exit(0)
except Exception as e:
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.message("Un fil s'est debranché")
    sleep(2)
    lcd.clear()
    ampoule.off()
    calorifere.off()
    print("Un fil s'est debranché")
    sys.exit(0)
    

