from Ant_system import AntSystem
from Board_sudoku import BoardSudoku
import sudoku_checker
PUZZLE_SIZE = 9
def main():
    numAnts = 10
    q0 = 0.9
    standard_eva = 0.9
    best_eva = 0.0005
    pher0 = 1 / 81
    
    extreme_board = [
        [0,7,0,0,0,0,0,9,0],
        [0,0,9,0,0,3,0,1,0],
        [5,6,0,0,2,8,0,0,0],
        [0,0,0,6,0,0,0,0,1],
        [0,0,0,0,4,0,0,0,0],
        [2,5,0,0,3,0,0,6,0],
        [8,0,0,0,5,0,9,0,0],
        [0,0,0,0,9,0,0,2,0],
        [0,0,6,0,0,0,0,7,0]
    ]
    
    board = BoardSudoku(extreme_board)
    
    solver = AntSystem(numAnts,q0,pher0,standard_eva,best_eva)
    
    success = solver.solve(board)
    
    if success is True:
        sol = solver.get_solution();
        
        for line in sol.board:
            print(line)
        valid = sudoku_checker.is_valid_sudoku(sol.board)
        print("is valid board" if valid else "is not valid board")

main()
    