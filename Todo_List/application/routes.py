from application import app, db
from application.models import Todos, AddForm
from flask import render_template, request

@app.route('/', methods = ['GET', 'POST'])
@app.route('/todos', methods = ['GET', 'POST'])
def todo():
    error = ''
    form = AddForm()
    all_todo = Todos.query.all()

    return render_template('index.html', form = form, all_todo = all_todo)

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ''
    form = AddForm()

    if request.method == 'POST':
        task = form.task.data
        submit_task = form.submit_task.data

        if submit_task == True:
            if len(task) == 0:
                error = "Please enter a task"
            else:
                new_todo = Todos(task=task)
                db.session.add(new_todo)
                db.session.commit()
                return f"Added {task} to the to do list!"

    return render_template('add.html', form=form, message=error)

@app.route('/complete/<id>', methods = ['GET', 'POST'])
def complete(id):
    error = ''
    form = AddForm()
    all_todo = Todos.query.all()
    to_do = Todos.query.filter_by(id=id).first()
    to_do.complete = True
    db.session.commit()
    return render_template('index.html', form = form, all_todo = all_todo)

@app.route('/incomplete/<id>', methods = ['GET', 'POST'])
def incomplete(id):
    error = ''
    form = AddForm()
    all_todo = Todos.query.all()
    to_do = Todos.query.filter_by(id=id).first()
    to_do.complete = False
    db.session.commit()
    return render_template('index.html', form = form, all_todo = all_todo)

@app.route('/delete/<id>')
def delete(id):
    to_do = Todos.query.filter_by(id=id).first()
    db.session.delete(to_do)
    db.session.commit()
    return f"Deleted: {to_do.task} from database."