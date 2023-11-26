# Apprendre la relation entre le courant, le voltage et la résistance: V = RI
import numpy as np
import pandas as pd # Structures de données: pip install panda
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt, random

# Étape 1: Générer des données artificielles
# np.random.seed() # Sans argument => nombres différents générés
#                     # à chaque invocation

# Circuit simple avec une seule résistance
# courant = np.random.uniform(low = 0, high = 0.015, size = 100) # en Ampères
# resistance = random.choices([220, 1000, 10000], k = 100) # en Ohms
# voltage = courant * resistance # en Volts

# # Créer un DataFrame
# donnees = pd.DataFrame({'Courant': courant, 'Resistance': resistance, 'Voltage': voltage})
# # Les deux lignes suivantes vous permettent de voir
# # le format des données si elles sont lues dans un fichier

# donnees.to_csv('vri.csv', index = False)
donnees = pd.read_csv("vri.csv")
print(donnees)
# Étape 2: Créer des données d'entraînement et de test

X = donnees[['Courant', 'Resistance']]
y = donnees['Voltage']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

# Étape 3: Le modèle de régression linéaire

modele = LinearRegression()

# Étape 4: Entraîner un  modèle
modele.fit(X_train, y_train)

# Étape 5: Évaluer ce modèle

y_pred = modele.predict(X_test)

rmse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred) # De -1 (pire) à +1 (mieux)
# Évaluer l'adéquation du modèle p/r aux données.

print("Erreur quadratique moyenne: {:0.2f}".format(rmse))
print("Coefficient de détermination: {:0.2f}".format(r2))

# Étape 6: Visualisation

plt.scatter(y_test, y_pred)
plt.xlabel('Voltage réel')
plt.ylabel('Voltage prédit')
plt.title('Réel vs. Prédit')
plt.show()
