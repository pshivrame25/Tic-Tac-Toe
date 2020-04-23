
import os 
import random 

#Initial display definition for the grid

def display_board(board):
	print("   |     |  ")
	print(" " + board[7] + " | "+ board[8] +"   | "+board[9])
	print('   |     |')
	print("-----------------")
	print('   |     |')
	print(" " + board[4] + " | "+ board[5] +"   | "+board[6])
	print('   |     |')
	print("-----------------")
	print('   |     |')
	print(" " + board[1] + " | "+ board[2] +"   | "+board[3])
	print('   |     |')
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

#take input from player 
def player_input():
	marker=""
	while not(marker=="X" or marker=="O"):
		marker=input("P1: Select Tic or Tac ?")
	if marker=="X":
		return("X","O") #tuple unpacking 
	else:
		return("O","X")

#take the position and print the input 
def place_holder(board,marker,position):
	board[position]=marker 

#place_holder(test_board,"P",7)
#display_board(test_board)


#check for WIN- Static method
def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    	(board[4]==mark and board[5]==mark and board[6]==mark)or
    	(board[1]==mark and board[2]==mark and board[3]==mark)or
    	(board[7]==mark and board[4]==mark and board[1]==mark)or
    	(board[8]==mark and board[5]==mark and board[2]==mark)or
    	(board[9]==mark and board[6]==mark and board[3]==mark)or
    	(board[7]==mark and board[5]==mark and board[3]==mark)or
    	(board[9]==mark and board[5]==mark and board[1]==mark) )


#win_check(test_board,"X")

def select_player():
	if random.randint(0,1) == 0:
		return "P1"
	else:
		return "P2"



#check for free space on the board

def free_space(board,position):
	return board[position] == ' '

def board_check(board):
	for i in range(1,10):
		if free_space(board,i):
			return False 
	return True

#Check for valid board entries 
def entry(board):
	position=0

	while position not in [1,2,3,4,5,6,7,8,9] or not free_space(board,position):
			position = int (input("Enter your next position")) 
	return position

def replay():
    return input('Do you want to play again? Enter Y/N ')

print( "")

while True: 
	big_board=[" "]*10
	p1_marker,p2_marker = player_input()
	print(p1_marker,p2_marker)
	turn = select_player()
	print(turn + " will play first")

	
	while True:
		if turn == "P1":
			display_board(big_board)
			print("player 1 plays")
			position = entry(big_board)
			place_holder(big_board,p1_marker,position)

			if win_check(big_board,p1_marker):
				display_board(big_board)
				print("WIN P1")
				break
			else:
				if (board_check(big_board)):
					display_board(big_board)
					print("Draw")
					break
				else:
					turn = "P2"
		else:
			display_board(big_board)
			print("player 2 plays")
			position = entry(big_board)
			place_holder(big_board,p2_marker,position)


			if win_check(big_board,p2_marker):
				display_board(big_board)
				print("WIN P2")
				break 
			else:
				if board_check(big_board):
					display_board(big_board)
					print("Draw")
					break
				else:
					turn = "P1"
	if not replay():
		break










