#etudiants.py
# Un dictionnaire pour les étudiants d'une classe
contactes = {
    "nombre":4,
    "etudiants":
        [
            {"nom":"Alain Bisson", "courriel":"abisson@example.com"},
            {"nom":"Zoé Zachman", "courriel":"zachman@example.com"},
            {"nom":"Artémise Boisvert", "courriel":"aboisvert@example.com"},
            {"nom":"François Claude", "courriel":"fclaude@example.com"}
        ]
}

print('Courriels des étudiants:')
for etud in contactes['etudiants']:
    print(etud['courriel'])
#abisson@example.com
#zachman@example.com
#aboisvert@example.com
#fclaude@example.com
print('Noms et courriels des étudiants:')
for etud in contactes['etudiants']:
    for cle, valeur in etud.items():
        print(cle, valeur)
#nom Alain Bisson
#courriel abisson@example.com
#nom Zoé Zachman
#courriel zachman@example.com
#nom Artémise Boisvert
#courriel aboisvert@example.com
#nom François Claude
#courriel fclaude@example.com

