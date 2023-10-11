# Mettez vos import ici
from gpiozero import PWMLED, RGBLED, LED
from time import sleep

# Vos structures de données sont les suivantes: il faut les respecter
laGrille= { '11': ' ' , '12': ' ' , '13': ' ' ,
            '21': ' ' , '22': ' ' , '23': ' ' ,
            '31': ' ' , '32': ' ' , '33': ' ' }

lesPWMLEDS = { 	'11': PWMLED(23) , 	'12': PWMLED(25) , 	'13': PWMLED(16) ,
                '21': PWMLED(24) , 	'22': PWMLED(12) , 	'23': PWMLED(20) ,
                '31': PWMLED(27), 	'32':PWMLED(22)  , 	'33': PWMLED(13) }

laRGBLED = RGBLED(18, 19, 26) # compléter les arguments

# Cette fonction reçoit la grille et l'affiche
def afficheGrille(grille):
    print()
    print(grille['11'] + '|' + grille['12'] + '|' + grille['13'])
    print('-+-+-')
    print(grille['21'] + '|' + grille['22'] + '|' + grille['23'])
    print('-+-+-')
    print(grille['31'] + '|' + grille['32'] + '|' + grille['33'])

# Cette fonction reçoit la grille et retourne vrai si elle est pleine (match nul) ou faux sinon
# def grillePleine(grille):
def checkWin() :
    #Check if the player has won
    if (laGrille['11'] == laGrille['12'] == laGrille['13'] == 'X' or
        laGrille['21'] == laGrille['22'] == laGrille['23'] == 'X' or
        laGrille['31'] == laGrille['32'] == laGrille['33'] == 'X' or
        laGrille['11'] == laGrille['21'] == laGrille['31'] == 'X' or
        laGrille['12'] == laGrille['22'] == laGrille['32'] == 'X' or
        laGrille['13'] == laGrille['23'] == laGrille['33'] == 'X' or
        laGrille['11'] == laGrille['22'] == laGrille['33'] == 'X' or
        laGrille['13'] == laGrille['22'] == laGrille['31'] == 'X'):
        return 'X'
    elif (laGrille['11'] == laGrille['12'] == laGrille['13'] == 'O' or
        laGrille['21'] == laGrille['22'] == laGrille['23'] == 'O' or
        laGrille['31'] == laGrille['32'] == laGrille['33'] == 'O' or
        laGrille['11'] == laGrille['21'] == laGrille['31'] == 'O' or
        laGrille['12'] == laGrille['22'] == laGrille['32'] == 'O' or
        laGrille['13'] == laGrille['23'] == laGrille['33'] == 'O' or
        laGrille['11'] == laGrille['22'] == laGrille['33'] == 'O' or
        laGrille['13'] == laGrille['22'] == laGrille['31'] == 'O'):
        return 'O'
    else :
        return 'N'

# Écrivez ici vos autres fonctions au besoin

# La fonction principale qui permet de jouer
def jeu():
    userInput = ""
    playing = True
    win = False
    userTurn = True
    while True :
        while playing:
            while True and userTurn :
                userInput = input("Enter votre coup: ")
                if (userInput not in laGrille.keys()):
                    print("Exception - cette case n'existe pas")
                    laRGBLED.pulse(1,1, (0,1,1), (0,0,0))
                    sleep(3)
                    laRGBLED.off()
                    continue
                elif (laGrille[userInput] == 'X' or laGrille[userInput] == 'O'):
                    print("Exception - cette case est déjà prise")
                    laRGBLED.pulse(1,1, (0,1,1), (0,0,0))
                    sleep(3)
                    laRGBLED.off()
                    continue
                else :
                    laGrille[userInput] = 'X'
                    afficheGrille(laGrille)
                    #Turn on the LED with intensity under 0.5
                    lesPWMLEDS[userInput].on()
                    lesPWMLEDS[userInput].value = 0.5
                    userTurn = False
                    break
            if (len([i for i, e in enumerate(laGrille.values()) if e == ' ']) == 4):
                laRGBLED.on()
                laRGBLED.color = (1,0,1)
            if userTurn == False :
                #play the computer turn
                for cle in laGrille.keys():
                    if (laGrille[cle] == ' '):
                        laGrille[cle] = 'O'
                        afficheGrille(laGrille)
                        #Turn on the LED with intensity under 0.5
                        lesPWMLEDS[cle].on()
                        lesPWMLEDS[cle].value = 0.05
                        userTurn = True
                        break
            win = checkWin()
            if (win == 'X'):
                print("Terminer, O a gagné!")
                break
            elif (win == 'O'):
                print("Terminer, X a gagné!")
                #Blink the RGB LED in green
                laRGBLED.blink(1,1,0,0,(1,1,0), (0,0,0))
                sleep(3)
                laRGBLED.off()
                break
            elif (win == 'N' and ' ' not in laGrille.values()):
                print("Match nul!")
                break
        if (' ' not in laGrille.values() or (win == 'X' or win == 'O')):
            replay = input("Voulez-vous rejouer? (o/n)")
            if (replay == "o"):
                playing = True
                for cle in laGrille:        
                    lesPWMLEDS[cle].off()
                for cle in laGrille:
                    laGrille[cle] = ' '
            else :
                playing = False
                print("Merci d'avoir joué!")
                break
  


      
#  Point de départ du programme V2
if __name__ == "__main__":
     jeu()
     for cle in laGrille:        
         lesPWMLEDS[cle].close() # terminer proprement
