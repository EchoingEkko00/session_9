import Freenove_DHT11 as DHT
from flask import Flask, render_template, redirect, request, url_for
from threading import Thread
from datetime import datetime
import cv2
from lobe import ImageModel
from gpiozero import DistanceSensor, OutputDevice, LED, Button
import time
import base64

# TODO: Ajouter le KeyPad pour le login
# TODO: Ajouter le capteur de distance (Fait)
# TODO: Ajouter le message vers la matrice de LED (Fait)

dht = DHT.DHT(4)
sensor = DistanceSensor(20, 16)
dataPin = OutputDevice(17)  # GPIO pin 17 (corresponding to 11 in BCM numbering)
latchPin = OutputDevice(27)  # GPIO pin 27 (corresponding to 13 in BCM numbering)
clockPin = OutputDevice(22)  # GPIO pin 22 (corresponding to 15 in BCM numbering)
#KeyPad
L1 = LED(5)
L2 = LED(6)
L3 = LED(13)
L4 = LED(19)
C1 = Button(26, pull_up=False)
C2 = Button(23, pull_up=False)
C3 = Button(24, pull_up=False)
C4 = Button(25, pull_up=False)

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
    0x00, 0x00, 0x1C, 0x22, 0x41, 0x41, 0x07, 0x00, # "G"
    0x00, 0x00, 0x7F, 0x08, 0x08, 0x7F, 0x00, 0x00, # "H"
    0x00, 0x00, 0x41, 0x7F, 0x41, 0x00, 0x00, 0x00, # "I"
    0x00, 0x00, 0x02, 0x01, 0x41, 0x7E, 0x40, 0x00, # "J"
    0x00, 0x00, 0x7F, 0x08, 0x14, 0x63, 0x00, 0x00, # "K"
    0x00, 0x00, 0x7F, 0x01, 0x01, 0x01, 0x00, 0x00, # "L"
    0x00, 0x00, 0x7F, 0x30, 0x0C, 0x7F, 0x00, 0x00, # "M"
    0x00, 0x00, 0x7F, 0x30, 0x0C, 0x7F, 0x00, 0x00, # "N"
    0x00, 0x00, 0x3E, 0x41, 0x41, 0x3E, 0x00, 0x00, # "O"
    0x00, 0x00, 0x7F, 0x48, 0x48, 0x30, 0x00, 0x00, # "P"
    0x00, 0x00, 0x3E, 0x41, 0x43, 0x3F, 0x00, 0x00, # "Q"
    0x00, 0x00, 0x7F, 0x48, 0x4C, 0x33, 0x00, 0x00, # "R"
    0x00, 0x00, 0x32, 0x49, 0x49, 0x26, 0x00, 0x00, # "S"
    0x00, 0x00, 0x40, 0x7F, 0x40, 0x00, 0x00, 0x00, # "T"
    0x00, 0x00, 0x7E, 0x01, 0x01, 0x7E, 0x00, 0x00, # "U"
    0x00, 0x00, 0x7C, 0x03, 0x03, 0x7C, 0x00, 0x00, # "V"
    0x00, 0x00, 0x7F, 0x06, 0x06, 0x7F, 0x00, 0x00, # "W"
    0x00, 0x00, 0x63, 0x1C, 0x1C, 0x63, 0x00, 0x00, # "X"
    0x00, 0x00, 0x70, 0x0F, 0x0F, 0x70, 0x00, 0x00, # "Y"
    0x00, 0x00, 0x43, 0x45, 0x49, 0x61, 0x00, 0x00, # "Z"
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # " "
]

indexOfChar = {
    ' ': 0,
    '0': 1,
    '1': 2,
    '2': 3,
    '3': 4,
    '4': 5,
    '5': 6,
    '6': 7,
    '7': 8,
    '8': 9,
    '9': 10,
    'A': 11,
    'B': 12,
    'C': 13,
    'D': 14,
    'E': 15,
    'F': 16,
    'G': 17,
    'H': 18,
    'I': 19,
    'J': 20,
    'K': 21,
    'L': 22,
    'M': 23,
    'N': 24,
    'O': 25,
    'P': 26,
    'Q': 27,
    'R': 28,
    'S': 29,
    'T': 30,
    'U': 31,
    'V': 32,
    'W': 33,
    'X': 34,
    'Y': 35,
    'Z': 36
}

LSBFIRST = 1
MSBFIRST = 2

