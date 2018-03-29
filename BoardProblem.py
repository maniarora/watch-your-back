from board import Board
import aima
from search import *
from utils import *
import copy

class Problem(object):
    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

class BoardProblem(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial,goal)
        
    def result(self, state,action):

        player = "O"
        opponent = "@"
        empty = '-'
        blocked = 'X'


        row = action[1][0]
        col = action[1][1]
        result = copy.deepcopy(state)

        #Left movement
        if action[0] == "LEFT":
            if col > 0 and state.board[row][col-1] != blocked:
                if col-1 == empty:
                    result =  state.makeMove([row,col],[row,col-1])

                elif col-1 == opponent or state.board[row][col-1] == player:
                    if col > 1 and state.board[row][col-2] == empty:
                        result = state.makeMove([row,col],[row,col-2])

        #Right Movement
        elif action[0] == "RIGHT":
            if col < Board.WIDTH-1 and state.board[row][col+1] != blocked:
                if col+1 == empty:
                    result = state.makeMove([row,col],[row,col+1])
                elif state.board[row][col+1] == opponent or state.board[row][col+1] == player:
                    if col < Board.WIDTH-2 and state.board[row][col+2] == empty:
                        result = state.makeMove([row,col],[row,col+2])

        #Up Movement
        elif action[0] == "UP":
            if row > 0 and state.board[row-1][col] != blocked:
                if state.board[row-1][col] == empty:
                    result = state.makeMove([row,col],[row-1,col])
                elif state.board[row-1][col] == opponent or state.board[row-1][col] == player:
                    if row > 1 and state.board[row-2][col] == empty:
                        result = state.makeMove([row,col],[row-2,col])

        #Down Movement
        elif action[0] == "DOWN":
            if row < Board.HEIGHT-1 and state.board[row+1][col] != blocked:
                if state.board[row+1][col] == empty:
                    result = state.makeMove([row,col], [row + 1, col])
                elif state.board[row+1][col] == opponent or state.board[row+1][col] == player:
                    if row < Board.HEIGHT-2 and state.board[row+2][col] == empty:
                        result = state.makeMove([row,col],[row+2,col])


        #Removes black
        for i in result.getLoc("black"):
            result.isKilled(i,"black")

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


    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1


    def h(self, node):
        print(self.goal)
        x1, y1 = node.state.get_location()
        x2, y2 = self.
        return abs(x2-x1) + abs(y2-y1)

#     def heuristic(a, b):
#         (x1, y1) = a
#         (x2, y2) = b
#         return abs(x2 - x1) + abs(y2 - y1)

