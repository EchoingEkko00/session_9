motHasard = "abaaa".upper()

dictLettre = {}
for i in range(0,len(motHasard)):
    dictLettre[i] = motHasard[i]
print(dictLettre)
print("A" in dictLettre.values())
for i in range(0,len(motHasard)):
    if "A" == dictLettre.get(i):
        print("ok")
        dictLettre.pop(i)