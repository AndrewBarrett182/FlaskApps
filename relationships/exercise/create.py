from app import db, Customers, Products, Purchases
db.drop_all()
db.create_all() # Creates all table classes defined