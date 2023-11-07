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


#Try to read vPot
actualPhotoResistance = 0
actualThermoResistance = 0
equilibrePhotoResistance = 0
equilibreThermoResistance = 0
moyennePhotoResistance = []
moyenneThermoResistance = []

def afficherTemperature():
    textTempature = "T  {equilibre:>{width}.0f} {actual:>{width}.0f}  {value}"
    lcd.setCursor(0,0)
    lcd.message(textTempature.format(equilibre = equilibreThermoResistance, actual = actualThermoResistance, value = calorifere.value, width=3))

def afficherPhoto():
    textPhoto = "P  {equilibre:>{width}.0f} {actual:>{width}.0f}  {value}"
    lcd.setCursor(0,1)
    lcd.message(textPhoto.format(equilibre = equilibrePhotoResistance, actual = actualPhotoResistance, value = ampoule.value, width=3))


lcd.clear()
lcd.setCursor(0,0)
lcd.message("Calibrage en")
lcd.setCursor(0,1)
lcd.message("Cours...")
ampoule.on()
ampoule.value = 0.5
for i in range(0, 20):
    moyennePhotoResistance.append(adc.lectureAnalogique(0))
    moyenneThermoResistance.append(adc.lectureAnalogique(1))
    time.sleep(0.5)
equilibrePhotoResistance = sum(moyennePhotoResistance) / len(moyennePhotoResistance)
equilibreThermoResistance = sum(moyenneThermoResistance) / len(moyenneThermoResistance)
lcd.clear()
while True :
    actualPhotoResistance = adc.lectureAnalogique(0)
    actualThermoResistance = adc.lectureAnalogique(1)
    afficherTemperature()
    afficherPhoto()
    
    

