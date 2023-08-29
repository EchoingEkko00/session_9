#jeu_des.py
import random
# les fonctions sont définies avant leur utilisation
def roulement_des():
    de = random.randint(1,max) # max est globale
    return de

def go(joueur1,joueur2):
    #joueur1 et joueur2 n'existe que dans go()
    des1 = roulement_des()
    des2 = roulement_des()

    print(joueur1, 'a lancé', des1)
    print(joueur2, 'a lancé', des2)

    if des1 > des2:
        print(joueur1, 'gagne!')
    elif des2 > des1:
        print(joueur2, 'gagne!')
    else:
        print('Vous êtes égaux!')

#la première instruction ne faisant pas partie
#  d'une fonction constitue le point de départ
#une variable créée dans le corps principal du script est globale
#les variables locales ont priorité sur les variables globales
#une variable ne peut être utilisée avant d'avoir été affectée
if __name__ == "__main__": # on s'assure que ce qui suit s'exécutera comme script
                            # mais pas dans un import
    max = int(input("Entrez la valeur maximum sur le dé: "))
    go("William","Chris")