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

    print(astar_search(problem, board))

def massacre(board):
    problem = search.Problem(board)



# print(board.print_board())

# print(problem.result(problem.initial, actions[5]))







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


