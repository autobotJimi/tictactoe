from random import randint, choice
from time import sleep
import os

rows, cols = (3, 3)
board = {"rows":{1:["_","_","_"],
                 2:["_","_","_"],
                 3:["_","_","_"]}}
row_words = {
    'top': 1, 
    'middle': 2, 
    'bottom': 3}
col_words = {
    'left': 1, 
    'middle': 2, 
    'right': 3}


class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token
    # the player
    

class Game():
    def __init__(self, players):
        self.players = players
        self.turn = randint(0, len(self.players)-1)
    
    def __repr__(self) -> str:
        print(" 1 | 2 | 3 |")
        print(" 1 " + str(board['rows'][1]))
        print(" 2 " + str(board['rows'][2]))
        print(" 3 " + str(board['rows'][3]))
    
    def is_full(board):
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

    def move(self, x, y, player):
        print(f"X = {x}")
        print(f"Y = {y}")
        initial_token = board['rows'][y][x-1]
        if board['rows'][y][x-1] == "_":
            board['rows'][y][x-1] = player.token
        return initial_token

    def winning_combination(self): # board['rows'][row (1, 3)][col (0, 2)]
        symbol_1 = self.players[0]
        symbol_2 = self.players[1]
        winner = False
        #rows
        for row in range(1, 3):
            if (board['rows'][row][0] == board['rows'][row][1] == board['rows'][row][2] == symbol_1):
                winner = True
                print(f"{self.players[0]}, you won!")
            elif (board['rows'][row][0] == board['rows'][row][1] == board['rows'][row][2] == symbol_2):
                winner = True
                print(f"{self.players[1]}, you won!")
        #columns
        for col in range(0, 2):
            if (board['rows'][1][col] == board['rows'][2][col] == board['rows'][3][col] == symbol_1):
                winner = True
                print(f"{self.players[0]}, you won!")
            elif (board['rows'][1][col] == board['rows'][2][col] == board['rows'][3][col] == symbol_2):
                winner = True
                print(f"{self.players[1]}, you won!")
        # diagnoals
        if board['rows'][1][0] == board['rows'][2][1] == board['rows'][3][2] == symbol_1: # (1, 1) (2, 2) (3, 1)
            winner = True 
            print(f"{self.players[0]}, you won!")
        elif board['rows'][1][0] == board['rows'][2][1] == board['rows'][3][2] == symbol_2:
            winner = True
            print(f"{self.players[1]}, you won!")
        elif board['rows'][1][2] == board['rows'][2][1] == board['rows'][3][0] == symbol_1: # (1, 3) (2, 2) (3, 1)
            winner = True
            print(f"{self.players[0]}, you won!")
        elif board['rows'][1][2] == board['rows'][2][1] == board['rows'][3][0] == symbol_2:
            winner = True
            print(f"{self.players[1]}, you won!")
        return winner

def player_move():
    used_words = False
    position = input("What's your next move?\n(examples: \"12\" or \"top, middle\") ")
    try:
        position = int(position) # they used numbers
        position = str(position)
        position = (position[0], position[1])
    except ValueError:
        used_words = True # they used words
        position = (position[:position.find(",")], position[position.find(",")+2:])
        position = (col_words[position[1]], row_words[position[0]])
    finally:
        x = int(position[0])
        y = int(position[1])
        coords_tup = (x, y)
        return coords_tup


# --- beginginng of the actual game
p1_name = input("Player 1 Name: ")
p1_token = input("Player 1 Token: ")
player_1 = Player(p1_name, p1_token)
p2_name = input("Player 2 Name: ")
p2_token = input("Player 2 Token: ")
player_2 = Player(p2_name, p2_token)
this_game = Game((player_1, player_2))
this_player = choice(this_game.players)
gaming = True
change_turn = False

while gaming:
    if this_game.winning_combination() == True:
        gaming = False

    # clear screen
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    # draw board
    this_game.__repr__()

    if not change_turn:
        print(f"{this_player.name}'s turn!")
        this_move = player_move() # asks user, returns coords
        if this_game.move(this_move[0], this_move[1], this_player) == "_": # spot was not taken
            change_turn = True
            print("Moved successfully.")
        else: # spot was taken
            print("That spot was already taken, so it's still...")
        sleep(1)
    else: # changing turn
        if this_player == this_game.players[0]:
            this_player = this_game.players[1]
        else:
            this_player = this_game.players[0]
        change_turn = False

