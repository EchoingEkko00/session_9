import numpy as np, sys
import matplotlib.pyplot as plt
def tracerDonnees(X,Y):
    plt.xlabel("Réservations", fontsize = 20)   # abscisse
    plt.ylabel("Pizzas vendues", fontsize = 20) # ordonné
    plt.scatter(X, Y, label = 'Données')  
# Prédictions de Y à partir des X pour un modèle (m,b) 
def predire(X, m, b):
    pass
# Erreur (perte) moyenne pour un modèle (m,b)
def perte(X, Y, m, b): # moyenne des pertes entre un modèle (m,b) et la réalité Y
    pass   
# Entraînement pour trouver un modèle (m,b)
def entraine(X, Y, iterations, ta): # ta = taux d'apprentissage
                                    # iterations: pour éviter les vas-et-vient infinis
                                    # but: trouver m et b
    pass
if __name__ == "__main__":
    # Importer les données dans deux tableaux distincts (unpack)
    X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)
    tracerDonnees(X,Y)
    plt.show()                                 
    # On entraîne de notre modèle
    m, b = entraine(X, Y, 2000, 0.01)
    # Visualisation et prédiction avec notre modèle
    print("Notre modèle: m = " + str(round(m, 2))+ " b = " + str(round(b, 2)))
    tracerDonnees(X, Y)
    # [X1, X2]  [Y1, Y2]  la droite que nous avons trouvée
    plt.plot([0, 30], [predire(0, m, b), predire(30, m, b)], color = "r", label='Droite apprise')
    plt.legend(loc = 'upper left')
    plt.show()                               
    # Faisons une prédiction avec notre modèle
    reservations = 21
    print("Prédictions: avec " + str(reservations)
      + " réservations, on prépare " + str(int(predire(reservations, m, b))) + " pizzas.")








