import copy

BLOCKED = 'X'
EMPTY   = '-'
BLACK   = '@'
WHITE   = 'O'


class Board:
    WIDTH = 8
    HEIGHT = 8

    # Initializing the board
    def __init__(self):

        # 2D array to store the board configuration
        self.board = [[0 for x in range(Board.WIDTH)]
                      for y in range(Board.HEIGHT)]

        # Store history of moves required for massacre
        self.move_history = []

    # Reading in the board from stdin
    def populate_board_from_input(self):

        for i in range(Board.HEIGHT):
            self.board[i] = input().split()

    # Carry out a move, from old_coordinate to new_coordinate
    def make_move(self, old_coord, new_coord):

        # Adjust symbols for the coordinates accordingly
        self.board[old_coord[0]][old_coord[1]] = EMPTY
        self.board[new_coord[0]][new_coord[1]] = WHITE

        # Record the move
        self.move_history.append((old_coord, new_coord))

    # Checks if a piece is sandwiched, if yes, its killed directly
    def is_killed(self, color):


        # Checking and storing player, opponent symbols
        if color == 'black':
            player      = '@'
            opponent    = 'O'
        elif color == 'white':
            player      = 'O'
            opponent    = '@'

        for coord in self.get_location(color):
            row = coord[0]
            col = coord[1]

            hostile = opponent + BLOCKED

            # Check if piece is sanwiched horizontally
            # Sanity checking to avoid indexing errors
            if row > 0 and row < Board.WIDTH - 1:
                if self.board[row + 1][col] in hostile \
                        and self.board[row - 1][col] in hostile:
                    # Piece is killed
                    self.board[row][col] = EMPTY

            # Check if piece is sanwiched vertically
            # Sanity checking to avoid indexing errors
            if col > 0 and col < Board.HEIGHT - 1:
                if self.board[row][col + 1] in hostile \
                        and self.board[row][col - 1] in hostile:
                    # Piece is killed
                    self.board[row][col] = EMPTY

    # Gets a list of the locations of all the 'color'-ed pieces
    def get_location(self, color):
        result = []

        if (color == 'white'):
            player = 'O'
        elif (color == 'black'):
            player = '@'

        for i in range(Board.HEIGHT):
            for j in range(Board.WIDTH):
                if (self.board[i][j] == player):
                    result.append([i, j])

        return result

    def expand_board(self):

        moves = []

        for i in self.get_location("white"):
            row = i[0]
            col = i[1]

            moves = moves + self.valid_moves([row, col], "white")

        return moves

    # Given a piece and its coordinate,
    # checks all the valid moves it can take in the board
    def valid_moves(self, coord, color):

        if color == 'white':
            player = 'O'
            opponent = "@"
        else:
            player - "@"
            opponent - "O"

        moves = []

        row = coord[0]
        col = coord[1]

        # LEFT MOVEMENTS
        if col > 0 and self.board[row][col - 1] != BLOCKED:

            if self.board[row][col - 1] == EMPTY:
                moves.append([[row, col], [row, col - 1]])

            elif self.board[row][col - 1] == opponent \
                    or self.board[row][col - 1] == player:

                if col > 1 and self.board[row][col - 2] == EMPTY:
                    moves.append([[row, col], [row, col - 2]])

        # RIGHT MOVEMENTS
        if col < Board.WIDTH - 1 and self.board[row][col + 1] != BLOCKED:

            if self.board[row][col + 1] == EMPTY:
                moves.append([[row, col], [row, col + 1]])

            elif self.board[row][col + 1] == opponent \
                    or self.board[row][col + 1] == player:

                if col < Board.WIDTH - 2 \
                        and self.board[row][col + 2] == EMPTY:
                    moves.append([[row, col], [row, col + 2]])

        # UP MOVEMENTS
        if row > 0 and self.board[row - 1][col] != BLOCKED:

            if self.board[row - 1][col] == EMPTY:
                moves.append([[row, col], [row - 1, col]])

            elif self.board[row - 1][col] == opponent \
                    or self.board[row - 1][col] == player:

                if row > 1 and self.board[row - 2][col] == EMPTY:
                    moves.append([[row, col], [row - 2, col]])

        # DOWN MOVEMENTS
        if row < Board.HEIGHT - 1 and self.board[row + 1][col] != BLOCKED:

            if self.board[row + 1][col] == EMPTY:
                moves.append([[row, col], [row + 1, col]])

            elif self.board[row + 1][col] == opponent \
                    or self.board[row + 1][col] == player:

                if row < Board.HEIGHT - 2 \
                        and self.board[row + 2][col] == EMPTY:
                    moves.append([[row, col], [row + 2, col]])

        return moves

    # To check if the massacre has finished,
    # i.e. all black pieces have been eliminated
    def goal_test(self):
        if len(self.get_location("black")) == 0:
            return True
        else:
            return False

    # Eliminate all opponents pieces
    def massacre(initial):

        # Store a list of possible board configurations
        states = []

        states.append(initial)

        for board in states:

            actions = board.expand_board()

            for i in actions:

                state = copy.deepcopy(board)
                state.make_move(i[0], i[1])

                state.is_killed("black")
                state.is_killed("white")

                # Check if all opponent pieces have been eliminated
                if state.goal_test():
                    return state
                else:
                    states.append(state)
