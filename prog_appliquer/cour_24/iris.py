from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np, random
from time import sleep

# Charger le fichier de données 
data = np.loadtxt('iris.data', skiprows = 1, delimiter = ',')

X = data[:, :-1]  # Toutes les lignes sans la dernière colonne
# Extract the last column into another list
y = data[:, -1]  # Toutes les lignes de la dernière colonne

# Sépare les données (90% entraînement, 10% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

# Crée un classifieur de type Support Vector Machine
classifieur_svm = SVC(kernel='linear') 

# On l'entraîne
classifieur_svm.fit(X_train, y_train)

# On fait des prédictions sur les tests
predictions = classifieur_svm.predict(X_test)
print(predictions)
# On évalue l'exactitude du modèle
exactitude = accuracy_score(y_test, predictions)
print(f"Exactitude: {exactitude:.2f}\n")

# Faisons des prédictions avec des données aléatoires
# [Classe]: 0 = Iris-setosa 1 = Iris-versicolor 2 = Iris-virginica
while True:
    uneFleur = random.sample(range(1, 10), 4)
    print("[Longueur_sépale_cm,Largeur_sépale_cm,Longueur_pétale_cm,Largeur_pétale_cm] [Classe]")
    print(uneFleur, classifieur_svm.predict([uneFleur]))
    sleep(1)

