# balleMouvementTkinter.py
#  clic gauche: agrandir la balle
#  clic droit: rapetisser la balle
#  clic central: relancer la balle aléatoirement à ce point 
#  touche Tab: quitte l'appli balle

import tkinter as tk
import random as rd
import time

class AppliBalle(tk.Tk):
    xDepart = 250
    yDepart = 250
    rayonBalle = 50
    pasDeplacement = 20
    tailleCanevas = 500
    couleurCanevas = 'light blue'
    couleurBalle = 'dark blue'
    periodeDeplacement = 25
    deplacementRedemarrage = [-30, -20, -10, 10, 20, 30]
    tailleBalleMinimale = tailleBalleChangement = 10
    tailleBalleMaximale = 200
    def __init__(self):
        # Constructeur de l'application
        tk.Tk.__init__(self)
        # Coordonnées de la balle au départ
        self.x, self.y = AppliBalle.xDepart, AppliBalle.yDepart
        # Rayon de la balle.
        self.size = AppliBalle.rayonBalle
        # Envergure d'un déplacement de la balle.
        self.dx, self.dy = AppliBalle.pasDeplacement, AppliBalle.pasDeplacement
        # Création et packing du canevas.
        self.canv = tk.Canvas(self, bg=AppliBalle.couleurCanevas, height=AppliBalle.tailleCanevas, width=AppliBalle.tailleCanevas)
        self.canv.pack()
        # Création de la balle.
        self.balle = self.canv.create_oval(self.x, self.y, self.x+self.size, self.y+self.size, width=4, fill=AppliBalle.couleurBalle)
        # Binding des actions.
        self.canv.bind("<Button-1>", self.incrementer)
        self.canv.bind("<Button-2>", self.redemarrer)
        self.canv.bind("<Button-3>", self.decrementer)
        self.bind("<Tab>", self.arreter)
        # Lancer la balle.
        self.deplacer()

    def deplacer(self):
        # Incrémenter les coordonées de la balle.
        self.x += self.dx
        self.y += self.dy
        # Vérifier que la balle ne sort pas du canevas.
        if self.x < AppliBalle.rayonBalle/2:
            self.dx = abs(self.dx)
        if self.x > AppliBalle.tailleCanevas-self.size-AppliBalle.rayonBalle/2:
            self.dx = -abs(self.dx)
        if self.y < AppliBalle.rayonBalle/2:
            self.dy = abs(self.dy)
        if self.y > AppliBalle.tailleCanevas-self.size-AppliBalle.rayonBalle/2:
            self.dy = -abs(self.dy)
        # Mise à jour des coordonnées.
        self.canv.coords(self.balle, self.x, self.y, self.x+self.size, self.y+self.size)
        # Rappel de deplacer périodiquement. C'est la même chose que:
        # import time
        # ...
        # while True:
        #   move()
        #   time.sleep(AppliBalle.periodeDeplacement/1000) # attendre AppliBalle.periodeDeplacement ms
        self.after(AppliBalle.periodeDeplacement, self.deplacer)

    def redemarrer(self, clic):
        #Relance la balle dans une direction aléatoire au point du clic.
        self.x = clic.x
        self.y = clic.y
        self.canv.create_text(self.x, self.y, text="clic", fill="red")
        self.dx = rd.choice(AppliBalle.deplacementRedemarrage)
        self.dy = rd.choice(AppliBalle.deplacementRedemarrage)

    def incrementer(self, lclic):
        #Augmente la taille de la balle.
        self.size += AppliBalle.tailleBalleChangement
        if self.size > AppliBalle.tailleBalleMaximale:
            self.size = AppliBalle.tailleBalleMaximale

    def decrementer(self, rclick):
        #Diminue la taille de la balle.
        self.size -= AppliBalle.tailleBalleChangement
        if self.size < AppliBalle.tailleBalleMinimale:
            self.size = AppliBalle.tailleBalleMinimale

    def arreter(self, esc):
        #Quitte l'application.
        self.quit()


if __name__ == "__main__":
    myapp = AppliBalle()
    myapp.title("Balle en mouvement !")
    print("Avant mainloop")
    myapp.mainloop()
    print("Après mainloop")
    