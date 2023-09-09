class Rectangle:
 def __init__(self, longueur=0.0, largeur=0.0, couleur="blanc"):
 #Constructeur
    self.longueur = longueur
    self.largeur = largeur
    self.couleur = couleur
 #Méthode qui calcule la surface.
 def calcule_surface(self):
    return self.longueur * self.largeur
 #Méthode qui transforme un rectangle en carré.
 def change_carre(self, cote):
    self.longueur = cote
    self.largeur = cote
if __name__ == "__main__":
 # Insérez ici la suite de votre programme Python
 # qui va utiliser la classe Rectangle.
    rectangle = Rectangle(10, 5, "rouge")
    print("longeur = ", rectangle.longueur, "largeur = ", rectangle.largeur, "couleur = ", rectangle.couleur)
    print("surface = ", rectangle.calcule_surface())
    print()
    rectangle.change_carre(30)
    print("surface du carre", rectangle.calcule_surface())

    rectangle2 = Rectangle(20, 10, "bleu")
    print("longeur = ", rectangle2.longueur, "largeur = ", rectangle2.largeur, "couleur = ", rectangle2.couleur)
    print("surface = ", rectangle2.calcule_surface())