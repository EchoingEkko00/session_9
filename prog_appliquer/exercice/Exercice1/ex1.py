import math;

a: float;
b: float;
c: float;
discriminant: float;
racine1: float;
racine2: float;
imaginaire: float;

donneeEntrer = input("Entrer a : ");
a = float(donneeEntrer);

donneeEntrer = input("Entrer b : ");
b = float(donneeEntrer);

donneeEntrer = input("Entrer c : ");
c = float(donneeEntrer);

discriminant = (b * b ) - ( 4 * a * c );

if discriminant < 0: 
    racine1 = (-b + math.sqrt(-discriminant)) / (2 * a);
    racine2 = (-b - math.sqrt(-discriminant)) / (2 * a);
    print("Il existe deux racines réelles distinctes : %.3f et %.3f\n", racine1, racine2);
elif discriminant == 0:
    racine1 = -b / (2 * a);
    print("Il existe une racine réelle double : %.3f\n", racine1);
elif discriminant < 0: 
    racine1 = -b / (2 * a);
    imaginaire = math.sqrt(-discriminant) / (2 * a);
    print("Il existe deux racines complexes conjuguées : %.3f + i%.3f et %.3f - i%.3f\n", racine1, imaginaire, racine1, imaginaire);

    