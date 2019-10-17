from flask import Flask, render_template

app = Flask(__name__)



games = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]
@app.route('/')
def games_index():
    """Show all games."""
    return render_template('games_index.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)