from models.player import Player
# from models.game import Game

player1 = Player("Emily", "Rock")
player2 = Player("Lewis", "Paper")

players = [player1, player2]

def check_winner(player_choice):
    if player_choice == "Rock" and player2.choice == "Scissors":
            return f"{player1.name} Wins"
    elif player_choice == "Scissors" and player2.choice == "Rock":
            return f"{player2.name} Wins"
    elif player_choice == "Scissors" and player2.choice == "Paper":
            return f"{player1.name} Wins"
    elif player_choice == "Paper" and player2.choice == "Scissors":
            return f"{player2.name} Wins"
    elif player_choice == "Paper" and player2.choice == "Rock":
            return f"{player1.name} Wins"
    elif player_choice == "Rock" and player2.choice == "Paper":
            return f"{player2.name} Wins"
    else:
        return "Draw"


print(check_winner("Rock"))
        
        
        
        
        
            
        
        






