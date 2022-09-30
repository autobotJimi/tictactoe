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

   
    def move(x, y, player):
        if board['rows'][y][x] == "_":
            board['rows'][y][x] = player.token

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

    def player_move():
        position = input("What's your next move? ")
        position = position.split(' ')
        x = row[position[0]]
        y = col[position[1]]
        return x, y
    print(player_move())


# --- beginginng of the actual game
p1_name = input("Player 1 Name: ")
p1_token = input("Player 1 Token: ")
player_1 = Player(p1_name, p1_token)
p2_name = input("Player 2 Name: ")
p2_token = input("Player 2 Token: ")
player_2 = Player(p2_name, p2_token)
this_game = Game((player_1, player_2))
gaming = True

while gaming:
    row = {
    'top': 1, 
    'middle': 2, 
    'bottom': 3
    }
col = {
    'left': 1, 
    'middle': 2, 
    'right': 3}
    active_player = this_game.players()
    print(f"{active_player}'s turn!")
    

