#passage.py
def changerParametres(immuable, muable ):
    immuable = 0
    muable.append('quatre')

if __name__ == "__main__": 
    liste = ['un', 'deux', 'trois']
    entier = 99

    print('avant :', entier, liste) # avant : 99 ['un', 'deux', 'trois']
    changerParametres(entier,liste)
    print('après :', entier, liste) # après : 99 ['un', 'deux', 'trois', 'quatre']

    # la fonction Python id() retourne l'adresse mémoire 'un objet
    print(liste, id(liste))    # ['un', 'deux', 'trois', 'quatre'] 2356669595584
    print(entier, id(entier))  # 99 2356669339056
    liste.append('cinq')
    entier = 0
    print(liste, id(liste))    # ['un', 'deux', 'trois', 'quatre', 'cinq'] 2356669595584 # muable
    print(entier, id(entier))  # 0 2356669147408 # immuable, il faut stocker ailleurs
    
    # Utilisation d'un ensemble (set)
    mots_set = {'pomme', 'banane', 'orange', 'pomme', 'poire'}
    print("Ensemble :", mots_set)  # Sortie : Ensemble : {'banane', 'pomme', 'orange', 'poire'}

    # Utilisation d'un dictionnaire (dict)
    mots_dict = {'pomme': 3, 'banane': 2, 'orange': 1, 'poire': 4}
    print("Dictionnaire :", mots_dict)  # Sortie : Dictionnaire : {'pomme': 3, 'banane': 2, 'orange': 1, 'poire': 4}






