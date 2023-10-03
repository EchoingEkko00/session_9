from gpiozero import LED, Button, Buzzer
import time

# the input must be a number between -128 and 127 or a string with only capital letters and spaces
buzzer = Buzzer(2)
bit1 = LED(3)
bit2 = LED(4)
bit3 = LED(17)
bit4 = LED(27)
bit5 = LED(22)
bit6 = LED(10)
bit7 = LED(9)
bit8 = LED(11)
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
if userInput.isdigit():
    userInput = int(userInput)
    if userInput < 0:
        bit8.on()
        userInput = userInput * -1
    else:
        bit8.off()
    if userInput >= 64:
        bit7.on()
        userInput = userInput - 64
    else:
        bit7.off()
    if userInput >= 32:
        bit6.on()
        userInput = userInput - 32
    else:
        bit6.off()
    if userInput >= 16:
        bit5.on()
        userInput = userInput - 16
    else:
        bit5.off()
    if userInput >= 8:
        bit4.on()
        userInput = userInput - 8
    else:
        bit4.off()
    if userInput >= 4:
        bit3.on()
        userInput = userInput - 4
    else:
        bit3.off()
    if userInput >= 2:
        bit2.on()
        userInput = userInput - 2
    else:
        bit2.off()
    if userInput >= 1:
        bit1.on()
        userInput = userInput - 1
    else:
        bit1.off()
