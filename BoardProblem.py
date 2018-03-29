from board import Board
from search import Problem

class BoardProblem(Problem):
    
    def __init__(self,initial,goal=None):
        super().__init__(initial, goal)
        
    
    def result(self, state,action):
        
        player = "O"
        opponent = "@"
        empty = '-'
        blocked = 'X'
        

        row = action[1][0]
        col = action[1][1]

        #Left movement
        if action[0] == "LEFT":
            if col > 0 and state.board[row][col-1] != blocked:
                if col-1 == empty:
                    return state.makeMove([row,col],[row,col-1])
                        
                elif col-1 == opponent or state.board[row][col-1] == player:
                    if col > 1 and state.board[row][col-2] == empty:
                        return state.makeMove([row,col],[row,col-2])
            
        #Right Movement
        if action[0] == "RIGHT":
            if col < Board.WIDTH-1 and state.board[row][col+1] != blocked:
                if col+1 == empty:
                    return state.makeMove([row,col],[row,col+1])
                elif state.board[row][col+1] == opponent or state.board[row][col+1] == player:
                    if col < Board.WIDTH-2 and state.board[row][col+2] == empty:
                            return state.makeMove([row,col],[row,col+2])

        #Up Movement
        if action[0] == "UP":
            if row > 0 and state.board[row-1][col] != blocked:
                if state.board[row-1][col] == empty:
                    return state.makeMove([row,col],[row-1,col])
                elif state.board[row-1][col] == opponent or state.board[row-1][col] == player:
                    if row > 1 and state.board[row-2][col] == empty:
                        return state.makeMove([row,col],[row-2,col])

        #Down Movement
        if action[0] == "DOWN":
            if row < Board.HEIGHT-1 and state.board[row+1][col] != blocked:
                if state.board[row+1][col] == empty:
                    return state.makeMove([row,col],[row+1,col])

                elif state.board[row+1][col] == opponent or state.board[row+1][col] == player:
                    if row < Board.HEIGHT-2 and state.board[row+2][col] == empty:
                        return state.makeMove([row,col],[row+2,col])
                            
    
    
    def actions(self,state):
        
        whites =  state.getLoc("white")
        
        actions = []
        for i in whites:
            actions.append(["UP",i])
            actions.append(["DOWN",i])
            actions.append(["LEFT",i])
            actions.append(["RIGHT",i])
            
        return actions
            
    def goal_test(self,state):
        if len(state.getLoc("black")) == 0 :
            return True
        else:
           return False

    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x2 - x1) + abs(y2 - y1)

    
            