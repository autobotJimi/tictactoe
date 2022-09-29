rows, cols = (3, 3)
board = [['']*cols]*rows

class Player():
    def __init__(self, name, token) -> None:
        self.name = name
        self.token = token
    

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

print(full_board(board))
print(board)