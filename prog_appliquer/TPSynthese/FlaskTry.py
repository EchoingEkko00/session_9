from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
import cv2
from lobe import ImageModel

noImage = 1
model = ImageModel.load('./modele')
capture = cv2.VideoCapture(0)
categorie = ""

app = Flask(__name__)
app.secret_key = 'secret_key'

valid_password = '2002'

def picture(): 
        _, img = capture.read()
        cv2.imshow('Frame',img)
        nomFichier = "./static/img1.jpg"
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
        return etiquette

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
    print(request.form['message'])
    return redirect(url_for('index'))

@app.route('/index')
def index():
    categorie = picture()
    date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    image_path = 'img1.jpg'
    return render_template('index.html', date=date, categorie=categorie, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True,)