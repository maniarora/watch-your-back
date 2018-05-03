from random import randint


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


        if action == None :
            return
        else:
            if isinstance(action[0], int):
                # Place opponent piece on board
                self.board[action[1]][action[0]] = self.getOpponent()

            # else:
                #Move opponents piece on board

        return





    def action(self, turns):
        
        if self.phase == 'placing':
            if (turns == 24 and self.colour == "black") or (turns == 23 and self.colour == "white") :
                self.phase = 'moving'
            
        
        
        
        # For placing phase
        if self.phase == 'placing':
            pos = self.placePiece()

            return (pos[1],pos[0])
        

        # elif self.phase == 'moving':
            #insert moving algorithm
        

        
 
        

    def checkBestFree(self,pos):
        y = pos[0]
        x = pos[1]
        
        player = self.board[y][x]
        empty = "-"
        blocked = "X"
        opponent = "@" if player == "O" else "O"
        threshold = range(0,5) if opponent == "O" else range(2,7)
        
        
        #Case where pos is at the side edges of the board.
        if x == 0 and self.board[y][x+1] == empty:
            return (y,x+1)
        elif x == 7 and self.board[y][x-1] == empty:
            return (y, x-1) 
        
        
        # Case where pos is at the top and bottom edges of the board.
        if y == 0:
            if self.board[y+1][x] == empty and y+1 in threshold:
                return (y+1,x)
            elif self.board[y][x-1] == empty:
                return (y,x- 1)
            elif self.board[y][x+1] == empty:
                return (y,x+1)
        elif y == 7:
            if self.board[y-1][x] == empty and y-1 in threshold:
                return (y+1,x)
            elif self.board[y][x-1] == empty:
                return (y,x- 1)
            elif self.board[y][x+1] == empty:
                return (y,x+1)
                
        
        # If above is taken and bottom is free
        if self.board[y-1][x] == opponent and self.board[y+1][x] == empty and y+1 in threshold:
            return(y+1,x)
        # If left is taken and right is free
        elif self.board[y][x-1] == empty:
            return(y,x- 1)
        
        # Places them left or above as preference:
        if self.board[y-1][x] == empty and y-1 in thresholds:
            return(y-1,x)
        elif self.board[y][x-1] == empty:
            return(y,x-1)
        #No need to put right or down because by default is always going to be
        #a piece at either left or up.
            
    
    def placePiece(self):
        # Check whether an opponent piece is on the board, and places a piece
        # next to that piece
        
        empty = "-"
        blocked = "X"
        opponent = self.getOpponent()
        player = "O" if opponent == "@" else "@"
            
            
        if self.colour == "white":
            for i in range(7):
                for j in range(8):
                    if self.board[i][j] == opponent:
                        free_pos = self.checkBestFree((i,j))
                        if free_pos != None:
                            self.board[free_pos[0]][free_pos[1]] = player
                            if self.isSurrounded(i,j):
                                self.board[i][j] = empty
                            return free_pos
                        else:
                            continue
            return (randint(0,7), randint(0,6))
                        
        elif self.colour == "black":
            for i in range(7,1,-1):
                for j in range(8):
                    if self.board[i][j] == opponent:
                        free_pos = self.checkBestFree((i,j))
                        if free_pos != None:
                            self.board[free_pos[0]][free_pos[1]] = player
                            if self.isSurrounded(i,j):
                                self.board[i][j] = empty
                            return free_pos
                        else:
                            continue
            return (randint(0,7),randint(2,7))
                        
    def getOpponent(self):
        
        #Check whether a player piece is surrounded by its enemies.
        if self.colour == "white":
            player = "O"
            opponent = "@"
        else:
            player = "@"
            opponent = "O"
        return opponent
    
    # Check whether the  piece of (x,y) is surrounded by opponent pieces
    def isSurrounded(self,y,x):
        
        player = self.board[y][x]
        blocked = "X"
        if player == '@':
            opponent = 'O'
        else:
            opponent = '@'
            
        
        if x == 0 or x == 7:
            return False
        
            
        
        if y == 0 or y == 7:
            if(self.board[y][x+1] == opponent or self.board[y-1][x] == blocked) and (self.board[y][x-1] == opponent or self.board[y][x-1] == blocked):
                return True
            else:
                return False
            
            
        
        #Case where it's not on any edge
        if (self.board[y-1][x] == opponent or self.board[y-1][x] == blocked) and (self.board[y+1][x] == opponent or self.board[y+1][x] == blocked):
            return True
        elif (self.board[y][x+1] == opponent or self.board[y-1][x] == blocked) and (self.board[y][x-1] == opponent or self.board[y][x-1] == blocked):
            return True
        else:
            return False
    
        