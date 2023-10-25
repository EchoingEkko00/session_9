from ADC_Composant import * # Assurez-vous qu’il soit présent
import RPi.GPIO as GPIO
import time, sys
import smbus

class ADC_Composant(object):
    def __init__(self):
        self.cmd = 0
        self.address = 0
        self.bus=smbus.SMBus(1)
        
    def detecteI2C(self,addr):
        try:
            self.bus.write_byte(addr,0)
            print("Composante trouvée à l'adresse 0x%x"%(addr))
            return True
        except:
            print("Composante non trouvée à l'adresse 0x%x"%(addr))
            return False
            
    def close(self):
        self.bus.close()

class ADS7830(ADC_Composant):
    def __init__(self):
        super(ADS7830, self).__init__()
        self.cmd = 0x84
        self.address = 0x4b # 0x4b est l'adresse i2c par défaut pour la composante ADS7830.   
        
    def lectureAnalogique(self, chn): # ADS7830 broches d'entrée: 0,1,2,3,4,5,6,7
        value = self.bus.read_byte_data(self.address, self.cmd|(((chn<<2 | chn>>1)&0x07)<<4))
        return value

listeLeds = [5,6,13,19,26,12,16,20,21,25]
nbLeds = len(listeLeds)
adc = ADC_Composant() # Déclare un convertisseur 
if(adc.detecteI2C(0x4b)): # Le détecte
    adc = ADS7830()
else:
    sys.exit("I2C non connecté sur votre Pi et/ou ADS7830")
GPIO.setmode(GPIO.BCM) # nomenclature GPIO pour les numéros de broches
GPIO.setup(listeLeds,GPIO.OUT) # on met la broche en mode sortie
GPIO.output(listeLeds,GPIO.HIGH) # on l’allume (HIGH = 3.3 volts)
time.sleep(2)
GPIO.output(listeLeds,GPIO.LOW) # on l’allume (HIGH = 3.3 volts)

def animation() :
    global listeLeds
    global whichLed

    for i in range(whichLed) :
            GPIO.output(listeLeds[i],GPIO.HIGH)
            time.sleep(0.1)
    for i in range(whichLed) :
        GPIO.output(listeLeds[whichLed-i-1],GPIO.LOW)
        time.sleep(0.1)
try :
    while True:
        v5 = adc.lectureAnalogique(0) # on lit le canal A0 sur le convertisseur
        vPot = adc.lectureAnalogique(1)
        print("v5 : " + str(v5))
        if v5 != 0 :
            whichLed = int(round(v5/(255/nbLeds)))
        else :
            whichLed = 0
        print("numero de la led : " + str(whichLed))
        if (whichLed == 0) :
            GPIO.output(listeLeds,GPIO.LOW)
            time.sleep(1)
        else :
            animation()
except KeyboardInterrupt:
    print("Attrape Ctrl-C")
except Exception as e:
    print("Erreur inattendue...")
    print(str(e))
finally:
    print("Fin du programme")
    adc.close()
    GPIO.cleanup()
    sys.exit(0)


