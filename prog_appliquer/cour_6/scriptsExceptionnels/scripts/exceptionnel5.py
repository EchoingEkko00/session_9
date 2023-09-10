#exceptionnel5.py
import sys
DIGIT_MAP = {
      'zéro':  '0',
      'un':    '1',
      'deux':  '2',
      'trois': '3',
      'quatre':'4',
      'cinq':  '5',
      'six':   '6',
      'sept':  '7',
      'huit':  '8',
      'neuf':  '9',
}
#converti une liste ["un", "deux", "trois"] en nombre entier 123
def convertir(nombres):
    try:
        nombre = ''
        for s in nombres:
            nombre += DIGIT_MAP[s]
        return(int(nombre))
    except (KeyError, TypeError) as e:
        print(f"Conversion manquée: {repr(e)}", file = sys.stderr)
        #repr(objet) retourne la version imprimable de cet objet
        #repr() est généralement redéfinie pour cet objet
        return -1
    return x

