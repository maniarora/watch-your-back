from random import randint
from gamerep import Board , Piece
from operator import itemgetter
import copy

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

            else:
                #Move opponents piece on board
          
                piece =  self.board.find_piece(action[0])
                piece.makemove(action[1])
                
                self.board = piece.board
                
                if piece.player == "@":
                    self.board.black_pieces.append(piece)
                else:
                    self.board.white_pieces.append(piece)
                    
                for i in self.board.white_pieces + self.board.black_pieces:
                    i.board = self.board
                

        return





    def action(self, turns):

        # For placing phase
        if self.phase == 'placing':
            action =  self.placePiece()
        
            if (turns == 23 and self.colour == "black") or (turns == 22 and self.colour == "white") :
                self.phase = 'moving'
            
            return action
                
        elif self.phase == 'moving':
            
            print(self.board,"\n")
            lst = self.expand_board()
            

            best_move = min(lst,key=itemgetter(1))[2]
            
            self.update(best_move)
#             for i in self.board.white_pieces + self.board.black_pieces:
#                 i.board = self.board
#                 
            return best_move
            


            
             
                                  
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
        
        
    def expand_board(self):
        
        player = "O" if self.colour == "white" else "@"
        possible_moves = []
        if player == "O":
            for i in self.board.white_pieces:
                if i.alive:
                    oldpos = i.pos
                    for j in i.moves():
                        eliminated_pieces = i.makemove(j)
                        possible_moves.append((i.board, self.get_utility(i.board) , (oldpos , i.pos)))
                        i.undomove(oldpos, eliminated_pieces)
                        
        if player == "@":
            for i in self.board.black_pieces:
                if i.alive:
                    oldpos = i.pos
                    for j in i.moves():
                        eliminated_pieces = i.makemove(j)
                        possible_moves.append((i.board, self.get_utility(i.board) , (oldpos , i.pos) ))
                        i.undomove(oldpos, eliminated_pieces)
                        
        return possible_moves
                        

    def is_terminal(self, node):
        assert node is not None
        
        return len([x for x in self.board.black_pieces + self.board.white_pieces if x.alive])


    def get_utility(self, board):
        player = "O" if self.colour == "white" else "@"
        
        sum = 0
        if player == "O":
            for i in board.white_pieces:
                if i.alive:
                    for j in board.black_pieces:
                        sum += self.manhattan_distance(i.pos,j.pos)
        else:
            for i in board.black_pieces:
                if i.alive:
                    for j in board.white_pieces:
                        sum += self.manhattan_distance(i.pos, j.pos)
        return sum


    # Helper function for utility function
    def manhattan_distance(self,start, end):
        sx, sy = start
        ex, ey = end
        return abs(ex - sx) + abs(ey - sy)
