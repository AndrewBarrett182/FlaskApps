from application import app, db
from application.models import Todos
from flask import render_template

@app.route('/')
@app.route('/todos')
def todo():
    return render_template('index.html', all_todo = Todos.query.all())

@app.route('/add')
def add():
    new_todo = Todos(task="New Todo")
    db.session.add(new_todo)
    db.session.commit()
    return "Added new todo to database"

@app.route('/complete/<id>')
def update(id):
    to_do = Todos.query.filter_by(id=id).first()
    to_do.complete = True
    db.session.commit()
    return f"Completed todo {id}"

@app.route('/delete/<id>')
def delete(id):
    to_do = Todos.query.filter_by(id=id).first()
    db.session.delete(to_do)
    db.session.commit()
    return f"Deleted: {to_do.task} from database."