from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.intense
games = db.games

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def games_index():
    """Show all games."""
    game_items = games.find()
    return render_template('games_index.html', game_items=game_items)

@app.route('/game/<game_id>')
def games_show(game_id):
    """Show a single playlist."""
    game = games.find_one({'_id': ObjectId(game_id)})
    return render_template('game_item.html', game=game)

@app.route('/games/new')
def games_new():
    """Create a new chip."""
    return render_template('games_new.html')

@app.route('/games', methods=['POST'])
def games_submit():
    """Submit a new playlist."""
    added_game = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'url': request.form.get('url')
    }
    print(added_game)
    games.insert_one(added_game)
    return redirect(url_for('games_index'))


if __name__ == '__main__':
    app.run(debug=True)