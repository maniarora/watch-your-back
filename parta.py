'''
Subject     : COMP30024
Project     : Watch Your Back (Part A)
Authors     : Manindra Arora    (827703)
            : Weng Kin Lee      (822386)
Last Edited : 30th March 2018
'''


from board import Board
import getMoves
import math
import copy

MOVES       = 'Moves'
MASSACRE    = 'Massacre'

# Driver program
# def main():

# Create an instance of the board,and populate it from input
board = Board()

board.populate_board_from_input()

# Check which run mode is desired
mode = input()


if(mode == MOVES):
    print(getMoves.moves(board, 'white'))
    print(getMoves.moves(board, 'black'))

elif(mode == MASSACRE):

    final =  board.massacre()

    for i in final.move_history:
        print("(%d, %d) -> (%d, %d)" % (i[0][1],i[0][0],i[1][1],i[1][0]))


