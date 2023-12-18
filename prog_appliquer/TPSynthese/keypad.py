from gpiozero import LED, Button
import time

L1 = LED(5)
L2 = LED(6)
L3 = LED(13)
L4 = LED(19)

C1 = Button(26, pull_up=False)
C2 = Button(23, pull_up=False)
C3 = Button(24, pull_up=False)
C4 = Button(25, pull_up=False)

def readLine(line, characters, current_input):
    line.on()
    if C1.is_pressed:
        current_input += characters[0]
    if C2.is_pressed:
        current_input += characters[1]
    if C3.is_pressed:
        current_input += characters[2]
    if C4.is_pressed:
        current_input += characters[3]
    line.off()
    return current_input

try:
    input_string = ""
    while True:
        input_string = readLine(L1, ["1", "2", "3", "A"], input_string)
        input_string = readLine(L2, ["4", "5", "6", "B"], input_string)
        input_string = readLine(L3, ["7", "8", "9", "C"], input_string)
        input_string = readLine(L4, ["*", "0", "#", "D"], input_string)
        if len(input_string) >= 4:
            print("Input:", input_string)
            input_string = ""  # Reset input string after capturing 4 characters
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")
