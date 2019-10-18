from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

#MONGO INFO

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/gamefeed')
client = MongoClient(host=host)
db = client.get_default_database()
games = db.games

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def games_index():
    """Show all games."""
    game_items = games.find()
    return render_template('games_index.html', game_items=game_items)

@app.route('/game/<game_id>')
def games_show(game_id):
    """Show a single game."""
    game = games.find_one({'_id': ObjectId(game_id)})
    return render_template('game_item.html', game=game)

@app.route('/games/new')
def games_new():
    """Create a new game."""
    return render_template('games_new.html')

@app.route('/games', methods=['POST'])
def games_submit():
    """Submit a new game."""
    added_game = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'url': request.form.get('url')
    }
    print(added_game)
    games.insert_one(added_game)
    return redirect(url_for('games_index'))

@app.route('/game/<game_id>/edit')
def games_edit(game_id):
    """Show the edit form for a game listing."""
    game = games.find_one({'_id': ObjectId(game_id)})
    return render_template('game_edit.html', game=game)

@app.route('/game/<game_id>/delete', methods=['POST'])
def games_delete(game_id):
    """Delete one game."""
    games.delete_one({'_id': ObjectId(game_id)})
    return redirect(url_for('games_index'))

@app.route('/game/<game_id>', methods=['POST'])
def games_update(game_id):
    """Submit an edited game log."""
    updated_game = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
    }
    games.update_one(
        {'_id': ObjectId(game_id)},
        {'$set': updated_game})
    return redirect(url_for('games_update', game_id=game_id))

@app.route('/create')
def create_user():
    return render_template('create_user.html')

@app.route('/create/<account>', methods=['POST'])
def add_user():
    return redirect(url_for('games.index'))
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))