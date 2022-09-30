from random import randint

rows, cols = (3, 3)
board = {"rows":{1:["_","_","_"],
                 2:["_","_","_"],
                 3:["_","_","_"]}}

class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token
    # the player
    

class Game():
    def __init__(self, players):
        self.players = players
        self.turn = randint(0, len(self.players-1))
    
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

    def calc_winner(): # row, col
        winning_combinations = [[(1, 1), (1, 2), (1, 3)],
                                [(2, 1), (2, 2), (2, 3)], 
                                [(3, 1), (3, 2), (3, 3)], 
                                [(1, 1), (2, 1), (3, 1)],
                                [(1, 2), (2, 2), (3, 2)],
                                [(1, 3), (2, 3), (3, 3)],
                                [(1, 1), (2, 2), (3, 3)],
                                [(3, 1), (2, 2), (1, 3)]]
    
    def move(x, y, player):
        if board['rows'][y][x] == "_":
            board['rows'][y][x] = player.token



p1_name = input("Player 1 Name: ")
p1_token = input("Player 1 Token: ")
player_1 = Player(p1_name, p1_token)
p2_name = input("Player 2 Name: ")
p2_token = input("Player 2 Token: ")
player_2 = Player(p2_name, p2_token)
this_game = Game((player_1, player_2))
gaming = True

while gaming:
    active_player = this_game.players()
    print(f"'s turn!")