from application import app, db
from application.models import Todos, AddForm
from flask import render_template, request, redirect, url_for

@app.route('/', methods = ['GET', 'POST'])
@app.route('/todos', methods = ['GET', 'POST'])
def todo():
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
                return redirect(url_for("todo"))

    return render_template('add.html', form=form, message=error)

@app.route('/complete/<id>', methods = ['GET', 'POST'])
def complete(id):
    to_do = Todos.query.filter_by(id=id).first()
    to_do.complete = True
    db.session.commit()
    return redirect(url_for("todo"))

@app.route('/incomplete/<id>', methods = ['GET', 'POST'])
def incomplete(id):
    to_do = Todos.query.filter_by(id=id).first()
    to_do.complete = False
    db.session.commit()
    return redirect(url_for("todo"))

@app.route('/delete/<id>', methods = ['GET', 'POST'])
def delete(id):
    to_do = Todos.query.filter_by(id=id).first()
    db.session.delete(to_do)
    db.session.commit()
    return redirect(url_for("todo"))

@app.route('/update/<id>', methods = ['GET', 'POST'])
def update(id):

    error = ''
    form = AddForm()

    if request.method == 'POST':
        task = form.task.data
        update = form.update.data

        if update == True:
            if len(task) == 0:
                error = "Please enter a task"
            else:
                to_do = Todos.query.filter_by(id=id).first()
                to_do.task = task
                db.session.commit()
                return redirect(url_for("todo"))

    return render_template('update.html', form=form, message=error)

@app.route('/order', methods = ['GET', 'POST'])
def order():
    form = AddForm()
    all_todo = Todos.query.all()

    if request.method == 'POST':
        order = form.order.data
        submit = form.submit_order.data
        if submit == True:
            if order == "Oldest":
                to_do = Todos.query.order_by(Todos.id).all()
                
                return render_template('index.html', form = form, all_todo = to_do)
            elif order == "Newest":
                to_do = Todos.query.order_by(Todos.id.desc()).all()
                
                return render_template('index.html', form = form, all_todo = to_do)
            elif order == "Completed":
                to_do = Todos.query.order_by(Todos.complete.desc()).all()
                
                return render_template('index.html', form = form, all_todo = to_do)
            elif order == "Not Completed":
                to_do = Todos.query.order_by(Todos.complete).all()
                
                return render_template('index.html', form = form, all_todo = to_do)

    return render_template('index.html', form = form, all_todo = all_todo)
