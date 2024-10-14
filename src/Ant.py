from Board import Board
from copy import deepcopy
from Board_sudoku import BoardSudoku as BS

class Ant:
    def __init__(self,system):
        self.sol: BS = None
        self.cell = 0 #cell that ant are currently occupying
        self.system = system # ref for the ACS
        self.fail_cells = 0 # cant be filled cells
        self.roulette = [] # pheromone roulette
        self.roulette_vals = [] #val for roulette
    
    def init_solution(self, puzzle: BS, start_cell):
        self.sol = deepcopy(puzzle) #give the ant a copy of the puzzle
        self.cell = start_cell # place the ant on the start_cell
        self.fail_cells = 0
        
        self.roulette = [0 for _ in range(9)] 
        self.roulette_vals = [0 for _ in range(9)]
        
    def num_cells_filled(self):
        return 81 - self.fail_cells 
    
    def step_solution(self):
        
        if self.sol.cell_empty(self.cell):
            #report cells that cant be filled bcs list_cell is empty --> caused by propagating constraint in previous iteration
            self.fail_cells += 1
        
        elif not self.sol.cell_fixed(self.cell):
            # IF CURRENT CELL IS NOT SET THEN SET CELL
            # use probabilistic action selection to determine exploitation or exploration --> formula (3)
            if self.system.get_random() > self.system.get_q0():
                #exploitation -> find the best pheromone choice in that cell
                best = 0
                max_pher = -1.0
                
                for choice in self.sol.list_cells[self.cell]:
                    #select choice that have the max pheromone
                    if self.system.get_pher(self.cell,choice - 1) > max_pher:
                        max_pher = self.system.get_pher(self.cell, choice - 1)
                        best = choice
                # SET CELL VALUE AND PROPAGATE CONSTRAINT
                self.sol.set_cell(self.cell, best)
                # UPDATE LOCAL PHEROMONE
                self.system.update_local_pheromone(self.cell, best - 1)
            else:
                #exploration --> use roulette wheel selection --> choices that have higher pheromone have bigger area in the roulette
                tot_pher = 0.0 #total amount of pheromones
                num_choices = 0 #determine how many choices are in the roulette
                
                for choice in self.sol.list_cells[self.cell]:
                    # set up the pheromone roulette
                    tot_pher = self.roulette[num_choices] = tot_pher + self.system.get_pher(self.cell,choice - 1)
                    self.roulette_vals[num_choices] = choice
                    num_choices += 1
                
                roulette_val = tot_pher * self.system.get_random() #probabilistic action selection threshold
                
                for i in range(num_choices):
                    # selecting roulette
                    if self.roulette[i] > roulette_val:
                        #SET CELL VALUE AND PROPAGATE CONSTRAINT
                        self.sol.set_cell(self.cell,self.roulette_vals[i])
                        #UPDATE LOCAL PHEROMONE
                        self.system.update_local_pheromone(self.cell,self.roulette_vals[i] - 1)
                        break
        # MOVE TO THE NEXT CELL
        self.cell += 1 
        
        if self.cell == 81:
            #if ant reach the end of the puzzle go to the beginning --> ensure the ant have gone through the entire board
            self.cell = 0
                    