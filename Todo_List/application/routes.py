from application import app, db
from application.models import Todos

@app.route('/')
def home():
    return 'THIS IS A TODO LIST'

@app.route('/todos')
def todo():
    all_todo = Todos.query.all()
    todo_string = "To do List: "
    for todo in all_todo:
        todo_string += "<br>"+ todo.task + ' ' + str(todo.complete)
    return todo_string