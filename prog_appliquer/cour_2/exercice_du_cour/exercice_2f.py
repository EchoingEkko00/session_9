prix = float(input("Entrer le prix de l'article : "));
print("Le prix de l'article avant taxe est de : ", prix, "%");
tps = (prix * 5) / 100;
tvq = (prix * 9.975) / 100;
prixAvecTaxe = prix + tps + tvq;
print("Le prix de la TPS est de : ", tps, "$");
print("Le prix de la TVQ est de : ", tvq, "$");
print("Le prix de l'article avec taxe est de : ", prixAvecTaxe, "$");