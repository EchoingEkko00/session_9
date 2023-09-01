# encapsulation.py
class Etudiant:
    def __init__(self, nom, matricule):
        # membre publique
        self.nom = nom
        # membre privé  __
        self.__matricule = matricule

    def affiche(self):
        print("Détails de l'étudant:", self.nom, self.__matricule)

    # getter
    def get_matricule(self):
        return self.__matricule

    # setter 
    def set_matricule(self, matricule):
        self.__matricule = matricule

jessica = Etudiant('Jessica', 1234567)
jessica.affiche()  # Détails de l'étudant: Jessica 1234567
print(jessica.nom) # Jessica
#print(jessica.__matricule)  # introuvable parce que privé
print(jessica.get_matricule()) # 1234567
jessica.nom = "Jessa"
jessica.__matricule = 7654321  # possible mais sans conséquence
jessica.affiche() # Détails de l'étudant: Jessa 1234567
jessica.set_matricule(7654321)
jessica.affiche() # Détails de l'étudant: Jessa 7654321





