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
        :param player_type: To check whether the player or opponent is referenced.
        :return: The symbol of the player, according to the player_type
        """
        if self.colour == "white":
            player      = "O"
            opponent    = "@"
        else:
            player      = "@"
            opponent    = "O"
        return player if player_type == 'player' else opponent

    def sync_boards(self):
        """
        Helper function to synchronize board states
        """
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
        """
        Given the number of turns that have occured, returns the action accordingly
        :param turns: number of turns passed
        :return: action specific to the current phase (placement or moving)
        """

        # For placing phase
        if self.phase == 'placing':
            action =  self.placePiece()

            # Check if each player has placed 12 pieces, if yes switch to moving phase
            if (turns == 23 and self.colour == "black") or (turns == 22 and self.colour == "white") :
                self.phase = 'moving'
            
            return action
                
        elif self.phase == 'moving':
            
            if (turns == 127 and self.colour == "black") or (turns == 126 and self.colour == "white") :
                self.board.shrink_board()
                
        
            possible_moves = self.expand_board()
            
            # Get the action with the minimum utility value
            best_move = min(possible_moves,key=itemgetter(1))[2]
            
            self.update(best_move)

            return best_move


    
    def placePiece(self):
        """
        Does the actual placing of the pieces. Will either place randomly
        or place next to the enemy in a position where it doesn't get
        eliminated.
        :return: Places a piece on the board, according to existence of enemies
        """
        # Initialising constants to use throughtout the process.
        player      = self.get_symbol('player')
        opponent    = self.get_symbol('opponent')

        # y_threshold here refers to the range of y values for each player in the
        # starting phase
        y_threshold = {"white" : (0,5) , "black" : (2,7)}
        threshold   = y_threshold[self.colour]
        
        
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
        :param threshold: Range of y values for player in the starting phase
        :return: Returns the action of placement (tuple)
        """
        square  = (randint(0,7), randint(threshold[0],threshold[1]))
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
        :param threshold: Range of y values for player in the starting phase
        :param enemy: List of enemy pieces
        :return: Action of placing the piece (tuple).
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
                    piece                       = Piece(player, free_space, self.board)
                    eliminated_pieces           = piece.makemove(free_space)
                    
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
        """
        Expands the current board state by returning a list of possible moves,
        represented by in the form a tuple containing  a board, utility cost and
        the action move.
        :return List of tuples in the form as stated above.
        """

        player = self.get_symbol('player')
        possible_moves = []
        if player == "O":
            for i in self.board.white_pieces:
                # Checks if the piece is alive.
                if i.alive:
                    oldpos = i.pos
                    # Iterate through the possible moves.
                    for j in i.moves():
                        eliminated_pieces   = i.makemove(j)
                        utility             = self.get_utility(i.board)
                        # Check that if the move kills the piece, adds 300 to 
                        # utility cost, pushing it down the order of which
                        # move to pick.
                        if i in eliminated_pieces:
                            utility += 300
                        possible_moves.append((i.board, utility , (oldpos , i.pos) ))
                        i.undomove(oldpos, eliminated_pieces)
        # For the case where the player is black.                
        if player == "@":
            for i in self.board.black_pieces:
                if i.alive:
                    oldpos = i.pos
                    for j in i.moves():
                        eliminated_pieces   = i.makemove(j)
                        utility             = self.get_utility(i.board)
                        if i in eliminated_pieces:
                            utility += 200
                        possible_moves.append((i.board, utility , (oldpos , i.pos) ))
                        i.undomove(oldpos, eliminated_pieces)
                        
        return possible_moves


    def get_utility(self, board):
        """
        Utility function for the algorithm
        Applies manhattan distance from each piece to all opponents piece, and also corner pieces
        and returns the sum
        :param board: board representation
        :return: the sum of manhattan distances, from the player to all enemy pieces, and or to the corner pieces
                dependent on the shrinking
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

