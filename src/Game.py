import pygame as pg
from Board import Board

class Game:
    PUZZLE_SIZE = 9
    BLACK = (0,0,0)
    
    def __init__(self,width,height):
        self.board = Board(40)
        self.row = self.col = self.PUZZLE_SIZE
        
        self.width = width
        self.height = height
        
        self.gap = self.width // 10
        self.selected = None
        
    def draw(self,screen):
        for i in range(self.row + 1):
            thick = 4 if not (i % 3) else 2
            #draw horizontal line
            pg.draw.line(screen, 
                         self.BLACK, 
                         (self.gap, self.gap + i * self.gap),
                         (self.width, self.gap + i*self.gap),
                         thick)
            #draw vertical line
            pg.draw.line(screen, 
                         self.BLACK, 
                         (self.gap + i *self.gap, self.gap),
                         (self.gap + i*self.gap, self.height),
                         thick)
  