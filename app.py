from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Game_feed
games = db.games

app = Flask(__name__)

@app.route('/')
def games_index():
    """Show all games."""
    return render_template('games_index.html', games=games.find())

if __name__ == '__main__':
    app.run(debug=True)