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

# Check to see if a diagonal area contains the same player token
def diag_win(board, player):
    win = True

    for tile in range(len(board)):
        if board[tile, tile] != player:
            win = False
    return(win)

# Check if there was a winner and who that winner was
def evaluation(board):
    winner = 0

    for player in [1, 2]:
        if (col_win(board, player) or row_win(board, player) or diag_win(board, player)):
            winner = player
        
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# Main function to start gameplay
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = random_position(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluation(board)
            if winner != 0:
                break
    return(winner)

# Runs the entire program
print("Winner is: " + str(play_game()))