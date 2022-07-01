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
#my code attempt 2"
board = []
for i in board:
  range(5)
  board.append("O") * 5
print (board)