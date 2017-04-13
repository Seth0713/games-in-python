#! /usr/bin/python3
# -*-coding:UTF-8 -*

from classes import Player

board = []
win = False
nbcase = 0
turn = 0
letter = ["   A"," B"," C"]
letter2 = []
number = ["1","2","3"]

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
    nbcase = 3    
    create_board(3)
    print ("\n You must align {0} form for win".format(nbcase))
    start_game()
    

def read_board(): #for determinate if a player has win
    global win
    if board[1][1]=="| X" and board[1][2]=="| X" and board[1][3]=="| X" \
        or board[3][1]=="| X" and board[3][2]=="| X" and board[3][3]=="| X" \
        or board[5][1]=="| X" and board[5][2]=="| X" and board[5][3]=="| X" \
        or board[1][1]=="| X" and board[3][1]=="| X" and board[5][1]=="| X" \
        or board[1][2]=="| X" and board[3][2]=="| X" and board[5][2]=="| X" \
        or board[1][3]=="| X" and board[3][3]=="| X" and board[5][3]=="| X" \
        or board[1][1]=="| X" and board[3][2]=="| X" and board[5][3]=="| X" \
        or board[1][3]=="| X" and board[3][2]=="| X" and board[5][1]=="| X":

        see_board(board)
        win = True
      
    return win

def start_game():
    global turn
    col = 0
    if turn == 0:
        print ("\n\n////////////// PLAYER 1 : "+player_1.name+" //////////////")
        see_board(board)
        choice_case = input(" Choose a case (for exemple : A2 or C1) : ")
        data = list(choice_case)
        alpha = ["A","B","C"]

        for i in range(nbcase):                     
                
            if data[0].upper()==alpha[i]:
                col = i+1
                
        for j in range(nbcase):
            if data[1]==number[j]:
                line = int(number[j])+(int(number[j])-1)
                print("line",line)
        
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
        alpha = ["A","B","C"]

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


    
    


