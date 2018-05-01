
class Player:
    """Wrapper for a Player class to simplify initialization"""
    def __init__(self, colour, board):
        self.colour = colour
        
         # board configuration (takes from game itself)
        self.board = board
        
        # setting initial phase of placing pieces
        self.phase = "placing"
        
    #Used to update the board after every turn 
    def syncBoard(self,board):
        self.board = board
        
    
    def update(self, action):
        
        
        self.player.update(move)
        
    def action(self, turns, board):
        
        if self.phase == 'placing':
            if (self.turns == 24 and self.colour == "black") or (self.turns == 23 and self.colour == "white") :
                self.phase = 'moving'
        
        self.board = board
        
        
        # For placing phase
        if self.phase == 'placing':
            pos = placePiece()
            return (pos[1],pos[0])
        
        elif self.phase == 'moving':
            #insert moving algorithm
        

        
 
        
        
    def checkFirstFree(pos):
        y = pos[0]
        x = pos[1]
        if self.board[y-1][x] == empty:
            return(y-1,x)
        elif self.board[y+1][x] == empty:
            return(y+1,x)    
        elif self.board[y][x+1] == empty:
            return(y,x+1)
        elif self.board[y][x-1] == empty:
            return(y,x- 1)
        else:
            return None
    
    def placePiece():
        # Check whether an opponent piece is on the board, and places a piece
        # next to that piece
        
        empty = "-"
        blocked = "x"
        if self.colour == "white":
            player = "O"
            opponent = "@"
        else:
            player = "@"
            opponent = "O"
            
            
        if self.colour == "white":
            for i in range(7):
                for j in range(8):
                    if self.board[i][j] == opponent:
                        free_pos = checkFirstFree((i,j))
                        if free_pos != None:
                            self.board[free_pos[0]][free_pos[1]] = player
                            return free_pos
                        else:
                            continue
            return None
                        
        elif self.colour == "black":
            for i in range(7,1,-1):
                for j in range(8):
                    if self.board[i][j] == opponent:
                        free_pos = checkFirstFree((i,j))
                        if free_pos != None:
                            self.board[free_pos[0]][free_pos[1]] = player
                            return free_pos
                        else:
                            continue
            return None
                        
        