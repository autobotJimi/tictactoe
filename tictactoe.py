rows, cols = (3, 3)

board={"rows":{1:{"_","_","_"},
               2:{"_","_","_"},
               3:{"_","_","_"}}}

class Player():
    def __init__(self, name, token):
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


def intro():
    p1_name = input("Player 1 Name: ")
    p1_token = input("Player 1 Token: ")
    player_1 = Player(p1_name, p1_token)
    p2_name = input("Player 2 Name: ")
    p2_token = input("Player 2 Token: ")
    player_2 = Player(p2_name, p2_token)
    