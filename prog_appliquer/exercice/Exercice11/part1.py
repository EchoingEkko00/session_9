import numpy as np, sys
import matplotlib.pyplot as plt

lesPertes = []
lesIterations = []
apprentissage = 0.005
apprentissage2 = 0.010
apprentissage3 = 0.020
def tracerDonnees(X,Y):
    plt.title(apprentissage, fontsize = 20) # titre
    plt.xlabel("Iterations", fontsize = 20)   # abscisse
    plt.ylabel("Perte", fontsize = 20) # ordonné
    plt.scatter(X, Y)  
# Prédictions de Y à partir des X pour un modèle (m,b) 
def predire(X, m, b):
    Y = m * X + b
    return Y
# Erreur (perte) moyenne pour un modèle (m,b)
def perte(X, Y, m, b): # moyenne des pertes entre un modèle (m,b) et la réalité Y
    predictionY = predire(X, m, b)
    return np.average((predictionY - Y) ** 2)
# Entraînement pour trouver un modèle (m,b)
def entraine(X, Y, iterations, ta): # ta = taux d'apprentissage
                                    # iterations: pour éviter les vas-et-vient infinis
                                    # but: trouver m et b
    m = b = 0
    for i in range(iterations):
        perteCourant = perte(X, Y, m, b)
        lesPertes.append(perteCourant)
        lesIterations.append(i)
        print("Iteration " + str(i) + " : m = " + str(m) + " b = " + str(b) + " perte = " + str(perteCourant))
        # On essaie de trouver un meilleur modèle
        if perte(X,Y,m - ta, b) < perteCourant:
            m = m - ta
        elif perte(X,Y,m + ta, b) < perteCourant:
            m = m + ta
        elif perte(X,Y,m, b - ta) < perteCourant:
            b = b - ta
        elif perte(X,Y, m, b + ta) < perteCourant:
            b = b + ta
        else:
            return m, b
    print("Nb iterations atteint, pt l'augmenter")
    return m, b
if __name__ == "__main__":
    # Importer les données dans deux tableaux distinc ts (unpack)
    X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)                       
    # On entraîne de notre modèle
    m, b = entraine(X, Y, 3000, apprentissage)
    # Visualisation et prédiction avec notre modèle
    print("Notre modèle: m = " + str(round(m, 2))+ " b = " + str(round(b, 2)))
    tracerDonnees(lesIterations, lesPertes)
    plt.show()                               
    # Faisons une prédiction avec notre modèle
    reservations = 21
    print("Prédictions: avec " + str(reservations)
      + " réservations, on prépare " + str(int(predire(reservations, m, b))) + " pizzas.")








