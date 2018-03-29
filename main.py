from board import Board
from BoardProblem import BoardProblem
import getMoves
import math
import aima

board = Board()

board.populateBoardFromInput()


# Check which run mode is desired
mode = input()

if(mode == 'Moves'):
    print(getMoves.moves(board, 'white'))
    print(getMoves.moves(board, 'black'))

elif(mode == 'Massacre'):
    print("Doing massacre")


def massacre(board):
    problem = search.Problem(board,None)


problem = BoardProblem(board)
actions = problem.actions(problem.initial)

print(board.print_board())

print(problem.result(problem.initial, actions[5]))





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


