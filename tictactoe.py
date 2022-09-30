rows, cols = (3, 3)
board = [['']*cols]*rows

class Player():
    def __init__(self, name, token) -> None:
        self.name = name
        self.token = token
    # the player
    

def full_board(board):
    squares_filled = 0
    for square in board:
        if len(square) == 0:
            pass
        elif len(square) > 0:
            squares_filled += 1
    if squares_filled == 9:
        return True
    else:
        return False
#
print(full_board(board))
print(board)

winning_combinations = {[row = 1: cols = 1, row = 1: cols = 2, row = 1, cols = 3], 
                        [row = 2 : cols = 1, row = 2 : cols = 1, row = 2, cols = 3], 
                        [row = 3 : cols = 1, row = 3 : cols = 2, row = 3 : cols = 3], 
                        [row = 1 : col = 1, row = 2 : cols = 1, row = 3 : col = 1],
                        [row = 1 : col = 2, row = 2 : cols = 2, row = 3 : col = 2],
                        [row = 1 : col = 3, row = 2 : cols = 3, row = 3 : col = 3],
                        [row = 1 : col = 1, row = 2 : cols = 2, row = 3 : col = 3],
                        [row = 3 : col = 1, row = 2 : cols = 2, row = 1 : col = 3]
                        }

row = {
    'top': 0, 
    'middle': 1, 
    'bottom': 2
    }
col = {
    'left': 0, 
    'middle': 1, 
    'right': 2}


def player_move():
    position = input("What's your next move? ")
    position = position.split(' ')
    x = row[position[0]]
    y = col[position[1]]
    return x, y
print(player_move())



def winning_combination(board, symbol_1, symbol_2):
    winner = True
    #rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")   
    #columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
    # diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")
    return winner


