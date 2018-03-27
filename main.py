from board import Board
import math
import aima 

board = Board()

board.popoulateBoardFromInput()

# Changeable values
boardWidth = 8
boardHeight = 8
 
def moves(board, color):
    moves_count = 0
    empty = '-'
    blocked = 'X'

    # Determining the color of the player
    if color == 'white':
        player = 'O'
        opponent = '@'
    else:
        player = '@'
        opponent = 'O'

    for i in range(boardHeight):
        for j in range(boardWidth):

            if board.board[i][j] == player:

                # Row comparisons

                # Checking for possible left movements
                if j > 0 and board.board[i][j-1] != blocked:
                    if board.board[i][j-1] == empty:
                        moves_count += 1
                    elif board.board[i][j-1] == opponent or board.board[i][j-1] == player:
                        if j > 1 and board.board[i][j-2] == empty:
                                moves_count += 1

                # Checking for possible right movements
                if j < Board.WIDTH-1 and board.board[i][j+1] != blocked:
                    if board.board[i][j+1] == empty:
                        moves_count += 1
                    elif board.board[i][j+1] == opponent or board.board[i][j+1] == player:
                        if j < Board.WIDTH-2 and board.board[i][j+2] == empty:
                                moves_count += 1

                # Column comparisons

                # Checking for possible upwards movements
                if i > 0 and board.board[i-1][j] != blocked:
                    if board.board[i-1][j] == empty:
                        moves_count += 1
                    elif board.board[i-1][j] == opponent or board.board[i-1][j] == player:
                        if i > 1 and board.board[i-2][j] == empty:
                                moves_count += 1

                # Checking for possible downwards movements
                if i < Board.HEIGHT-1 and board.board[i+1][j] != blocked:
                    if board.board[i+1][j] == empty:
                        moves_count += 1
                    elif board.board[i+1][j] == opponent or board.board[i+1][j] == player:
                        if i < Board.HEIGHT-2 and board.board[i+2][j] == empty:
                                moves_count += 1
    return moves_count

def massacre(board):
    player = 'O'
    opponent = '@'
    empty = '-'
    blocked = 'X'
    whiteLoc = board.getLoc("white")
    
    moves= []
            
    for i in board.getLoc('black'):
        col = i[0]
        row = i[1]
        
        up = False
        down = False
        left = False
        right = False
        
        if (board.board[row-1][col] in (player+blocked)) and row > 0:
            up = True
        if (board.board[row+1][col] in (player+blocked)) and row < 7:
            down = True
        if (board.board[row][col+1] in (player+blocked)) and col < 7:
            right = True
        if (board.board[row][col-1] in (player+blocked)) and col > 0:
            left = True
        
        while(not(up and down) or not(left and right)):
            for j in whiteLoc:
                if next(j,i):
                    continue
                
                
            

def next(p1, p2):
    if abs(p1[0] - p2[0]) == 1 or abs(p1[1] -p2[0]) == 1:
        return True
    else:
        return False

print(moves(board, 'white'))
print(moves(board, 'black'))
# X O O O O O O X
# - @ - - - - - -
# - @ - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - @
# X - - - - - - X


#X - - - - - - X
#- - - - - - - -
#- - - - - O - -
#- - - - @ O - -
#- - - - - - O -
#- - - - - O @ -
#- - - - - - - @
#X - - - - - - X