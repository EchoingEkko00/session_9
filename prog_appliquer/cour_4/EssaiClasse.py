class vegetaux: 
    def __init__(self, nom, taille, couleur, type):
        self.nom = nom
        self.taille = taille
        self.couleur = couleur
        self.type = type

    def afficher(self):
        print("Nom : ", self.nom, ", Taille: ", self.taille, ", Couleur: ", self.couleur, ", Type: ", self.type)
class carotte(vegetaux):
    saveur = "douce"
    def __init__(self, nom, taille, type):
        super().__init__(nom, taille, "orange", type)
    def afficher(self):
        print("Nom : ", self.nom, ", Taille: ", self.taille, ", Couleur: ", self.couleur, ", Type: ", self.type, ", Saveur: ", self.saveur)
    def changer_saveur(self, saveur):
        self.saveur = saveur
    def __str__(self):
        return ("Nom: " + self.nom + ", Taille: " + str(self.taille) + ", Couleur: " + self.couleur + ", Type: " + self.type + ", Saveur: " + self.saveur)

__name__ = "__main__"
carotte1 = carotte("carotte1", 10, "racine")
carotte1.afficher()
carotte2 = carotte("carotte2", 20, "racine")
carotte2.afficher()
carotte1.changer_saveur("amère")
print(carotte1)
print(carotte2)