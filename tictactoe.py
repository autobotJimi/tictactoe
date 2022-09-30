"""

Jimi was here

"""
rows, cols = (3, 3)
board = [['']*cols]*rows

def board_layout(*args):
    board_dict = {"rows":{1:("_","_","_"),
                          2:("_","_","_"),
                          3:("_","_","_")}}

    #--First Row
    print(board_dict["rows"][1][0] + "|" + board_dict["rows"][1][1] + "|" + board_dict["rows"][1][2])
    #--Second Row
    print(board_dict["rows"][2][0] + "|" + board_dict["rows"][2][1] + "|" + board_dict["rows"][2][2])
    #--Third Row
    print(board_dict["rows"][3][0] + "|" + board_dict["rows"][3][1] + "|" + board_dict["rows"][3][2])


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