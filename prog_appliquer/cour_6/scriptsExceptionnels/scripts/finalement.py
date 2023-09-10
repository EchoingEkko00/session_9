#finalement.py
import os
import sys

def creer_dossier(chemin, dossier):
    chemin_original = os.getcwd()
    print(chemin_original)
    try:
        os.chdir(chemin)
        os.mkdir(dossier)
    except OSError as e:
        print(e)
    finally: # s’exécute indépendamment du résultat du bloc try
        os.chdir(chemin_original)
        print("retour au bercail de toute façon")
