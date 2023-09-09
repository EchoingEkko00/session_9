#Utilisation commune
acronymes = ['LOL', 'TBH', 'SMH', 'IDK']
for acronyme in acronymes:
    print(acronyme)
for i in range(len(acronymes)):
    print('Un acronyme : ' + acronymes[i])
for acronyme in acronymes:
    print(acronyme, end = ' ')
print() # retour à la ligne
#Itération sur les éléments d'une chaîne
for lettre in 'Python':
    print('Lettre courante :', lettre)
#Comparaison entre une liste et un range
print(type(acronymes))
print(type(range(0,7,1)))
total = 0
depenses = []
for d in range(3):
    depenses.append(float(input("Entrez une dépense: ")))
total = sum(depenses)
print("Vous avez dépensé $", total, sep = '')
# Un while ... else: le else devient pertinent quand on break dans le while
# Le else s'exécute seulement si on sort sans le break (donc normalement). 
i = 0
while i < 5:
    print(i)
    if i == 2:
        break  
    i = i + 1
else:
    print('ELSE')
print("Instruction suivante") 