from Ant import Ant
from Board import Board
from copy import deepcopy
import random
MAX_PHEROMONE = 100000000000000000
class AntSystem:
    def __init__(self,num_ants,q0, pher0,standard_eva, best_eva):
        #init ant
        self.num_ants = num_ants # number of ants
        self.ant_list = [Ant(self) for _ in range(num_ants)] 
        self.randomGen = random.Random() # random value for deciding exploitation or exploration
        self.q0 = q0 #threshold value for deciding exploit vs explore
        self.pher0 = pher0 #initial pheromone val
        self.standard_eva = standard_eva #
        self.best_eva = best_eva
    
    def init_pheromone(self, num_cells, values_per_cell):
        self.num_cells = num_cells
        self.pher = [[self.pher0] * values_per_cell for _ in range(num_cells)]# each cell have values_per_cell choices where they are init with pher0
    
    def get_solution(self):    
        return self.best_sol
    def get_random(self):
        return self.randomGen.uniform(0.0,1.0)
    
    def get_q0(self):
        return self.q0
    
    def get_pher(self,i,k):
        return self.pher[i][k]
    
    def clear_pher(self):
        self.pher = []
        
    def update_local_pheromone(self, cell, choice):
        self.pher[cell][choice] = self.pher[cell][choice] * 0.9 + self.pher0 * 0.1 #formula (4)
    
    def pher_add(self,cells_filled):
        if self.num_cells == cells_filled: 
            #if cell_filled = num_cells then this is the solution --> return the maximum pheromone
            return MAX_PHEROMONE
        return self.num_cells * 1.0 / (self.num_cells - cells_filled) #see formula 4
    
    def update_global_pheromone(self):
        for i in range(self.num_cells):
            #iterate  through each cell and update pheromone for each cell
            row, col = i // 9, i % 9
            bSol_cell = self.best_sol.board[row][col] 
            if bSol_cell > 0:
                #formula (6)
                self.pher[i][bSol_cell - 1] = self.pher[i][bSol_cell - 1] * (1 - self.standard_eva) + self.standard_eva*self.best_pher 
                
    def solve(self,board):
        iter = 0
        solved = False
        best_pher = 0
        #INITIALIZE PHEROMONE MATRIX
        self.init_pheromone(81,9)
        
        while not solved:
            # GIVE EACH ANT A COPY OF THE PUZZLE AND A RANDOM LOCATION ON THE BOARD
            for ant in self.ant_list:
                #ant go do sth
                rnd = random. randint(0,80)
                ant.init_solution(board, rnd)
            # LINE 9 - 19 IN PSEUDO CODE
            for i in range(81):
                for ant in self.ant_list:
                    ant.step_solution()
            
            best_ant = 0
            best_val = 0
            for ant in self.ant_list:
                #FIND BEST ANT
                if ant.num_cells_filled() > best_val:
                    best_val = ant.num_cells_filled();
                    best_ant = ant
            
            pher_to_add = self.pher_add(best_val) #update delta T
            
            if pher_to_add > best_pher:
                #when delta T exceed current best pheromone to add(delta T best)
                self.best_sol = deepcopy(best_ant.sol) # get the solution of the best ant
                self.best_pher = pher_to_add # set delta T best to delta T
                if best_val == self.num_cells: 
                    #obviously if best val(num of cell filled by the best ant) = number of cell need to be filled then it is solved
                    solved = True
            #UPDATE GLOBAL PHEROMONE
            self.update_global_pheromone()
            # BEST VALUE EVAPORATION -> formula(7)
            best_pher *= (1.0 - self.best_eva)
            
            iter += 1
            if iter % 100 == 0:
                break
            
        if solved:
            print('Iteration: ',iter)
        self.clear_pher() 
        return solved
    


    