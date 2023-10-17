from gpiozero import DistanceSensor, LED
from signal import pause

capteur = DistanceSensor(23, 24, max_distance=1, threshold_distance=0.2)
led = LED(16)

capteur.when_in_range = led.on
capteur.when_out_of_range = led.off

pause()