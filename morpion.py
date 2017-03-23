board = []

def create_board(case):
               
    for x in range(0, case):
        board.append([" --"] * case)  
        board.append(["|  "] * case)
    board.append([" --"] * case)
        
def see_board(board):
    for line in board:
        print (" ".join(line))

nbcase = int(input("How many cases : "))

create_board(nbcase)

see_board(board)
    
