from board import Board
import search

class BoardProblem(search.Problem):
    
    def __init__(self,initial,goal=None):
        super().__init__(initial, goal)
        
    
    def actions(self, state):
        
        player = "O"
        opponent = "@"
        empty = '-'
        blocked = 'X'
        
        moves = []
        
        for i in state.getLoc("white"):
            row = i[0]
            col = i[1]
            
            #Left movement
            if col > 0 and state.board[row][col-1] != blocked:
                    if col-1 == empty:
                        moves.append(state.makeMove([row,col],[row,col-1]))
                        
                    elif col-1 == opponent or state.board[row][col-1] == player:
                        if col > 1 and state.board[row][col-2] == empty:
                                moves.append(state.makeMove([row,col],[row,col-2]))
            
            #Right Movement
            if col < Board.WIDTH-1 and state.board[row][col+1] != blocked:
                    if col+1 == empty:
                        moves.append(state.makeMove([row,col],[row,col+1]))
                    elif state.board[row][col+1] == opponent or state.board[row][col+1] == player:
                        if col < Board.WIDTH-2 and state.board[row][col+2] == empty:
                                moves.append(state.makeMove([row,col],[row,col+2]))
            
            #Up Movement
            if row > 0 and state.board[row-1][col] != blocked:
                    if state.board[row-1][col] == empty:
                        moves.append(state.makeMove([row,col],[row-1,col]))
                    elif state.board[row-1][col] == opponent or state.board[row-1][col] == player:
                        if row > 1 and state.board[row-2][col] == empty:
                                moves.append(state.makeMove([row,col],[row-2,col]))
                                
            #Down Movement
            if row < Board.HEIGHT-1 and state.board[row+1][col] != blocked:
                    if state.board[row+1][col] == empty:
                        moves.append(state.makeMove([row,col],[row+1,col]))
                    elif state.board[row+1][col] == opponent or state.board[row+1][col] == player:
                        if row < Board.HEIGHT-2 and state.board[row+2][col] == empty:
                                moves.append(state.makeMove([row,col],[row+2,col]))
                                
        return moves
            