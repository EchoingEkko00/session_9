# Table de multiplication avec base, debut, fin et incrementation
def tableMultiplcation(base, debut, fin, incrementation) :
    for i in range(debut, fin, incrementation) :
        print(i, "x", base, "=", base * i)

# Fonction cubique
def cube(x) :
    return x * x * x

# Fonction qui calcule le volume d'un sphere de rayon r
def volumeSphere(r) :
    return 4 / 3 * 3.14 * cube(r)

#Tests
tableMultiplcation(7, 2, 13, 2)
print(volumeSphere(5))
