from random import randint
from gamerep import Board , Piece
from pywt._thresholding import threshold

class Player:
    def __init__(self, colour):
        self.colour = colour
        
         # board configuration (takes from game itself)
        self.board = Board()
        
        # setting initial phase of placing pieces
        self.phase = "placing"

    def update(self, action):


        if action == None :
            return
        else:
            if isinstance(action[0], int):
                # Place opponent piece on board
                self.board.grid[action] = self.getOpponent()
                
                piece = Piece(self.getOpponent(), action , self.board)
                piece.makemove(action)
                
                self.board = piece.board
                
                if self.colour == "white":
                    self.board.black_pieces.append(piece)
                elif self.colour == "black":
                    self.board.white_pieces.append(piece)

            # else:
                #Move opponents piece on board

        return





    def action(self, turns):
        print(self.phase, self.colour, turns)

        # For placing phase
        if self.phase == 'placing':
            action =  self.placePiece()
        
            if (turns == 23 and self.colour == "black") or (turns == 22 and self.colour == "white") :
                self.phase = 'moving'
            
            return action
                
        elif self.phase == 'moving':
            
            
            return ((1,0),(2,0))


            
             
                                  
    def getOpponent(self):
        
        #Check whether a player piece is surrounded by its enemies.
        if self.colour == "white":
            player = "O"
            opponent = "@"
        else:
            player = "@"
            opponent = "O"
        return opponent
    
    def placePiece(self):
        """
        Does the actual placing of the pieces. Will either place randomly
        or place next to the enemy in a position where it doesn't get 
        eliminated.
        
        """
        
        # Initialising constants to use throughtout the process.
        player = "O" if self.getOpponent() == "@" else "@"
        opponent = self.getOpponent()
        ythreshold = {"white" : (0,5) , "black" : (2,7)}
        threshold = ythreshold[self.colour]
        
        
        #Assigns enemy list
        if player == "O":
            enemy = self.board.black_pieces
        else:
            enemy = self.board.white_pieces
         
        # Commented out code is placing next to enemy wherever possible
        # One player will have disadvantage if both use the same strategy
        # If no enemy, randomly place piece   
        if len(enemy) == 0:
             
            return self.place_piece_random(threshold)
   
        # If there is pieces, puts a piece on the left of the first enemy piece
        # by default
        else:
             
            return self.place_piece_enemy(threshold, enemy)

                         
    def place_piece_random(self, threshold):
        """
        Places a piece randomly on the board based on a given y axis threshold
        
        """
        square = (randint(0,7), randint(threshold[0],threshold[1]))
        corners = [(0,0), (0,7),(7,0),(7,7)]
        player = "O" if self.getOpponent() == "@" else "@"
        
        # Checks if square is assigned to a corner
        while square in corners:
            square = (randint(0,7), randint(threshold[0],threshold[1]))
        
        # Checks if the square is already occupied by another piece.
        while self.board.grid[square] != "-":
               square = (randint(0,7), randint(threshold[0],threshold[1]))
        # Puts the piece in the player's board
        self.board.grid[square] = player
        
        # Creates piece from square and adds itself to list of pieces
        piece = Piece(player, square, self.board )
        piece.makemove(square)
        self.board = piece.board
        
        for i in self.board.white_pieces + self.board.black_pieces:
            i.board = self.board
        
        if player == "O":
            self.board.white_pieces.append(piece)
        elif player == "@":
            self.board.black_pieces.append(piece)
        
        # Return the action
        return square
    
    def place_piece_enemy(self, threshold, enemy):
        """ 
        Places a piece on the free spot of any existing enemy piece.
        
        """
        
        player = "O" if self.getOpponent() == "@" else "@"
        
        free_space = None
        for i in enemy:
            
            if not i.alive:
                continue
            
            free_spaces = i.surrounded()
            
            # Checks which free space is valid
            for space in free_spaces:
                if space[1] in range(threshold[0],threshold[1]):
                    free_space = space
                    
                    # Places the piece in the free space
                    self.board.grid[free_space] = player
                    piece = Piece(player, free_space, self.board)
                    eliminated_pieces = piece.makemove(free_space)
                    
                    # Checks that if free_space causes the placed piece
                    # to be eliminated, roll back the move and place it 
                    # elsewhere.
                    if piece in eliminated_pieces:
                        piece.undomove(free_space, eliminated_pieces)
                        self.board.grid[free_space] = "-"
                    else:
                        break
                # Default is having no free_space.
                else:
                    free_space = None         
  
            if free_space == None:
                continue
            
            else:
                # Syncs up all the boards of each piece
                for i in self.board.white_pieces + self.board.black_pieces:
                    i.board = self.board
                # Assigns the placed piece in the piece list.
                if player == "O":
                    self.board.white_pieces.append(piece)
                elif player == "@":
                    self.board.black_pieces.append(piece)
                
                return free_space
            
        if free_space == None:
            return self.place_piece_random(threshold)


    def __init__(self):
        self.root = root

    def minimax(self,node):



    def min_value(self, node):
        if self.is_terminal(node):
            return self.get_utility(node)

        infinity = float('inf')
        min_value = infinity

        successor_states = self.getSuccessors(node)
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
        return min_value


    def max_value(self, node):
        if self.is_terminal(node):
            return self.get_utility(node)

        infinity = float('inf')
        max_value = -infinity

        successors_states = self.getSuccessors(node)
        for state in successors_states:
            max_value = max(max_value, self.min_value(state))
        return max_value

    def is_terminal(self, node):
        assert node is not None
        return ((len(self.board.black_pieces) < 2) and (len(self.board.white_pieces) < 2) ) or \
                   ((len(self.board.black_pieces) < 2) or (len(self.board.white_pieces) < 2))



    def get_utility(self):
        player = "O" if self.colour == "white" else "@"

        if player == "O":
            for i in self.board.white_pieces:
                for j in self.board.black_pieces:
                    sum += manhattan_distance(i.pos,j.pos)
       else:
            for i in self.board.black_pieces:
                for j in self.board.white_pieces:
                    sum += manhattan_distance(i.pos, j.pos)
        return sum


    # Helper function for utility function
    def manhattan_distance(start, end):
        sx, sy = start
        ex, ey = end
        return abs(ex - sx) + abs(ey - sy)
