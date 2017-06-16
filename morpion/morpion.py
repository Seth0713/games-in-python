#! /usr/bin/python3
# -*-coding:UTF-8 -*

from classes import *

plateau = Board()
player_1 = Player(input(' Player 1 / Enter your name : '),0,0,0,True,False)
player_2 = Player(input(' Player 2 / Enter your name : '),0,0,0,False,False)

print ("\n You must align {0} form for win, may the best win !".format(plateau.nbcase))
win = False

def engine(name, sign, turn1, turn2):
    print ("\n ||||||||||||||||||||||||||||||",name,"||||||||||||||||||||||||||||||")        
    plateau.see(plateau)
    choice_case = list(input("\n"+name+" choose a place (for exemple : A2 or C1) : "))

    if choice_case not in plateau.choicelist:
        plateau.write(choice_case[0],choice_case[1],sign)
        plateau.choicelist.append(choice_case) 
        player_1.turn=turn1
    else:
        print('\n\n\n \\\\\ BECAREFUL THE PLACE IS NOT EMPTY ? CHOOSE AN ANOTHER PLACE \\\\\ ')
        player_1.turn=turn2 


def main():
    while plateau.win==False:
        if player_1.turn==True:
        
            engine(player_1.name,'| X',False,True)
            if plateau.control('| X') is True:
                print (plateau.win)
                again = input("Good you win, can you play again ? (Y or N) : ")
                if again=="Y":
                    main()
              
        else:
            engine(player_2.name,'| O',True,False)
    print(win)

main()
    
                
#Message pour la fin de partie
#incrémenter victoire, défaite ou égalité
#enregistrer résultats dans un fichier
#Debugger





    
    



    
    


