import copy

class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.board = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        self.whiteCount = 0
        self.blackCount  = 0
        self.moveHistory = []

    # Reading in the board
    def populateBoardFromInput(self):
        for i in range(Board.HEIGHT):
            self.board[row] = input().split()
            self.whiteCount += self.board[row].count('O')
            self.blackCount += self.board[row].count('@')

    def makeMove(self, oldCoord, newCoord):

        # result = copy.deepcopy(self)

        self.board[oldCoord[0]][oldCoord[1]] = "-"
        self.board[newCoord[0]][newCoord[1]] = "O"

        self.moveHistory.append((oldCoord),(newCoord))
        # print(print_board(self.board))
        # return result

    def isKilled(self, coord, color):
        # Checks if a piece is sandwiched, if yes, its killed directly

        empty = '-'
        blocked = 'X'

        if color == 'black':
            player = '@'
            opponent = 'O'
        elif color == 'white':
            player = 'O'
            opponent = '@'

        row = coord[0]
        col = coord[1]
        hostile = opponent + blocked

        if row > 0 and row < Board.WIDTH - 1:
            if self.board[row + 1][col] in hostile and self.board[row - 1][col] in hostile:
                self.board[row][col] = empty

        if col > 0 and col < Board.WIDTH - 1:
            if self.board[row][col + 1] in hostile and self.board[row][col - 1] in hostile:
                self.board[row][col] = empty







# Helper functions
def __str__(self):
    result = []
    for i in range(Board.WIDTH):
        result.append(self.board[row])
    return str(result)

# Print board in order
def print_board(self):
    for i in range(8):
        str = ""
        for j in range(8):
            str += self.board[row][col]
            str += " "
        print(str)

def getLoc(self, color):
    result = []

    if (color == 'white'):
        player = 'O'
    elif (color == 'black'):
        player = '@'

    for i in range(Board.HEIGHT):
        for j in range(Board.WIDTH):
            if (self.board[row][col] == player):
                result.append([i, j])  # Change to [col,i] later for x, y coordinate system

    return result

def expandBoard(self):
    
    for i in self.getLoc("white"):
        row = i[0]
        col = i[1]
        

def validMoves(coord,color):
    if color == 'white':
        player = 'O'
        
        moves = []
        
        row = coord[0]
        col = coord[1]
        
    #LEFT MOVEMENTS
    if col > 0 and self.board[row][col - 1] != blocked:
        if board[row][col - 1] == empty:
            moves.append([row,col-1])
        elif board[row][col - 1] == opponent or board[row][col - 1] == player:
            if col > 1 and board[row][col - 2] == empty:
                moves.append([row,col-2])
        
    #RIGHT MOVEMENTS
    if col < Board.WIDTH-1 and state.board[row][col+1] != blocked:
        if col+1 == empty:
            moves.append([row,col+1])
        elif state.board[row][col+1] == opponent or state.board[row][col+1] == player:
            if col < Board.WIDTH-2 and state.board[row][col+2] == empty:
                moves.append([row,col+2])
                
    #UP MOVEMENTS
    if row > 0 and state.board[row-1][col] != blocked:
        if state.board[row-1][col] == empty:
            moves.append([row-1,col])
        elif state.board[row-1][col] == opponent or state.board[row-1][col] == player:
            if row > 1 and state.board[row-2][col] == empty:
                moves.append([row-2,col])
                        
    #DOWN MOVEMENTS
    if row < Board.HEIGHT-1 and state.board[row+1][col] != blocked:
        if state.board[row+1][col] == empty:
            moves.append( [row + 1, col])
        elif state.board[row+1][col] == opponent or state.board[row+1][col] == player:
            if row < Board.HEIGHT-2 and state.board[row+2][col] == empty:
                moves.append([row+2,col])
    
    return moves

