from gpiozero import DistanceSensor
from time import sleep

capteur = DistanceSensor(23, 24)

while True:
    print("Distance de l'objet le plus proche: ", capteur.distance, 'm')
    sleep(1)
    
    