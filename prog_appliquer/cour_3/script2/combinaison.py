#combinaison.py
#Listes de menus
dejeuner = ["Oeufs", "Bagel", "Café"]
diner = ["Sandwich", "Hot Dog", "Riz frit"]
souper = ["Pâtes", "Boeuf", "Poisson"]
#on les combine
menus = []
menus.append(dejeuner)
menus.append(diner)
menus.append(souper)
print(menus, menus[1],menus[1][1])
#[['Oeufs', 'Bagel', 'Café'], ['Sandwich', 'Hot Dog', 'Riz frit'], ['Pâtes', 'Boeuf', 'Poisson']]
# ['Sandwich', 'Hot Dog', 'Riz frit'] Hot Dog
#voici une meilleure oragnistion de nos menus avec un dictionnaire
menus = {'déjeuner': dejeuner, 'dîner': diner, 'souper': souper}
print(menus, menus['dîner'],menus['dîner'][1])
#{'déjeuner': ['Oeufs', 'Bagel', 'Café'], 'dîner': ['Sandwich', 'Hot Dog', 'Riz frit'],
#'souper': ['Pâtes', 'Boeuf', 'Poisson']} ['Sandwich', 'Hot Dog', 'Riz frit'] Hot Dog
#affichons les clés 
for menu in menus:
    print(menu)
# déjeuner dîner souper
#méthode utile pour un dictionnaire: items()
print(menus.items())
#dict_items([('déjeuner', ['Oeufs', 'Bagel', 'Café']), ('dîner', ['Sandwich', 'Hot Dog', 'Riz frit']), ('souper', ['Pâtes', 'Boeuf', 'Poisson'])])
#on peut maintenant afficher la clé et la valeur
for cle, valeur in menus.items():
        print(cle, ":", valeur)
#déjeuner : ['Oeufs', 'Bagel', 'Café']
#dîner : ['Sandwich', 'Hot Dog', 'Riz frit']
#souper : ['Pâtes', 'Boeuf', 'Poisson']

#utilisation particulière d'un dictionnaire: la représentation d'objets
personne = {
    'nom': 'Jean',
    'age': 30,
    'ville': 'New York'
}
# Avec keys() on obtient toutes les clés du dictionnaire
cles = personne.keys()
print("Clés:", cles)
# Avec values() on obtient toutes les valeurs du dictionnaire
valeurs = personne.values()
print("Valeurs:", valeurs)

