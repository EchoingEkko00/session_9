motHasard = "abaaa".upper()
#Create a dictionary with the the position of each letter in the word as key and the letter as value
dictLettre = {}
for i in range(0,len(motHasard)):
    dictLettre[i] = motHasard[i]

print("A" in dictLettre.values())