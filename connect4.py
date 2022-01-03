import numpy as np

COLUMN_COUNT = 7
ROW_COUNT = 6

board = np.zeros((ROW_COUNT,COLUMN_COUNT), dtype=int)

class Player ():
    def __init__ (self, name, piece):
        self.name = name
        self.piece = piece

def play_game ():
    p1 = Player(input("Enter player1 name: "), 1)
    p2 = Player(input("Enter player2 name: "), 2)
    print_board()

    while True:
        row = int(input(f"{p1.name}, what row do you want to put your piece? (0-6): "))
        while put_piece(row, p1.piece) == False:
            row = int(input(f"{p1.name}, that row is full or invalid, try again. (0-6): "))
        
        print_board()

        if winning_move(board, p1.piece):
            print(f"{p1.name} wins the game!")
            break

        row = int(input(f"{p2.name}, what row do you want to put your piece? (0-6): "))
        while put_piece(row, p2.piece) == False:
            row = int(input(f"{p2.name}, that row is full or invalid, try again. (0-6): "))
            
        print_board()

        if winning_move(board, p2.piece):
            print(f"{p2.name} wins the game!")
            break

def print_board ():
    string =  "        ROWS       \n"
    string += "0  1  2  3  4  5  6\n"
    string += "--------------------\n"
    for i in range(ROW_COUNT):
        row = ""
        for j in range(COLUMN_COUNT):
            row += str(board[i][j]) + "  "

        string += "{}\n".format(row)

    print()
    print(string)

def winning_move (board, piece):
    for c in range(COLUMN_COUNT-3):
	for r in range(ROW_COUNT):
	    if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
		return True

    for c in range(COLUMN_COUNT):
	for r in range(ROW_COUNT-3):
	    if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
		return True

    for c in range(COLUMN_COUNT-3):
	for r in range(ROW_COUNT-3):
	    if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
		return True

    for c in range(COLUMN_COUNT-3):
	for r in range(3, ROW_COUNT):
	    if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
		return True

def put_piece (column, piece):
    try:
        i = -1
        while board[i][column] != 0:
            i -= 1
        
        board[i][column] = piece
        return True
    except:
        return False

if __name__ == "__main__":
    play_game()
