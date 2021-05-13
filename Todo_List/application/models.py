from wtforms.fields.core import BooleanField, SelectField
from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False)
    complete = db.Column(db.Boolean, default=False)

class AddForm(FlaskForm):
    task = StringField('Task')
    submit_task = SubmitField('Add Task')
    complete = SubmitField('Complete Task')
    incomplete = SubmitField('Incomplete Task')
    delete = SubmitField('Delete Task')
    update = SubmitField('Update Task')
    order = SelectField('Sort by', choices = [("Oldest", "Oldest"), ("Newest", "Newest"), ("Completed", "Completed"), ("Not Completed", "Not Completed")])
    submit_order = SubmitField('Submit')