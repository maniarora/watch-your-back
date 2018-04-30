
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
        
    def action(self, turns):
        
        if self.phase == 'placing':
            if (self.turns == 24 and self.colour == "black") or (self.turns == 23 and self.colour == "white") :
                self.phase = 'moving'
        
        
        self.board = board

