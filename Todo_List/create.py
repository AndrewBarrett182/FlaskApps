# from app import db, Todos

# db.drop_all()
# db.create_all() # Creates all table classes defined

# new_todo = Todos(task = 'eat food', complete = False)
# db.session.add(new_todo)
# db.session.commit()

from application import db

db.drop_all()
db.create_all()