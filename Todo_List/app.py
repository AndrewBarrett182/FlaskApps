# from flask import Flask 
# from flask_sqlalchemy import SQLAlchemy 

# app = Flask(__name__) # Declare Flask object

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.74.237:3306/todo" # Set the connection string to connect to a database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# db = SQLAlchemy(app) # Declare SQLAlchemy object

# class Todos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(30), nullable=False)
#     complete = db.Column(db.Boolean, nullable=False)

# @app.route('/')
# def home():
#     return 'THIS IS A TODO LIST'

# @app.route('/todos')
# def todo():
#     return 'THIS IS A TODO LIST'

from application import app

if __name__=='__main__':
    app.run(debug=True)