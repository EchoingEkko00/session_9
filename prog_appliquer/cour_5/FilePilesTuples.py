# code pour files, piles et tuples
FILE1 = []
FILE1.append("Annie")
FILE1.append("Bernard")
FILE1.append("Carole")
print(FILE1)
print(FILE1.pop(0))
print(FILE1)
FILE1.append("Denis")
FILE1.pop(0)
FILE1.pop(0)
FILE1.append("Élise")
print(FILE1)
FILE1.pop(0)
FILE1.pop(0)
print(FILE1)

PILE1 = []
PILE1.append("Annie")
PILE1.append("Bernard")
PILE1.append("Carole")
print(PILE1)
print(PILE1.pop())
print(PILE1)
PILE1.append("Denis")
PILE1.pop()
PILE1.pop()
PILE1.append("Élise")
print(PILE1)
PILE1.pop()
PILE1.pop()
print(PILE1)

tuple1 = (2, 7, 8, -6)
tuple2 = (2, 1.6, "Bonjour toi", 3, 6, 9)
tuple3 = ()
tuple4 = (1, 2, (5, 6, 7), 3, 4)
print(type(tuple4[2])) # retourne "tuple"
print(tuple4[2]) # retourne le tuple (5, 6, 7)
print(tuple4[2][1]) # retourne le nombre 6
tuple5 = ( (1, 2, 3), (4, -1, 9), (-2, 5, 0), (3, 2, 7) )
print(tuple5[2][1]) 	# retourne la valeur 5 car le nombre 5 correspond au
                # 2ème élément (indice 1) du 3ème élément (indice 2) du tuple "tuple5".
tuple6 = tuple(range(1, 100, 2))
print(tuple6[2:5]) # affiche (5,7,9)
print((2,3,4) + (4,5,6)) # affiche (2, 3, 4, 4, 5, 6)
print(len(tuple6)) # affiche 50
print(list((1,2,3))) # affiche [1, 2, 3]
print(set((1,2,3))) # affiche {1, 2, 3}
print(tuple6.index(5)) # affiche 2
print((1,2,3,4,5,4,3,2,1).count(3)) # affiche 2