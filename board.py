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
        
        result = copy.deepcopy(self.board)
        
        
        result[oldCoord[0]][oldCoord[1]] = "-"
        result[newCoord[0]][newCoord[1]] = "O"
        
        return result

