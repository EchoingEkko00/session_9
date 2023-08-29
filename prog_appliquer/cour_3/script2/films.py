#films.py
# Un dictionnaire pour l'heure de projection de films
films_affiche = {'Monsieur Hire': '11:00am',
                 'Neuf semaines et demi': '1:00pm',
                 'Manon des Sources': '3:00pm',
                 'Jean de Florette': '5:00pm'}

print("Voici les films présentement à l'affiche:")
for cle in films_affiche:
    print(cle)
#Monsieur Hire
#Neuf semaines et demi
#Manon des Sources
#Jean de Florette
film = input('Quel film voulez-vous voir? ')

horaire = films_affiche.get(film)
if(horaire == None):
    print("Ce film n'est pas à l'affiche")
else:
    print(film, 'est présenté à', horaire)
#Quel film voulez-vous voir? Manon des Sources
#Manon des Sources est présenté à 3:00pm

