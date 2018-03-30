from board import Board

player = 'O'
opponent = '@'

BLOCKED = 'X'
EMPTY   = '-'
BLACK   = '@'
WHITE   = 'O'


def moves(board, color):
    moves_count = 0

    # Determining the color of the player
    if color == 'white':
        player      = 'O'
        opponent    = '@'
    else:
        player      = '@'
        opponent    = 'O'

    for i in range(Board.HEIGHT):
        for j in range(Board.WIDTH):

            if board.board[i][j] == player:
                # Row comparisons
                moves_count = check_left    (board.board, i, j, moves_count)
                moves_count = check_right   (board.board, i, j, moves_count)

                # Column comparisons
                moves_count = check_up      (board.board, i, j, moves_count)
                moves_count = check_down    (board.board, i, j, moves_count)

    return moves_count


def check_left(board, i, j, moves_count):

    if j > 0 and board[i][j - 1] != BLOCKED:
        # Check if adjacent piece is empty
        if board[i][j - 1] == EMPTY:
            moves_count += 1

        # Check if a jump is possible
        elif board[i][j - 1] == opponent or board[i][j - 1] == player:
            if j > 1 and board[i][j - 2] == EMPTY:
                moves_count += 1
                
    return moves_count


def check_right(board, i, j, moves_count):

    if j < Board.WIDTH - 1 and board[i][j + 1] != BLOCKED:
        # Check if adjacent piece is empty
        if board[i][j + 1] == EMPTY:
            moves_count += 1

        # Check if a jump is possible
        elif board[i][j + 1] == opponent or board[i][j + 1] == player:
            if j < Board.WIDTH - 2 and board[i][j + 2] == EMPTY:
                moves_count += 1

    return moves_count


def check_up(board, i, j, moves_count):

    if i > 0 and board[i - 1][j] != BLOCKED:
        # Check if adjacent piece is empty
        if board[i - 1][j] == EMPTY:
            moves_count += 1

        # Check if a jump is possible
        elif board[i - 1][j] == opponent or board[i - 1][j] == player:
            if i > 1 and board[i - 2][j] == EMPTY:
                moves_count += 1

    return moves_count


def check_down(board, i, j, moves_count):

    if i < Board.HEIGHT - 1 and board[i + 1][j] != BLOCKED:
        # Check if adjacent piece is empty
        if board[i + 1][j] == EMPTY:
            moves_count += 1

        # Check if a jump is possible
        elif board[i + 1][j] == opponent or board[i + 1][j] == player:
            if i < Board.HEIGHT - 2 and board[i + 2][j] == EMPTY:
                moves_count += 1

    return moves_count
