from Ant_system import AntSystem
import pygame as pg
from Game import Game

SCREEN_WIDTH, SCREEN_HEIGHT = 550, 550
PUZZLE_WIDTH, PUZZLE_HEIGHT = 500, 500
WHITE = (251,247,245)
BLACK = (0,0,0)

def main():
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pg.display.set_caption('Sudoku')
    
    board = Game(PUZZLE_WIDTH,PUZZLE_HEIGHT)
    
    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
        draw_Window(screen,board)
        pg.display.update()
def draw_Window(screen, board:Game):
    screen.fill(WHITE)
    font = pg.font.SysFont('Comic Sans MS', 35)
    board.draw(screen)
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()