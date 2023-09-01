# heritage.py
import classes
class Fruit:
    categorie = "alimentation"
    def __init__(self, saveur=None, forme=None):
        print("Je suis dans le constructeur de la classe Fruit")
        self.saveur = saveur
        self.forme = forme
        print("Je viens de créer self.saveur et self.forme")
    def montre_conseil(self, type_fruit, conseil):
        print("Je suis dans la méthode .montre_conseil() de la "
              "classe Fruit\n")
        return (f"Instance {type_fruit}\n"
                f"saveur: {self.saveur}, forme: {self.forme}\n"
                f"conseil: {conseil}\n")
class Poire(Fruit):
    def __init__(self, saveur=None, forme=None):
        print("Je rentre dans le constructeur de Poire, et je vais appeler "
              "le constructeur de la classe mère Fruit !")
        Fruit.__init__(self, saveur, forme)
        print("J'ai fini dans le constructeur de Poire, les attributs sont :\n"
              f"self.saveur: {self.saveur}, self.forme: {self.forme}\n")
    def __str__(self): # On surcharge str qui est utilisé par print()
        print("Je rentre dans la méthode .__str__() de la classe Poire")
        print("Je vais lancer la méthode .montre_conseil() héritée "
              "de la classe Fruit")
        return self.montre_conseil("Poire", "Bon en croustade !")   
class Kiwi(Fruit):
    def __init__(self, saveur=None, forme=None):
        self.saveur = saveur  # Je n'appel pas le constructeur parent
        self.forme = forme      
    def __str__(self):
        return self.montre_conseil("Kiwi", "Bon en salade !")
if __name__ == "__main__":
    # On crée une poire et un kiwi
    poire = Poire(saveur="juteuse", forme="poire")
    print("Poire>>",poire)
    print("-------")
    kiwi = Kiwi(saveur="douce", forme="ballon")
    print("Kiwi>>",kiwi)

