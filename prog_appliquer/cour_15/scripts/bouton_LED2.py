from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(26)

print("C'est parti!")

led.source = button # mis-à-jour dans un thread séparé
pause()

