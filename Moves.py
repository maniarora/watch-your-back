# Changeable values
boardWidth = 8
boardHeight = 8

# Initializing board
w, h = boardWidth, boardHeight;
board = [[0 for x in range(w)] for y in range(h)]
whiteCount = 0
blackCount = 0

# Reading in board and counting pieces for each color.
for i in range(boardHeight):
    board[i] = input().split()
    whiteCount += board[i].count('O')
    blackCount += board[i].count('@')


def moves(board, color):
    movesCount = 0
    empty = '-'
    blocked = 'X'
    if color == 'white':
        player = 'O'
        opponent = '@'
    else:
        player = '@'
        opponent = 'O'
    for i in range(boardHeight):
        for j in range(boardWidth):

            if board[i][j] == player:

                # Row comparisons

                # Checking for possible left movements
                if j > 0 and board[i][j-1] != blocked:
                    if board[i][j-1] == empty:
                        movesCount += 1
                    elif board[i][j-1] == opponent or board[i][j-1] == player:
                        if j > 1:
                            if board[i][j-2] == empty:
                                movesCount += 1

                # Checking for possible right movements
                if j < boardWidth-1 and board[i][j+1] != blocked:
                    if board[i][j+1] == empty:
                        movesCount += 1
                    elif board[i][j+1] == opponent or board[i][j+1] == player:
                        if j < boardWidth-2:
                            if board[i][j+2] == empty:
                                movesCount += 1

                # Column comparisons

                # Checking for possible upwards movements
                if i > 0 and board[i-1][j] != blocked:
                    if board[i-1][j] == empty:
                        movesCount += 1
                    elif board[i-1][j] == opponent or board[i-1][j] == player:
                        if i > 1:
                            if board[i-2][j] == empty:
                                movesCount += 1

                # Checking for possible downwards movements
                if i < boardHeight-1 and board[i+1][j] != blocked:
                    if board[i+1][j] == empty:
                        movesCount += 1
                    elif board[i+1][j] == opponent or board[i+1][j] == player:
                        if i < boardHeight-2:
                            if board[i+2][j] == empty:
                                movesCount += 1
    return movesCount





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