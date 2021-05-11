# from app1 import db, users

# #db.drop_all()
# db.create_all()

# first = input("Input first name: ")
# last = input("Input last name: ")
# age = int(input("Input age: "))

# testuser = users(first_name = first, last_name = last, age = age)
# db.session.add(testuser)
# db.session.commit()

from app1 import db, todo_list

#db.drop_all()
db.create_all()

todo = input("Input task to do: ")
doing = input("Input task currently doing: ")
done = input("Input task done: ")

testlist = todo_list(todo = todo, doing = doing, done = done)
db.session.add(testlist)
db.session.commit()