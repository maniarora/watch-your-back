import copy

class Board:
    WIDTH = 8
    HEIGHT = 8
    def __init__(self):
        self.board = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        self.whiteCount = 0
        self.blackCount  = 0

    # Reading in the board
    def populateBoardFromInput(self):
        for i in range(Board.HEIGHT):
            self.board[i] = input().split()
            self.whiteCount += self.board[i].count('O')
            self.blackCount += self.board[i].count('@')

    def __str__(self):
        result = []
        for i in range(Board.WIDTH):
            result.append(self.board[i])
        return str(result)

    # Print board in order
    def print_board(self):
        for i in range(8):
            str = ""
            for j in range(8):
                str += self.board[i][j]
                str += " "
            print(str)

    # Gets all x, y locations for the white player in the board
    def getLoc(self, color):
        
        result = []
        goalState = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]

        if(color == 'white'):
            player = 'O'
        elif(color == 'black'):
            player = '@'
        
        for i in range (Board.HEIGHT):
            for j in range (Board.WIDTH):
                goalState[i][j] = self.board[i][j]
                if(self.board[i][j] == player):
                    result.append([i,j])            # Change to [j,i] later for x, y coordinate system


        return result
    
    def makeMove(self, oldCoord, newCoord):
        
        result = copy.deepcopy(self)
        
        
        print(print_board(self.board))
        return result
    
    def isKilled(self, coord,color):
        
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
        hostile = opponent+blocked
        
        if self.board[row+1][col] in hostile and self.board[row-1][col] in hostile and row <Board.WIDTH-1 and row > 0 :
            self.board[row][col] = empty
        if self.board[row][col+1] in hostile and self.board[row][col-1] in hostile and col < Board.WIDTH-1  and col >0:
            self.board[row][col] = empty
        
            
            