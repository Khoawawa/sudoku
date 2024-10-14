import sys
import pygame
from random import randint, sample


class Board:
    PUZZLE_SIZE = 9
    WHITE = (251,247,245)
    BLACK = (0,0,0)
    
    def __init__(self,num_empties):
        self.original_board = [[0] * 9 for _ in range(9)] # 
        self.board = [[0] * 9 for _ in range(9)] # 
        self.empty = num_empties
        self.list_empty = []
        self.generate_board()
        
    def generate_board(self):
        self.fill_all_boxes(0)
        self.remove_elements()
    
    def fill_all_boxes(self, cell_index):
        # fill all cell from the current board starting from cell_index with a random number
        if cell_index == self.PUZZLE_SIZE * self.PUZZLE_SIZE:
            return True
        
        cell_row, cell_col = cell_index // 9, cell_index % 9
        list_nums = sample(range(1,10), 9)
        for num in list_nums:
            if self.safe_to_fill(cell_row,cell_col, num):
                self.board[cell_row][cell_col] = num
                if self.fill_all_boxes(cell_index + 1) is True:
                    return True
                self.board[cell_row][cell_col] = 0
        
        return False
    def safe_to_fill(self,row,col, num):
        return self.row_is_safe(row,num) and self.col_is_safe(col,num) and self.innerbox_is_safe(row - row%3, col - col%3, num)
    
    def row_is_safe(self,row,num):
        for i in range(9):
            if self.board[row][i] == num:
                return False
        return True
    def col_is_safe(self,col,num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True
    def innerbox_is_safe(self,row,col,num):
        for i in range(3):
            for j in range(3):
                if self.board[row + i][col + j] == num:
                    return False
        return True
    def remove_elements(self):
        #remove self.empty elements out of the board 
        while self.empty != 0:
            idx = randint(0,80)
            row, col = idx // 9, idx % 9
            while self.board[row][col - 1 if col != 0 else col] == 0:
                idx = randint(0,80)
                row, col = idx // 9, idx % 9 - 1
            self.board[row][col - 1 if col != 0 else col] = 0
            self.empty -= 1
        self.original_board = [[self.board[row][col] for col in range(self.PUZZLE_SIZE)] for row in range(self.PUZZLE_SIZE)]
        
if __name__ == "__main__":
    board = Board(4)
    board