from secrets import choice
from models.player import Player
from models.player_list import *

class Game: 
    def __init__(self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2

    def check_winner(self):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            return "Player 1 Wins"
        elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            return "Player 2 Wins"
        else: 
            return None



