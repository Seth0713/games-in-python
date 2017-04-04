class Player(object):
    def __init__(self, nom, victoire):
        self.nom = nom
        self.victoire = victoire

board = []
letter = ["   A"," B"," C"," D"," E"," F"," G"," H"," I"," J"]
letter2 = []
number = ["1","2","3","4","5","6","7","8","9"]

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

def choose_case():
    nbcase = int(input("\n How many cases do you want for the game, choose a number between 1 and 9 ? : "))
    if nbcase >=1 and nbcase <=9:
        create_board(nbcase)
        see_board(board)
    else:
        print ("\n Becareful, your entered is not correct")
        choose_case()
        
    

player_1 = Player(input(' Player 1 / Enter your name : '),0)
player_2 = Player(input(' Player 2 / Enter your name : '),0)

choose_case()
    
    


