#! /usr/bin/python3
# -*-coding:UTF-8 -*

class Player(object):
    def __init__(self, name, victory):
        self.name = name
        self.victory = victory

board = []
global turn, nbcase
nbcase = 0
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

def begin(): #Choose number of cases
    global nbcase
    try:
        nbcase = int(input("\n How many cases do you want for the game, choose a number between 3 and 9 ? : "))
    except :
        begin()
    if nbcase >=3 and nbcase <=9:
        create_board(nbcase)
        start_game()
    else:
        print ("\n Becareful, your entered is not correct")
        begin()

def start_game():
    print (nbcase)
    global turn
    col = 0
    if turn == 0:
        print ("\n\n////////////// PLAYER 1 : "+player_1.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        data = list(choice_case)
        print (data)
        alpha = ["A","B","C","D","E","F","G","H","I","J"]

        for i in range(nbcase):
            if data[0]==alpha[i]:
                col = i+1
                print (col)
                print (alpha[i])
            

        if data[1]=="1":
            line=1
        elif data[1]=="2":
            line=3

        board[line][col]="| X"
        turn = 1
        start_game()
    else:
        print ("\n\n////////////// PLAYER 2 : "+player_2.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        turn = 0
        start_game()     

begin()

    
    


