# classes.py
class Orange:
    forme = "rond" # attribut de classe, constant pour tous
    def __init__(self, couleur="orange", taille="standard", masse=0): # constructeur
        self.couleur = couleur # attribut d'instance
        self.taille = taille # attribut d'instance
        self.masse = masse # attribut d'instance 
    def augmente_masse(self, valeur):
        self.masse += valeur # instance
    def change_forme(self, f):
        Orange.forme = f  # classe
if __name__ == "__main__":
    orange1 = Orange()
    orange2 = Orange()
    print("Attributs de classe :", orange1.forme, orange2.forme)
    print("Attributs d'instance :", orange1.masse, orange2.masse)
    orange1.change_forme("oval")
    orange1.augmente_masse(100)
    print("Attributs de classe :", orange1.forme, orange2.forme)
    print("Attributs d'instance :", orange1.masse, orange2.masse)

