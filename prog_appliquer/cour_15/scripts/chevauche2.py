from gpiozero import PWMLED, Buzzer, GPIOZeroError
from time import sleep

try:
    led = PWMLED(26)
    led.value = 0.05 # il faut entre 0 et 1
    sleep(1)
    led.off()
    led.close() # permettant la réutilisation
    bz = Buzzer(26)
    bz.on()
    sleep(1)
    bz.off()
    bz.close()
except GPIOZeroError as e:
    print('EXCEPTION')
    print(e)
    


    
    
    
    
