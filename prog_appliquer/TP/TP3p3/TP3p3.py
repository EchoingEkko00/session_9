from threading import Thread
from gpiozero import AngularServo, LEDCharDisplay, Button, LEDCharFont
from time import sleep
import tkinter as tk
import sys
my_font = LEDCharFont({
    " ": (0,0,0,0,0,0,0),
    'A': (1, 1, 1, 0, 1, 1, 1),
    'B': (1, 1, 1, 1, 1, 1, 1),
    'C': (1, 0, 0, 1, 1, 1, 0),
    'D': (1, 1, 1, 1, 1, 0, 0),
    'E': (1, 0, 0, 1, 1, 1, 1),
    'F': (1, 0, 0, 0, 1, 1, 1),
    'G': (1, 0, 1, 1, 1, 1, 0),
    'H': (0, 1, 1, 0, 1, 1, 1),
    'I': (0, 0, 0, 0, 1, 1, 0),
    'J': (0, 1, 1, 1, 0, 0, 0),
    'K': (1, 0, 1, 0, 1, 1, 1),
    'L': (0, 0, 0, 1, 1, 1, 0),
    'M': (1, 1, 0, 1, 0, 1, 0),
    'N': (1, 1, 1, 0, 1, 1, 0),
    'O': (1, 1, 1, 1, 1, 1, 0),
    'P': (1, 1, 0, 0, 1, 1, 1),
    'Q': (1, 1, 0, 1, 0, 1, 1),
    'R': (1, 1, 0, 1, 1, 1, 1),
    'S': (1, 0, 1, 1, 0, 1, 1),
    'T': (1, 0, 0, 0, 1, 1, 0),
    'U': (0, 1, 1, 1, 1, 1, 0),
    'V': (0, 1, 1, 1, 0, 1, 0),
    'W': (1, 0, 1, 1, 1, 0, 0),
    'X': (1, 0, 0, 1, 0, 0, 1),
    'Y': (0, 1, 0, 1, 0, 1, 1),
    'Z': (1, 1, 0, 1, 1, 0, 1),

    '0': (1, 1, 1, 1, 1, 1, 0),
    '1': (0, 1, 1, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1),
    '3': (1, 1, 1, 1, 0, 0, 1),
    '4': (0, 1, 1, 0, 0, 1, 1),
    '5': (1, 0, 1, 1, 0, 1, 1),
    '6': (1, 0, 1, 1, 1, 1, 1),
    '7': (1, 1, 1, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 0, 1, 1),
})

maxPw = (2.5)/1000
minPw = (0.5)/1000
servo = AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=minPw, max_pulse_width=maxPw, initial_angle=0)
ledChar = LEDCharDisplay(13,19,16,20,21,6,26, dp=25, active_high=False, font=my_font)
buttonRouge = Button(5)
buttonBleu = Button(17)
userInputTemp = ""
userInput = ""
alreadyShowed = False
entry = ""

def getAnglePosition() :
    global servo
    if servo.angle == 0 :
        return '1'
    elif servo.angle == 45 :
        return '2'
    elif servo.angle == 90 :
        return '3'
    elif servo.angle == 135 :
        return '4'
    elif servo.angle == 180 :
        return '5'

def get_input():
    global userInput
    global userInputTemp
    global alreadyShowed
    global entry
    userInputTemp = entry.get()
    if (userInputTemp == ""):
        print("Peut pas etre vide")
        return
    if (not userInputTemp.isalnum() and (not userInputTemp.isalpha() and not userInputTemp.isdigit())):
        print("Doit etre soit des lettres soit des chiffres ou les deux")
    else :
        userInputTemp = userInput
        userInput = entry.get()
        userInput = userInput.upper()
        alreadyShowed = False
        print("User Input:", userInput)


def upLever():
    global servo
    if (servo.angle == 180) :
        servo.angle = 0
    else :
        servo.angle += 45

def downLever():
    global servo
    if (servo.angle == 0) :
        servo.angle = 180
    else:
        servo.angle -= 45

def programe():
    global servo
    global ledChar
    global buttonRouge
    global buttonBleu
    global userInput
    global userInputTemp
    global alreadyShowed
    while True:
        ledChar.value = getAnglePosition()
        sleep(0.1)
        if (buttonRouge.is_pressed):
            downLever()
        elif (buttonBleu.is_pressed):
            upLever()
        if (userInput != "" and not alreadyShowed):
            for i in userInput :
                ledChar.value = i
                sleep(1)
            alreadyShowed = True
            ledChar.value = getAnglePosition()
    

def drawing() :
    global entry
    root = tk.Tk()
    root.title("Tkinter Example")

    # Blue Button
    blue_button = tk.Button(root, text="Tourner le bras de +45 degres", fg="blue", command=upLever)
    blue_button.pack()

    # Red Button
    red_button = tk.Button(root, text="Tourner le bras de -45 degres", fg="red", command=downLever)
    red_button.pack()

    # Entry Widget
    entry = tk.Entry(root)
    entry.pack()

    # Black Button
    black_button = tk.Button(root, text="Afficher le text sur le segment", fg="black", command=get_input)
    black_button.pack()

    root.mainloop()


#Start both threads
if __name__ == "__main__":
    program_thread = Thread(target=programe)
    drawing_thread = Thread(target=drawing)

    program_thread.daemon = True  # Set the program thread as a daemon
    drawing_thread.daemon = True  # Set the drawing thread as a daemon

    program_thread.start()
    drawing_thread.start()

    try:
        program_thread.join()
        drawing_thread.join()
    except (KeyboardInterrupt, AttributeError):
        print("Program stopped by user")
        ledChar.close()
        buttonBleu.close()
        buttonRouge.close()
        sys.exit(0)