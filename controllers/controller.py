from flask import render_template
from app import app
from models.player import Player
from models.game import Game

# @app.route("/players")
# def index():
#     return render_template("index.html", players=players)

@app.route("/<player1choice>/<player2choice>")
def check_win(player1choice, player2choice):
    player1 = Player(player1choice)
    player2 = Player(player2choice)
    new_game = Game(player1, player2)
    result = new_game.check_winner()
    return render_template("index.html", result=result)
    




