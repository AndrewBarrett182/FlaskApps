from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.74.237:3306/todo" # Set the connection string to connect to a database
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app) # Declare SQLAlchemy object

from application import routes