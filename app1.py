# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.189.67.211:3306/users"

# db = SQLAlchemy(app)

# class users(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     first_name = db.Column(db.String(20), nullable = False)
#     last_name = db.Column(db.String(20), nullable = False)
#     age = db.Column(db.Integer, nullable = False)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.189.67.211:3306/users"

db = SQLAlchemy(app)

class todo_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    todo = db.Column(db.String(50), nullable = False)
    doing = db.Column(db.String(50), nullable = False)
    done = db.Column(db.String(50), nullable = False)

if __name__ == "__main__":
    app.run(debug=True)