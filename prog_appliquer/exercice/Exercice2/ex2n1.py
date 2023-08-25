ma_chaine = 'Christopher William'
print((ma_chaine+" ")*3)

phrase1= "Bonjour"
phrase2= "tout le monde"
phrase3= "comment allez-vous ?"

print(len(phrase1 + phrase2 + phrase3))
print(len(phrase1) + len(phrase2) + len(phrase3))

texte = open("/home/pureleaf/Documents/session_9/prog_appliquer/cour_2/bovary.txt", encoding="utf-8").read()
premiere_partie = texte[texte.rfind("PREMIÈRE PARTIE"):texte.find("DEUXIÈME PARTIE")]
print(premiere_partie[0:100])