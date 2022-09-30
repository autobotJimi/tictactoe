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