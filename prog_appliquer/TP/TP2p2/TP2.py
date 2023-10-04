from gpiozero import LED, Button, Buzzer
import time

# the input must be a number between -128 and 127 or a string with only capital letters and spaces
buzzer = Buzzer(2)
bit1 = LED(3)
bit1On = False
bit2 = LED(4)
bit2On = False
bit3 = LED(17)
bit3On = False
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
error = True
onlyNumber = False
onlyLetter = False
#Braille dictionary
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
while error:
    userInput = input("Quelle est votre entrée? : ")
    if userInput.isdigit() or userInput.isdigit and userInput[0] == "-":
        if int(userInput) >= -128 and int(userInput) <= 127:
            error = False
            onlyNumber = True
            break
        else:
            buzzer.on()
            time.sleep(1)
            buzzer.off()
            print("Le nombre doit être entre -128 et 127")
    #Look if the string only contains capital letters, numbers and spaces
    elif userInput.isupper() and (userInput.isalnum() or userInput.__contains__(" ") or userInput.__contains__("-")) or userInput.isspace() or userInput.__contains__("-")  : 
        for i in userInput:
            if not i.isdigit() and not i.isupper() and not i.isspace() and not i == "-":
                buzzer.on()
                time.sleep(1)
                buzzer.off()
                print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
                break
            #If the string contains french capital accents the buzzer go on
            elif i == "À" or i == "Â" or i == "É" or i == "È" or i == "Ê" or i == "Ë" or i == "Î" or i == "Ï" or i == "Ô" or i == "Û" or i == "Ù" or i == "Ü" or i == "Ç":
                buzzer.on()
                time.sleep(1)
                buzzer.off()
                print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
                break
            if i == userInput[-1]:
                error = False
                onlyLetter = True
                break
    #If the string only contains capital letters, numbers and spaces
    else: 
        buzzer.on()
        time.sleep(1)
        buzzer.off()
        print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
print("Le texte est: " + userInput)
#Encode the string if it only digits to binary to send it to the LEDs
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
#if the number is negative, the program turn the 8th bit on and turn all the other bits to match the input
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
#Encode userInput into braille to send it to the LEDs
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
                    buzzer.blink(0.1, 0.1, 1)
                    time.sleep(0.5)
                elif j == 1:
                    bit2.on()
                    buzzer.blink(0.1, 0.1, 1)
                    time.sleep(0.5)
                elif j == 2:
                    bit3.on()
                    buzzer.blink(0.1, 0.1, 1)
                    time.sleep(0.5)
                elif j == 3:
                    bit4.on()
                    buzzer.blink(0.1, 0.1, 1)
                    time.sleep(0.5)
                elif j == 4:
                    bit5.on()
                    buzzer.blink(0.1, 0.1, 1)
                    time.sleep(0.5)
                elif j == 5:
                    bit6.on()
                    buzzer.blink(0.1, 0.1, 1)
                    time.sleep(0.5)
        time.sleep(1)
        bit1.off()
        bit2.off()
        bit3.off()
        bit4.off()
        bit5.off()
        bit6.off()