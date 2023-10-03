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
error = True
while error:
    userInput = input("Quelle est votre entrée? : ")
    if userInput.isdigit():
        if int(userInput) >= -128 and int(userInput) <= 127:
            error = False
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
                break
    #If the string only contains capital letters, numbers and spaces
    else: 
        buzzer.on()
        time.sleep(1)
        buzzer.off()
        print("Le texte ne doit contenir que des lettres majuscules, des nombres et des espaces")
print("Le texte est: " + userInput)

#Encode the string if it only digits to binary to send it to the LEDs
if userInput.isdigit() and int(userInput) > 0:
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
elif int(userInput) < 0:
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
time.sleep(3)
bit1.off()
bit2.off()
bit3.off()
bit4.off()
bit5.off()
bit6.off()
bit7.off()
bit8.off()

#Use the 3 first bit to determine the color of the RGB LED, if all the 3 first bit are off, the LED is white
rgbRed.on()
rgbGreen.on()
rgbBlue.on()
if bit1On: 
    rgbRed.off()
if bit2On:
    rgbGreen.off()
if bit3On:
    rgbBlue.off()
time.sleep(3)