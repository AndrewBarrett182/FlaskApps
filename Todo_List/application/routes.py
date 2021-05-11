from application import app, db
from application.models import Todos

@app.route('/')
def home():
    return 'THIS IS A TODO LIST'

@app.route('/todos')
def todo():
    all_todo = Todos.query.all()
    todo_string = "<h1>To do List: </h1>"
    for todo in all_todo:
        todo_string += f"{todo.task} = {str(todo.complete)} <br><br>"
    return todo_string