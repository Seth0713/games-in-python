#! /usr/bin/python3
# -*-coding:UTF-8 -*

from Classes import Player

board = []
win = False
nbcase = 0
turn = 0
letter = ["   A"," B"," C"," D"," E"," F"," G"," H"," I"," J"]
letter2 = []
number = ["1","2","3","4","5"]

player_1 = Player(input(' Player 1 / Enter your name : '),0,0,0)
player_2 = Player(input(' Player 2 / Enter your name : '),0,0,0)

def create_board(case):
    
    for x in range(0, case):
        board.append([" "]+[" ——"] * case)  
        board.append([number[x]]+["|  "] * case + ["|"]+[number[x]])
    board.append([" "]+[" ——"] * case)

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

def begin(): #Choose number of cases
    global nbcase
    try:
        nbcase = int(input("\n How many cases do you want for the game, choose a number between 3 and 5 ? : "))
    except :
        begin()
    if nbcase >=3 and nbcase <=5:
        create_board(nbcase)
        print ("\n You must align {0} form for win".format(nbcase))
        start_game()
    else:
        print ("\n Becareful, your entered is not correct")
        begin()


def read_board(): #for determinate if a player has win
    global win
    print(board)
    #win = True 


def start_game():
    global turn
    col = 0
    if turn == 0:
        print ("\n\n////////////// PLAYER 1 : "+player_1.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        data = list(choice_case)
        alpha = ["A","B","C","D","E","F","G","H","I","J"]

        for i in range(nbcase):                     
                
            if data[0].upper()==alpha[i]:
                col = i+1
                
        for j in range(nbcase):
            if data[1]==number[j]:
                line = int(number[j])+(int(number[j])-1)                       
        
        board[line][col]="| X"
        read_board()
            
        if win==True:
            print (" {0} win the party".format(player_1.name))            
        else:
            turn = 1
            start_game()
    else:
        print ("\n\n////////////// PLAYER 2 : "+player_2.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        data = list(choice_case)
        alpha = ["A","B","C","D","E","F","G","H","I","J"]

        for i in range(nbcase):
            if data[0].upper()==alpha[i]:
                col = i+1
                
        for j in range(nbcase):
            if data[1]==number[j]:
                line = int(number[j])+(int(number[j])-1)                       
        
        board[line][col]="| O"      

        read_board()
            
        if win==True:
            print (" {0} win the party".format(player_2.name))            
        else:
            turn = 0
            start_game()

begin()


    
    


