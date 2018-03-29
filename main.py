from board import Board
import getMoves
import math
import copy



board = Board()

board.populateBoardFromInput()


# Check which run mode is desired
mode = input()


def massacre(initial):
    
    states = []
    
    states.append(initial)
    
    for board in states:
        
       actions = board.expandBoard()
       
       
       for i in actions:
           
            state = copy.deepcopy(board)
            state.makeMove(i[0],i[1])
            state.isKilled("black")
            state.isKilled("white")
            if state.goal_test():
                return state
            else:
                   states.append(state)
                
           
    

if(mode == 'Moves'):
    print(getMoves.moves(board, 'white'))
    print(getMoves.moves(board, 'black'))

elif(mode == 'Massacre'):
    print("Doing massacre")

    final = massacre(board)
    
    for i in final.moveHistory:
        print("(%d, %d) -> (%d, %d)" % (i[0][0],i[0][1],i[1][0],i[1][1]))


        


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


