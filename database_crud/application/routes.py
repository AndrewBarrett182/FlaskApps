from application import app, db
from application.models import Games

@app.route('/')
def home():
    string = "<title>CRUD Database</title><a href=http://localhost:5000/add>Add</a><br><br> <a href=http://localhost:5000/read>Read</a><br><br> <a href=http://localhost:5000/update>Update (add /name to change)</a><br><br> <a href=http://localhost:5000/delete>Delete</a><br><br> <a href=http://localhost:5000/count>Count</a><br><br>"
    return string

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete')
def delete():
    game_to_delete = Games.query.first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return f"Deleted: {game_to_delete.name} from database."

@app.route('/count')
def count():
    number_of_games = Games.query.count()
    return f"Number of games = {number_of_games}"