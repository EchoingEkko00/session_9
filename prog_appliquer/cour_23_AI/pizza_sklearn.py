import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)

# Create a linear regression model
model = LinearRegression()

# Trouve un modèle pour les données
model.fit(X.reshape(-1,1), Y.reshape(-1,1)) 
# Faire deux prédictions pour tracer notre droite 
X_new = np.array([[0], [30]])
Y_pred = model.predict(X_new)
plt.scatter(X, Y, label='Données')
plt.plot(X_new, Y_pred, color = 'r', label = 'Droite apprise')
plt.xlabel("Réservations", fontsize = 20)   
plt.ylabel("Pizzas vendues", fontsize = 20)      
plt.legend(loc = 'upper left')
plt.show()
