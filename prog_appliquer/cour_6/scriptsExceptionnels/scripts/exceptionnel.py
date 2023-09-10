#exceptionnel.py
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
      nombre = ''
      for s in nombres:
          nombre += DIGIT_MAP[s]
      x = int(nombre)
      return x

