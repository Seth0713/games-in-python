#! /usr/bin/python3
# -*-coding:UTF-8 -*

class Player(object):
    def __init__(self, name, victory, defeat, equality, turn):
        self.name = name
        self.victory = victory
        self.defeat = defeat
        self.equality = equality
        self.turn = turn            
        
class Board(object):       
    def __init__(self):
        self.nbcase = 3
        self.number = ["1","2","3"]
        self.letter = ["A","B","C"]
        self.board = []
        self.choicelist = []

        for x in range(0, self.nbcase):
            self.board.append([" "]+[" ——"] * self.nbcase)
            self.board.append([self.letter[x]]+["|  "] * self.nbcase + ["|"])
        self.board.append([" "]+[" ——"] * self.nbcase)
        
    def see(self, board):
        print ("\n   ",self.number[0]," ",self.number[1]," ",self.number[2])
        for line in self.board:           
            print ((" ").join(line))

    def write(self, line, col, sign):
        self.line = line
        self.col = col
        self.sign = sign
        self.line = self.line.upper()
        
        for i in range(self.nbcase):              
            if self.line==self.letter[i]:
                self.line = i+(i+1)        
        self.board[int(self.line)][int(self.col)]=self.sign  

    def control(self):
        if self.board[1][1]=="| X" and self.board[1][2]=="| X" and self.board[1][3]=="| X" \
        or self.board[3][1]=="| X" and self.board[3][2]=="| X" and self.board[3][3]=="| X" \
        or self.board[5][1]=="| X" and self.board[5][2]=="| X" and self.board[5][3]=="| X" \
        or self.board[1][1]=="| X" and self.board[3][1]=="| X" and self.board[5][1]=="| X" \
        or self.board[1][2]=="| X" and self.board[3][2]=="| X" and self.board[5][2]=="| X" \
        or self.board[1][3]=="| X" and self.board[3][3]=="| X" and self.board[5][3]=="| X" \
        or self.board[1][1]=="| X" and self.board[3][2]=="| X" and self.board[5][3]=="| X" \
        or self.board[1][3]=="| X" and self.board[3][2]=="| X" and self.board[5][1]=="| X":

            win = True
            



