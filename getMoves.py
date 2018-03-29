from board import Board
from BoardProblem import BoardProblem


empty = '-'
blocked = 'X'
player = 'O'
opponent = '@'

# Changeable values
boardWidth = 8
boardHeight = 8

def moves(board, color):
    moves_count = 0

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
                moves_count = checkleft(board.board, i, j, moves_count)
                moves_count = checkright(board.board, i, j, moves_count)

                # Column comparisons
                moves_count = checkupwards(board.board, i, j, moves_count)
                moves_count = checkdownwards(board.board, i, j, moves_count)

    return moves_count



def checkleft(board,i,j, moves_count):

    if j > 0 and board[i][j - 1] != blocked:
        if board[i][j - 1] == empty:
            moves_count += 1
        elif board[i][j - 1] == opponent or board[i][j - 1] == player:
            if j > 1 and board[i][j - 2] == empty:
                moves_count += 1
    return moves_count


def checkright(board,i,j,moves_count):

    if j < Board.WIDTH - 1 and board[i][j + 1] != blocked:
        if board[i][j + 1] == empty:
            moves_count += 1
        elif board[i][j + 1] == opponent or board[i][j + 1] == player:
            if j < Board.WIDTH - 2 and board[i][j + 2] == empty:
                moves_count += 1

    return moves_count


def checkupwards(board,i,j,moves_count):

    if i > 0 and board[i - 1][j] != blocked:
        if board[i - 1][j] == empty:
            moves_count += 1
        elif board[i - 1][j] == opponent or board[i - 1][j] == player:
            if i > 1 and board[i - 2][j] == empty:
                moves_count += 1

    return moves_count

def checkdownwards(board,i,j,moves_count):

    if i < Board.HEIGHT - 1 and board[i + 1][j] != blocked:
        if board[i + 1][j] == empty:
            moves_count += 1
        elif board[i + 1][j] == opponent or board[i + 1][j] == player:
            if i < Board.HEIGHT - 2 and board[i + 2][j] == empty:
                moves_count += 1

    return moves_count
