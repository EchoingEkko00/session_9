#callback.py
def fct_callback(arg):
    print(f"J'aime bien le {arg} !")


def une_fct(ma_callback):
    print("Je m'apprête à appeler la fonction callback :")
    ma_callback("psyllium")
    print("Je termine.")

if __name__ == "__main__":
    une_fct(fct_callback)