from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(26)
   
def pressed():
    print("Pressé")
def released():
    print("Relâché")

button.when_pressed = pressed
button.when_released = released
pause()