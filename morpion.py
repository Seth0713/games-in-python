#! /usr/bin/python3
# -*-coding:UTF-8 -*

class Player(object):
    def __init__(self, name, victory):
        self.name = name
        self.victory = victory

board = []
global turn
turn = 0
letter = ["   A"," B"," C"," D"," E"," F"," G"," H"," I"," J"]
letter2 = []
number = ["1","2","3","4","5","6","7","8","9"]

player_1 = Player(input(' Player 1 / Enter your name : '),0)
player_2 = Player(input(' Player 2 / Enter your name : '),0)

def create_board(case):
 
    for x in range(0, case):
        board.append([" "]+[" --"] * case)  
        board.append([number[x]]+["|  "] * case + ["|"]+[number[x]])
    board.append([" "]+[" --"] * case)

    for x in range(0, case):
        letter2.append(letter[x])    
        
def showletter():
    showletter = ("  ").join(letter2)
    print (" "+showletter)
    return showletter
   
def see_board(board):
    print ("\n")
    showletter()
    for line in board:
        board = (" ").join(line)    
        print (board)
    showletter()
    print ("\n")
    return board

def start_game():
    
    print (player_1)
    see_board(board)

def choose_case():
    try:
        nbcase = int(input("\n How many cases do you want for the game, choose a number between 1 and 9 ? : "))
    except :
        choose_case()
    if nbcase >=1 and nbcase <=9:
        create_board(nbcase)
        start_game()
    else:
        print ("\n Becareful, your entered is not correct")
        choose_case()

def start_game():
    global turn
    if turn == 0:
        print ("\n\n////////////// PLAYER 1 : "+player_1.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        board[3][2]="| X"
        turn = 1
        start_game()
    else:
        print ("\n\n////////////// PLAYER 2 : "+player_2.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        turn = 0
        start_game()     

choose_case()



    
    

    


    
    

    
    


