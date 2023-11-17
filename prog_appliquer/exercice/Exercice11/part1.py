import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X, Y = np.loadtxt("ledData.txt", skiprows=1, unpack=True)

# Create a linear regression model
model = LinearRegression()

# Trouve un modèle pour les données
model.fit(X.reshape(-1,1), Y.reshape(-1,1)) 
# Faire deux prédictions pour tracer notre droite 
X_new = np.array([[0], [1000]])
Y_pred = model.predict(X_new)
plt.scatter(X, Y, label='Données')
plt.plot(X_new, Y_pred, color = 'r', label = 'Droite apprise')
plt.xlabel("LedValue", fontsize = 20)   
plt.ylabel("PhotoMeter value", fontsize = 20)   
plt.ylim(0, 255)
plt.xlim(0, 1)  
plt.legend(loc = 'upper left')
plt.show()
