from lobe import ImageModel

modele = ImageModel.load("..")

for i in range(3):
    resultat = modele.predict_from_file('test/a'+str(i+1)+'.jpeg')
    for animal, confiance in resultat.labels:
        print("Animal " + str(i+1) + f" {animal}: {confiance*100}%")