from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Game_feed
games = db.games

app = Flask(__name__, static_url_path='/static')

'''games.insert_many([
    {'title': 'skyrim', 'description': 'description : fun ass game'},
    {'title': 'yeah', 'description': 'description : fun-ish game'}
])'''


@app.route('/')
def games_index():
    """Show all games."""
    game_item = games.find()
    return render_template('games_index.html', game_item=game_item)

@app.route('/chip/<chips_id>')
def chips_show(chips_id):
    """Show a single playlist."""
    chip = chips.find_one({'_id': ObjectId(chips_id)})
    return render_template('chip_item.html', chip=chip)

@app.route('/games/new')
def chips_new():
    """Create a new game listing."""
    return render_template('game_new.html')

if __name__ == '__main__':
    app.run(debug=True)