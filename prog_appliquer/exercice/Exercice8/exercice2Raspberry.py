from gpiozero import Button, LED
from time import sleep
import random

led = LED(17)
ledVerte = LED(27)

player_1 = Button(2)
player_2 = Button(3)
player_3 = Button(12)

vertOuRouge = random.random() < 0.8

time = random.uniform(5, 10)
sleep(time)
if vertOuRouge:
    led.on()
else:
    ledVerte.on()
while True:
    if ledVerte.is_lit:
        if player_1.is_pressed:
            print("Player 1 lose!")
            break
        if player_2.is_pressed:
            print("Player 2 lose!")
            break
        if player_3.is_pressed:
            print("Player 3 lose!")
            break
    elif led.is_lit:
        if player_1.is_pressed:
            print("Player 1 wins!")
            break
        if player_2.is_pressed:
            print("Player 2 wins!")
            break
        if player_3.is_pressed:
            print("Player 3 wins!")
            break
ledVerte.off()
led.off()