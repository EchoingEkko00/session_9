#exceptionnel7.py
import sys
from math import log
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
        raise # relance l'exception
    return x
#converti une liste ["un deux trois"] en son logarithme naturel 4.812184355372417
def string_log(s):
    try:
        v = convertir(s)
    except:
        return -1
    return log(v)

