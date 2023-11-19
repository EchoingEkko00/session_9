import numpy as np, sys
import matplotlib.pyplot as plt


X, Y = np.loadtxt("SentimData.txt", skiprows=1, unpack=True, usecols=(0,1))
plt.xlabel("Iterations", fontsize = 20)
plt.ylabel("Log-likelihood", fontsize = 20)
plt.scatter(X, Y, color = 'blue', label = 'Log-likelihood en fonction des iterations')
plt.xlim(0, max(X))
plt.ylim(-0.8, -0.2)
plt.show()

X, Y = np.loadtxt("SentimData.txt", skiprows=1, unpack=True, usecols=(0,2))
plt.xlabel("Iterations", fontsize = 20)
plt.ylabel("Accuracy", fontsize = 20)
plt.scatter(X, Y, color = 'blue', label = 'Accuracy en fonction des iterations')
plt.xlim(0, max(X))
plt.ylim(0.45, 0.90)
plt.show()