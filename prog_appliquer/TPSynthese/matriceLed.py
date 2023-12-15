from gpiozero import OutputDevice
import time

LSBFIRST = 1
MSBFIRST = 2

dataPin = OutputDevice(17)  # GPIO pin 17 (corresponding to 11 in BCM numbering)
latchPin = OutputDevice(27)  # GPIO pin 27 (corresponding to 13 in BCM numbering)
clockPin = OutputDevice(22)  # GPIO pin 22 (corresponding to 15 in BCM numbering)


leds = [OutputDevice(pin) for pin in range(64)]

pic = [0x1c, 0x22, 0x51, 0x45, 0x45, 0x51, 0x22, 0x1c]
data = [     # data of "0-F"
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # " "
    0x00, 0x00, 0x3E, 0x41, 0x41, 0x3E, 0x00, 0x00, # "0"
    0x00, 0x00, 0x21, 0x7F, 0x01, 0x00, 0x00, 0x00, # "1"
    0x00, 0x00, 0x23, 0x45, 0x49, 0x31, 0x00, 0x00, # "2"
    0x00, 0x00, 0x22, 0x49, 0x49, 0x36, 0x00, 0x00, # "3"
    0x00, 0x00, 0x0E, 0x32, 0x7F, 0x02, 0x00, 0x00, # "4"
    0x00, 0x00, 0x79, 0x49, 0x49, 0x46, 0x00, 0x00, # "5"
    0x00, 0x00, 0x3E, 0x49, 0x49, 0x26, 0x00, 0x00, # "6"
    0x00, 0x00, 0x60, 0x47, 0x48, 0x70, 0x00, 0x00, # "7"
    0x00, 0x00, 0x36, 0x49, 0x49, 0x36, 0x00, 0x00, # "8"
    0x00, 0x00, 0x32, 0x49, 0x49, 0x3E, 0x00, 0x00, # "9"   
    0x00, 0x00, 0x3F, 0x44, 0x44, 0x3F, 0x00, 0x00, # "A"
    0x00, 0x00, 0x7F, 0x49, 0x49, 0x36, 0x00, 0x00, # "B"
    0x00, 0x00, 0x3E, 0x41, 0x41, 0x22, 0x00, 0x00, # "C"
    0x00, 0x00, 0x7F, 0x41, 0x41, 0x3E, 0x00, 0x00, # "D"
    0x00, 0x00, 0x7F, 0x49, 0x49, 0x41, 0x00, 0x00, # "E"
    0x00, 0x00, 0x7F, 0x48, 0x48, 0x40, 0x00, 0x00, # "F"
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # " "
]


def shift_out(data_pin, clock_pin, order, val):
    for i in range(0, 8):
        clock_pin.off()
        if order == 1:
            data_pin.value = (0x01 & (val >> i)) == 0x01
        elif order == 2:
            data_pin.value = (0x80 & (val << i)) == 0x80
        clock_pin.on()


def loop():
    while True:
        for j in range(0, 500):  # Repeat enough times to display the smiling face for a period of time
            x = 0x80
            for i in range(0, 8):
                latchPin.off()
                shift_out(dataPin, clockPin, 2, pic[i])  # Line information to first stage 74HC959
                shift_out(dataPin, clockPin, 2, ~x)  # Column information to second stage 74HC959
                latchPin.on()
                time.sleep(0.001)  # Display the next column
                x >>= 1

        for k in range(0, len(data) - 8):  # Total number of "0-F" columns
            for j in range(0, 20):  # Times of repeated displaying LEDMatrix in every frame
                x = 0x80  # Set the column information to start from the first column
                for i in range(k, k + 8):
                    latchPin.off()
                    shift_out(dataPin, clockPin, 2, data[i])
                    shift_out(dataPin, clockPin, 2, ~x)
                    latchPin.on()
                    time.sleep(0.001)
                    x >>= 1

picTest = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
def testLED(): # affiche durant 0.1 seconde chacune des 64 leds de gauche à droite, de haut en bas
    x = 0x80
    for i in range(64):
        latchPin.off()
        shift_out(dataPin, clockPin, 2, picTest[i % 8])  # Line information
        shift_out(dataPin, clockPin, 2, ~x)  # Column information
        latchPin.on()
        time.sleep(0.1)
        if i in [7, 15, 23, 31, 39, 47, 55]:
            x >>= 1

def destroy():
    dataPin.off()
    latchPin.off()
    clockPin.off()
    dataPin.close()
    latchPin.close()
    clockPin.close()


if __name__ == '__main__':
    print('Program is starting...')
    try:
        testLED()
        loop()
    except KeyboardInterrupt:
        destroy()