humidity = ""
temperature = ""
categorie = ""
distance = 0
sms = ""
keypadPassword = ""
imgNumber = 1
isDisplaying = False
model = ImageModel.load('./modele')
def shiftOut(d_pin, c_pin, order, val):
    for i in range(0, 8):
        c_pin.off()
        if order == LSBFIRST:
            d_pin.value = (0x01 & (val >> i) == 0x01)
        elif order == MSBFIRST:
            d_pin.value = (0x80 & (val << i) == 0x80)
        c_pin.on()
def destroy():
    dataPin.off()
    latchPin.off()
    clockPin.off()
    dataPin.close()
    latchPin.close()
    clockPin.close()
def display_string(input_string):
    global isDisplaying
    isDisplaying = True
    dataCombine = []
    string = ' ' + input_string + ' '
    for char in string:
        index = indexOfChar.get(char.upper(), 0) * 8
        dataCombine.extend(data[index: index + 8])
    
    for k in range(0,len(dataCombine)-8): #len(data) total number of "0-F" columns 
        for j in range(0,20): # times of repeated displaying LEDMatrix in every frame, the bigger the "j", the longer the display time.
            x=0x80      # Set the column information to start from the first column
            for i in range(k,k+8):
                latchPin.off()
                shiftOut(dataPin, clockPin, MSBFIRST, dataCombine[i])
                shiftOut(dataPin, clockPin, MSBFIRST, ~x)
                latchPin.on()
                time.sleep(0.001)
                x >>= 1
    isDisplaying = False
def picture():
        global imgNumber
        capture = cv2.VideoCapture(-1)
        ret, img = capture.read()
        cv2.imshow('A Frame',img)
        nomFichier = "./static/img" + str(imgNumber) + ".jpg"
        cv2.imwrite(nomFichier, img)
        print("Capture #1 terminée.")
        resultat = model.predict_from_file(nomFichier)
        # L'étiquette de la prédiction, on l'inscrit sur l'image
        etiquette = resultat.prediction
        # Le niveau de confiance pour le meilleur choix
        confiance = resultat.labels[0][1]
        # Résultats
        print(f"Prédiction: {etiquette} | Confiance: {confiance * 100: .2f}") 
        cv2.putText(img, f"{etiquette} | {confiance * 100: .2f}", (0,100), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        imgNumber += 1
        capture.release()
        cv2.destroyAllWindows()
        return etiquette
def get_sensor_data():
    global humidity
    global temperature
    while True:
        verification = dht.readDHT11()
        if verification == dht.DHTLIB_OK:
        #    humidity = str(1)
            humidity = str(dht.humidity)
        #    temperature = str(2)
            temperature = str(dht.temperature)
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

def read_keypad():
    global keypadPassword
    while True:
        keypadPassword = readLine(L1, ["1", "2", "3", "A"], keypadPassword)
        keypadPassword = readLine(L2, ["4", "5", "6", "B"], keypadPassword)
        keypadPassword = readLine(L3, ["7", "8", "9", "C"], keypadPassword)
        keypadPassword = readLine(L4, ["*", "0", "#", "D"], keypadPassword)
        if len(keypadPassword) == 4:
            print("Input:", keypadPassword)
        time.sleep(0.2)
def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'

    valid_password = '2002'

    @app.route('/')
    def login():
        return render_template('login.html')
    @app.route('/authenticate', methods=['POST'])
    def authenticate():
        password = request.form['password']
        if password == valid_password and password.isdigit() and len(password) == 4:
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=True)
    @app.route('/send' , methods=['POST'])
    def send():
        global isDisplaying
        data = request.get_json()
        message = data.get('message')
        print(message)
        if (isDisplaying == False):
            display_string(message)
        else :
            while (isDisplaying == True):
                time.sleep(0.1)
            display_string(message)
    @app.route('/getKeypadPassword', methods=['GET'])
    def getKeypadPassword():
        global keypadPassword
        if len(keypadPassword) == 4:
            tmp = keypadPassword
            keypadPassword = ""
            print("API call : " + tmp)
            return tmp
        else:
            return ""
    @app.route('/index')
    def index():
        global humidity
        global temperature
        global categorie
        global distance
        global sms
        global imgNumber
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        distance = round(sensor.distance * 100, 2)
        categorie = picture()
        with open('./static/img' + str(imgNumber - 1) + '.jpg', 'rb') as img_file :
            encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
        if (categorie == "Arme"):
            sms = date + "\nPersonne armee"
        elif (distance <= 10):
           sms = date + "\nTrop proche"
        return render_template('index.html', humidity=humidity, temperature=temperature, date=date, categorie=categorie, image=encoded_string, sms=sms, distance=distance)
    return app

if __name__ == '__main__':
    Thread(target=read_keypad).start()
    Thread(target=get_sensor_data).start()
    app = create_app()
    app.run(debug=False, host='0.0.0.0', use_reloader=False)