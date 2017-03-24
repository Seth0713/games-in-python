board = []

def create_board(case):
               
    for x in range(0, case):
        board.append([" --"] * case)  
        board.append(["| ."] * case + ["|"])
    board.append([" --"] * case)
    
        
def see_board(board):
    for line in board:
        board = (" ").join(line)
    
        print (board)
    return board

nbcase = int(input("How many cases do you want for the game ? : "))

create_board(nbcase)

see_board(board)
    
