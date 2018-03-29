from board import Board
from BoardProblem import BoardProblem
import getMoves
import math
import copy
import aima
from utils import *
from search import *



board = Board()

board.populateBoardFromInput()


# Check which run mode is desired
mode = input()

problem = BoardProblem(board)
actions = problem.actions(problem.initial)



if(mode == 'Moves'):
    print(getMoves.moves(board, 'white'))
    print(getMoves.moves(board, 'black'))

elif(mode == 'Massacre'):
    print("Doing massacre")

    print(breadthFirst(problem))

def massacre(problem):
    
    states = []
    
    states.append(problem.initial)
    
    for board in states:
        
        for 
        
    




# X O O O O O O X
# - @ - - - - - -
# - @ - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - @
# X - - - - - - X


# X - - - - - - X
# - - - - - - - -
# - - - - - O - -
# - - - - @ O - -
# - - - - - - O -
# - - - - - O @ -
# - - - - - - - @
# X - - - - - - X
# Massacre


