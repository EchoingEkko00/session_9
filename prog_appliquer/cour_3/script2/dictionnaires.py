#dictionnaires.py
acronymes = ['JPP', 'Mdr', 'GG', 'ASAP']
traductions = ["j'en peux plus", "mort de rire", "bien joué", "aussi tôt que possible"]
#si on enlève un acronyme, il faut aussi l'enlever dans la traduction
del acronymes[0]
del traductions[0]
#un dictionnaire associe des clés à des valeurs (notez les accolades)
dictionnaire_vide = {}
acronymes = {'JPP': "j'en peux plus", 'Mdr': "mort de rire", 'GG': "bien joué", 'ASAP': "aussi tôt que possible"}
print(acronymes['GG'])  # bien joué
#un dictionnaire peut contenir n'importe quel type de données
menu = {'Soupe':5, 'Salade': 6}
meli_melo = {'chaine':'chaine', 12:13, 'chaine':23.5, 45:'chaine'}
print(meli_melo[12])  # 13
#on peut ajouter des éléments: ils seront ajoutés sans ordre particulier et sans répétition (écrasement)
acronymes['gf'] = "petite amie"
acronymes['bf'] = "petit ami"
acronymes['TBH'] = "to be honest"
print(acronymes) 	# {'JPP': "j'en peux plus", 'Mdr': 'mort de rire', 'GG': 'bien joué',
                    # 'ASAP': 'aussi tôt que possible',
                    # 'gf': 'petite amie', 'bf': 'petit ami', 'TBH': 'to be honest'}
#mise à jour du dictionnaire
acronymes['TBH'] = "honnêtement"
print(acronymes) 	# {'JPP': "j'en peux plus", 'Mdr': 'mort de rire', 'GG': 'bien joué',
                    # 'ASAP': 'aussi tôt que possible',
                    # 'gf': 'petite amie', 'bf': 'petit ami', 'TBH': 'honnêtement'}
#effacer une valeur
del acronymes["bf"]
print(acronymes) 	# {'JPP': "j'en peux plus", 'Mdr': 'mort de rire', 'GG': 'bien joué',
                    # 'ASAP': 'aussi tôt que possible', 'gf': 'petite amie', 'TBH': 'honnêtement'}
#si on essaie d'accéder à ce qui n'existe pas, on provoque une erreur
# print(acronymes["absent"]) # KeyError: 'absent'
#c'est mieux de le faire avec la méthode get, on obtiendra le type None
if acronymes.get("absent") == None: # encore mieux : enlever == None et inverser la condition
    print("N'existe pas")
else:
    print("Existe")
#exemple d'utilisation pratique: traduire une phrase
jargon = "JPP de ma gf"
francais = acronymes.get("JPP") + " de ma " + acronymes.get("gf")
print(francais) # j'en peux plus de ma petite amie





