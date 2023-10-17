from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(26)

while True:
    if button.is_pressed:
        print("Pressé")
        sleep(1)
    else:
        print("Relâché")
        sleep(1)


