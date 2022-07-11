import random
from models.player import Player

class Game():

    def __init__(self):
        self.selections = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

    def play(self, player_1, player_2):

        winner = None

        if self.selections[player_1.choice.lower()] == player_2.choice.lower():
            winner = player_1
        elif self.selections[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2

        return winner 


    def generate_computer_player(self):
        all_moves = list(self.selections.keys())
        computer_hand = random.choice(all_moves)
        computer = Player("Computer", computer_hand)
        print(all_moves)
        return computer

