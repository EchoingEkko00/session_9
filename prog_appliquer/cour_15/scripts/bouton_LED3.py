from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(26)

print("C'est parti!")
while True:
    led.value = button.value
    sleep(0.01)

