'''
Subject     : COMP30024
Project     : Watch Your Back (Part B)
Authors     : Manindra Arora    (827703)
            : Weng Kin Lee      (822386)
Last Edited : 11th May 2018
'''


from random import randint
from game_representation import Board , Piece
from operator import itemgetter
import copy


# Helper function to get the utility value
def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


class Player:
    def __init__(self, colour):
        self.colour = colour
        
         # board configuration (takes from game itself)
        self.board = Board()
        
        # setting initial phase of placing pieces
        self.phase = "placing"

    def get_symbol(self, player_type):
        """
        Helper function to obtain the required player's symbolic representation
        """
        if self.colour == "white":
            player = "O"
            opponent = "@"
        else:
            player = "@"
            opponent = "O"
        return player if player_type == 'player' else opponent

    # Helper function to synchronize board states
    def sync_boards(self):
        for i in self.board.white_pieces + self.board.black_pieces:
            i.board = self.board

    def update(self, action):

        if action == None :
            return
        else:
            # Check if a piece is placed
            if isinstance(action[0], int):

                # Place opponent piece on board
                self.board.grid[action] = self.get_symbol('opponent')
                
                piece = Piece(self.get_symbol('opponent'), action , self.board)
                piece.makemove(action)

                # Synchronize both boards
                self.board = piece.board

                # Update the list representation of the opponents pieces inside board.
                if self.colour == "white":
                    self.board.black_pieces.append(piece)
                elif self.colour == "black":
                    self.board.white_pieces.append(piece)

            # Update piece movements
            else:
                piece =  self.board.find_piece(action[0])
                piece.makemove(action[1])
                
                self.board = piece.board
                
                if piece.player == "@":
                    self.board.black_pieces.append(piece)
                else:
                    self.board.white_pieces.append(piece)

                self.sync_boards()
        return


    def action(self, turns):

        # For placing phase
        if self.phase == 'placing':
            action =  self.placePiece()

            # Check if each player has placed 12 pieces, if yes switch to moving phase
            if (turns == 23 and self.colour == "black") or (turns == 22 and self.colour == "white") :
                self.phase = 'moving'
            
            return action
                
        elif self.phase == 'moving':

            print(self.board,"\n")

            lst = self.expand_board()
            
            if (turns == 127 and self.colour == "black") or (turns == 126 and self.colour == "white") :
                self.board.shrink_board()

            # Get the action with the minimum utility value
            best_move = min(lst,key=itemgetter(1))[2]
            
            self.update(best_move)

            return best_move


    
    def placePiece(self):
        """
        Does the actual placing of the pieces. Will either place randomly
        or place next to the enemy in a position where it doesn't get 
        eliminated.
        
        """

        # Initialising constants to use throughtout the process.
        player      = self.get_symbol('player')
        opponent    = self.get_symbol('opponent')

        # y_threshold here refers to the range of y values for each player in the
        # starting phase
        y_threshold = {"white" : (0,5) , "black" : (2,7)}
        threshold = y_threshold[self.colour]
        
        
        #Assigns enemy list
        if player == "O":
            enemy = self.board.black_pieces
        else:
            enemy = self.board.white_pieces

        # If no enemy piece has been placed, randomly place piece
        if len(enemy) == 0:

            return self.place_piece_random(threshold)
   
        # If enemey pieces exist on the board, puts a piece on the left of the
        # first enemy piece by default
        else:
             
            return self.place_piece_enemy(threshold, enemy)

                         
    def place_piece_random(self, threshold):
        """
        Places a piece randomly on the board based on a given y axis threshold
        
        """
        square = (randint(0,7), randint(threshold[0],threshold[1]))
        corners = self.board.corner_pieces

        # Initialising constants to use throughtout the process.
        player      = self.get_symbol('player')
        opponent    = self.get_symbol('opponent')
        
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

        self.sync_boards()
        
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

        # Initialising constants to use throughtout the process.
        player      = self.get_symbol('player')
        opponent    = self.get_symbol('opponent')
        
        free_space = None
        for i in enemy:

            if not i.alive:
                continue

            free_spaces = i.surrounded()

            # Checks which free space is valid
            for space in free_spaces:

                # Ensure placement of piece is within its own defined starting area.
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
                self.sync_boards()
                # Assigns the placed piece in the piece list.
                if player == "O":
                    self.board.white_pieces.append(piece)
                elif player == "@":
                    self.board.black_pieces.append(piece)
                
                return free_space
            
        if free_space == None:
            return self.place_piece_random(threshold)
        
        
    def expand_board(self):
        
        player = self.get_symbol('player')
        possible_moves = []
        if player == "O":
            for i in self.board.white_pieces:
                if i.alive:
                    oldpos = i.pos
                    for j in i.moves():
                        eliminated_pieces = i.makemove(j)
                        utility = self.get_utility(i.board)
                        if i in eliminated_pieces:
                            utility += 200
                        possible_moves.append((i.board, utility , (oldpos , i.pos) ))
                        i.undomove(oldpos, eliminated_pieces)
                        
        if player == "@":
            for i in self.board.black_pieces:
                if i.alive:
                    oldpos = i.pos
                    for j in i.moves():
                        eliminated_pieces = i.makemove(j)
                        utility = self.get_utility(i.board)
                        if i in eliminated_pieces:
                            utility += 200
                        possible_moves.append((i.board, utility , (oldpos , i.pos) ))
                        i.undomove(oldpos, eliminated_pieces)
                        
        return possible_moves
                        

    def is_terminal(self, node):
        assert node is not None
        
        return len([x for x in self.board.black_pieces + self.board.white_pieces if x.alive])

    def get_utility(self, board):
        """
        Utility function for the algorithm
        Applies manhattan distance from each piece to all opponents piece, and also corner pieces
        and returns the sum
        """
        player = self.get_symbol('player')
        
        sum = 0

        if player == "O":

            for i in board.white_pieces:
                if i.alive:
                    for j in board.black_pieces:
                        sum += manhattan_distance(i.pos,j.pos)

                    # Checks if final shrink has occured. If not, take corners into consideration
                    if(board.n_shrinks < 2):
                        for k in board.corner_pieces:
                            sum += manhattan_distance(i.pos, k)

        else:
            for i in board.black_pieces:
                if i.alive:
                    for j in board.white_pieces:
                        sum += manhattan_distance(i.pos, j.pos)

                    # Checks if final shrink has occured. If not, take corners into consideration
                    if (board.n_shrinks < 2):
                        for k in board.corner_pieces:
                            sum += manhattan_distance(i.pos, k)
        return sum

