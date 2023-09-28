from gpiozero import LED
from time import sleep

ledrouge = LED(17)
ledjaune = LED(27)
ledvert = LED(22)
while True:
    ledrouge.on()
    sleep(10)
    ledrouge.off()

    ledjaune.on()
    ledrouge.on()
    sleep(2)
    ledjaune.off()
    ledrouge.off()

    ledvert.on()
    sleep(14)
    ledvert.off()

    #Make the ledvert blink during 10 seconds
    ledvert.blink(0.5,0.5)
    sleep(10)
    ledvert.off()

    ledjaune.on()
    sleep(3)
    ledjaune.off()