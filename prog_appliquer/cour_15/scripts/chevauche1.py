from gpiozero import LED, Buzzer
from time import sleep

led = LED(26)
led.on() # cela va démarrer le Buzzer aussi
sleep(1)
led.off()
led.close() # obligatoire pour libérer
            # la pin 26, sinon exception
buzzer = Buzzer(26)
buzzer.on()
sleep(1)
buzzer.off()
buzzer.close()

