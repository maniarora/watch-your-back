class Board:
    WIDTH = 8
    HEIGHT = 8
    def __init__(self):
        self.board = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        self.whiteCount = 0
        self.blackCount  = 0
        
    def popoulateBoardFromInput(self):
        for i in range(Board.HEIGHT):
            self.board[i] = input().split()
            self.whiteCount += self.board[i].count('O')
            self.blackCount += self.board[i].count('@')

    
    
    
    def __str__(self):
        result = []
        for i in range(Board.WIDTH):
            result.append(self.board[i])
        return str(result)
    
    def getLoc(self, color):
        
        result = []
        
        if(color == 'white'):
            player = 'O'
        elif(color == 'black'):
            player = '@'
        
        for i in range (Board.HEIGHT):
            for j in range (Board.WIDTH):
                if(self.board[i][j] == player):
                    result.append([i,j])
        return result