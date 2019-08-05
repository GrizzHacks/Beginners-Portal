import numpy as np 
import random 
from time import sleep 
  
# Creates an empty board 
def create_board(): 
    return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]])) 

def empty_spaces(board):
    available = []

    for row in range(len(board)):
        for column in range(len(board)):

            if board[row][column] == 0:
                available.append((row, column))
    
    return(available)

def random_position(board, player):
    selection = empty_spaces(board)
    determined_location = random.choice(selection)
    board[determined_location] = player
    
    return(board)