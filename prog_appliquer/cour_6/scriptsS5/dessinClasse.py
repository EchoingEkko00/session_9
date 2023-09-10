#dessinClasse.py
import tkinter as tk
import random as rd # pour générer des coordonnées et couleurs aléatoires

class AppliCanevas(tk.Tk):
    taille = 500
    couleurs = ["black", "red", "green", "blue", "yellow", "magenta","cyan", "white", "purple"]
    diametreMax = 50
    maxDessins = 10
    def __init__(self):
        tk.Tk.__init__(self)
        self.size = AppliCanevas.taille # taille de mon application
        self.creer_widgets()

    def creer_widgets(self):
        # création du canevas
        self.canv = tk.Canvas(self, bg="light gray", height=self.size, width=self.size)
        self.canv.pack(side=tk.LEFT) #TOP (défaut), BOTTOM, ou RIGHT
        # boutons
        self.bouton_cercles = tk.Button(self, text="Cercles", command=self.dessine_cercles) #callback
        self.bouton_cercles.pack(side=tk.TOP)
        self.bouton_lignes = tk.Button(self, text="Lignes", command=self.dessine_lignes) #callback
        self.bouton_lignes.pack()
        self.bouton_quitter = tk.Button(self, text="Quitter",command=self.quit)#callback
        self.bouton_quitter.pack(side=tk.BOTTOM)

    def couleur_aleatoire(self):
        return rd.choice(AppliCanevas.couleurs)

    def dessine_cercles(self):
        for i in range(AppliCanevas.maxDessins):
            # génère une coordonnée (deux nombres) aléatoire
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diametre = rd.randint(1, AppliCanevas.diametreMax)
            self.canv.create_oval(x, y, x+diametre, y+diametre,fill=self.couleur_aleatoire())

    def dessine_lignes(self):
        for i in range(AppliCanevas.maxDessins):
            # génère une liste de deux coordonnées (quatre nombres) aléatoires
            x, y, x2, y2 = [rd.randint(1, self.size) for j in range(4)]
            self.canv.create_line(x, y, x2, y2, fill=self.couleur_aleatoire())

if __name__ == "__main__":
    app = AppliCanevas()
    app.title("Dessins de lignes et cercles aléatoires !")
    app.mainloop()