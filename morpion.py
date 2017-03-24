board = []
letter = [" A"," B"," C"," D"," E"," F"," G"," H"," I"," J"]
letter2 = []
number = [1,2,3,4,5,6,7,8,9,10]

def create_board(case):
     
    for x in range(0, case):
        board.append([" --"] * case)  
        board.append(["|  "] * case + ["|"])
    board.append([" --"] * case)

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

nbcase = int(input("How many cases do you want for the game ? : "))

create_board(nbcase)

see_board(board)
    
