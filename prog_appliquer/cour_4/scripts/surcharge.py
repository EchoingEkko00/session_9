# surcharge.py 
class Orange:
    forme = "sphère" # attribut de classe, constant
    def __init__(self, couleur="orange", taille=10, masse=0):
        self.couleur = couleur # attribut d'instance
        self.taille = taille # attribut d'instance
        self.masse = masse # attribut d'instance (masse en gramme)
    def __add__(self, o): # surcharge de l'opérateur +
        return self.masse + o.masse
    def __len__(self): # surcharge de la fonction standard len
        return self.taille
            
if __name__ == "__main__":
    orange1 = Orange("orange", 10,100)
    orange2 = Orange("orange", 20,100)
    print(orange1 + orange2, len(orange1), len(orange2))
	    


