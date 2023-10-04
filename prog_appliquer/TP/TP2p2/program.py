import threading
from gpiozero import LED, Buzzer
import time
from turtle import *

braille = {
    'A': '100000',
    'B': '101000',
    'C': '110000',
    'D': '110100',
    'E': '100100',
    'F': '111000',
    'G': '111100',
    'H': '101100',
    'I': '011000',
    'J': '011100',
    'K': '100010',
    'L': '101010',
    'M': '110010',
    'N': '110110',
    'O': '100110',
    'P': '111010',
    'Q': '111110',
    'R': '101110',
    'S': '011010',
    'T': '011110',
    'U': '100011',
    'V': '101011',
    'W': '011101',
    'X': '110011',
    'Y': '110111',
    'Z': '100111',
    ' ': '000000',
    '-': '000000'
}

tortue = Turtle()
buzzer = Buzzer(2)
bit1 = LED(3)
bit2 = LED(4)
bit3 = LED(17)
bit4 = LED(27)
bit5 = LED(22)
bit6 = LED(10)
bit7 = LED(9)
bit8 = LED(11)
rgbRed = LED(16)
rgbGreen = LED(20)
rgbBlue = LED(21)
rgbRed.on()
rgbGreen.on()
rgbBlue.on()
led = False
error = True
onlyNumber = False
onlyLetter = False
bit1On = False
bit2On = False
bit3On = False

def first_program():
    def confirmNoError():
        global error
        error = not error

    def confirmNumber():
        global onlyNumber
        onlyNumber = not onlyNumber

    def confirmLetter():
        global onlyLetter
        onlyLetter = not onlyLetter

    def changeBit1():
        global bit1On
        bit1On = not bit1On

    def changeBit2():
        global bit2On
        bit2On = not bit2On

    def changeBit3():
        global bit3On
        bit3On = not bit3On

    while error:
        userInput = input("Quelle est votre entrée? : ")
        if userInput.isdigit() or userInput.isdigit and userInput[0] == "-":
            if int(userInput) >= -128 and int(userInput) <= 127:
                confirmNoError()
                confirmNumber()
                break
            else:
                buzzer.on()
                time.sleep(1)
                buzzer.off()
                print("Le nombre doit être entre -128 et 127")
        elif userInput.isupper() and (userInput.isalnum() or userInput.__contains__(" ") or userInput.__contains__("-")) or userInput.isspace() or userInput.__contains__("-")  : 
            for i in userInput:
                if not i.isdigit() and not i.isupper() and not i.isspace() and not i == "-":
                    buzzer.on()
                    time.sleep(1)
                    buzzer.off()
                    print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
                    break
                elif i == "À" or i == "Â" or i == "É" or i == "È" or i == "Ê" or i == "Ë" or i == "Î" or i == "Ï" or i == "Ô" or i == "Û" or i == "Ù" or i == "Ü" or i == "Ç":
                    buzzer.on()
                    time.sleep(1)
                    buzzer.off()
                    print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
                    break
                if i == userInput[-1]:
                    confirmNoError()
                    confirmLetter()
                    break
        else: 
            buzzer.on()
            time.sleep(1)
            buzzer.off()
            print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
    print("Le texte est: " + userInput)
    
    if onlyNumber and int(userInput) > 0:
        if int(userInput) >= 128:
            bit8.on()
            userInput = int(userInput) - 128
        if int(userInput) >= 64:
            bit7.on()
            userInput = int(userInput) - 64
        if int(userInput) >= 32:
            bit6.on()
            userInput = int(userInput) - 32
        if int(userInput) >= 16:
            bit5.on()
            userInput = int(userInput) - 16
        if int(userInput) >= 8:
            bit4.on()
            userInput = int(userInput) - 8
        if int(userInput) >= 4:
            bit3.on()
            changeBit3()
            userInput = int(userInput) - 4
        if int(userInput) >= 2:
            bit2.on()
            changeBit2()
            userInput = int(userInput) - 2
        if int(userInput) >= 1:
            bit1.on()
            changeBit1()
            userInput = int(userInput) - 1
    elif onlyNumber and int(userInput) < 0:
        bit8.on()
        userInput = int(userInput) + 128
        if int(userInput) >= 64:
            bit7.on()
            userInput = int(userInput) - 64
        if int(userInput) >= 32:
            bit6.on()
            userInput = int(userInput) - 32
        if int(userInput) >= 16:
            bit5.on()
            userInput = int(userInput) - 16
        if int(userInput) >= 8:
            bit4.on()
            userInput = int(userInput) - 8
        if int(userInput) >= 4:
            bit3.on()
            bit3On = True
            userInput = int(userInput) - 4
        if int(userInput) >= 2:
            bit2.on()
            bit2On = True
            userInput = int(userInput) - 2
        if int(userInput) >= 1:
            bit1.on()
            bit1On = True
            userInput = int(userInput) - 1
    if onlyNumber :
        time.sleep(3)
        bit1.off()
        bit2.off()
        bit3.off()
        bit4.off()
        bit5.off()
        bit6.off()
        bit7.off()
        bit8.off()

        if bit1On: 
            rgbRed.off()
        if bit2On:
            rgbGreen.off()
        if bit3On:
            rgbBlue.off()
        time.sleep(3)
        rgbRed.on()
        rgbGreen.on()
        rgbBlue.on()
    if onlyLetter:
        for i in userInput:
            if i == "À":
                i = "A"
            elif i == "Â":
                i = "A"
            elif i == "É":
                i = "E"
            elif i == "È":
                i = "E"
            elif i == "Ê":
                i = "E"
            elif i == "Ë":
                i = "E"
            elif i == "Î":
                i = "I"
            elif i == "Ï":
                i = "I"
            elif i == "Ô":
                i = "O"
            elif i == "Û":
                i = "U"
            elif i == "Ù":
                i = "U"
            elif i == "Ü":
                i = "U"
            elif i == "Ç":
                i = "C"
            if i == " ":
                bit1.off()
                bit2.off()
                bit3.off()
                bit4.off()
                bit5.off()
                bit6.off()
                bit7.off()
                bit8.off()
                time.sleep(1)
            for j in range(0, len(braille[i])):
                if braille[i][j] == "1":
                    if j == 0:
                        bit1.on()
                        buzzer.on()
                        time.sleep(0.1)
                        buzzer.off()
                        time.sleep(0.5)
                    elif j == 1:
                        bit2.on()
                        buzzer.on()
                        time.sleep(0.1)
                        buzzer.off()
                        time.sleep(0.5)
                    elif j == 2:
                        bit3.on()
                        buzzer.on()
                        time.sleep(0.1)
                        buzzer.off()
                        time.sleep(0.5)
                    elif j == 3:
                        bit4.on()
                        buzzer.on()
                        time.sleep(0.1)
                        buzzer.off()
                        time.sleep(0.5)
                    elif j == 4:
                        bit5.on()
                        buzzer.on()
                        time.sleep(0.1)
                        buzzer.off()
                        time.sleep(0.5)
                    elif j == 5:
                        bit6.on()
                        buzzer.on()
                        time.sleep(0.1)
                        buzzer.off()
                        time.sleep(0.5)
            time.sleep(1)
            bit1.off()
            bit2.off()
            bit3.off()
            bit4.off()
            bit5.off()
            bit6.off()

