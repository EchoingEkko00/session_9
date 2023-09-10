#baseTkinter.py
import tkinter as tk

racine = tk.Tk()
etiquette = tk.Label(racine, text="J'aime Python !")
bouton = tk.Button(racine, text="Quitter", command=racine.destroy) #quitte la mainloop, ne détruit pas 
bouton["fg"] = "red" #autre façon de modifier les paramètres d'un widget, a postiori
etiquette.pack()
bouton.pack()
racine.mainloop() #gestion événementielle
print("C'est terminé !") #ne s'affichera que lorsqu'on quittera la boucle principale
