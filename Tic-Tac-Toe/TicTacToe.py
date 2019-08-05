import numpy as np 
import random 
from time import sleep 
  
# Creates an empty board 
def create_board(): 
    return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]])) 

# Check which spaces are empty on the board
def empty_spaces(board):
    available = []

    for row in range(len(board)):
        for column in range(len(board)):

            if board[row][column] == 0:
                available.append((row, column))
    
    return(available)

# Choose a random position on the board to place a player token
def random_position(board, player):
    selection = empty_spaces(board)
    determined_location = random.choice(selection)
    board[determined_location] = player
    
    return(board)

# Check to see if a column on the board contains the same player token
def col_win(board, player):
    for row in range(len(board)):
        win = True

        for column in range(len(board)):
            if board[column][row] != player:
                win = False
                continue

        if win == True:
            return(win)

    return(win)

# Check to see if a row on the board contains the same player token
def row_win(board, player):
    for row in range(len(board)):
        win = True

        for column in range(len(board)):
            if board[row, column] != player:
                win = False
                continue
            
        if win == True:
            return(win)
    return(win)