
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
        
    
    def update(self, move):
        self.player.update(move)
        
    def action(self, turns):
        
        action = self.player.action(turns)
        
        return action