def attrapeClic(x, y): # x et y sont les coordonnées du clic
        global led
        if x >= -100 and x <= 0 and y >= 0 and y <= 100:
            led = True
        elif x >= 10 and x <= 110 and y >= 0 and y <= 100:
            led = False
            
def second_program():
    rgbRed.on()
    rgbGreen.on()
    rgbBlue.on()
     # Fonction qui va s'occuper des clics
    # On déclare quelle méthode va attraper les clics gauches
    onscreenclick(attrapeClic,1) # 1: clic gauche
    # on dessine un rectangle rouge en plein centre
    col = 'blue'
    tortue.speed(0)
    tortue.goto(-100, 0)
    tortue.fillcolor(col)
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(100)
        tortue.left(90)
    tortue.end_fill()
    tortue.goto(-50, 0)
    tortue.write("ON", align="center", font=("Arial", 12, "bold"))
    tortue.penup()

    tortue.goto(10, 0)
    tortue.pendown()
    tortue.fillcolor('red')
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(100)
        tortue.left(90)
    tortue.end_fill()
    tortue.goto(60, 0)
    tortue.write("OFF", align="center", font=("Arial", 12, "bold"))
    tortue.hideturtle()
    while True:
        if led:
            rgbRed.on()
            rgbGreen.off()
            rgbBlue.on()
            bit1.on()
            bit2.on()
            bit3.on()
            bit4.on()
            bit5.on()
            bit6.on()
            bit7.on()
            bit8.on()
            buzzer.on()
        else:
            rgbRed.on()
            rgbGreen.on()
            rgbBlue.on()
            bit1.off()
            bit2.off()
            bit3.off()
            bit4.off()
            bit5.off()
            bit6.off()
            bit7.off()
            bit8.off()
            buzzer.off()

first_program_thread = threading.Thread(target=first_program)
second_program_thread = threading.Thread(target=second_program)

first_program_thread.start()
second_program_thread.start()

mainloop()
