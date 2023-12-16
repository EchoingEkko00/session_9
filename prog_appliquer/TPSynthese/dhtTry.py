import Freenove_DHT11 as DHT # le fichier Freenove_DHT11 est fourni sur Moodle
from gpiozero import DistanceSensor
import time
dht = DHT.DHT(4) # ATTENTION: vérifier ce que vous avez à la ligne 26 du
# module Freenove_DHT11.py pour spécifier correctement
# le numéro de la broche

sensor = DistanceSensor(20, 16)
while True:
    verification = dht.readDHT11() # on fait une lecture
    if (verification is dht.DHTLIB_OK): # si les lectures sont valides, on peut les lire
        print(dht.humidity, dht.temperature)
    # print distance in cm
    print('Distance: ', sensor.distance * 100)
    print(sensor.distance)
    time.sleep(1)