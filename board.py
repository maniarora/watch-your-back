import copy

class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.board = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        self.moveHistory = []

    # Reading in the board
    def populateBoardFromInput(self):
        for i in range(Board.HEIGHT):
            self.board[i] = input().split()

    def makeMove(self, oldCoord, newCoord):

        # result = copy.deepcopy(self)

        self.board[oldCoord[0]][oldCoord[1]] = "-"
        self.board[newCoord[0]][newCoord[1]] = "O"
        
        self.moveHistory.append((oldCoord,newCoord))
        # print(print_board(self.board))
        # return result

    def isKilled(self, color):
        # Checks if a piece is sandwiched, if yes, its killed directly

        empty = '-'
        blocked = 'X'

        if color == 'black':
            player = '@'
            opponent = 'O'
        elif color == 'white':
            player = 'O'
            opponent = '@'
            
        for coord in self.getLoc(color):
            row = coord[0]
            col = coord[1]
            hostile = opponent + blocked
    
            if row > 0 and row < Board.WIDTH - 1:
                if self.board[row + 1][col] in hostile and self.board[row - 1][col] in hostile:
                    self.board[row][col] = empty
    
            if col > 0 and col < Board.WIDTH - 1:
                if self.board[row][col + 1] in hostile and self.board[row][col - 1] in hostile:
                    self.board[row][col] = empty
    
    def getLoc(self, color):
        result = []
    
        if (color == 'white'):
            player = 'O'
        elif (color == 'black'):
            player = '@'
    
        for i in range(Board.HEIGHT):
            for j in range(Board.WIDTH):
                if (self.board[i][j] == player):
                    result.append([i, j])  # Change to [j,i] later for x, y coordinate system
    
        return result

    def expandBoard(self):
        
        moves = []
        
        for i in self.getLoc("white"):
            row = i[0]
            col = i[1]
            
            moves = moves + self.validMoves([row,col],"white")
        
        return moves
            
            
    
    def validMoves(self,coord,color):
        
        blocked = "X"
        empty = "-"
        
        if color == 'white':
            player = 'O'
            opponent = "@"
        else:
            player - "@"
            opponent - "O"
            
        moves = []
        
        row = coord[0]
        col = coord[1]
        
        #LEFT MOVEMENTS
        if col > 0 and self.board[row][col - 1] != blocked:
            if self.board[row][col - 1] == empty:
                moves.append([[row,col],[row,col-1]])
            elif self.board[row][col - 1] == opponent or self.board[row][col - 1] == player:
                if col > 1 and self.board[row][col - 2] == empty:
                    moves.append([[row,col],[row,col-2]])
            
        #RIGHT MOVEMENTS
        if col < Board.WIDTH-1 and self.board[row][col+1] != blocked:
            if self.board[row][col+1] == empty:
                moves.append([[row,col],[row,col+1]])
            elif self.board[row][col+1] == opponent or self.board[row][col+1] == player:
                if col < Board.WIDTH-2 and self.board[row][col+2] == empty:
                    moves.append([[row,col],[row,col+2]])
                    
        #UP MOVEMENTS
        if row > 0 and self.board[row-1][col] != blocked:
            if self.board[row-1][col] == empty:
                moves.append([[row,col],[row-1,col]])
            elif self.board[row-1][col] == opponent or self.board[row-1][col] == player:
                if row > 1 and self.board[row-2][col] == empty:
                    moves.append([[row,col],[row-2,col]])
                            
        #DOWN MOVEMENTS
        if row < Board.HEIGHT-1 and self.board[row+1][col] != blocked:
            if self.board[row+1][col] == empty:
                moves.append([[row,col], [row + 1, col]])
            elif self.board[row+1][col] == opponent or self.board[row+1][col] == player:
                if row < Board.HEIGHT-2 and self.board[row+2][col] == empty:
                    moves.append([[row,col],[row+2,col]])
        
        return moves

    def goal_test(self):
        print(len(self.getLoc("black")))
        if len(self.getLoc("black")) == 0 :
            return True
        else:
            return False
    
    # Print board in order
    def print_board(self):
        for i in range(8):
            str = ""
            for j in range(8):
                str += self.board[i][j]
                str += " "
            print(str)