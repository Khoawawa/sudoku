from Board import Board
from copy import deepcopy

class BoardSudoku:
    def __init__(self, board):
        self.board = deepcopy(board)
        
        self.list_cells = [] # list contain all possible values for cells, tuple
        self.list_fixed = [] # list for cells that are fixed
        
        for row in range(9):
            for col in range(9):
                if self.board[row][col] > 0:
                    self.list_fixed.append((row,col))
                    self.list_cells.append([self.board[row][col]])
                else: 
                    self.list_cells.append([i + 1 for i in range(9)])
        #
        for i in range(len(self.list_fixed)):
            #PROPAGATE CONSTRAINTS
            self.propagation(self.list_fixed[i][0],self.list_fixed[i][1])
    
    def propagation(self,row,col):
        #constraint propagation algorithm
        pos = row * 9 + col 
        for i in range(9):
            if row* 9 + i != pos:
                #iterate through row
                if self.board[row][col] in self.list_cells[row*9 + i]:
                    self.list_cells[row*9 + i].remove(self.board[row][col])
                    if len(self.list_cells[row*9 + i]) == 1:
                        self.board[row][i] = self.list_cells[row*9 + i][0]
                        self.propagation(row,i)
            if i * 9 + col != pos:
                #iterate through col
                if self.board[row][col] in self.list_cells[i*9 + col]:
                    self.list_cells[i*9 + col].remove(self.board[row][col])
                    if len(self.list_cells[i*9 + col]) == 1:
                        self.board[i][col] = self.list_cells[i*9 + col][0]
                        self.propagation(i,col)
        
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for i in range(3):
            for j in range(3):
                #iterate through inner box
                posx = (box_row + i) * 9 + (box_col + j)
                if posx != pos:
                    if self.board[row][col] in self.list_cells[posx]:
                        self.list_cells[posx].remove(self.board[row][col])
                        if len(self.list_cells[posx]) == 1:
                            self.board[box_row+i][box_col+j] = self.list_cells[posx][0]
                            self.propagation(box_row+i,box_col+j)
    
    def cell_empty(self,cell):
        return len(self.list_cells[cell]) == 0
    
    def cell_fixed(self,cell):
        return len(self.list_cells[cell]) == 1
    
    def set_cell(self, cell, choice_val):
        #SET CELL VALUE
        self.board[cell // 9][cell % 9] = choice_val
        #PROPAGATING CONSTRAINT
        self.propagation(cell // 9, cell % 9)
        