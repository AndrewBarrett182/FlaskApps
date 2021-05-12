from wtforms.fields.core import BooleanField
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