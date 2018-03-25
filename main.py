from board import Board

board = Board()

board.popoulateBoardFromInput()

# Changeable values
boardWidth = 8
boardHeight = 8

print(board)

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