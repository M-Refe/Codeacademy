#create the game, battleship!
#set up the game board
board = []
#use python function to generate board| make into a 5x5 grid of all O's for ocean
    #create 5x5 grid initialized to all 'O's and store into board.
        #use range() to loop 5 times
        #inside loop, append() a list containing 5 "O"s to the board
        #these are captial O and not zeros
#solution
board = []
for i in range(5):
  board.append(['O'] * 5)
print (board)

#my code attempt 1:
board = []
for n in range(0, 5):
    board.append("O") * 5
print (n)
#my code attempt 2:
board = []
for i in board:
  range(5)
  board.append("O") * 5
print (board)

#to print board like a grid with each row on it's own line
#solution
board = []
for i in range(5):
  board.append(['O']*5)

def print_board(board_in):
  for row in board:
    print (row)

print_board(board)

#my code attempt 1:
board = []
for i in range(5):
  board.append(['O']*5)

def print_board(board_in):
  for row in board:
    print (board)

#to store data as a list for a playable board
#use print " ".join(row)
board = []
for i in range(5):
  board.append(['O']*5)

def print_board(board_in):
  for row in board:
    print "_".join(row)

print_board(board)

#now to hide battleship in a random location on the board
#two variables to store the ship's location, ship_row and ship_col
#create random_row and random_col
#given
from random import randint 
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

# Add your code below!
def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

#with instructions, i got the code correctly, it was given. 

#store coordinates for the ship in the variables, and write code to allow the player to guess where the battle ship is.
#given
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Add your code below!
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

#it was easy because the instructions gave it to me again
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")

#if the guess is incorrect, need to do something else
#add else under the if, print statement "You missed my battleship!", and set the list element at guess_row, guess_col to "x"
#and as the last line in else statement, print_board(board) again to see the "X", make sure to enter a col and row that is one the board
#my code attempt 1
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")
else: 
    print ("You missed my battleship!")
    guess_row = "X" 
    guess_col = "X" 
    return (print_board(board))

#solution
if guess_row == ship_row and guess_col == ship_col:
  print ("Congratulations! You sank my battleship!")  
else:
  print ("You missed my battleship!")
  board[guess_row][guess_col] = "X"
  print_board(board)

#need to clarify the "miss" condition more. 
#guess on the board, can't guess that's already guess, and can't miss the ship

